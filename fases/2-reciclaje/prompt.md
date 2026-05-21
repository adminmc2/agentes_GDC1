# Prompt envoltorio — Fase 2 Reciclaje (por unidad)

> **Qué es:** entry point operativo de fase 2. Describe cómo se procesa el reciclaje de **una unidad**. Espeja el rol de `prompt.md` en fase 1.
>
> ⚠️ **Fase 2 PAUSADA** (decisión 36). Este prompt es el contrato para cuando fase 2 se reactive; hoy no se ejecuta. El rediseño que lo sustenta está en `REDISEÑO-EN-CURSO.md`.
>
> ⚠️ **Estado: esqueleto-contrato.** El flujo de alto nivel está fijado por el modelo (`REDISEÑO-EN-CURSO.md` §1-§13). El **detalle operativo del pipeline** (script de Capa 1, sesión de Capa 2, validadores) es **Nivel 3** del rediseño, aún sin implementar — este prompt no asume que esos scripts existan.

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

1. **Capa 1 — esqueleto determinista.** Genera/actualiza mecánicamente los hilos de nivel `mapa` (desde `nc1-curso.json`) y `auto` (desde los 5 bloques del inventario). Precomputa lo mecánico del triage (`procedencia_indice: declarado`). *Procedimiento concreto: Nivel 3.*
2. **Capa 2 — sesión IA enriquecedora.** Sobre el esqueleto:
   - Aplica los **tres momentos de análisis** (`reglas-reciclaje.md` / §2.1): intra-unidad, cross-atrás, cross-adelante.
   - Asigna las **etiquetas** del evento (§3 de reglas) y completa el **triage** `procedencia_indice` (§4).
   - Trata anticipación (§5), formas verbales (§6), explicación (§7), siempre-presentes (§8).
   - Genera las **`propuestas[]`** de lo no obvio (§11) — la IA propone, el humano cierra.

## Criterio de cierre

El reciclaje de la unidad se cierra cuando cumple las 5 condiciones de `reglas-reciclaje.md` §13 (generado + chequeo estructural + validador cross-unidad R1-R5 + `propuestas[]` resueltas/diferidas + revisión editorial del autor).

⚠️ Los **comandos concretos** del chequeo estructural y del validador R1-R5 son **Nivel 3** (pendientes de implementar). Hasta entonces, el gate se aplica según el contrato de §13, no como comandos cerrados.

## Lo que NO se hace

- No editar a mano los hilos/eventos de nivel `mapa`/`auto` — se regeneran desde la fuente (`reglas-reciclaje.md` §12).
- No inventar títulos canónicos — el universo es cerrado (§2 de reglas); lo no canónico se escala como propuesta.
- No cerrar decisiones editoriales en automático — lo no obvio va a `propuestas[]` con cierre humano.
- No asumir que los scripts de Capa 1 / validadores existen — son Nivel 3.