#!/usr/bin/env python3
"""
Serializador canónico de inventarios `unidades/UX/UX-nc1-inventario.json`.

Reescribe un inventario JSON preservando el estilo editorial del proyecto:

- Indent 2 espacios.
- Items de `vocabulario_consolidado.*.items[]`, `gramatica_consolidada.*.items[]`
  y `pronunciacion_ortografia_consolidada.*.items[]` con shape {palabra, fuentes}
  inline en una sola línea, **uno por línea** (clave de legibilidad).
- Items de `tiempos_y_verbos[]` y `tiempos_y_verbos_consolidado[]` (con
  `lema/tiempo/formas_trabajadas` y opcional `estructura_perifrastica`) inline.
- Arrays cortos de strings (≤ 220 chars) inline.
- Objetos pequeños tipo `audio: {presente, pista, transcripcion}`,
  `imagen: {presente, descripcion}`, `video: {presente}` inline si caben.
- Resto: indent estándar `json.dumps(indent=2)`.

Reemplaza el enfoque "post-regex" que fallaba al colapsar items consecutivos
sin preservar el newline entre ellos.

Uso programático:
    from scripts.format_inventario import format_inventory_json
    text = format_inventory_json(data_dict)

Uso CLI:
    python3 scripts/format_inventario.py unidades/U1/U1-nc1-inventario.json
"""
from __future__ import annotations
import json
import sys
from collections import OrderedDict
from pathlib import Path

INLINE_OBJECT_MAX = 240
INLINE_ARRAY_MAX = 220


def _is_palabra_fuentes(obj) -> bool:
    return (
        isinstance(obj, dict)
        and set(obj.keys()) <= {"palabra", "fuentes"}
        and "palabra" in obj
    )


def _is_tiempo_verbo(obj) -> bool:
    return (
        isinstance(obj, dict)
        and "lema" in obj
        and "tiempo" in obj
        and "formas_trabajadas" in obj
        and set(obj.keys()) <= {"lema", "tiempo", "formas_trabajadas", "estructura_perifrastica", "tipo_de_verbo"}
    )


def _all_primitives(d: dict) -> bool:
    return all(not isinstance(v, (dict, list)) for v in d.values())


def _all_strings(lst: list) -> bool:
    return all(isinstance(x, str) for x in lst)


def _serialize(value, indent_level: int = 0) -> str:
    """Recursive serializer that respects the project style."""
    ind = "  " * indent_level
    inner_ind = "  " * (indent_level + 1)

    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return json.dumps(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)

    if isinstance(value, list):
        if not value:
            return "[]"
        # Inline arrays of strings if short
        if _all_strings(value):
            compact = "[" + ", ".join(json.dumps(s, ensure_ascii=False) for s in value) + "]"
            if len(compact) <= INLINE_ARRAY_MAX:
                return compact
            # Multi-line strings array
            parts = [json.dumps(s, ensure_ascii=False) for s in value]
            return "[\n" + ",\n".join(f"{inner_ind}{p}" for p in parts) + f"\n{ind}]"
        # Items of palabra/fuentes: inline each, one per line
        if all(_is_palabra_fuentes(x) for x in value):
            parts = [json.dumps(x, ensure_ascii=False) for x in value]
            return "[\n" + ",\n".join(f"{inner_ind}{p}" for p in parts) + f"\n{ind}]"
        # Items of tiempos_y_verbos: inline each, one per line if all short
        if all(_is_tiempo_verbo(x) for x in value):
            parts = [json.dumps(x, ensure_ascii=False) for x in value]
            if all(len(p) <= 300 for p in parts):
                return "[\n" + ",\n".join(f"{inner_ind}{p}" for p in parts) + f"\n{ind}]"
        # Generic multi-line array
        parts = [_serialize(x, indent_level + 1) for x in value]
        return "[\n" + ",\n".join(f"{inner_ind}{p}" for p in parts) + f"\n{ind}]"

    if isinstance(value, dict):
        if not value:
            return "{}"
        # Inline small object with only primitive values
        if _all_primitives(value):
            compact = "{ " + ", ".join(
                f'{json.dumps(k, ensure_ascii=False)}: {_serialize(v, 0)}'
                for k, v in value.items()
            ) + " }"
            if len(compact) <= INLINE_OBJECT_MAX:
                return compact
        # Generic multi-line object
        parts = []
        for k, v in value.items():
            key_s = json.dumps(k, ensure_ascii=False)
            val_s = _serialize(v, indent_level + 1)
            parts.append(f"{inner_ind}{key_s}: {val_s}")
        return "{\n" + ",\n".join(parts) + f"\n{ind}}}"

    raise TypeError(f"Cannot serialize {type(value).__name__}: {value!r}")


def format_inventory_json(data) -> str:
    """Returns the canonical-format JSON text for an inventory dict."""
    return _serialize(data, indent_level=0) + "\n"


def main():
    if len(sys.argv) < 2:
        print("Usage: format_inventario.py <inventory.json> [<inventory.json> ...]", file=sys.stderr)
        sys.exit(2)
    for path_arg in sys.argv[1:]:
        p = Path(path_arg)
        data = json.loads(p.read_text(), object_pairs_hook=OrderedDict)
        # Sanity round-trip
        text = format_inventory_json(data)
        parsed_back = json.loads(text)
        # Compare structurally (json.loads collapses OrderedDict to dict; ordering should still match)
        original = json.loads(p.read_text())
        if parsed_back != original:
            print(f"ERROR: round-trip failed for {p}", file=sys.stderr)
            sys.exit(1)
        p.write_text(text)
        print(f"Reformatted: {p} ({len(text)} bytes)")


if __name__ == "__main__":
    main()
