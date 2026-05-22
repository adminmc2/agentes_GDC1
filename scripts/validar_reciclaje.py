#!/usr/bin/env python3
"""
Validador estructural de `nc1-reciclaje.json` — componente (a) del gate §13.

Comprueba la conformidad de `nc1-reciclaje.json` con `schema-reciclaje.md`:
claves, tipos y enumeraciones. Es el **chequeo estructural** del criterio de
cierre de fase 2 (`reglas-reciclaje.md` §13 (a)): debe dar **0 errores**.

Alcance:
  - Valida el archivo en CUALQUIER estadio del pipeline — salida de Capa 1
    (esqueleto mecánico) o de Capa 2 (enriquecido con etiquetas, triage
    `reconciliado`/`nuevo`, `explicacion`, `detalle`).
  - NO comprueba las invariantes específicas de la salida de Capa 1 (§11.4):
    eso lo hace el propio `generar_reciclaje_capa1.py` antes de escribir.
  - NO comprueba la calidad cross-unidad R1-R5 (`reglas-reciclaje.md` §14):
    ese es un validador aparte.

Nota: desde v11.68 el `unidades/nc1-reciclaje.json` canónico está en el shape
del rediseño (lo regenera `generar_reciclaje_capa1.py`); este validador da
0 errores sobre él.

Uso:
    python3 scripts/validar_reciclaje.py [ruta]
        `ruta` opcional; por defecto `unidades/nc1-reciclaje.json`.
"""
import argparse
import json
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
RECICLAJE_DEFAULT = PROJECT / "unidades" / "nc1-reciclaje.json"

# --- enumeraciones del schema (schema-reciclaje.md §2-§6) ------------------
BLOQUES = {
    "vocabulario", "gramatica", "pronunciacion_ortografia", "verbal", "perifrasis",
}
NIVELES = {"mapa", "auto", "detalle"}
TIEMPOS = {"Presente", "Pretérito indefinido", "Imperativo", "Infinitivo"}
GRUPOS = {
    "Determinantes", "Pronombres", "Sintagma nominal y concordancia",
    "Construcciones", "Tiempos y modos verbales", "Adverbios y marcadores",
    "Preposiciones",
}
ETIQUETAS = {
    "introduce", "amplia", "aplica", "sistematiza", "contrasta",
    "anticipacion", "discrimina",
}
PROCEDENCIAS = {"declarado", "reconciliado", "nuevo"}
PROPUESTA_TIPOS = {"reconciliacion", "categoria_nueva", "siempre_presente"}
PROPUESTA_ESTADOS = {"pendiente", "aceptada", "rechazada"}

# bloques cuyo evento lleva `tiempo` obligatorio (schema §3)
BLOQUES_CON_TIEMPO = {"verbal", "perifrasis"}


def _es_lista_de_str(valor) -> bool:
    return isinstance(valor, list) and all(isinstance(x, str) for x in valor)


def validar_schema(reciclaje: dict) -> list:
    """Valida `reciclaje` contra `schema-reciclaje.md`. Devuelve lista de
    errores (vacía si es conforme)."""
    errores = []

    if not isinstance(reciclaje, dict):
        return ["raíz: el documento no es un objeto JSON"]

    # --- top-level (schema §1) --------------------------------------------
    for clave in ("_meta", "hilos", "propuestas"):
        if clave not in reciclaje:
            errores.append(f"top-level: falta '{clave}'")

    # --- _meta (schema §1.1) ----------------------------------------------
    meta = reciclaje.get("_meta", {})
    if not isinstance(meta, dict):
        errores.append("_meta: no es un objeto")
        meta = {}
    for clave in ("version", "fecha", "unidades_cubiertas", "estado"):
        if clave not in meta:
            errores.append(f"_meta: falta '{clave}'")
    cubiertas = meta.get("unidades_cubiertas")
    if cubiertas is not None and not (
        isinstance(cubiertas, list) and all(isinstance(x, int) for x in cubiertas)
    ):
        errores.append("_meta.unidades_cubiertas: debe ser lista de enteros")
        cubiertas = []
    cubiertas = set(cubiertas or [])

    # --- hilos (schema §2-§5) ---------------------------------------------
    hilos = reciclaje.get("hilos", [])
    if not isinstance(hilos, list):
        errores.append("hilos: no es una lista")
        hilos = []

    ids_vistos = set()
    for h in hilos:
        if not isinstance(h, dict):
            errores.append("hilos: hay un elemento que no es objeto")
            continue
        hid = h.get("id", "<sin-id>")
        if "id" not in h or not isinstance(hid, str) or not hid:
            errores.append(f"hilo {hid}: 'id' ausente o no es string no vacío")
        if hid in ids_vistos:
            errores.append(f"hilo {hid}: id duplicado")
        ids_vistos.add(hid)

        bloque = h.get("bloque")
        if bloque not in BLOQUES:
            errores.append(f"hilo {hid}: bloque inválido '{bloque}'")
        if not isinstance(h.get("titulo"), str) or not h.get("titulo"):
            errores.append(f"hilo {hid}: 'titulo' ausente o vacío")

        nivel = h.get("nivel_analisis")
        if nivel not in NIVELES:
            errores.append(f"hilo {hid}: nivel_analisis inválido '{nivel}'")

        # _grupo: presente y válido solo en gramática (schema §2, §6.3)
        if bloque == "gramatica":
            if h.get("_grupo") not in GRUPOS:
                errores.append(f"hilo {hid}: _grupo inválido '{h.get('_grupo')}'")
        elif "_grupo" in h:
            errores.append(f"hilo {hid}: _grupo no debe aparecer fuera de gramática")

        # detalle: solo cuando nivel_analisis == detalle (schema §2, §5)
        if "detalle" in h:
            if nivel != "detalle":
                errores.append(
                    f"hilo {hid}: 'detalle' presente con nivel_analisis '{nivel}'"
                )
            errores.extend(_validar_detalle(hid, h["detalle"]))

        errores.extend(_validar_eventos(hid, bloque, h.get("eventos"), cubiertas))

    # --- propuestas (schema §6) -------------------------------------------
    propuestas = reciclaje.get("propuestas", [])
    if not isinstance(propuestas, list):
        errores.append("propuestas: no es una lista")
        propuestas = []
    for p in propuestas:
        if not isinstance(p, dict):
            errores.append("propuestas: hay un elemento que no es objeto")
            continue
        pid = p.get("id", "<sin-id>")
        if "id" not in p:
            errores.append("propuesta sin 'id'")
        if p.get("tipo") not in PROPUESTA_TIPOS:
            errores.append(f"propuesta {pid}: tipo inválido '{p.get('tipo')}'")
        if not isinstance(p.get("descripcion"), str) or not p.get("descripcion"):
            errores.append(f"propuesta {pid}: 'descripcion' ausente o vacía")
        estado = p.get("estado")
        if estado not in PROPUESTA_ESTADOS:
            errores.append(f"propuesta {pid}: estado inválido '{estado}'")
        # `resolucion` exigible cuando la propuesta ya no está pendiente (§6)
        if estado in {"aceptada", "rechazada"} and not p.get("resolucion"):
            errores.append(
                f"propuesta {pid}: estado '{estado}' sin 'resolucion'"
            )

    return errores


def _validar_eventos(hid: str, bloque: str, eventos, cubiertas: set) -> list:
    """Valida la lista de eventos de un hilo (schema §3-§4)."""
    errores = []
    if not isinstance(eventos, list) or not eventos:
        errores.append(f"hilo {hid}: 'eventos' ausente o vacío")
        return errores

    claves_evento = set()
    for ev in eventos:
        if not isinstance(ev, dict):
            errores.append(f"hilo {hid}: hay un evento que no es objeto")
            continue
        unidad = ev.get("unidad")
        if not isinstance(unidad, int):
            errores.append(f"hilo {hid}: evento con 'unidad' no entera")
        elif cubiertas and unidad not in cubiertas:
            errores.append(
                f"hilo {hid} u{unidad}: unidad fuera de _meta.unidades_cubiertas"
            )

        # tiempo: obligatorio y válido en verbal/perífrasis; ausente en el resto
        tiempo = ev.get("tiempo")
        if bloque in BLOQUES_CON_TIEMPO:
            if tiempo not in TIEMPOS:
                errores.append(f"hilo {hid} u{unidad}: tiempo inválido '{tiempo}'")
        elif tiempo is not None:
            errores.append(
                f"hilo {hid} u{unidad}: 'tiempo' no debe aparecer en {bloque}"
            )

        # unicidad de la clave mecánica del evento (schema §3, invariante 7)
        clave = (unidad, tiempo)
        if clave in claves_evento:
            errores.append(f"hilo {hid}: evento duplicado para {clave}")
        claves_evento.add(clave)

        # etiquetas: lista de valores de la enumeración (pueden coexistir)
        etiquetas = ev.get("etiquetas")
        if not isinstance(etiquetas, list):
            errores.append(f"hilo {hid} u{unidad}: 'etiquetas' no es lista")
        else:
            for et in etiquetas:
                if et not in ETIQUETAS:
                    errores.append(
                        f"hilo {hid} u{unidad}: etiqueta inválida '{et}'"
                    )

        # procedencia_indice: enumeración; `reconciliado` exige `reconciliado_con`
        proc = ev.get("procedencia_indice")
        if proc is not None and proc not in PROCEDENCIAS:
            errores.append(
                f"hilo {hid} u{unidad}: procedencia_indice inválida '{proc}'"
            )
        if proc == "reconciliado" and not ev.get("reconciliado_con"):
            errores.append(
                f"hilo {hid} u{unidad}: procedencia 'reconciliado' sin 'reconciliado_con'"
            )
        if proc != "reconciliado" and "reconciliado_con" in ev:
            errores.append(
                f"hilo {hid} u{unidad}: 'reconciliado_con' sin procedencia 'reconciliado'"
            )

        # evidencias: lista de string
        if not _es_lista_de_str(ev.get("evidencias")):
            errores.append(
                f"hilo {hid} u{unidad}: 'evidencias' ausente o no es lista de string"
            )

        # formas: lista de string, solo en verbal (schema §3)
        if bloque == "verbal":
            if not _es_lista_de_str(ev.get("formas")):
                errores.append(
                    f"hilo {hid} u{unidad}: 'formas' ausente o no es lista de string"
                )
        elif "formas" in ev:
            errores.append(
                f"hilo {hid} u{unidad}: 'formas' solo aplica al bloque verbal"
            )

        # explicacion: objeto con las tres claves del schema §4
        if "explicacion" in ev:
            errores.extend(_validar_explicacion(hid, unidad, ev["explicacion"]))

    return errores


def _validar_explicacion(hid: str, unidad, explicacion) -> list:
    """Valida el objeto `explicacion` de un evento (schema §4)."""
    if not isinstance(explicacion, dict):
        return [f"hilo {hid} u{unidad}: 'explicacion' no es objeto"]
    errores = []
    for clave in ("que_dice_el_libro", "fuente", "analisis_ia"):
        if not isinstance(explicacion.get(clave), str) or not explicacion.get(clave):
            errores.append(
                f"hilo {hid} u{unidad}: explicacion.{clave} ausente o vacía"
            )
    return errores


def _validar_detalle(hid: str, detalle) -> list:
    """Valida el objeto `detalle` de un hilo (schema §5 — contrato mínimo)."""
    if not isinstance(detalle, dict):
        return [f"hilo {hid}: 'detalle' no es objeto"]
    errores = []
    for clave in ("nodos", "enlaces"):
        if not isinstance(detalle.get(clave), list):
            errores.append(f"hilo {hid}: detalle.{clave} ausente o no es lista")
    return errores


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validador estructural de nc1-reciclaje.json (gate §13 (a))."
    )
    parser.add_argument(
        "ruta", nargs="?", default=str(RECICLAJE_DEFAULT),
        help="ruta del archivo a validar (por defecto unidades/nc1-reciclaje.json)",
    )
    args = parser.parse_args()

    ruta = Path(args.ruta)
    if not ruta.exists():
        print(f"✗ No existe el archivo: {ruta}")
        return 1
    try:
        with open(ruta, encoding="utf-8") as fh:
            reciclaje = json.load(fh)
    except json.JSONDecodeError as exc:
        print(f"✗ JSON inválido en {ruta}: {exc}")
        return 1

    errores = validar_schema(reciclaje)
    print(f"Validador estructural — {ruta}")
    if errores:
        print(f"\n✗ {len(errores)} errores contra schema-reciclaje.md:")
        for e in errores:
            print(f"    - {e}")
        return 1
    print("\n✓ Conforme con schema-reciclaje.md (0 errores).")
    return 0


if __name__ == "__main__":
    sys.exit(main())