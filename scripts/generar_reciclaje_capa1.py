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

# campo de `nc1-curso.json` que indexa cada bloque, para el triage `declarado`
CURSO_CAMPO = {
    "vocabulario": "vocabulario",
    "gramatica": "gramatica",
    "pronunciacion_ortografia": "pronunciacion_ortografia",
}


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
        # canónico -> conjunto de aliases del índice (para el triage `declarado`)
        self.vocab = {}
        for c in campos:
            self.vocab[c["canonico"]] = {
                slug(a) for a in c.get("aliases_indice", [])
            }

        gram = cargar_json(REG_GRAMATICA)["categorias"]
        # categoría -> _grupo
        self.gramatica = {k: v.get("_grupo") for k, v in gram.items()}

        pron = cargar_json(REG_PRONORTO)["categorias"]
        self.pronorto = set(pron.keys())

        self.verbos = set(cargar_json(REG_VERBOS)["verbos"].keys())
        self.perifrasis = set(cargar_json(REG_PERIFRASIS)["perifrasis"].keys())

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
    """Entradas del índice editorial por unidad y bloque, ya slugificadas."""

    def __init__(self, curso: dict):
        # (unidad, campo_curso) -> conjunto de slugs de entradas del índice
        self._idx = {}
        # entradas planas por unidad (U0 usa `contenido_general` para todo)
        self._general = {}
        for u in curso.get("unidades", []):
            num = u["unidad"]
            for campo in ("vocabulario", "gramatica", "pronunciacion_ortografia"):
                valor = u.get(campo)
                if valor is None:
                    continue
                items = [valor] if isinstance(valor, str) else valor
                self._idx[(num, campo)] = {slug(x) for x in items}
            general = u.get("contenido_general") or []
            self._general[num] = {slug(x) for x in general}

    def declarado(self, unidad: int, bloque: str, titulo: str,
                  aliases: set) -> bool:
        """True si `titulo` coincide literalmente con una entrada del índice.

        Coincidencia mecánica (§11.3): igualdad de slug, prefijo del slug del
        índice (absorbe paréntesis del índice como '... (el, la, los, las)'),
        o coincidencia con un alias del índice declarado en el registry.
        """
        campo = CURSO_CAMPO.get(bloque)
        objetivo = slug(titulo)
        candidatos = set(self._general.get(unidad, set()))
        if campo is not None:
            candidatos |= self._idx.get((unidad, campo), set())
        for entrada in candidatos:
            if entrada == objetivo or entrada.startswith(objetivo + "-"):
                return True
            if entrada in aliases:
                return True
        return False


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
            "etiquetas": [],  # vacío: lo puebla la Capa 2 (§11.2)
            "evidencias": sorted(set(evidencias or [])),
        }
        if tiempo is not None:
            evento["tiempo"] = tiempo
        if bloque == "verbal":
            evento["formas"] = sorted(set(formas or []))
        # triage mecánico: solo `declarado` (§11.2, §11.4 invariante 8)
        aliases = self.reg.vocab.get(titulo, set()) if bloque == "vocabulario" else set()
        if self.indice.declarado(unidad, bloque, titulo, aliases):
            evento["procedencia_indice"] = "declarado"
        hilo["eventos"].append(evento)

    def add_evento_mapa(self, bloque: str, titulo: str, unidad: int):
        """Registra un evento de nivel `mapa` desde el índice del curso (§4.2).

        `titulo` ya viene resuelto y es canónico (`Registries.resolver`). El
        evento no lleva evidencias ni etiquetas. Si ya existe un evento para
        esa `(unidad)` —procedente de inventario—, no lo pisa: solo garantiza
        el triage `declarado` (la entrada está en el índice por definición).
        """
        self.unidades.add(unidad)
        hilo = self._hilo(bloque, titulo)
        for ev in hilo["eventos"]:
            if ev["unidad"] == unidad and ev.get("tiempo") is None:
                ev["procedencia_indice"] = "declarado"
                return
        hilo["eventos"].append({
            "unidad": unidad,
            "etiquetas": [],
            "evidencias": [],
            "procedencia_indice": "declarado",
        })

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
def validar_capa1(reciclaje: dict) -> list:
    """Invariantes específicas de la SALIDA de la Capa 1 (§11.4).

    Complementa al chequeo estructural general (`validar_schema`, en
    `validar_reciclaje.py`): comprueba lo que la Capa 1 promete por encima
    del schema — no asigna etiquetas, no escribe `reconciliado`/`nuevo`, no
    fabrica `explicacion`/`detalle`. Estas comprobaciones NO aplican a un
    `nc1-reciclaje.json` enriquecido por la Capa 2, por eso viven aquí y no
    en el validador estructural compartido.
    """
    errores = []
    for h in reciclaje.get("hilos", []):
        hid = h.get("id", "<sin-id>")
        # la Capa 1 nunca fabrica el nivel `detalle` (invariante 9)
        if "detalle" in h:
            errores.append(
                f"hilo {hid}: 'detalle' presente en salida de Capa 1 (invariante 9)"
            )
        for ev in h.get("eventos", []):
            unidad = ev.get("unidad")
            # la Capa 1 nunca asigna etiquetas (invariante 9)
            if ev.get("etiquetas"):
                errores.append(
                    f"hilo {hid} u{unidad}: etiquetas no vacías en salida de Capa 1"
                    " (invariante 9)"
                )
            # triage: la Capa 1 solo escribe `declarado` (invariante 8)
            proc = ev.get("procedencia_indice")
            if proc is not None and proc != "declarado":
                errores.append(
                    f"hilo {hid} u{unidad}: procedencia_indice '{proc}'"
                    " no permitido en Capa 1 (invariante 8)"
                )
            # la Capa 1 nunca fabrica contenido editorial (invariante 9)
            if "explicacion" in ev:
                errores.append(
                    f"hilo {hid} u{unidad}: 'explicacion' presente en salida"
                    " de Capa 1 (invariante 9)"
                )
    return errores


# --------------------------------------------------------------------------
# orquestación — modo íntegro (§11.5)
# --------------------------------------------------------------------------
def generar() -> tuple:
    """Construye la proyección mecánica íntegra.

    Devuelve `(reciclaje, descartados, avisos_indice)`.
    """
    registries = Registries()
    curso = cargar_json(CURSO)
    indice = IndiceCurso(curso)
    constructor = Constructor(registries, indice)

    # pasada `auto`: hilos y eventos desde los inventarios cerrados (§11.2)
    cubiertas = []
    for u in range(0, 10):
        inv_path = UNIDADES / f"U{u}" / f"U{u}-nc1-inventario.json"
        if not inv_path.exists():
            continue
        cubiertas.append(u)
        procesar_unidad(constructor, u, cargar_json(inv_path))

    # pasada `mapa`: siembra desde el índice del curso (§4.2, §4.5)
    avisos = procesar_indice(constructor, curso, set(cubiertas))

    # nivel definitivo de cada hilo según el grado de población alcanzado
    constructor.finalizar_niveles()

    # ordenación estable: por bloque y luego por id
    orden_bloque = {b: i for i, b in enumerate(
        ["vocabulario", "gramatica", "pronunciacion_ortografia", "verbal", "perifrasis"]
    )}
    hilos = sorted(
        constructor.hilos.values(),
        key=lambda h: (orden_bloque.get(h["bloque"], 99), h["id"]),
    )
    for h in hilos:
        h["eventos"].sort(key=lambda e: (e["unidad"], e.get("tiempo") or ""))

    # preservación de propuestas[] y cierres humanos (§11.1 input 4, §11.4.10)
    propuestas = []
    if RECICLAJE.exists():
        previo = cargar_json(RECICLAJE)
        propuestas = previo.get("propuestas", [])

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
    return reciclaje, constructor.descartados, avisos


def main() -> int:
    parser = argparse.ArgumentParser(description="Generador de Capa 1 de fase 2.")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="genera y valida sin escribir nc1-reciclaje.json",
    )
    args = parser.parse_args()

    reciclaje, descartados, avisos = generar()

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