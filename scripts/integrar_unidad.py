#!/usr/bin/env python3
"""
Integra el inventario de una unidad desde su worktree a main.

Pasos reales (en este orden):
1. Localiza el inventario en el worktree extract/UN.
2. Copia el inventario a unidades/UN/ guardando en memoria la versión previa si existe.
3. Valida. Si falla, restaura la versión previa (o borra si no había) y aborta.
4. [Opcional, OFF por defecto] Regenera nc1-reciclaje.json. Solo se ejecuta
   si se pasa --regenerar-reciclaje. Mientras fase 2 esté pausada (decisión
   36 de PROCESO-MAESTRO), el reciclaje no se toca en integraciones
   ordinarias.
5. Hace commit aislado: solo el inventario (más reciclaje si se regeneró).

Uso:
    python3 scripts/integrar_unidad.py <N>
    python3 scripts/integrar_unidad.py 6
    python3 scripts/integrar_unidad.py 6 --regenerar-reciclaje
    python3 scripts/integrar_unidad.py 6 /ruta/al/worktree/unidades

El worktree se busca por defecto en:
    ~/Desktop/guia-didactica-extract-U<N>/unidades/U<N>/

Si está en otra ruta, pásala como argumento posicional.
"""
import json
import subprocess
import sys
import shutil
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
DESKTOP = Path.home() / "Desktop"

# Flag de guardia para la regeneración de reciclaje. Cuando fase 2 se
# reactive, este flag puede dejar de ser necesario y la llamada volverá
# a ser parte del flujo por defecto. Ver decisión 36 de PROCESO-MAESTRO.
FLAG_REGENERAR_RECICLAJE = "--regenerar-reciclaje"


def run(cmd: list, cwd=None) -> tuple[int, str]:
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd or PROJECT)
    return r.returncode, (r.stdout + r.stderr).strip()


def restaurar(dst: Path, dst_prev: bytes | None):
    if dst_prev is not None:
        dst.write_bytes(dst_prev)
    else:
        dst.unlink(missing_ok=True)


def main():
    # Parsear args: 1 obligatorio (N), 1 opcional posicional (ruta worktree), 1 flag (--regenerar-reciclaje)
    args = sys.argv[1:]
    regenerar = FLAG_REGENERAR_RECICLAJE in args
    args = [a for a in args if a != FLAG_REGENERAR_RECICLAJE]

    if len(args) < 1:
        print(
            "Uso: python3 scripts/integrar_unidad.py <N> [ruta_worktree_unidades] "
            f"[{FLAG_REGENERAR_RECICLAJE}]\n"
            "  Sin --regenerar-reciclaje, el reciclaje queda congelado (fase 2 pausada)."
        )
        sys.exit(1)

    n = args[0]
    unit_id = f"U{n}"
    inventario_nombre = f"{unit_id}-nc1-inventario.json"

    # Localizar worktree
    if len(args) >= 2:
        worktree_unidades = Path(args[1])
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

    # 4. Regenerar reciclaje — OPCIONAL, off por defecto mientras fase 2 esté pausada
    reciclaje_path = PROJECT / "unidades" / "nc1-reciclaje.json"
    if regenerar:
        reciclaje_prev = reciclaje_path.read_bytes() if reciclaje_path.exists() else None
        code, out = run(["python3", "scripts/regenerar_reciclaje_vocabulario.py"])
        print(out)
        if code != 0:
            restaurar(dst, dst_prev)
            restaurar(reciclaje_path, reciclaje_prev)
            print("❌ Error al regenerar reciclaje. Main restaurado al estado anterior.")
            sys.exit(1)
        print("✓ Reciclaje actualizado")
    else:
        print("⏸ Reciclaje no regenerado (fase 2 pausada — usa --regenerar-reciclaje para forzar).")

    # 5. Commit aislado — solo el inventario, y reciclaje si se regeneró
    d = json.loads(dst.read_text(encoding="utf-8"))
    acts = sum(len(p.get("actividades", [])) for p in d.get("paginas_detalle", []))
    cuadros = sum(len(p.get("cuadros", [])) for p in d.get("paginas_detalle", []))

    inventario_rel = str(dst.relative_to(PROJECT))
    reciclaje_rel = "unidades/nc1-reciclaje.json"
    paths_commit = [inventario_rel]
    if regenerar:
        paths_commit.append(reciclaje_rel)

    msg = (
        f"integración {unit_id} a main (worktree extract/{unit_id}, "
        f"{acts} actividades, {cuadros} cuadros, 0/{avisos})"
    )
    # git add primero para que funcione tanto con archivos nuevos como con ya trackeados.
    run(["git", "add", "--"] + paths_commit)
    # git commit -m <msg> -- <paths>: limita el commit exactamente a esos paths.
    code, out = run(["git", "commit", "-m", msg, "--"] + paths_commit)
    print(out)
    if code != 0:
        print("❌ Error al hacer commit.")
        sys.exit(1)

    print(f"\n✅ {unit_id} integrada correctamente.")


if __name__ == "__main__":
    main()
