#!/usr/bin/env python3
"""
Saneador de inventario — aplicación de §5.10 + §5.11 a un inventario.

(Antes `cleanup_v150.py`; renombrado en v11.20 — el nombre `v150` sugería
un one-shot pero es la herramienta de saneamiento activa del flujo de fase 1.)

Aplica las 3 FASES del saneamiento §5.10/§5.11:
  FASE 1: §5.10 — retirar fuentes A sin aparición literal en contenido
          didáctico (§5.2) + respuestas[] + cuerpo de cuadros.
  FASE 2: §5.11 — unificar flexiones cuando hay ≥2 formas atestadas
          (adj/gent: masc sg; sustantivos: sg conservando género).
  FASE 3: saneamiento — recomputar cat.fuentes, reformatear, validar.

Pron queda fuera del alcance material de §5.10 A (toda Cat B).

CLI:
  python3 scripts/sanear_inventario.py --unit N [--apply]
  python3 scripts/sanear_inventario.py --unit N --report ruta.md

Sin --apply → dry-run (default). Con --apply → escribe + valida.
"""
import argparse, json, os, re, shutil, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Importar el módulo matcher
sys.path.insert(0, str(REPO / "scripts"))
from matcher import (
    expand_needle, match_substring, norm,
    gather_text, build_activity_index,
    activity_input_text, activity_resp_text,
    dedupe_keep_order, INPUT_FIELDS
)

# ---------- Clasificación de items de gramática (Cat A vs B) ----------

def is_gramatica_categoria_A(palabra, catname=None):
    """Heurística (alineada con §5.10 + criterio discriminante).
    A — realización superficial: corta, sin signos editoriales, no es
        plantilla con elipsis ni alternancia con barra ni paradigma.
    B — etiqueta / paradigma editorial / notación / label reproducido.

    Reglas conservadoras: en duda → B (no tocar). El precio de un FN
    (marcar B algo que era A) es no limpiar; el de un FP (marcar A algo
    que era B) es retirar contenido legítimo del consolidado.
    """
    if not palabra: return False
    p = palabra.strip()
    # Signos editoriales que delatan paradigma/plantilla/notación
    if any(c in p for c in "()→+?…"): return False
    if "..." in p or ".." in p: return False  # "¿Qué...?", elipsis
    if "/" in p: return False  # alternancia editorial: "un / unos", "abuelo/abuela"
    if any(c in p for c in "ˈˌʝθχ↑↓"): return False  # IPA
    if ":" in p: return False  # "intensificadores: mucho..."
    # Item idéntico al nombre de la categoría → label reproducido como item (B)
    if catname and p.strip().lower() == catname.strip().lower(): return False
    # Multi-token largo → probablemente descripción editorial
    if len(p.split()) > 3: return False
    if len(p) > 25: return False
    return True

# ---------- Cuerpo del cuadro (también cuenta como input según §5.10) ----------

def cuadro_body_text(cuadro):
    out = []
    for k, v in cuadro.items():
        if k in ("vocabulario", "tiempos_y_verbos", "gramatica",
                 "pronunciacion_ortografia", "tipo_cuadro", "pagina", "id"):
            continue
        gather_text(v, out)
    return " ".join(out)

# ---------- FASE 1: §5.10 ----------

def fase1_aparicion_material(d, apply_changes, act_idx, cuadros_idx):
    """Retira fuentes A que no verifican aparición literal.
    Devuelve listas de records: retiradas_fuentes, retirados_items, retirados_labels.
    """
    retiradas_fuentes = []   # (bloque, tier, cat, palabra, fuente)
    retirados_items = []     # (bloque, tier, cat, palabra)
    retirados_labels = []    # (lista_tipada_path, label)

    # --- 1A: VOCAB items (todos Cat A) ---
    vc = d.get("vocabulario_consolidado", {})
    for tier in ("principal", "recurrente"):
        cats = vc.get(tier, {})
        if not isinstance(cats, dict): continue
        for catname, cat in list(cats.items()):
            if not isinstance(cat, dict): continue
            items = cat.get("items", []) or []
            new_items = []
            for item in items:
                palabra = item.get("palabra") or ""
                fuentes_orig = item.get("fuentes", []) or []
                new_fuentes = []
                for f in fuentes_orig:
                    if not isinstance(f, str):
                        new_fuentes.append(f); continue
                    if f.startswith("cuadro@"):
                        # cuadro: verificar contra cuerpo del cuadro
                        cuadro_obj = cuadros_idx.get(f)
                        if cuadro_obj and match_substring(palabra, cuadro_body_text(cuadro_obj)):
                            new_fuentes.append(f)
                        elif cuadro_obj:
                            retiradas_fuentes.append(("vocab", tier, catname, palabra, f))
                        else:
                            new_fuentes.append(f)  # cuadro no encontrado, conservar
                        continue
                    # actividad
                    m = re.match(r"^(p\d+-act\d+)(@R)?$", f)
                    if not m:
                        new_fuentes.append(f); continue
                    key, suf = m.group(1), m.group(2) or ""
                    a = act_idx.get(key)
                    if not a:
                        new_fuentes.append(f); continue
                    # @R verifica contra respuestas; plain verifica contra input+respuestas
                    if suf == "@R":
                        ok = match_substring(palabra, activity_resp_text(a))
                    else:
                        ok = (match_substring(palabra, activity_input_text(a)) or
                              match_substring(palabra, activity_resp_text(a)))
                    if ok:
                        new_fuentes.append(f)
                    else:
                        retiradas_fuentes.append(("vocab", tier, catname, palabra, f))
                if new_fuentes:
                    if apply_changes:
                        item["fuentes"] = dedupe_keep_order(new_fuentes)
                    new_items.append(item)
                else:
                    retirados_items.append(("vocab", tier, catname, palabra))
            if apply_changes:
                cat["items"] = new_items

    # --- 1B: TIEMPOS_Y_VERBOS (formas_trabajadas en listas tipadas + consolidado) ---
    # Para verbos, la evidencia literal vive en formas_trabajadas (Cat A directo)
    tv = d.get("tiempos_y_verbos_consolidado", [])
    if isinstance(tv, list):
        new_tv = []
        for vobj in tv:
            if not isinstance(vobj, dict):
                new_tv.append(vobj); continue
            lema = vobj.get("lema") or ""
            formas = vobj.get("formas_trabajadas", []) or []
            fuentes_orig = vobj.get("fuentes", []) or []
            new_fuentes = []
            for f in fuentes_orig:
                if not isinstance(f, str):
                    new_fuentes.append(f); continue
                if f.startswith("cuadro@"):
                    cuadro_obj = cuadros_idx.get(f)
                    if cuadro_obj:
                        body = cuadro_body_text(cuadro_obj)
                        if any(match_substring(forma, body) for forma in formas):
                            new_fuentes.append(f)
                        else:
                            retiradas_fuentes.append(("verbos", None, lema, lema, f))
                    else:
                        new_fuentes.append(f)
                    continue
                m = re.match(r"^(p\d+-act\d+)(@R)?$", f)
                if not m:
                    new_fuentes.append(f); continue
                key, suf = m.group(1), m.group(2) or ""
                a = act_idx.get(key)
                if not a:
                    new_fuentes.append(f); continue
                if suf == "@R":
                    txt = activity_resp_text(a)
                else:
                    txt = activity_input_text(a) + " " + activity_resp_text(a)
                if any(match_substring(forma, txt) for forma in formas):
                    new_fuentes.append(f)
                else:
                    retiradas_fuentes.append(("verbos", None, lema, lema, f))
            if new_fuentes:
                if apply_changes:
                    vobj["fuentes"] = dedupe_keep_order(new_fuentes)
                new_tv.append(vobj)
            else:
                retirados_items.append(("verbos", None, lema, lema))
        if apply_changes:
            d["tiempos_y_verbos_consolidado"] = new_tv

        # También: retirar formas concretas no atestadas de las listas tipadas
        # actividad.tiempos_y_verbos[].formas_trabajadas (y cuadro)
        # Si formas_trabajadas queda vacía → retirar el objeto verbal entero.
        for p in d.get("paginas_detalle", []):
            for a in p.get("actividades", []) or []:
                tvlist = a.get("tiempos_y_verbos", []) or []
                key = f"p{p.get('pagina')}-act{a.get('numero')}"
                inp_resp = activity_input_text(a) + " " + activity_resp_text(a)
                new_tvlist = []
                for vobj in tvlist:
                    if not isinstance(vobj, dict):
                        new_tvlist.append(vobj); continue
                    formas = vobj.get("formas_trabajadas", []) or []
                    kept = [f for f in formas if match_substring(f, inp_resp)]
                    if len(kept) != len(formas):
                        retirados = [f for f in formas if f not in kept]
                        for rf in retirados:
                            retiradas_fuentes.append(("verbos-listatipada", None,
                                                      vobj.get("lema"), rf, key))
                    if kept:
                        if apply_changes:
                            vobj["formas_trabajadas"] = kept
                        new_tvlist.append(vobj)
                    else:
                        # objeto verbal sin formas → retirar
                        retirados_items.append(("verbos-listatipada", None,
                                                vobj.get("lema"), key))
                if apply_changes:
                    a["tiempos_y_verbos"] = new_tvlist
            # Mismo tratamiento en cuadros
            for c in p.get("cuadros", []) or []:
                tvlist = c.get("tiempos_y_verbos", []) or []
                if not tvlist: continue
                body = cuadro_body_text(c)
                new_tvlist = []
                for vobj in tvlist:
                    if not isinstance(vobj, dict):
                        new_tvlist.append(vobj); continue
                    formas = vobj.get("formas_trabajadas", []) or []
                    kept = [f for f in formas if match_substring(f, body)]
                    if kept:
                        if apply_changes:
                            vobj["formas_trabajadas"] = kept
                        new_tvlist.append(vobj)
                if apply_changes:
                    c["tiempos_y_verbos"] = new_tvlist

    # --- 1C: GRAMATICA items (separar Cat A vs B con heurística) ---
    gc = d.get("gramatica_consolidada", {})
    for tier in ("principal", "recurrente"):
        cats = gc.get(tier, {})
        if not isinstance(cats, dict): continue
        for catname, cat in list(cats.items()):
            if not isinstance(cat, dict): continue
            items = cat.get("items", []) or []
            new_items = []
            for item in items:
                palabra = item.get("palabra") or ""
                if not is_gramatica_categoria_A(palabra, catname):
                    new_items.append(item)  # Cat B: no se toca
                    continue
                fuentes_orig = item.get("fuentes", []) or []
                new_fuentes = []
                for f in fuentes_orig:
                    if not isinstance(f, str):
                        new_fuentes.append(f); continue
                    if f.startswith("cuadro@"):
                        cuadro_obj = cuadros_idx.get(f)
                        if cuadro_obj and match_substring(palabra, cuadro_body_text(cuadro_obj)):
                            new_fuentes.append(f)
                        elif cuadro_obj:
                            retiradas_fuentes.append(("gramatica", tier, catname, palabra, f))
                        else:
                            new_fuentes.append(f)
                        continue
                    m = re.match(r"^(p\d+-act\d+)(@R)?$", f)
                    if not m:
                        new_fuentes.append(f); continue
                    key, suf = m.group(1), m.group(2) or ""
                    a = act_idx.get(key)
                    if not a:
                        new_fuentes.append(f); continue
                    if suf == "@R":
                        ok = match_substring(palabra, activity_resp_text(a))
                    else:
                        ok = (match_substring(palabra, activity_input_text(a)) or
                              match_substring(palabra, activity_resp_text(a)))
                    if ok:
                        new_fuentes.append(f)
                    else:
                        retiradas_fuentes.append(("gramatica", tier, catname, palabra, f))
                if new_fuentes:
                    if apply_changes:
                        item["fuentes"] = dedupe_keep_order(new_fuentes)
                    new_items.append(item)
                else:
                    retirados_items.append(("gramatica", tier, catname, palabra))
            if apply_changes:
                cat["items"] = new_items

    return retiradas_fuentes, retirados_items, retirados_labels

# ---------- FASE 2: §5.11 unificación de flexiones ----------

def detectar_flexion(palabra1, palabra2):
    """¿Son palabra1 y palabra2 flexiones del mismo lema?
    Devuelve la forma canónica si lo son, None si no.
    Adj/gent: masc sg. Sustantivos: sg conservando género (no se determina
    automáticamente; se preserva la forma sin -s/-es)."""
    if not palabra1 or not palabra2: return None
    a, b = norm(palabra1), norm(palabra2)
    if a == b: return None
    if " " in a or " " in b: return None  # compuestos no aplican
    # Adj/gent en -o/-a (mismo lema con género)
    if a.endswith("o") and b.endswith("a") and a[:-1] == b[:-1]:
        return palabra1 if palabra1[-1].lower()=="o" else palabra2  # devolver masc
    if a.endswith("a") and b.endswith("o") and a[:-1] == b[:-1]:
        return palabra1 if palabra1[-1].lower()=="o" else palabra2
    # Sing/plural -s
    if a + "s" == b: return palabra1
    if b + "s" == a: return palabra2
    # Sing/plural -es (consonante)
    if a + "es" == b: return palabra1
    if b + "es" == a: return palabra2
    # -és/-esa (gent: francés/francesa)
    if a.endswith("és") and b.endswith("esa") and a[:-2] == b[:-3]:
        return palabra1 if a.endswith("és") else palabra2
    if a.endswith("esa") and b.endswith("és") and a[:-3] == b[:-2]:
        return palabra2 if b.endswith("és") else palabra1
    # -án/-ana (gent: alemán/alemana)
    if a.endswith("án") and b.endswith("ana") and a[:-2] == b[:-3]:
        return palabra1 if a.endswith("án") else palabra2
    # masc consonante + femenino con -a (español/española)
    if b == a + "a": return palabra1
    if a == b + "a": return palabra2
    return None

def reescribir_notacion_barra(item, act_idx, cuadros_idx):
    """Si item.palabra tiene notación 'lema/-suf' (registry verbatim),
    reescribir según atestación:
    - Si masc está atestado en alguna fuente → palabra = masc.
    - Si solo otra flexiva atestada → palabra = esa flexiva.
    - Si ninguna atestada → no se toca aquí (FASE 1 ya lo habrá retirado).
    Devuelve nueva palabra o None si no aplica.
    """
    palabra = item.get("palabra") or ""
    m = re.match(r"^(.+?)/-([a-záéíóúñü]+)$", palabra, re.IGNORECASE)
    if not m: return None
    left, suf = m.group(1).strip(), m.group(2).strip()
    # Variantes derivadas por expand_needle
    variants = expand_needle(palabra)
    # Buscar cuál variante está atestada en las fuentes del item
    atestadas = set()
    for f in item.get("fuentes", []) or []:
        if not isinstance(f, str): continue
        if f.startswith("cuadro@"):
            c = cuadros_idx.get(f)
            txt = cuadro_body_text(c) if c else ""
        else:
            mm = re.match(r"^(p\d+-act\d+)(@R)?$", f)
            if not mm: continue
            a = act_idx.get(mm.group(1))
            if not a: continue
            txt = activity_input_text(a) + " " + activity_resp_text(a)
        for v in variants:
            if v == palabra: continue  # forma con barra no se busca literal
            if match_substring(v, txt):
                atestadas.add(v)
    if not atestadas: return None
    # Prioridad: masc (=left tal cual)
    if left in atestadas:
        return left
    # Si solo una atestada, devolverla
    if len(atestadas) == 1:
        return list(atestadas)[0]
    # Varias atestadas pero no masc — devolver masc canónico igualmente
    return left


def fase2_unificar_flexiones(d, apply_changes, act_idx=None, cuadros_idx=None,
                              paso_a_only=False, paso_b_only=False):
    pares = []  # (categoria, palabras_unidas, lema_canonico)
    reescrituras = []  # (categoria, palabra_orig, palabra_nueva)
    vc = d.get("vocabulario_consolidado", {})
    # PASO A: reescribir notación verbatim 'lema/-suf' según atestación
    if not paso_b_only and act_idx is not None and cuadros_idx is not None:
        for tier in ("principal", "recurrente"):
            cats = vc.get(tier, {})
            if not isinstance(cats, dict): continue
            for catname, cat in cats.items():
                for item in cat.get("items", []) or []:
                    nueva = reescribir_notacion_barra(item, act_idx, cuadros_idx)
                    if nueva and nueva != item.get("palabra"):
                        reescrituras.append((catname, item.get("palabra"), nueva))
                        if apply_changes:
                            item["palabra"] = nueva
    if paso_a_only:
        return pares, reescrituras
    # PASO B: detectar y fusionar pares de flexiones
    for tier in ("principal", "recurrente"):
        cats = vc.get(tier, {})
        if not isinstance(cats, dict): continue
        for catname, cat in cats.items():
            items = cat.get("items", []) or []
            # Encontrar grupos de flexión
            grupos = {}  # idx_lema → [idxs]
            assignment = {}  # idx → idx_lema
            for i, it in enumerate(items):
                p_i = it.get("palabra") or ""
                if " " in p_i: continue  # compuesto, no aplica
                if i in assignment: continue
                grupo = [i]
                lema_idx = i
                for j, jt in enumerate(items[i+1:], start=i+1):
                    if j in assignment: continue
                    p_j = jt.get("palabra") or ""
                    canon = detectar_flexion(p_i, p_j)
                    if canon:
                        grupo.append(j)
                        # Quien es masc → lema_idx
                        if canon == p_j:
                            lema_idx = j
                if len(grupo) >= 2:
                    grupos[lema_idx] = grupo
                    for k in grupo: assignment[k] = lema_idx
            # Aplicar fusión
            if grupos:
                if apply_changes:
                    new_items = []
                    for i, it in enumerate(items):
                        if i in assignment:
                            if i == assignment[i]:
                                # Este es el lema canónico — fusionar fuentes de su grupo
                                all_fuentes = []
                                for k in grupos[i]:
                                    all_fuentes.extend(items[k].get("fuentes", []) or [])
                                it["fuentes"] = dedupe_keep_order(all_fuentes)
                                new_items.append(it)
                            # else: era una flexión absorbida, no se mantiene
                        else:
                            new_items.append(it)
                    cat["items"] = new_items
                for lema_idx, grupo in grupos.items():
                    palabras = [items[k].get("palabra") for k in grupo]
                    canon = items[lema_idx].get("palabra")
                    pares.append((catname, palabras, canon))
    return pares, reescrituras

# ---------- FASE 3: saneamiento ----------

def fase3_saneamiento(d):
    """Recomputa cat.fuentes agregadas como unión deduplicada de items[].fuentes."""
    for block_key in ("vocabulario_consolidado", "gramatica_consolidada",
                       "pronunciacion_ortografia_consolidada"):
        block = d.get(block_key, {})
        for tier, cats in block.items():
            if not isinstance(cats, dict): continue
            for catname, cat in cats.items():
                if not isinstance(cat, dict): continue
                items = cat.get("items", []) or []
                union = []
                for it in items:
                    for f in it.get("fuentes", []) or []:
                        union.append(f)
                cat["fuentes"] = dedupe_keep_order(union)

# ---------- FASE 4: retirar categorías vacías + labels en listas tipadas ----------

# Map bloque consolidado → campo en listas tipadas
BLOQUE_A_LISTA = {
    "vocabulario_consolidado": "vocabulario",
    "gramatica_consolidada": "gramatica",
    "pronunciacion_ortografia_consolidada": "pronunciacion_ortografia",
}

def fase4_retirar_vacias(d, apply_changes):
    """Retira categorías sin items[] del consolidado y limpia su label de
    las listas tipadas (actividad.X / cuadro.X) en todo el JSON.
    Devuelve lista de (bloque, tier, categoria) retiradas."""
    retiradas = []
    for block_key, lista_field in BLOQUE_A_LISTA.items():
        block = d.get(block_key, {})
        if not isinstance(block, dict): continue
        for tier in list(block.keys()):
            cats = block.get(tier)
            if not isinstance(cats, dict): continue
            for catname in list(cats.keys()):
                cat = cats[catname]
                if not isinstance(cat, dict): continue
                if not cat.get("items"):  # vacío
                    retiradas.append((block_key, tier, catname))
                    if apply_changes:
                        del cats[catname]
    # Limpiar labels en listas tipadas
    if apply_changes and retiradas:
        cats_retiradas_por_bloque = {}
        for bk, _, cn in retiradas:
            cats_retiradas_por_bloque.setdefault(BLOQUE_A_LISTA[bk], set()).add(cn)
        for p in d.get("paginas_detalle", []):
            for a in p.get("actividades", []) or []:
                for lista_field, retirar in cats_retiradas_por_bloque.items():
                    if lista_field in a and isinstance(a[lista_field], list):
                        a[lista_field] = [x for x in a[lista_field] if x not in retirar]
            for c in p.get("cuadros", []) or []:
                for lista_field, retirar in cats_retiradas_por_bloque.items():
                    if lista_field in c and isinstance(c[lista_field], list):
                        c[lista_field] = [x for x in c[lista_field] if x not in retirar]
    return retiradas

# ---------- Indexar cuadros ----------

def build_cuadros_index(d):
    """Devuelve dict {key: cuadro_obj} con key tipo 'cuadro@pNN' o 'cuadro@pNN#K'."""
    idx = {}
    for p in d.get("paginas_detalle", []):
        page = p.get("pagina")
        cuadros = p.get("cuadros", []) or []
        for i, c in enumerate(cuadros, start=1):
            key_simple = f"cuadro@p{page}"
            key_num = f"cuadro@p{page}#{i}"
            idx[key_simple] = c
            idx[key_num] = c
    return idx

# ---------- Render informe ----------

def render_report(unit, mode, retiradas_fuentes, retirados_items, pares, reescrituras, cats_retiradas=None):
    cats_retiradas = cats_retiradas or []
    out = [f"# Cleanup v10.150 — U{unit}, modo {mode}", ""]
    out.append("## Resumen FASE 1 (§5.10 retirar inferencias)")
    out.append(f"- Fuentes A retiradas: {len(retiradas_fuentes)}")
    out.append(f"- Items A retirados (todas sus fuentes inferencia): {len(retirados_items)}")
    out.append("")
    out.append("## Resumen FASE 2 (§5.11 unificar flexiones)")
    out.append(f"- Notaciones `lema/-suf` reescritas según atestación: {len(reescrituras)}")
    out.append(f"- Pares unificados: {len(pares)}")
    out.append("")
    out.append("## Resumen FASE 4 (retirar categorías vacías + labels en listas tipadas)")
    out.append(f"- Categorías retiradas: {len(cats_retiradas)}")
    out.append("")

    def tabla(titulo, rows, cols):
        out.append(f"### {titulo} ({len(rows)})")
        if not rows: out.append("_(ninguno)_"); out.append(""); return
        out.append("| " + " | ".join(cols) + " |")
        out.append("|" + "|".join(["---"]*len(cols)) + "|")
        for r in rows[:80]:
            out.append("| " + " | ".join(str(x) for x in r) + " |")
        if len(rows) > 80:
            out.append(f"| … (+{len(rows)-80} más) |")
        out.append("")

    tabla("Fuentes A retiradas",
          [(b, t or "-", c or "-", p, f) for (b,t,c,p,f) in retiradas_fuentes],
          ["bloque", "tier", "categoría", "palabra", "fuente"])
    tabla("Items A retirados",
          [(b, t or "-", c or "-", p) for (b,t,c,p) in retirados_items],
          ["bloque", "tier", "categoría", "palabra"])
    tabla("Notaciones `lema/-suf` reescritas",
          [(c, orig, nuevo) for (c,orig,nuevo) in reescrituras],
          ["categoría", "palabra_original", "palabra_nueva"])
    tabla("Pares unificados §5.11",
          [(c, " + ".join(p), canon) for (c,p,canon) in pares],
          ["categoría", "palabras_unidas", "lema_canónico"])
    tabla("Categorías retiradas (vacías tras FASE 1)",
          [(b, t, c) for (b,t,c) in cats_retiradas],
          ["bloque", "tier", "categoría"])
    return "\n".join(out)

# ---------- Main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--unit", type=int, required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", type=str, default=None)
    args = ap.parse_args()
    if args.apply and args.dry_run:
        sys.stderr.write("ERROR: --apply y --dry-run mutuamente excluyentes.\n"); sys.exit(2)

    path = REPO / f"unidades/U{args.unit}/U{args.unit}-nc1-inventario.json"
    if not path.exists():
        sys.stderr.write(f"ERROR: no existe {path}\n"); sys.exit(2)
    d = json.loads(path.read_text())

    if args.apply:
        bak = path.with_suffix(path.suffix + ".bak.v10.150")
        shutil.copy2(path, bak)
        sys.stderr.write(f"Backup: {bak}\n")

    act_idx = build_activity_index(d)
    cuadros_idx = build_cuadros_index(d)

    # Mutamos siempre el dict en memoria; escribir al disco solo si --apply.
    # Esto permite que dry-run muestre categorías vaciadas por FASE 1.
    # Orden importante:
    # 1) FASE 2 PASO A: reescribir notación lema/-suf según atestación
    #    (antes de FASE 1, para que la verificación de aparición vea la
    #    palabra ya canonizada).
    # 2) FASE 1: aparición material.
    # 3) FASE 2 PASO B: detectar y fusionar pares atestados.
    # 4) FASE 4: retirar categorías vacías.
    pares_pre, reescrituras = fase2_unificar_flexiones(d, True, act_idx, cuadros_idx,
                                                       paso_a_only=True)
    retiradas_fuentes, retirados_items, _ = fase1_aparicion_material(
        d, True, act_idx, cuadros_idx)
    pares, _ = fase2_unificar_flexiones(d, True, act_idx, cuadros_idx,
                                         paso_b_only=True)

    cats_retiradas = fase4_retirar_vacias(d, True)

    if args.apply:
        fase3_saneamiento(d)
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        # Reformatear canónico
        rf = subprocess.run(["python3", "scripts/format_inventario.py", str(path)],
                            cwd=str(REPO), capture_output=True, text=True)
        if rf.returncode != 0:
            sys.stderr.write(rf.stdout + rf.stderr)
            sys.stderr.write(f"\n❌ Reformat falló. Backup en {bak}\n"); sys.exit(3)

    mode = "APPLY" if args.apply else "DRY-RUN"
    report = render_report(args.unit, mode, retiradas_fuentes, retirados_items, pares, reescrituras, cats_retiradas)
    if args.report:
        Path(args.report).write_text(report)
        sys.stderr.write(f"Informe en {args.report}\n")
    else:
        print(report)

    if args.apply:
        r = subprocess.run(["python3", "scripts/validar_inventario.py", str(args.unit)],
                           cwd=str(REPO), capture_output=True, text=True)
        sys.stderr.write(r.stdout + r.stderr)
        if r.returncode != 0:
            sys.stderr.write(f"\n❌ Validador falló. Rollback: mv '{bak}' '{path}'\n")
            sys.exit(3)
        sys.stderr.write(f"\n✅ Aplicado U{args.unit}: "
                         f"{len(retiradas_fuentes)} fuentes retiradas, "
                         f"{len(retirados_items)} items retirados, "
                         f"{len(pares)} pares unificados. Validador 0/0/0.\n")

if __name__ == "__main__":
    main()
