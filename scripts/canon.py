#!/usr/bin/env python3
"""
Módulo compartido del canon semántico de fase 1.

Single point of contact para cualquier script que necesite leer, validar
o modificar el canon de campos semánticos (`campos-semanticos-canonicos.json`).

Cuatro funciones públicas:

    cargar_canon()
        Lee el JSON canónico y lo devuelve como dict. Sin validación
        (validación opcional vía validar_canon).

    validar_canon(canon)
        Comprueba los 9 invariantes. Devuelve lista de errores (vacía si OK).

    escribir_canon(canon, path=None)
        Valida y persiste atómicamente. Backup del previo + lock + escritura.
        Aborta sin tocar disco si validar_canon falla.

    detectar_pendientes(inventarios_paths=None)
        Recorre los inventarios indicados (todos por defecto) y devuelve
        la lista de campos no canónicos detectados: `campo_semantico` de
        actividades + claves de `vocabulario_consolidado.{principal,
        recurrente,comprension}`. No modifica nada.

Política, rollout y árbol de decisión: ver
`fases/1-extraccion-inventario/reglas-operativas.md` §5.6.

Schema del JSON canónico: ver
`fases/1-extraccion-inventario/schema-inventario.md` §9-§10.

Estado: paso 2 — cargar/validar/escribir implementados. detectar_pendientes stub.
"""
import fcntl
import json
import os
import tempfile
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
CANON_PATH = (
    PROJECT
    / "fases"
    / "1-extraccion-inventario"
    / "campos-semanticos-canonicos.json"
)
CURSO_PATH = PROJECT / "unidades" / "nc1-curso.json"

ORIGEN_VALIDOS = {"indice", "pcic_a1", "excepcion"}


def cargar_canon(path: Path | None = None) -> dict:
    """Lee el JSON canónico y lo devuelve como dict.

    Args:
        path: Ruta del JSON. Por defecto: `CANON_PATH`.

    Returns:
        Diccionario con el contenido del canon.

    Raises:
        FileNotFoundError: si el archivo no existe.
        json.JSONDecodeError: si el archivo no es JSON válido.
    """
    p = Path(path) if path is not None else CANON_PATH
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def validar_canon(canon: dict) -> list[str]:
    """Aplica los 9 invariantes del canon.

    Invariantes:
        1. Estructura mínima: top-level con `version`, `actualizado`, `campos`.
           Cada entrada de `campos` con `canonico`, `origen`, `aliases_indice`,
           `aliases_auto`.
        2. Enum cerrado de `origen`: solo {`indice`, `pcic_a1`, `excepcion`}.
        3. Nota obligatoria si `origen == "excepcion"`: string no vacío.
        4. Unicidad global de `canonico`.
        5. Unicidad global de aliases (un alias no aparece en más de una
           entrada, sea indice o auto).
        6. No autorreferencia: un `canonico` no puede aparecer en sus propios
           `aliases_indice` ni `aliases_auto`.
        7. Coherencia `origen=indice` ↔ `nc1-curso.json`: el `canonico` (o
           algún `aliases_indice`) debe existir literalmente en
           `vocabulario[]` o `contenido_general[]`.
        8. Coherencia `origen=pcic_a1`: `aliases_indice` debe estar vacía.
        9. No colisión alias↔canónico ajeno: ningún alias coincide con el
           `canonico` de otra entrada.

    Args:
        canon: Diccionario del canon.

    Returns:
        Lista de strings con los errores detectados. Lista vacía si OK.
    """
    errores: list[str] = []

    # Invariante 1 — estructura mínima top-level
    for clave in ("version", "actualizado", "campos"):
        if clave not in canon:
            errores.append(f"[inv-1] falta clave top-level '{clave}'")
    if "campos" in canon and not isinstance(canon["campos"], list):
        errores.append("[inv-1] 'campos' debe ser lista")
        return errores  # sin lista no se puede seguir
    if errores:
        return errores

    # Invariante 1 — estructura mínima por entrada
    for i, entrada in enumerate(canon["campos"]):
        if not isinstance(entrada, dict):
            errores.append(f"[inv-1] campos[{i}] debe ser dict")
            continue
        for clave in ("canonico", "origen", "aliases_indice", "aliases_auto"):
            if clave not in entrada:
                errores.append(f"[inv-1] campos[{i}] falta clave '{clave}'")
        # Tipos básicos
        if not isinstance(entrada.get("canonico"), str) or not entrada.get("canonico", "").strip():
            errores.append(f"[inv-1] campos[{i}].canonico debe ser string no vacío")
        for clave in ("aliases_indice", "aliases_auto"):
            v = entrada.get(clave)
            if v is not None and not isinstance(v, list):
                errores.append(f"[inv-1] campos[{i}].{clave} debe ser lista")
            elif isinstance(v, list):
                for j, a in enumerate(v):
                    if not isinstance(a, str) or not a.strip():
                        errores.append(f"[inv-1] campos[{i}].{clave}[{j}] debe ser string no vacío")

    if errores:
        return errores  # cortar antes de invariantes que asumen estructura OK

    # Invariante 2 — enum cerrado de origen
    for i, entrada in enumerate(canon["campos"]):
        if entrada["origen"] not in ORIGEN_VALIDOS:
            errores.append(
                f"[inv-2] campos[{i}] '{entrada['canonico']}': origen "
                f"'{entrada['origen']}' no es válido (debe ser {ORIGEN_VALIDOS})"
            )

    # Invariante 3 — nota obligatoria si origen == excepcion
    for i, entrada in enumerate(canon["campos"]):
        if entrada["origen"] == "excepcion":
            nota = entrada.get("nota")
            if not isinstance(nota, str) or not nota.strip():
                errores.append(
                    f"[inv-3] campos[{i}] '{entrada['canonico']}': origen=excepcion "
                    f"requiere 'nota' string no vacío"
                )

    # Invariante 4 — unicidad global de canonico
    visto_canonico: dict[str, int] = {}
    for i, entrada in enumerate(canon["campos"]):
        c = entrada["canonico"]
        if c in visto_canonico:
            errores.append(
                f"[inv-4] canonico '{c}' duplicado en campos[{visto_canonico[c]}] y campos[{i}]"
            )
        else:
            visto_canonico[c] = i

    # Invariante 5 — unicidad global de aliases (indice + auto, todos juntos)
    visto_alias: dict[str, tuple[int, str]] = {}  # alias → (idx_entrada, lista_origen)
    for i, entrada in enumerate(canon["campos"]):
        for lista_nombre in ("aliases_indice", "aliases_auto"):
            for a in entrada.get(lista_nombre, []) or []:
                if a in visto_alias:
                    prev_i, prev_lista = visto_alias[a]
                    errores.append(
                        f"[inv-5] alias '{a}' aparece en campos[{prev_i}].{prev_lista} "
                        f"y en campos[{i}].{lista_nombre}"
                    )
                else:
                    visto_alias[a] = (i, lista_nombre)

    # Invariante 6 — no autorreferencia (canonico no en sus propios aliases)
    for i, entrada in enumerate(canon["campos"]):
        c = entrada["canonico"]
        for lista_nombre in ("aliases_indice", "aliases_auto"):
            if c in (entrada.get(lista_nombre, []) or []):
                errores.append(
                    f"[inv-6] campos[{i}] '{c}': canonico aparece en sus propios {lista_nombre}"
                )

    # Invariante 7 — coherencia origen=indice ↔ nc1-curso.json
    if any(e["origen"] == "indice" for e in canon["campos"]):
        curso: dict | None = None
        try:
            curso = json.loads(CURSO_PATH.read_text(encoding="utf-8"))
        except FileNotFoundError:
            errores.append(f"[inv-7] no se puede leer {CURSO_PATH} para validar origen=indice (archivo no existe)")
        except json.JSONDecodeError as e:
            errores.append(f"[inv-7] {CURSO_PATH} no es JSON válido: {e}")
        if curso is not None:
            literales_indice: set[str] = set()
            for u in curso.get("unidades", []):
                for clave in ("vocabulario", "contenido_general"):
                    v = u.get(clave)
                    if isinstance(v, list):
                        literales_indice.update(s for s in v if isinstance(s, str))
            for i, entrada in enumerate(canon["campos"]):
                if entrada["origen"] != "indice":
                    continue
                candidatos = {entrada["canonico"]} | set(entrada.get("aliases_indice", []) or [])
                if not (candidatos & literales_indice):
                    errores.append(
                        f"[inv-7] campos[{i}] '{entrada['canonico']}' (origen=indice): ni el canonico "
                        f"ni ningún aliases_indice existen literalmente en vocabulario[]/contenido_general[] "
                        f"de nc1-curso.json"
                    )

    # Invariante 8 — pcic_a1 sin aliases_indice
    for i, entrada in enumerate(canon["campos"]):
        if entrada["origen"] == "pcic_a1" and entrada.get("aliases_indice"):
            errores.append(
                f"[inv-8] campos[{i}] '{entrada['canonico']}' (origen=pcic_a1): "
                f"aliases_indice debe estar vacío"
            )

    # Invariante 9 — no colisión alias ↔ canonico ajeno
    canonicos_set = {e["canonico"] for e in canon["campos"]}
    for i, entrada in enumerate(canon["campos"]):
        propio = entrada["canonico"]
        for lista_nombre in ("aliases_indice", "aliases_auto"):
            for a in entrada.get(lista_nombre, []) or []:
                if a in canonicos_set and a != propio:
                    errores.append(
                        f"[inv-9] alias '{a}' en campos[{i}].{lista_nombre} coincide con "
                        f"el canonico de otra entrada"
                    )

    return errores


def escribir_canon(canon: dict, path: Path | None = None) -> None:
    """Valida los invariantes y persiste atómicamente.

    Comportamiento:
        1. Llama a `validar_canon(canon)`. Si hay errores, aborta sin tocar disco.
        2. Crea backup del archivo previo (si existe) en
           `<path>.bak`.
        3. Escribe el nuevo contenido a un archivo temporal y lo renombra
           atómicamente sobre `path`.
        4. Usa lock (FileLock o similar) para evitar carreras entre sesiones.

    Args:
        canon: Diccionario del canon ya completo.
        path: Ruta destino. Por defecto: `CANON_PATH`.

    Raises:
        ValueError: si `validar_canon` devuelve errores.
        OSError: si falla la escritura atómica.
    """
    errores = validar_canon(canon)
    if errores:
        raise ValueError(
            "El canon no pasa los invariantes; aborto sin tocar disco:\n  - "
            + "\n  - ".join(errores)
        )

    destino = Path(path) if path is not None else CANON_PATH
    destino.parent.mkdir(parents=True, exist_ok=True)

    # Lock por archivo (advisory, no impide lectura)
    lock_path = destino.with_suffix(destino.suffix + ".lock")
    with lock_path.open("w") as lock_file:
        fcntl.flock(lock_file.fileno(), fcntl.LOCK_EX)
        try:
            # Backup del previo si existe
            if destino.exists():
                backup = destino.with_suffix(destino.suffix + ".bak")
                backup.write_bytes(destino.read_bytes())

            # Escritura atómica: archivo temporal + rename
            tmp_fd, tmp_name = tempfile.mkstemp(
                prefix=destino.name + ".",
                suffix=".tmp",
                dir=str(destino.parent),
            )
            try:
                with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
                    json.dump(canon, f, ensure_ascii=False, indent=2)
                    f.write("\n")
                # Normalizar permisos al estándar del repo (rw-r--r--).
                # mkstemp crea con 0600 por seguridad; aquí queremos lectura
                # general como cualquier otro JSON del proyecto.
                os.chmod(tmp_name, 0o644)
                os.replace(tmp_name, destino)
            except Exception:
                # Limpieza si algo falla antes del rename
                try:
                    os.unlink(tmp_name)
                except OSError:
                    pass
                raise
        finally:
            fcntl.flock(lock_file.fileno(), fcntl.LOCK_UN)
    # Limpieza del archivo de lock (best-effort)
    try:
        lock_path.unlink()
    except OSError:
        pass


def detectar_pendientes(inventarios_paths: list[Path] | None = None) -> list[dict]:
    """Detecta campos no canónicos en los inventarios indicados.

    Recorre dos superficies en cada inventario:
        - `actividad.campo_semantico` (campo opcional en cada actividad).
        - Claves de `vocabulario_consolidado.principal/recurrente/comprension`,
          excluyendo la clave reservada `_descripcion`.

    Para cada valor encontrado, busca en el canon:
        - Como `canonico` literal → no pendiente.
        - Como alias en `aliases_indice` o `aliases_auto` → pendiente con
          sugerencia (el canónico al que apunta).
        - Sin match → pendiente sin sugerencia.

    Args:
        inventarios_paths: Lista de paths a inventarios. Por defecto:
            todos los `unidades/U*/U*-nc1-inventario.json`.

    Returns:
        Lista de dicts con la forma:
            {
                "unidad": <int>,
                "ubicacion": <str — ej. "vocabulario_consolidado.principal" o "actividad/U5-p52-act01.campo_semantico">,
                "valor": <str — el campo no canónico hallado>,
                "sugerencia": <str | None — canónico sugerido si coincide con alias>,
            }
    """
    raise NotImplementedError("Implementación en paso 2/posteriores.")


if __name__ == "__main__":
    # Autoverificación mínima del módulo (paso 1).
    print(f"canon.py — módulo cargado")
    print(f"PROJECT: {PROJECT}")
    print(f"CANON_PATH: {CANON_PATH}")
    print(f"CANON_PATH existe: {CANON_PATH.exists()}")
    print(f"ORIGEN_VALIDOS: {ORIGEN_VALIDOS}")
    for fn in (cargar_canon, validar_canon, escribir_canon, detectar_pendientes):
        print(f"  {fn.__name__}: {fn.__doc__.splitlines()[0] if fn.__doc__ else '(sin docstring)'}")