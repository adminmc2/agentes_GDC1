"""
Wrapper de promptfoo para el agente Recurvo de CrewAI.
promptfoo lo llama como script: python provider_crewai.py <prompt> <config_json>
Devuelve JSON a stdout con el resultado.
"""

import json
import os
import sys

# Add project paths
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts", "crewai"))

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

import psycopg2
from psycopg2.extras import RealDictCursor

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_DU3EHycC7KhT@ep-floral-unit-anln8vly.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require",
)


def limpiar_tarjetas(unidad):
    """Elimina tarjetas previas para empezar limpio."""
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM tarjetas_vocabulario
        WHERE unidad_id = (SELECT id FROM unidades WHERE numero = %s)
    """, (unidad,))
    conn.commit()
    conn.close()


def contar_tarjetas(unidad):
    """Cuenta tarjetas y devuelve métricas de calidad."""
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT t.palabra, t.genero, t.silaba_tonica, t.regla,
               t.campo_semantico, t.combos, t.frecuencia,
               t.trad_it, t.trad_fr, t.trad_pt_br, t.trad_en,
               t.trad_cs, t.trad_pl, t.trad_tr,
               t.nivel_jerarquia, t.estado
        FROM tarjetas_vocabulario t
        JOIN unidades u ON t.unidad_id = u.id
        WHERE u.numero = %s
        ORDER BY t.nivel_jerarquia, t.palabra
    """, (unidad,))
    tarjetas = [dict(r) for r in cur.fetchall()]
    conn.close()

    # Métricas de calidad
    total = len(tarjetas)
    plurales = [t for t in tarjetas if t["palabra"].endswith("s") and t["palabra"] not in ("padres",) and any(
        t2["palabra"] == t["palabra"].rstrip("s") or t2["palabra"] == t["palabra"].rstrip("as") + "a" or t2["palabra"] == t["palabra"].rstrip("os") + "o"
        for t2 in tarjetas
    )]
    nivel1 = [t for t in tarjetas if t["nivel_jerarquia"] == 1]
    nivel2 = [t for t in tarjetas if t["nivel_jerarquia"] == 2]
    nivel3 = [t for t in tarjetas if t["nivel_jerarquia"] == 3]

    # Check combos: are they varied or all "mi X, tu X"?
    combos_repetitivos = 0
    for t in tarjetas:
        c = t.get("combos") or []
        if len(c) >= 3:
            posesivos = sum(1 for x in c if x.startswith(("mi ", "tu ", "su ", "el ", "la ", "mis ", "tus ")))
            if posesivos >= 3:
                combos_repetitivos += 1

    # Check traducciones: are all 7 present?
    trad_campos = ["trad_it", "trad_fr", "trad_pt_br", "trad_en", "trad_cs", "trad_pl", "trad_tr"]
    trad_vacias = sum(1 for t in tarjetas for c in trad_campos if not t.get(c))

    return {
        "total_tarjetas": total,
        "nivel_1": len(nivel1),
        "nivel_2": len(nivel2),
        "nivel_3": len(nivel3),
        "plurales_detectados": len(plurales),
        "combos_repetitivos": combos_repetitivos,
        "traducciones_vacias": trad_vacias,
        "palabras": [t["palabra"] for t in tarjetas],
        "tarjetas": tarjetas,
    }


def ejecutar_agente(model, prompt_text, unidad=3):
    """Ejecuta el agente CrewAI con el modelo y prompt dados."""
    from crewai import Agent, Task, Crew, Process, LLM
    from tools import (
        ConsultarInventario, ConsultarTarjetasPrevias,
        ConsultarCorrecciones, EscribirTarjetas, ExportarCSV,
    )

    llm = LLM(model=model, max_tokens=8192)

    tools_lectura = [ConsultarInventario(), ConsultarTarjetasPrevias(), ConsultarCorrecciones()]
    tools_escritura = [EscribirTarjetas(), ExportarCSV()]

    generador = Agent(
        name="recurvo_generador",
        role="Extractor y generador de tarjetas de vocabulario",
        goal="Consultar la BD, extraer vocabulario y generar tarjetas estandarizadas.",
        backstory=prompt_text,
        tools=tools_lectura,
        llm=llm,
        verbose=False,
        max_iter=10,
    )

    escritor = Agent(
        name="recurvo_escritor",
        role="Escritor de tarjetas en base de datos",
        goal="Recibir tarjetas y escribirlas en la BD, luego exportar CSV.",
        backstory="Agente técnico. Solo ejecuta escribir_tarjetas y exportar_csv. No genera contenido.",
        tools=tools_escritura,
        llm=llm,
        verbose=False,
        max_iter=5,
    )

    tarea_generar = Task(
        description=f"""Genera tarjetas de vocabulario para la Unidad {unidad}.
PROCESO: 1) consultar_inventario unidad={unidad} 2) consultar_tarjetas_previas unidad={unidad}
3) consultar_correcciones 4) Clasificar en niveles 1/2/3 5) Generar tarjetas con 24 campos.
REGLAS: Solo formas genéricas (singular M y F), nunca plurales. Sílaba tónica en MAYÚSCULAS sin guiones ni tildes inventadas.
Regla formato: "M en -o, F en -a: abuel-o / abuel-a". Combos: 4 chunks léxicos variados (no solo posesivos).""",
        expected_output="JSON array con tarjetas generadas, cada una con 24 campos.",
        agent=generador,
    )

    tarea_escribir = Task(
        description=f"""Ejecuta escribir_tarjetas con el JSON de tarjetas recibido. Luego ejecuta exportar_csv con unidad={unidad}.""",
        expected_output="Confirmación de tarjetas insertadas y CSV exportado.",
        agent=escritor,
        context=[tarea_generar],
    )

    crew = Crew(
        agents=[generador, escritor],
        tasks=[tarea_generar, tarea_escribir],
        process=Process.sequential,
        verbose=False,
        memory=False,
    )

    resultado = crew.kickoff()
    return str(resultado)


def main():
    """Entry point para promptfoo."""
    prompt = sys.argv[1] if len(sys.argv) > 1 else ""
    config = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}

    model = config.get("model", "groq/openai/gpt-oss-120b")
    unidad = config.get("unidad", 3)

    # Limpiar BD antes de cada ejecución
    limpiar_tarjetas(unidad)

    try:
        # Ejecutar agente
        raw_output = ejecutar_agente(model, prompt, unidad)

        # Medir calidad
        metricas = contar_tarjetas(unidad)

        output = {
            "output": json.dumps(metricas, ensure_ascii=False, default=str),
            "metadata": {
                "model": model,
                "total_tarjetas": metricas["total_tarjetas"],
                "nivel_1": metricas["nivel_1"],
                "nivel_2": metricas["nivel_2"],
                "nivel_3": metricas["nivel_3"],
                "plurales": metricas["plurales_detectados"],
                "combos_repetitivos": metricas["combos_repetitivos"],
                "trad_vacias": metricas["traducciones_vacias"],
            }
        }
    except Exception as e:
        output = {"output": f"ERROR: {e}", "error": str(e)}

    print(json.dumps(output))


if __name__ == "__main__":
    main()
