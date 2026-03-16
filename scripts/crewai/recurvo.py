#!/usr/bin/env python3
"""
Agente Recurvo — Extractor y generador de tarjetas de vocabulario.
Fase 1 (Recursos). Ejecutar con: python scripts/crewai/recurvo.py [unidad]

Arquitectura de 2 tareas secuenciales:
  Tarea 1 (generador): consulta BD + genera tarjetas JSON
  Tarea 2 (escritor):  recibe tarjetas + escribe en BD + exporta CSV
"""

import json
import os
import sys

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

# --- LLM ---
LLM_MODEL = os.environ.get("RECURVO_LLM", "groq/openai/gpt-oss-120b")
llm = LLM(model=LLM_MODEL, max_tokens=8192)

# --- Tools separados por función ---
tools_lectura = [
    ConsultarInventario(),
    ConsultarTarjetasPrevias(),
    ConsultarCorrecciones(),
]

tools_escritura = [
    EscribirTarjetas(),
    ExportarCSV(),
]

# --- Agente 1: Generador ---
generador = Agent(
    name="recurvo_generador",
    role="Extractor y generador de tarjetas de vocabulario",
    goal=(
        "Consultar la base de datos, extraer vocabulario de la unidad indicada "
        "y generar tarjetas estandarizadas con todos los campos requeridos."
    ),
    backstory=(
        "Eres un especialista en lexicología aplicada a ELE A1.1. "
        "Conoces los campos semánticos del nivel, las 7 L1 del aula "
        "(italiano, francés, portugués brasileño, inglés, checo, polaco, turco), "
        "las reglas morfológicas del español (género, número, acentuación) "
        "y el inventario léxico de las unidades previas del curso. "
        "IMPORTANTE: Las tarjetas son material impreso que llega al alumno. "
        "Tolerancia a errores = CERO."
    ),
    tools=tools_lectura,
    llm=llm,
    verbose=True,
    max_iter=10,
)

# --- Agente 2: Escritor ---
escritor = Agent(
    name="recurvo_escritor",
    role="Escritor de tarjetas en base de datos",
    goal=(
        "Recibir tarjetas de vocabulario generadas y escribirlas en la base de datos, "
        "luego exportar el CSV para InDesign."
    ),
    backstory=(
        "Eres un agente técnico. Tu ÚNICO trabajo es tomar las tarjetas que te pasan "
        "y ejecutar dos herramientas: escribir_tarjetas para guardar en BD, "
        "y exportar_csv para generar el archivo CSV. No generas contenido, solo escribes."
    ),
    tools=tools_escritura,
    llm=llm,
    verbose=True,
    max_iter=5,
)


def crear_tareas(unidad: int) -> list[Task]:
    tarea_generar = Task(
        description=f"""
Genera las tarjetas de vocabulario para la Unidad {unidad} del libro "Nuevo Compañeros 1".

PROCESO OBLIGATORIO (sigue estos pasos en orden):

1. CONSULTAR INVENTARIO: Usa consultar_inventario con unidad={unidad}.
   Lee contenidos_indice para identificar el campo semántico principal (campo "vocabulario").
   Lee todas las actividades para extraer vocabulario.

2. CONSULTAR TARJETAS PREVIAS: Usa consultar_tarjetas_previas con unidad={unidad}.
   Si hay tarjetas de unidades anteriores, márcalas como reutilizadas.

3. CONSULTAR CORRECCIONES: Usa consultar_correcciones.
   Si hay correcciones previas, NO repitas esos errores.

4. CLASIFICAR VOCABULARIO en 3 niveles:
   - Nivel 1: Palabras del campo semántico principal del índice → OBLIGATORIAS
   - Nivel 2: Palabras de campos secundarios (por frecuencia en actividades) → PROPUESTAS
   - Nivel 3: Palabras difíciles sueltas → PROPUESTAS
   - Identifica expresiones multipalabra: "hermano menor" = 1 tarjeta, NO 2

5. GENERAR TARJETAS con TODOS estos campos para cada palabra:
   palabra, genero (M/F), color_genero (azul/rojo), silaba_tonica (sin guiones, tónica en MAYÚSCULAS),
   regla, campo_semantico, color_campo, ejemplo, frecuencia (1-3), irregularidad,
   combos (EXACTAMENTE 4), trad_it, trad_fr, trad_pt_br, trad_en, trad_cs, trad_pl, trad_tr,
   seccion, pagina, nivel_jerarquia (1/2/3), estado (nueva/reutilizada),
   unidad_origen ({unidad} para nuevas), unidad ({unidad}).

REGLAS CRÍTICAS:
- Sílabas tónicas: SIN guiones. Ejemplo correcto: aBUElo. Incorrecto: a-BUE-lo.
- Combos: siempre exactamente 4 por tarjeta.
- Expresiones multipalabra: "hermano menor", "hermano mayor" → 1 tarjeta cada una.
""",
        expected_output="""
Un JSON array con todas las tarjetas generadas. Cada tarjeta es un objeto con los 24 campos.
Ejemplo de una tarjeta:
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

    tarea_escribir = Task(
        description=f"""
Tu trabajo es SOLO ejecutar dos herramientas con los datos que recibes del paso anterior.

PASO 1: Llama a escribir_tarjetas.
- El parámetro se llama tarjetas_json.
- Pasa como valor el JSON array COMPLETO de tarjetas que recibiste del paso anterior.
- Es un string JSON con el array de tarjetas.

PASO 2: Llama a exportar_csv con unidad={unidad}.

NO generes contenido nuevo. NO modifiques las tarjetas. Solo ejecuta las dos herramientas.
""",
        expected_output=f"""
Confirmación con el número de tarjetas insertadas y la ruta del CSV exportado.
Ejemplo: {{"insertadas": 20, "csv": "datos/tarjetas/U{unidad:02d}-vocabulario.csv"}}
""",
        agent=escritor,
        context=[tarea_generar],
    )

    return [tarea_generar, tarea_escribir]


def main():
    unidad = int(sys.argv[1]) if len(sys.argv) > 1 else 3

    print(f"\n{'='*60}")
    print(f"  AGENTE RECURVO — Unidad {unidad}")
    print(f"  Modelo: {LLM_MODEL}")
    print(f"  Arquitectura: 2 tareas (generador → escritor)")
    print(f"{'='*60}\n")

    tareas = crear_tareas(unidad)
    crew = Crew(
        agents=[generador, escritor],
        tasks=tareas,
        process=Process.sequential,
        verbose=True,
        memory=False,
    )

    resultado = crew.kickoff()

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


if __name__ == "__main__":
    main()
