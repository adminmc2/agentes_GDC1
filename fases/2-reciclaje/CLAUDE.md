# Fase 2 — Reciclaje de contenidos

> Auto-cargado por Claude Code al trabajar dentro de `fases/2-reciclaje/`. Contrato corto de la fase: qué produce, dónde input/output, cómo validar, reglas críticas, navegación.

> ✅ **Hito de reactivación (2026-05-22, v11.69):** **FASE 2 REACTIVADA** — la pausa de decisión 36 queda levantada. Los cuatro niveles **originales** del rediseño (modelo IA-first) están cerrados en su parte de herramienta: **Nivel 1** modelo conceptual (§1-§10), **Nivel 2** contrato operativo (`schema-reciclaje.md`, `reglas-reciclaje.md`, `prompt.md`, este `CLAUDE.md`), **Nivel 3** diseño del pipeline (§11-§13 + `reglas-reciclaje.md` §14), **Nivel 4** implementación en código — `scripts/generar_reciclaje_capa1.py` (Capa 1), `scripts/validar_reciclaje.py` (chequeo estructural §13a), `scripts/validar_cross_unidad.py` (validador R1-R5 §13b) — y `nc1-reciclaje.json` regenerado al shape del rediseño (v11.68). Los scripts viejos `regenerar_reciclaje_*.py` quedan obsoletos (pre-rediseño). **Nivel 5 abierto en v12.19** (procedimentalización de Capa 2) — ver `REDISEÑO-EN-CURSO.md` §5.
>
> ⚠️ **Capa 2 corrida como shakedown en U0-U3** (v11.80, v11.84, v12.4, v12.10, v12.18) — el procedimiento §12 funciona como contrato general, pero las cuatro sesiones evidenciaron que el contrato sigue **sub-procedimentado**: las etiquetas (§3 reglas) están definidas semánticamente sin árbol de decisión cerrado; la procedencia verbal (§4) queda como excepción decidida por la sesión; el cierre cross-hilo (§15) deja `tipo` y dirección al humano. Cierre operativo abierto en `REDISEÑO-EN-CURSO.md` §5 Nivel 5 (v12.19) — pipeline de sub-trabajos discretos, mecánico + IA aislada, hasta que el contrato sea reproducible bajo Claude Code supervisado hoy y bajo agente autónomo mañana. **No abrir Capa 2 sobre U4-U9 hasta que el Nivel 5 cierre los puntos 2-4 del plan.**

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

La población la hace el **pipeline de fase 2** (Capa 1 determinista + Capa 2 IA). La Capa 1 está implementada en código (`scripts/generar_reciclaje_capa1.py`); la Capa 2 es una sesión IA supervisada por unidad (procedimiento `REDISEÑO-EN-CURSO.md` §12, corrida como shakedown en U0-U3; su procedimentalización está abierta en §5 Nivel 5). Los scripts viejos `regenerar_reciclaje_*.py` son pre-rediseño y quedan obsoletos.

## Input y output

- **Input mapa:** `unidades/nc1-curso.json` — índice editorial del curso con vocabulario, gramática, comunicación, etc. por unidad.
- **Input auto:** `unidades/UX/UX-nc1-inventario.json` — inventarios extraídos en fase 1.
- **Output:** `unidades/nc1-reciclaje.json` — único archivo con todos los hilos.

## Cómo se invoca

El entry point operativo de fase 2 es `prompt.md` — procesa el reciclaje de una unidad. El pipeline es híbrido en dos capas (`REDISEÑO-EN-CURSO.md` §1.3):

**Capa 1 — esqueleto determinista.** Script:
```bash
python3 scripts/generar_reciclaje_capa1.py            # regenera nc1-reciclaje.json (modo íntegro)
python3 scripts/generar_reciclaje_capa1.py --dry-run  # valida sin escribir
```
Genera los hilos `mapa` (desde `nc1-curso.json`) y `auto` (desde los inventarios), precomputa el triage mecánico (`procedencia_indice: declarado`) y preserva `propuestas[]`. No asigna etiquetas ni decide nada editorial — eso es Capa 2.

**Capa 2 — sesión IA enriquecedora.** No es un script: es una sesión IA supervisada por unidad (`REDISEÑO-EN-CURSO.md` §12) que, sobre el esqueleto de Capa 1, asigna etiquetas, completa el triage, escribe `explicacion` y escala `propuestas[]`. La IA propone, el autor cierra. **Corrida como shakedown en U0-U3** — el contrato sigue sub-procedimentado; ver `REDISEÑO-EN-CURSO.md` §5 Nivel 5 (v12.19) para el plan de cierre operativo y el banner de estado arriba.

## Sincronización automática de `_meta.version`

`_meta.version` y `_meta.fecha` del canónico `nc1-reciclaje.json` se mantienen al día automáticamente por un pre-commit hook (v11.82). El hook detecta cuándo el JSON está en el commit y bumpea `_meta` al estado actual (versión máxima de `CHANGELOG.md` + fecha de hoy) antes de cerrar el commit. Si no se ha instalado el hook, ejecutar una vez:

```bash
git config core.hooksPath scripts/hooks
```

Si conviene sincronizar a mano (sin commit): `python3 scripts/sync_meta_reciclaje.py` (idempotente).

## Cómo validar

El **criterio de cierre** del reciclaje de una unidad está en `reglas-reciclaje.md` §13-§14. Los dos validadores automáticos del gate ya existen como script:

```bash
python3 scripts/validar_reciclaje.py        # (a) chequeo estructural contra schema-reciclaje.md
python3 scripts/validar_cross_unidad.py     # (b) validador cross-unidad R1-R5
```

El chequeo estructural debe dar **0 errores**; el cross-unidad no debe dejar **alertas R1/R3/R4 sin resolver** (R2/R5 son pre-condiciones que abortan). El tercer componente del gate —revisión editorial del autor— no es automatizable.

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
| ¿Cómo funciona el pipeline de Capa 1/Capa 2? | Diseño cerrado — `REDISEÑO-EN-CURSO.md` §11-§13. Implementación en código (Nivel 4 ✅): `scripts/generar_reciclaje_capa1.py`, `scripts/validar_reciclaje.py`, `scripts/validar_cross_unidad.py`. Procedimentalización de Capa 2 en curso (Nivel 5, §5). |
| ¿Qué shape tiene nc1-reciclaje.json? | `schema-reciclaje.md` (contrato del rediseño nuevo) · `../../PROCESO-MAESTRO.md` §B1.5 (modelo viejo) |