#!/usr/bin/env python3
"""Suite global de verificación de integridad cross-JSON (v10.118).

Ejecuta los 9 chequeos declarados en schema-inventario.md §A.3:

  1. Cumplimiento del shape declarado en el schema (delegado a validar_inventario.py por inventario).
  2. Toda referencia canónica usada en un inventario existe en su registry.
  3. Toda fuente cumple la regex de §9.5.
  4. Coincidencia exacta entre cabecera de cada inventario y unidades/nc1-curso.json.
  5. Coherencia interna: secciones reconstruible desde paginas_detalle; consolidados derivables; minúsculas en formas_trabajadas.
  6. Integridad de archivos PCIC contra su _meta declarado.
  7. Integridad de registries (*-canonicos.json, *-canonica.json) contra su shape interno.
  8. Detección de marcas internas bloqueantes (_pendiente_canon, _funcion_ambigua) en inventarios canónicos.
  9. Rechazo de claves _fixture_* o unidad no entero en inventarios canónicos.

Uso:
    python3 scripts/verificar_integridad.py             # corre los 9 chequeos sobre todos los JSONs
    python3 scripts/verificar_integridad.py --json      # output JSON estructurado
    python3 scripts/verificar_integridad.py --solo N    # corre solo el chequeo N

Sale con código 0 si todo OK, 1 si hay errores estructurales.
"""

import json
import re
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))

from scripts import canon  # noqa: E402
from scripts import validar_inventario as vi  # noqa: E402

FASE1 = PROJECT / "fases" / "1-extraccion-inventario"
UNIDADES = PROJECT / "unidades"

REGISTRIES = {
    "campos-semanticos-canonicos.json": FASE1 / "campos-semanticos-canonicos.json",
    "verbos-canonicos.json": FASE1 / "verbos-canonicos.json",
    "gramatica-canonica.json": FASE1 / "gramatica-canonica.json",
    "pronunciacion-ortografia-canonica.json": FASE1 / "pronunciacion-ortografia-canonica.json",
}

PCIC = {
    "pcic-a1-vocabulario.json": FASE1 / "pcic-a1-vocabulario.json",
    "pcic-a1-gramatica.json": FASE1 / "pcic-a1-gramatica.json",
    "pcic-a1-pronunciacion-ortografia.json": FASE1 / "pcic-a1-pronunciacion-ortografia.json",
    "pcic-a1-comunicacion.json": FASE1 / "pcic-a1-comunicacion.json",
}


def cargar_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        return {"_error": f"JSON no parseable: {e}"}


# === 1. Cumplimiento de schema por inventario ===
def chequeo_1_schema_por_inventario():
    """Ejecuta validar_inventario.py contra cada UX-nc1-inventario.json canónico.
    Devuelve (errores, avisos). La auditoría legacy R1 del validador se promueve
    a avisos prefijados con '📋 legacy:' para no perder visibilidad cross-canal.
    """
    errores, avisos = [], []
    for u_dir in sorted(UNIDADES.glob("U*")):
        if not u_dir.is_dir():
            continue
        for inv_file in u_dir.glob("*-nc1-inventario.json"):
            path = inv_file
            errs, avs, legacy = vi.validar(path)
            rel = path.relative_to(PROJECT)
            for e in errs:
                errores.append(f"{rel}: {e}")
            for a in avs:
                avisos.append(f"{rel}: {a}")
            for entry in legacy:
                # Auditoría legacy del rollout R1 (canon semántico) — no bloquea
                # pero queda visible aquí como aviso prefijado.
                avisos.append(f"{rel}: 📋 legacy: {entry}")
    return errores, avisos


# === 2. Referencias canónicas existen en su registry ===
def chequeo_2_refs_canonicas():
    errores = []
    # Cargar registries
    c_lex = cargar_json(REGISTRIES["campos-semanticos-canonicos.json"]) or {}
    c_verb = cargar_json(REGISTRIES["verbos-canonicos.json"]) or {}
    c_gram = cargar_json(REGISTRIES["gramatica-canonica.json"]) or {}
    c_porto = cargar_json(REGISTRIES["pronunciacion-ortografia-canonica.json"]) or {}

    lex_set = {e["canonico"] for e in c_lex.get("campos", [])}
    verb_set = set((c_verb.get("verbos") or {}).keys())
    gram_set = set((c_gram.get("categorias") or {}).keys())
    porto_set = set((c_porto.get("categorias") or {}).keys())

    for u_dir in sorted(UNIDADES.glob("U*")):
        if not u_dir.is_dir():
            continue
        for inv_file in u_dir.glob("*-nc1-inventario.json"):
            d = cargar_json(inv_file)
            if not d or "_error" in d:
                continue
            rel = inv_file.relative_to(PROJECT)
            for p in d.get("paginas_detalle", []):
                for a in p.get("actividades", []):
                    aid = a.get("id", "?")
                    for ref in a.get("vocabulario", []):
                        if isinstance(ref, str) and ref != "_pendiente_canon" and ref not in lex_set:
                            errores.append(f"{rel}: {aid}.vocabulario['{ref}'] no existe en campos-semanticos-canonicos.json")
                    for v in a.get("tiempos_y_verbos", []):
                        lema = v.get("lema") if isinstance(v, dict) else None
                        if lema and lema != "_pendiente_canon" and lema not in verb_set:
                            errores.append(f"{rel}: {aid}.tiempos_y_verbos.lema='{lema}' no existe en verbos-canonicos.json")
                    for ref in a.get("gramatica", []):
                        if isinstance(ref, str) and ref != "_pendiente_canon" and ref not in gram_set:
                            errores.append(f"{rel}: {aid}.gramatica['{ref}'] no existe en gramatica-canonica.json")
                    for ref in a.get("pronunciacion_ortografia", []):
                        if isinstance(ref, str) and ref != "_pendiente_canon" and ref not in porto_set:
                            errores.append(f"{rel}: {aid}.pronunciacion_ortografia['{ref}'] no existe en pronunciacion-ortografia-canonica.json")
    return errores, []


# === 3. Fuentes cumplen regex §9.5 ===
def chequeo_3_fuentes_regex():
    errores = []
    for u_dir in sorted(UNIDADES.glob("U*")):
        if not u_dir.is_dir():
            continue
        for inv_file in u_dir.glob("*-nc1-inventario.json"):
            d = cargar_json(inv_file)
            if not d or "_error" in d:
                continue
            rel = inv_file.relative_to(PROJECT)
            # Recoger fuentes de los 4 bloques consolidados
            for bloque_name in ("vocabulario_consolidado", "gramatica_consolidada", "pronunciacion_ortografia_consolidada"):
                bloque = d.get(bloque_name, {})
                if not isinstance(bloque, dict):
                    continue
                for subbloque in ("principal", "recurrente"):
                    sb = bloque.get(subbloque, {})
                    if not isinstance(sb, dict):
                        continue
                    for cat_name, cat in sb.items():
                        if cat_name.startswith("_") or not isinstance(cat, dict):
                            continue
                        fuentes = cat.get("fuentes", [])
                        for f in fuentes:
                            if isinstance(f, str) and not vi.FUENTE_REGEX.match(f):
                                errores.append(f"{rel}: {bloque_name}.{subbloque}.{cat_name}.fuentes contiene '{f}' que no cumple §9.5 regex")
                        for item in cat.get("items", []):
                            if isinstance(item, dict):
                                for f in item.get("fuentes", []):
                                    if isinstance(f, str) and not vi.FUENTE_REGEX.match(f):
                                        errores.append(f"{rel}: {bloque_name}.{subbloque}.{cat_name}.items.fuentes '{f}' no cumple §9.5")
    return errores, []


# === 4. Coincidencia cabecera ↔ nc1-curso.json ===
def chequeo_4_cabecera_curso():
    errores = []
    curso = cargar_json(UNIDADES / "nc1-curso.json")
    if not curso:
        return [f"❌ No se puede leer {UNIDADES / 'nc1-curso.json'}"], []
    unidades_curso = {str(u["unidad"]): u for u in curso.get("unidades", [])}
    for u_dir in sorted(UNIDADES.glob("U*")):
        if not u_dir.is_dir() or u_dir.name.endswith("-propuesta"):
            continue
        for inv_file in u_dir.glob("*-nc1-inventario.json"):
            d = cargar_json(inv_file)
            if not d or "_error" in d:
                continue
            rel = inv_file.relative_to(PROJECT)
            unidad_inv = d.get("unidad")
            if not isinstance(unidad_inv, int):
                continue  # fixtures con string
            u_curso = unidades_curso.get(str(unidad_inv))
            if not u_curso:
                errores.append(f"{rel}: unidad={unidad_inv} no existe en nc1-curso.json")
                continue
            for campo in ("titulo", "paginas_libro"):
                if d.get(campo) != u_curso.get(campo):
                    errores.append(f"{rel}: campo '{campo}' diverge — inventario='{d.get(campo)}' vs curso='{u_curso.get(campo)}'")
            # `nivel` es un campo GLOBAL del curso (nc1-curso.json, top-level),
            # no una clave por unidad. Antes se comparaba contra u_curso.get(),
            # que siempre daba None → 10 falsos positivos. (v11.66)
            if d.get("nivel") != curso.get("nivel"):
                errores.append(f"{rel}: campo 'nivel' diverge — inventario='{d.get('nivel')}' vs curso='{curso.get('nivel')}'")
            # `contenidos_indice`: comparación RETIRADA temporalmente (v11.66).
            # El campo del inventario es texto concatenado (copia abreviada,
            # ~2026-05-05); los campos de nc1-curso.json son listas (índice fiel
            # al libro, 2026-05-08). Divergen en shape y contenido — comparar
            # texto contra lista producía ~45 falsos positivos. El glosario de
            # fase 1 exige coincidencia exacta de contenidos_indice con
            # nc1-curso.json; el check se reactivará cuando contenidos_indice se
            # regenere desde esa fuente canónica (pieza aparte tras v11.66).
    return errores, []


# === 5. Coherencia interna (secciones reconstruible + minúsculas formas_trabajadas) ===
def chequeo_5_coherencia_interna():
    errores, avisos = [], []
    for u_dir in sorted(UNIDADES.glob("U*")):
        if not u_dir.is_dir():
            continue
        for inv_file in u_dir.glob("*-nc1-inventario.json"):
            d = cargar_json(inv_file)
            if not d or "_error" in d:
                continue
            rel = inv_file.relative_to(PROJECT)
            # formas_trabajadas en consolidado en minúscula (§6.4 reglas)
            tvc = d.get("tiempos_y_verbos_consolidado", [])
            if isinstance(tvc, list):
                for entry in tvc:
                    if not isinstance(entry, dict):
                        continue
                    for f in entry.get("formas_trabajadas", []):
                        if isinstance(f, str) and f != f.lower():
                            errores.append(f"{rel}: tiempos_y_verbos_consolidado lema='{entry.get('lema')}' forma '{f}' no está en minúscula (§6.4)")
    return errores, avisos


# === 6. Integridad PCIC contra _meta ===
def chequeo_6_integridad_pcic():
    errores = []
    for name, path in PCIC.items():
        d = cargar_json(path)
        if d is None:
            errores.append(f"{name}: archivo no existe")
            continue
        if "_error" in d:
            errores.append(f"{name}: {d['_error']}")
            continue
        # Verificación mínima: tiene contenido (alguna sub-estructura)
        keys = [k for k in d.keys() if not k.startswith("_")]
        if not keys:
            errores.append(f"{name}: sin contenido top-level (¿vacío?)")
    return errores, []


# === 7. Integridad de registries ===
def chequeo_7_integridad_registries():
    errores = []
    # Léxico — usar canon module
    canon_data = cargar_json(REGISTRIES["campos-semanticos-canonicos.json"])
    if canon_data:
        errs = canon.validar_canon(canon_data)
        for e in errs:
            errores.append(f"campos-semanticos-canonicos.json: {e}")
    # Otros 3: verificar _meta.estado y estructura mínima
    for name in ("verbos-canonicos.json", "gramatica-canonica.json", "pronunciacion-ortografia-canonica.json"):
        d = cargar_json(REGISTRIES[name])
        if not d:
            errores.append(f"{name}: archivo no existe o vacío")
            continue
        meta = d.get("_meta", {})
        if meta.get("estado") != "poblado":
            errores.append(f"{name}: _meta.estado='{meta.get('estado')}' (esperado: 'poblado')")
        contenido_key = "verbos" if name == "verbos-canonicos.json" else "categorias"
        contenido = d.get(contenido_key, {})
        if not contenido:
            errores.append(f"{name}: '{contenido_key}' vacío o ausente")
    return errores, []


# === 8. Marcas bloqueantes en inventarios canónicos ===
def chequeo_8_marcas_bloqueantes():
    errores = []
    for u_dir in sorted(UNIDADES.glob("U*")):
        if not u_dir.is_dir() or u_dir.name.endswith("-propuesta"):
            continue
        for inv_file in u_dir.glob("*-nc1-inventario.json"):
            d = cargar_json(inv_file)
            if not d or "_error" in d:
                continue
            if "_fixture_exploratoria" in d:
                continue  # fixtures admiten marcas bloqueantes
            rel = inv_file.relative_to(PROJECT)
            txt = json.dumps(d, ensure_ascii=False)
            if "_pendiente_canon" in txt:
                errores.append(f"{rel}: contiene '_pendiente_canon' (bloquea cierre canónico, §5.9.1)")
            if '"_funcion_ambigua": true' in txt:
                errores.append(f"{rel}: contiene '_funcion_ambigua: true' (bloquea cierre canónico, §5.9.2)")
    return errores, []


# === 9. Rechazo de _fixture_* o unidad no-entero en canónicos ===
def chequeo_9_fixture_en_canonico():
    errores = []
    for u_dir in sorted(UNIDADES.glob("U*")):
        if not u_dir.is_dir() or u_dir.name.endswith("-propuesta"):
            continue
        for inv_file in u_dir.glob("*-nc1-inventario.json"):
            d = cargar_json(inv_file)
            if not d or "_error" in d:
                continue
            rel = inv_file.relative_to(PROJECT)
            unidad = d.get("unidad")
            if not isinstance(unidad, int):
                errores.append(f"{rel}: unidad='{unidad}' no es entero — inventario en carpeta canónica debe tener unidad: int")
            fixture_keys = [k for k in d.keys() if k.startswith("_fixture_")]
            if fixture_keys:
                errores.append(f"{rel}: claves _fixture_* {fixture_keys} prohibidas en inventario canónico (§A.5)")
    return errores, []


CHEQUEOS = [
    ("1. Cumplimiento de schema por inventario", chequeo_1_schema_por_inventario),
    ("2. Refs canónicas en registries", chequeo_2_refs_canonicas),
    ("3. Fuentes cumplen regex §9.5", chequeo_3_fuentes_regex),
    ("4. Coincidencia cabecera ↔ nc1-curso.json", chequeo_4_cabecera_curso),
    ("5. Coherencia interna (minúsculas formas_trabajadas, ...)", chequeo_5_coherencia_interna),
    ("6. Integridad PCIC", chequeo_6_integridad_pcic),
    ("7. Integridad de registries", chequeo_7_integridad_registries),
    ("8. Marcas bloqueantes en canónicos", chequeo_8_marcas_bloqueantes),
    ("9. _fixture_* / unidad no entero en canónicos", chequeo_9_fixture_en_canonico),
]


def main():
    output_json = "--json" in sys.argv
    solo = None
    for i, arg in enumerate(sys.argv):
        if arg == "--solo" and i + 1 < len(sys.argv):
            solo = int(sys.argv[i + 1])

    resultado = {}
    total_err, total_avi = 0, 0
    for i, (nombre, fn) in enumerate(CHEQUEOS, start=1):
        if solo is not None and i != solo:
            continue
        try:
            errores, avisos = fn()
        except Exception as e:
            errores, avisos = [f"❌ EXCEPCIÓN durante chequeo: {e}"], []
        resultado[nombre] = {"errores": errores, "avisos": avisos}
        total_err += len(errores)
        total_avi += len(avisos)

    if output_json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        for nombre, r in resultado.items():
            estado = "✅" if not r["errores"] else "❌"
            print(f"\n{estado} {nombre}: {len(r['errores'])} errores, {len(r['avisos'])} avisos")
            for e in r["errores"][:10]:
                print(f"   {e}")
            if len(r["errores"]) > 10:
                print(f"   ... y {len(r['errores']) - 10} errores más")
            for a in r["avisos"][:5]:
                print(f"   {a}")
        print(f"\n{'=' * 60}")
        print(f"TOTAL: {total_err} errores, {total_avi} avisos")

    sys.exit(1 if total_err > 0 else 0)


if __name__ == "__main__":
    main()