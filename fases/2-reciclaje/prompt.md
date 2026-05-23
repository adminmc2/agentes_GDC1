# Prompt envoltorio — Fase 2 Reciclaje (por unidad)

> **Qué es:** entry point operativo de fase 2. Describe cómo se procesa el reciclaje de **una unidad**. Espeja el rol de `prompt.md` en fase 1.
>
> ✅ **Fase 2 REACTIVADA** (v11.69 — pausa de decisión 36 levantada). El pipeline está cerrado en sus cuatro niveles de herramienta: Capa 1 implementada (`scripts/generar_reciclaje_capa1.py`), validadores del gate como script (`validar_reciclaje.py`, `validar_cross_unidad.py`), `nc1-reciclaje.json` regenerado al shape del rediseño. El rediseño que lo sustenta está en `REDISEÑO-EN-CURSO.md`.
>
> ⚠️ **La Capa 2 no se ha estrenado.** El procedimiento de la sesión IA enriquecedora (§12) está cerrado como contrato pero nunca se ha ejecutado: la primera unidad que se procese es también el shakedown de la Capa 2 — revísala con ese ojo.

---

## Qué produce

El **reciclaje incremental de una unidad**: la actualización de `unidades/nc1-reciclaje.json` con los hilos y eventos de la unidad recién integrada, según el modelo de hilos del rediseño.

## Lectura mínima obligatoria

**Gate de arranque:** antes de procesar, declarar en chat haber leído los tres contratos vivos de fase 2:

- `CLAUDE.md` de fase 2 — contrato corto.
- `schema-reciclaje.md` — shape canónico de `nc1-reciclaje.json`.
- `reglas-reciclaje.md` — autoridad decisional (cómo decidir y poblar).

## Input y output

- **Input:** `unidades/nc1-curso.json` (índice del curso) + el inventario de la unidad `UX-nc1-inventario.json` + los inventarios de las unidades anteriores (necesarios para el análisis cross-atrás) + los registries canónicos.
- **Output:** `unidades/nc1-reciclaje.json` actualizado.

## Flujo operativo

El procesamiento es híbrido en dos capas, **no a la vez** (`REDISEÑO-EN-CURSO.md` §1.3):

1. **Capa 1 — esqueleto determinista.** Genera/actualiza mecánicamente los hilos de nivel `mapa` (desde `nc1-curso.json`) y `auto` (desde los 5 bloques del inventario). Resuelve mecánicamente `procedencia_indice` para vocabulario, gramática, pron/orto y perífrasis: `declarado` / `reconciliado` (con prefijo `indice:` o `pcic:`) / `nuevo` (v11.76). En verbal la procedencia queda sin asignar — la decide Capa 2. *Procedimiento: `REDISEÑO-EN-CURSO.md` §11; script: `python3 scripts/generar_reciclaje_capa1.py`.*
2. **Capa 2 — sesión IA enriquecedora.** Sobre el esqueleto:
   - Aplica los **tres momentos de análisis** (`reglas-reciclaje.md` / §2.1): intra-unidad, cross-atrás, cross-adelante.
   - **Asigna las `etiquetas`** del evento (§3 de reglas), **escribe `explicacion`** cuando haya cuadro (§7) y **escala `propuestas[]`** lo no obvio (§11).
   - Trata anticipación (§5), formas verbales (§6), siempre-presentes (§8).
   - `procedencia_indice` (§4) **no** forma parte del núcleo ordinario de Capa 2 desde v11.76: la Capa 1 la resuelve mecánicamente para vocabulario, gramática, pron/orto y perífrasis. Capa 2 solo la toca en dos casos: (a) **hilos verbales** —`verbos-canonicos.json` no expone respaldo estructurado, así que la procedencia llega sin asignar y la decide la sesión—; (b) **corrección excepcional** de un caso mecánicamente mal clasificado.

## Criterio de cierre

El reciclaje de la unidad se cierra cuando cumple las 5 condiciones de `reglas-reciclaje.md` §13 (generado + chequeo estructural + validador cross-unidad R1-R5 + `propuestas[]` resueltas/diferidas + revisión editorial del autor).

Comandos del gate: `python3 scripts/validar_reciclaje.py` (chequeo estructural §13a) y `python3 scripts/validar_cross_unidad.py` (validador cross-unidad R1-R5 §13b). La revisión editorial del autor no es automatizable.

## Lo que NO se hace

- No editar a mano los hilos/eventos de nivel `mapa`/`auto` — se regeneran desde la fuente (`reglas-reciclaje.md` §12).
- No inventar títulos canónicos — el universo es cerrado (§2 de reglas); lo no canónico se escala como propuesta.
- No cerrar decisiones editoriales en automático — lo no obvio va a `propuestas[]` con cierre humano.
- No dar por rodada la Capa 2 hasta que su primera corrida real lo confirme.