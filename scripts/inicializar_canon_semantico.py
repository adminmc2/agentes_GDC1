#!/usr/bin/env python3
"""
Inicialización one-off del canon semántico.

Pobla `fases/1-extraccion-inventario/campos-semanticos-canonicos.json` con:
  1. Una entrada `origen: "indice"` por cada string literal de `vocabulario[]`
     (todas las unidades) y `contenido_general[]` (U0) en `nc1-curso.json`.
  2. Una entrada `origen: "pcic_a1"` por cada subcategoría del subset curado
     del PCIC A1 (Instituto Cervantes), filtrado por relevancia para libro
     escolar A1 dirigido a adolescentes 12-15.

Reglas aplicadas durante la inicialización:
  - Si una subcategoría PCIC coincide literalmente con una entrada del índice
    YA creada, NO se duplica como pcic_a1 (gana indice).
  - Ningún `canonico` se normaliza automáticamente. El texto literal del libro
    queda como `canonico` en las entradas `indice` (su `aliases_indice` queda
    vacío porque el canonico ya coincide). La normalización a nombres más
    cortos ("Establecimientos" en vez de "Establecimientos: cine,
    restaurante, farmacia...") es trabajo posterior del humano vía Claude Code.
  - `aliases_auto` arranca siempre vacía. Se va poblando conforme se sanean
    los inventarios legacy (U0-U9).

Tras escribir, ejecuta `validar_canon` vía `escribir_canon` — si los
invariantes fallan, aborta sin tocar disco.

Uso: python3 scripts/inicializar_canon_semantico.py

Ejecuta solo una vez al arrancar el sistema. Re-ejecuciones SOBRESCRIBEN
el canon — protección: si el archivo ya existe, requiere flag --force.
"""
import argparse
import json
import sys
from datetime import date
from pathlib import Path

# Permite importar el módulo canon estando en scripts/
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts import canon  # noqa: E402

# Subset curado PCIC A1 (Instituto Cervantes) para NC1 (adolescentes 12-15,
# libro escolar A1). Filtrado de las 103 subcategorías A1 originales por
# relevancia editorial; excluye subcategorías fuera del alcance del libro
# (justicia, ejército, religión, economía empresarial, derechos laborales,
# pesca, etc.).
#
# Fuente: caes complete system / references / plan_curricular /
#         by_level / a1 / a1_nociones_especificas_completo.json
SUBSET_PCIC_A1: list[str] = [
    # Dimensión física y perceptiva
    "Partes del cuerpo",
    "Características físicas",
    "Acciones y posiciones que se realizan con el cuerpo",
    "Carácter y personalidad",
    # Identidad personal
    "Nombre",
    "Dirección",
    "Número de teléfono",
    "Lugar y fecha de nacimiento",
    "Nacionalidad",
    "Edad",
    "Sexo",
    "Profesión",
    "Documentación",
    "Objetos personales",
    # Relaciones humanas y sociales
    "Relaciones familiares",
    "Relaciones sociales",
    "Celebraciones y actos familiares, sociales y religiosos",
    # Alimentación
    "Dieta y nutrición",
    "Bebida",
    "Alimentos",
    "Platos",
    "Restaurante",
    # Educación
    "Centros e instituciones educativas",
    "Profesorado y alumnado",
    "Sistema educativo",
    "Aprendizaje y enseñanza",
    "Exámenes y calificaciones",
    "Lenguaje de aula",
    "Material educativo y mobiliario de aula",
    # Trabajo
    "Profesiones y cargos",
    "Lugares, herramientas y ropa de trabajo",
    "Actividad laboral",
    # Ocio
    "Tiempo libre y entretenimiento",
    "Espectáculos y exposiciones",
    "Deportes",
    # Información y medios de comunicación
    "Correspondencia escrita",
    "Teléfono",
    "Prensa escrita",
    "Televisión y radio",
    "Internet",
    # Vivienda
    "Acciones relacionadas con la vivienda - Ocupación",
    "Características de la vivienda - Tipos",
    "Características de la vivienda - Partes",
    "Objetos domésticos - Muebles y objetos domésticos",
    "Objetos domésticos - Electrodomésticos",
    # Servicios
    "Servicios sanitarios",
    "Servicios sociales",
    # Compras
    "Lugares, personas y actividades",
    "Ropa, calzado y complementos",
    "Pagos",
    # Salud e higiene
    "Salud y enfermedades",
    "Síntomas",
    "Centros de asistencia sanitaria",
    "Higiene",
    # Viajes, alojamiento y transporte
    "Tipos de viajes",
    "La playa",
    "La montaña",
    "Alojamiento",
    "Sistema de transporte - Tipos de transporte por tierra",
    "Sistema de transporte - Tipos de transporte aéreo",
    # Ciencia y tecnología
    "Cuestiones generales",
    "Matemáticas",
    "Informática y nuevas tecnologías",
    # Cultura y arte
    "Música y danza",
    "Cine y teatro",
    # Geografía y naturaleza
    "Universo y espacio",
    "Geografía física, humana y política",
    "Paisaje y accidentes geográficos",
    "Ciudad",
    "Campo",
    "Clima y tiempo atmosférico",
    "Fauna",
    "Flora",
]


def cargar_entradas_indice() -> list[str]:
    """Lee nc1-curso.json y devuelve todas las strings literales de
    vocabulario[] (todas las unidades) y contenido_general[] (U0)."""
    curso = json.loads(canon.CURSO_PATH.read_text(encoding="utf-8"))
    literales: list[str] = []
    vistos: set[str] = set()
    for u in curso.get("unidades", []):
        for clave in ("vocabulario", "contenido_general"):
            v = u.get(clave)
            if isinstance(v, list):
                for s in v:
                    if isinstance(s, str) and s not in vistos:
                        vistos.add(s)
                        literales.append(s)
    return literales


def construir_canon() -> dict:
    """Construye el dict del canon inicial."""
    campos: list[dict] = []
    canonicos_vistos: set[str] = set()

    # 1. Entradas origen=indice: una por cada string literal del índice
    for literal in cargar_entradas_indice():
        if literal in canonicos_vistos:
            continue
        campos.append({
            "canonico": literal,
            "origen": "indice",
            "aliases_indice": [],
            "aliases_auto": [],
        })
        canonicos_vistos.add(literal)

    # 2. Entradas origen=pcic_a1: solo si no coinciden con un canonico ya creado
    for subcat in SUBSET_PCIC_A1:
        if subcat in canonicos_vistos:
            # Ya está como indice; gana indice
            continue
        campos.append({
            "canonico": subcat,
            "origen": "pcic_a1",
            "aliases_indice": [],
            "aliases_auto": [],
        })
        canonicos_vistos.add(subcat)

    return {
        "version": "1.0",
        "actualizado": str(date.today()),
        "campos": campos,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--force",
        action="store_true",
        help="Sobrescribir el canon existente sin preguntar",
    )
    args = parser.parse_args()

    if canon.CANON_PATH.exists() and not args.force:
        print(
            f"❌ {canon.CANON_PATH} ya existe.\n"
            f"   Este script es one-off. Usa --force solo si sabes lo que haces "
            f"(se hará backup automático en .bak)."
        )
        return 1

    nuevo = construir_canon()
    indice = sum(1 for c in nuevo["campos"] if c["origen"] == "indice")
    pcic = sum(1 for c in nuevo["campos"] if c["origen"] == "pcic_a1")
    print(f"Construyendo canon inicial:")
    print(f"  - origen=indice: {indice} entradas (desde nc1-curso.json)")
    print(f"  - origen=pcic_a1: {pcic} entradas (subset A1 curado)")
    print(f"  - total: {len(nuevo['campos'])}")

    try:
        canon.escribir_canon(nuevo)
    except ValueError as e:
        print(f"\n❌ Validación falló:\n{e}")
        return 1

    print(f"\n✅ Canon escrito en {canon.CANON_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())