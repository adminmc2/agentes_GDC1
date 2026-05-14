# Worktree de prueba — Contrato v10.115 (fase 1)

> **Este worktree NO es el repo principal.** Existe solo para certificar el contrato v10.115 (reset IA-first de fase 1) antes de fast-forward a `main`.

## Identidad esperada de esta carpeta

| Comprobación | Valor esperado |
|---|---|
| `git rev-parse --show-toplevel` | `/Users/armandocruz/Desktop/guia-prueba-v10.115` |
| `git branch --show-current` | `v10.115-wip` |

Si abres un chat aquí y la herramienta reporta otra cosa, el chat está montado en el workspace equivocado y la corrida **no debe empezar**.

## Identidad esperada del contrato documental

`fases/1-extraccion-inventario/reglas-operativas.md` debe contener encabezados:

- `### §0.1. Propuesta-en-chat ante toda decisión no clara`
- `### §0.3. Procedimiento OBLIGATORIO de poblado de `recurrente``
- `### §6.5. Sufijo `@R` en fuentes`

Si el archivo contiene en su lugar `§5.10`, `§5.11`, `§5.12`, `§5.13` o `§5.14`, estás viendo el contrato viejo (v10.114). La corrida **no debe empezar**.

## Protocolo obligatorio antes de la extracción

1. Abrir VSCode con esta carpeta como root del workspace (no basta con `cd` en la terminal de una ventana ya abierta sobre el repo principal).
2. Lanzar un chat limpio de Claude Code.
3. Enviar como primer mensaje el **Ping de control Git**.
4. Solo si pasa, enviar el **Ping de control documental**.
5. Solo si pasa, enviar el **Prompt de extracción**.

Los tres bloques los pasa el autor por separado. Si cualquier ping falla, abandonar el chat sin reutilizarlo.

## Si la prueba pasa

Fast-forward de `main` → `v10.115-wip` en el repo principal y eliminación de este worktree.

## Si la prueba falla

Diagnóstico, ajustes en `v10.115-wip`, nuevo intento. Los artefactos de cualquier corrida inválida se archivan en `docs/historico/pruebas-fallidas/` (en el repo principal), no se borran.
