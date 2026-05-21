# Fase 2 — Reciclaje de contenidos

> Auto-cargado por Claude Code al trabajar dentro de `fases/2-reciclaje/`. Contrato corto de la fase: qué produce, dónde input/output, cómo validar, reglas críticas, navegación.

> ⚠️ **Estado actual (2026-05-21, v11.49):** **FASE 2 PAUSADA** por decisión 36. El rediseño de fase 2 (modelo IA-first) tiene cerrados el **Nivel 1 — modelo conceptual** (§1-§10) y el **Nivel 2 — contrato operativo** (`schema-reciclaje.md`, `reglas-reciclaje.md` §1-§13, `prompt.md`, este `CLAUDE.md`). Pendiente: **Nivel 3 — implementación** (pipeline de Capa 1/Capa 2, validadores estructural y cross-unidad R1-R5) y **Nivel 4 — reactivación operativa**. Los scripts viejos (`regenerar_reciclaje_mapa.py`, `regenerar_reciclaje_vocabulario.py`) y el `nc1-reciclaje.json` actual están en shape pre-rediseño (v10.114) y se sustituirán en el Nivel 3. El rediseño se construye en `REDISEÑO-EN-CURSO.md` (documento único; el viejo se archivó en `docs/historico/` en v11.34).

---

## Qué produce esta fase

Un mapa de hilos de reciclaje (`unidades/nc1-reciclaje.json`) que modela cómo cada contenido del curso se introduce, amplía, aplica, sistematiza o contrasta a lo largo de las unidades.

> **Alcance del rediseño activo (decidido 2026-05-20):** el rediseño de fase 2 en curso cubre los **bloques lingüísticos** del inventario — vocabulario, gramática, pronunciación/ortografía y verbal (más `perifrasis` derivado). Las **funciones comunicativas** y las **estrategias** quedan **pospuestas** a un desarrollo posterior; no las modela el rediseño vigente. Ver `REDISEÑO-EN-CURSO.md` §5 Nivel 1 y bitácora de `PROCESO-MAESTRO.md`.

El campo `nivel_analisis` indica el **grado de población de un mismo hilo** — no son tres archivos ni tres hilos paralelos: el hilo nace en `mapa`, se enriquece a `auto` y se completa a `detalle` (modelo recursivo, `REDISEÑO-EN-CURSO.md` §4.2):

| `nivel_analisis` | Qué añade | Fuente |
|---|---|---|
| `mapa` | Esqueleto: identidad del hilo + eventos básicos | `nc1-curso.json` (índice del curso) |
| `auto` | Enriquece los eventos: contenidos por unidad, etiquetas, triage | Inventarios `UX-nc1-inventario.json` (los 5 bloques — `REDISEÑO-EN-CURSO.md` §2.2) |
| `detalle` | Justificación lingüístico-pedagógica del procedimiento | Análisis cross-unidad sobre el inventario |

La población la hace el **pipeline de fase 2** (Capa 1 determinista + Capa 2 IA) — su implementación es Nivel 3 del rediseño, pendiente. Los scripts viejos `regenerar_reciclaje_*.py` son pre-rediseño.

## Input y output

- **Input mapa:** `unidades/nc1-curso.json` — índice editorial del curso con vocabulario, gramática, comunicación, etc. por unidad.
- **Input auto:** `unidades/UX/UX-nc1-inventario.json` — inventarios extraídos en fase 1.
- **Output:** `unidades/nc1-reciclaje.json` — único archivo con todos los hilos.

## Cómo se invoca

**Modelo nuevo (rediseño):** el entry point operativo de fase 2 es `prompt.md` — procesa el reciclaje de una unidad. Su pipeline (Capa 1/Capa 2) es Nivel 3, pendiente de implementar.

**Modelo viejo (mientras fase 2 sigue PAUSADA):** los comandos de abajo siguen sirviendo para inspección, pero no reflejan el contrato nuevo.

**Nivel mapa — una sola vez** (o cuando cambia `nc1-curso.json`):
```bash
python3 scripts/regenerar_reciclaje_mapa.py
```
Este script crea `nc1-reciclaje.json` si no existe. Debe ejecutarse antes que el de auto.

**Nivel auto — fase 2 PAUSADA actualmente (decisión 36, v10.108):**

Mientras dure la pausa de fase 2 (canon semántico de fase 1 en desarrollo), `scripts/integrar_unidad.py` **no regenera reciclaje por defecto**. La integración de una unidad copia el inventario, valida y hace commit del inventario, pero deja `nc1-reciclaje.json` congelado.

Para forzar la regeneración en una integración concreta (excepción consciente), usar el flag explícito `--regenerar-reciclaje`:

```bash
# Comportamiento por defecto: NO regenera reciclaje
python3 scripts/integrar_unidad.py 6

# Excepción consciente: SÍ regenera (commit incluye reciclaje)
python3 scripts/integrar_unidad.py 6 --regenerar-reciclaje
```

Cuando fase 2 se reactive, este flag puede dejar de ser necesario.

## Cómo validar

El **criterio de cierre** del reciclaje de una unidad (chequeo estructural + validador cross-unidad R1-R5 + revisión editorial) está definido en `reglas-reciclaje.md` §13. Los validadores como script son Nivel 3 del rediseño (pendientes). Mientras fase 2 esté PAUSADA, el gate no se ejecuta.

*(Los comandos del modelo viejo — `regenerar_reciclaje_mapa.py` y vista RECICLAJE del dashboard — siguen sirviendo para inspección, pero no reflejan el contrato nuevo.)*

---

## Reglas críticas

1. **Naming obligatorio:** el `titulo` de un hilo es siempre el nombre canónico del contenido tal como aparece en `nc1-curso.json` o en las claves de los bloques top-level consolidados del inventario (`vocabulario_consolidado.{principal,recurrente}`, `gramatica_consolidada.{principal,recurrente}`, `pronunciacion_ortografia_consolidada.{principal,recurrente}`, `tiempos_y_verbos_consolidado[].lema`). Nunca un nombre inventado o genérico. *(Tras v10.115 la clave `campo_semantico` por actividad fue eliminada; el naming canónico se toma ahora de los bloques consolidados y de las referencias en las 4 listas tipadas por actividad.)*
2. **Granularidad del hilo por bloque** (ver `REDISEÑO-EN-CURSO.md` §2.2): vocabulario → campo semántico; gramática → categoría gramatical; pron/orto → categoría; verbal → lema; perífrasis → perífrasis. No se agrupan unidades de análisis distintas en un mismo hilo (ej. "Países hispanohablantes" y "Nacionalidades" son dos hilos, no uno).
3. **Etiquetas con criterio:** el evento lleva una lista `etiquetas[]` (coexisten) — ver `reglas-reciclaje.md` §3. *(El modelo nuevo sustituye la `accion` única del modelo viejo por la lista de etiquetas.)*
4. **Los scripts no inventan:** si un contenido no aparece en la fuente, no se genera hilo. Los scripts solo leen, no interpretan.
5. **No editar `nc1-reciclaje.json` a mano para hilos mapa/auto.** Para cambiar un hilo: editar `nc1-curso.json` (nivel mapa) o el inventario correspondiente (nivel auto) y regenerar con el script.

---

## Para qué consultar qué archivo

| Pregunta | Archivo |
|---|---|
| ¿Cuándo separar o agrupar hilos? ¿Qué nombre usar? | `reglas-reciclaje.md` §1 (granularidad) y §2 (naming canónico) |
| ¿Qué etiquetas asignar a cada evento? | `reglas-reciclaje.md` §3 |
| ¿Cómo se clasifica respecto al índice? | `reglas-reciclaje.md` §4 (triage `procedencia_indice`) |
| ¿Cómo funcionan los scripts de Capa 1? | Pendiente — Nivel 3 del rediseño (`REDISEÑO-EN-CURSO.md` §5). |
| ¿Qué shape tiene nc1-reciclaje.json? | `schema-reciclaje.md` (contrato del rediseño nuevo) · `../../PROCESO-MAESTRO.md` §B1.5 (modelo viejo) |