#!/usr/bin/env python3
"""
Validador cross-unidad R1-R5 — componente (b) del gate de cierre §13.

Implementa el contrato de `reglas-reciclaje.md` §14: cinco reglas de control
de calidad cruzado entre las unidades de fase 1, que se ejecutan sobre los
inventarios `UX-nc1-inventario.json` antes de dar por cerrado el reciclaje.

Naturaleza de cada regla (§14):
  - R2, R5 — PRE-CONDICIONES. Un fallo es bug de extracción de fase 1; el
    validador ABORTA (no procesa R1/R3/R4). Aquí se delegan a la verificación
    de integridad de fase 1, que ya las cubre (regla de oro 4 — fuente única):
        R2 (materialidad/trazabilidad) ⊂ verificar_integridad.py chequeo 1
           (delegado a validar_inventario.py §5.10 A) + chequeo 3 (fuentes).
        R5 (coherencia bidireccional)  ⊂ verificar_integridad.py chequeo 5
           (consolidados derivables desde paginas_detalle).
  - R1, R3, R4 — ALERTAS. No abortan; entran en el criterio de cierre §13
    (no deben quedar alertas sin resolver). Se calculan aquí.

R1 — versión PROXY determinista (decidida 2026-05-22). El R1 del contrato
mira frecuencia de léxico sobre el texto crudo de las actividades; eso es
ruidoso (stopwords, morfología, instrucciones). Esta primera iteración usa
solo lo ya estructurado y trazable de fase 1: detecta contenido consolidado
como `recurrente` en U(n) cuyo `principal` aparece por primera vez en una
unidad posterior — anticipación material trazable. No cubre léxico que nunca
llegó al consolidado; esa cobertura queda para un R1 con frecuencia, fuera
del gate, si más adelante se decide.

Códigos de salida:
    0 — limpio (pre-condiciones OK, sin alertas).
    1 — pre-condiciones OK pero hay alertas R1/R3/R4 sin resolver.
    2 — pre-condición R2/R5 fallida: el validador aborta.

Uso:
    python3 scripts/validar_cross_unidad.py
"""
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
UNIDADES = PROJECT / "unidades"
SCRIPTS = PROJECT / "scripts"
FASE1 = PROJECT / "fases" / "1-extraccion-inventario"

VERIFICAR_INTEGRIDAD = SCRIPTS / "verificar_integridad.py"

REG_CAMPOS = FASE1 / "campos-semanticos-canonicos.json"
REG_GRAMATICA = FASE1 / "gramatica-canonica.json"
REG_PRONORTO = FASE1 / "pronunciacion-ortografia-canonica.json"
REG_VERBOS = FASE1 / "verbos-canonicos.json"

# bloque del reciclaje -> clave del bloque consolidado en el inventario
CONSOLIDADO = {
    "vocabulario": "vocabulario_consolidado",
    "gramatica": "gramatica_consolidada",
    "pronunciacion_ortografia": "pronunciacion_ortografia_consolidada",
}

# chequeos de verificar_integridad.py que cubren las pre-condiciones R2/R5
# (1 schema+materialidad · 2 refs canónicas · 3 fuentes · 5 coherencia interna)
CHEQUEOS_PRECONDICION = {1, 2, 3, 5}


def cargar_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def slug(s: str) -> str:
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.lower().strip()


def cargar_inventarios() -> dict:
    """Devuelve {unidad: inventario} de las unidades con inventario presente."""
    inventarios = {}
    for u in range(0, 10):
        path = UNIDADES / f"U{u}" / f"U{u}-nc1-inventario.json"
        if path.exists():
            inventarios[u] = cargar_json(path)
    return inventarios


# --------------------------------------------------------------------------
# pre-condiciones R2/R5 — delegadas a verificar_integridad.py
# --------------------------------------------------------------------------
def comprobar_precondiciones() -> tuple:
    """Ejecuta `verificar_integridad.py` y lee su resumen por chequeo.

    Devuelve `(ok, fallos_precondicion, otros_fallos)`:
      - `ok`: True si los chequeos R2/R5 (CHEQUEOS_PRECONDICION) están en 0 errores.
      - `fallos_precondicion`: líneas de los chequeos R2/R5 con errores.
      - `otros_fallos`: líneas del resto de chequeos con errores (informativo —
        p. ej. el chequeo 4 cabecera↔curso, ajeno a R2/R5).
    """
    res = subprocess.run(
        [sys.executable, str(VERIFICAR_INTEGRIDAD)],
        capture_output=True, text=True,
    )
    fallos_precondicion, otros_fallos = [], []
    patron = re.compile(r"^(✅|❌)\s+(\d+)\.\s+(.*?):\s+(\d+)\s+errores")
    for linea in res.stdout.splitlines():
        m = patron.match(linea.strip())
        if not m:
            continue
        numero, nombre, errores = int(m.group(2)), m.group(3), int(m.group(4))
        if errores == 0:
            continue
        entrada = f"chequeo {numero} ({nombre}): {errores} errores"
        if numero in CHEQUEOS_PRECONDICION:
            fallos_precondicion.append(entrada)
        else:
            otros_fallos.append(entrada)
    ok = not fallos_precondicion
    return ok, fallos_precondicion, otros_fallos


# --------------------------------------------------------------------------
# utilidades de tiers principal/recurrente
# --------------------------------------------------------------------------
def tiers_por_unidad(inventarios: dict, bloque: str) -> tuple:
    """Devuelve `(principal, recurrente)`: dict {unidad: set(categorías)}."""
    clave = CONSOLIDADO[bloque]
    principal, recurrente = {}, {}
    for u, inv in inventarios.items():
        bd = inv.get(clave) or {}
        principal[u] = set((bd.get("principal") or {}).keys())
        recurrente[u] = set((bd.get("recurrente") or {}).keys())
    return principal, recurrente


# --------------------------------------------------------------------------
# R1 — anticipación de léxico (versión proxy determinista, §14 + decisión 2026-05-22)
# --------------------------------------------------------------------------
def regla_r1(inventarios: dict) -> list:
    """Alerta: categoría `recurrente` en U(n) cuyo `principal` es posterior."""
    alertas = []
    for bloque in CONSOLIDADO:
        principal, recurrente = tiers_por_unidad(inventarios, bloque)
        primer_principal = {}
        for u in sorted(principal):
            for cat in principal[u]:
                primer_principal.setdefault(cat, u)
        for u in sorted(recurrente):
            for cat in recurrente[u]:
                if cat in principal.get(u, set()):
                    continue
                fp = primer_principal.get(cat)
                if fp is not None and fp > u:
                    alertas.append({
                        "regla": "R1", "bloque": bloque, "unidad": u,
                        "contenido": cat, "unidad_canonica": fp,
                        "detalle": (f"'{cat}' es recurrente en U{u} pero su "
                                    f"principal aparece por primera vez en "
                                    f"U{fp} — anticipación material"),
                    })
    return alertas


# --------------------------------------------------------------------------
# R3 — errores de clasificación por dimensión (§14)
# --------------------------------------------------------------------------
def regla_r3(inventarios: dict, registries: dict) -> list:
    """Alerta: categoría consolidada en un bloque pero canónica de otra dimensión."""
    alertas = []
    por_bloque = {
        "vocabulario": registries["campos"],
        "gramatica": registries["gramatica"],
        "pronunciacion_ortografia": registries["pronorto"],
    }
    for u, inv in sorted(inventarios.items()):
        for bloque, clave in CONSOLIDADO.items():
            propio = por_bloque[bloque]
            otros = {b: r for b, r in por_bloque.items() if b != bloque}
            bd = inv.get(clave) or {}
            for tier in ("principal", "recurrente"):
                for cat in (bd.get(tier) or {}):
                    if cat in propio:
                        continue  # canónico en su dimensión → correcto
                    # no está en su registry: ¿es canónico en otra dimensión?
                    for otro_bloque, otro_reg in otros.items():
                        if cat in otro_reg:
                            alertas.append({
                                "regla": "R3", "bloque": bloque, "unidad": u,
                                "contenido": cat,
                                "detalle": (f"'{cat}' está en {clave} de U{u} "
                                            f"pero es canónico de la dimensión "
                                            f"'{otro_bloque}'"),
                            })
    return alertas


# --------------------------------------------------------------------------
# R4 — inconsistencias de progresión (§14)
# --------------------------------------------------------------------------
def regla_r4(inventarios: dict, registries: dict) -> list:
    """Alertas: (a) `recurrente` que nunca es `principal`; (b) lemas verbales
    ubicados en `vocabulario_consolidado`."""
    alertas = []

    # (a) recurrente en U(n) que no es principal en ninguna unidad
    for bloque in CONSOLIDADO:
        principal, recurrente = tiers_por_unidad(inventarios, bloque)
        cats_principal = set()
        for cats in principal.values():
            cats_principal |= cats
        for u in sorted(recurrente):
            for cat in recurrente[u]:
                if cat not in cats_principal:
                    alertas.append({
                        "regla": "R4", "bloque": bloque, "unidad": u,
                        "contenido": cat,
                        "detalle": (f"'{cat}' aparece como recurrente en U{u} "
                                    f"pero nunca es principal en ninguna unidad"),
                    })

    # (b) lemas verbales en vocabulario_consolidado
    verbos = registries["verbos"]
    for u, inv in sorted(inventarios.items()):
        vc = inv.get("vocabulario_consolidado") or {}
        for tier in ("principal", "recurrente"):
            for cat, catdata in (vc.get(tier) or {}).items():
                if not isinstance(catdata, dict):
                    continue
                for item in catdata.get("items") or []:
                    palabra = (item.get("palabra") or "").strip()
                    if slug(palabra) in verbos:
                        alertas.append({
                            "regla": "R4", "bloque": "vocabulario", "unidad": u,
                            "contenido": palabra,
                            "detalle": (f"'{palabra}' en vocabulario_consolidado "
                                        f"de U{u} ({tier}.'{cat}') es un lema "
                                        f"verbal canónico — debería vivir en "
                                        f"tiempos_y_verbos_consolidado"),
                        })
    return alertas


def cargar_registries() -> dict:
    """Carga los conjuntos de nombres canónicos de los registries de fase 1."""
    campos = {c["canonico"] for c in cargar_json(REG_CAMPOS)["campos"]}
    gramatica = set(cargar_json(REG_GRAMATICA)["categorias"].keys())
    pronorto = set(cargar_json(REG_PRONORTO)["categorias"].keys())
    verbos = {slug(v) for v in cargar_json(REG_VERBOS)["verbos"].keys()}
    return {
        "campos": campos, "gramatica": gramatica,
        "pronorto": pronorto, "verbos": verbos,
    }


def main() -> int:
    inventarios = cargar_inventarios()
    print("Validador cross-unidad R1-R5 — fase 2")
    print(f"  unidades con inventario: {sorted(inventarios)}")

    # --- pre-condiciones R2/R5 (abortan si fallan) -------------------------
    ok, fallos_pre, otros = comprobar_precondiciones()
    if otros:
        print("\n  ⓘ Integridad fase 1 — fallos ajenos a R2/R5 (informativo, "
              "no aborta):")
        for f in otros:
            print(f"      {f}")
    if not ok:
        print("\n✗ Pre-condición R2/R5 FALLIDA — un fallo es bug de fase 1:")
        for f in fallos_pre:
            print(f"      {f}")
        print("\nEl validador cross-unidad ABORTA (§14). No se procesan R1/R3/R4.")
        return 2
    print("  ✓ Pre-condiciones R2/R5: verificar_integridad.py chequeos "
          f"{sorted(CHEQUEOS_PRECONDICION)} sin errores.")

    # --- R1/R3/R4 (alertas) ------------------------------------------------
    registries = cargar_registries()
    alertas = (
        regla_r1(inventarios)
        + regla_r3(inventarios, registries)
        + regla_r4(inventarios, registries)
    )

    if not alertas:
        print("\n✓ R1/R3/R4: 0 alertas. Gate cross-unidad limpio.")
        return 0

    por_regla = {}
    for a in alertas:
        por_regla.setdefault(a["regla"], []).append(a)
    print(f"\n⚠ {len(alertas)} alertas R1/R3/R4 (entran en el criterio de "
          f"cierre §13 — no deben quedar sin resolver):")
    for regla in ("R1", "R3", "R4"):
        grupo = por_regla.get(regla, [])
        if not grupo:
            continue
        print(f"\n  {regla} — {len(grupo)} alertas:")
        for a in grupo:
            print(f"      [U{a['unidad']} · {a['bloque']}] {a['detalle']}")
    return 1


if __name__ == "__main__":
    sys.exit(main())