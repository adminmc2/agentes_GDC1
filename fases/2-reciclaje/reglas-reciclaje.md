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

La clasificación `principal`/`recurrente` del inventario de fase 1 **no dicta** la etiqueta — la decide la Capa 2 leyendo el contexto. Prior: la mayoría de `recurrente` reciben etiquetas de repetición, pero `introduce` sobre un `recurrente` es legítimo (caso de un hilo que aparece primero como `recurrente` y nunca llega a ser `principal`).

### §3.1. Matriz de decisión (cierre operativo del Nivel 5, v12.21)

La asignación de etiquetas de las cinco categorías **deterministas** (`introduce`, `amplia`, `aplica`, `sistematiza`, `anticipacion`) se resuelve mecánicamente con seis predicados sobre el canónico y la proyección canónica de fase 1. `contrasta` y `discrimina` quedan fuera del cierre determinista — ver §3-bis.

**Inputs (6 predicados binarios).**

| Sigla | Predicado | Fuente de verdad |
|---|---|---|
| **A** | Es la primera aparición efectiva del hilo en el recorrido del curso. | `min(unidad)` entre eventos del hilo en `nc1-reciclaje.json`. |
| **B** | La unidad actual es **unidad canónica** del hilo. | Proyección canónica de fase 1, por bloque: vocab → `vocabulario_consolidado.{principal,recurrente}` del inventario, alias resueltos por `campos-semanticos-canonicos.json`. Gram → `gramatica_consolidada.{principal,recurrente}`, alias por `gramatica-canonica.json`. Pron/orto → `pronunciacion_ortografia_consolidada.{principal,recurrente}`, alias por `pronunciacion-ortografia-canonica.json`. Verbal → `tiempos_y_verbos_consolidado[].lema`, universo cerrado por `verbos-canonicos.json`. Perífrasis → registry decisor `fases/2-reciclaje/perifrasis-canonicas.json`; `tiempos_y_verbos_consolidado[].estructura_perifrastica` del inventario solo aporta **evidencia material** de presencia/apoyo de detección — no decide B/C, y por la naturaleza híbrida de la anticipación perifrástica (§5) tampoco se considera input fiable para D_any (que se mide siempre sobre `nc1-reciclaje.json`). **No** literalidad de `nc1-curso.json`. |
| **C** | Existe **unidad canónica posterior** del hilo. | Misma fuente que B, cross-adelante. |
| **D_any** | Existe evento previo del hilo en unidades anteriores. | `nc1-reciclaje.json` cross-atrás. |
| **D_ant** | Existe evento previo del hilo etiquetado `anticipacion`. | `nc1-reciclaje.json` cross-atrás filtrado por etiqueta. |
| **E** | La unidad expone un cuadro/regla del hilo. | `cuadros[]` del inventario `UX-nc1-inventario.json` referido al hilo. |

**Capa 1 — función principal del evento** (asigna una etiqueta de las cinco deterministas):

| Patrón | A | B | C | D_any | D_ant | E | Función principal |
|---|---|---|---|---|---|---|---|
| Anticipación: primera aparición efectiva, no canónica | sí | no | sí | no | — | — | `anticipacion` |
| Anticipación recurrente (no es la primera aparición, sigue antes de su canónica) | no | no | sí | sí | — | — | `anticipacion` |
| Primera aparición canónica pura | sí | sí | — | no | no | — | `introduce` |
| Primera aparición sobre recurrente, sin canónica posterior | sí | no | no | no | no | — | `introduce` |
| Sistematización canónica tras anticipación previa | no | sí | — | sí | sí | sí | `sistematiza` |
| Sistematización post-introducción | no | sí | — | sí | no | sí (holístico) | `sistematiza` |
| Ampliación: añade ítems/formas/usos | no | sí | — | sí | no | (no holístico) | `amplia` |
| Aplicación post-introducción | no | — | — | sí | no | no | `aplica` |

`sistematiza` exige siempre **E=sí**: sin cuadro/regla del libro no hay sistematización.

**Capa 2 — coexistencias permitidas** (admitidas por `REDISEÑO-EN-CURSO.md` §2.3). Se añaden sobre la función principal de Capa 1:

| Coexistencia | Condición | Caso |
|---|---|---|
| `introduce + sistematiza` | función principal = `introduce` **y** E=sí (cuadro holístico simultáneo a la primera aparición canónica). | `verb · ser` U1 (cuadros@p14#1, p15, p20#1, p20#3). |
| `amplia + sistematiza` | función principal = `amplia` **y** E=sí + el cuadro presenta paradigma completo añadiendo formas. | Hipotético — admitido por contrato. |
| `aplica + anticipacion` | función principal = `aplica` **y** C=sí (reutiliza contenido previo y anticipa material de unidad posterior). | Hipotético — admitido por contrato. |

**Excepción residual conservada** (único resto de juicio editorial). Cuando A=no + B=sí + D_any=sí + D_ant=no + E=sí, la matriz tiene dos filas posibles (`sistematiza` post-introducción y `amplia + sistematiza`). La distinción es editorial: si el cuadro presenta paradigma holístico recogiendo lo ya activo → `sistematiza`; si añade ítems/formas específicas al inventario previo → `amplia` o `amplia + sistematiza` según haya o no presentación holística. Se declara aquí como excepción explícita; **no** se esconde dentro de la tabla.

**Hilos sin canónico.** Cuando un contenido no tiene canónico resuelto (caso `voc · Gentilicios` U1 en limbo editorial hasta cerrar la propuesta de alias): `etiquetas: []`, fuera de matriz. La etiqueta se asigna cuando la propuesta de reconciliación/canonización se cierra.

### §3-bis. Etiquetas no cerradas en cierre determinista (provisional, v12.21)

Las etiquetas `contrasta` y `discrimina` se mantienen en el enum del schema pero **su asignación queda como decisión editorial supervisada**, no determinista. Razón: el inventario de fase 1 no codifica hoy un campo estructurado de "foco contrastivo" en los cuadros — los contrastes viven en texto libre/notas (`schema-inventario.md` actual). El predicado análogo a F del rediseño exploratorio no es input determinista todavía.

El cierre determinista se reabrirá cuando se cumpla **una** de estas condiciones:

- (a) el inventario de fase 1 incorpora un campo estructurado de foco contrastivo en `cuadros[]`;
- (b) se acumula corpus suficiente (≥5 casos atestados en el canónico) para inducir una regla determinista por inducción empírica.

Mientras tanto: `contrasta` y `discrimina` se asignan caso a caso con criterio del autor y se anotan como hallazgo, no como propuesta cerrada. El reparto observado en U0-U3 es 0/0; el primer caso atestado abrirá registro.

## §4. `procedencia_indice` — triage respecto al índice y al PCIC (eje identitario mecanizado, v11.76)

Eje **identitario puro**, ortogonal a `etiquetas`. Responde a "¿el título canónico del hilo está respaldado por el índice del curso o por los registries (incluido PCIC)?". La temporalidad la lleva la etiqueta, no este eje.

| Valor | Criterio | Quién lo escribe |
|---|---|---|
| `declarado` | El título canónico coincide **literalmente** con una entrada del índice del curso, **en cualquier unidad** (slug curso-wide; absorbe paréntesis del índice). | **Capa 1**, mecánico. |
| `reconciliado` con prefijo `indice:` | El canónico es alias de una entrada del índice del curso (resuelto vía `aliases_indice` del registry de campos). `reconciliado_con: "indice:<entrada del curso>"`. | **Capa 1**, mecánico (v11.76). |
| `reconciliado` con prefijo `pcic:` | El canónico tiene respaldo PCIC pero no entrada en el curso (`origen=pcic_a1` en vocab; `_pcic_ref` en gramática/pron/perif). `reconciliado_con: "pcic:<ref>"` o `"pcic:A1"` como fallback. | **Capa 1**, mecánico (v11.76). |
| `nuevo` | No está en el índice ni vía aliases ni vía respaldo PCIC. Solo en `origen=excepcion` sin aliases. Caso residual. | **Capa 1**, mecánico. |
| **sin asignar** | **Solo bloque `verbal`**: `verbos-canonicos.json` no expone respaldo estructurado equivalente a `_pcic_ref`. La Capa 1 deja la procedencia vacía. | **Capa 2 decide** (excepción al modelo mecánico, v11.76). |

El valor es **estable por hilo** (depende del título canónico contra el índice y los registries globales, no de la unidad). Se persiste por evento por compatibilidad de schema. La cronología la marca la etiqueta: `anticipacion` (antes), sin etiqueta temporal (en su unidad canónica), `aplica` (después).

**Cambio de modelo v11.76**: en v11.75 todos los `reconciliado`/`nuevo` eran propuestas de Capa 2 (cautela anti-alias). Comprobado que el registry ya curado de fase 1 trae el respaldo estructurado necesario para 4 bloques, la Capa 1 mecaniza el triage íntegro salvo verbal.

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

5. **"Reciclaje cerrado para una unidad"** = su reciclaje incremental está generado **y** ha pasado el criterio de cierre vigente de fase 2 (§13) **y** sus `propuestas[]` están resueltas o explícitamente diferidas. Fase 2 está **reactivada** (v11.69): el pipeline corre y una unidad puede cerrar su reciclaje. A fecha de la reactivación ninguna unidad ha pasado aún por la Capa 2, así que ninguna tiene todavía el reciclaje cerrado.

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

**Comandos** (implementados en el Nivel 4 — fase 2 reactivada en v11.69):

- (a) Chequeo estructural → `python3 scripts/validar_reciclaje.py` — 0 errores contra `schema-reciclaje.md`.
- (b) Validador cross-unidad R1-R5 → `python3 scripts/validar_cross_unidad.py` — sin alertas R1/R3/R4 sin resolver; R2/R5 son pre-condiciones que abortan.

La revisión editorial del autor (c) no es automatizable.

## §14. Validador cross-unidad — R1-R5

Detalle del componente (b) del gate de cierre (§13). Cinco reglas de **validación cruzada entre unidades** que se ejecutan sobre los inventarios de fase 1 antes de dar por cerrado el reciclaje. Diseño heredado, cerrado en 2026-05-12.

**R1 — Anticipación de léxico.** Detecta léxico frecuente en U(n) que **no** está en el `principal` ni `recurrente` de esa unidad pero **es canónico en una unidad posterior** → alerta de anticipación. Algoritmo: leer el índice del curso + el `principal`/`recurrente` de cada inventario + re-ejecutar frecuencias; para cada término frecuente no declarado en U(n), si es canónico en U(n+k) → alerta. Alimenta sobre todo la etiqueta `anticipacion` (§3). `procedencia_indice` (§4) **no** cambia por R1 — el eje identitario es estable por hilo y curso-wide; si el contenido está en el índice del curso es `declarado` independientemente de en qué unidad aparezca el evento (v11.75). Output: `{unidad, término, unidad_canónica, frecuencia, ejemplos}`.

**R2 — Materialidad y trazabilidad del contenido extraído.** Todo contenido consolidado debe estar sustentado por **evidencias reales** de actividad o cuadro en la unidad. En vocabulario, los ítems deben aparecer **literalmente**; en verbal, las formas o el lema deben estar **atestiguados** según el contrato de fase 1; en gramática y pron/orto, la categoría debe estar **trazada a actividades/cuadros** que la trabajan (la etiqueta canónica no tiene por qué aparecer literal en el libro). Si falla, es bug de extracción de fase 1. Pre-condición.

**R3 — Errores de clasificación por dimensión.** Chequeo contra los registries y el contrato de fase 1 para detectar contenido ubicado en la **dimensión equivocada**. Caso típico: término léxico en un campo semántico incorrecto. Sanity check post-extracción; produce alerta, no aborta.

**R4 — Inconsistencias de progresión.** Detecta: léxico `recurrente` en U(n) que nunca fue `principal` antes; el mismo contenido con dos nombres distintos en unidades distintas (→ candidato a reconciliación, §4); verbos en `vocabulario_consolidado` que deberían vivir en `tiempos_y_verbos_consolidado`. Produce alerta.

**R5 — Coherencia bidireccional de trazabilidad.** `actividad.X` ↔ `fuentes` del bloque consolidado deben coincidir en los dos sentidos. Pre-condición; si falla, fase 2 aborta.

**Qué bloquea:** R2 y R5 son **pre-condiciones** (un fallo es bug de fase 1; fase 2 aborta). R1, R3 y R4 producen **alertas** que entran en el criterio de cierre §13 (no quedan alertas sin resolver). El validador está implementado en `scripts/validar_cross_unidad.py`: R2/R5 se delegan a `verificar_integridad.py` (fase 1); R1 va en versión proxy determinista (anticipación material trazable — ver el docstring del script).

## §15. Relaciones cross-hilo (v11.86)

Las relaciones cross-hilo materializan lecturas editoriales del tipo "este hilo se apoya en aquel", "este contrasta con aquel". Viven en `hilo.relaciones[]` (§7 del schema) una vez cerradas, y nacen como propuestas con `tipo: relacion_cross_hilo` (§6 del schema).

**Cómo se detectan los candidatos.** La señal de partida son los **cuadros compartidos**: un mismo `cuadro@pXX` referenciado por eventos de dos hilos distintos en la misma unidad — un solo cuadro tratando dos contenidos a la vez es indicio fuerte de que la unidad los pone en relación. El helper `scripts/proponer_relaciones_cuadro.py` recorre el canónico y, para cada par de hilos que comparten ≥1 cuadro, crea (o actualiza, si ya existe pendiente) una propuesta con `tipo: relacion_cross_hilo` y `relacion_candidata: {hilos: [a, b] ordenados, cuadros_compartidos: [...]}`. **Solo cuadros**: las actividades compartidas no son señal suficiente (son demasiado polifónicas).

**Identidad no dirigida del candidato.** La propuesta candidata representa un **par no dirigido** de hilos: el payload guarda los dos hilos sin asignar origen ni destino. Tres de los cinco `tipo` (`usa`, `prerrequisito`, `activa`) son **direccionales**; los otros dos (`contrasta`, `comparte`) son **simétricos**. Fijar la dirección antes de tiempo (p. ej. por orden alfabético) sesgaría editorialmente el dato. Por eso la propuesta se mantiene neutral y la dirección se decide **solo al aceptar**: el humano elige `tipo` y, si es direccional, qué hilo del par actúa como origen — esa elección se materializa al escribir la entrada en `hilo.relaciones[]` del hilo de origen. La propuesta candidata **no tiene `hilo_ref`** (schema §6).

**Tipos** — enum cerrado de `tipo`:

| Tipo | Criterio | Ejemplo |
|---|---|---|
| `usa` | El hilo A se sirve de B operativamente sin que B sea un prerrequisito formal. | "Saludos y despedidas" *usa* "Tú/usted" para elegir registro. |
| `prerrequisito` | B debe estar activo (introducido o sistematizado) antes de que A pueda funcionar. | "Concordancia adjetivo-sustantivo" tiene como *prerrequisito* "Género y número del sustantivo". |
| `activa` | A funciona como disparador didáctico que pone en juego B aunque B no sea el foco. | "Presentaciones" *activa* "Verbo llamarse". |
| `contrasta` | A y B se trabajan en oposición explícita (par contrastivo). | "Ser" *contrasta* "Estar". |
| `comparte` | A y B comparten un mismo cuadro/escena editorial sin que la relación sea de uso, prerrequisito, activación o contraste — coocurrencia editorial sin jerarquía. | "Países hispanohablantes" *comparte* cuadro con "Gentilicios". |

Si dudas entre `usa` y `prerrequisito`, pregunta "¿se puede trabajar A sin B?" — si la respuesta es no, es `prerrequisito`; si es "sí pero con menos sentido", es `usa`. `activa` se reserva para cuando A es la actividad/escena y B es el contenido lingüístico que sale a flote.

**Política de extensión del enum.** No se añaden tipos silenciosamente. Para extender: entrada nueva en la tabla de arriba con **criterio + ejemplo del curso**, mención en `schema-reciclaje.md §7` y actualización del validador. Una propuesta de Capa 2 con un `tipo` no listado se considera mal formada.

**Política de cierre de la propuesta.**

- **Aceptada** → el humano elige `tipo` y, si es direccional, qué hilo del par `hilos[]` actúa como **origen** (el otro queda como destino). Se añade entrada a `hilos[origen].relaciones[]` con `{hilo_ref: destino, tipo, detalle, unidad_relevante?}`. La propuesta queda con `estado: aceptada` y `resolucion` registra la dirección elegida (formato sugerido: `"aceptada como '<tipo>' origen=<id_origen> destino=<id_destino>"`; para tipos simétricos basta `"aceptada como '<tipo>' entre <id_a> y <id_b>"`). No se crea relación recíproca automática — si la inversa también es interesante (raro fuera de `contrasta`/`comparte`, donde la entrada en un solo lado suele bastar), se añade una segunda entrada manualmente en el hilo simétrico citando la misma propuesta cerrada.
- **Rechazada** → `estado: rechazada` y `resolucion` con motivo corto (ej. "coocurrencia accidental — no hay vínculo editorial"). No se toca `hilo.relaciones[]`.
- **Diferida** → se mantiene `pendiente`; el helper, en pasadas siguientes, **no duplica** la propuesta (mismo `id` canónico del par ordenado) sino que la actualiza si emergen cuadros compartidos nuevos.

**Idempotencia — un único constructor de id.** Helper y cualquier flujo de cierre manual comparten un único constructor de id del par ordenado: `id_relacion_par(hilo_a, hilo_b)` en `scripts/proponer_relaciones_cuadro.py` ordena alfabéticamente y devuelve `prop-rel-<menor>-<mayor>`. Mismo cálculo para crear, buscar duplicados y cerrar — evita desalineaciones sutiles.

**Frontera con `detalle.enlaces`** (recordatorio de schema §7). `hilo.relaciones[]` resume la lectura editorial cross-hilo (entrada corta, una por relación importante). `detalle.enlaces` es el grafo lingüístico-pedagógico profundo del hilo cuando alcanza `nivel: detalle`. No se sustituyen — un hilo en `auto` puede tener `relaciones` y, al promoverse a `detalle`, sumar `enlaces` sin tocar las primeras.