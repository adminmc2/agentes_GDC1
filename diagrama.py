#!/usr/bin/env python3
"""Diagrama de procesos del proyecto - Guía Didáctica del Profesor.

Genera diagramas Mermaid desde el estado real del proyecto.
Uso: python3 diagrama.py -> http://127.0.0.1:8081
"""

import datetime
import http.server
import json
import hashlib
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import uuid
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
load_dotenv()

PROJECT = Path(__file__).parent
PORT = 8081


# === Paleta del proyecto (MD3 oliva-crema, coherente con web/index.html) ===
# Tokens duplicados de :root en web/index.html para usarlos en los mermaids.
PAL = {
    "primary":          "#7D7432",  # oliva
    "primary_dark":     "#6E6528",
    "primary_light":    "#B5A84C",
    "on_primary":       "#FFFFFF",
    "primary_container":"#F5F0D0",  # crema claro (fondo de tarjeta)
    "on_primary_container": "#3A3510",
    "surface":          "#FFFDF6",
    "surface_variant":  "#F5F0DC",
    "on_surface":       "#1C1B17",
    "on_surface_variant":"#5E5C52",
    "outline":          "#DDD9C8",
    "outline_variant":  "#EDEADF",
    "success":          "#2E7D32",
    "error":            "#C62828",
    "warning":          "#E65100",
}

# Paleta extendida "cat-tag" (chips/etiquetas del dashboard, web/index.html L156-163).
# Cada tono = (fondo, texto, borde). 8 tonos pastel suaves con texto oscuro y borde
# semitransparente — para diferenciar tipos de nodo de forma legible y no chillona.
CHIPS = {
    "azul":      ("#E3F2FD", "#1A4F7A", "#BBDEFB"),
    "verde":     ("#E8F5E9", "#2E5A33", "#C8E6C9"),
    "amarillo":  ("#FFF8E1", "#7A5D00", "#FFECB3"),
    "rosa":      ("#FCE4EC", "#7A2148", "#F8BBD0"),
    "lila":      ("#F3E5F5", "#5A3170", "#E1BEE7"),
    "melocoton": ("#FFF3E0", "#7A3F12", "#FFE0B2"),
    "menta":     ("#E0F2F1", "#1F5751", "#B2DFDB"),
    "gris":      ("#ECEFF1", "#455A64", "#CFD8DC"),
}


def _chip_style(tone):
    """Devuelve directiva de estilo Mermaid para un nodo con tono chip dado.

    El radio (rx/ry) refuerza el aspecto pill aunque el nodo ya use shape
    redondeado en la sintaxis (`("...")`).
    """
    bg, fg, br = CHIPS[tone]
    return f"fill:{bg},color:{fg},stroke:{br},stroke-width:1px,rx:10,ry:10"


# === Auto-discovery del filesystem (se ejecuta en cada hit a /api/diagrams) ===

def discover_fases():
    """Devuelve [(numero, nombre_slug, path)] de las carpetas reales en fases/.

    Solo incluye carpetas con patrón `<N>-<nombre>`. Ordenadas por número.
    """
    fases = []
    base = PROJECT / "fases"
    if not base.exists():
        return fases
    for p in base.iterdir():
        if not p.is_dir():
            continue
        m = re.match(r"^(\d+)-(.+)$", p.name)
        if not m:
            continue
        fases.append((int(m.group(1)), m.group(2), p))
    fases.sort(key=lambda x: x[0])
    return fases


def discover_registries():
    """Lista de archivos canónicos en fases/1-extraccion-inventario/.

    Cubre tanto `*-canonicos.json` (plural) como `*-canonica.json` (singular).
    """
    base = PROJECT / "fases" / "1-extraccion-inventario"
    if not base.exists():
        return []
    names = set()
    for pat in ("*-canonicos.json", "*-canonica.json"):
        for p in base.glob(pat):
            names.add(p.name)
    return sorted(names)


def discover_scripts():
    """Lista de scripts ejecutables en scripts/."""
    base = PROJECT / "scripts"
    if not base.exists():
        return []
    return sorted([p.name for p in base.glob("*.py") if not p.name.startswith("_")])


def discover_inventarios():
    """Devuelve {numero: path} para inventarios UX-nc1-inventario.json existentes."""
    out = {}
    base = PROJECT / "unidades"
    if not base.exists():
        return out
    for p in base.iterdir():
        m = re.match(r"^U(\d+)$", p.name)
        if not m:
            continue
        inv = p / f"{p.name}-nc1-inventario.json"
        if inv.exists():
            out[int(m.group(1))] = inv
    return out

def _read_version():
    """Lee la versión más reciente del CHANGELOG.md. Siempre actualizado sin intervención manual."""
    try:
        for line in (PROJECT / "CHANGELOG.md").read_text(encoding="utf-8").splitlines():
            if line.startswith("## [v"):
                m = re.search(r'\[v([\d.]+)', line)
                if m:
                    return m.group(1)
    except Exception:
        pass
    return "unknown"

SERVER_VERSION = _read_version()

# --- Langfuse client (para API de trazas) ---
# Requiere langfuse 2.x (litellm 1.82.2 no es compatible con langfuse 3.x/4.x).
_langfuse_client = None
if os.environ.get("LANGFUSE_PUBLIC_KEY"):
    try:
        from langfuse import Langfuse
        _langfuse_client = Langfuse()
        print("[Langfuse] API de trazas disponible")
    except Exception as e:
        print(f"[Langfuse] No disponible: {e}")
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "",
)


def _db():
    return psycopg2.connect(DATABASE_URL)


def get_tarjetas(unidad):
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT t.id, t.palabra, t.genero, t.color_genero, t.silaba_tonica,
               t.regla, t.campo_semantico, t.color_campo, t.ejemplo,
               t.frecuencia, t.combos,
               t.trad_it, t.trad_fr, t.trad_pt_br, t.trad_en,
               t.trad_cs, t.trad_pl, t.trad_tr,
               t.seccion, t.pagina, t.nivel_jerarquia, t.estado, t.unidad_origen,
               t.estado_revision
        FROM tarjetas_vocabulario t
        JOIN unidades u ON t.unidad_id = u.id
        WHERE u.numero = %s
        ORDER BY t.nivel_jerarquia, t.campo_semantico, t.palabra
    """, (unidad,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def get_correcciones(unidad=None):
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    if unidad:
        cur.execute("""
            SELECT id, agente, unidad, palabra, campo, valor_original,
                   valor_corregido, tipo_error, fecha
            FROM correcciones WHERE unidad = %s ORDER BY fecha DESC
        """, (unidad,))
    else:
        cur.execute("""
            SELECT id, agente, unidad, palabra, campo, valor_original,
                   valor_corregido, tipo_error, fecha
            FROM correcciones ORDER BY fecha DESC LIMIT 100
        """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def insert_correccion(data):
    conn = _db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO correcciones (agente, unidad, palabra, campo,
                                  valor_original, valor_corregido, tipo_error)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (
        data.get("agente", "recurso_vocabulario"),
        data["unidad"],
        data["palabra"],
        data["campo"],
        data["valor_original"],
        data["valor_corregido"],
        data["tipo_error"],
    ))
    new_id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return new_id


def get_reglas(crew="recurvo"):
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT id, crew, tipo_error, regla, ejemplos, n_correcciones, activa,
               created_at, updated_at
        FROM reglas_aprendidas
        WHERE crew = %s
        ORDER BY activa DESC, n_correcciones DESC
    """, (crew,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def upsert_regla(data):
    conn = _db()
    cur = conn.cursor()
    regla_id = data.get("id")
    if regla_id:
        cur.execute("""
            UPDATE reglas_aprendidas
            SET tipo_error = %s, regla = %s, ejemplos = %s,
                n_correcciones = %s, activa = %s, updated_at = NOW()
            WHERE id = %s RETURNING id
        """, (
            data["tipo_error"], data["regla"], data.get("ejemplos", ""),
            data.get("n_correcciones", 0), data.get("activa", True), regla_id
        ))
    else:
        cur.execute("""
            INSERT INTO reglas_aprendidas (crew, tipo_error, regla, ejemplos, n_correcciones, activa)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
        """, (
            data.get("crew", "recurvo"), data["tipo_error"], data["regla"],
            data.get("ejemplos", ""), data.get("n_correcciones", 0),
            data.get("activa", True)
        ))
    regla_id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return regla_id


def delete_regla(regla_id):
    conn = _db()
    cur = conn.cursor()
    cur.execute("DELETE FROM reglas_aprendidas WHERE id = %s", (regla_id,))
    conn.commit()
    conn.close()


def get_correcciones_stats(unidad=None):
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    if unidad:
        cur.execute("""
            SELECT tipo_error, COUNT(*) as total,
                   array_agg(DISTINCT palabra) as palabras
            FROM correcciones WHERE unidad = %s
            GROUP BY tipo_error ORDER BY total DESC
        """, (unidad,))
    else:
        cur.execute("""
            SELECT tipo_error, COUNT(*) as total,
                   array_agg(DISTINCT palabra) as palabras
            FROM correcciones
            GROUP BY tipo_error ORDER BY total DESC
        """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def delete_tarjeta(tarjeta_id):
    conn = _db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tarjetas_vocabulario WHERE id = %s", (tarjeta_id,))
    conn.commit()
    conn.close()


def _scan_zona(base, pattern_carpeta, pattern_archivo, zona):
    """Escanea una zona (viejo/nuevo) buscando inventarios."""
    out = []
    if not base.exists():
        return out
    for d in sorted(base.iterdir()):
        if not d.is_dir() or not d.name.startswith("U"):
            continue
        # archivo puede ser inventario.json (viejo) o U3-nc1-inventario.json (nuevo)
        candidates = list(d.glob("*inventario.json"))
        if not candidates:
            continue
        f = candidates[0]
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            try:
                archivo = str(f.relative_to(PROJECT))
            except ValueError:
                # Path fuera de PROJECT (caso típico: worktree paralelo
                # via EXTRA_UNIDADES_PATHS). Usar absoluto.
                archivo = str(f)
            out.append({
                "unidad": data.get("unidad"),
                "carpeta": d.name,
                "zona": zona,
                "archivo": archivo,
                "titulo": data.get("titulo", ""),
                "paginas": data.get("paginas", "") or data.get("paginas_libro", ""),
                "nivel": data.get("nivel", ""),
            })
        except Exception:
            pass
    return out


def _extra_unidades_paths():
    """Paths adicionales a escanear, desde la env var EXTRA_UNIDADES_PATHS.

    Permite ver inventarios en working-tree de worktrees paralelos
    (ej. extracciones en curso) sin tener que commitearlos a main.
    Separador: ':' (estilo PATH).
    Ejemplo: EXTRA_UNIDADES_PATHS=/Users/.../guia-didactica-extract-U2/unidades
    """
    raw = os.environ.get("EXTRA_UNIDADES_PATHS", "")
    paths = []
    from pathlib import Path
    for p in raw.split(":"):
        p = p.strip()
        if not p:
            continue
        path = Path(p).resolve()
        if path.exists() and path.is_dir():
            paths.append(path)
    return paths


def list_inventarios():
    """Lista unidades con inventario en unidades/ + paths extra (env var).

    Main tiene prioridad: si una unidad existe en main, no se añade
    desde un path extra aunque también esté allí. Las unidades que solo
    están en paths extra (working tree de un worktree paralelo) se
    marcan con zona='extra' para distinguirlas en la UI.
    """
    seen = set()
    out = []
    for inv in _scan_zona(PROJECT / "unidades", None, None, ""):
        out.append(inv)
        seen.add(inv["unidad"])
    for ep in _extra_unidades_paths():
        for inv in _scan_zona(ep, None, None, "extra"):
            if inv["unidad"] not in seen:
                out.append(inv)
                seen.add(inv["unidad"])
    return sorted(out, key=lambda x: (x["unidad"] is None, str(x["unidad"])))


def get_inventario(unidad, zona=""):
    """Lee inventario de main o de paths extra (main tiene prioridad).

    `unidad` puede ser int (U0-U9) o str (variantes tipo "1p" para propuestas).
    """
    try:
        folder_name = f"U{int(unidad)}"
    except (TypeError, ValueError):
        # Variantes tipo "Np" (propuestas): U1p → U1-propuesta, U2p → U2-propuesta, etc.
        import re as _re
        s = f"U{unidad}"
        m = _re.match(r"^U(\d+)p$", s)
        folder_name = f"U{m.group(1)}-propuesta" if m else s
    folder = PROJECT / "unidades" / folder_name
    candidates = list(folder.glob("*inventario.json")) if folder.exists() else []
    if candidates:
        return json.loads(candidates[0].read_text(encoding="utf-8"))
    for ep in _extra_unidades_paths():
        folder = ep / folder_name
        candidates = list(folder.glob("*inventario.json")) if folder.exists() else []
        if candidates:
            return json.loads(candidates[0].read_text(encoding="utf-8"))
    return {"error": f"No hay inventario para U{unidad}"}


def get_reciclaje():
    """Lee unidades/nc1-reciclaje.json (índice global de reciclaje cross-unidad)."""
    path = PROJECT / "unidades" / "nc1-reciclaje.json"
    if not path.exists():
        return {"error": "nc1-reciclaje.json no existe"}
    return json.loads(path.read_text(encoding="utf-8"))


def get_evaluaciones(unidad=None):
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    if unidad:
        cur.execute("""
            SELECT id, run_id, unidad, modelo, prompt_version,
                   total_tarjetas, metricas, duracion_s,
                   tokens_input, tokens_output, coste_usd, fecha
            FROM evaluaciones WHERE unidad = %s ORDER BY fecha DESC LIMIT 50
        """, (unidad,))
    else:
        cur.execute("""
            SELECT id, run_id, unidad, modelo, prompt_version,
                   total_tarjetas, metricas, duracion_s,
                   tokens_input, tokens_output, coste_usd, fecha
            FROM evaluaciones ORDER BY fecha DESC LIMIT 50
        """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def get_trazas(limit=20):
    """Obtiene las últimas trazas desde Langfuse API."""
    if not _langfuse_client:
        return {"error": "Langfuse no configurado", "trazas": []}
    try:
        traces = _langfuse_client.api.trace.list(limit=limit)
        result = []
        for t in traces.data:
            result.append({
                "id": t.id,
                "name": t.name,
                "timestamp": str(t.timestamp) if t.timestamp else None,
                "latency": t.latency,
                "total_cost": t.total_cost,
                "input": str(t.input)[:200] if t.input else None,
                "output": str(t.output)[:500] if t.output else None,
                "metadata": t.metadata,
                "tags": t.tags,
                "observations_count": len(t.observations) if t.observations else 0,
            })
        return {"trazas": result, "total": len(result)}
    except Exception as e:
        return {"error": str(e), "trazas": []}


def get_traza_detalle(trace_id):
    """Obtiene el detalle de una traza con todas sus observaciones."""
    if not _langfuse_client:
        return {"error": "Langfuse no configurado"}
    try:
        t = _langfuse_client.api.trace.get(trace_id)
        observations = []
        for obs in (t.observations or []):
            observations.append({
                "id": obs.id,
                "type": obs.type,
                "name": obs.name,
                "start_time": str(obs.start_time) if obs.start_time else None,
                "end_time": str(obs.end_time) if obs.end_time else None,
                "latency": obs.latency,
                "input": str(obs.input)[:500] if obs.input else None,
                "output": str(obs.output)[:500] if obs.output else None,
                "level": obs.level,
                "status_message": obs.status_message,
                "usage": obs.usage.model_dump() if obs.usage else None,
                "total_cost": obs.calculated_total_cost,
                "parent_id": obs.parent_observation_id,
            })
        # Sort by start_time
        observations.sort(key=lambda x: x["start_time"] or "")
        return {
            "id": t.id,
            "name": t.name,
            "timestamp": str(t.timestamp) if t.timestamp else None,
            "latency": t.latency,
            "total_cost": t.total_cost,
            "input": str(t.input)[:1000] if t.input else None,
            "output": str(t.output)[:2000] if t.output else None,
            "observations": observations,
        }
    except Exception as e:
        return {"error": str(e)}


# --- Ejecución de agentes en background ---
_agent_runs = {}  # run_id -> {status, agente, unidad, modelo, output, start_time, end_time}

AGENT_SCRIPTS = {
    "recurvo": "scripts/crewai/recurvo.py",
}

AVAILABLE_MODELS = [
    # --- Groq (gratis) ---
    {"id": "groq/openai/gpt-oss-120b", "name": "GPT-OSS 120B (Groq)", "provider": "groq", "cost": "gratis", "ctx": "131K", "nota": "Probado — funciona"},
    {"id": "groq/openai/gpt-oss-20b", "name": "GPT-OSS 20B (Groq)", "provider": "groq", "cost": "gratis", "ctx": "131K", "nota": "Más rápido, menor calidad"},
    {"id": "groq/llama-3.3-70b-versatile", "name": "Llama 3.3 70B (Groq)", "provider": "groq", "cost": "gratis", "ctx": "131K", "nota": "Buen instruction-following"},
    {"id": "groq/llama-3.1-8b-instant", "name": "Llama 3.1 8B (Groq)", "provider": "groq", "cost": "gratis", "ctx": "131K", "nota": "Ultra-rápido, ideal para tools"},
    {"id": "groq/meta-llama/llama-4-scout-17b-16e-instruct", "name": "Llama 4 Scout 17B (Groq)", "provider": "groq", "cost": "gratis", "ctx": "131K", "nota": "MoE, Llama 4"},
    {"id": "groq/moonshotai/kimi-k2-instruct-0905", "name": "Kimi K2 (Groq)", "provider": "groq", "cost": "gratis", "ctx": "262K", "nota": "Versión nueva, preview"},
    {"id": "groq/qwen/qwen3-32b", "name": "Qwen 3 32B (Groq)", "provider": "groq", "cost": "gratis", "ctx": "131K", "nota": "Errores factuales en pruebas"},
    # --- Anthropic (Claude) ---
    {"id": "anthropic/claude-opus-4-20250514", "name": "Claude Opus 4", "provider": "anthropic", "cost": "$15/$75", "ctx": "200K", "nota": "Máxima capacidad, costoso"},
    {"id": "anthropic/claude-sonnet-4-20250514", "name": "Claude Sonnet 4", "provider": "anthropic", "cost": "$3/$15", "ctx": "200K", "nota": "Mejor equilibrio calidad/precio"},
    {"id": "anthropic/claude-haiku-3-5-20241022", "name": "Claude Haiku 3.5", "provider": "anthropic", "cost": "$0.80/$4", "ctx": "200K", "nota": "Rápido y barato"},
    # --- DeepSeek ---
    {"id": "deepseek/deepseek-chat", "name": "DeepSeek V3", "provider": "deepseek", "cost": "$0.27/$1.10", "ctx": "64K", "nota": "Buena calidad, muy económico"},
    {"id": "deepseek/deepseek-reasoner", "name": "DeepSeek R1", "provider": "deepseek", "cost": "$0.55/$2.19", "ctx": "64K", "nota": "Razonamiento avanzado (CoT)"},
]


def start_agent(agente, unidad, agents_cfg):
    """Lanza un agente en un subproceso. Devuelve run_id.
    agents_cfg: dict con claves "0","1","2" → {model, temperature, max_tokens, top_p} por agente.
    Acepta también string simple (retrocompatible: se usa como RECURVO_LLM).
    """
    script = AGENT_SCRIPTS.get(agente)
    if not script:
        return {"error": f"Agente '{agente}' no tiene script asignado"}

    run_id = str(uuid.uuid4())[:8]
    script_path = (PROJECT / script).resolve()
    cmd = [sys.executable, str(script_path), str(unidad)]
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"  # forzar output inmediato

    # Map per-agent config to env vars
    ENV_MAP = {
        "0": {"model": "RECURVO_LLM_GEN", "temperature": "RECURVO_TEMP_GEN",
              "max_tokens": "RECURVO_MAXTOK_GEN", "top_p": "RECURVO_TOPP_GEN"},
        "1": {"model": "RECURVO_LLM_VER", "temperature": "RECURVO_TEMP_VER",
              "max_tokens": "RECURVO_MAXTOK_VER", "top_p": "RECURVO_TOPP_VER"},
        "2": {"model": "RECURVO_LLM_WR", "temperature": "RECURVO_TEMP_WR",
              "max_tokens": "RECURVO_MAXTOK_WR", "top_p": "RECURVO_TOPP_WR"},
    }

    if isinstance(agents_cfg, dict) and any(isinstance(v, dict) for v in agents_cfg.values()):
        for idx, mapping in ENV_MAP.items():
            cfg = agents_cfg.get(idx, {})
            if isinstance(cfg, dict):
                for param, env_var in mapping.items():
                    if param in cfg:
                        env[env_var] = str(cfg[param])
        modelo_display = " | ".join(
            f"{['Gen','Ver','Wr'][int(i)]}:{agents_cfg.get(i,{}).get('model','default').split('/')[-1]}"
            for i in ["0","1","2"] if i in agents_cfg
        )
    elif isinstance(agents_cfg, dict):
        # Old format: {0: "model_id", ...}
        for idx, mapping in ENV_MAP.items():
            if idx in agents_cfg:
                env[mapping["model"]] = str(agents_cfg[idx])
        modelo_display = " | ".join(
            f"{['Gen','Ver','Wr'][int(i)]}:{str(agents_cfg.get(i,'')).split('/')[-1]}"
            for i in ["0","1","2"] if i in agents_cfg
        )
    else:
        env["RECURVO_LLM"] = str(agents_cfg)
        modelo_display = str(agents_cfg)

    cwd = str(script_path.parent)  # ejecutar desde el directorio del script

    _agent_runs[run_id] = {
        "status": "running",
        "agente": agente,
        "unidad": unidad,
        "modelo": modelo_display,
        "agents_cfg": agents_cfg if isinstance(agents_cfg, dict) else {"0": {"model": str(agents_cfg)}},
        "output": "",
        "start_time": time.time(),
        "end_time": None,
    }

    def _run():
        try:
            proc = subprocess.Popen(
                cmd, env=env, cwd=cwd,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, bufsize=1,
            )
            deadline = time.time() + 600
            for line in proc.stdout:
                _agent_runs[run_id]["output"] += line
                if time.time() > deadline:
                    proc.kill()
                    _agent_runs[run_id]["output"] += "\nTimeout: el agente tardó más de 10 minutos\n"
                    break
            proc.wait(timeout=10)
            _agent_runs[run_id]["status"] = "completed" if proc.returncode == 0 else "error"
        except Exception as e:
            _agent_runs[run_id]["output"] += f"\nError: {e}\n"
            _agent_runs[run_id]["status"] = "error"
        _agent_runs[run_id]["end_time"] = time.time()

    threading.Thread(target=_run, daemon=True).start()
    return {"run_id": run_id, "status": "running"}


def get_agent_status(run_id=None):
    """Devuelve estado de una ejecución o todas las recientes."""
    if run_id:
        run = _agent_runs.get(run_id)
        if not run:
            return {"error": "run_id no encontrado"}
        elapsed = (run["end_time"] or time.time()) - run["start_time"]
        return {**run, "run_id": run_id, "elapsed_s": round(elapsed, 1)}
    # All runs, most recent first
    runs = []
    for rid, r in sorted(_agent_runs.items(), key=lambda x: x[1]["start_time"], reverse=True):
        elapsed = (r["end_time"] or time.time()) - r["start_time"]
        runs.append({
            "run_id": rid,
            "status": r["status"],
            "agente": r["agente"],
            "unidad": r["unidad"],
            "modelo": r["modelo"],
            "elapsed_s": round(elapsed, 1),
            "start_time": r["start_time"],
        })
    return {"runs": runs[:20]}


def run_evaluation(unidad):
    """Ejecuta evaluación sobre las tarjetas de una unidad y guarda resultado."""
    # Importar desde eval/
    eval_dir = os.path.join(str(PROJECT), "eval")
    sys.path.insert(0, eval_dir)
    from evaluar_tarjetas import obtener_tarjetas, evaluar_tarjetas, guardar_evaluacion, crear_tabla_evaluaciones
    crear_tabla_evaluaciones()
    tarjetas = obtener_tarjetas(unidad)
    if not tarjetas:
        return {"error": f"No hay tarjetas para U{unidad:02d}"}
    metricas = evaluar_tarjetas(tarjetas)
    eval_id = guardar_evaluacion(unidad, "manual", metricas)
    return {"id": eval_id, "metricas": metricas}


def get_crew_agents(crew_name):
    """Devuelve todos los agentes de un crew, ordenados por pipeline."""
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT id, crew, agent_key, agent_order, role, goal, backstory,
               task_description, task_expected_output, max_iter, updated_at
        FROM crew_agents
        WHERE crew = %s
        ORDER BY agent_order
    """, (crew_name,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def update_crew_agent(agent_id, data):
    """Actualiza campos mutables de un agente. Devuelve True si actualizó."""
    allowed = {"role", "goal", "backstory", "task_description",
               "task_expected_output", "max_iter"}
    fields = {k: v for k, v in data.items() if k in allowed}
    if not fields:
        return False
    conn = _db()
    cur = conn.cursor()
    set_clause = ", ".join(f"{k} = %s" for k in fields)
    values = list(fields.values()) + [agent_id]
    cur.execute(
        f"UPDATE crew_agents SET {set_clause}, updated_at = NOW() WHERE id = %s",
        values,
    )
    ok = cur.rowcount > 0
    conn.commit()
    conn.close()
    return ok


def update_tarjeta_field(tarjeta_id, campo, valor):
    allowed = {
        "palabra", "genero", "color_genero", "silaba_tonica", "regla",
        "campo_semantico", "color_campo", "ejemplo", "frecuencia",
        "trad_it", "trad_fr", "trad_pt_br", "trad_en",
        "trad_cs", "trad_pl", "trad_tr", "seccion", "pagina",
        "nivel_jerarquia", "estado", "unidad_origen", "estado_revision",
    }
    if campo not in allowed:
        return False
    conn = _db()
    cur = conn.cursor()
    cur.execute(
        f"UPDATE tarjetas_vocabulario SET {campo} = %s, fecha_modificacion = NOW() WHERE id = %s",
        (valor, tarjeta_id),
    )
    conn.commit()
    conn.close()
    return True

UNITS = [f"U{i}" for i in range(0, 10)]
SECTIONS = ["vocabulario", "gramatica", "comunicacion", "destrezas",
            "cultura", "evaluacion", "itinerarios"]
SECTION_LABELS = {
    "vocabulario": "Vocabulario",
    "gramatica": "Gramática",
    "comunicacion": "Comunicación",
    "destrezas": "Destrezas",
    "cultura": "Cultura",
    "evaluacion": "Evaluación",
    "itinerarios": "Itinerarios",
}

AGENTS = {
    "vocabulario": {"name": "Vocabulario", "rep": "viejo/repertorios/vocabulario.md"},
    "gramatica": {"name": "Gramática", "rep": "viejo/repertorios/gramatica.md"},
    "comunicacion": {"name": "Comunicación", "rep": "viejo/repertorios/comunicacion.md"},
    "destrezas": {"name": "Destrezas", "rep": "viejo/repertorios/destrezas.md"},
    "cultura": {"name": "Cultura", "rep": "viejo/repertorios/cultura.md"},
    "evaluacion": {"name": "Evaluación", "rep": "viejo/repertorios/evaluacion.md"},
}


def scan_section(unit_dir, unit, section):
    # Nueva canónica (post-rediseño): unidades/UN/propuesta/<section>.md (sin prefijo)
    propuesta_dir = unit_dir / "propuesta"
    new_candidates = list(propuesta_dir.glob(f"{section}.md")) if propuesta_dir.exists() else []
    # U0 atípica: una sola propuesta `punto-de-partida.md` cubre la unidad entera.
    # Si existe, se propaga a todas las celdas de U0.
    if unit == "U0" and propuesta_dir.exists():
        atipica = list(propuesta_dir.glob("punto-de-partida.md"))
        if atipica:
            new_candidates = atipica
    # Legacy: unidades/UN/UN-<section>*.md (compatibilidad hacia atrás)
    legacy_candidates = [f for f in unit_dir.glob(f"{unit}-{section}*.md") if "-paginas" not in f.name]
    main = new_candidates + legacy_candidates
    if not main:
        return {"status": "missing", "lines": 0, "pendiente": 0, "path": ""}
    f = main[0]
    text = f.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    pend = sum(1 for l in lines if "*pendiente*" in l)
    n = len(lines)
    # Criterio v11.0a: el conteo de líneas no es señal de calidad.
    # complete = archivo existe sin marcadores *pendiente*. in-progress = tiene pendientes.
    if pend == 0:
        st = "complete"
    else:
        st = "in-progress"
    return {"status": st, "lines": n, "pendiente": pend,
            "path": str(f.relative_to(PROJECT))}


def scan_all():
    result = {}
    for u in UNITS:
        d = PROJECT / "unidades" / u
        result[u] = {}
        for s in SECTIONS:
            if d.exists():
                result[u][s] = scan_section(d, u, s)
            else:
                result[u][s] = {"status": "missing", "lines": 0, "pendiente": 0, "path": ""}
    return result


def color_for(status):
    if status == "complete": return "#2ecc71"
    if status == "in-progress": return "#f39c12"
    if status == "structure-only": return "#e67e22"
    return "#bdc3c7"


def _mermaid_init():
    """Bloque init de Mermaid con tipografía + paleta MD3 del proyecto.

    Reduce el font-size al del dashboard (12-13 px) y fija fuente Inter
    para coherencia con el resto del UI.
    """
    return (
        "%%{init: {'theme':'base','themeVariables':{"
        "'fontFamily':'Inter, system-ui, sans-serif',"
        "'fontSize':'13px',"
        f"'primaryColor':'{PAL['surface']}',"
        f"'primaryTextColor':'{PAL['on_surface']}',"
        f"'primaryBorderColor':'{PAL['primary']}',"
        f"'lineColor':'{PAL['primary']}',"
        f"'secondaryColor':'{PAL['surface_variant']}',"
        f"'tertiaryColor':'{PAL['surface']}'"
        "}}}%%"
    )


def mermaid_level1():
    """Arquitectura del sistema activo — auto-discovered desde el filesystem.

    Diseño coherente con las etiquetas `.cat-tag` del dashboard (paleta CHIPS,
    8 tonos pastel suaves). Nodos redondeados, etiquetas con título + subtítulo
    explicativo, leyenda visual al final que mapea cada tono a un rol.

    Convenciones de tono:
    - azul       → Fuente externa (libro, PDFs)
    - lila       → Especificación / contratos / registries
    - menta      → Sistema IA (Claude Code)
    - verde      → Producto validado (inventarios validados)
    - amarillo   → Código operativo (scripts)
    - melocoton  → Interfaz humana (autor, dashboard)
    """
    inv = len(discover_inventarios())
    reg = len(discover_registries())
    scr = len(discover_scripts())

    lines = [_mermaid_init(), "graph TD"]

    # Nodos: shape redondeado A("...") con título + subtítulo breve
    lines.append(f'    LIBRO("Libro NC1<br/><small>Nuevo Compañeros 1 · SGEL · A1.1</small>")')
    lines.append(f'    PDFS("PDFs por unidad<br/><small>unidades/UX/fuente/ · {inv}/10</small>")')
    lines.append('    CONTRATOS("Contratos fase 1<br/><small>prompt · schema · reglas · convenciones</small>")')
    lines.append(f'    REG("Registries canónicos<br/><small>{reg} archivos · léxico · verbal · gramatical · pron-orto</small>")')
    lines.append('    PCIC("PCIC A1<br/><small>4 archivos fuente · respaldo decisional</small>")')
    lines.append('    CLAUDE("Claude Code<br/><small>extracción dry-run en worktree aislado</small>")')
    lines.append(f'    INV("Inventarios JSON<br/><small>{inv}/10 producidos · shape v10.117</small>")')
    lines.append(f'    SCRIPTS("Scripts Python<br/><small>{scr} archivos · validador · serializador · integrador</small>")')
    lines.append('    DASH("Dashboard<br/><small>diagrama.py + web/index.html · auto-actualizado</small>")')
    lines.append('    AUTOR("Autor / revisor<br/><small>revisión visual · dictamen editorial</small>")')

    # Flujo
    lines.append('    LIBRO --> PDFS --> CLAUDE')
    lines.append('    CONTRATOS --> CLAUDE')
    lines.append('    PCIC --> REG --> CLAUDE')
    lines.append('    CLAUDE --> INV')
    lines.append('    INV --> SCRIPTS')
    lines.append('    INV --> DASH')
    lines.append('    SCRIPTS --> AUTOR')
    lines.append('    DASH --> AUTOR')
    lines.append('    AUTOR -.-> CONTRATOS')

    # Asignación de tonos
    tones = {
        "LIBRO": "azul",
        "PDFS": "azul",
        "CONTRATOS": "lila",
        "REG": "lila",
        "PCIC": "lila",
        "CLAUDE": "menta",
        "INV": "verde",
        "SCRIPTS": "amarillo",
        "DASH": "melocoton",
        "AUTOR": "melocoton",
    }
    for node, tone in tones.items():
        lines.append(f"    style {node} {_chip_style(tone)}")

    return "\n".join(lines)


LEGEND_LEVEL1 = [
    ("Fuente externa", "azul"),
    ("Especificación", "lila"),
    ("Sistema IA", "menta"),
    ("Validado", "verde"),
    ("Código", "amarillo"),
    ("Interfaz humana", "melocoton"),
]


def mermaid_level2():
    """Flujo operativo de fase 1 — extracción del inventario.

    Nodos redondeados, paleta CHIPS coherente con `.cat-tag` del dashboard.
    Convención de tono:
    - melocoton → acción humana (autor)
    - menta     → acción del sistema IA (Claude)
    - amarillo  → acción de código (scripts)
    - lila      → revisión humana visual
    - verde     → cierre validado
    """
    lines = [_mermaid_init(), "graph LR"]

    lines.append('    P1("1 · Exporta PDF<br/><small>autor → unidades/UX/fuente/</small>")')
    lines.append('    P2("2 · Invoca Claude<br/><small>autor → chat en worktree</small>")')
    lines.append('    P3("3 · Lee contratos + PDF<br/><small>Claude → schema · reglas · convenciones</small>")')
    lines.append('    P4("4 · Genera inventario<br/><small>Claude → UX-nc1-inventario.json</small>")')
    lines.append('    P5("5 · Valida automático<br/><small>scripts/validar_inventario.py</small>")')
    lines.append('    P6("6 · Revisión visual<br/><small>autor → dashboard</small>")')
    lines.append('    P7("7 · Fase cerrada<br/><small>integración a main</small>")')

    lines.append('    P1 --> P2 --> P3 --> P4 --> P5 --> P6')
    lines.append('    P6 -->|OK| P7')
    lines.append('    P6 -->|errores| P4')

    tones = {
        "P1": "melocoton",
        "P2": "melocoton",
        "P3": "menta",
        "P4": "menta",
        "P5": "amarillo",
        "P6": "lila",
        "P7": "verde",
    }
    for node, tone in tones.items():
        lines.append(f"    style {node} {_chip_style(tone)}")

    return "\n".join(lines)


LEGEND_LEVEL2 = [
    ("Acción humana", "melocoton"),
    ("Acción IA", "menta"),
    ("Acción código", "amarillo"),
    ("Revisión visual", "lila"),
    ("Validado", "verde"),
]


def mermaid_level3():
    """Fases del proceso editorial — auto-discovered desde fases/N-<nombre>/.

    Solo muestra fases que tienen carpeta real en el repo. El estado por fase
    se añadirá en una iteración posterior (decisión del autor, 2026-05-15).
    """
    fases = discover_fases()
    lines = [_mermaid_init(), "graph LR"]

    if not fases:
        lines.append('    EMPTY("Sin fases definidas en fases/")')
        lines.append(f"    style EMPTY {_chip_style('gris')}")
        return "\n".join(lines)

    # Nodos: shape redondeado con título + nombre slug legible
    for numero, slug, _ in fases:
        nombre = slug.replace("-", " ")
        lines.append(f'    F{numero}("Fase {numero}<br/><small>{nombre}</small>")')

    # Encadenamiento secuencial entre fases consecutivas
    for i in range(len(fases) - 1):
        lines.append(f"    F{fases[i][0]} --> F{fases[i + 1][0]}")

    # Estilos: F1 activa (verde), resto sin estado (gris suave)
    for idx, (numero, _, _) in enumerate(fases):
        tone = "verde" if idx == 0 else "gris"
        lines.append(f"    style F{numero} {_chip_style(tone)}")

    return "\n".join(lines)


LEGEND_LEVEL3 = [
    ("Activa", "verde"),
    ("Sin estado declarado", "gris"),
]


def mermaid_level4(status):
    """Estado actual por unidad - inventario extraido o pendiente."""
    lines = ["graph LR"]
    lines.append('    LIBRO["Libro NC1"]')
    for n in range(0, 10):
        u = f"U{n}"
        info = status.get(u, {})
        # info no tiene "inventario" hoy; usamos presencia del archivo
        inv_path = PROJECT / "unidades" / u / f"{u}-nc1-inventario.json"
        existe = inv_path.exists()
        st = "OPERATIVO" if existe else "pendiente"
        color = "#27ae60" if existe else "#bdc3c7"
        text_color = "#fff" if existe else "#000"
        label = f"{u} - inventario {st}"
        lines.append(f'    {u}["{label}"]')
        lines.append(f"    LIBRO --> {u}")
        lines.append(f"    style {u} fill:{color},color:{text_color}")
    lines.append('    style LIBRO fill:#3498db,color:#fff')
    return "\n".join(lines)


def mermaid_database():
    return """erDiagram
    unidades {
        int id PK
        int numero UK
        text curso
        text titulo
        text paginas
        text nivel
        jsonb contenidos_indice
    }
    paginas {
        int id PK
        int unidad_id FK
        int numero
        text seccion
    }
    actividades {
        int id PK
        int pagina_id FK
        text codigo UK
        int numero
        text tipo
        text instruccion
        jsonb contenido_linguistico
        text destreza
        boolean tiene_audio
        int pista_audio
        boolean tiene_imagen
        text descripcion
    }
    respuestas {
        int id PK
        int actividad_id FK
        int orden
        text texto
    }
    cuadros {
        int id PK
        int pagina_id FK
        text tipo_cuadro
        text titulo
        jsonb contenido
    }
    autoevaluaciones {
        int id PK
        int unidad_id FK
        int pagina
        text instruccion_original
        jsonb opciones
        boolean emoticonos
    }
    reciclaje {
        int id PK
        int actividad_origen_id FK
        int actividad_destino_id FK
        text contenido
        text tipo
    }
    profesores {
        int id PK
        text nombre
        text centro
        text pais
        text nivel_escolar
    }
    grupos {
        int id PK
        int profesor_id FK
        text nombre_grupo
        int cantidad_estudiantes
        boolean nee
        text nee_detalle
        numeric horas_semana
        int duracion_clase
        numeric horas_ano
    }
    personalizaciones {
        int id PK
        int grupo_id FK
        int actividad_id FK
        int tiempo_custom
        text variante
        text notas
        boolean completada
    }

    unidades ||--o{ paginas : "tiene"
    paginas ||--o{ actividades : "contiene"
    paginas ||--o{ cuadros : "incluye"
    unidades ||--o| autoevaluaciones : "tiene (opcional)"
    actividades ||--o{ respuestas : "tiene"
    actividades ||--o{ reciclaje : "origen"
    actividades ||--o{ reciclaje : "destino"
    profesores ||--o{ grupos : "tiene"
    grupos ||--o{ personalizaciones : "crea"
    actividades ||--o{ personalizaciones : "recibe"
"""


def build_diagrams_json():
    """Return all diagram codes + status + legends as JSON for live polling."""
    status = scan_all()
    legends = {
        "nivel1": [{"label": l, "tone": t} for l, t in LEGEND_LEVEL1],
        "nivel2": [{"label": l, "tone": t} for l, t in LEGEND_LEVEL2],
        "nivel3": [{"label": l, "tone": t} for l, t in LEGEND_LEVEL3],
    }
    return json.dumps({
        "nivel1": mermaid_level1(),
        "nivel2": mermaid_level2(),
        "nivel3": mermaid_level3(),
        "nivel4": mermaid_level4(status),
        "database": mermaid_database(),
        "legends": legends,
        "status": status,
        "hash": hashlib.md5(json.dumps(status, sort_keys=True).encode()).hexdigest()[:8],
    }, ensure_ascii=False)


HTML_FILE = PROJECT / "web" / "index.html"


def load_html_template():
    """Lee el HTML desde disco en cada request (hot reload)."""
    return HTML_FILE.read_text(encoding="utf-8")


TOOLS_FILE = PROJECT / "scripts" / "crewai" / "tools.py"
TOOL_VERSIONS_FILE = PROJECT / "scripts" / "crewai" / "tool_versions.json"
TOOLS_BACKUP = PROJECT / "scripts" / "crewai" / "tools.py.backup"


def get_tool_sources():
    """Lee tools.py y extrae el código fuente de cada clase tool."""
    if not TOOLS_FILE.exists():
        return {}
    text = TOOLS_FILE.read_text(encoding="utf-8")
    parts = re.split(r"(?=^class \w+\(BaseTool\))", text, flags=re.MULTILINE)
    result = {}
    for part in parts:
        m = re.search(r'name:\s*str\s*=\s*["\'](\w+)["\']', part)
        if m:
            result[m.group(1)] = part.strip()
    return result


def get_tool_versions():
    """Lee versiones por tool del sidecar JSON. Inicializa si no existe."""
    if TOOL_VERSIONS_FILE.exists():
        return json.loads(TOOL_VERSIONS_FILE.read_text(encoding="utf-8"))
    sources = get_tool_sources()
    versions = {}
    for name in sources:
        versions[name] = {"version": 1, "updated_at": None}
    TOOL_VERSIONS_FILE.write_text(
        json.dumps(versions, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return versions


def save_tool_source(tool_name, new_source):
    """Guarda código editado de un tool. Retorna (ok, version_o_error)."""
    if not TOOLS_FILE.exists():
        return False, "tools.py not found"

    text = TOOLS_FILE.read_text(encoding="utf-8")
    parts = re.split(r"(?=^class \w+\(BaseTool\))", text, flags=re.MULTILINE)

    preamble = parts[0]
    classes = parts[1:]

    target_idx = None
    for i, part in enumerate(classes):
        m = re.search(r'name:\s*str\s*=\s*["\'](\w+)["\']', part)
        if m and m.group(1) == tool_name:
            target_idx = i
            break

    if target_idx is None:
        return False, f"Tool '{tool_name}' not found in tools.py"

    classes[target_idx] = new_source.strip()

    reconstructed = preamble.rstrip("\n") + "\n\n\n" + "\n\n\n".join(
        c.strip() for c in classes
    ) + "\n"

    try:
        compile(reconstructed, "tools.py", "exec")
    except SyntaxError as e:
        return False, f"Error de sintaxis: {e.msg} (línea {e.lineno})"

    recheck = re.split(r"(?=^class \w+\(BaseTool\))", reconstructed, flags=re.MULTILINE)
    if len(recheck) - 1 != len(classes):
        return False, "La estructura de clases cambió — operación cancelada"

    shutil.copy2(TOOLS_FILE, TOOLS_BACKUP)
    TOOLS_FILE.write_text(reconstructed, encoding="utf-8")

    versions = get_tool_versions()
    tv = versions.get(tool_name, {"version": 0, "updated_at": None})
    tv["version"] += 1
    tv["updated_at"] = datetime.datetime.now().isoformat()
    versions[tool_name] = tv
    TOOL_VERSIONS_FILE.write_text(
        json.dumps(versions, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return True, tv["version"]


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        if os.environ.get("DEBUG"):
            print(fmt % args)

    def _respond(self, code, ctype, body):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        if parsed.path == "/api/version":
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"version": _read_version()}))
        elif parsed.path == "/api/status":
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(scan_all(), ensure_ascii=False))
        elif parsed.path == "/api/diagrams":
            self._respond(200, "application/json; charset=utf-8",
                          build_diagrams_json())
        elif parsed.path == "/api/tarjetas":
            unidad = int(qs.get("unidad", [3])[0])
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_tarjetas(unidad), ensure_ascii=False, default=str))
        elif parsed.path == "/api/correcciones":
            unidad = qs.get("unidad", [None])[0]
            unidad = int(unidad) if unidad else None
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_correcciones(unidad), ensure_ascii=False, default=str))
        elif parsed.path == "/api/correcciones/stats":
            unidad = qs.get("unidad", [None])[0]
            unidad = int(unidad) if unidad else None
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_correcciones_stats(unidad), ensure_ascii=False, default=str))
        elif parsed.path == "/api/reglas":
            crew = qs.get("crew", ["recurvo"])[0]
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_reglas(crew), ensure_ascii=False, default=str))
        elif parsed.path == "/api/inventarios":
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(list_inventarios(), ensure_ascii=False))
        elif parsed.path == "/api/inventario":
            raw_u = qs.get("unidad", ["3"])[0]
            try:
                unidad = int(raw_u)
            except ValueError:
                unidad = raw_u  # variante string (ej. "1p" para propuesta de rediseño)
            zona = qs.get("zona", ["activo"])[0]
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_inventario(unidad, zona), ensure_ascii=False))
        elif parsed.path == "/api/reciclaje":
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_reciclaje(), ensure_ascii=False))
        elif parsed.path == "/api/evaluaciones":
            unidad = qs.get("unidad", [None])[0]
            unidad = int(unidad) if unidad else None
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_evaluaciones(unidad), ensure_ascii=False, default=str))
        elif parsed.path == "/api/agente/status":
            run_id = qs.get("run_id", [None])[0]
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_agent_status(run_id), ensure_ascii=False, default=str))
        elif parsed.path == "/api/agente/output":
            run_id = qs.get("run_id", [""])[0]
            run = _agent_runs.get(run_id, {})
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"output": run.get("output", ""), "status": run.get("status", "unknown")}, default=str))
        elif parsed.path == "/api/crew_agents":
            crew = qs.get("crew", ["recurvo"])[0]
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_crew_agents(crew), ensure_ascii=False, default=str))
        elif parsed.path == "/api/modelos":
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(AVAILABLE_MODELS, ensure_ascii=False))
        elif parsed.path == "/api/tool_sources":
            sources = get_tool_sources()
            versions = get_tool_versions()
            merged = {}
            for name, src in sources.items():
                v = versions.get(name, {"version": 1, "updated_at": None})
                merged[name] = {"source": src, "version": v["version"],
                                "updated_at": v["updated_at"]}
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(merged, ensure_ascii=False))
        elif parsed.path == "/api/trazas":
            limit = int(qs.get("limit", [20])[0])
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_trazas(limit), ensure_ascii=False, default=str))
        elif parsed.path.startswith("/api/trazas/"):
            trace_id = parsed.path.split("/api/trazas/")[1]
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_traza_detalle(trace_id), ensure_ascii=False, default=str))
        elif parsed.path in ("/favicon.ico", "/favicon.svg", "/web/favicon.svg"):
            svg_path = PROJECT / "web" / "favicon.svg"
            if svg_path.exists():
                self._respond(200, "image/svg+xml", svg_path.read_text(encoding="utf-8"))
            else:
                self.send_response(204)
                self.end_headers()
        elif parsed.path == "/":
            html = load_html_template()
            self._respond(200, "text/html; charset=utf-8", html)
        else:
            self.send_error(404)

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}

        if parsed.path == "/api/correcciones":
            new_id = insert_correccion(body)
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"id": new_id, "ok": True}))
        elif parsed.path == "/api/tarjetas/delete":
            delete_tarjeta(body["id"])
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"ok": True}))
        elif parsed.path == "/api/tarjetas/update":
            ok = update_tarjeta_field(body["id"], body["campo"], body["valor"])
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"ok": ok}))
        elif parsed.path == "/api/evaluaciones/run":
            unidad = body.get("unidad", 3)
            result = run_evaluation(unidad)
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(result, ensure_ascii=False, default=str))
        elif parsed.path == "/api/crew_agents/update":
            agent_id = body.get("id")
            ok = update_crew_agent(agent_id, body)
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"ok": ok}))
        elif parsed.path == "/api/reglas":
            regla_id = upsert_regla(body)
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"id": regla_id, "ok": True}))
        elif parsed.path == "/api/reglas/delete":
            delete_regla(body["id"])
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"ok": True}))
        elif parsed.path == "/api/tool_sources/update":
            tool_name = body.get("tool_name", "")
            source = body.get("source", "")
            ok, result = save_tool_source(tool_name, source)
            if ok:
                self._respond(200, "application/json; charset=utf-8",
                              json.dumps({"ok": True, "version": result}))
            else:
                self._respond(400, "application/json; charset=utf-8",
                              json.dumps({"ok": False, "error": result}, ensure_ascii=False))
        elif parsed.path == "/api/agente/run":
            agente = body.get("agente", "recurvo")
            unidad = body.get("unidad", 3)
            agents_cfg = body.get("agents", body.get("modelos", body.get("modelo", "groq/openai/gpt-oss-120b")))
            result = start_agent(agente, unidad, agents_cfg)
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(result, ensure_ascii=False, default=str))
        else:
            self.send_error(404)


if __name__ == "__main__":
    HOST = os.environ.get("HOST", "0.0.0.0")
    PORT = int(os.environ.get("PORT", PORT))
    server = http.server.HTTPServer((HOST, PORT), Handler)
    print(f"Sistema de gestión: http://{HOST}:{PORT}")
    print("En vivo - se actualiza cada 3 segundos")
    print("Ctrl+C para detener")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDetenido.")
