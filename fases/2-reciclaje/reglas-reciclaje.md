# Reglas operativas — Fase 2 Reciclaje

> **Qué es:** autoridad **decisional** de fase 2 — cómo decidir y poblar `nc1-reciclaje.json`. Complementa a `schema-reciclaje.md` (el *shape*): este archivo dice *cómo decidir*, no qué forma tiene el dato.
>
> **Qué NO es:** no define el shape (eso es `schema-reciclaje.md`), no es bitácora de diseño (el rediseño se discute en `REDISEÑO-EN-CURSO.md` mientras siga abierto; al cerrarse se archivará), no contiene lógica de implementación de scripts (eso es Nivel 3).
>
> **Precedencia en conflicto:** `schema-reciclaje.md` > `reglas-reciclaje.md`.
>
> **Origen:** destila el modelo cerrado en `REDISEÑO-EN-CURSO.md` §1-§10. Las referencias `§N` a ese documento se mantienen mientras el rediseño esté vivo.

---

## §1. Granularidad del hilo — un hilo por contenido

Un hilo = el recorrido de un contenido a lo largo del curso. La unidad de análisis depende del bloque:

| Bloque | Granularidad del hilo |
|---|---|
| `vocabulario` | campo semántico |
| `gramatica` | categoría gramatical |
| `pronunciacion_ortografia` | categoría pron/orto |
| `verbal` | lema |
| `perifrasis` | perífrasis |

No se agrupan unidades de análisis distintas en un mismo hilo. El bloque `gramatica` se sub-organiza con el campo `_grupo` (subsistema gramatical) — es organización interna, no cambia la granularidad.

## §2. Naming canónico

El `titulo` del hilo es **literal** del registry de su dimensión. Universo cerrado de **5 registries**, físicamente **4 + 1** por propiedad de fase:

- 4 de fase 1: `fases/1-extraccion-inventario/{campos-semanticos,gramatica,pronunciacion-ortografia,verbos}-canonicos.json`.
- 1 derivado, propio de fase 2: `fases/2-reciclaje/perifrasis-canonicas.json`.

Fase 2 **no inventa** títulos. Si un contenido no tiene canónico, **no se rechaza ni se inventa**: se escala como propuesta (§11).

El `id` del hilo es un slug estable `<bloque>-<slug>` (clave primaria); no se recalcula si el `titulo` se corrige.

## §2-bis. Canonización de categorías gramaticales nuevas

Procedimiento **reproducible** para dar de alta una categoría canónica nueva en el registry gramatical cuando se detecta contenido que el canon vigente no cubre. Las categorías resultantes son específicas del curso; el procedimiento es **transversal**: con otro libro o nivel se re-ejecuta, no se improvisa.

**1. Fuentes admitidas.** Una candidata se releva de **dos fuentes, ambas necesarias**:
- **Plan curricular del nivel aplicable para gramática** — respaldo curricular.
- **Corpus del curso** — inventarios, cuadros gramaticales, `rasgo_por_tiempo` y bloques consolidados. Evidencia material.

No se admite ninguna otra base de alta.

**2. Separación en dos carriles.** El contenido verbal se releva en dos planos que **no se mezclan**:
- **Flexión / paradigmas** — el sistema de conjugación como contenido enseñado.
- **Usos de tiempos y modos** — para qué sirve cada tiempo o modo.

Una misma evidencia puede generar candidatos en ambos carriles; se tratan por separado.

**3. Criterio de alta con umbral de evidencia.** Una candidata se canoniza solo si:
- Tiene **evidencia material** en el corpus; no basta el respaldo curricular.
- Se canoniza **separada por paradigma o uso real**, no en un saco único.
- El **nombre canónico** se ancla, cuando exista, en la formulación del plan curricular.
- Si la evidencia es **débil o demasiado lema-específica**, no se canoniza; se deja como hallazgo.

**4. Cierre humano.** La Capa 2 IA **propone** las altas con su evidencia; el **autor decide**. Ninguna alta entra en automático. Al aprobarse, se escribe en el registry con `_grupo`, `_pcic_ref` y `_apariciones`, y se sincronizan, **si procede**, los conteos y referencias documentales.

## §3. Etiquetas del evento

Cada evento lleva una **lista** `etiquetas[]` (coexisten, no es valor único). Las siete:

| Etiqueta | Cuándo |
|---|---|
| `introduce` | Primera aparición canónica del contenido en el curso. |
| `amplia` | Añade ítems/formas/usos a un contenido ya introducido. |
| `aplica` | Reutiliza el contenido sin presentarlo como objeto de estudio. |
| `sistematiza` | Recoge y organiza explícitamente lo ya activo (cuadro, regla, paradigma). |
| `contrasta` | Pone en oposición con otro contenido. |
| `anticipacion` | Aparece como input incidental antes de ser canónico en una unidad posterior. |
| `discrimina` | **Solo `pronunciacion_ortografia`**: discriminación auditiva/ortográfica de formas opuestas. |

**Detección por momento de análisis** (§2.1 del rediseño): `introduce` y `anticipacion` exigen el análisis cross-adelante; `amplia`/`aplica`/`sistematiza`/`contrasta` exigen el cross-atrás. La etiqueta no se asigna solo con el análisis intra-unidad.

La clasificación `principal`/`recurrente` del inventario de fase 1 **no dicta** la etiqueta — la decide la Capa 2 IA leyendo el contexto. Prior: la mayoría de `recurrente` reciben etiquetas de repetición, pero `introduce` sobre un `recurrente` es legítimo.

## §4. `procedencia_indice` — triage respecto al índice

Cada evento lleva `procedencia_indice`, eje **ortogonal** a `etiquetas`. Tres salidas:

| Valor | Criterio |
|---|---|
| `declarado` | El contenido coincide con una entrada del índice del curso para esa unidad. Precomputable mecánicamente. |
| `reconciliado` | No está literal en el índice, pero es el mismo contenido que una entrada del índice con otro nombre. Se anota `reconciliado_con`. |
| `nuevo` | Aparece en el libro pero no está en el índice ni es reconciliable. |

Se marca **por evento** (un contenido puede ser `nuevo` en una unidad y `declarado` en otra). `reconciliado` y `nuevo` son propuestas (§11); lo no declarado no se vuelca a `nuevo` por defecto — se analiza para distinguir reconciliable de nuevo.

## §5. Anticipación

Una forma/contenido cuyo lema o categoría es canónico de una unidad **posterior** y aparece antes como input incidental. Fase 1 no la registra en el consolidado; la anota con poco detalle en marcas transitorias (`_migracion_rediseno`).

**Modelo híbrido:** fase 2 **lee** ese registro transitorio **y completa** el análisis re-mirando las actividades de la unidad. Genera el evento con etiqueta `anticipacion`. La perífrasis anticipatoria se recupera por la misma vía (no depende de `estructura_perifrastica`).

## §6. Formas verbales

El hilo verbal es por lema; el evento es por **lema-tiempo-unidad** y lleva el campo `formas` (formas conjugadas concretas que esa unidad trabaja). La **progresión del paradigma** se lee comparando los `formas` de eventos sucesivos. El atributo `rasgo_por_tiempo` del inventario (regular/irregular) se mantiene en el hilo verbal; no migra al grupo gramatical "Tiempos y modos verbales".

## §7. Explicación

Cuando el libro expone una explicación/cuadro de un contenido, el evento de esa unidad lleva el objeto `explicacion`, con dos partes:

- `que_dice_el_libro` — lo que el cuadro expone literalmente. Válido tenerlo; no es el trabajo.
- `analisis_ia` — el trabajo de fase 2: relaciones lógicas, prerrequisitos, coherencia, incoherencias.

Aplica a los 5 bloques. La explicación es **atributo del evento**, nunca un hilo aparte.

## §8. Componentes "siempre presentes no indexados"

Componentes que aparecen sistemáticamente en el corpus pero no se enseñan como contenido del índice (conjunciones `y/o`, adverbios `sí/no`…). Son un patrón cross-unidad: un contenido que el triage marca `nuevo` de forma sistemática. Los detecta la Capa 2 IA en los hitos cross-unidad y genera propuesta al autor con tres salidas: canonizar / modelar como bloque analítico / ignorar.

## §9. Marcas internas de fase 1

| Marca | Tratamiento en fase 2 |
|---|---|
| `_pendiente_canon` | No bloquea fase 2; se procesa el inventario y se trata como hallazgo pendiente. |
| `_funcion_ambigua` | Se analiza y se lleva a chat con el autor; no se resuelve en automático. |
| `_decisiones_ia` | Se lee como contexto, se cuestiona si entra en conflicto con el análisis cross-unidad, se proponen ajustes. No se acepta a ciegas. |

## §10. Sufijo `@R`

Las referencias con sufijo `@R` (contenido que solo aparece en respuestas de actividades productivas) **no reciben tratamiento diferencial**: el evento se registra igual. Al copiar la referencia al evento, se **preserva el sufijo** como metadato de trazabilidad. Sin etiqueta especial, sin filtrado.

## §11. Cuándo escalar como propuesta

Fase 2 **no decide sola** lo no obvio: genera una propuesta para `propuestas[]` (cola con `estado`), la IA propone y el humano cierra. Se escala como propuesta:

- Una reconciliación de `procedencia_indice` (§4).
- Una categoría/contenido `nuevo` no declarado (§4) — ¿canonizar o dejar como hallazgo?
- Un componente "siempre presente" detectado (§8).
- Una estructura que no encaja en ningún registry (universo cerrado para escritura, abierto para detección).

El análisis IA ya consolidado (`explicacion.analisis_ia`, razonamiento del `detalle`) **no** va a `propuestas[]` — va inline en el hilo/evento. `propuestas[]` es solo lo pendiente de cierre humano.

## §12. Ciclo de vida de `nc1-reciclaje.json` (contrato de regeneración — P1)

Ratifica y formaliza la decisión P1 (opción A, heredada del rediseño viejo, 2026-05-10).

1. **Archivo único canónico.** El reciclaje enriquecido vive en un único archivo: `unidades/nc1-reciclaje.json`. No hay copias ni derivados paralelos.

2. **No se edita a mano.** Los hilos y eventos de nivel `mapa`/`auto` **no se editan manualmente**: se **regeneran** desde los inputs fuente (`nc1-curso.json`, inventarios `UX-nc1-inventario.json`) vía el pipeline de fase 2. Para cambiar un hilo `mapa`/`auto`, se edita la fuente y se regenera. **Excepción:** las entradas de `propuestas[]` y la persistencia del cierre humano sí se escriben — esa es su función.

3. **Disparadores de regeneración** (alineados con los hitos cross-unidad, `REDISEÑO-EN-CURSO.md` §1.4):
   - **Incremental** — al integrar cada unidad: ciclo de reciclaje de esa unidad (Capa 1 + Capa 2 sobre la unidad recién integrada).
   - **Revisión cross-unidad ampliada** — tras 3 unidades acumuladas: la Capa 2 revisa el bloque de unidades. Es revisión, **no** regeneración íntegra.
   - **Regeneración íntegra** — solo al **cierre de bloque** (todas las unidades del curso): regeneración completa de `nc1-reciclaje.json`.

4. **Determinista vs cierre humano.** La **Capa 1** regenera el esqueleto mecánico — reproducible. La **Capa 2 IA** enriquece y produce `propuestas[]`; cada propuesta se cierra con el humano y su resolución se persiste con `estado` (§6 del schema). La parte determinista se puede rehacer sin pérdida; la parte humana vive en `propuestas[]`.

5. **"Reciclaje cerrado para una unidad"** = su reciclaje incremental está generado **y** ha pasado el criterio de cierre vigente de fase 2 (§13) **y** sus `propuestas[]` están resueltas o explícitamente diferidas. Mientras fase 2 esté **PAUSADA** operativamente, **ninguna unidad** tiene su reciclaje cerrado: la pausa significa que el pipeline no corre; "cerrado" aplica por unidad solo tras la reactivación.

## §13. Validación y criterio de cierre

La validación del reciclaje de una unidad tiene **tres partes**:

- **(a) Chequeo estructural** — conformidad de `nc1-reciclaje.json` con `schema-reciclaje.md` (claves, tipos, enumeraciones). Automatizable; debe dar **0 errores**.
- **(b) Validador cross-unidad R1-R5** — control de calidad cruzado entre unidades: R1 anticipación de léxico, R2 detección de inventos, R3 errores de clasificación semántica, R4 inconsistencias de progresión, R5 coherencia bidireccional de trazabilidad. No debe dejar **alertas sin resolver**.
- **(c) Revisión editorial del autor** — el autor revisa el reciclaje de la unidad en el dashboard.

**Criterio de cierre por unidad** — el reciclaje de una unidad se considera **cerrado** solo si se cumplen **todas** estas condiciones:

1. El reciclaje incremental está **generado** (Capa 1 + Capa 2 ejecutadas sobre la unidad).
2. Pasa el **chequeo estructural** (a) — 0 errores contra `schema-reciclaje.md`.
3. El **validador cross-unidad R1-R5** (b) no deja alertas sin resolver.
4. Las `propuestas[]` que afectan a esa unidad están **resueltas o explícitamente diferidas**.
5. La **revisión editorial del autor** (c) está hecha.

**Comandos:** el chequeo estructural (a) y el validador cross-unidad (b) son scripts de **Nivel 3** (pendientes de implementar; ver `REDISEÑO-EN-CURSO.md` §5). Este §13 fija **qué deben comprobar**; el cómo (nombre de comando, salida) se cierra al implementarlos. Mientras fase 2 esté **PAUSADA**, el gate no se ejecuta — ninguna unidad puede cerrarse (§12.5).