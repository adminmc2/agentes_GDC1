#!/usr/bin/env python3
"""
Evaluación automática de tarjetas de vocabulario.

Dos modos de uso:
  1. Evaluar tarjetas ya en BD:  python eval/evaluar_tarjetas.py --unidad 3
  2. Evaluar + guardar resultado: python eval/evaluar_tarjetas.py --unidad 3 --modelo groq/openai/gpt-oss-120b

Los resultados se guardan en la tabla `evaluaciones` y son visibles en la web de gestión.
"""

import json
import os
import re
import sys
import unicodedata

import psycopg2
from psycopg2.extras import Json, RealDictCursor

# Añadir raíz del proyecto al path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from dotenv import load_dotenv
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

DATABASE_URL = os.environ.get("DATABASE_URL")


def _db():
    return psycopg2.connect(DATABASE_URL)


def crear_tabla_evaluaciones():
    """Crea la tabla evaluaciones si no existe."""
    conn = _db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS evaluaciones (
            id SERIAL PRIMARY KEY,
            run_id TEXT NOT NULL,
            unidad INT NOT NULL,
            modelo TEXT NOT NULL DEFAULT 'desconocido',
            prompt_version TEXT DEFAULT 'v1',
            total_tarjetas INT DEFAULT 0,
            metricas JSONB DEFAULT '{}',
            duracion_s FLOAT DEFAULT 0,
            tokens_input INT DEFAULT 0,
            tokens_output INT DEFAULT 0,
            coste_usd FLOAT DEFAULT 0,
            fecha TIMESTAMPTZ DEFAULT NOW()
        );
    """)
    conn.commit()
    conn.close()
    print("[BD] Tabla evaluaciones verificada/creada.")


def obtener_tarjetas(unidad):
    """Obtiene las tarjetas de una unidad desde la BD."""
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT t.* FROM tarjetas_vocabulario t
        JOIN unidades u ON t.unidad_id = u.id
        WHERE u.numero = %s
        ORDER BY t.palabra
    """, (unidad,))
    tarjetas = [dict(r) for r in cur.fetchall()]
    conn.close()
    return tarjetas


# ==========================================================================
#  MÉTRICAS RULE-BASED (gratuitas, deterministas, instantáneas)
# ==========================================================================

def tiene_tilde(texto):
    """Verifica si el texto contiene alguna vocal con tilde."""
    return bool(re.search(r'[áéíóúÁÉÍÓÚ]', texto or ""))


def es_plural_no_deseado(palabra):
    """Detecta si una palabra parece ser un plural innecesario.
    Regla: si termina en -os/-as/-es y existe la forma singular natural,
    probablemente es un plural no deseado (queremos 'abuelo', no 'abuelos').
    Excepción: palabras que solo existen en plural (gafas, tijeras, etc.)
    """
    PLURALES_VALIDOS = {
        "gafas", "tijeras", "pantalones", "vacaciones", "padres",
        "deberes", "matemáticas", "ciencias",
    }
    p = (palabra or "").lower().strip()
    if p in PLURALES_VALIDOS:
        return False
    if p.endswith("os") or p.endswith("as"):
        return True
    if p.endswith("es") and len(p) > 4:
        return True
    return False


def evaluar_silaba_tonica(silaba):
    """Verifica formato correcto de sílaba tónica: sin guiones, tónica en MAYÚSCULAS.
    Correcto: aBUElo, herMAno
    Incorrecto: a-BUE-lo, ABUELO, abuelo
    """
    s = (silaba or "").strip()
    if not s:
        return {"ok": False, "error": "vacío"}
    if "-" in s:
        return {"ok": False, "error": "contiene guiones"}
    # Debe tener al menos una mayúscula y al menos una minúscula
    if not re.search(r'[A-ZÁÉÍÓÚ]', s):
        return {"ok": False, "error": "sin mayúsculas (no marca tónica)"}
    if not re.search(r'[a-záéíóú]', s):
        return {"ok": False, "error": "todo mayúsculas"}
    return {"ok": True, "error": None}


def evaluar_combos(combos):
    """Evalúa los combos de una tarjeta.
    Reglas: exactamente 4, sin repetidos, no vacíos.
    """
    if not combos or not isinstance(combos, list):
        return {"ok": False, "count": 0, "repetidos": 0, "vacios": 0}
    vacios = sum(1 for c in combos if not (c or "").strip())
    unicos = set(c.lower().strip() for c in combos if c)
    repetidos = len([c for c in combos if c]) - len(unicos)
    return {
        "ok": len(combos) == 4 and vacios == 0 and repetidos == 0,
        "count": len(combos),
        "repetidos": repetidos,
        "vacios": vacios,
    }


def evaluar_traducciones(tarjeta):
    """Verifica que las 7 traducciones estén presentes."""
    IDIOMAS = ["trad_it", "trad_fr", "trad_pt_br", "trad_en", "trad_cs", "trad_pl", "trad_tr"]
    presentes = sum(1 for i in IDIOMAS if (tarjeta.get(i) or "").strip())
    vacias = [i.replace("trad_", "").upper() for i in IDIOMAS if not (tarjeta.get(i) or "").strip()]
    return {
        "ok": presentes == 7,
        "presentes": presentes,
        "total": 7,
        "vacias": vacias,
    }


def evaluar_regla(regla):
    """Verifica que la regla morfológica tenga formato adecuado.
    Debe ser concisa y describir el patrón (ej: 'M en -o, F en -a').
    """
    r = (regla or "").strip()
    if not r:
        return {"ok": False, "error": "vacía"}
    if len(r) > 100:
        return {"ok": False, "error": "demasiado larga (>100 chars)"}
    return {"ok": True, "error": None}


# ==========================================================================
#  EVALUACIÓN COMPLETA
# ==========================================================================

def evaluar_tarjetas(tarjetas):
    """Ejecuta todas las métricas sobre un conjunto de tarjetas.
    Devuelve un diccionario con métricas agregadas y detalle por tarjeta.
    """
    n = len(tarjetas)
    if n == 0:
        return {"total": 0, "error": "No hay tarjetas para evaluar"}

    # Contadores
    plurales = 0
    silabas_ok = 0
    silabas_con_guiones = 0
    silabas_vacias = 0
    combos_ok = 0
    combos_no_4 = 0
    combos_repetidos = 0
    traducciones_completas = 0
    traducciones_parciales = 0
    reglas_ok = 0
    reglas_vacias = 0
    niveles = {1: 0, 2: 0, 3: 0}
    campos_semanticos = set()
    errores_detalle = []

    for t in tarjetas:
        palabra = t.get("palabra", "")

        # Plurales
        if es_plural_no_deseado(palabra):
            plurales += 1
            errores_detalle.append({"palabra": palabra, "tipo": "plural", "detalle": f"'{palabra}' parece plural"})

        # Sílaba tónica
        sil = evaluar_silaba_tonica(t.get("silaba_tonica"))
        if sil["ok"]:
            silabas_ok += 1
        else:
            if sil["error"] == "contiene guiones":
                silabas_con_guiones += 1
            elif sil["error"] == "vacío":
                silabas_vacias += 1
            errores_detalle.append({"palabra": palabra, "tipo": "silaba", "detalle": sil["error"]})

        # Combos
        combo_eval = evaluar_combos(t.get("combos"))
        if combo_eval["ok"]:
            combos_ok += 1
        else:
            if combo_eval["count"] != 4:
                combos_no_4 += 1
            if combo_eval["repetidos"] > 0:
                combos_repetidos += 1
            errores_detalle.append({"palabra": palabra, "tipo": "combo", "detalle": f"combos={combo_eval['count']}, rep={combo_eval['repetidos']}"})

        # Traducciones
        trad = evaluar_traducciones(t)
        if trad["ok"]:
            traducciones_completas += 1
        else:
            traducciones_parciales += 1
            errores_detalle.append({"palabra": palabra, "tipo": "traduccion", "detalle": f"faltan: {', '.join(trad['vacias'])}"})

        # Regla
        regla = evaluar_regla(t.get("regla"))
        if regla["ok"]:
            reglas_ok += 1
        else:
            reglas_vacias += 1

        # Niveles
        nivel = t.get("nivel_jerarquia", 1)
        niveles[nivel] = niveles.get(nivel, 0) + 1

        # Campos semánticos
        cs = t.get("campo_semantico", "")
        if cs:
            campos_semanticos.add(cs)

    # Calcular scores (0-100)
    score_plurales = round(100 * (1 - plurales / n), 1)
    score_silabas = round(100 * silabas_ok / n, 1)
    score_combos = round(100 * combos_ok / n, 1)
    score_traducciones = round(100 * traducciones_completas / n, 1)
    score_reglas = round(100 * reglas_ok / n, 1)

    # Score global (media ponderada)
    score_global = round(
        0.25 * score_plurales +
        0.20 * score_silabas +
        0.20 * score_combos +
        0.20 * score_traducciones +
        0.15 * score_reglas,
        1,
    )

    return {
        "total": n,
        "score_global": score_global,
        "scores": {
            "sin_plurales": score_plurales,
            "silabas_correctas": score_silabas,
            "combos_correctos": score_combos,
            "traducciones_completas": score_traducciones,
            "reglas_correctas": score_reglas,
        },
        "contadores": {
            "plurales": plurales,
            "silabas_ok": silabas_ok,
            "silabas_con_guiones": silabas_con_guiones,
            "silabas_vacias": silabas_vacias,
            "combos_ok": combos_ok,
            "combos_no_4": combos_no_4,
            "combos_repetidos": combos_repetidos,
            "traducciones_completas": traducciones_completas,
            "traducciones_parciales": traducciones_parciales,
            "reglas_ok": reglas_ok,
            "reglas_vacias": reglas_vacias,
        },
        "niveles": niveles,
        "campos_semanticos": sorted(campos_semanticos),
        "errores": errores_detalle[:50],  # Limitar a 50 para la web
    }


def guardar_evaluacion(unidad, modelo, metricas, run_id=None, duracion=0,
                       tokens_in=0, tokens_out=0, coste=0, prompt_version="v1"):
    """Guarda el resultado de una evaluación en la BD."""
    if run_id is None:
        import uuid
        run_id = str(uuid.uuid4())[:8]

    conn = _db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO evaluaciones (run_id, unidad, modelo, prompt_version,
                                  total_tarjetas, metricas, duracion_s,
                                  tokens_input, tokens_output, coste_usd)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (
        run_id, unidad, modelo, prompt_version,
        metricas["total"], Json(metricas), duracion,
        tokens_in, tokens_out, coste,
    ))
    eval_id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return eval_id


def obtener_evaluaciones(unidad=None, limit=50):
    """Obtiene el historial de evaluaciones."""
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    if unidad:
        cur.execute("""
            SELECT * FROM evaluaciones WHERE unidad = %s
            ORDER BY fecha DESC LIMIT %s
        """, (unidad, limit))
    else:
        cur.execute("""
            SELECT * FROM evaluaciones ORDER BY fecha DESC LIMIT %s
        """, (limit,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


# ==========================================================================
#  MAIN — ejecución desde terminal
# ==========================================================================

def print_report(metricas):
    """Imprime un informe visual en terminal."""
    print(f"\n{'='*60}")
    print(f"  EVALUACIÓN DE TARJETAS")
    print(f"{'='*60}")
    print(f"\n  Total tarjetas: {metricas['total']}")
    print(f"  Score global:   {metricas['score_global']}/100")
    print()

    scores = metricas["scores"]
    bar_width = 30
    for name, score in scores.items():
        filled = int(bar_width * score / 100)
        bar = "█" * filled + "░" * (bar_width - filled)
        color = "\033[92m" if score >= 80 else "\033[93m" if score >= 60 else "\033[91m"
        print(f"  {name:.<30s} {color}{bar} {score}%\033[0m")

    cont = metricas["contadores"]
    print(f"\n  Detalle:")
    print(f"    Plurales no deseados:     {cont['plurales']}")
    print(f"    Sílabas con guiones:      {cont['silabas_con_guiones']}")
    print(f"    Combos ≠ 4:               {cont['combos_no_4']}")
    print(f"    Combos repetidos:         {cont['combos_repetidos']}")
    print(f"    Traducciones incompletas: {cont['traducciones_parciales']}")
    print(f"    Reglas vacías:            {cont['reglas_vacias']}")

    niveles = metricas["niveles"]
    print(f"\n  Niveles: N1={niveles.get(1,0)} N2={niveles.get(2,0)} N3={niveles.get(3,0)}")
    print(f"  Campos semánticos: {', '.join(metricas['campos_semanticos'])}")

    if metricas["errores"]:
        print(f"\n  Primeros errores detectados:")
        for e in metricas["errores"][:10]:
            print(f"    [{e['tipo']}] {e['palabra']}: {e['detalle']}")

    print(f"\n{'='*60}\n")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Evaluar tarjetas de vocabulario")
    parser.add_argument("--unidad", type=int, default=3, help="Número de unidad")
    parser.add_argument("--modelo", type=str, default=None, help="Nombre del modelo (para guardar en BD)")
    parser.add_argument("--guardar", action="store_true", help="Guardar resultado en BD")
    parser.add_argument("--json", action="store_true", help="Output en JSON")
    args = parser.parse_args()

    # Asegurar que existe la tabla
    crear_tabla_evaluaciones()

    # Obtener tarjetas
    tarjetas = obtener_tarjetas(args.unidad)
    if not tarjetas:
        print(f"No hay tarjetas para U{args.unidad:02d}")
        sys.exit(1)

    # Evaluar
    metricas = evaluar_tarjetas(tarjetas)

    if args.json:
        print(json.dumps(metricas, ensure_ascii=False, indent=2, default=str))
    else:
        print_report(metricas)

    # Guardar en BD
    if args.guardar or args.modelo:
        modelo = args.modelo or "desconocido"
        eval_id = guardar_evaluacion(args.unidad, modelo, metricas)
        print(f"Evaluación guardada en BD con id={eval_id}")


if __name__ == "__main__":
    main()
