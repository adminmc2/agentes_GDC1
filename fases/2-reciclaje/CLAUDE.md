# Fase 2 — Reciclaje de contenidos

> Auto-cargado por Claude Code al trabajar dentro de `fases/2-reciclaje/`. Contrato corto de la fase: qué produce, dónde input/output, cómo validar, reglas críticas, navegación.

> ⚠️ **Estado actual (2026-05-15, v10.120):** **FASE 2 PAUSADA** por decisión 36 (v10.108). Bloqueo operativo añadido tras v10.115-118: los **scripts** `regenerar_reciclaje_mapa.py` y `regenerar_reciclaje_vocabulario.py` y el **output** `unidades/nc1-reciclaje.json` (fechado 2026-05-11) están en **shape v10.114** (pre-rediseño). Tras los cambios de fase 1 v10.115-118 (eliminación de `campo_semantico` y de `vocabulario_consolidado.comprension`, renombrado `fonetica → pronunciacion_ortografia`, 4 bloques top-level consolidados nuevos, 4 listas tipadas por actividad), los scripts fallarán si se ejecutan contra inventarios en shape v10.117. La reactivación operativa de fase 2 está **bloqueada por el procesamiento de unidades U1-U9 con shape v10.117** (U0 ya migrada en v10.119) y exige adaptación previa de los 2 scripts + regeneración íntegra de `nc1-reciclaje.json`. Pendiente: ratificar/formalizar decisión P1 (opción A) + implementar Capa 1 (R1-R5). El rediseño activo se construye paso a paso en `REDISEÑO-EN-CURSO.md` (documento único; el viejo se archivó en `docs/historico/` el 2026-05-20, v11.34).

---

## Qué produce esta fase

Un mapa de hilos de reciclaje (`unidades/nc1-reciclaje.json`) que modela cómo cada contenido del curso se introduce, amplía, aplica, sistematiza o contrasta a lo largo de las unidades.

> **Alcance del rediseño activo (decidido 2026-05-20):** el rediseño de fase 2 en curso cubre los **bloques lingüísticos** del inventario — vocabulario, gramática, pronunciación/ortografía y verbal (más `perifrasis` derivado). Las **funciones comunicativas** y las **estrategias** quedan **pospuestas** a un desarrollo posterior; no las modela el rediseño vigente. Ver `REDISEÑO-EN-CURSO.md` §5 Nivel 1 y bitácora de `PROCESO-MAESTRO.md`.

El archivo tiene tres niveles de análisis que se generan por separado:

| nivel_analisis | Origen | Generado por |
|---|---|---|
| `mapa` | `nc1-curso.json` (índice editorial del curso) | Script `regenerar_reciclaje_mapa.py` |
| `auto` | Inventarios `UX-nc1-inventario.json` (los 5 bloques: vocabulario, gramática, pron/orto, verbal, perífrasis — ver `REDISEÑO-EN-CURSO.md` §2.2) | Script `regenerar_reciclaje_vocabulario.py` |
| `detalle` | Inventarios (actividades individuales) | Fase futura |

## Input y output

- **Input mapa:** `unidades/nc1-curso.json` — índice editorial del curso con vocabulario, gramática, comunicación, etc. por unidad.
- **Input auto:** `unidades/UX/UX-nc1-inventario.json` — inventarios extraídos en fase 1.
- **Output:** `unidades/nc1-reciclaje.json` — único archivo con todos los hilos.

## Cómo se invoca

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

1. `python3 scripts/regenerar_reciclaje_mapa.py` → sin errores.
2. `python3 diagrama.py` → `http://localhost:8081` → vista RECICLAJE → revisar timeline.

---

## Reglas críticas

1. **Naming obligatorio:** el `titulo` de un hilo es siempre el nombre canónico del contenido tal como aparece en `nc1-curso.json` o en las claves de los bloques top-level consolidados del inventario (`vocabulario_consolidado.{principal,recurrente}`, `gramatica_consolidada.{principal,recurrente}`, `pronunciacion_ortografia_consolidada.{principal,recurrente}`, `tiempos_y_verbos_consolidado[].lema`). Nunca un nombre inventado o genérico. *(Tras v10.115 la clave `campo_semantico` por actividad fue eliminada; el naming canónico se toma ahora de los bloques consolidados y de las referencias en las 4 listas tipadas por actividad.)*
2. **Granularidad del hilo por bloque** (ver `REDISEÑO-EN-CURSO.md` §2.2): vocabulario → campo semántico; gramática → categoría gramatical; pron/orto → categoría; verbal → lema; perífrasis → perífrasis. No se agrupan unidades de análisis distintas en un mismo hilo (ej. "Países hispanohablantes" y "Nacionalidades" son dos hilos, no uno).
3. **Acciones con criterio:** ver `reglas-reciclaje.md` §2 para la tabla de acciones (introduce/amplia/aplica/sistematiza/contrasta).
4. **Los scripts no inventan:** si un contenido no aparece en la fuente, no se genera hilo. Los scripts solo leen, no interpretan.
5. **No editar `nc1-reciclaje.json` a mano para hilos mapa/auto.** Para cambiar un hilo: editar `nc1-curso.json` (nivel mapa) o el inventario correspondiente (nivel auto) y regenerar con el script.

---

## Para qué consultar qué archivo

| Pregunta | Archivo |
|---|---|
| ¿Cuándo separar o agrupar hilos? ¿Qué nombre usar? | `reglas-reciclaje.md` §1 |
| ¿Qué acción asignar a cada evento? | `reglas-reciclaje.md` §2 |
| ¿Cómo funciona el script de mapa? | `regenerar_reciclaje_mapa.py` + `reglas-reciclaje.md` §3 |
| ¿Cómo funciona el script de auto? | `regenerar_reciclaje_vocabulario.py` + `reglas-reciclaje.md` §4 |
| ¿Qué shape tiene nc1-reciclaje.json? | `../../PROCESO-MAESTRO.md` §B1.5 |