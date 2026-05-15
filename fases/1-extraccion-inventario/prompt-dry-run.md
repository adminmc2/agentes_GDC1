# Procesamiento de unidad — prompt dry-run con revisión iterativa

> **Propósito:** prompt envoltorio para procesar una unidad en chat limpio sin escribir nada hasta aprobación explícita del autor. Wrapper operativo sobre `prompt.md` (el contrato canónico de extracción). Pensado para usar **uno por unidad** en chats nuevos durante el lote de migración de U0-U9 al shape v10.117.
>
> **Cómo se usa:** copiar el cuerpo del prompt (debajo de la línea horizontal) en un chat nuevo de Claude Code dentro del workspace del repo. Sustituir `U[X]` y `[X]` por el número real de la unidad a procesar.

---

# Procesamiento de unidad — modo dry-run con revisión iterativa

Vas a procesar la unidad **U[X]** (cámbialo por el número que toca) siguiendo el flujo de fase 1 del proyecto.

## Contratos vivos a leer (en orden)

- `fases/1-extraccion-inventario/prompt.md` — entry point operativo.
- `fases/1-extraccion-inventario/schema-inventario.md` — shape canónico.
- `fases/1-extraccion-inventario/reglas-operativas.md` — autoridad operativa.
- `fases/1-extraccion-inventario/convenciones-y-casos.md` — transcripción y casebook (lookup puntual, no obligatorio leer entero).
- `fases/1-extraccion-inventario/glosario.md` — terminología (lookup).

**Precedencia jerárquica en caso de conflicto:** schema > reglas > convenciones.

## Registries canónicos disponibles (poblados — usa solo nombres literales)

- `campos-semanticos-canonicos.json` — 99 categorías léxicas.
- `verbos-canonicos.json` — 48 lemas verbales.
- `gramatica-canonica.json` — 17 categorías gramaticales.
- `pronunciacion-ortografia-canonica.json` — 7 categorías pron-ortográficas.

PCIC A1 como respaldo en `pcic-a1-*.json` (4 archivos).

## Modo de trabajo (importante — NO TE LO SALTES)

**NO escribas NINGÚN archivo durante esta corrida.** Trabajamos en dry-run:

1. Extraes el inventario completo de la unidad siguiendo el contrato.
2. **Presentas el resultado en chat**, sin tocar el filesystem para escribir el JSON definitivo.
3. Yo reviso lo que me presentas, doy feedback, pido cambios.
4. Iteramos las veces que haga falta.
5. **Solo cuando te dé OK explícito**, escribes el JSON final en `unidades/UX/UX-nc1-inventario.json`.

Sí puedes (necesitas) leer el PDF y los contratos. Lo que NO puedes hacer es persistir el output sin mi aprobación.

## Política operativa durante la extracción

- **§0.1 propuesta-en-chat**: si encuentras una decisión no clara durante la extracción (canónico ambiguo, frontera de clasificación, contenido raro), plantéala en chat con 2-4 opciones razonables ANTES de seguir. No dejes nada silencioso para presentarlo al final.
- Naming canónico literal del registry. PROHIBIDO inventar nombres.
- `_pendiente_canon` y `_funcion_ambigua` solo tras propuesta-en-chat.
- Sufijo `@R` en fuentes solo cuando el `tipo` está en los 5 productivos (regla §6.5).
- 4 listas tipadas siempre presentes en cada actividad (vacías si no aplica).

## Qué me presentas al terminar la extracción (todo en chat, no escribir)

1. **Inventario JSON completo** en bloque de código markdown.
2. **Resumen de estructura**: páginas extraídas, conteo de actividades por sección, conteo de cuadros, conteo de entradas en cada bloque consolidado.
3. **Trazado §0.3 A/B/C** en las 3 dimensiones con `recurrente` (vocabulario, gramática, pron-orto) — declarar barrido aunque alguna pasada termine en vacío.
4. **`_decisiones_ia`** registradas y por qué.
5. **Propuestas abiertas** (§0.1) que surgieron durante la corrida y mi resolución para cada una.
6. **Anomalías o gaps detectados** respecto al contrato (casos frontera, canon insuficiente, etc.).

## Cuando yo apruebe

Te diré explícitamente "OK, escribe". Entonces:

1. Escribe `unidades/UX/UX-nc1-inventario.json`.
2. Ejecuta `python3 scripts/validar_inventario.py X` y reporta el resultado.
   **Expectativa esperada:** 0 errores y 0 avisos sobre este inventario nuevo (puede haber auditoría legacy si quedan canónicos en `vocabulario_consolidado` no presentes en `campos-semanticos-canonicos.json`; se evalúa caso por caso).
3. **(Opcional, contexto-dependiente)** Si quieres chequear coherencia cross-JSON de este inventario respecto a los registries y `nc1-curso.json`, ejecuta `python3 scripts/verificar_integridad.py`.
   **Expectativa esperada DURANTE LA MIGRACIÓN (estado actual):** la suite global recorre TODOS los inventarios del repo, así que reportará errores masivos de las unidades U0-U9 que aún están en shape v10.114 pre-rediseño (faltan 4 bloques consolidados, faltan 4 listas tipadas, etc.). Eso es ruido esperado, NO es bug. Lo único relevante de esta corrida son los errores/avisos que aparezcan etiquetados con la ruta de la unidad nueva que acabas de escribir. Filtra mentalmente o usa `grep` para aislarlos. La suite global solo dará un resultado limpio agregado cuando U0-U9 estén migradas al shape v10.117 (lote operativo posterior).
4. Confirma que el chequeo intra-unidad del validador (paso 2) termina limpio para esta unidad nueva.

Si validador reporta errores tras escribir, paramos, los analizamos y decidimos si arreglamos o si los aceptamos como deuda explícita.

## Empieza ahora

Lee primero `prompt.md`, sigue su flujo, y empieza la extracción de **U[X]** (sustituye [X] por el número). Cuando tengas el JSON listo, presentámelo en chat sin escribirlo. Espera mi feedback antes de cualquier cambio en el filesystem.