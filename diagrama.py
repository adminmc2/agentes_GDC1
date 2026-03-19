#!/usr/bin/env python3
"""Diagrama de procesos del proyecto - Guía Didáctica del Profesor.

Genera diagramas Mermaid desde el estado real del proyecto.
Uso: python3 diagrama.py -> http://127.0.0.1:8080
"""

import http.server
import json
import hashlib
import os
import re
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
PORT = 8080
SERVER_VERSION = "8.5"  # major.minor — major para cambios grandes, minor para deploys pequeños

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

UNITS = [f"U{i:02d}" for i in range(1, 10)]
SECTIONS = ["vocabulario", "gramatica", "comunicacion", "destrezas",
            "cultura", "reflexion", "evaluacion", "itinerarios"]
SECTION_LABELS = {
    "vocabulario": "Vocabulario",
    "gramatica": "Gramática",
    "comunicacion": "Comunicación",
    "destrezas": "Destrezas",
    "cultura": "Cultura",
    "reflexion": "Reflexión",
    "evaluacion": "Evaluación",
    "itinerarios": "Itinerarios",
}

AGENTS = {
    "vocabulario": {"name": "Vocabulario", "rep": "repertorios/vocabulario.md"},
    "gramatica": {"name": "Gramática", "rep": "repertorios/gramatica.md"},
    "comunicacion": {"name": "Comunicación", "rep": "repertorios/comunicacion.md"},
    "destrezas": {"name": "Destrezas", "rep": "repertorios/destrezas.md"},
    "cultura": {"name": "Cultura", "rep": "repertorios/cultura.md"},
    "evaluacion": {"name": "Evaluación", "rep": "repertorios/evaluacion.md"},
}


def scan_section(unit_dir, unit, section):
    candidates = list(unit_dir.glob(f"{unit}-{section}*.md"))
    main = [f for f in candidates if "-paginas" not in f.name]
    if not main:
        return {"status": "missing", "lines": 0, "pendiente": 0, "path": ""}
    f = main[0]
    text = f.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    pend = sum(1 for l in lines if "*pendiente*" in l)
    n = len(lines)
    if pend == 0 and n > 100:
        st = "complete"
    elif n > 50:
        st = "in-progress"
    else:
        st = "structure-only"
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


def mermaid_level1():
    return """graph TD
    LIBRO["Libro de texto - Nuevo Compañeros 1"]
    FUENTE["Material fuente - datos/fuente/ - PDF embebido por unidad"]
    INV["Inventario JSON - datos/inventarios/UXX-inventario.json"]
    BD[("Neon PostgreSQL - Base de datos - Fuente de verdad")]

    subgraph INFRA["Infraestructura pedagógica"]
        MT["Marco teórico - 72 KB"]
        CG["Curso general - 50 KB"]
        REF["10 bancos de técnicas - 800+ técnicas"]
    end

    subgraph REPS["Repertorios - opciones de explotación"]
        R_V["rep/vocabulario"]
        R_G["rep/gramática"]
        R_C["rep/comunicación"]
        R_D["rep/destrezas"]
        R_CU["rep/cultura"]
        R_E["rep/evaluación"]
    end

    subgraph AGENTES["Sistema de agentes - prompts v5.0"]
        AG_V["Vocabulario"]
        AG_G["Gramática"]
        AG_C["Comunicación"]
        AG_D["Destrezas"]
        AG_CU["Cultura"]
        AG_E["Evaluación"]
    end

    subgraph OUTPUT["Output por unidad"]
        EXP["Explotación didáctica - 7 secciones"]
        PIL["Píldoras formativas - 10 por unidad"]
        TAR["Tarjetas - vocabulario + gramática"]
        ITI["Itinerarios - 8 sesiones"]
    end

    LIBRO --> FUENTE
    FUENTE --> INV
    INV -->|"importación"| BD
    BD --> AGENTES
    INFRA --> AGENTES
    REPS --> AGENTES
    AGENTES --> OUTPUT

    OUTPUT --> GUIA["CAPA 1 - Guía impresa SGEL"]
    BD -.->|"consultas"| PERS["CAPA 3 - Guías personalizadas - futuro"]
    OUTPUT -.-> PERS

    style LIBRO fill:#3498db,color:#fff
    style FUENTE fill:#2980b9,color:#fff
    style INV fill:#8e44ad,color:#fff
    style BD fill:#e74c3c,color:#fff
    style GUIA fill:#2ecc71,color:#fff
    style PERS fill:#95a5a6,color:#fff,stroke-dasharray: 5 5
    style INFRA fill:#e8eaf6
    style AGENTES fill:#fff3e0
    style REPS fill:#e8f5e9
    style OUTPUT fill:#fce4ec"""


def mermaid_level2():
    return """graph LR
    subgraph PREP["1 - Preparación manual"]
        P1["Extraer actividades del inventario"]
        P2["Filtrar repertorio aplicable"]
        P3["Compilar reciclaje previo"]
        P4["Compilar contexto lingüístico"]
        P1 --> P2 --> P3 --> P4
    end

    subgraph GEN["2 - Generación con Claude Code"]
        G1["Cargar prompt del agente"]
        G2["Proporcionar inputs"]
        G3["Generar explotación + píldoras"]
        G1 --> G2 --> G3
    end

    subgraph POST["3 - Post-producción"]
        V1["Horas total máx. 7h"]
        V2["Variedad de opciones"]
        V3["Reciclaje mín. 30%"]
        V4["Ritmo máx. 15 min"]
        V5["Coherencia inter-sección"]
        V1 --- V2 --- V3 --- V4 --- V5
    end

    PREP --> GEN --> POST
    POST -->|OK| DONE["Sección validada"]
    POST -->|Falla| GEN

    style PREP fill:#e3f2fd
    style GEN fill:#fff3e0
    style POST fill:#f3e5f5
    style DONE fill:#2ecc71,color:#fff"""


def mermaid_level3():
    return """graph TD
    VOC["S1 Vocabulario - Ciclo 5 fases"]
    GRA["S2 Gramática - Ciclo 5 fases"]
    COM["S3 Comunicación - Protocolo A/C"]
    DES["S4 Destrezas - Protocolos L/E/CO/H"]
    CUL["S5 Cultura - Protocolo CU"]
    EVA["S7 Reflexión y Evaluación - Protocolo RE"]

    VOC -->|"exposición incidental"| GRA
    VOC -->|"vocabulario formalizado"| COM
    GRA -->|"gramática formalizada"| COM
    VOC -->|"reciclaje"| DES
    GRA -->|"reciclaje"| DES
    COM -->|"funciones comunicativas"| DES
    VOC -->|"contenedor mapeado"| CUL
    GRA -->|"contenedor mapeado"| CUL
    COM -->|"contenedor mapeado"| CUL
    DES -->|"estrategias"| CUL
    VOC -->|"100% reciclaje"| EVA
    GRA -->|"100% reciclaje"| EVA
    COM -->|"100% reciclaje"| EVA
    DES -->|"100% reciclaje"| EVA
    CUL -->|"100% reciclaje"| EVA

    subgraph CAJA["Estación de Servicio - tarjetas acumulativas"]
        C1["Caja 1 Vocabulario"]
        C2["Caja 2 Tips y esquemas"]
        C3["Caja 3 Gramatips"]
        C4["Caja 4 Estrategias destreza"]
        C5["Caja 5 Estrategia intercultural"]
    end

    VOC -.-> C1
    COM -.-> C2
    GRA -.-> C3
    DES -.-> C4
    CUL -.-> C5

    style VOC fill:#3498db,color:#fff
    style GRA fill:#2ecc71,color:#fff
    style COM fill:#e74c3c,color:#fff
    style DES fill:#9b59b6,color:#fff
    style CUL fill:#f39c12,color:#fff
    style EVA fill:#1abc9c,color:#fff
    style CAJA fill:#f5f5f5"""


def mermaid_level4(status):
    lines = ["graph LR"]
    for sid, info in AGENTS.items():
        s = status.get("U03", {}).get(sid, {})
        st = s.get("status", "missing")
        c = color_for(st)
        n = s.get("lines", 0)
        label = f'{info["name"]} - {n} líneas - {st}'
        lines.append(f'    AG_{sid}["{label}"]')
        lines.append(f'    REP_{sid}["{info["rep"]}"]')
        lines.append(f"    REP_{sid} --> AG_{sid}")
        lines.append(f"    style AG_{sid} fill:{c},color:#fff")
    lines.append('    INV["datos/inventarios/U03-inventario.json"] --> AG_vocabulario')
    lines.append("    INV --> AG_gramatica")
    lines.append("    INV --> AG_comunicacion")
    lines.append("    INV --> AG_destrezas")
    lines.append("    INV --> AG_cultura")
    lines.append("    INV --> AG_evaluacion")
    lines.append("    style INV fill:#3498db,color:#fff")
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
    cuadros_gramaticales {
        int id PK
        int pagina_id FK
        text titulo
        jsonb contenido
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
    paginas ||--o{ cuadros_gramaticales : "incluye"
    actividades ||--o{ respuestas : "tiene"
    actividades ||--o{ reciclaje : "origen"
    actividades ||--o{ reciclaje : "destino"
    profesores ||--o{ grupos : "tiene"
    grupos ||--o{ personalizaciones : "crea"
    actividades ||--o{ personalizaciones : "recibe"
"""


def build_diagrams_json():
    """Return all diagram codes + status as JSON for live polling."""
    status = scan_all()
    return json.dumps({
        "nivel1": mermaid_level1(),
        "nivel2": mermaid_level2(),
        "nivel3": mermaid_level3(),
        "nivel4": mermaid_level4(status),
        "database": mermaid_database(),
        "status": status,
        "hash": hashlib.md5(json.dumps(status, sort_keys=True).encode()).hexdigest()[:8],
    }, ensure_ascii=False)


HTML_FILE = PROJECT / "web" / "index.html"


def load_html_template():
    """Lee el HTML desde disco en cada request (hot reload)."""
    return HTML_FILE.read_text(encoding="utf-8")


def get_tool_sources():
    """Lee tools.py y extrae el código fuente de cada clase tool."""
    tools_file = PROJECT / "scripts" / "crewai" / "tools.py"
    if not tools_file.exists():
        return {}
    text = tools_file.read_text(encoding="utf-8")
    parts = re.split(r"(?=^class \w+\(BaseTool\))", text, flags=re.MULTILINE)
    result = {}
    for part in parts:
        m = re.search(r'name:\s*str\s*=\s*["\'](\w+)["\']', part)
        if m:
            result[m.group(1)] = part.strip()
    return result


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
                          json.dumps({"version": SERVER_VERSION}))
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
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_tool_sources(), ensure_ascii=False))
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
