#!/usr/bin/env python3
"""
Migración v10.145 — @R como marcador de localización.

Clasifica cada fuente `pNN-actMM` (sin @R) de un bloque consolidado en:
  - input-only  → no acción
  - respuesta-only → candidato A (escribible en modo A)
  - dual           → candidato B-only (diferido a Lote 3)
  - no-match       → anomalía, reportar
Fuentes que NO se tocan: cuadro@*, fuentes con @R ya presente, items con
dual-tracking ya completo (plain + @R en la misma lista).

Defaults: --block vocab --dry-run. --apply solo permitido para vocab en
esta fase (Lote 2 v10.145); el resto de bloques solo dry-run.

Uso:
  python3 scripts/migrate_at_r_v10145.py --unit 4
  python3 scripts/migrate_at_r_v10145.py --unit 4 --block vocab --apply
  python3 scripts/migrate_at_r_v10145.py --unit 4 --block all
"""
import argparse, json, os, re, shutil, subprocess, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BLOCK_MAP = {
    "vocab":    "vocabulario_consolidado",
    "verbos":   "tiempos_y_verbos_consolidado",
    "gramatica":"gramatica_consolidada",
    "pron":     "pronunciacion_ortografia_consolidada",
}
INPUT_FIELDS = ("instruccion_original","datos","dialogo","dialogo_completo",
                "texto","texto_completo","items_libro","muestra_de_lengua",
                "opciones","audio")

def gather_text(o, out):
    if isinstance(o, dict):
        for v in o.values(): gather_text(v, out)
    elif isinstance(o, list):
        for x in o: gather_text(x, out)
    elif isinstance(o, str):
        out.append(o)

def norm(s): return re.sub(r"\s+", " ", s or "").strip().lower()

def match_substring(needle, haystack):
    """Match literal case-insensitive con normalización leve de espacios."""
    n = norm(needle)
    h = norm(haystack)
    return bool(n) and n in h

def build_activity_index(d):
    idx = {}
    for p in d.get("paginas_detalle", []):
        page = p.get("pagina")
        for a in p.get("actividades", []) or []:
            num = a.get("numero")
            if page is None or num is None: continue
            idx[f"p{page}-act{num}"] = a
    return idx

def activity_input_text(a):
    out = []
    for f in INPUT_FIELDS:
        if f in a: gather_text(a[f], out)
    return " ".join(out)

def activity_resp_text(a):
    out = []
    gather_text(a.get("respuestas", []), out)
    return " ".join(out)

def iter_items(consolidated_block, block_key):
    """Yields (tier, categoria, item_dict, palabra_for_match).
    Para 'tiempos_y_verbos_consolidado': el item es un dict con 'lema'
    (string) usado como palabra. Para los otros 3 bloques: items[].palabra.
    """
    if block_key == "tiempos_y_verbos_consolidado":
        # Shape: dict { tier: [ items ] } o lista directa según implementación
        # Por simplicidad: recorrer dict de tier → lista de objetos con 'lema'
        for tier, container in (consolidated_block or {}).items():
            if not isinstance(container, list): continue
            for item in container:
                if not isinstance(item, dict): continue
                yield tier, None, item, item.get("lema") or ""
    else:
        for tier, cats in (consolidated_block or {}).items():
            if not isinstance(cats, dict): continue
            for catname, cat in cats.items():
                if not isinstance(cat, dict): continue
                for item in cat.get("items", []) or []:
                    if not isinstance(item, dict): continue
                    yield tier, catname, item, item.get("palabra") or ""

def classify_fuente(fuente, palabra, act_idx):
    """Returns ('input-only'|'respuesta-only'|'dual'|'no-match'|'skip', tipo)."""
    m = re.match(r"^p(\d+)-act(\d+)$", fuente)
    if not m: return ("skip", None)  # cuadro@ o ya @R
    key = f"p{m.group(1)}-act{m.group(2)}"
    a = act_idx.get(key)
    if not a: return ("warn-no-act", None)
    in_input = match_substring(palabra, activity_input_text(a))
    in_resp  = match_substring(palabra, activity_resp_text(a))
    tipo = a.get("tipo")
    if in_input and in_resp: return ("dual", tipo)
    if in_input:             return ("input-only", tipo)
    if in_resp:              return ("respuesta-only", tipo)
    return ("no-match", tipo)

def dedupe_keep_order(seq):
    seen = set(); out = []
    for x in seq:
        if x not in seen:
            seen.add(x); out.append(x)
    return out

def process_block(block, block_key, act_idx, apply_changes):
    """Mutates items in-place if apply_changes. Returns lists of records.
    Para bloques con categorías (vocab/gramatica/pron), tras mutar items
    recomputa también category.fuentes como unión deduplicada preservando
    orden (schema §9: la categoría agrega fuentes de sus items)."""
    A, B, NO, WARN = [], [], [], []
    if not block: return A, B, NO, WARN
    # Categorías con cambios para recomputar agregado al final
    dirty_categories = []  # list of (cat_dict,) refs
    for tier, cat, item, palabra in iter_items(block, block_key):
        fuentes = item.get("fuentes")
        if not isinstance(fuentes, list): continue
        existing_at_r = {f[:-2] for f in fuentes if isinstance(f, str) and f.endswith("@R")}
        new_fuentes = list(fuentes)
        item_changed = False
        for f in list(fuentes):
            if not isinstance(f, str): continue
            if f.endswith("@R"): continue
            if f.startswith("cuadro@"): continue
            if f in existing_at_r: continue  # dual-tracking ya completo
            status, tipo = classify_fuente(f, palabra, act_idx)
            rec = {"tier":tier, "categoria":cat, "palabra":palabra,
                   "fuente":f, "tipo":tipo}
            if status == "respuesta-only":
                A.append(rec)
                if apply_changes:
                    idx_in_new = new_fuentes.index(f)
                    new_fuentes[idx_in_new] = f + "@R"
                    item_changed = True
            elif status == "dual":
                B.append(rec)
            elif status == "no-match":
                NO.append(rec)
            elif status == "warn-no-act":
                WARN.append(rec)
        if apply_changes and item_changed:
            item["fuentes"] = dedupe_keep_order(new_fuentes)
    # Recomputar fuentes agregadas de categoría (solo bloques anidados tier→cat→items)
    if apply_changes and block_key != "tiempos_y_verbos_consolidado":
        for tier, cats in (block or {}).items():
            if not isinstance(cats, dict): continue
            for catname, cat in cats.items():
                if not isinstance(cat, dict): continue
                items = cat.get("items", []) or []
                if not items: continue
                union = []
                for it in items:
                    for f in it.get("fuentes", []) or []:
                        union.append(f)
                cat["fuentes"] = dedupe_keep_order(union)
    return A, B, NO, WARN

def render_report(unit, block_arg, mode, totals, A, B, NO, WARN):
    out = []
    out.append(f"# Migración @R v10.145 — U{unit}, bloque {block_arg}, modo {mode}")
    out.append("")
    out.append("## Resumen")
    out.append(f"- Items inspeccionados: {totals['items']}")
    out.append(f"- Fuentes inspeccionadas (no-cuadro, no-@R, no-dual-existente): {totals['fuentes']}")
    out.append(f"- Candidatos A (respuesta-only): {len(A)}   ← aplicar ahora (vocab) / diferido (resto)")
    out.append(f"- Candidatos B-only (dual): {len(B)}        ← diferido a Lote 3")
    out.append(f"- Anomalías (no-match): {len(NO)}           ← revisar manualmente")
    out.append(f"- Warnings (actividad no resuelta): {len(WARN)}")
    out.append("")
    def table(title, rows):
        out.append(f"## {title} ({len(rows)})")
        if not rows:
            out.append("_(ninguno)_"); out.append(""); return
        out.append("| Bloque-tier | Categoría | Palabra | Fuente | tipo |")
        out.append("|---|---|---|---|---|")
        for r in rows[:200]:
            out.append(f"| {r['tier']} | {r['categoria'] or '-'} | {r['palabra']} | {r['fuente']} | {r['tipo'] or '?'} |")
        if len(rows) > 200:
            out.append(f"| … | … | … | … | (+{len(rows)-200} más) |")
        out.append("")
    table("Candidatos A — respuesta-only", A)
    table("Candidatos B-only — dual (diferido)", B)
    table("Anomalías (no-match)", NO)
    table("Warnings (actividad no encontrada)", WARN)
    return "\n".join(out)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--unit", type=int, required=True)
    ap.add_argument("--block", choices=list(BLOCK_MAP.keys())+["all"], default="vocab")
    ap.add_argument("--apply", action="store_true", help="escribe in-place (default: dry-run)")
    ap.add_argument("--dry-run", action="store_true", help="explícito (default si no se pasa --apply)")
    ap.add_argument("--report", type=str, default=None)
    args = ap.parse_args()
    if args.apply and args.dry_run:
        sys.stderr.write("ERROR: --apply y --dry-run son mutuamente excluyentes.\n"); sys.exit(2)

    blocks = list(BLOCK_MAP.keys()) if args.block == "all" else [args.block]
    experimental_blocks = {b for b in blocks if b != "vocab"}

    if args.apply and experimental_blocks:
        sys.stderr.write(
            f"ERROR: --apply solo permitido para --block vocab en Lote 2 (v10.145).\n"
            f"Bloques experimentales detectados: {sorted(experimental_blocks)}.\n"
            f"Usa --dry-run para estos bloques hasta validar U4.\n")
        sys.exit(2)

    path = REPO / f"unidades/U{args.unit}/U{args.unit}-nc1-inventario.json"
    if not path.exists():
        sys.stderr.write(f"ERROR: no existe {path}\n"); sys.exit(2)
    with path.open() as fh: d = json.load(fh)
    act_idx = build_activity_index(d)

    if args.apply:
        bak = path.with_suffix(path.suffix + ".bak.v10.145")
        shutil.copy2(path, bak)
        print(f"Backup: {bak}", file=sys.stderr)

    all_A, all_B, all_NO, all_WARN = [], [], [], []
    items_total = fuentes_total = 0
    for bkey in blocks:
        block_key_full = BLOCK_MAP[bkey]
        block = d.get(block_key_full)
        # count for resumen
        for _, _, item, _ in iter_items(block, block_key_full):
            items_total += 1
            for f in item.get("fuentes", []) or []:
                if isinstance(f, str) and not f.startswith("cuadro@") and not f.endswith("@R"):
                    fuentes_total += 1
        A, B, NO, WARN = process_block(block, block_key_full, act_idx,
                                       apply_changes=(args.apply and bkey == "vocab"))
        for rec in A+B+NO+WARN: rec["bloque"] = block_key_full
        all_A += A; all_B += B; all_NO += NO; all_WARN += WARN

    mode = "APPLY" if args.apply else "DRY-RUN"
    totals = {"items": items_total, "fuentes": fuentes_total}
    report = render_report(args.unit, args.block, mode, totals, all_A, all_B, all_NO, all_WARN)
    if args.report:
        Path(args.report).write_text(report)
        print(f"Informe escrito en {args.report}", file=sys.stderr)
    else:
        print(report)

    if args.apply:
        with path.open("w") as fh: json.dump(d, fh, ensure_ascii=False, indent=2)
        # Reformatear con el serializador canónico (palabras/fuentes inline)
        rf = subprocess.run(["python3", "scripts/format_inventario.py", str(path)],
                            cwd=str(REPO), capture_output=True, text=True)
        if rf.returncode != 0:
            sys.stderr.write(rf.stdout + rf.stderr)
            sys.stderr.write(f"\n❌ Reformat falló. .bak preservado en {bak}\n"
                             f"   Rollback: mv '{bak}' '{path}'\n")
            sys.exit(3)
        # validador
        r = subprocess.run(["python3", "scripts/validar_inventario.py", str(args.unit)],
                           cwd=str(REPO), capture_output=True, text=True)
        sys.stderr.write(r.stdout + r.stderr)
        if r.returncode != 0:
            sys.stderr.write(f"\n❌ Validador falló. .bak preservado en {bak}\n"
                             f"   Rollback: mv '{bak}' '{path}'\n")
            sys.exit(3)
        sys.stderr.write(f"\n✅ Aplicado. {len(all_A)} reemplazos. Validador 0/0/0.\n")

if __name__ == "__main__":
    main()
