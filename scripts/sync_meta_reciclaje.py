#!/usr/bin/env python3
"""
Sincroniza `_meta.version` y `_meta.fecha` de `unidades/nc1-reciclaje.json` con
el estado actual del proyecto:

  - `_meta.version` ← versión máxima `vX.Y` encontrada en `CHANGELOG.md`.
  - `_meta.fecha`   ← fecha del día.

Útil cuando se escribe directamente al canónico (sesiones de Capa 2,
ediciones manuales) sin pasar por el generador de Capa 1, que solo bumpea
`_meta` cuando regenera. Se ejecuta automáticamente desde el pre-commit hook
(`scripts/hooks/pre-commit`) si el JSON está staged. También se puede ejecutar
a mano: `python3 scripts/sync_meta_reciclaje.py`.

Idempotente: si ya está sincronizado no hace nada (y sale con código 0).
"""
import json
import re
import sys
from datetime import date
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
CHANGELOG = PROJECT / "CHANGELOG.md"
RECICLAJE = PROJECT / "unidades" / "nc1-reciclaje.json"


def version_actual_de_changelog() -> str:
    try:
        txt = CHANGELOG.read_text(encoding="utf-8")
    except OSError:
        return "v0.0"
    versiones = re.findall(r"v(\d+)\.(\d+)", txt)
    if not versiones:
        return "v0.0"
    mayor = max((int(a), int(b)) for a, b in versiones)
    return f"v{mayor[0]}.{mayor[1]}"


def main() -> int:
    if not RECICLAJE.exists():
        print(f"(no hay {RECICLAJE.relative_to(PROJECT)} — nada que sincronizar)")
        return 0
    raw = RECICLAJE.read_text(encoding="utf-8")
    d = json.loads(raw)
    meta = d.setdefault("_meta", {})
    version_destino = version_actual_de_changelog()
    fecha_destino = date.today().isoformat()
    if meta.get("version") == version_destino and meta.get("fecha") == fecha_destino:
        return 0  # ya sincronizado, idempotente
    cambios = []
    if meta.get("version") != version_destino:
        cambios.append(f"version: {meta.get('version')} → {version_destino}")
        meta["version"] = version_destino
    if meta.get("fecha") != fecha_destino:
        cambios.append(f"fecha: {meta.get('fecha')} → {fecha_destino}")
        meta["fecha"] = fecha_destino
    with open(RECICLAJE, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"✓ _meta sincronizado: {' · '.join(cambios)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())