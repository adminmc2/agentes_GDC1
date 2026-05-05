#!/usr/bin/env python3
"""Valida estructuralmente un UX-nc1-inventario.json contra el schema canónico.

Uso:
    python3 scripts/validar_inventario.py 3
    python3 scripts/validar_inventario.py unidades/U3/U3-nc1-inventario.json

Sale con código 0 si todo OK, 1 si hay errores. Reporta avisos sin fallar.
Sin LLM, cero tokens.
"""

import json
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]

CLAVES_TOP = {"unidad", "curso", "titulo", "paginas_libro", "nivel", "fuente",
              "contenidos_indice", "vocabulario_consolidado", "secciones",
              "paginas_detalle"}

SECCIONES_CANONICAS = {"vocabulario", "gramatica", "comunicacion", "destrezas",
                       "cultura", "evaluacion", "reflexion"}

TIPOS_VALIDOS = {
    "escucha_y_repite", "escucha_y_responde", "completa_huecos", "relaciona",
    "ordena", "clasifica", "seleccion_multiple", "verdadero_falso",
    "produccion_oral_pareja", "produccion_oral_libre",
    "produccion_escrita_guiada", "produccion_escrita_libre",
    "comprension_lectora", "comprension_auditiva", "busqueda_informacion",
    "tarea_final", "juego",
}

# Tipos de actividad que deben llevar items_libro u otro contenido visible
TIPOS_QUE_REQUIEREN_ITEMS = {
    "completa_huecos", "relaciona", "ordena", "clasifica",
    "seleccion_multiple", "verdadero_falso",
}

CONTENIDOS_VISIBLES = {
    "items_libro", "texto_completo", "dialogo_completo", "frases", "preguntas",
    "preguntas_opciones", "ejemplo_libro", "texto_modelo", "nombres_dados",
    "palabras_recuadro", "cuadricula", "afirmaciones_a_corregir",
    "texto_correo", "frases_libro", "respuestas_libro",
    "expresiones_dadas", "definiciones",
}


def validar(path):
    errores, avisos = [], []
    if not path.exists():
        return [f"❌ Archivo no existe: {path}"], []

    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"❌ JSON no parseable: {e}"], []

    # 1. Claves top-level
    faltan = CLAVES_TOP - set(d.keys())
    if faltan:
        errores.append(f"❌ Faltan claves top-level: {sorted(faltan)}")

    sobra = set(d.keys()) - CLAVES_TOP - {"registro"}  # registro tolerado
    if sobra:
        avisos.append(f"⚠ Claves top-level no canónicas: {sorted(sobra)}")

    # 2. fuente, contenidos_indice, secciones tienen estructura esperada
    if "fuente" in d:
        if not isinstance(d["fuente"], dict) or "archivo" not in d["fuente"]:
            errores.append("❌ fuente debe tener al menos {archivo}")

    if "contenidos_indice" in d:
        secciones_idx = set(d["contenidos_indice"].keys())
        esperadas = {"vocabulario", "gramatica", "comunicacion", "destrezas", "cultura"}
        faltan_idx = esperadas - secciones_idx
        if faltan_idx:
            avisos.append(f"⚠ contenidos_indice incompleto, faltan: {sorted(faltan_idx)}")

    if "secciones" in d:
        for k in d["secciones"]:
            if k not in SECCIONES_CANONICAS:
                errores.append(f"❌ secciones contiene clave no canónica: '{k}'")
            v = d["secciones"][k]
            if not isinstance(v, dict) or "paginas" not in v or "actividades_ids" not in v:
                errores.append(f"❌ secciones.{k} mal formada (falta paginas o actividades_ids)")

    # 3. paginas_detalle: estructura, IDs únicos, validaciones por actividad
    if "paginas_detalle" in d:
        pags = d["paginas_detalle"]
        if not isinstance(pags, list):
            errores.append("❌ paginas_detalle debe ser lista")
        else:
            ids_vistos = set()
            ids_secciones = set()
            if "secciones" in d:
                for s in d["secciones"].values():
                    ids_secciones.update(s.get("actividades_ids", []))

            paginas_orden = []
            for i, p in enumerate(pags):
                pref = f"paginas_detalle[{i}]"
                if "pagina" not in p:
                    errores.append(f"❌ {pref}: falta 'pagina'")
                else:
                    paginas_orden.append(p["pagina"])
                if "seccion" not in p:
                    errores.append(f"❌ {pref}: falta 'seccion'")
                elif p["seccion"] not in SECCIONES_CANONICAS:
                    errores.append(f"❌ {pref}: seccion '{p['seccion']}' no canónica")
                if "actividades" not in p or not isinstance(p["actividades"], list):
                    errores.append(f"❌ {pref}: 'actividades' debe ser lista")
                    continue

                for j, a in enumerate(p["actividades"]):
                    apref = f"{pref}.actividades[{j}] (id={a.get('id', '?')})"

                    # ID único
                    aid = a.get("id")
                    if not aid:
                        errores.append(f"❌ {apref}: falta 'id'")
                    elif aid in ids_vistos:
                        errores.append(f"❌ {apref}: id duplicado")
                    else:
                        ids_vistos.add(aid)

                    # tipo válido
                    tipo = a.get("tipo")
                    if not tipo:
                        errores.append(f"❌ {apref}: falta 'tipo'")
                    elif tipo not in TIPOS_VALIDOS:
                        errores.append(f"❌ {apref}: tipo '{tipo}' no es de la taxonomía cerrada")

                    # respuestas siempre presente como lista
                    if "respuestas" not in a:
                        errores.append(f"❌ {apref}: falta 'respuestas' (debe estar siempre, vacío si no aplica)")
                    elif not isinstance(a["respuestas"], list):
                        errores.append(f"❌ {apref}: 'respuestas' debe ser lista")

                    # audio/imagen/video como sub-objetos con presente
                    for medio in ("audio", "imagen", "video"):
                        if medio not in a:
                            errores.append(f"❌ {apref}: falta '{medio}'")
                        elif not isinstance(a[medio], dict) or "presente" not in a[medio]:
                            errores.append(f"❌ {apref}: '{medio}' debe ser dict con clave 'presente'")

                    # imagen.descripcion obligatoria si presente
                    img = a.get("imagen", {})
                    if img.get("presente") and not img.get("descripcion"):
                        errores.append(f"❌ {apref}: imagen.presente=true requiere 'descripcion'")

                    # tipos que requieren items_libro o equivalente
                    if tipo in TIPOS_QUE_REQUIEREN_ITEMS:
                        datos = a.get("datos", {})
                        if not any(k in datos for k in CONTENIDOS_VISIBLES):
                            errores.append(
                                f"❌ {apref}: tipo '{tipo}' requiere contenido visible "
                                f"(uno de: items_libro, frases_libro, preguntas_opciones, etc.)"
                            )

            # IDs en secciones coinciden con IDs reales
            sobra_sec = ids_secciones - ids_vistos
            falta_sec = ids_vistos - ids_secciones
            if sobra_sec:
                errores.append(f"❌ IDs en 'secciones' que no existen en paginas_detalle: {sorted(sobra_sec)}")
            if falta_sec:
                avisos.append(f"⚠ IDs en paginas_detalle que faltan en 'secciones': {sorted(falta_sec)}")

            # Páginas en orden
            if paginas_orden != sorted(paginas_orden):
                avisos.append(f"⚠ Páginas no en orden ascendente: {paginas_orden}")

    return errores, avisos


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)

    arg = sys.argv[1]
    if arg.isdigit():
        n = int(arg)
        path = PROJECT / "unidades" / f"U{n}" / f"U{n}-nc1-inventario.json"
    else:
        path = Path(arg).resolve()

    print(f"Validando: {path.relative_to(PROJECT) if path.is_relative_to(PROJECT) else path}")
    errores, avisos = validar(path)

    for a in avisos:
        print(a)
    for e in errores:
        print(e)

    if errores:
        print(f"\n❌ {len(errores)} errores · {len(avisos)} avisos")
        sys.exit(1)
    print(f"\n✅ JSON válido · {len(avisos)} avisos")
    sys.exit(0)


if __name__ == "__main__":
    main()
