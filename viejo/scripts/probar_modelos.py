#!/usr/bin/env python3
"""
Prueba comparativa de 3 modelos LLM para generación de contenido didáctico.
Genera la misma sección (Vocabulario U03) con 3 modelos y guarda los resultados.

Uso: python3 scripts/probar_modelos.py
"""
import json
import os
import time
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(Path(__file__).parent.parent / ".env")

import anthropic
from groq import Groq

# === CONFIGURACIÓN ===
PROJECT = Path(__file__).parent.parent

MODELOS = {
    "claude-sonnet": {
        "provider": "anthropic",
        "model_id": "claude-sonnet-4-6",
        "label": "Claude Sonnet 4.6 (referencia de calidad)",
    },
    "kimi-k2": {
        "provider": "groq",
        "model_id": "moonshotai/kimi-k2-instruct",
        "label": "Kimi K2 (Groq — $1.00/M input)",
    },
    "qwen3-32b": {
        "provider": "groq",
        "model_id": "qwen/qwen3-32b",
        "label": "Qwen 3 32B (Groq — $0.29/M input)",
    },
}

# === CARGAR INPUTS ===

def cargar_prompt_agente():
    """Carga el prompt del agente de vocabulario."""
    return (PROJECT / "agentes" / "ag-vocabulario.md").read_text(encoding="utf-8")

def cargar_repertorio():
    """Carga el repertorio de vocabulario."""
    return (PROJECT / "repertorios" / "vocabulario.md").read_text(encoding="utf-8")

def cargar_inventario_vocabulario():
    """Extrae solo las páginas de vocabulario (34-35) del inventario U03."""
    with open(PROJECT / "datos" / "inventarios" / "U03-inventario.json", encoding="utf-8") as f:
        data = json.load(f)

    vocab_pages = [p for p in data["paginas_detalle"] if p["pagina"] in [34, 35]]

    return json.dumps({
        "unidad": data["unidad"],
        "titulo": data["titulo"],
        "nivel": data["nivel"],
        "contenidos_indice": data["contenidos_indice"],
        "paginas_vocabulario": vocab_pages,
    }, ensure_ascii=False, indent=2)


def construir_mensaje_usuario(repertorio, inventario):
    """Construye el mensaje de usuario con los inputs del agente."""
    return f"""## TAREA

Genera la explotación didáctica completa de la sección de VOCABULARIO de la Unidad 3 ("La Familia").

## INVENTARIO DE ACTIVIDADES (páginas 34-35)

{inventario}

## REPERTORIO DE OPCIONES DE EXPLOTACIÓN

{repertorio}

## CONTEXTO LINGÜÍSTICO

- Unidad anterior (U02): Descripciones físicas, nacionalidades, profesiones. Verbos ser, tener, llevar.
- Esta unidad (U03): La familia — parentesco.
- Vocabulario nuevo principal: abuelo/a, padre/madre, tío/a, hermano/a, primo/a, hijo/a.
- Contenido reciclable: nombres, nacionalidades, descripciones, verbo ser.

## INSTRUCCIÓN

Genera la explotación de vocabulario siguiendo tu protocolo. Output en español, ~1.700 palabras, formato guía del profesor."""


# === LLAMADAS A MODELOS ===

def llamar_anthropic(system_prompt, user_message, model_id):
    """Llama a la API de Anthropic."""
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    t0 = time.time()
    response = client.messages.create(
        model=model_id,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
        temperature=0.7,
    )
    elapsed = time.time() - t0
    text = response.content[0].text
    usage = {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    }
    return text, elapsed, usage


def llamar_groq(system_prompt, user_message, model_id):
    """Llama a la API de Groq."""
    client = Groq(api_key=os.environ["GROQ_API_KEY"])
    t0 = time.time()
    response = client.chat.completions.create(
        model=model_id,
        max_tokens=4096,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
    )
    elapsed = time.time() - t0
    text = response.choices[0].message.content
    usage = {
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
    }
    return text, elapsed, usage


# === MAIN ===

def main():
    print("=" * 60)
    print("PRUEBA COMPARATIVA DE MODELOS — Vocabulario U03")
    print("=" * 60)

    # Cargar inputs
    print("\n📂 Cargando inputs...")
    prompt_agente = cargar_prompt_agente()
    repertorio = cargar_repertorio()
    inventario = cargar_inventario_vocabulario()
    user_message = construir_mensaje_usuario(repertorio, inventario)

    print(f"  Prompt agente: {len(prompt_agente):,} caracteres")
    print(f"  Repertorio: {len(repertorio):,} caracteres")
    print(f"  Inventario vocab: {len(inventario):,} caracteres")
    print(f"  Mensaje usuario total: {len(user_message):,} caracteres")

    # Directorio de resultados
    output_dir = PROJECT / "scripts" / "resultados_prueba"
    output_dir.mkdir(exist_ok=True)

    resultados = {}

    for nombre, config in MODELOS.items():
        print(f"\n{'─' * 60}")
        print(f"🤖 {config['label']}")
        print(f"   Modelo: {config['model_id']}")
        print(f"   Llamando...", end="", flush=True)

        try:
            if config["provider"] == "anthropic":
                text, elapsed, usage = llamar_anthropic(
                    prompt_agente, user_message, config["model_id"]
                )
            else:
                text, elapsed, usage = llamar_groq(
                    prompt_agente, user_message, config["model_id"]
                )

            # Calcular coste
            if nombre == "claude-sonnet":
                cost = (usage["input_tokens"] / 1e6 * 3.0) + (usage["output_tokens"] / 1e6 * 15.0)
            elif nombre == "kimi-k2":
                cost = (usage["input_tokens"] / 1e6 * 1.0) + (usage["output_tokens"] / 1e6 * 3.0)
            else:  # qwen3
                cost = (usage["input_tokens"] / 1e6 * 0.29) + (usage["output_tokens"] / 1e6 * 0.59)

            words = len(text.split())

            print(f" ✅ ({elapsed:.1f}s)")
            print(f"   Tokens: {usage['input_tokens']:,} in / {usage['output_tokens']:,} out")
            print(f"   Palabras generadas: {words:,}")
            print(f"   Coste estimado: ${cost:.4f}")

            # Guardar output
            output_file = output_dir / f"{nombre}.md"
            output_file.write_text(
                f"# Resultado: {config['label']}\n\n"
                f"- Modelo: `{config['model_id']}`\n"
                f"- Tiempo: {elapsed:.1f}s\n"
                f"- Tokens: {usage['input_tokens']:,} input / {usage['output_tokens']:,} output\n"
                f"- Palabras: {words:,}\n"
                f"- Coste: ${cost:.4f}\n\n"
                f"---\n\n"
                f"{text}\n",
                encoding="utf-8"
            )

            resultados[nombre] = {
                "label": config["label"],
                "elapsed": elapsed,
                "usage": usage,
                "words": words,
                "cost": cost,
                "file": str(output_file),
            }

        except Exception as e:
            print(f" ❌ ERROR: {e}")
            resultados[nombre] = {"error": str(e)}

    # Resumen
    print(f"\n{'=' * 60}")
    print("RESUMEN COMPARATIVO")
    print(f"{'=' * 60}")
    print(f"\n{'Modelo':<25} {'Tiempo':>8} {'Palabras':>10} {'Coste':>10}")
    print(f"{'─' * 25} {'─' * 8} {'─' * 10} {'─' * 10}")
    for nombre, r in resultados.items():
        if "error" in r:
            print(f"{nombre:<25} {'ERROR':>8}")
        else:
            print(f"{r['label'][:25]:<25} {r['elapsed']:>7.1f}s {r['words']:>10,} ${r['cost']:>9.4f}")

    print(f"\n📁 Resultados guardados en: {output_dir}/")
    print(f"   Abre cada archivo .md para comparar la calidad del español.\n")

    # Guardar resumen JSON
    with open(output_dir / "resumen.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
