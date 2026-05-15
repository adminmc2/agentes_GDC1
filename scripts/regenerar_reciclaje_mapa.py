#!/usr/bin/env python3
"""
Regenera los hilos de nivel `mapa` en `unidades/nc1-reciclaje.json`
a partir de `unidades/nc1-curso.json`.

⚠️ ESTADO TRANSITORIO (2026-05-15, v10.119):
   Este script lee `nc1-curso.json`, que no cambió de shape entre v10.114 y v10.117.
   En principio sigue siendo operativo aunque fase 2 esté pausada (decisión 36, v10.108).
   PERO: el output que genera (hilos `nivel_analisis: "mapa"` en `nc1-reciclaje.json`)
   convive con los hilos `nivel_analisis: "auto"` generados por `regenerar_reciclaje_vocabulario.py`,
   que SÍ está en shape v10.114 obsoleto. Mientras `nc1-reciclaje.json` no se regenere
   íntegramente con scripts adaptados al shape v10.117, ejecutar solo este script puede
   producir un `nc1-reciclaje.json` mixto (mapa nuevo + auto viejo). Coordinar la
   regeneración completa cuando se reactive fase 2.

Comportamiento:
- Lee nc1-curso.json y extrae vocabulario, gramática, comunicación,
  pronunciación y para_aprender por unidad.
- Por cada contenido, genera o actualiza un hilo con nivel_analisis "mapa".
- Primera aparición → accion "introduce". Siguientes → "amplia".
- Preserva hilos con nivel_analisis "auto" o "detalle" intactos.
- Sobrescribe únicamente los hilos de nivel "mapa".

Reglas de naming: ver fases/2-reciclaje/reglas-reciclaje.md §1.
Reglas de acciones: ver fases/2-reciclaje/reglas-reciclaje.md §2.

Uso: python3 scripts/regenerar_reciclaje_mapa.py
"""
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
CURSO = PROJECT / "unidades" / "nc1-curso.json"
RECICLAJE = PROJECT / "unidades" / "nc1-reciclaje.json"

# Campos de nc1-curso.json que generan hilos mapa y su tipo de hilo
CAMPO_TIPO = {
    "vocabulario": "vocabulario",
    "gramatica": "contenido_gramatical",
    "comunicacion": "estrategia",
    "pronunciacion_ortografia": "contenido_gramatical",
    "para_aprender": "estrategia",
}

# Impacto por defecto según el campo
CAMPO_IMPACTO = {
    "vocabulario": "alto",
    "gramatica": "alto",
    "comunicacion": "medio",
    "pronunciacion_ortografia": "medio",
    "para_aprender": "medio",
}

# Sección del schema según el campo
CAMPO_SECCION = {
    "vocabulario": "vocabulario",
    "gramatica": "gramatica",
    "comunicacion": "comunicacion",
    "pronunciacion_ortografia": "pronunciacion_ortografia",
    "para_aprender": "vocabulario",  # "para aprender" = recursos de aula → vocabulario funcional
    "contenido_general": "contenido_general",  # U0 usa este campo para todo su contenido
}

# U0 tiene campo_general en lugar de los campos estándar
CAMPO_TIPO["contenido_general"] = "vocabulario"
CAMPO_IMPACTO["contenido_general"] = "alto"


def slug(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s


def hilo_id(titulo: str) -> str:
    return f"hilo-{slug(titulo)}"


def normalizar(s: str) -> str:
    """Normaliza un título para comparación (minúsculas, sin tildes, sin puntuación)."""
    return slug(s)


def build_mapa_hilos(curso: dict) -> list[dict]:
    """
    Construye la lista de hilos mapa a partir de nc1-curso.json.
    Regla de agrupación: un hilo por contenido atómico (string), un campo semántico = un hilo.
    """
    # titulo_norm → hilo acumulado
    hilos_by_titulo: dict[str, dict] = {}

    for unidad_data in curso.get("unidades", []):
        unidad_num = unidad_data["unidad"]

        for campo, tipo_hilo in CAMPO_TIPO.items():
            valor = unidad_data.get(campo)
            if not valor:
                continue

            # El campo puede ser string o lista de strings
            items = [valor] if isinstance(valor, str) else valor

            for titulo_raw in items:
                titulo = titulo_raw.strip()
                norm = normalizar(titulo)

                if norm not in hilos_by_titulo:
                    # Primera aparición → introduce
                    hilos_by_titulo[norm] = {
                        "id": hilo_id(titulo),
                        "titulo": titulo,
                        "tipo": tipo_hilo,
                        "nivel_analisis": "mapa",
                        "eventos": [
                            {
                                "unidad": unidad_num,
                                "seccion": CAMPO_SECCION[campo],
                                "accion": "introduce",
                                "descripcion": titulo,
                                "impacto": CAMPO_IMPACTO[campo],
                            }
                        ],
                    }
                else:
                    # Aparición posterior → amplia
                    hilos_by_titulo[norm]["eventos"].append(
                        {
                            "unidad": unidad_num,
                            "seccion": CAMPO_SECCION[campo],
                            "accion": "amplia",
                            "descripcion": titulo,
                            "impacto": CAMPO_IMPACTO[campo],
                        }
                    )

    return list(hilos_by_titulo.values())


def main():
    if not CURSO.exists():
        print(f"ERROR: no encontrado {CURSO}")
        return

    with CURSO.open(encoding="utf-8") as f:
        curso = json.load(f)

    # Leer reciclaje existente o crear estructura base
    if RECICLAJE.exists():
        with RECICLAJE.open(encoding="utf-8") as f:
            reciclaje = json.load(f)
    else:
        reciclaje = {"curso": "nc1", "actualizado": str(date.today()), "hilos": []}

    hilos_existentes = reciclaje.get("hilos", [])

    # Preservar hilos auto y detalle
    hilos_preservados = [
        h for h in hilos_existentes if h.get("nivel_analisis") in ("auto", "detalle")
    ]

    # Construir nuevos hilos mapa
    nuevos_mapa = build_mapa_hilos(curso)

    # Combinar: mapa primero, luego auto/detalle
    reciclaje["hilos"] = nuevos_mapa + hilos_preservados
    reciclaje["actualizado"] = str(date.today())

    with RECICLAJE.open("w", encoding="utf-8") as f:
        json.dump(reciclaje, f, ensure_ascii=False, indent=2)

    print(f"OK — {len(nuevos_mapa)} hilos mapa generados.")
    print(f"     {len(hilos_preservados)} hilos auto/detalle preservados.")
    print(f"     Total: {len(reciclaje['hilos'])} hilos en {RECICLAJE.name}")


if __name__ == "__main__":
    main()