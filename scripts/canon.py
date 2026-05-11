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

Estado: paso 1 — esqueleto + cargar_canon funcional. Resto stub.
"""
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
CANON_PATH = (
    PROJECT
    / "fases"
    / "1-extraccion-inventario"
    / "campos-semanticos-canonicos.json"
)

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
    raise NotImplementedError("Implementación en paso 2/posteriores.")


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
    raise NotImplementedError("Implementación en paso 2/posteriores.")


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