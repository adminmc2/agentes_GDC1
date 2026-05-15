#!/usr/bin/env python3
"""Valida estructuralmente un UX-nc1-inventario.json contra el schema canónico.

Uso:
    python3 scripts/validar_inventario.py 3
    python3 scripts/validar_inventario.py unidades/U3/U3-nc1-inventario.json

Sale con código 0 si todo OK, 1 si hay errores. Reporta avisos y auditoría
legacy sin fallar. Sin LLM, cero tokens.

Tres canales de salida:
    - errores: bloquean cierre (exit 1).
    - avisos: no bloquean, indican deuda formal.
    - auditoría legacy: no bloquean, informativos durante el rollout R1 del
      canon semántico (campos no canónicos en unidades pre-canon).

Canon semántico (`fases/1-extraccion-inventario/campos-semanticos-canonicos.json`):
    Política completa en `fases/1-extraccion-inventario/reglas-operativas.md` §5.6.
    Iteración activa controlada por ROLLOUT_CANON_ITERACION abajo.
"""

import json
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]

# Importar el módulo del canon (vive en scripts/canon.py)
sys.path.insert(0, str(PROJECT))
from scripts import canon  # noqa: E402

# === Rollout del endurecimiento del canon ===
# Cambiar entre R1 → R2 → R3 requiere commit explícito + entrada en
# PROCESO-MAESTRO.md. Ver reglas-operativas.md §5.6.
ROLLOUT_CANON_ITERACION = "R1"  # R1 | R2 | R3

# Unidades ya integradas al entrar en vigor R1. En R1 estas reciben auditoría
# legacy (no error) cuando un campo no es canónico. Vaciar para pasar a R2.
LEGACY_UNIDADES_R1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

CLAVES_TOP = {"unidad", "curso", "titulo", "paginas_libro", "nivel", "fuente",
              "contenidos_indice",
              # 4 bloques top-level consolidados (v10.111+)
              "vocabulario_consolidado", "tiempos_y_verbos_consolidado",
              "gramatica_consolidada", "pronunciacion_ortografia_consolidada",
              "secciones", "paginas_detalle"}

CLAVES_TOP_OPCIONALES = {"autoevaluacion", "_nota_unidad_atipica",
                         "_decisiones_ia",         # marca interna §14 schema
                         "_migracion_rediseno"}    # clave transitoria §A.2 schema

SECCIONES_CANONICAS = {"vocabulario", "gramatica", "comunicacion", "destrezas",
                       "cultura", "evaluacion", "reflexion"}

TIPOS_CUADRO_VALIDOS = {
    "gramatical", "lexical", "cultural", "comunicativo", "pronunciacion_ortografia",
}

# Enum cerrado de tiempo verbal (§5d schema, v10.115 — 4 valores)
# Perífrasis retirado por opción B; estructura sintáctica, no tiempo.
TIEMPOS_VALIDOS = {"Presente", "Pretérito indefinido", "Imperativo", "Infinitivo"}

# Los 5 tipos productivos que admiten sufijo @R en fuentes (§6.5 reglas, §9.5 schema)
TIPOS_PRODUCTIVOS_AR = {
    "produccion_escrita_guiada", "expresion_escrita_libre", "expresion_oral_libre",
    "tarea_final", "interaccion_oral",
}

# Regex de fuentes (§9.5 schema): pNN-actMM(@R)? | cuadro@pNN(#K)?
import re
FUENTE_REGEX = re.compile(r"^(p\d+-act\d+(@R)?|cuadro@p\d+(#\d+)?)$")

TIPOS_VALIDOS = {
    # Taxonomía v10.59 — basada en la acción específica del enunciado del libro.
    # input sin acción específica posterior
    "escucha",                    # "Escucha" / "Mira X y escucha" — input puro auditivo, sin lectura de texto
    "lee_y_escucha",              # "Lee y escucha" / "Lee y escucha el diálogo"
    "ver_video",                  # "Mira el vídeo"
    # acciones orales reproductivas/responsivas
    "escucha_y_repite",
    "escucha_y_responde",
    # mecánicas de manipulación de elementos dados
    "completa_huecos",            # "Completa", "Lee y completa", "Escucha y completa"
    "relaciona",
    "ordena",
    "clasifica",
    "seleccion_multiple",         # "Subraya", "Marca", "Escucha y marca"
    "verdadero_falso",
    # responder preguntas (separados por tipo de respuesta)
    "responder_preguntas_cerradas",  # respuesta concreta que sale del input
    "responder_preguntas_abiertas",  # respuesta personal/libre
    # producción oral
    "interaccion_oral",           # parejas / grupos
    "expresion_oral_libre",
    # producción escrita
    "produccion_escrita_guiada",  # "Escribe frases con", "Forma frases", "Coloca el artículo"
    "expresion_escrita_libre",    # "Escribe a tu amigo", "Escribe un correo"
    # otros
    "busqueda_informacion",
    "tarea_final",
    "juego",
}

DESTREZAS_VALIDAS = {
    "comprension_auditiva",
    "comprension_lectora",
    "expresion_escrita",
    "expresion_oral",
    "interaccion_oral",
    "mediacion",
}

ENFOQUES_VALIDOS = {
    "gramatica",
    "vocabulario",
    "comunicacion",
    "pronunciacion_ortografia",  # renombrado de 'fonetica' en v10.115
    "cultura",
    "transversal",
}

# Tipos de actividad que deben llevar items_libro u otro contenido visible
TIPOS_QUE_REQUIEREN_CONTENIDO_VISIBLE = {
    "completa_huecos", "relaciona", "ordena", "clasifica",
    "seleccion_multiple", "verdadero_falso",
    "responder_preguntas_cerradas", "responder_preguntas_abiertas",
    "lee_y_escucha", "ver_video",
}

CONTENIDOS_VISIBLES = {
    "items_libro", "texto_completo", "dialogo_completo", "textos_personajes",
    "columnas_relaciona",
    "frases", "preguntas",
    "preguntas_opciones", "ejemplo_libro", "texto_modelo", "nombres_dados",
    "palabras_recuadro", "cuadricula", "afirmaciones_a_corregir",
    "texto_correo", "frases_libro", "respuestas_libro",
    "expresiones_dadas", "definiciones",
    "ejemplos_modelo", "programas_tv", "horarios_digitales",
}


def _validar_canon_inventario(d: dict) -> tuple[list[str], list[str], list[str]]:
    """Valida `actividad.campo_semantico` y claves de `vocabulario_consolidado`
    contra el canon semántico de fase 1.

    Devuelve (errores, avisos, auditoria_legacy). Marca '_pendiente_canon'
    es siempre error duro. El comportamiento ante valores no canónicos
    depende de ROLLOUT_CANON_ITERACION y de si la unidad está en
    LEGACY_UNIDADES_R1. Ver `reglas-operativas.md` §5.6.
    """
    errores: list[str] = []
    avisos: list[str] = []
    auditoria: list[str] = []

    # Cargar canon (si falla, reportar como error y abortar este bloque)
    try:
        canon_data = canon.cargar_canon()
    except FileNotFoundError:
        errores.append(
            "❌ canon: no se puede leer "
            f"{canon.CANON_PATH.relative_to(PROJECT)} "
            "(¿ejecutaste scripts/inicializar_canon_semantico.py?)"
        )
        return errores, avisos, auditoria
    except json.JSONDecodeError as e:
        errores.append(f"❌ canon: JSON no parseable: {e}")
        return errores, avisos, auditoria

    # Validar estructura del canon antes de usarlo. Si el canon está
    # corrupto, no podemos validar el inventario de forma fiable: reportamos
    # error controlado y abortamos.
    canon_errores = canon.validar_canon(canon_data)
    if canon_errores:
        errores.append(
            f"❌ canon: estructura inválida ({len(canon_errores)} errores). "
            f"Imposible validar este inventario contra canon hasta que se sanee."
        )
        for ce in canon_errores[:3]:
            errores.append(f"   · {ce}")
        if len(canon_errores) > 3:
            errores.append(f"   · ... ({len(canon_errores) - 3} más)")
        return errores, avisos, auditoria

    canonicos: set[str] = {e["canonico"] for e in canon_data["campos"]}
    aliases_indice_map: dict[str, str] = {}  # alias_indice → canonico
    aliases_auto_map: dict[str, str] = {}    # alias_auto → canonico
    for e in canon_data["campos"]:
        for a in e.get("aliases_indice") or []:
            aliases_indice_map[a] = e["canonico"]
        for a in e.get("aliases_auto") or []:
            aliases_auto_map[a] = e["canonico"]

    unidad = d.get("unidad")
    es_legacy_r1 = (
        ROLLOUT_CANON_ITERACION == "R1"
        and isinstance(unidad, int)
        and unidad in LEGACY_UNIDADES_R1
    )

    def evaluar(valor: str, ubicacion: str) -> None:
        # Marca transitoria — error duro siempre, en todas las iteraciones
        if valor == "_pendiente_canon":
            errores.append(
                f"❌ {ubicacion}: marca '_pendiente_canon' presente "
                f"(estado transitorio de worktree, bloquea cierre — "
                f"resolver vía árbol de decisión §5.6 antes de integrar)"
            )
            return

        if valor in canonicos:
            return  # OK silencioso

        if valor in aliases_indice_map:
            sugerido = aliases_indice_map[valor]
            msg = f"{ubicacion}: '{valor}' es alias_indice de '{sugerido}'"
            if ROLLOUT_CANON_ITERACION == "R3":
                errores.append(f"❌ {msg} (R3 exige canónico literal)")
            elif ROLLOUT_CANON_ITERACION == "R2":
                # aliases_indice = nomenclatura editorial legítima del libro.
                # En R2 se acepta silenciosamente. La normalización al canónico
                # es trabajo del flujo editorial, no del validador.
                return
            elif es_legacy_r1:
                auditoria.append(f"📋 {msg}")
            else:  # R1, unidad no legacy
                errores.append(f"❌ {msg} (canon R1 exige canónico literal para unidades nuevas)")
            return

        if valor in aliases_auto_map:
            sugerido = aliases_auto_map[valor]
            msg = f"{ubicacion}: '{valor}' es alias_auto de '{sugerido}'"
            if ROLLOUT_CANON_ITERACION == "R3":
                errores.append(f"❌ {msg} (R3 exige canónico literal)")
            elif ROLLOUT_CANON_ITERACION == "R2":
                avisos.append(f"⚠ {msg} (deuda: actualizar a canónico)")
            elif es_legacy_r1:
                auditoria.append(f"📋 {msg}")
            else:  # R1, unidad no legacy
                errores.append(f"❌ {msg} (canon R1 exige canónico literal para unidades nuevas)")
            return

        # No coincide con canon ni con alias
        msg = f"{ubicacion}: '{valor}' no está en el canon"
        if es_legacy_r1:
            auditoria.append(f"📋 {msg}")
        else:
            errores.append(f"❌ {msg}")

    # Superficie 1: claves de vocabulario_consolidado.{principal,recurrente}
    # (v10.115: sub-bloque 'comprension' eliminado del modelo)
    voc = d.get("vocabulario_consolidado")
    if isinstance(voc, dict):
        for bloque in ("principal", "recurrente"):
            bloq = voc.get(bloque)
            if isinstance(bloq, dict):
                for clave in bloq.keys():
                    if clave.startswith("_"):
                        continue  # claves reservadas (_descripcion, _pendiente_canon como clave)
                    evaluar(clave, f"vocabulario_consolidado.{bloque}.<{clave}>")

    # Superficie 2: referencias léxicas en actividad.vocabulario y cuadro.vocabulario
    # (v10.115: actividad.campo_semantico eliminado; reemplazado por lista actividad.vocabulario)
    for p in d.get("paginas_detalle", []) or []:
        if not isinstance(p, dict):
            continue
        for a in p.get("actividades", []) or []:
            if not isinstance(a, dict):
                continue
            voc_ref = a.get("vocabulario", [])
            if isinstance(voc_ref, list):
                aid = a.get("id", "?")
                for ref in voc_ref:
                    if isinstance(ref, str):
                        evaluar(ref, f"actividad[{aid}].vocabulario")
        for c in p.get("cuadros", []) or []:
            if not isinstance(c, dict):
                continue
            voc_ref = c.get("vocabulario", [])
            if isinstance(voc_ref, list):
                pag = p.get("pagina", "?")
                for ref in voc_ref:
                    if isinstance(ref, str):
                        evaluar(ref, f"cuadro@p{pag}.vocabulario")

    return errores, avisos, auditoria


def validar(path):
    errores, avisos, auditoria_legacy = [], [], []
    if not path.exists():
        return [f"❌ Archivo no existe: {path}"], [], []

    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"❌ JSON no parseable: {e}"], [], []

    # 1. Claves top-level
    # Tolerancia de fixtures exploratorias (schema §A.5):
    # si _fixture_exploratoria está presente, se admiten claves _fixture_*.
    es_fixture = "_fixture_exploratoria" in d
    if es_fixture and not isinstance(d.get("unidad"), str):
        avisos.append("⚠ _fixture_exploratoria presente pero 'unidad' no es string ('Np')")

    faltan = CLAVES_TOP - set(d.keys())
    if faltan:
        errores.append(f"❌ Faltan claves top-level: {sorted(faltan)}")

    sobra = set(d.keys()) - CLAVES_TOP - CLAVES_TOP_OPCIONALES - {"registro"}  # registro tolerado
    # Filtrar claves _fixture_* en fixtures (metadata extracontractual §A.5)
    if es_fixture:
        sobra = {k for k in sobra if not k.startswith("_fixture_")}
    if sobra:
        avisos.append(f"⚠ Claves top-level no canónicas: {sorted(sobra)}")

    # _migracion_rediseno y _decisiones_ia opcionales canónicas
    if "_decisiones_ia" in d and not isinstance(d["_decisiones_ia"], list):
        errores.append("❌ _decisiones_ia (top-level) debe ser lista de strings")
    if "_migracion_rediseno" in d and not isinstance(d["_migracion_rediseno"], dict):
        errores.append("❌ _migracion_rediseno debe ser objeto (clave transitoria §A.2)")

    # Rechazo de _fixture_* en inventarios canónicos (schema §A.5)
    if not es_fixture and isinstance(d.get("unidad"), int):
        fixture_keys = [k for k in d.keys() if k.startswith("_fixture_")]
        if fixture_keys:
            errores.append(f"❌ Inventario canónico (unidad entero) con claves _fixture_*: {fixture_keys} — prohibidas por §A.5")

    # 1bis. Shape de los 4 bloques top-level consolidados (schema §9, v10.111+)
    # vocabulario_consolidado, gramatica_consolidada, pronunciacion_ortografia_consolidada → 2 sub-bloques principal/recurrente
    for bloque_name in ("vocabulario_consolidado", "gramatica_consolidada", "pronunciacion_ortografia_consolidada"):
        if bloque_name in d:
            bloque = d[bloque_name]
            if not isinstance(bloque, dict):
                errores.append(f"❌ {bloque_name} debe ser objeto con sub-bloques principal/recurrente")
                continue
            for subbloque in ("principal", "recurrente"):
                if subbloque not in bloque:
                    avisos.append(f"⚠ {bloque_name}: falta sub-bloque '{subbloque}' (puede ser objeto vacío)")
                elif not isinstance(bloque[subbloque], dict):
                    errores.append(f"❌ {bloque_name}.{subbloque} debe ser objeto")
    # tiempos_y_verbos_consolidado → lista plana de objetos
    if "tiempos_y_verbos_consolidado" in d:
        tvc = d["tiempos_y_verbos_consolidado"]
        if not isinstance(tvc, list):
            errores.append("❌ tiempos_y_verbos_consolidado debe ser lista plana de objetos verbales")
        else:
            for i, entry in enumerate(tvc):
                if not isinstance(entry, dict):
                    errores.append(f"❌ tiempos_y_verbos_consolidado[{i}] debe ser objeto")
                    continue
                if "lema" not in entry:
                    errores.append(f"❌ tiempos_y_verbos_consolidado[{i}]: falta 'lema'")
                if "tiempos" in entry and isinstance(entry["tiempos"], list):
                    for t in entry["tiempos"]:
                        if t not in TIEMPOS_VALIDOS:
                            errores.append(f"❌ tiempos_y_verbos_consolidado[{i}]: tiempo '{t}' no válido (enum §5d: {sorted(TIEMPOS_VALIDOS)})")

    # autoevaluacion (opcional): si existe, validar estructura completa
    if "autoevaluacion" in d:
        ae = d["autoevaluacion"]
        if not isinstance(ae, dict):
            errores.append("❌ autoevaluacion debe ser dict")
        else:
            for k in ("pagina", "instruccion_original", "opciones", "emoticonos"):
                if k not in ae:
                    errores.append(f"❌ autoevaluacion: falta '{k}'")
            if "pagina" in ae and not isinstance(ae["pagina"], int):
                errores.append("❌ autoevaluacion.pagina debe ser int")
            if "instruccion_original" in ae and not isinstance(ae["instruccion_original"], str):
                errores.append("❌ autoevaluacion.instruccion_original debe ser str")
            if "emoticonos" in ae and not isinstance(ae["emoticonos"], bool):
                errores.append("❌ autoevaluacion.emoticonos debe ser bool")
            if "opciones" in ae:
                if not isinstance(ae["opciones"], list) or len(ae["opciones"]) != 3:
                    errores.append("❌ autoevaluacion.opciones debe ser lista de 3 elementos")
                elif not all(isinstance(o, str) for o in ae["opciones"]):
                    errores.append("❌ autoevaluacion.opciones debe contener strings")

            # Valores fijos para curso NC1 (ver prompt fase 1, sección "Bloque de autoevaluación")
            if d.get("curso") == "nc1":
                NC1_INSTRUCCION = "Mis resultados en esta unidad son:"
                NC1_OPCIONES = ["MUY BUENOS", "BUENOS", "NO MUY BUENOS"]
                if ae.get("instruccion_original") != NC1_INSTRUCCION:
                    errores.append(f"❌ autoevaluacion.instruccion_original NC1 fijo: '{NC1_INSTRUCCION}'")
                if ae.get("opciones") != NC1_OPCIONES:
                    errores.append(f"❌ autoevaluacion.opciones NC1 fijo: {NC1_OPCIONES}")
                if ae.get("emoticonos") is not True:
                    errores.append("❌ autoevaluacion.emoticonos NC1 fijo: true")

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
                if "cuadros_gramaticales" in p:
                    errores.append(f"❌ {pref}: clave obsoleta 'cuadros_gramaticales' — usar 'cuadros' con campo 'tipo_cuadro'")

                for ci, c in enumerate(p.get("cuadros", [])):
                    cpref = f"{pref}.cuadros[{ci}]"
                    if "tipo_cuadro" not in c:
                        errores.append(f"❌ {cpref}: falta 'tipo_cuadro'")
                    elif c["tipo_cuadro"] not in TIPOS_CUADRO_VALIDOS:
                        errores.append(f"❌ {cpref}: tipo_cuadro '{c['tipo_cuadro']}' no válido (valores: {sorted(TIPOS_CUADRO_VALIDOS)})")

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

                    # numero: opcional, pero si está presente debe ser int (schema §3.1)
                    if "numero" in a and not isinstance(a["numero"], int):
                        errores.append(f"❌ {apref}: 'numero' debe ser int si está presente")

                    # tipo válido
                    tipo = a.get("tipo")
                    if not tipo:
                        errores.append(f"❌ {apref}: falta 'tipo'")
                    elif tipo not in TIPOS_VALIDOS:
                        errores.append(f"❌ {apref}: tipo '{tipo}' no es de la taxonomía cerrada")

                    # destreza: lista no vacía, valores del enum cerrado, orden alfabético, sin duplicados
                    if "destreza" not in a:
                        errores.append(f"❌ {apref}: falta 'destreza' (lista de valores del enum cerrado)")
                    elif not isinstance(a["destreza"], list):
                        errores.append(f"❌ {apref}: 'destreza' debe ser lista (no string)")
                    elif len(a["destreza"]) == 0:
                        errores.append(f"❌ {apref}: 'destreza' no puede ser lista vacía")
                    else:
                        for dx in a["destreza"]:
                            if dx not in DESTREZAS_VALIDAS:
                                errores.append(f"❌ {apref}: destreza '{dx}' no válida (enum: {sorted(DESTREZAS_VALIDAS)})")
                        if len(set(a["destreza"])) != len(a["destreza"]):
                            errores.append(f"❌ {apref}: 'destreza' contiene duplicados")
                        if a["destreza"] != sorted(a["destreza"]):
                            errores.append(f"❌ {apref}: 'destreza' debe estar en orden alfabético — actual {a['destreza']}, esperado {sorted(a['destreza'])}")

                    # enfoque: string obligatorio del enum cerrado
                    if "enfoque" not in a:
                        errores.append(f"❌ {apref}: falta 'enfoque' (string del enum cerrado)")
                    elif not isinstance(a["enfoque"], str):
                        errores.append(f"❌ {apref}: 'enfoque' debe ser string")
                    elif a["enfoque"] not in ENFOQUES_VALIDOS:
                        errores.append(f"❌ {apref}: enfoque '{a['enfoque']}' no válido (enum: {sorted(ENFOQUES_VALIDOS)})")

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

                    # 4 listas tipadas siempre presentes (schema §3, v10.111+)
                    for lista_tipada in ("vocabulario", "tiempos_y_verbos", "gramatica", "pronunciacion_ortografia"):
                        if lista_tipada not in a:
                            errores.append(f"❌ {apref}: falta lista tipada '{lista_tipada}' (debe estar siempre, lista vacía si no aplica)")
                        elif not isinstance(a[lista_tipada], list):
                            errores.append(f"❌ {apref}: '{lista_tipada}' debe ser lista")

                    # tiempos_y_verbos[] shape (schema §3.2)
                    for vi, v_obj in enumerate(a.get("tiempos_y_verbos", [])):
                        vpref = f"{apref}.tiempos_y_verbos[{vi}]"
                        if not isinstance(v_obj, dict):
                            errores.append(f"❌ {vpref}: debe ser objeto {{lema, tiempo, formas_trabajadas[, estructura_perifrastica]}}")
                            continue
                        for campo in ("lema", "tiempo", "formas_trabajadas"):
                            if campo not in v_obj:
                                errores.append(f"❌ {vpref}: falta '{campo}'")
                        if "tiempo" in v_obj and v_obj["tiempo"] not in TIEMPOS_VALIDOS:
                            errores.append(f"❌ {vpref}: tiempo '{v_obj['tiempo']}' no válido (enum: {sorted(TIEMPOS_VALIDOS)})")
                        if "formas_trabajadas" in v_obj:
                            ft = v_obj["formas_trabajadas"]
                            if not isinstance(ft, list) or len(ft) == 0:
                                errores.append(f"❌ {vpref}: 'formas_trabajadas' debe ser lista no vacía")
                            elif not all(isinstance(s, str) and s.strip() for s in ft):
                                errores.append(f"❌ {vpref}: 'formas_trabajadas' debe contener strings no vacíos")
                        # estructura_perifrastica opcional (opción B v10.115)
                        if "estructura_perifrastica" in v_obj and not isinstance(v_obj["estructura_perifrastica"], str):
                            errores.append(f"❌ {vpref}: 'estructura_perifrastica' debe ser string si está presente")

                    # @R en fuentes: solo si tipo está en los 5 productivos (§6.5 reglas)
                    if tipo and tipo not in TIPOS_PRODUCTIVOS_AR:
                        for v_obj in a.get("tiempos_y_verbos", []):
                            for fuente in v_obj.get("fuentes", []) if isinstance(v_obj, dict) else []:
                                if isinstance(fuente, str) and fuente.endswith("@R"):
                                    errores.append(f"❌ {apref}: fuente con sufijo @R '{fuente}' en tipo no productivo '{tipo}' (§6.5: solo {sorted(TIPOS_PRODUCTIVOS_AR)})")

                    # Marcas internas (schema §14)
                    if "_funcion_ambigua" in a and not isinstance(a["_funcion_ambigua"], bool):
                        errores.append(f"❌ {apref}: '_funcion_ambigua' debe ser bool")
                    if "_decisiones_ia" in a:
                        if not isinstance(a["_decisiones_ia"], list):
                            errores.append(f"❌ {apref}: '_decisiones_ia' (en actividad) debe ser lista de strings")

                    # tipos que requieren contenido visible (items_libro, columnas_relaciona u otro canónico)
                    if tipo in TIPOS_QUE_REQUIEREN_CONTENIDO_VISIBLE:
                        datos = a.get("datos", {})
                        if not any(k in datos for k in CONTENIDOS_VISIBLES):
                            errores.append(
                                f"❌ {apref}: tipo '{tipo}' requiere contenido visible "
                                f"(items_libro, columnas_relaciona, preguntas_opciones u otro canónico)"
                            )

                    # validación estructural de textos_personajes y columnas_relaciona
                    # (schema-inventario.md §3 + reglas-operativas.md §2.5)
                    datos = a.get("datos", {})

                    # columnas_relaciona: objeto {izquierda: [str], derecha: [str]}
                    if "columnas_relaciona" in datos:
                        cr = datos["columnas_relaciona"]
                        if not isinstance(cr, dict):
                            errores.append(f"❌ {apref}: datos.columnas_relaciona debe ser objeto {{izquierda, derecha}}")
                        else:
                            for lado in ("izquierda", "derecha"):
                                col = cr.get(lado)
                                if not isinstance(col, list) or not col:
                                    errores.append(f"❌ {apref}: datos.columnas_relaciona.{lado} debe ser lista no vacía de strings")
                                elif not all(isinstance(s, str) and s.strip() for s in col):
                                    errores.append(f"❌ {apref}: datos.columnas_relaciona.{lado} debe contener solo strings no vacíos")
                    if "textos_personajes" in datos:
                        tp = datos["textos_personajes"]
                        if not isinstance(tp, list):
                            errores.append(f"❌ {apref}: datos.textos_personajes debe ser lista de objetos {{personaje, texto}}")
                        else:
                            for i, item in enumerate(tp):
                                ipref = f"{apref}.datos.textos_personajes[{i}]"
                                if not isinstance(item, dict):
                                    errores.append(f"❌ {ipref}: cada elemento debe ser objeto con claves 'personaje' y 'texto'")
                                    continue
                                if not isinstance(item.get("personaje"), str) or not item.get("personaje", "").strip():
                                    errores.append(f"❌ {ipref}: falta 'personaje' (string no vacío)")
                                if not isinstance(item.get("texto"), str) or not item.get("texto", "").strip():
                                    errores.append(f"❌ {ipref}: falta 'texto' (string no vacío)")

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

    # Validación contra canon semántico (siempre se ejecuta)
    err_canon, avi_canon, audit_canon = _validar_canon_inventario(d)
    errores.extend(err_canon)
    avisos.extend(avi_canon)
    auditoria_legacy.extend(audit_canon)

    return errores, avisos, auditoria_legacy


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
    print(f"Canon rollout: {ROLLOUT_CANON_ITERACION} "
          f"(legacy R1: {len(LEGACY_UNIDADES_R1)} unidades)")
    errores, avisos, auditoria_legacy = validar(path)

    for a in avisos:
        print(a)
    for e in errores:
        print(e)

    if auditoria_legacy:
        print(f"\n— Auditoría legacy ({len(auditoria_legacy)}) —")
        for entry in auditoria_legacy:
            print(entry)

    if errores:
        print(
            f"\n❌ {len(errores)} errores · {len(avisos)} avisos · "
            f"{len(auditoria_legacy)} legacy"
        )
        sys.exit(1)
    print(
        f"\n✅ JSON válido · {len(avisos)} avisos · "
        f"{len(auditoria_legacy)} legacy"
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
