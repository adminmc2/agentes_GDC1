#!/usr/bin/env python3
"""
Crew Recurvo — Vocabulary card generation pipeline.
Run with: python scripts/crewai/recurvo.py [unidad]

Architecture: 3 sequential tasks, each with its own agent and LLM.
  Task 1 (Generator):  reads BD → produces JSON array of cards
  Task 2 (Verifier):   validates cards against source data → corrected JSON
  Task 3 (Writer):     persists cards to BD + exports CSV
"""

import json
import os
import sys
import time

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, Process, LLM
from tools import (
    ConsultarInventario,
    ConsultarTarjetasPrevias,
    ConsultarCorrecciones,
    EscribirTarjetas,
    ExportarCSV,
)

# --- Langfuse (trazabilidad via litellm callback) ---
# litellm intercepta cada llamada LLM que CrewAI hace y la envía a Langfuse.
# Se activa automáticamente si LANGFUSE_PUBLIC_KEY está en .env.
# Requiere langfuse 2.x (litellm 1.82.2 no es compatible con langfuse 3.x/4.x).
if os.environ.get("LANGFUSE_PUBLIC_KEY"):
    import litellm
    litellm.success_callback = ["langfuse"]
    litellm.failure_callback = ["langfuse"]
    print("[Langfuse] Trazabilidad ACTIVA — cada llamada LLM se registra en cloud.langfuse.com")
else:
    print("[Langfuse] No configurado — ejecutando sin trazabilidad")

# --- LLMs (one per agent, each with its own model + params) ---
LLM_CFG = {
    "gen": {
        "model": os.environ.get("RECURVO_LLM_GEN",
                                os.environ.get("RECURVO_LLM", "groq/openai/gpt-oss-120b")),
        "max_tokens": int(os.environ.get("RECURVO_MAXTOK_GEN", "8192")),
        "temperature": float(os.environ.get("RECURVO_TEMP_GEN", "0.7")),
        "top_p": float(os.environ.get("RECURVO_TOPP_GEN", "1.0")),
    },
    "ver": {
        "model": os.environ.get("RECURVO_LLM_VER", "groq/llama-3.3-70b-versatile"),
        "max_tokens": int(os.environ.get("RECURVO_MAXTOK_VER", "8192")),
        "temperature": float(os.environ.get("RECURVO_TEMP_VER", "0.2")),
        "top_p": float(os.environ.get("RECURVO_TOPP_VER", "1.0")),
    },
    "wr": {
        "model": os.environ.get("RECURVO_LLM_WR", "groq/llama-3.1-8b-instant"),
        "max_tokens": int(os.environ.get("RECURVO_MAXTOK_WR", "2048")),
        "temperature": float(os.environ.get("RECURVO_TEMP_WR", "0.0")),
        "top_p": float(os.environ.get("RECURVO_TOPP_WR", "1.0")),
    },
}

llm_gen = LLM(**LLM_CFG["gen"])
llm_ver = LLM(**LLM_CFG["ver"])
llm_wr  = LLM(**LLM_CFG["wr"])

# --- Tools by function ---
tools_lectura = [
    ConsultarInventario(),
    ConsultarTarjetasPrevias(),
    ConsultarCorrecciones(),
]

tools_verificacion = [
    ConsultarInventario(),
]

tools_escritura = [
    EscribirTarjetas(),
    ExportarCSV(),
]

# --- Agent 1: Generator ---
generador = Agent(
    name="recurvo_generador",
    role="Vocabulary card extractor and generator",
    goal=(
        "Generate accurate, error-free vocabulary cards from activity inventories, "
        "incorporating prior human corrections to avoid repeating mistakes."
    ),
    backstory=(
        "You have deep expertise in applied linguistics for vocabulary instruction "
        "in ELE (Spanish as a Foreign Language), specifically at A1.1 level for "
        "adolescent learners (12-15 years). You understand semantic field theory "
        "and how vocabulary organizes into thematic networks — you classify words "
        "by their primary semantic field (from the unit index) and identify secondary "
        "fields by analyzing word frequency across activities. You have working "
        "knowledge of the Spanish linguistic system relevant to A1 vocabulary: "
        "gender and number rules, stress patterns, word formation, and how words "
        "combine in frequent collocations. Cards are printed editorial material "
        "distributed to students — errors cannot be corrected after printing. "
        "You improve through a human correction feedback loop: each run incorporates "
        "lessons from previously corrected errors to prevent recurrence."
    ),
    tools=tools_lectura,
    llm=llm_gen,
    verbose=True,
    max_iter=10,
)

# --- Agent 2: Verifier ---
verificador = Agent(
    name="recurvo_verificador",
    role="Vocabulary card quality verifier",
    goal=(
        "Verify every generated card against the source inventory and linguistic rules, "
        "correcting errors before cards reach the database."
    ),
    backstory=(
        "You are a quality control specialist for printed educational materials. "
        "You receive a JSON array of vocabulary cards and the original activity inventory, "
        "then systematically check each card for factual and linguistic errors. "
        "You do not generate new cards — you only validate and correct what you receive. "
        "Your corrections prevent costly reprinting errors."
    ),
    tools=tools_verificacion,
    llm=llm_ver,
    verbose=True,
    max_iter=8,
)

# --- Agent 3: Writer ---
escritor = Agent(
    name="recurvo_escritor",
    role="Database card writer and CSV exporter",
    goal=(
        "Persist verified vocabulary cards to the database and export them "
        "as a CSV file ready for InDesign import."
    ),
    backstory=(
        "You are a technical agent. Your ONLY job is to take the cards passed to you "
        "and execute two tools: escribir_tarjetas to save to the database, "
        "and exportar_csv to generate the CSV file. You do not generate content, "
        "you only write what you receive."
    ),
    tools=tools_escritura,
    llm=llm_wr,
    verbose=True,
    max_iter=5,
)


def crear_tareas(unidad: int) -> list[Task]:
    tarea_generar = Task(
        description=f"""
Generate vocabulary cards for Unit {unidad} of "Nuevo Compañeros 1".
All card content MUST be in Spanish (es-ES). Instructions here are in English.

MANDATORY PROCESS (follow these steps in order):

1. QUERY INVENTORY: Use consultar_inventario with unidad={unidad}.
   Read contenidos_indice to identify the main semantic field ("vocabulario" key).
   Read all activities to extract vocabulary items.

2. QUERY PREVIOUS CARDS: Use consultar_tarjetas_previas with unidad={unidad}.
   If cards exist from earlier units, mark them as reutilizada.

3. QUERY CORRECTIONS: Use consultar_correcciones.
   If prior corrections exist, DO NOT repeat those errors.

4. CLASSIFY VOCABULARY into 3 levels:
   - Level 1: Words from the main semantic field in the index → MANDATORY
   - Level 2: Words from secondary fields (by frequency in activities) → PROPOSED
   - Level 3: Isolated difficult words → PROPOSED
   - Identify multi-word expressions: "hermano menor" = 1 card, NOT 2

5. GENERATE CARDS with ALL these fields per word:
   palabra, genero (M/F), color_genero (azul/rojo), silaba_tonica (no hyphens, stressed syllable in UPPERCASE),
   regla, campo_semantico, color_campo, ejemplo, frecuencia (1-3), irregularidad,
   combos (EXACTLY 4), trad_it, trad_fr, trad_pt_br, trad_en, trad_cs, trad_pl, trad_tr,
   seccion, pagina, nivel_jerarquia (1/2/3), estado (nueva/reutilizada),
   unidad_origen ({unidad} for new cards), unidad ({unidad}).

CRITICAL RULES:
- Stressed syllables: NO hyphens. Correct: aBUElo. Wrong: a-BUE-lo.
- Combos: always exactly 4 per card.
- Multi-word expressions: "hermano menor", "hermano mayor" → 1 card each.
""",
        expected_output="""
A JSON array with all generated cards. Each card is an object with 24 fields.
Example card:
{{"palabra": "abuelo", "genero": "M", "color_genero": "azul", "silaba_tonica": "aBUElo",
  "regla": "M en -o, F en -a", "campo_semantico": "Parentesco", "color_campo": "violeta",
  "ejemplo": "Mi abuelo vive en Madrid.", "frecuencia": 3, "irregularidad": "",
  "combos": ["mi abuelo", "tu abuelo", "el abuelo de", "abuelo materno"],
  "trad_it": "nonno", "trad_fr": "grand-père", "trad_pt_br": "avô", "trad_en": "grandfather",
  "trad_cs": "dědeček", "trad_pl": "dziadek", "trad_tr": "büyükbaba",
  "seccion": "vocabulario", "pagina": 34, "nivel_jerarquia": 1,
  "estado": "nueva", "unidad_origen": 3, "unidad": 3}}
""",
        agent=generador,
    )

    tarea_verificar = Task(
        description=f"""
Verify the vocabulary cards generated in the previous step against the source inventory.
You receive a JSON array of cards. Use consultar_inventario with unidad={unidad} to get the source data.

CHECK EACH CARD for these errors:

1. TRANSLATIONS: Verify all 7 translations are present and non-empty.
2. STRESSED SYLLABLE: Must contain exactly one UPPERCASE syllable, no hyphens.
   Correct: aBUElo, faMIlia. Wrong: a-BUE-lo, ABUELO, abuelo.
3. GENDER: Must be M or F. Verify against standard Spanish gender rules.
   Words ending in -o are typically M, words ending in -a are typically F.
   Flag exceptions that may be wrong (e.g., "el día" = M despite -a ending).
4. COMBOS: Each card must have exactly 4 frequent combinations.
   Verify they are natural collocations in Spanish, not invented.
5. EXAMPLE SENTENCE: Must be a natural Spanish sentence at A1 level.
6. SEMANTIC FIELD: Must match what contenidos_indice says for this unit.
7. DUPLICATES: No two cards should have the same palabra value.

OUTPUT: Return the CORRECTED JSON array. If a card has errors, fix them in place.
Add a "_verificacion" field to each card:
- "_verificacion": "ok" if no changes were needed
- "_verificacion": "corregido: [what was fixed]" if corrections were made

Do NOT remove cards. Do NOT add new cards. Only correct existing ones.
""",
        expected_output="""
The same JSON array of cards, with corrections applied and _verificacion field added.
Example: {{"palabra": "abuelo", ..., "_verificacion": "ok"}}
Example: {{"palabra": "día", "genero": "M", ..., "_verificacion": "corregido: género cambiado de F a M"}}
""",
        agent=verificador,
        context=[tarea_generar],
    )

    tarea_escribir = Task(
        description=f"""
Your ONLY job is to execute two tools with the data you receive from the previous step.

STEP 1: Call escribir_tarjetas.
- Parameter name: tarjetas_json.
- Value: the COMPLETE JSON array of verified cards from the previous step.
- Remove the _verificacion field from each card before writing.

STEP 2: Call exportar_csv with unidad={unidad}.

Do NOT generate new content. Do NOT modify card data. Only execute the two tools.
""",
        expected_output=f"""
Confirmation with the number of cards inserted and CSV path.
Example: {{"insertadas": 20, "csv": "datos/tarjetas/U{unidad:02d}-vocabulario.csv"}}
""",
        agent=escritor,
        context=[tarea_verificar],
    )

    return [tarea_generar, tarea_verificar, tarea_escribir]


def main():
    unidad = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    t0 = time.time()

    def _fmt(cfg):
        return f"{cfg['model']}  temp={cfg['temperature']}  max={cfg['max_tokens']}  top_p={cfg['top_p']}"

    print(f"\n{'='*70}")
    print(f"  CREW RECURVO — Unidad {unidad}")
    print(f"  Generador:   {_fmt(LLM_CFG['gen'])}")
    print(f"  Verificador: {_fmt(LLM_CFG['ver'])}")
    print(f"  Escritor:    {_fmt(LLM_CFG['wr'])}")
    print(f"  Pipeline:    generador → verificador → escritor")
    print(f"{'='*70}\n")

    tareas = crear_tareas(unidad)
    crew = Crew(
        agents=[generador, verificador, escritor],
        tasks=tareas,
        process=Process.sequential,
        verbose=True,
        memory=False,
    )

    resultado = crew.kickoff()
    duracion = time.time() - t0

    print(f"\n{'='*60}")
    print("  RESULTADO")
    print(f"{'='*60}")
    print(resultado)

    # Save raw output
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "datos", "tarjetas",
    )
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"U{unidad:02d}-recurvo-output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(resultado))
    print(f"\nOutput guardado en: {output_path}")
    print(f"Duración: {duracion:.1f}s")

    print("[Langfuse] Trazas enviadas automáticamente via litellm callback")


if __name__ == "__main__":
    main()
