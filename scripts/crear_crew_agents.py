#!/usr/bin/env python3
"""
Crea la tabla crew_agents en Neon y la puebla con los 3 agentes de Recurvo.
Idempotente: usa ON CONFLICT DO UPDATE.
"""
import os
import sys
from pathlib import Path

# Load .env from project root
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent.parent / ".env")

import psycopg2

CREATE_SQL = """
CREATE TABLE IF NOT EXISTS crew_agents (
    id            SERIAL PRIMARY KEY,
    crew          VARCHAR(50) NOT NULL,
    agent_key     VARCHAR(50) NOT NULL,
    agent_order   INTEGER     NOT NULL,
    role          TEXT        NOT NULL,
    goal          TEXT        NOT NULL,
    backstory     TEXT        NOT NULL,
    task_description      TEXT NOT NULL,
    task_expected_output  TEXT NOT NULL,
    max_iter      INTEGER DEFAULT 10,
    updated_at    TIMESTAMP DEFAULT NOW(),
    UNIQUE(crew, agent_key)
);
"""

# task_description uses {unidad} as a runtime template placeholder.
# recurvo.py will call .format(unidad=N) before passing to Task().
AGENTS = [
    {
        "crew": "recurvo",
        "agent_key": "generador",
        "agent_order": 1,
        "role": "Vocabulary card extractor and generator",
        "goal": (
            "Generate accurate, error-free vocabulary cards from activity inventories, "
            "incorporating prior human corrections to avoid repeating mistakes."
        ),
        "backstory": (
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
        "task_description": (
            'Generate vocabulary cards for Unit {unidad} of "Nuevo Companeros 1".\n'
            'All card content MUST be in Spanish (es-ES). Instructions here are in English.\n\n'
            'MANDATORY PROCESS (follow these steps in order):\n\n'
            '1. QUERY INVENTORY: Use consultar_inventario with unidad={unidad}.\n'
            '   Read contenidos_indice to identify the main semantic field ("vocabulario" key).\n'
            '   Read all activities to extract vocabulary items.\n\n'
            '2. QUERY PREVIOUS CARDS: Use consultar_tarjetas_previas with unidad={unidad}.\n'
            '   If cards exist from earlier units, mark them as reutilizada.\n\n'
            '3. QUERY CORRECTIONS: Use consultar_correcciones.\n'
            '   If prior corrections exist, DO NOT repeat those errors.\n\n'
            '4. CLASSIFY VOCABULARY into 3 levels:\n'
            '   - Level 1: Words from the main semantic field in the index -> MANDATORY\n'
            '   - Level 2: Words from secondary fields (by frequency in activities) -> PROPOSED\n'
            '   - Level 3: Isolated difficult words -> PROPOSED\n'
            '   - Identify multi-word expressions: "hermano menor" = 1 card, NOT 2\n\n'
            '5. GENERATE CARDS with ALL these fields per word:\n'
            '   palabra, genero (M/F), color_genero (azul/rojo), silaba_tonica (no hyphens, stressed syllable in UPPERCASE),\n'
            '   regla, campo_semantico, color_campo, ejemplo, frecuencia (1-3), irregularidad,\n'
            '   combos (EXACTLY 4), trad_it, trad_fr, trad_pt_br, trad_en, trad_cs, trad_pl, trad_tr,\n'
            '   seccion, pagina, nivel_jerarquia (1/2/3), estado (nueva/reutilizada),\n'
            '   unidad_origen ({unidad} for new cards), unidad ({unidad}).\n\n'
            'CRITICAL RULES:\n'
            '- Stressed syllables: NO hyphens. Correct: aBUElo. Wrong: a-BUE-lo.\n'
            '- Combos: always exactly 4 per card.\n'
            '- Multi-word expressions: "hermano menor", "hermano mayor" -> 1 card each.'
        ),
        "task_expected_output": (
            'A JSON array with all generated cards. Each card is an object with 24 fields.\n'
            'Example card:\n'
            '{"palabra": "abuelo", "genero": "M", "color_genero": "azul", "silaba_tonica": "aBUElo",\n'
            '  "regla": "M en -o, F en -a", "campo_semantico": "Parentesco", "color_campo": "violeta",\n'
            '  "ejemplo": "Mi abuelo vive en Madrid.", "frecuencia": 3, "irregularidad": "",\n'
            '  "combos": ["mi abuelo", "tu abuelo", "el abuelo de", "abuelo materno"],\n'
            '  "trad_it": "nonno", "trad_fr": "grand-pere", "trad_pt_br": "avo", "trad_en": "grandfather",\n'
            '  "trad_cs": "dedecek", "trad_pl": "dziadek", "trad_tr": "buyukbaba",\n'
            '  "seccion": "vocabulario", "pagina": 34, "nivel_jerarquia": 1,\n'
            '  "estado": "nueva", "unidad_origen": 3, "unidad": 3}'
        ),
        "max_iter": 10,
    },
    {
        "crew": "recurvo",
        "agent_key": "verificador",
        "agent_order": 2,
        "role": "Vocabulary card quality verifier",
        "goal": (
            "Verify every generated card against the source inventory and linguistic rules, "
            "correcting errors before cards reach the database."
        ),
        "backstory": (
            "You are a quality control specialist for printed educational materials. "
            "You receive a JSON array of vocabulary cards and the original activity inventory, "
            "then systematically check each card for factual and linguistic errors. "
            "You do not generate new cards — you only validate and correct what you receive. "
            "Your corrections prevent costly reprinting errors."
        ),
        "task_description": (
            'Verify the vocabulary cards generated in the previous step against the source inventory.\n'
            'You receive a JSON array of cards. Use consultar_inventario with unidad={unidad} to get the source data.\n\n'
            'CHECK EACH CARD for these errors:\n\n'
            '1. TRANSLATIONS: Verify all 7 translations are present and non-empty.\n'
            '2. STRESSED SYLLABLE: Must contain exactly one UPPERCASE syllable, no hyphens.\n'
            '   Correct: aBUElo, faMIlia. Wrong: a-BUE-lo, ABUELO, abuelo.\n'
            '3. GENDER: Must be M or F. Verify against standard Spanish gender rules.\n'
            '   Words ending in -o are typically M, words ending in -a are typically F.\n'
            '   Flag exceptions that may be wrong (e.g., "el dia" = M despite -a ending).\n'
            '4. COMBOS: Each card must have exactly 4 frequent combinations.\n'
            '   Verify they are natural collocations in Spanish, not invented.\n'
            '5. EXAMPLE SENTENCE: Must be a natural Spanish sentence at A1 level.\n'
            '6. SEMANTIC FIELD: Must match what contenidos_indice says for this unit.\n'
            '7. DUPLICATES: No two cards should have the same palabra value.\n\n'
            'OUTPUT: Return the CORRECTED JSON array. If a card has errors, fix them in place.\n'
            'Add a "_verificacion" field to each card:\n'
            '- "_verificacion": "ok" if no changes were needed\n'
            '- "_verificacion": "corregido: [what was fixed]" if corrections were made\n\n'
            'Do NOT remove cards. Do NOT add new cards. Only correct existing ones.'
        ),
        "task_expected_output": (
            'The same JSON array of cards, with corrections applied and _verificacion field added.\n'
            'Example: {"palabra": "abuelo", ..., "_verificacion": "ok"}\n'
            'Example: {"palabra": "dia", "genero": "M", ..., "_verificacion": "corregido: genero cambiado de F a M"}'
        ),
        "max_iter": 8,
    },
    {
        "crew": "recurvo",
        "agent_key": "escritor",
        "agent_order": 3,
        "role": "Database card writer and CSV exporter",
        "goal": (
            "Persist verified vocabulary cards to the database and export them "
            "as a CSV file ready for InDesign import."
        ),
        "backstory": (
            "You are a technical agent. Your ONLY job is to take the cards passed to you "
            "and execute two tools: escribir_tarjetas to save to the database, "
            "and exportar_csv to generate the CSV file. You do not generate content, "
            "you only write what you receive."
        ),
        "task_description": (
            'Your ONLY job is to execute two tools with the data you receive from the previous step.\n\n'
            'STEP 1: Call escribir_tarjetas.\n'
            '- Parameter name: tarjetas_json.\n'
            '- Value: the COMPLETE JSON array of verified cards from the previous step.\n'
            '- Remove the _verificacion field from each card before writing.\n\n'
            'STEP 2: Call exportar_csv with unidad={unidad}.\n\n'
            'Do NOT generate new content. Do NOT modify card data. Only execute the two tools.'
        ),
        "task_expected_output": (
            'Confirmation with the number of cards inserted and CSV path.\n'
            'Example: {"insertadas": 20, "csv": "datos/tarjetas/U{unidad:02d}-vocabulario.csv"}'
        ),
        "max_iter": 5,
    },
]

INSERT_SQL = """
INSERT INTO crew_agents
    (crew, agent_key, agent_order, role, goal, backstory,
     task_description, task_expected_output, max_iter)
VALUES
    (%(crew)s, %(agent_key)s, %(agent_order)s, %(role)s, %(goal)s, %(backstory)s,
     %(task_description)s, %(task_expected_output)s, %(max_iter)s)
ON CONFLICT (crew, agent_key) DO UPDATE SET
    agent_order          = EXCLUDED.agent_order,
    role                 = EXCLUDED.role,
    goal                 = EXCLUDED.goal,
    backstory            = EXCLUDED.backstory,
    task_description     = EXCLUDED.task_description,
    task_expected_output = EXCLUDED.task_expected_output,
    max_iter             = EXCLUDED.max_iter,
    updated_at           = NOW();
"""


def main():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        print("ERROR: DATABASE_URL no encontrado en .env", file=sys.stderr)
        sys.exit(1)

    conn = psycopg2.connect(db_url)
    cur = conn.cursor()

    cur.execute(CREATE_SQL)
    print("✓ Tabla crew_agents creada (o ya existia)")

    for agent in AGENTS:
        cur.execute(INSERT_SQL, agent)
        print(f"✓ {agent['crew']}/{agent['agent_key']} (orden {agent['agent_order']}, max_iter={agent['max_iter']})")

    conn.commit()

    print("\n--- Verificacion ---")
    cur.execute(
        "SELECT crew, agent_key, agent_order, role, max_iter, "
        "LENGTH(task_description) AS td_len, LENGTH(backstory) AS bs_len "
        "FROM crew_agents ORDER BY crew, agent_order"
    )
    for r in cur.fetchall():
        print(f"  [{r[0]}/{r[1]}] orden={r[2]} max_iter={r[4]} "
              f"task_desc={r[5]}c backstory={r[6]}c  role: {r[3]}")

    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    main()
