#!/usr/bin/env python3
"""
Generador de Capa 1 de fase 2 — proyección mecánica de `nc1-reciclaje.json`.

Implementa el contrato del Nivel 3 del rediseño de fase 2:
  - `fases/2-reciclaje/REDISEÑO-EN-CURSO.md` §11 — procedimiento de la Capa 1.
  - `fases/2-reciclaje/schema-reciclaje.md`     — shape canónico de salida.

La Capa 1 produce el ESQUELETO MECÁNICO del reciclaje: identidad de los hilos,
eventos por unidad, evidencias trazables, `procedencia_indice: declarado` por
coincidencia literal con el índice y formas verbales. NO toma decisiones
editoriales — las etiquetas interpretativas, `reconciliado`/`nuevo`,
`explicacion` y `detalle` son trabajo de la Capa 2 IA (§11.2).

Modo implementado: ÍNTEGRO (§11.5) — recalcula toda la proyección mecánica del
curso. Preserva `propuestas[]` y los cierres humanos del `nc1-reciclaje.json`
existente, que la Capa 1 nunca invalida (invariante §11.4.10).

El generador materializa las dos proyecciones que pueblan la Capa 1 (§4.5):
  - `auto`  — hilos y eventos derivados de los inventarios cerrados (§11.2).
  - `mapa`  — siembra desde el índice de `nc1-curso.json` (§4.2): se resuelve
              cada entrada del índice a su título canónico de registry con
              criterio CONSERVADOR — solo cuando la coincidencia es inequívoca
              (§11.4 invariantes 2-3). Las entradas que no resuelven (ambiguas,
              compuestas, o sin categoría canónica) NO se fuerzan: se reportan
              como avisos para revisión. `finalizar_niveles()` fija el nivel
              de cada hilo: `auto` si tiene evento respaldado por inventario,
              `mapa` si solo está declarado en el índice.

La salida se valida estructuralmente contra `schema-reciclaje.md` y contra las
invariantes §11.4 ANTES de escribirse: si la validación falla, no se escribe.

Uso:
    python3 scripts/generar_reciclaje_capa1.py            # genera y escribe
    python3 scripts/generar_reciclaje_capa1.py --dry-run  # valida sin escribir
"""
import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import date
from pathlib import Path

# Validador estructural: fuente única del chequeo de schema (regla de oro 4).
# Ambos scripts viven en scripts/, así que el import directo funciona al
# ejecutar `python3 scripts/generar_reciclaje_capa1.py`.
from validar_reciclaje import TIEMPOS, validar_schema

PROJECT = Path(__file__).resolve().parent.parent
UNIDADES = PROJECT / "unidades"
CURSO = UNIDADES / "nc1-curso.json"
RECICLAJE = UNIDADES / "nc1-reciclaje.json"
CHANGELOG = PROJECT / "CHANGELOG.md"
FASE1 = PROJECT / "fases" / "1-extraccion-inventario"
FASE2 = PROJECT / "fases" / "2-reciclaje"

REG_CAMPOS = FASE1 / "campos-semanticos-canonicos.json"
REG_GRAMATICA = FASE1 / "gramatica-canonica.json"
REG_PRONORTO = FASE1 / "pronunciacion-ortografia-canonica.json"
REG_VERBOS = FASE1 / "verbos-canonicos.json"
REG_PERIFRASIS = FASE2 / "perifrasis-canonicas.json"

# prefijo del `id` del hilo por bloque (schema §2)
PREFIJO = {
    "vocabulario": "voc",
    "gramatica": "gram",
    "pronunciacion_ortografia": "pron",
    "verbal": "verb",
    "perifrasis": "perif",
}
# `TIEMPOS` (enumeración del schema) se importa de `validar_reciclaje` — el
# resto de enumeraciones las usa solo el validador estructural, no la generación.



# --------------------------------------------------------------------------
# utilidades
# --------------------------------------------------------------------------
def slug(s: str) -> str:
    """Normaliza una cadena a slug ASCII (minúsculas, sin tildes, guiones)."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s


def hilo_id(bloque: str, titulo: str) -> str:
    return f"{PREFIJO[bloque]}-{slug(titulo)}"


def cargar_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def leer_version_changelog() -> str:
    """Última versión vX.Y declarada en CHANGELOG.md (schema _meta.version)."""
    try:
        txt = CHANGELOG.read_text(encoding="utf-8")
    except OSError:
        return "v0.0"
    versiones = re.findall(r"v(\d+)\.(\d+)", txt)
    if not versiones:
        return "v0.0"
    mayor = max((int(a), int(b)) for a, b in versiones)
    return f"v{mayor[0]}.{mayor[1]}"


def walk_dicts(obj):
    """Recorre recursivamente todos los dicts de una estructura JSON."""
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from walk_dicts(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_dicts(v)


# --------------------------------------------------------------------------
# registries — universo cerrado de hilos válidos (§6.1, §11.4 invariantes 2-3)
# --------------------------------------------------------------------------
class Registries:
    """Carga los 5 registries canónicos y expone consultas de canonicidad."""

    def __init__(self):
        campos = cargar_json(REG_CAMPOS)["campos"]
        # canónico -> conjunto de aliases del índice (slugs)
        self.vocab = {}
        # Entradas crudas indexadas por canónico — para resolver procedencia
        # vía `origen` + `aliases_indice` (v11.76, REDISEÑO §9.2).
        self.campos_raw = {}
        for c in campos:
            self.vocab[c["canonico"]] = {
                slug(a) for a in c.get("aliases_indice", [])
            }
            self.campos_raw[c["canonico"]] = c

        gram = cargar_json(REG_GRAMATICA)["categorias"]
        self.gramatica = {k: v.get("_grupo") for k, v in gram.items()}
        self.gramatica_raw = gram  # categoria -> {_grupo, _pcic_ref, ...}

        pron = cargar_json(REG_PRONORTO)["categorias"]
        self.pronorto = set(pron.keys())
        self.pronorto_raw = pron

        self.verbos = set(cargar_json(REG_VERBOS)["verbos"].keys())

        perif = cargar_json(REG_PERIFRASIS)["perifrasis"]
        self.perifrasis = set(perif.keys())
        self.perifrasis_raw = perif

    def canonico(self, bloque: str, titulo: str) -> bool:
        if bloque == "vocabulario":
            return titulo in self.vocab
        if bloque == "gramatica":
            return titulo in self.gramatica
        if bloque == "pronunciacion_ortografia":
            return titulo in self.pronorto
        if bloque == "verbal":
            return titulo in self.verbos
        if bloque == "perifrasis":
            return titulo in self.perifrasis
        return False

    def grupo(self, titulo: str):
        return self.gramatica.get(titulo)

    def es_deprecated(self, bloque: str, titulo: str) -> bool:
        """¿La entry canónica está marcada como `_deprecated` en su registry?

        Capa 1 no debe proyectar hilos `mapa` desde el índice del curso para
        canónicos deprecated — son entradas históricas conservadas como
        trazabilidad, no contenido vigente. Si el índice los menciona
        (por convención de verbatim del libro), Capa 1 los ignora.
        """
        entry = None
        if bloque == "vocabulario":
            entry = self.campos_raw.get(titulo)
        elif bloque == "gramatica":
            entry = self.gramatica_raw.get(titulo)
        elif bloque == "pronunciacion_ortografia":
            entry = self.pronorto_raw.get(titulo)
        elif bloque == "perifrasis":
            entry = self.perifrasis_raw.get(titulo)
        # verbal: la clave es `lema`, no aplica concepto de deprecated aquí
        if not entry:
            return False
        return "_deprecated" in entry

    @staticmethod
    def _match(objetivo: str, claves: set) -> int:
        """Puntúa una entrada contra un conjunto de claves: 2=exacto, 1=prefijo."""
        mejor = 0
        for clave in claves:
            if not clave:
                continue
            if objetivo == clave:
                mejor = max(mejor, 2)
            elif objetivo.startswith(clave + "-"):
                mejor = max(mejor, 1)
        return mejor

    def resolver(self, bloque: str, entrada: str):
        """Resuelve una entrada del índice del curso a su título canónico.

        Devuelve el título canónico solo si la resolución es **inequívoca**;
        `None` si no hay coincidencia o si es ambigua (varios candidatos al
        mismo nivel de coincidencia). Resolución conservadora: la Capa 1 nunca
        inventa ni adivina un título (§11.4 invariantes 2-3).

        Coincidencia mecánica: igualdad de slug, prefijo (absorbe paréntesis
        del índice, p. ej. 'Artículos determinados (el, la, los, las)') y, en
        vocabulario, los `aliases_indice` del registry.
        """
        objetivo = slug(entrada)
        if not objetivo:
            return None
        candidatos = []  # (titulo, score)
        if bloque == "vocabulario":
            for canonico, aliases in self.vocab.items():
                puntua = self._match(objetivo, {slug(canonico)} | set(aliases))
                if puntua:
                    candidatos.append((canonico, puntua))
        elif bloque == "gramatica":
            for cat in self.gramatica:
                puntua = self._match(objetivo, {slug(cat)})
                if puntua:
                    candidatos.append((cat, puntua))
        elif bloque == "pronunciacion_ortografia":
            for cat in self.pronorto:
                puntua = self._match(objetivo, {slug(cat)})
                if puntua:
                    candidatos.append((cat, puntua))
        if not candidatos:
            return None
        mejor = max(p for _, p in candidatos)
        ganadores = [t for t, p in candidatos if p == mejor]
        return ganadores[0] if len(ganadores) == 1 else None


# --------------------------------------------------------------------------
# índice del curso — soporte del triage `procedencia_indice: declarado` (§9.1)
# --------------------------------------------------------------------------
class IndiceCurso:
    """Índice editorial del curso slugificado.

    Eje identitario puro (v11.75): `procedencia_indice: declarado` se decide
    por coincidencia LITERAL del título canónico contra el conjunto de slugs
    del índice **curso-wide** (todas las unidades unidas), **sin aliases**.
    La temporalidad (esta unidad vs la canónica) la lleva la etiqueta del
    evento, no este eje. Aliases del registry son territorio de Capa 2 →
    `reconciliado`, propuesta con cierre humano (§9.2).
    """

    # Todos los campos de contenido por unidad de nc1-curso.json (excluye
    # metadatos: unidad, titulo, pagina_inicio, paginas_libro, ...). Para el
    # eje identitario, "está en el índice del curso" se interpreta sobre el
    # índice completo, no solo los 3 bloques lingüísticos del rediseño.
    _CAMPOS_INDICE = (
        "vocabulario", "gramatica", "pronunciacion_ortografia", "para_aprender",
        "comunicacion", "destrezas", "cultura", "contenido_general",
    )

    def __init__(self, curso: dict):
        # slug → entrada literal del índice (primer match preservado).
        # Mantenemos el texto original para poder construir `reconciliado_con:
        # "indice:<entrada>"` cuando hay alias resolution (v11.76).
        slug_to_entrada = {}
        for u in curso.get("unidades", []):
            for campo in self._CAMPOS_INDICE:
                valor = u.get(campo)
                if valor is None:
                    continue
                items = [valor] if isinstance(valor, str) else valor
                for item in items:
                    s = slug(item)
                    slug_to_entrada.setdefault(s, item)
        self._slug_to_entrada = slug_to_entrada
        self._slugs = set(slug_to_entrada.keys())

    def declarado(self, titulo: str):
        """Devuelve la entrada literal del índice que matchea el título
        canónico (curso-wide; literal o prefijo). None si no hay match.

        Acepta prefijo del slug del índice — absorbe paréntesis del índice
        ('Artículos determinados (el, la, los, las)' matchea el canónico
        'Artículos determinados'). NO acepta aliases: para alias-matching,
        usar `entrada_para_alias` (v11.76).
        """
        objetivo = slug(titulo)
        if not objetivo:
            return None
        # Match exacto primero
        if objetivo in self._slugs:
            return self._slug_to_entrada[objetivo]
        # Match prefijo
        for entrada_slug, entrada_txt in self._slug_to_entrada.items():
            if entrada_slug.startswith(objetivo + "-"):
                return entrada_txt
        return None

    def entrada_para_alias(self, alias: str):
        """Devuelve la entrada literal del índice cuyo slug iguala al alias
        slug, o None si no hay match. Usado por la resolución `indice:<X>` del
        `reconciliado` mecánico (v11.76)."""
        s = slug(alias)
        return self._slug_to_entrada.get(s)


# --------------------------------------------------------------------------
# acumulador de hilos
# --------------------------------------------------------------------------
class Constructor:
    """Acumula hilos y eventos a lo largo de las unidades procesadas."""

    def __init__(self, registries: Registries, indice: IndiceCurso):
        self.reg = registries
        self.indice = indice
        self.hilos = {}            # id -> hilo
        self.descartados = []      # (bloque, titulo, unidad) fuera de registry
        self.unidades = set()

    def _hilo(self, bloque: str, titulo: str) -> dict:
        hid = hilo_id(bloque, titulo)
        h = self.hilos.get(hid)
        if h is None:
            h = {
                "id": hid,
                "bloque": bloque,
                "titulo": titulo,
                # provisional: `finalizar_niveles()` fija el nivel definitivo
                # según el grado de población alcanzado (§4.2).
                "nivel_analisis": "mapa",
                "eventos": [],
            }
            if bloque == "gramatica":
                h["_grupo"] = self.reg.grupo(titulo)
            self.hilos[hid] = h
        return h

    def resolver_procedencia(self, bloque: str, titulo: str):
        """Triage identitario mecánico (REDISEÑO §9, v11.76).

        Devuelve `(procedencia, reconciliado_con)` o `(None, None)`:
          - `declarado` — slug literal del título canónico en el índice del curso.
          - `reconciliado` + `"indice:<entrada>"` — alias de una entrada del
            índice resuelto vía registry (aliases_indice en vocab).
          - `reconciliado` + `"pcic:<ref>"` o `"pcic:A1"` — respaldo PCIC sin
            entrada en el curso (origen=pcic_a1 en vocab; _pcic_ref en
            gramatica/pron/perif).
          - `nuevo` — sin respaldo de ningún tipo.
          - `(None, None)` — bloque `verbal`: Capa 2 lo decide (los lemas
            verbales no llevan respaldo PCIC estructurado en su registry).
        """
        if bloque == "verbal":
            return None, None
        if self.indice.declarado(titulo) is not None:
            return "declarado", None
        if bloque == "vocabulario":
            entry = self.reg.campos_raw.get(titulo)
            if entry is not None:
                # 1) ¿algún alias coincide con una entrada del índice?
                for alias in entry.get("aliases_indice") or []:
                    entrada = self.indice.entrada_para_alias(alias)
                    if entrada:
                        return "reconciliado", f"indice:{entrada}"
                # 2) ¿respaldo PCIC (origen=pcic_a1)?
                if entry.get("origen") == "pcic_a1":
                    return "reconciliado", "pcic:A1"
                # 3) origen=excepcion sin aliases → contenido sin respaldo
                return "nuevo", None
        elif bloque == "gramatica":
            entry = self.reg.gramatica_raw.get(titulo)
            ref = (entry or {}).get("_pcic_ref")
            if ref:
                return "reconciliado", f"pcic:{ref}"
            return "nuevo", None
        elif bloque == "pronunciacion_ortografia":
            entry = self.reg.pronorto_raw.get(titulo)
            ref = (entry or {}).get("_pcic_ref")
            if ref:
                return "reconciliado", f"pcic:{ref}"
            return "nuevo", None
        elif bloque == "perifrasis":
            entry = self.reg.perifrasis_raw.get(titulo)
            ref = (entry or {}).get("_pcic_ref")
            if ref:
                return "reconciliado", f"pcic:{ref}"
            return "nuevo", None
        return "nuevo", None

    def _aplicar_procedencia(self, evento: dict, bloque: str, titulo: str):
        """Aplica el resultado del resolver al evento, sin meter campos `None`."""
        proc, recon = self.resolver_procedencia(bloque, titulo)
        if proc is not None:
            evento["procedencia_indice"] = proc
        if recon is not None:
            evento["reconciliado_con"] = recon

    def add_evento(self, bloque, titulo, unidad, evidencias, tiempo=None,
                   formas=None):
        """Registra (o fusiona) un evento mecánico en su hilo."""
        if not self.reg.canonico(bloque, titulo):
            self.descartados.append((bloque, titulo, unidad))
            return
        self.unidades.add(unidad)
        hilo = self._hilo(bloque, titulo)

        # clave mecánica de unicidad del evento (§11.4 invariante 7)
        existente = None
        for ev in hilo["eventos"]:
            if ev["unidad"] == unidad and ev.get("tiempo") == tiempo:
                existente = ev
                break
        if existente is not None:
            # fusiona evidencias / formas de una fuente repetida en la unidad
            existente["evidencias"] = sorted(
                set(existente["evidencias"]) | set(evidencias or [])
            )
            if formas:
                existente["formas"] = sorted(
                    set(existente.get("formas", [])) | set(formas)
                )
            return

        evento = {
            "unidad": unidad,
            "etiquetas": [],
            "evidencias": sorted(set(evidencias or [])),
        }
        if tiempo is not None:
            evento["tiempo"] = tiempo
        if bloque == "verbal":
            evento["formas"] = sorted(set(formas or []))
        # Triage identitario mecánico, v11.76 — 4 bloques resueltos en Capa 1;
        # verbal queda sin asignar (Capa 2 decide).
        self._aplicar_procedencia(evento, bloque, titulo)
        hilo["eventos"].append(evento)

    def add_evento_mapa(self, bloque: str, titulo: str, unidad: int):
        """Registra un evento de nivel `mapa` desde el índice del curso (§4.2).

        Procedencia mecánica via el resolver — el evento queda con la misma
        clasificación que tendría si viniera del inventario.

        Si el canónico está marcado como `_deprecated` en su registry, NO se
        proyecta como hilo mapa: la entry histórica del registry se conserva
        para trazabilidad, pero no produce un hilo huérfano en el reciclaje.
        El índice del curso (`nc1-curso.json`) puede seguir mencionando el
        canónico viejo por convención de verbatim del libro — el filtro vive
        aquí, en Capa 1.
        """
        if self.reg.es_deprecated(bloque, titulo):
            return
        self.unidades.add(unidad)
        hilo = self._hilo(bloque, titulo)
        proc, recon = self.resolver_procedencia(bloque, titulo)
        for ev in hilo["eventos"]:
            if ev["unidad"] == unidad and ev.get("tiempo") is None:
                if proc is not None:
                    ev["procedencia_indice"] = proc
                if recon is not None:
                    ev["reconciliado_con"] = recon
                return
        nuevo_ev = {
            "unidad": unidad,
            "etiquetas": [],
            "evidencias": [],
        }
        if proc is not None:
            nuevo_ev["procedencia_indice"] = proc
        if recon is not None:
            nuevo_ev["reconciliado_con"] = recon
        hilo["eventos"].append(nuevo_ev)

    def finalizar_niveles(self):
        """Fija `nivel_analisis` de cada hilo según el grado de población (§4.2):
        `auto` si tiene algún evento respaldado por inventario (con evidencias);
        `mapa` si todos sus eventos son solo declaración del índice del curso.
        """
        for hilo in self.hilos.values():
            respaldado = any(ev.get("evidencias") for ev in hilo["eventos"])
            hilo["nivel_analisis"] = "auto" if respaldado else "mapa"


# --------------------------------------------------------------------------
# extracción mecánica por bloque desde un inventario de unidad
# --------------------------------------------------------------------------
def _ref_actividad(parent: dict) -> str:
    """Referencia trazable de una actividad/cuadro, sin el prefijo 'UX-'."""
    ref = parent.get("id") or parent.get("ref") or ""
    return re.sub(r"^U\d+-", "", ref)


def items_tiempos_y_verbos(inventario: dict):
    """Itera (parent, item) por cada entrada de `*.tiempos_y_verbos[]`.

    Aplica a actividades y cuadros (§3.2, §3.3). Excluye el consolidado, que
    usa la clave `tiempos` (lista), no `tiempos_y_verbos`.
    """
    for d in walk_dicts(inventario):
        tyv = d.get("tiempos_y_verbos")
        if not isinstance(tyv, list):
            continue
        for item in tyv:
            if isinstance(item, dict):
                yield d, item


def formas_verbales_por_actividad(inventario: dict) -> dict:
    """Agrega `formas_trabajadas` por (lema, tiempo) desde las actividades.

    El consolidado da una lista plana de formas por lema; el desglose por
    tiempo se reconstruye leyendo `*.tiempos_y_verbos[]` (§7.1, §7.4).
    """
    formas = {}
    for _, item in items_tiempos_y_verbos(inventario):
        lema = item.get("lema")
        tiempo = item.get("tiempo")
        if not lema or not tiempo:
            continue
        formas.setdefault((lema, tiempo), set()).update(
            item.get("formas_trabajadas") or []
        )
    return formas


def perifrasis_por_actividad(inventario: dict) -> dict:
    """Agrega evidencias por (perífrasis, tiempo) desde `*.tiempos_y_verbos[]`.

    La perífrasis se modela como hilo aparte; su fuente es el campo
    `estructura_perifrastica` de las entradas de actividad/cuadro (§3.3).
    """
    perif = {}
    for parent, item in items_tiempos_y_verbos(inventario):
        estructura = item.get("estructura_perifrastica")
        if not estructura:
            continue
        tiempo = item.get("tiempo")
        ref = _ref_actividad(parent)
        clave = (estructura, tiempo)
        if ref:
            perif.setdefault(clave, set()).add(ref)
        else:
            perif.setdefault(clave, set())
    return perif


def procesar_unidad(constructor: Constructor, unidad: int, inventario: dict):
    """Vuelca la proyección mecánica de los 5 bloques de una unidad."""
    # --- vocabulario / gramática / pronunciación-ortografía -----------------
    consolidados = {
        "vocabulario": "vocabulario_consolidado",
        "gramatica": "gramatica_consolidada",
        "pronunciacion_ortografia": "pronunciacion_ortografia_consolidada",
    }
    for bloque, clave in consolidados.items():
        bloque_data = inventario.get(clave) or {}
        for sub in ("principal", "recurrente"):
            for titulo, cat in (bloque_data.get(sub) or {}).items():
                evidencias = cat.get("fuentes") or []
                constructor.add_evento(bloque, titulo, unidad, evidencias)

    # --- verbal + perífrasis -----------------------------------------------
    formas_idx = formas_verbales_por_actividad(inventario)
    for entrada in inventario.get("tiempos_y_verbos_consolidado") or []:
        lema = entrada.get("lema")
        if not lema:
            continue
        fuentes = entrada.get("fuentes") or []
        tiempos = entrada.get("tiempos") or []
        for tiempo in tiempos:
            if tiempo not in TIEMPOS:
                # tiempo fuera de la enumeración del schema: se descarta
                constructor.descartados.append(("verbal", f"{lema}::{tiempo}", unidad))
                continue
            formas = formas_idx.get((lema, tiempo))
            if not formas:
                # sin desglose por actividad: cae al consolidado agregado
                formas = entrada.get("formas_trabajadas") or []
            constructor.add_evento(
                "verbal", lema, unidad, fuentes, tiempo=tiempo, formas=formas
            )

    # --- perífrasis: hilo aparte, fuente `estructura_perifrastica` (§3.3) ---
    for (estructura, tiempo), refs in perifrasis_por_actividad(inventario).items():
        if tiempo not in TIEMPOS:
            constructor.descartados.append(
                ("perifrasis", f"{estructura}::{tiempo}", unidad)
            )
            continue
        constructor.add_evento(
            "perifrasis", estructura, unidad, sorted(refs), tiempo=tiempo
        )


# --------------------------------------------------------------------------
# proyección de nivel `mapa` desde el índice del curso (§4.2, §4.5)
# --------------------------------------------------------------------------
def procesar_indice(constructor: Constructor, curso: dict, cubiertas: set) -> list:
    """Siembra hilos/eventos de nivel `mapa` desde el índice de `nc1-curso.json`.

    Resolución **conservadora** (§11.4 invariantes 2-3): cada entrada del índice
    se resuelve a su título canónico solo si la coincidencia es inequívoca; las
    entradas que no resuelven (ambiguas, compuestas, o sin categoría canónica —
    p. ej. lemas verbales embebidos en `gramatica`) NO se fuerzan: se devuelven
    como avisos para revisión, sin generar hilo.

    Solo cubre vocabulario, gramática y pron/orto: el índice no lista lemas
    verbales ni perífrasis de forma individual (esos hilos nacen del inventario).

    Devuelve la lista de entradas no resueltas: `(unidad, campo, entrada)`.
    """
    avisos = []
    campos = ("vocabulario", "gramatica", "pronunciacion_ortografia")
    for u in curso.get("unidades", []):
        unidad = u["unidad"]
        if unidad not in cubiertas:
            continue
        # campos tipados del índice — cada uno fija el bloque destino
        for campo in campos:
            valor = u.get(campo)
            if not valor:
                continue
            items = [valor] if isinstance(valor, str) else valor
            for entrada in items:
                titulo = constructor.reg.resolver(campo, entrada)
                if titulo is None:
                    avisos.append((unidad, campo, entrada))
                else:
                    constructor.add_evento_mapa(campo, titulo, unidad)
        # U0 (atípica): `contenido_general` se prueba contra los tres bloques;
        # se acepta solo si resuelve de forma inequívoca en exactamente uno.
        for entrada in u.get("contenido_general") or []:
            hits = [
                (campo, constructor.reg.resolver(campo, entrada))
                for campo in campos
            ]
            hits = [(c, t) for c, t in hits if t is not None]
            if len(hits) == 1:
                constructor.add_evento_mapa(hits[0][0], hits[0][1], unidad)
            else:
                avisos.append((unidad, "contenido_general", entrada))
    return avisos


# --------------------------------------------------------------------------
# validación de la salida — schema general + invariantes §11.4 de la Capa 1
# --------------------------------------------------------------------------
_PROCEDENCIAS_CAPA1 = {"declarado", "reconciliado", "nuevo"}


def validar_capa1(reciclaje: dict) -> list:
    """Invariantes de la salida MECÁNICA de la Capa 1 (§11.4, ajustado v11.76).

    Complementa el chequeo estructural (`validar_schema`). La Capa 1 ahora
    resuelve mecánicamente `declarado`, `reconciliado` y `nuevo` para los 4
    bloques no-verbales (vocab/gram/pron/perif). Verbal queda sin asignar
    para que la Capa 2 lo decida. La Capa 1 sigue sin asignar etiquetas y
    sin fabricar explicacion/detalle.

    Nota: estas invariantes describen lo que la propia Capa 1 produce. Tras
    una sesión de Capa 2, las etiquetas y explicaciones legítimas conviven en
    el archivo y el validador estructural sí las acepta — `validar_capa1` se
    usa al **regenerar** sobre un archivo recién creado, no sobre uno ya
    enriquecido (por eso el flujo de merge no destructivo).
    """
    errores = []
    for h in reciclaje.get("hilos", []):
        hid = h.get("id", "<sin-id>")
        for ev in h.get("eventos", []):
            unidad = ev.get("unidad")
            proc = ev.get("procedencia_indice")
            if proc is not None and proc not in _PROCEDENCIAS_CAPA1:
                errores.append(
                    f"hilo {hid} u{unidad}: procedencia_indice '{proc}' no válido"
                )
            recon = ev.get("reconciliado_con")
            if proc == "reconciliado":
                if not isinstance(recon, str) or not (
                    recon.startswith("indice:") or recon.startswith("pcic:")
                ):
                    errores.append(
                        f"hilo {hid} u{unidad}: reconciliado_con debe empezar"
                        " por 'indice:' o 'pcic:' (schema §3, v11.76)"
                    )
            elif recon is not None:
                errores.append(
                    f"hilo {hid} u{unidad}: reconciliado_con sin procedencia"
                    " reconciliado"
                )
    return errores


# --------------------------------------------------------------------------
# merge no destructivo — Capa 1 sobreescribe lo mecánico, preserva lo editorial
# --------------------------------------------------------------------------
# Campos del evento que la Capa 1 SOBREESCRIBE en cada regeneración (mecánicos).
_EV_MECANICOS = {"unidad", "tiempo", "evidencias", "formas",
                 "procedencia_indice", "reconciliado_con"}
# Campos del evento que la Capa 1 PRESERVA del archivo previo (interpretativos
# de la Capa 2). Si vienen rellenos en el JSON existente, sobreviven al regenerar.
_EV_INTERPRETATIVOS = {"etiquetas", "explicacion"}


def _evento_tiene_enriquecimiento(ev: dict, bloque: str) -> bool:
    """True si el evento contiene material editorial (Capa 2) no recuperable
    desde inventario/registry. Disparador del abort-on-loss.

    En `verbal`, `procedencia_indice` y `reconciliado_con` son trabajo de
    Capa 2 (verbal no tiene resolución mecánica por contrato §9, v11.76) —
    también se protegen.
    """
    if ev.get("etiquetas"):
        return True
    if "explicacion" in ev:
        return True
    if bloque == "verbal" and (
        ev.get("procedencia_indice") or ev.get("reconciliado_con")
    ):
        return True
    return False


def _hilo_tiene_enriquecimiento(h: dict) -> bool:
    bloque = h.get("bloque", "")
    if "detalle" in h or h.get("nivel_analisis") == "detalle":
        return True
    return any(_evento_tiene_enriquecimiento(ev, bloque) for ev in h.get("eventos", []))


def merge_no_destructivo(nuevos: list, existentes: list) -> tuple:
    """Fusiona los hilos nuevos (Capa 1) con los del archivo previo.

    Política:
      - Capa 1 sobreescribe los campos mecánicos.
      - Preserva del archivo previo: `etiquetas`, `explicacion`, `detalle` y
        cualquier `nivel_analisis: detalle` ya alcanzado.
      - Si un hilo/evento del archivo previo desaparece de la salida nueva y
        tenía enriquecimiento editorial → se registra como **pérdida**. El
        flujo `main()` decide abortar o continuar con log.

    Devuelve `(merged, perdidas)`.
    """
    existentes_por_id = {h["id"]: h for h in existentes}
    nuevos_ids = {h["id"] for h in nuevos}
    perdidas = []
    merged = []

    for nuevo in nuevos:
        prev = existentes_por_id.get(nuevo["id"])
        if prev is None:
            merged.append(nuevo)
            continue
        # Hilo-level: empezamos por el nuevo, preservamos `detalle` y nivel si
        # el previo lo alcanzó.
        fusion = dict(nuevo)
        if prev.get("nivel_analisis") == "detalle":
            fusion["nivel_analisis"] = "detalle"
        if "detalle" in prev:
            fusion["detalle"] = prev["detalle"]

        # Eventos: cruzar por clave mecánica (unidad, tiempo).
        bloque = nuevo.get("bloque", "")
        prev_eventos = {(e["unidad"], e.get("tiempo")): e
                        for e in prev.get("eventos", [])}
        fusion_eventos = []
        for ev_n in nuevo["eventos"]:
            clave = (ev_n["unidad"], ev_n.get("tiempo"))
            ev_prev = prev_eventos.pop(clave, None)
            if ev_prev is None:
                fusion_eventos.append(ev_n)
                continue
            # Tomar mecánico del nuevo, preservar interpretativo del previo.
            ev_fusion = dict(ev_n)
            for campo in _EV_INTERPRETATIVOS:
                if campo in ev_prev and ev_prev[campo]:
                    ev_fusion[campo] = ev_prev[campo]
            # En verbal, procedencia_indice / reconciliado_con son escritos por
            # Capa 2 (no por Capa 1). Preservarlos cuando el evento nuevo no los
            # trae — si no, la regeneración los borraría silenciosamente (v11.76).
            if bloque == "verbal":
                for campo in ("procedencia_indice", "reconciliado_con"):
                    if campo not in ev_fusion and campo in ev_prev:
                        ev_fusion[campo] = ev_prev[campo]
            fusion_eventos.append(ev_fusion)
        # Eventos que estaban en el previo y ya no en el nuevo: pérdida si
        # tenían enriquecimiento.
        for clave, ev_huerfano in prev_eventos.items():
            if _evento_tiene_enriquecimiento(ev_huerfano, bloque):
                perdidas.append({
                    "tipo": "evento",
                    "hilo_id": nuevo["id"],
                    "titulo": nuevo.get("titulo"),
                    "clave_evento": {"unidad": clave[0], "tiempo": clave[1]},
                    "evento_perdido": ev_huerfano,
                })
        fusion["eventos"] = fusion_eventos
        merged.append(fusion)

    # Hilos del previo que ya no aparecen en la salida nueva.
    for hid, prev in existentes_por_id.items():
        if hid in nuevos_ids:
            continue
        if _hilo_tiene_enriquecimiento(prev):
            perdidas.append({
                "tipo": "hilo",
                "hilo_id": hid,
                "titulo": prev.get("titulo"),
                "hilo_perdido": prev,
            })

    return merged, perdidas


# --------------------------------------------------------------------------
# orquestación — modo íntegro con merge no destructivo (§11.5, v11.76)
# --------------------------------------------------------------------------
def generar() -> tuple:
    """Construye la proyección mecánica íntegra, fusionándola con el archivo
    previo de forma no destructiva.

    Devuelve `(reciclaje, descartados, avisos_indice, perdidas)`. Si `perdidas`
    es no-vacío, el `main()` decide entre abortar o continuar (flag explícito).
    """
    registries = Registries()
    curso = cargar_json(CURSO)
    indice = IndiceCurso(curso)
    constructor = Constructor(registries, indice)

    cubiertas = []
    for u in range(0, 10):
        inv_path = UNIDADES / f"U{u}" / f"U{u}-nc1-inventario.json"
        if not inv_path.exists():
            continue
        cubiertas.append(u)
        procesar_unidad(constructor, u, cargar_json(inv_path))

    avisos = procesar_indice(constructor, curso, set(cubiertas))
    constructor.finalizar_niveles()

    orden_bloque = {b: i for i, b in enumerate(
        ["vocabulario", "gramatica", "pronunciacion_ortografia", "verbal", "perifrasis"]
    )}
    hilos = sorted(
        constructor.hilos.values(),
        key=lambda h: (orden_bloque.get(h["bloque"], 99), h["id"]),
    )
    for h in hilos:
        h["eventos"].sort(key=lambda e: (e["unidad"], e.get("tiempo") or ""))

    # Merge no destructivo con el archivo previo (v11.76).
    propuestas = []
    perdidas = []
    if RECICLAJE.exists():
        previo = cargar_json(RECICLAJE)
        propuestas = previo.get("propuestas", [])
        hilos, perdidas = merge_no_destructivo(hilos, previo.get("hilos", []))

    reciclaje = {
        "_meta": {
            "version": leer_version_changelog(),
            "fecha": date.today().isoformat(),
            "unidades_cubiertas": sorted(cubiertas),
            "estado": "en construcción",
        },
        "hilos": hilos,
        "propuestas": propuestas,
    }
    return reciclaje, constructor.descartados, avisos, perdidas


def main() -> int:
    parser = argparse.ArgumentParser(description="Generador de Capa 1 de fase 2.")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="genera y valida sin escribir nc1-reciclaje.json",
    )
    parser.add_argument(
        "--permitir-perdidas", action="store_true",
        help=("permite continuar cuando el merge detecte pérdida de "
              "enriquecimiento editorial (etiquetas / explicación / detalle); "
              "vuelca el detalle de lo perdido en docs/historico/"),
    )
    args = parser.parse_args()

    reciclaje, descartados, avisos, perdidas = generar()

    n_hilos = len(reciclaje["hilos"])
    n_eventos = sum(len(h["eventos"]) for h in reciclaje["hilos"])
    niveles = Counter(h["nivel_analisis"] for h in reciclaje["hilos"])
    print(f"Capa 1 — modo íntegro")
    print(f"  unidades cubiertas : {reciclaje['_meta']['unidades_cubiertas']}")
    print(f"  hilos generados    : {n_hilos}  (auto: {niveles['auto']}, "
          f"mapa: {niveles['mapa']})")
    print(f"  eventos generados  : {n_eventos}")
    print(f"  propuestas preservadas: {len(reciclaje['propuestas'])}")

    if avisos:
        print(f"\n  ⚠ {len(avisos)} entradas del índice del curso sin resolver "
              f"a título canónico (proyección `mapa`, resolución conservadora):")
        vistos = set()
        for unidad, campo, entrada in avisos:
            if entrada in vistos:
                continue
            vistos.add(entrada)
            print(f"      [U{unidad} · {campo}] {entrada}")

    if descartados:
        print(f"\n  ⚠ {len(descartados)} contenidos descartados (fuera del "
              f"universo cerrado de registries, §11.4 invariante 3):")
        vistos = set()
        for bloque, titulo, unidad in descartados:
            clave = (bloque, titulo)
            if clave in vistos:
                continue
            vistos.add(clave)
            print(f"      [{bloque}] {titulo}  (primera vez en U{unidad})")

    # Política de merge no destructivo (v11.76): abort-on-loss por defecto.
    if perdidas:
        print(f"\n✗ Pérdida de enriquecimiento editorial detectada — "
              f"{len(perdidas)} elementos del archivo previo desaparecerían:")
        for p in perdidas[:10]:
            if p["tipo"] == "evento":
                k = p["clave_evento"]
                print(f"    [evento] hilo '{p['titulo']}' u{k['unidad']}"
                      f"{' · ' + k['tiempo'] if k['tiempo'] else ''}")
            else:
                print(f"    [hilo]   '{p['titulo']}' ({p['hilo_id']})")
        if len(perdidas) > 10:
            print(f"    ... y {len(perdidas) - 10} más")
        if not args.permitir_perdidas:
            print("\nLa regeneración aborta para evitar pérdida silenciosa de "
                  "trabajo editorial. Para continuar conscientemente, repite "
                  "con --permitir-perdidas (el detalle de lo perdido se vuelca "
                  "en docs/historico/).")
            return 2
        # Continuar: volcar el log.
        ruta_log = (PROJECT / "docs" / "historico" /
                    f"reciclaje-merge-loss-{date.today().isoformat()}.json")
        ruta_log.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta_log, "w", encoding="utf-8") as fh:
            json.dump({"fecha": date.today().isoformat(),
                       "version": leer_version_changelog(),
                       "perdidas": perdidas}, fh, ensure_ascii=False, indent=2)
        print(f"\n  ⚠ --permitir-perdidas activo → continúa. Log en "
              f"{ruta_log.relative_to(PROJECT)}")

    # chequeo estructural compartido (gate §13 a) + invariantes §11.4 de Capa 1
    errores = validar_schema(reciclaje) + validar_capa1(reciclaje)
    if errores:
        print(f"\n✗ Validación FALLIDA — {len(errores)} errores:")
        for e in errores:
            print(f"    - {e}")
        print("\nNo se escribe nc1-reciclaje.json.")
        return 1

    print("\n✓ Validación superada (schema-reciclaje.md + invariantes §11.4).")

    if args.dry_run:
        print("[--dry-run] No se escribe nc1-reciclaje.json.")
        return 0

    with open(RECICLAJE, "w", encoding="utf-8") as fh:
        json.dump(reciclaje, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"✓ Escrito {RECICLAJE.relative_to(PROJECT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())