#!/usr/bin/env python3
"""
Integra el inventario de una unidad desde su worktree a main.

Pasos reales (en este orden):
1. Localiza el inventario en el worktree extract/UN.
2. Copia el inventario a unidades/UN/ guardando en memoria la versión previa si existe.
3. Valida. Si falla, restaura la versión previa (o borra si no había) y aborta.
4. Actualiza nc1-reciclaje.json. Si falla, restaura la versión previa y aborta.
5. Hace commit aislado: solo los dos archivos esperados, ignorando el índice.

Uso:
    python3 scripts/integrar_unidad.py <N>
    python3 scripts/integrar_unidad.py 6

El worktree se busca en:
    ~/Desktop/guia-didactica-extract-U<N>/unidades/U<N>/

Si está en otra ruta, pásala como segundo argumento:
    python3 scripts/integrar_unidad.py 6 /ruta/al/worktree/unidades
"""
import json
import subprocess
import sys
import shutil
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
DESKTOP = Path.home() / "Desktop"


def run(cmd: list, cwd=None) -> tuple[int, str]:
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd or PROJECT)
    return r.returncode, (r.stdout + r.stderr).strip()


def restaurar(dst: Path, dst_prev: bytes | None):
    if dst_prev is not None:
        dst.write_bytes(dst_prev)
    else:
        dst.unlink(missing_ok=True)


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 scripts/integrar_unidad.py <N> [ruta_worktree_unidades]")
        sys.exit(1)

    n = sys.argv[1]
    unit_id = f"U{n}"
    inventario_nombre = f"{unit_id}-nc1-inventario.json"

    # Localizar worktree
    if len(sys.argv) >= 3:
        worktree_unidades = Path(sys.argv[2])
    else:
        worktree_unidades = DESKTOP / f"guia-didactica-extract-U{n}" / "unidades"

    src = worktree_unidades / unit_id / inventario_nombre
    dst_dir = PROJECT / "unidades" / unit_id
    dst = dst_dir / inventario_nombre

    # 1. Verificar que el inventario existe en el worktree
    if not src.exists():
        print(f"❌ No encontrado: {src}")
        sys.exit(1)

    # 2. Copiar a main, guardando versión previa en memoria para poder restaurar
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst_prev = dst.read_bytes() if dst.exists() else None
    shutil.copy2(src, dst)
    print(f"✓ Copiado: {src.name} → unidades/{unit_id}/")

    # 3. Validar — si falla, restaura main al estado anterior
    code, out = run(["python3", "scripts/validar_inventario.py", n])
    print(out)
    if code != 0:
        restaurar(dst, dst_prev)
        print("❌ Validación fallida. Main restaurado al estado anterior.")
        sys.exit(1)
    avisos = sum(1 for l in out.splitlines() if l.strip().startswith("⚠"))
    print(f"✓ Validación: 0 errores · {avisos} avisos")

    # 4. Actualizar hilos auto del reciclaje — si falla, restaura main
    code, out = run(["python3", "scripts/regenerar_reciclaje_vocabulario.py"])
    print(out)
    if code != 0:
        restaurar(dst, dst_prev)
        print("❌ Error al regenerar reciclaje. Main restaurado al estado anterior.")
        sys.exit(1)
    print("✓ Reciclaje actualizado")

    # 5. Commit aislado — solo los dos archivos, sin tocar el resto del índice
    d = json.loads(dst.read_text(encoding="utf-8"))
    acts = sum(len(p.get("actividades", [])) for p in d.get("paginas_detalle", []))
    cuadros = sum(len(p.get("cuadros", [])) for p in d.get("paginas_detalle", []))

    inventario_rel = str(dst.relative_to(PROJECT))
    reciclaje_rel = "unidades/nc1-reciclaje.json"
    msg = (
        f"integración {unit_id} a main (worktree extract/{unit_id}, "
        f"{acts} actividades, {cuadros} cuadros, 0/{avisos})"
    )
    # git commit -m <msg> -- <paths>: -m está antes de --, es una opción válida.
    # Commitea solo esos paths desde el working tree, aislado del índice actual.
    code, out = run(["git", "commit", "-m", msg, "--", inventario_rel, reciclaje_rel])
    print(out)
    if code != 0:
        print("❌ Error al hacer commit.")
        sys.exit(1)

    print(f"\n✅ {unit_id} integrada correctamente.")


if __name__ == "__main__":
    main()
