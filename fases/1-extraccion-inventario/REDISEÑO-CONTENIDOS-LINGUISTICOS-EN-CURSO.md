# Propuesta arquitectónica — contenidos lingüísticos en fase 1 y rol activo de fase 2

> **Estado:** EN CONSTRUCCIÓN. Documento de trabajo local (no trackeado). Se elimina cuando la propuesta se cierre y las decisiones vivan en los documentos canónicos de fase 1 y fase 2.
>
> **Progreso de cierre por cuestión:**
> - ✅ **Cuestión 1 — Arquitectura de contenidos lingüísticos de fase 1: VALIDADA POR REVISOR 2026-05-11.** Cerrada a nivel arquitectónico. Partes A–J coherentes internamente. Detalle del cierre en §13.
> - 🔄 **Pieza 3 — Registry gramatical: REABIERTA 2026-05-12.** El cierre del 2026-05-11 con 15 categorías quedó superado. La nueva estrategia (§14.0) usa PCIC A1 como fuente vinculante (`fases/1-extraccion-inventario/pcic-a1-gramatica.json`); pieza 3 queda como scaffold conceptual. La lista anterior se conserva como registro histórico.
> - ✅ **Pieza 2 — Lista exacta del registry verbal: cerrada 2026-05-11 (diseño + materialización).** Shape + enums + política de ingreso + límite fase 1/fase 2 + matriz de cobertura de 48 lemas extraídos. Archivo materializado: `fases/1-extraccion-inventario/verbos-canonicos.json`. Detalle en §15.
> - ✅ **Pieza 4 — Lista exacta del registry de pronunciación/ortografía: cerrada 2026-05-11.** Matriz de cobertura cruzada contra las 9 entradas de `pronunciacion_ortografia[]` de `nc1-curso.json` + entrada de mayúsculas reasignada de pieza 3 + lista final de 7 categorías. Detalle en §16.
> - ✅ **Todas las piezas arquitectónicas cerradas.** Siguiente paso: spike E1.5 sobre una unidad real para validar implementabilidad antes de propagación E2.
>
> **Audiencia:** revisor + autor. Tras la pasada C de claridad de fase 1 (v10.110), el autor identifica una limitación profunda del schema y propone un cambio arquitectónico mayor. El documento integra el diccionario terminológico, la propuesta del autor, los matices del revisor y las decisiones tomadas. Antes de implementar, dictamen.

---

## Cómo leer este documento

El documento está dividido en **10 partes ordenadas para análisis secuencial**. Cada parte cierra una decisión o conjunto de decisiones. El revisor y el autor pueden abordarlo en este orden:

| Parte | Propósito | Qué se decide |
|---|---|---|
| **A** — Marco compartido (§0-§1) | Fijar vocabulario común y diagnóstico empírico | Punto de partida |
| **B** — Principio arquitectónico (§2) | Aprobar o rechazar la dirección general y el cambio de naturaleza de fase 1 | Principio |
| **C** — Modelo de datos (§3-§4) | Cerrar el shape: actividad, bloques consolidados, nomenclatura, trazabilidad | Shape |
| **D** — Sistema canónico (§5) | Decidir la forma del canon ampliado (registries paralelos vs alternativas) | Canon |
| **E** — Fase 2 redefinida (§6) | Cerrar las tres capas: validación cruzada, proyección, relaciones | Pipeline de fase 2 |
| **F** — Reglas de coherencia (§7) | Fijar invariantes intra-unidad y cross-unidad | Validación |
| **G** — Decisiones consolidadas (§8) | Verificar que la tabla de las 9 piezas refleja el estado real | Cierre formal |
| **H** — Impacto operativo (§9) | Aprobar el plan de 5 etapas (E1, E1.5, E2, E3, E4a, E4b) | Roadmap |
| **I** — Estado del repo (§10) | Referencia de partida (no se decide nada) | Contexto |
| **J** — Renegociaciones con el repo vigente (§11) | Reconocer los 4 conflictos y planificar su renegociación explícita | Trazabilidad |

Cierre del documento: **§12 — Preguntas residuales al revisor**.

Cada parte termina con una caja **"Decisión a tomar / Estado actual"** para que el lector vea de un vistazo qué hay que aprobar y qué ya está acordado.

---

# Parte A — Marco compartido

> **Propósito de esta parte:** fijar el vocabulario común antes de discutir nada arquitectónico, y diagnosticar empíricamente por qué se replantea el modelo. Sin esto, las discusiones siguientes pueden generar malentendidos terminológicos.

---

## §0 — Diccionario terminológico del sistema

Antes de discutir arquitectura conviene fijar el vocabulario propio del sistema NC1. Hay términos que se solapan peligrosamente.

### A. Conceptos del libro publicado

**`seccion`** — apartado editorial físico de cada unidad. Enumeración cerrada de 7: `vocabulario`, `gramatica`, `comunicacion`, `destrezas`, `cultura`, `evaluacion`, `reflexion`.

⚠ La sección "vocabulario" del libro no significa que solo se trabaje vocabulario allí. Es apartado físico, no clasificación de contenido.

### B. Atributos de cada actividad (ejes ortogonales)

**`tipo`** — mecánica del enunciado. Enumeración cerrada de 20 (`completa_huecos`, `relaciona`, `escucha_y_repite`, etc.).

**`destreza`** — habilidad lingüística MCER que ejercita el alumno. Lista del enum de 6 vigente en `schema-inventario.md:185-191`: `comprension_auditiva`, `comprension_lectora`, `expresion_escrita`, `expresion_oral`, `interaccion_oral`, `mediacion`.

⚠ Las destrezas son habilidades del Marco Común Europeo. **NO existen** "destreza gramatica", "destreza vocabulario", "destreza pronunciacion_ortografia" — eso no son destrezas MCER, son contenidos.

**`enfoque`** — campo informativo del foco predominante de la actividad cuando la `destreza` MCER no basta para describirla. Enumeración cerrada de 6: `vocabulario`, `gramatica`, `comunicacion`, `cultura`, `pronunciacion_ortografia`, `transversal`.

> **Decisión revisada (2026-05-12):** valor `fonetica` renombrado a `pronunciacion_ortografia` para alinear con el bloque top-level `pronunciacion_ortografia_consolidada`. Ver `schema-inventario.md` §5c y Apéndice §A.3.

⚠ **Decisión del autor (esta propuesta):** `enfoque` queda como **informativo, no clasificatorio**. No se usa para decidir qué vocabulario, gramática, verbos o pronunciación trabaja la actividad. Esa información se extrae objetivamente del contenido real, independiente del `enfoque` declarado.

### C. Contenido lingüístico real de la actividad

**Lo que la actividad realmente contiene a nivel lingüístico**, independiente del `enfoque` declarado. Cuatro categorías ortogonales: vocabulario, tiempos y verbos, gramática, pronunciación y ortografía.

⚠ **Punto crítico aclarado:** una actividad con `enfoque=gramatica` puede contener vocabulario léxico real en sus frases ejemplo. Una actividad con `enfoque=vocabulario` puede tener gramática implícita. **El contenido lingüístico real es objetivo y se extrae del texto, no del `enfoque` declarado.**

### D. Catálogos consolidados de la unidad (top-level)

**Bloques top-level del inventario** que agregan, por unidad, todo el contenido lingüístico que la unidad enseña. Cuatro bloques paralelos:

- `vocabulario_consolidado`
- `tiempos_y_verbos_consolidado` (estructura plana por entrada verbal: ver §E)
- `gramatica_consolidada`
- `pronunciacion_ortografia_consolidada`

⚠ **En esta propuesta los bloques son DERIVADOS automáticamente** del agregado del contenido lingüístico de las actividades. No se mantienen a mano.

#### `vocabulario_consolidado` — qué es y cómo se nombra cada entrada

Bloque del inventario, **vive a nivel raíz del JSON (top-level)**, que cataloga todo el léxico que la unidad enseña. Su estructura interna tiene **dos sub-bloques** (decisión 2026-05-12: `comprension` eliminado del modelo):

| Sub-bloque | Criterio de pertenencia | Cómo se determina |
|---|---|---|
| `principal` | **Vocabulario declarado en el índice editorial de la unidad** (`nc1-curso.json`, campo `vocabulario[]`). Es el contenido léxico nuevo nuclear que la unidad enseña explícitamente. | Comparación directa con el índice. |
| `recurrente` | **Léxico identificado por frecuencia de aparición** en las actividades de la unidad, **no declarado en el `vocabulario[]` del índice de la propia unidad**, **y que tampoco es canónico en una unidad posterior**. Puede incluir léxico aprendido en unidades anteriores que vuelve a circular, o léxico que aparece varias veces sin ser contenido oficial de ninguna unidad. | Requiere **análisis profundo del contenido de todas las actividades** + **lectura del índice editorial completo de `nc1-curso.json`** para aplicar el filtro de anticipación (ver §7 regla 7). Si un término frecuente es canónico en una unidad posterior U(n+k), **no se codifica como `recurrente`** — fase 2 lo detecta como anticipación. |

⚠ **`comprension` eliminado (2026-05-12).** El sub-bloque que cubría "léxico nuevo necesario para entender el input" se retira del modelo. El léxico que antes encajaba ahí debe reclasificarse: si es canónico en una unidad posterior, es anticipación (fuera); si es frecuente y no es canónico en ninguna unidad, entra en `recurrente`; el resto desaparece silenciosamente del inventario consolidado (sigue presente en el texto de las actividades a través de `datos.items_libro` u otros campos verbatim, pero no se cataloga). Razón: el criterio de pertenencia de `comprension` era subjetivo ("desconoce el significado y es relevante para la comprensión") y se solapaba en la práctica con `recurrente`.

> **Shape obsoleto retirado (2026-05-13).** Las descripciones y ejemplos de shape de `vocabulario_consolidado` que vivían aquí ya no son vigentes. **Shape canónico actual → `schema-inventario.md` §9.1** y glosario "Bloques consolidados" / `vocabulario_consolidado`.

**Jerarquía estricta de naming de cada clave de categoría:**

1. **Primero, el nombre tal cual aparece en el índice editorial del libro** (`unidades/nc1-curso.json`, campos `vocabulario[]` y `contenido_general[]`). Si la unidad declara "Parientes" en su índice, la clave es `"Parientes"`.
2. **Si no aparece en el índice del libro**, el nombre se toma del **plan curricular PCIC A1** del Instituto Cervantes. Si el contenido encaja en la subcategoría PCIC "Relaciones familiares", la clave es esa.
3. **Si no aparece en ninguno de los dos**, es un caso de excepción: lo decide el autor con nota justificativa.

Esta jerarquía aplica también a las claves de los otros tres bloques consolidados (`gramatica_consolidada`, `pronunciacion_ortografia_consolidada`, `tiempos_y_verbos_consolidado` con sus campos como `rasgo_verbal`).

⚠ La jerarquía garantiza que el sistema **no inventa nombres**: siempre tiene una fuente canónica de procedencia para cada nombre de categoría.

### E. Estructura del contenido verbal en el inventario (revisada tras dictamen del revisor)

**Decisión cerrada:** la jerarquía profunda de v10.95 (tiempo → uso → tipo_verbo → verbo) **NO se usa como shape del inventario unitario**. Esa jerarquía es lógica de proyección cross-unidad que vive en **fase 2** (al construir hilos), no estructura nativa del inventario.

> **Shape obsoleto retirado (2026-05-13).** El ejemplo concreto del shape de `tiempos_y_verbos_consolidado` que vivía aquí ya no es vigente (incluía `procedencia`, `secciones`, y `comprension` como valor posible). **Shape canónico actual → `schema-inventario.md` §9.2** y glosario "tiempos_y_verbos_consolidado". El principio de fondo (lista plana, una entrada por lema, propiedades solo cuando aplican) sí sigue siendo válido.

**Los usos del tiempo** (Universo Dele: acciones momentáneas, hábitos, información personal, verdades universales, futuro próximo) son metadata de proyección de fase 2, **no campo del inventario**.

**`formas_trabajadas`** — las conjugaciones concretas del verbo que el libro presenta en esa unidad. Un verbo no siempre se enseña entero: suele introducirse en formas parciales y ampliarse en unidades posteriores. Ejemplo:

| Unidad | Verbo | `formas_trabajadas` |
|---|---|---|
| U1 | ser | `["soy", "eres", "es"]` (singular) |
| U2 | ser | `["somos", "sois", "son"]` (amplía a plural) |
| U3 | ser | `["es", "son"]` (aplica, sin formas nuevas) |

### F. Canon

Universo cerrado de nombres válidos para los contenidos lingüísticos. **Doble fuente con prioridad estricta:**

1. **`nc1-curso.json`** (índice editorial del libro) — canon prioritario.
2. **PCIC A1** del Instituto Cervantes — secundario, solo para contenidos que aparezcan en actividades y no estén en el índice.

⚠ Hoy el canon (`campos-semanticos-canonicos.json`, v10.108) cubre **solo léxico semántico**. Esta propuesta lo amplía a los 4 tipos.

### G. Términos que se solapan (clarificados en esta propuesta)

La palabra **"vocabulario"** significa 4 cosas distintas según el contexto:

| Contexto | Significado |
|---|---|
| `seccion: vocabulario` | Apartado físico del libro |
| `enfoque: vocabulario` | Foco predominante informativo de una actividad |
| `vocabulario` como tipo de contenido lingüístico | Categoría real del contenido (independiente del enfoque) |
| `vocabulario_consolidado` | Bloque top-level que cataloga el léxico de la unidad |

Lo mismo aplica a "gramática" y "pronunciación y ortografía". El diccionario fija el contexto para cada uso.

### H. Términos técnicos del JSON

**`top-level`** — el nivel raíz del archivo JSON, lo que aparece al primer nivel cuando se abre el inventario. No está metido dentro de ningún otro objeto.

En `UX-nc1-inventario.json`, son top-level los campos:

`unidad`, `curso`, `titulo`, `paginas_libro`, `nivel`, `fuente`, `contenidos_indice`, `vocabulario_consolidado` (y los 3 nuevos bloques consolidados de esta propuesta), `secciones`, `autoevaluacion`, `_nota_unidad_atipica`, `paginas_detalle`.

**NO son top-level:** todo lo que está dentro de `paginas_detalle` (páginas, actividades, cuadros con sus campos como `id`, `tipo`, `datos.*`, etc.).

⚠ **Por qué importa la distinción:** los bloques **top-level** consolidados aplican a la unidad entera. Los datos **dentro de actividades** aplican a esa actividad concreta. Esta propuesta define la relación entre ambos niveles (las 4 listas en cada actividad referencian al canon; los bloques top-level se derivan del agregado).

---

## §1 — Contexto: por qué se replantea el modelo

Trabajando con el dashboard y los inventarios actuales, el autor detecta tres problemas vinculados:

**Problema 1 — desincronización entre vista preparada y generación actual del reciclaje.**

El dashboard (`web/index.html:615`, `:657`) tiene reservados color y orden de render para el tipo `tiempos_y_verbos`. La intención del sistema, declarada desde v10.95, era cubrir ese tipo con hilos jerárquicos.

Sin embargo, los **scripts de generación actual de fase 2 no producen ese tipo**:

- `regenerar_reciclaje_mapa.py:29` proyecta desde `nc1-curso.json` hacia los tipos `vocabulario`, `contenido_gramatical` y `estrategia`. No emite `tiempos_y_verbos`.
- `regenerar_reciclaje_vocabulario.py:55` proyecta desde `vocabulario_consolidado` exclusivamente hacia hilos de tipo `vocabulario`.

**Estado del JSON resultante:** 181 hilos repartidos en 115 `vocabulario` + 39 `contenido_gramatical` + 27 `estrategia` + **0 `tiempos_y_verbos`** (`nc1-reciclaje.json`).

**Por qué esto importa para el rediseño (y por qué NO es solo fix del bloque vacío):**

El bloque jerárquico de v10.95 se construía manualmente en chat. Al automatizar la regeneración en v10.97, los scripts no aprendieron a producir ese tipo porque su input (`nc1-curso.json` y `vocabulario_consolidado`) **no contiene la información verbal con la granularidad necesaria** (tiempo, uso, tipo_verbo, formas trabajadas). Esa información no vive en ningún sitio estructurado del sistema actual.

La consecuencia: el rediseño no busca "rellenar el bloque vacío" añadiendo manual una vez más. Busca **dar a fase 1 la estructura necesaria para que la información verbal exista en los inventarios**, y a partir de ahí fase 2 pueda proyectarla con la jerarquía vigente desde v10.95.

Sin el cambio en fase 1, los scripts de fase 2 nunca tendrán datos suficientes para construir hilos `tiempos_y_verbos` desde input automático. El bloque vacío es el síntoma; la raíz es la ausencia de información verbal estructurada en los inventarios.

**Problema 2 — `vocabulario_consolidado` mezcla cuatro categorías lingüísticas distintas.**

Antes del rediseño, `vocabulario_consolidado.{principal,recurrente,comprension}` contenía de forma indiferenciada léxico semántico, verbos, palabras gramaticales y, en menor medida, fonética: era un cajón de sastre. (Estado superado: `comprension` retirado y los cuatro contenidos separados en bloques propios — ver `schema-inventario.md` §9.1–§9.4.)

**Problema 3 — superficie por actividad sin contrato claro** (hallazgo del revisor sobre v10.110).

Cada actividad tiene `contenido_linguistico` (lista libre, sin reglas operativas), `campo_semantico` (canon-controlado), y campos sueltos en `datos`. La relación entre esta superficie y los bloques top-level no está formalizada: el sistema tiene **dos verdades compitiendo** (lo declarado en consolidado vs lo presente en actividades).

**Auditoría:**

- 423 actividades en total (U0-U9).
- 423 (100 %) tienen `contenido_linguistico`.
- Solo 72 (17 %) tienen además `campo_semantico`.
- `contenido_linguistico` es prosa libre sin canon (ej. `["parientes", "vocabulario familiar"]`).
- No hay validación cruzada entre `actividad.campo_semantico` y `vocabulario_consolidado.principal.Parientes`.

> **Estado de la Parte A:** diagnóstico empírico y vocabulario común fijados. No requiere aprobación — es fundamento de las siguientes partes.

---

# Parte B — Principio arquitectónico

> **Propósito:** decidir si la dirección general (modelado lingüístico completo en fase 1, fase 2 analítica) y el cambio de naturaleza de fase 1 se aprueban. Es la decisión más alta del documento. Si esta parte se rechaza, el resto pierde sentido.

---

## §2 — Principio que propone el autor

**Toda la estructura de contenidos lingüísticos vive completa en fase 1 (en cada inventario). Fase 2 deja de generar datos: pasa a ser un agente analítico que lee, valida cruzadamente y construye relaciones.**

Resuelve los tres problemas a la vez:

- El bloque `tiempos_y_verbos` del dashboard reaparece automáticamente.
- La mezcla en `vocabulario_consolidado` desaparece (cada tipo tiene su contenedor).
- La doble verdad entre actividad y top-level desaparece (los bloques top-level son derivados de las actividades, no fuente paralela).

### §2.1 — Declaración explícita: la propuesta cambia la naturaleza de fase 1

Esta propuesta **no es un refactor local del schema**. Modifica la naturaleza misma de fase 1.

**Naturaleza vigente** (declarada en `CLAUDE.md:28` y reflejada en `schema-inventario.md`):

> Fase 1 = extracción del contenido visible al alumno del libro a JSON estructurado.

El único bloque consolidado top-level es `vocabulario_consolidado`. La normalización es ligera: capturar verbatim lo visible, agrupar el léxico explícito de la sección Vocabulario, y poco más.

**Naturaleza propuesta** (esta arquitectura):

> Fase 1 = extracción del contenido visible al alumno **más modelado lingüístico estructurado completo** (vocabulario léxico, jerarquía de tiempos y verbos, gramática, pronunciación y ortografía), con referencias canónicas controladas por canon doble (índice + PCIC A1) y bloques consolidados derivados por unidad.

**Lo que esto implica:**

- Fase 1 deja de ser "extracción + normalización ligera" para pasar a **"extracción + modelado lingüístico completo"**.
- El ejecutor de fase 1 ya no se limita a capturar texto visible: también identifica y clasifica el contenido lingüístico real de cada actividad según las 4 categorías ortogonales y referencia al canon.
- El validador de fase 1 se endurece para cubrir esa estructura adicional.
- El esfuerzo cognitivo y de tokens por unidad sube: cada actividad requiere análisis lingüístico explícito.

**Por qué es defendible este cambio:**

- La información lingüística real **ya existe implícitamente** en los inventarios actuales (las palabras léxicas viven en `datos.items_libro`, los verbos aparecen en frases, los sonidos están descritos en `reglas_foneticas`). El cambio formaliza lo que ya está, no añade contenido nuevo.
- Sin ese modelado, fase 2 no puede automatizar nada con fiabilidad — el rediseño v10.97 demostró las consecuencias.
- Los agentes futuros (CrewAI, agentes especializados) tendrán contrato claro de qué consumen, en vez de heurísticas sobre texto libre.
- El coste editorial mayor se contiene como deuda controlada (saneamiento U0-U9 explícito en pieza 13).

**Compromiso documental que esta declaración impone si la propuesta se aprueba:**

Antes de implementar, hay que actualizar:

- `CLAUDE.md:28` (raíz y de fase 1) — redefinir la naturaleza de fase 1.
- `schema-inventario.md:1` (responsabilidad del archivo) — ampliar a 4 bloques consolidados.
- `PROCESO-MAESTRO.md` — registrar el cambio como decisión cerrada nueva, con cita a esta propuesta y a la decisión 36 anterior (canon semántico) que esta supera y amplía.
- `REVIEW.md` — refletar nueva etapa.

Sin esa actualización documental coordinada, el cambio sería una contradicción interna del propio contrato.

> **Decisión a tomar / Estado actual de la Parte B:**
>
> - Aprobar o rechazar el principio general (modelado lingüístico completo en fase 1, fase 2 analítica).
> - Aprobar o rechazar el cambio de naturaleza de fase 1 declarado en §2.1, con sus implicaciones documentales obligatorias.
>
> **Si esta parte se aprueba**, se cierra el principio y se pasa a definir el shape (Parte C). **Si se rechaza**, el resto del documento no procede.

---

# Parte C — Modelo de datos

> **Propósito:** cerrar el shape concreto del nuevo modelo: qué llevan las actividades, qué llevan los bloques consolidados top-level, cómo se relacionan, y qué nomenclatura. Es la pieza más extensa porque define la estructura exacta de los inventarios futuros.

---

## §3 — Modelo nuevo de la actividad

### Lo que se elimina del schema de actividad

- **`contenido_linguistico`** — lista libre, campo huérfano (sin reglas operativas).
- **`campo_semantico`** — se sustituye por `actividad.vocabulario` (referencia canónica al léxico real presente).

⚠ **Cambio de modelo, no simple supresión:** la actividad deja de describir su contenido lingüístico en una bolsa libre (`contenido_linguistico` con texto narrativo) y pasa a **referenciarlo por carriles tipados** (4 listas con referencias canónicas controladas). El extractor ya no escribe prosa libre sobre qué trabaja la actividad; declara explícitamente qué léxico, qué verbos, qué gramática y qué pronunciación/ortografía aparece, cada uno en su lista correspondiente, contra el canon.

### Lo que se añade al schema de actividad

Cuatro listas mínimas de referencias canónicas, todas opcionales (cada actividad lleva las que correspondan a su contenido real):

```jsonc
"actividad": {
  ...
  "vocabulario": [<canonico>],              // léxico semántico presente
  "tiempos_y_verbos": [                     // verbos presentes (forma compacta por entrada)
    { "lema": "ser", "tiempo": "Presente", "formas_trabajadas": ["soy","eres","es"] }
  ],
  "gramatica": [<canonico>],                // puntos gramaticales presentes
  "pronunciacion_ortografia": [<canonico>], // sonidos / patrones / correspondencias presentes
  ...
}
```

**Sobre la forma compacta de verbos en la actividad:**

Cada elemento de `actividad.tiempos_y_verbos` lleva los campos atómicos que el libro presenta en esa actividad: `lema`, `tiempo` y `formas_trabajadas` (shape canónico en `schema-inventario.md` §3.2). Las propiedades adicionales del lema en el curso (categoría sintáctico-semántica, comportamiento morfológico por tiempo, descripción pedagógica, etc.) viven en la entrada del bloque `tiempos_y_verbos_consolidado` del top-level — no se repiten en cada actividad. Shape vigente del bloque consolidado → `schema-inventario.md` §9.2.

**Sobre la procedencia (principal / recurrente):**

⚠ **La actividad NO declara la procedencia de cada referencia.** Las 4 listas de la actividad (`vocabulario`, `tiempos_y_verbos`, `gramatica`, `pronunciacion_ortografia`) solo contienen las referencias canónicas presentes — sin etiquetarlas como principal o recurrente.

La procedencia se **deriva durante la agregación al top-level** según los criterios definidos en §0.D:

- **`principal`**: comparación directa con el índice editorial de la unidad (`nc1-curso.json`).
- **`recurrente`**: análisis de frecuencia + posición + valor pedagógico (ver glosario "vocabulario_consolidado / recurrente").

Esto evita que el ejecutor de la actividad tenga que decidir clasificación que requiere mirar todo el corpus. La determinación de procedencia es trabajo del script de agregación + apoyo humano en casos ambiguos.

### Lo que se mantiene tal cual

- `tipo`, `destreza`, `enfoque` (este último ahora explícitamente informativo).
- `instruccion_original`, `audio`/`imagen`/`video`, `respuestas`.
- `datos.items_libro`, `datos.texto_completo`, `datos.dialogo_completo`, etc. (contenido verbatim del libro). No son referencias canónicas; son el texto que el alumno ve.

### Lo que se elimina del schema de `datos.*`

- **`datos.reglas_foneticas`** (presente en 2 actividades de 423, ~0%) — codificación añadida por el extractor, no texto verbatim. Su contenido lo cubre `actividad.pronunciacion_ortografia` (referencia canónica) + `datos.items_libro` (texto verbatim).
- **`datos.palabras_modelo`** (presente en 7 actividades de 423, ~1%) — idem.

**Razón:** estos dos campos generaban doble verdad respecto a la referencia canónica nueva. Como su uso real es marginal y duplica información, se eliminan. Las 9 actividades afectadas se migran en el saneamiento de U0-U9 (E3).

**`datos.*` queda como contenido literal del libro únicamente.** Cero codificación intermedia. Cumple la regla de oro de fase 1.

---

## §4 — Bloques consolidados top-level (derivados)

Cuatro bloques paralelos en el inventario:

```
UX-nc1-inventario.json
├── ...
├── vocabulario_consolidado                  ← léxico semántico
├── tiempos_y_verbos_consolidado             ← plano por entrada verbal (una entrada por lema)
├── gramatica_consolidada                    ← puntos gramaticales
└── pronunciacion_ortografia_consolidada     ← sonidos y patrones
```

`vocabulario_consolidado`, `gramatica_consolidada` y `pronunciacion_ortografia_consolidada` se subdividen en `principal` y `recurrente`. `tiempos_y_verbos_consolidado` es **plano por entrada verbal** (no jerárquico), una entrada por lema.

> **Shape obsoleto retirado (2026-05-13).** Los ejemplos JSON concretos que vivían aquí (con campos `procedencia`, `secciones`, `palabras` y `fuentes` como objetos `{pagina, actividad_id}`) ya no son vigentes. **Shape canónico actual:**
> - Bloques consolidados con sub-bloques `principal`/`recurrente` → `schema-inventario.md` §9.1 / §9.3 / §9.4 (entradas `{ items: [{palabra, fuentes}], fuentes: [...], descripcion: {...} }`).
> - Bloque verbal plano → `schema-inventario.md` §9.2 (campos vigentes: `lema`, `tipo_de_verbo`, `rasgo_por_tiempo`, `tiempos`, `formas_trabajadas`, `fuentes`, `descripcion`).
> - Formato canónico de `fuentes` (string regex, no objeto) → `schema-inventario.md` §9.5.
>
> El principio de fondo (los bloques son derivados automáticamente del agregado de actividades + cuadros, y `tiempos_y_verbos_consolidado` es lista plana) sigue siendo válido.

**Doble fuente explícita:**

| Fuente | Aporta a los bloques top-level |
|---|---|
| **Actividades** | Vía `actividad.vocabulario`, `actividad.tiempos_y_verbos`, `actividad.gramatica`, `actividad.pronunciacion_ortografia`. |
| **Cuadros** | Vía referencias canónicas en cada cuadro (`cuadro.vocabulario`, `cuadro.tiempos_y_verbos`, etc.) + su `contenido` detallado (tablas, paradigmas) como información específica. |

Una unidad puede llenar un bloque consolidado solo con actividades (sin cuadros), o solo con cuadros (sin actividad asociada explícita), o con ambos. Las dos fuentes confluyen en el agregado.

### §4.0bis — Relación con los cuadros del libro

Los cuadros son **información de referencia** del libro (tablas de conjugación, paradigmas, listados sistematizados). Aportan a los bloques top-level mediante:

- **Referencia canónica** (`cuadro.vocabulario`, `cuadro.tiempos_y_verbos`, `cuadro.gramatica`, `cuadro.pronunciacion_ortografia`) — paralelo a las 4 listas de la actividad.
- **`contenido` detallado** — tabla, paradigma o texto literal del cuadro tal como aparece en el libro.

El `tipo_cuadro` (enum cerrado vigente de 5 valores: `gramatical`, `lexical`, `pronunciacion_ortografia`, `cultural`, `comunicativo`) **no se modifica** en esta propuesta. La división verbal vs no-verbal vive en la referencia canónica del cuadro (`cuadro.tiempos_y_verbos` vs `cuadro.gramatica`), no en `tipo_cuadro`.

> **Decisión revisada (2026-05-12):** valor `fonetico` renombrado a `pronunciacion_ortografia` para alinear con el bloque top-level. Ver `schema-inventario.md` §7 y Apéndice §A.3.

**`tipo_cuadro: comunicativo` y `tipo_cuadro: cultural`** se mantienen vigentes como tipos de cuadro, pero **no alimentan los 4 bloques top-level** definidos en esta propuesta. Estos cuadros siguen siendo información de referencia para el alumno pero su contenido no se proyecta a las 4 categorías lingüísticas.

**Consecuencia:** la única fuente de verdad del contenido lingüístico de la unidad es **el agregado de las actividades + cuadros**. Los consolidados son proyección.

### §4.1 — Nota sobre la nomenclatura de los bloques

El revisor sugirió alternativas para los nombres de los bloques verbal y pronunciación:

- Para verbal: `contenido_verbal` o `verbos_y_tiempos` (en lugar de `tiempos_y_verbos_consolidado`).
- Para pronunciación: `fonetica_ortografia` como alternativa válida (`pronunciacion_ortografia_consolidada` también aceptado por el revisor).
- Para gramática: `gramatica` sin sufijo (en lugar de `gramatica_consolidada`).

**Decisión del autor:** se mantienen los nombres actuales (`tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`).

**Justificación:**

- `tiempos_y_verbos` es el nombre **vivo en el código del dashboard** desde v10.95 (`web/index.html:615` y `:657`) y es el tipo de hilo declarado en `nc1-reciclaje.json` para los hilos jerárquicos. Cambiarlo a `verbos_y_tiempos` o `contenido_verbal` rompería coherencia con código vivo y con datos históricos.
- El sufijo `_consolidado/-a` mantiene simetría con `vocabulario_consolidado` (ya existente en main) y desambigua del campo `enfoque: gramatica` (atributo de actividad, enum cerrado) y del campo `actividad.gramatica` (lista de referencias). Sin sufijo, los tres conceptos compartirían nombre.
- La sugerencia del revisor `pronunciacion_ortografia` está incorporada (con sufijo `_consolidada` por coherencia interna).

Esta decisión no cierra la puerta a renombrar en el futuro si aparece motivo arquitectónico mayor — pero hoy, la coherencia con código vivo pesa más que la afinación léxica.

> **Decisión a tomar / Estado actual de la Parte C:**
>
> - Schema de la actividad (§3) — ✅ cerrado con la decisión de la opción B (3 campos mínimos para verbos en la actividad).
> - Bloques consolidados top-level (§4) — ✅ cerrado: 4 bloques paralelos, plano por entrada verbal, jerarquía profunda fuera del inventario.
> - Nomenclatura (§4.1) — ✅ cerrado: opción A (mantener nombres por coherencia con código vivo).
> - Trazabilidad (§4.0bis) — ✅ cerrado: campo `fuentes` obligatorio en cada entrada consolidada.
>
> **Validar:** que el shape detallado describe completamente la estructura. Posibles afinamientos quirúrgicos antes de E2.

---

# Parte D — Sistema canónico

> **Propósito:** decidir cómo se gobierna el universo de nombres válidos para los 4 bloques. Es decisión arquitectónica autónoma — encaja con cualquiera de los modelos anteriores, pero condiciona el coste operativo.

---

## §5 — Canon ampliado

### Doble fuente con prioridad estricta

1. **`nc1-curso.json`** (índice editorial del libro) — canon prioritario. Cualquier contenido lingüístico que aparezca en una actividad y esté declarado en el índice **debe** referenciarse con el nombre canónico del índice.

2. **PCIC A1** del Instituto Cervantes (`caes complete system/references/plan_curricular/by_level/a1/`) — canon secundario. Solo cubre lo que aparezca en actividades y NO esté en el índice.

3. **Si algo aparece en una actividad y no está ni en el índice ni en PCIC A1** → notificación al humano + decisión: (a) excepción justificada con nota, (b) error de codificación a corregir.

### Alcance del canon ampliado

El canon actual (`campos-semanticos-canonicos.json`, v10.108) cubre solo léxico semántico (98 entradas). Tras esta propuesta, el sistema de canon **se compone de 4 registries paralelos** (uno por bloque top-level), no de un canon único. El léxico se mantiene en su registry actual intacto; los otros 3 bloques estrenan registry propio (ver §5 "Forma del canon — registries paralelos"). Conjuntamente cubren los 4 tipos de contenido lingüístico:

- **Vocabulario:** del `vocabulario[]` y `contenido_general[]` de `nc1-curso.json` + `pcic-a1-vocabulario.json` (nociones específicas PCIC A1).
- **Gramática:** del `gramatica[]` de `nc1-curso.json` + `pcic-a1-gramatica.json`.
- **Tiempos y verbos:** registry **plano** de entradas verbales (`verbos-canonicos.json`), alineado con el shape del top-level. Cada entrada lleva su lema + metadata (tiempo, modo, rasgo verbal) como propiedades del propio canónico — no como niveles de un árbol. Fuentes: tiempos verbales del `gramatica[]` de `nc1-curso.json` cuando los menciona + paradigmas verbales en `pcic-a1-gramatica.json` + verbos léxicos en `pcic-a1-vocabulario.json`. La jerarquía pedagógica (tiempo → uso → rasgo → verbo) es lógica de proyección de fase 2 al construir hilos cross-unidad, no shape del registry. **No hay PCIC verbal propio:** el PCIC distribuye los verbos entre gramática (paradigmas) y nociones específicas (verbos léxicos).
- **Pronunciación y ortografía:** del `pronunciacion_ortografia[]` de `nc1-curso.json` + `pcic-a1-pronunciacion-ortografia.json` (sub-bloques `pronunciacion` extraído de Cervantes web + `ortografia` extraído de CAES).

### Decisiones sobre PCIC A1

**Decisión revisada (2026-05-13):** se materializa el consumo PCIC A1 como **archivos fuente propios en `fases/1-extraccion-inventario/`** (paralelos a cada registry canónico), no solo como ingesta en los registries. Esto preserva trazabilidad pedagógica, permite citar `"PCIC A1 §X.Y.Z — ..."` y abre la puerta a actualizaciones controladas cuando Cervantes publique revisión o se amplíe a A2.

**Archivos PCIC creados (estado actual):**

| Archivo PCIC en fase 1 | Origen | Estado |
|---|---|---|
| `pcic-a1-gramatica.json` | `caes/.../processed/gramatica_a1_a2.json` | Copiado, 1.078 líneas |
| `pcic-a1-vocabulario.json` | `caes/.../a1/a1_nociones_especificas_completo.json` (417 entradas trimeadas) | Copiado, 1.504 líneas |
| `pcic-a1-pronunciacion-ortografia.json` | Sub-bloques: `pronunciacion` (Cervantes web, no estaba en CAES) + `ortografia` (CAES, 101 entradas trimeadas) | Copiado, 1.003 líneas |
| `pcic-a1-comunicacion.json` | `caes/.../a1/a1_funciones_comunicativas_completo.json` (141 entradas trimeadas) | Copiado, 745 líneas. Fuera de las 4 dimensiones del schema; se conserva como recurso disponible |

**Inventarios PCIC descartados (no se copian):**

- `a1_consolidado_total.json` — redundante respecto a los archivos per-tipo de CAES.
- `a1_nociones_generales_completo.json` — no aporta para léxico de NC1 (decisión del autor).
- `a1_pragmatica_completo.json` — fuera de las 4 dimensiones del schema.

**Hallazgo importante:** PCIC A1 **no tiene** inventario propio de tiempos y verbos. Los paradigmas viven en `pcic-a1-gramatica.json` y los verbos léxicos en `pcic-a1-vocabulario.json`. El registry `verbos-canonicos.json` se nutre del cruce de ambos. Por tanto no se crea `pcic-a1-verbos.json`.

**Hallazgo importante:** PCIC A1 (CAES) **no tiene** inventario propio de pronunciación, solo de ortografía. La pronunciación se extrajo del sitio web del Instituto Cervantes (`cvc.cervantes.es`) y se integró en el sub-bloque `pronunciacion` del archivo combinado `pcic-a1-pronunciacion-ortografia.json`.

**Forma común** de todos los archivos `pcic-a1-*.json`: cabecera con `fuente`, `nivel`, `origen`, `fecha_copia` + bloque `categorias` (árbol jerárquico). **Trim aplicado a los archivos CAES:** conservados `contenido`, `descripcion` (cuando distinta del contenido), `ejemplo`; eliminados `id_original`, `tipo_contenido`, `nivel`, `orden`, `campos_originales`, `metadata_original`. Detalle en `glosario.md` sección "Fuentes PCIC y registries canónicos".

### Forma del canon — registries paralelos (decisión cerrada con matiz del revisor)

**Decisión:** se mantiene el canon léxico actual (`campos-semanticos-canonicos.json`, v10.108) **intacto y sin romper** como registry de léxico semántico. Se añaden **registries paralelos** por bloque, reutilizando la misma lógica de validación, escritura atómica y alias del módulo `scripts/canon.py`:

- `campos-semanticos-canonicos.json` (existente) — léxico semántico.
- `verbos-canonicos.json` (nuevo) — entradas verbales con metadata (lema, rasgo verbal, tiempo/modo aplicables).
- `gramatica-canonica.json` (nuevo) — para gramática, puede bastar un **enum cerrado más pequeño** (no canon rico con jerarquía como el léxico).
- `pronunciacion-ortografia-canonica.json` (nuevo) — sonidos, entonación, acentuación, correspondencias ortográficas.

**Rechazado explícitamente:** mega-canon único heterogéneo. Mezclar 4 dominios distintos en una sola tabla complicaría validación y querying. Cada bloque tiene su forma idiomática.

**Rechazado explícitamente:** naming libre sin canon. Todos los bloques tienen control de naming (canon rico o enum cerrado).

**`scripts/canon.py` se generaliza** para servir como módulo compartido de los 4 registries, manteniendo los 9 invariantes que ya implementa y añadiendo lectura/escritura de los archivos nuevos.

> **Decisión a tomar / Estado actual de la Parte D:**
>
> - ✅ Cerrado: registries paralelos + canon léxico actual intacto + reutilización de `scripts/canon.py` + rechazo de mega-canon único y de naming libre.
>
> **Validar:** que la forma del canon léxico actual no necesite ajustes para servir como referencia simétrica a los 3 nuevos registries.

---

# Parte E — Fase 2 redefinida

> **Propósito:** cerrar el pipeline de fase 2 con sus tres capas. Esta parte solo se aborda después de aprobar Parte B (principio) y Parte C (modelo de datos), porque las capas operan sobre el shape decidido allí.

---

## §6 — Fase 2 redefinida — análisis activo en tres capas

Fase 2 deja de ser productora de datos. Pasa a ser **agente analítico**:

### Capa 1 — Validación cruzada

Detecta lo que solo se ve viendo todos los inventarios a la vez:

- Un campo de `vocabulario` aparece como `recurrente` en U5 sin haber sido `principal` en ninguna unidad anterior.
- Dos unidades usan nombres distintos para el mismo contenido.
- Inconsistencias de progresión a lo largo del curso.
- Verbos que aparecen en `vocabulario` cuando deberían ir en `tiempos_y_verbos`.
- **Anticipación de léxico (regla nueva, 2026-05-12):** detecta términos que aparecen con frecuencia en las actividades de U(n) pero no fueron codificados como `recurrente` por fase 1 (porque ese léxico es canónico en una unidad posterior U(n+k)). Si esto ocurre, emite **alerta de anticipación**: la unidad U(n) está exponiendo léxico antes de su introducción oficial. Procedimiento en 4 pasos:
  1. Leer el índice editorial completo (todas las unidades).
  2. Leer el `principal` de cada unidad (declarado por fase 1).
  3. Leer el `recurrente` de cada unidad (declarado por fase 1).
  4. Re-ejecutar análisis de frecuencias sobre las actividades. Si un término aparece frecuente pero **no** está en `principal` ni en `recurrente` de U(n), y **sí** es canónico en una unidad posterior U(n+k), reportar como anticipación. Si el término es canónico en una unidad anterior y no figura en `recurrente`, no es alerta (es repaso normal que fase 1 puede no haber detectado por umbral de frecuencia).

**Output (decisión cerrada — combinación c con orden de ejecución):**

- **Autoridad formal:** un validador propio `scripts/validar_inventarios_cross.py`. Es la autoridad de la coherencia cross-unidad, simétrico al `scripts/validar_inventario.py` que ya es autoridad intra-unidad.
- **Reflejo en dashboard:** una sección/vista del dashboard que muestra las incongruencias como helper de lectura humana. NO es autoridad — refleja lo que dice el validador.
- **Orden de ejecución en el roadmap:** primero el validador (opción a), después el reflejo en dashboard (opción b). Aceptar solo dashboard sería insuficiente.

### Capa 2 — Proyección (decisión cerrada)

Construye `nc1-reciclaje.json` (único contenedor) con la taxonomía de **5 tipos**: `vocabulario`, `tiempos_y_verbos`, `gramatica`, `pronunciacion_ortografia`, `estrategia`.

Eventos `(unidad, seccion, accion)` por cada aparición del canónico, con distinción `principal` / `recurrente` (excepto en `tiempos_y_verbos`, donde la procedencia y el contexto vienen de las entradas planas del bloque consolidado y se proyectan a la jerarquía pedagógica al construir hilos cross-unidad).

**`comprension` retirado del modelo el 2026-05-12** (ver §0.D). Los eventos del reciclaje solo distinguen `principal` y `recurrente`.

### Capa 3 — Relaciones (decisión cerrada — opción b)

Conexiones que no están explícitas en JSONs individuales:

- "El verbo X de U2 se usa con el campo semántico Y en U5."
- "El sonido /θ/ de U3 reaparece en U7."
- "La preposición Z se introduce en U4 y se consolida en U6."

**Output:** artefacto separado `unidades/nc1-relaciones.json`. NO se embebe en cada evento de `nc1-reciclaje.json` ni se mete como campo nuevo del mismo archivo.

**Justificación:** el reciclaje es un timeline lineal (eventos ordenados por unidad). Las relaciones forman una red/grafo. Mezclar las dos topologías en el mismo archivo acopla representaciones distintas y dificulta análisis. Mejor dos artefactos con sus propias responsabilidades.

> **Decisión a tomar / Estado actual de la Parte E:**
>
> - Capa 1 — ✅ cerrada: validador propio como autoridad + dashboard como reflejo.
> - Capa 2 — ✅ cerrada: `nc1-reciclaje.json` único con 5 tipos.
> - Capa 3 — ✅ cerrada: artefacto separado `nc1-relaciones.json`.

---

# Parte F — Reglas de coherencia

> **Propósito:** fijar los invariantes obligatorios que el sistema debe mantener para que el modelo funcione. Son las reglas que el validador (fase 1) y el validador cross-unidad (fase 2 capa 1) aplican.

---

## §7 — Reglas de coherencia

1. **Cada elemento de `actividad.{vocabulario, gramatica, pronunciacion_ortografia}` es un canónico válido del canon** (en su tipo correspondiente — registry léxico, gramatical u ortográfico). Para `actividad.tiempos_y_verbos`, que es lista de objetos compactos (§3), la regla es asimétrica por campo:
   - `lema` — **referencia canónica** al registry `verbos-canonicos.json`. Mismo nombre de campo en actividad y en top-level (no `verbo`).
   - `tiempo` — **referencia canónica** a la enumeración cerrada de tiempos verbales del registry verbal (Presente, Pretérito perfecto, etc.).
   - `formas_trabajadas` — **NO canónico.** Es lista literal de las formas conjugadas tal como aparecen en el libro en esa actividad (formas superficiales). El validador comprueba que pertenecen al paradigma del lema declarado, pero no exige que sean entradas de un canon.
2. **Los bloques consolidados top-level son derivados.** Si un script de regeneración los reconstruye desde las actividades y el resultado difiere del JSON guardado, hay incoherencia (a corregir).
3. **Los datos literales del libro (`datos.items_libro`, `datos.texto_completo`, etc.) no son referencias canónicas.** Son texto del libro. (Nota: `datos.reglas_foneticas` y `datos.palabras_modelo` se eliminan en esta propuesta — ver §3 "Lo que se elimina del schema de `datos.*`".)
4. **`enfoque` no se usa para validar contenido lingüístico.** Es informativo. Una actividad con `enfoque=gramatica` puede tener `actividad.vocabulario` no vacío y eso no es error.
5. **Marca `_pendiente_canon`** (introducida en v10.108) se mantiene: si el ejecutor no encuentra canónico seguro durante extracción, escribe la marca literal. Bloquea cierre del inventario.

6. **Coherencia bidireccional de trazabilidad (regla nueva, pieza 9 refinada):**
   - Si `actividad.X` (con X ∈ {vocabulario, tiempos_y_verbos, gramatica, pronunciacion_ortografia}) contiene una referencia a un canónico `K`, entonces la entrada consolidada de `K` en el top-level debe listar esa actividad en su campo `fuentes`.
   - Si una entrada consolidada lista una actividad como fuente, esa actividad debe referenciar el canónico en su lista correspondiente.
   - Lo mismo para cuadros.
   - El validador de fase 1 chequea esta coherencia intra-unidad. El validador cross-unidad de fase 2 (capa 1) la asume como pre-condición.

7. **Validación de `recurrente` en 3 pasos — aplica a todos los bloques (2026-05-12, refinado):**

   Para que un término entre como `recurrente` en U(n) en cualquier bloque consolidado (vocabulario, gramática, pron/orto), debe pasar este filtro **secuencial**:

   **Paso 1 — verificación previa:** ¿aparece declarado en el índice maestro (`nc1-curso.json`) de alguna unidad anterior U(n−k)?
   - **Sí** → entra como `recurrente` legítimo (es léxico/contenido ya enseñado que vuelve a circular). Fin del filtro.
   - **No** → continúa con paso 2.

   **Paso 2 — verificación posterior:** ¿es canónico en el índice de alguna unidad posterior U(n+k)?
   - **Sí** → **anticipación**, no se codifica como `recurrente`. Fase 1 lo deja fuera silenciosamente; fase 2 (capa 1) lo detecta y reporta como alerta. Fin del filtro.
   - **No** → continúa con paso 3.

   **Paso 3 — análisis de valor pedagógico:** el término no es canónico en ninguna unidad. ¿Es contenido **necesario** para lo que U(n) construye/proyecta?
   - **Sí** → se mantiene en `recurrente` con descripción explícita que justifique por qué es necesario.
   - **No** → no entra en el consolidado. El texto sigue vivo en `datos.*` de las actividades, pero no se cataloga.

   **Pre-condiciones que ya deben cumplirse antes de aplicar el filtro:**
   - Frecuencia mínima ≥ 2 apariciones en contenido (no en instrucción, ver regla 11).
   - No está en el índice de la propia unidad U(n) (en cuyo caso iría a `principal`).
   - Función verificada (ver regla 14): la palabra aparece con la función gramatical/léxica declarada.

8. **🚫 PROHIBIDO INVENTAR PALABRAS (regla absoluta, refuerzo de regla de oro global):**
   - En **cualquier bloque consolidado** (`vocabulario_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`, `tiempos_y_verbos_consolidado`) **solo pueden aparecer palabras / lemas / categorías que aparecen literalmente en el texto del libro** (actividades, cuadros, instrucciones, respuestas, autoevaluación).
   - Si una palabra no aparece literalmente, **no se añade. No se infiere. No se completa la serie.**
   - Si el ejecutor cree que "debería" estar pero no la ve, marca el caso para revisión del autor; no la inserta.
   - Cada entrada del consolidado debe llevar su lista de `fuentes` (ver regla 10). Si una entrada no tiene fuentes, es invento → eliminar.

9. **Clasificación semántica coherente:**
   - Cada palabra debe encajar semánticamente en la categoría que se le asigna. `campeón` no es nacionalidad; `mesa` no es color; `hospital` no es profesión.
   - **Conectores, conjunciones, adverbios y marcadores temporales NO van en `vocabulario_consolidado` — van en `gramatica_consolidada`.** Ejemplos: `y`, `o`, `pero`, `también`, `no`, `sí`, `muy`, `mucho`, `bastante`, `mañana`, `ayer`, `hoy`. El léxico semántico es sustantivos comunes, adjetivos calificativos y verbos como léxico (no como paradigma). Lo demás es gramática.
   - Si una palabra aparece en una categoría incorrecta, es bug de extracción a corregir, no decisión editorial. El validador de fase 1 chequea casos conocidos a partir del canon semántico.

10. **Trazabilidad obligatoria con formato estándar (`fuentes`):**
    - Cada palabra/lema/entrada de un bloque consolidado lleva una lista `fuentes` con las localizaciones literales donde aparece, en formato compacto: `["p13-act4", "p16-act1", "cuadro@p20"]`.
    - El formato canónico es `p{numero_pagina}-act{numero_actividad}` para actividades y `cuadro@p{numero_pagina}` para cuadros (con `#idx` opcional si hay varios cuadros en la misma página).
    - **Sufijo `@R` para fuentes de respuesta** (2026-05-12): si la palabra aparece únicamente en el campo `respuestas` de una actividad (no en el contenido directo `datos.*`), la fuente se marca con el sufijo `@R`. Ejemplo: `"p15-act6@R"` indica que `el` aparece en la respuesta de p15-act6 ("Las profesoras son mexicanas") pero no en los prompts o textos del libro. Razón: el alumno produce ese token; no lo lee del libro. El dashboard renderiza estas fuentes con un color distinto (azul claro) para diferenciarlas de las fuentes de contenido directo.
    - El número de fuentes es la frecuencia real. Esto **obliga al extractor a contar**: si no encuentra al menos una fuente, la entrada no se incluye (refuerza regla 8).
    - Para el shape de las entradas en bloques consolidados, ver §0.D y §4.0bis.

11. **Solo el contenido que el ALUMNO LEE cuenta (regla nueva refinada, 2026-05-12):**

    **Principio:** una fuente válida es texto que el **alumno lee o procesa** cuando hace la actividad. **Lo que el extractor describe ABOUT la actividad (metadatos, descripciones narrativas, notas) NO cuenta**, aunque viva dentro de `datos` o de otros campos del JSON.

    **Tabla canónica de campos de inventario y su validez como fuente:**

    | Campo | ¿Alumno lo lee/procesa? | Validez como fuente |
    |---|---|---|
    | `instruccion_original` | No (lo dice el profe oralmente) | ❌ excluir |
    | `datos.pasos`, `datos.pasos_a_seguir` | No (instrucciones de tarea) | ❌ excluir |
    | `datos.instrucciones_adicionales`, `datos.guion_didactico` | No | ❌ excluir |
    | `datos._nota`, `datos._comentario` (cualquier campo con prefijo `_`) | No (nota interna del extractor) | ❌ excluir |
    | `datos.subtipo`, `datos.objetivo`, `datos.objetivos` | No (metadata pedagógica) | ❌ excluir |
    | `imagen.descripcion` | **No** (descripción narrativa del extractor de lo que muestra la imagen) | ❌ excluir |
    | `audio.descripcion` (si existe, narrativa) | No | ❌ excluir |
    | **`datos.items_libro`** (sin contar el numerador estructural inicial `1`, `2`) | Sí (los lee/completa) | ✅ contar |
    | **`datos.texto_completo`** | Sí (lo lee) | ✅ contar |
    | **`datos.dialogo_completo`** | Sí (lo lee/escucha) | ✅ contar |
    | **`datos.ejemplo_libro`**, **`datos.ejemplos_modelo`** | Sí (modelo) | ✅ contar |
    | **`datos.palabras_recuadro`** | Sí (banco de palabras) | ✅ contar |
    | **`datos.preguntas`**, **`datos.opciones_respuesta`** | Sí (responde) | ✅ contar |
    | **`datos.dialogos_modelo`**, **`datos.expresiones_dadas`** | Sí | ✅ contar |
    | **`respuestas`** | Sí (parte del ejercicio resuelto) | ✅ contar |
    | **`audio.transcripcion`** (si existe transcripción literal del audio) | Sí (escucha lo que está transcrito) | ✅ contar |
    | **Contenido de `cuadros`** (`cuadro.contenido` y sus subcampos) | Sí (tabla/explicación pedagógica) | ✅ contar |

    **Regla general:**

    > Si el contenido del campo es **texto que aparece en el libro del alumno** (lo que él ve impreso o escucha en el audio), cuenta. Si es **metadata generada por el extractor** para describir la actividad/imagen/audio, no cuenta.

    **Heurísticas para distinguir:**
    - Si el texto está redactado en **imperativo dirigido al alumno** ("Completa...", "Practica..."), es directivo → excluir.
    - Si el texto está redactado como **narración descriptiva del extractor** ("Foto de chico levantando la mano", "Ilustración de dos amigos"), es metadata → excluir.
    - Si el campo tiene prefijo `_` (subrayado), es interno → excluir.
    - Cualquier campo cuyo nombre incluya `descripcion`, `nota`, `subtipo`, `objetivo`, `guion`, `pasos`, `instruccion` → excluir por defecto.

    **Lista de exclusiones también:**
    - Numeradores estructurales de items (`1 _____`, `2 _____`).
    - Marcadores de huecos (`[1]`, `[2]`, `_____`, `___`).
    - Etiquetas tipo "a)", "b)" usadas para enumerar opciones de respuesta.
    - **Paréntesis-anotación dentro de campos de contenido:** cuando un campo válido (p. ej. `respuestas`) contiene un paréntesis con anotación del extractor sobre **cómo aparece visualmente algo en el libro** (no contenido real). Patrones típicos:
      - `(con círculo morado en el libro)`, `(con marca azul)`
      - `(subrayado)`, `(en negrita)`, `(en cursiva)`, `(tachado)`, `(resaltado)`
      - `(destacado tipográficamente)`, `(ilustrado)`
      - `(en el libro)` precedido de cualquier descripción visual
    - **Operativa:** el extractor elimina estos paréntesis antes del análisis, manteniendo solo el contenido real del campo. Ejemplo:
      - `"Números marcados (con círculo morado en el libro): 20, 11, 10"` → tras limpieza → `"Números marcados : 20, 11, 10"`. Los artículos/conjunciones dentro del paréntesis NO se contabilizan.
    - **Se excluyen explícitamente:**
      - `instruccion_original` — meta-texto principal que le dice al alumno qué hacer.
      - **Cualquier campo de `datos` que sea texto directivo/instructivo**, no contenido para aprender. Ejemplos típicos en NC1:
        - `datos.pasos` — pasos de una tarea final ("Practica el diálogo con tus compañeros").
        - `datos.pasos_a_seguir`, `datos.instrucciones_adicionales`, `datos.guion_didactico`.
        - Cualquier campo de `datos` cuyo contenido sea **lo que el alumno debe HACER**, no lo que LEE/ESCUCHA como input lingüístico.
      - Numeradores estructurales de items (`1 _____`, `2 _____`).
      - Marcadores de huecos (`[1]`, `[2]`, `_____`, `___`).
      - Etiquetas tipo "a)", "b)" usadas para enumerar opciones de respuesta.
      - **Criterio operativo:** si el texto se redacta en imperativo dirigido al alumno (*"Completa..."*, *"Escucha..."*, *"Practica..."*, *"Representa..."*) o describe la mecánica de la actividad, es directivo y se excluye.
    - **Audio:** si la palabra está declarada con transcripción literal en el inventario, cuenta. Si solo se escucha sin transcribir, no se puede contabilizar (limitación práctica reconocida).
    - **Por qué:** la instrucción usa léxico genérico de aula ("compañero", "tu", "ejercicio") que no es léxico que la unidad enseña — usarlo como fuente infla artificialmente la frecuencia y desvirtúa la noción de "recurrente".

12. **Lectura cruzada del índice maestro del libro (regla nueva, 2026-05-12):**
    - El extractor lee **todos los campos del índice maestro del libro** (`nc1-curso.json`), no solo uno por unidad: `vocabulario`, `gramatica`, `para_aprender`, `pronunciacion_ortografia`, `comunicacion`, `destrezas`, `cultura`.
    - **Aclaración fundamental:** `nc1-curso.json` refleja el **índice maestro del libro** (más descriptivo). Este índice clasifica cada contenido en un campo concreto, y esa clasificación **sí es vinculante** para decidir si una categoría es `principal` en el bloque modelo correspondiente.
    - **Mapeo campo del índice → bloque del modelo:**

      | Campo del índice | Bloque consolidado del modelo |
      |---|---|
      | `vocabulario` | `vocabulario_consolidado.principal` |
      | `gramatica` (entradas no verbales) | `gramatica_consolidada.principal` |
      | `gramatica` (entradas "Verbo X" / "Tiempo X") | `tiempos_y_verbos_consolidado` |
      | `pronunciacion_ortografia` | `pronunciacion_ortografia_consolidada.principal` |
      | `comunicacion`, `destrezas`, `cultura`, `para_aprender` | contexto/función, no consolidan léxico directo |

    - **Casos especiales** donde el contenido tiene **doble dimensión** (aparece tanto en vocabulario como en gramática u otro bloque, por su naturaleza lingüística):
      - **`Colores`** (en `gramatica[]` U1) es léxico semántico → `vocabulario_consolidado.principal` como categoría. La concordancia de género que el libro introduce mediante colores vive en `gramatica_consolidada.principal` como `Concordancia de género`. Doble dimensión: un mismo contenido pedagógico vehicula dos categorías canónicas distintas.
      - **`Interrogativos`** (en `pronunciacion_ortografia` U1) se queda en `pronunciacion_ortografia_consolidada.principal` (signos ¿? + entonación). NO se reasigna a gramática: el índice maestro lo coloca en pron/orto y eso vincula el modelo.

13. **Descripción por categoría con función PCIC obligatoria (regla nueva refinada, 2026-05-12):**

    **A — La descripción va por CATEGORÍA, no por palabra individual.**
    - Cada **categoría** (Artículos determinados, Concordancia de género, Pronombres personales, Conjunciones…) lleva su campo `descripcion`.
    - Las palabras individuales dentro de cada categoría llevan solo `{palabra, fuentes}`. NO se duplica la función palabra-a-palabra.

    **B — Aplica por igual a `principal` y `recurrente`, en los 3 bloques** (vocabulario, gramática, pron/orto). Mismo shape, mismo formato.

    **C — La descripción se basa en el PCIC, no se inventa.**
    - Fuente vinculante: `fases/1-extraccion-inventario/pcic-a1-gramatica.json` (copia local del Plan Curricular del Instituto Cervantes, sección Gramática A1).
    - Para cada categoría canónica del modelo, se mapea con su entrada PCIC A1 correspondiente y se redacta una descripción que respete su clasificación.
    - Si la categoría no encaja en PCIC A1 directamente, se documenta con `_origen_descripcion: "adaptado"` y se justifica.
    - **Prohibido inventar** la descripción si existe la correspondiente en PCIC.

    **D — Shape por unidad:** `descripcion: { "U1": "...", "U2": "..." }`. Diccionario con clave = unidad, valor = string. Mismo formato que `lo_que_se_trabaja` de los verbos (§15.2).

    Ejemplo:
    ```jsonc
    "Pronombres personales": {
      "items": [
        {"palabra": "yo", "fuentes": ["p14-act1", "p16-act1", ...]},
        {"palabra": "tú", "fuentes": [...]}
      ],
      "descripcion": {
        "U1": "PCIC A1 §7.1.1 Pronombre sujeto. Función de sujeto para personas: 1ª, 2ª y 3ª singular y plural. Deixis personal (yo = hablante, tú = oyente). Sujeto tácito como norma general; pronombre explícito para énfasis, contraste o desambiguación."
      }
    }
    ```

14. **Desambiguación funcional — principio general (regla nueva refinada, 2026-05-12):**

    **Principio:** para que una palabra `X` cuente como fuente de la categoría `C`, **la función real que `X` ejerce en el contexto específico de esa actividad o cuadro debe corresponderse con la función que define la categoría `C`**. Si la función no concuerda, esa ocurrencia **no es fuente válida** para esa categoría.

    **Criterio de las tres coincidencias.** El extractor verifica que coincidan:

    1. **Nombre de la categoría** (ej. `Conjunciones disyuntivas`).
    2. **Descripción de la categoría** (ej. "indica alternativa entre elementos").
    3. **Uso real del término en el contexto concreto** (ej. ¿es alternativa en "¿X o Y?" o es la letra "o" en "-o/-a"?).

    Si las tres no concuerdan → la ocurrencia se descarta.

    **Contextos en los que la función se aparta del uso natural** (no exhaustivo):

    | Contexto | Función real ≠ categoría |
    |---|---|
    | Actividades centradas en abecedario o deletreo | Palabra-letra, no la palabra gramatical |
    | Notas explicativas con morfemas: `-o/-a`, `-mente`, `-s`, `-es`, `-ón`, `-dad` | Morfema/marca, no la palabra léxica |
    | Referencias metalingüísticas: "la letra X", "el sonido /X/", "el verbo Y", "la palabra Z" | Mención, no uso |
    | Operaciones matemáticas: `dos más tres = cinco` | Operador matemático, no comparativo |
    | Enumeración estructural: `a)`, `b)`, `1.`, `2.` | Etiqueta de orden, no palabra léxica |
    | Marcadores de hueco: `_____`, `[1]`, `[2]` | Estructura editorial, no contenido |
    | Etiquetas de columnas/filas de tablas (cuando el cuadro NO se centra en esa función) | Etiqueta de organización, no contenido trabajado |
    | Nombres de personajes en diálogos: "PABLO:", "JULIA:" | Etiqueta de turno, no léxico |
    | Citas/títulos del libro: "Unidad 1", "página 14" | Referencia editorial, no contenido lingüístico |

    **Aplicación operativa:**
    - Para cada candidato a fuente, el extractor analiza el **contexto inmediato** (palabras antes y después + tipo de bloque donde aparece) y decide si la función es coherente con la categoría destino.
    - Si la actividad contiene **ambos usos** del mismo término (uno real, uno metalingüístico), la actividad cuenta como fuente solo si hay al menos una ocurrencia con función real.
    - Para palabras frecuentes con muchos usos posibles, el extractor lista solo las apariciones donde la función real coincide. Si la duda persiste en un caso concreto, marca con `_funcion_ambigua: true` y consulta al autor.

    **Ejemplos concretos en NC1 U1:**
    - `o` en `cuadro@p14#4` aparece dentro de la nota "Las terminaciones -o/-a están resaltadas tipográficamente" — es **morfema**, no conjunción disyuntiva. Descartado para `Conjunciones disyuntivas`.
    - `o` en `cuadro@p20#3` aparece en "usted, ustedes **o** vos" — es **conjunción real**. Cuenta.
    - `te` en `p13-act6` aparece en "Pe-a-te-erre-i-ce-i-a" — es **letra**, no pronombre. Descartado para `Pronombre clítico`.
    - `te` en `p16-act2` aparece en "¿Cómo te llamas?" — es **pronombre clítico**. Cuenta.
    - `más` en `p17-act6` aparece en "tres más cinco = ocho" — es **operador matemático**, no comparativo. Descartado para `Cuantificadores comparativos`.

    **Esta regla aplica a TODOS los bloques consolidados** (vocabulario, gramática, pronunciación/ortografía, verbos), no solo a casos puntuales como abecedario.

    ---

    ### §7bis — Protocolo de verificación obligatorio por categoría (regla 14 operacionalizada, 2026-05-12)

    **Por qué este protocolo:** la regla 14 enunciada arriba es un principio. Sin un protocolo operativo concreto, el extractor (humano, Claude Code o agente) cae en atajos: listas hardcodeadas de actividades, regex frágiles, o asume coincidencia funcional sin verificarla. Esto introduce errores sistemáticos. **Por cada categoría canónica se define un protocolo específico de verificación** que el extractor debe ejecutar antes de declarar una fuente válida.

    #### Principios generales del protocolo

    1. **Análisis del contexto sintáctico inmediato** — no basta con encontrar la palabra; hay que analizar las palabras circundantes (antes y después) para verificar que el papel sintáctico coincide con la definición de la categoría.
    2. **Análisis del contexto temático del cuadro/actividad** — si la actividad o cuadro está centrado en otra dimensión lingüística (p. ej. abecedario, ortografía, paradigma verbal), las palabras gramaticales que aparecen pueden estar ahí por razones estructurales, no por trabajo de su función.
    3. **Prohibido el análisis simple por regex aislado** — toda asignación debe ir acompañada de una verificación documentada, no de un `find_locs` que devuelve coincidencias literales.
    4. **Atajos hardcodeados (listas tipo `ABC_ACTS`) prohibidos como mecanismo principal** — solo aceptables como referencia auxiliar; el filtro principal debe venir del análisis funcional.

    #### Verificaciones específicas por categoría

    **`Pronombre sujeto` (PCIC §7.1.1)** — el pronombre cuenta solo si ejerce función de sujeto:
    - ✅ Sujeto explícito antepuesto al verbo: "**Yo** me llamo Pedro."
    - ✅ Sujeto pospuesto o tópico: "**Ella** se llama Elisabeth."
    - ✅ En tabla de paradigmas: "yo soy / tú eres / él es" (el pronombre es etiqueta del paradigma trabajado).
    - ❌ Tras preposición (objeto preposicional, pronombre tónico): "sin **ella**", "con **él**", "a **ti**", "para **mí**". Función ≠ sujeto.
    - ❌ Como referencia deíctica metalingüística: "¿Con h o sin **ella**?" donde *ella* refiere a la letra h.
    - **Verificación:** examinar la palabra inmediatamente anterior (en el mismo enunciado o cláusula). Si es preposición (`a`, `ante`, `bajo`, `con`, `contra`, `de`, `desde`, `en`, `entre`, `hacia`, `hasta`, `para`, `por`, `según`, `sin`, `sobre`, `tras`), la ocurrencia se descarta.

    **`Pronombre clítico de objeto` (si se incorpora — PCIC §7.1.2/§7.1.3)** — pronombres átonos:
    - ✅ Adyacente al verbo, en función de OD/OI: "Me llamo Lucía", "Se llama Pedro".
    - ❌ Como letra: "Pe-a-**te**-erre-i-ce-i-a".
    - **Verificación:** examinar si está en contexto de deletreo (secuencia de letras separadas por guion o por espacio en activitidad de abecedario).

    **`Conjunciones copulativas` (PCIC §14.1) / `disyuntivas` (§14.2)** — conexión sintáctica:
    - ✅ Une dos elementos del mismo rango: "rojo **y** azul", "¿g **o** j?".
    - ❌ Como letra (`y` = "i griega", `o` = letra "o"): "la letra **o**".
    - ❌ En descripción morfológica: "las terminaciones -**o**/-a", "el morfema -**y**".
    - **Verificación:** examinar contexto a ±20 caracteres. Si aparece patrón `letra X`, `terminación -X`, `morfema -X`, `-X/-Y`, `/X/`, `sonido /X/`, descartar.

    **`Adverbios de afirmación y negación` (PCIC §8)** — sí, no:
    - ✅ `no` antepuesto a verbo: "No me llamo Pedro".
    - ✅ `sí`/`no` como respuesta breve a interrogativa: "— ¿Eres profesor? — Sí."
    - ❌ `no` en construcciones tipo "ni... ni..." (sería de coordinación, no negación frasal).
    - **Verificación:** examinar la palabra siguiente (`no` + verbo finito) o el contexto interrogativo previo (`sí`/`no` como respuesta).

    **`Adverbios de grado / intensificadores` (PCIC §8)** — muy:
    - ✅ `muy` antepuesto a adjetivo o adverbio: "muy bien", "muy alto".
    - ❌ `muy` en otros contextos (raro pero verificar).
    - **Verificación:** examinar palabra siguiente — debe ser adjetivo o adverbio.

    **`Cuantificadores comparativos` (PCIC §8)** — más, menos:
    - ✅ Comparativo de superioridad: "más alto que", "más alto".
    - ❌ Operador matemático: "tres más cinco = ocho".
    - **Verificación:** si la actividad contiene operaciones aritméticas (signos `+`, `=`, números consecutivos), descartar.

    **`Artículos definidos / indefinidos` (PCIC §3)** — el, la, los, las / un, una, unos, unas:
    - ✅ Antepuesto a sustantivo: "**el** libro", "**la** silla".
    - ❌ `el` en función de pronombre tónico (no debería confundirse con `él` con tilde, pero verificar).
    - **Verificación:** examinar palabra siguiente — debe ser sustantivo común.

    **`Concordancia de género`** — términos `masculino` / `femenino`:
    - ✅ En contexto explicativo de género gramatical o etiqueta de columna en tabla de género: "masculino: el libro / femenino: la mesa".
    - ❌ Como sustantivo común (raro en NC1 A1).
    - **Verificación:** examinar contexto — debe ser cuadro o explicación gramatical sobre género, no uso casual.

    **`Vocabulario` (cualquier categoría léxica)** — sustantivos comunes, adjetivos:
    - ✅ Uso real en frase o enumeración: "Tengo un **libro** y una **mochila**".
    - ❌ Mención metalingüística: "la palabra **libro**", "el sustantivo **libro**".
    - **Verificación:** examinar si la palabra está siendo USADA o MENCIONADA. Marcadores de mención: `la palabra X`, `el sustantivo X`, `el verbo X`, comillas tipográficas envolviendo X.

    #### Documentación obligatoria de cada fuente

    Cuando el extractor declara que `palabra X` tiene fuente `p13-act7`, debe poder responder por escrito:

    - **¿Qué función ejerce X en p13-act7?** (sujeto / OD / OI / atributo / conjunción / cuantificador / etc.)
    - **¿Esa función coincide con la categoría declarada?** (sí/no, con justificación)
    - **¿Hay menciones metalingüísticas u otros contextos especiales?** (sí/no)

    Si la respuesta a la 2ª pregunta no es un "sí" claro, la fuente **no se declara**. Si la duda persiste, se marca con `_funcion_ambigua` y se escala al autor.

    #### Por qué este protocolo (registro de aprendizaje)

    Casos reales que llevaron a formalizar este protocolo:

    1. `te` en `p13-act7` matchea por "¿Cómo **te** llamas?" (clítico real) **pero también** por estar en actividad del abecedario donde `te` también puede aparecer como nombre de letra T. La distinción requiere análisis contextual, no lista de actividades.
    2. `ella` en `p13-act7` matchea por "sin **ella**" (referencia deíctica a la letra h). El criterio "es actividad de abecedario, excluir" es insuficiente: el verdadero criterio es "está tras preposición, no es sujeto".
    3. `o` en `cuadro@p14#4` matchea por la nota explicativa "-**o**/-a". El criterio "es cuadro de género, excluir" es insuficiente: el verdadero criterio es "está en patrón morfológico `-X/-Y`, no es conjunción".
    4. `más` en `p17-act6` matchea por "tres **más** cinco = ocho". El criterio "es actividad de sumas, excluir" es insuficiente: el verdadero criterio es "está en operación aritmética, no es comparativo".

    **Patrón común:** el atajo hardcodeado por actividad pierde el principio general. La regla correcta es el análisis sintáctico-semántico del contexto inmediato.

> **Decisión a tomar / Estado actual de la Parte F:**
>
> - ✅ Cerrada: 14 reglas operativas obligatorias.
> - **Validar:** que la lista cubre todos los invariantes necesarios o si falta alguno.

---

# Parte G — Decisiones consolidadas

> **Propósito:** verificar de un vistazo el estado real de todas las decisiones del documento. Es la tabla de cierre formal. Si alguna pieza marcada como decidida no lo está realmente, hay que volver a la parte correspondiente.

---

## §8 — Piezas estructurales decididas vs abiertas

| # | Pieza | Estado | Decisión |
|---|---|---|---|
| 1 | Schema del inventario | ✅ Decidido | 4 bloques top-level paralelos, derivados de **doble fuente: actividades + cuadros** (§4.0bis). Cada entrada del top-level lleva `fuentes` con referencias a actividades y/o cuadros del propio inventario. |
| 2 | Estructura de `tiempos_y_verbos` | ✅ Decidido (principio) — shape canónico vive en `schema-inventario.md` §9.2 | **Principio:** inventario plano por entrada verbal (una entrada por lema). **Shape canónico actual → `schema-inventario.md` §9.2** (campos vigentes: `lema`, `tipo_de_verbo`, `rasgo_por_tiempo`, `tiempos`, `formas_trabajadas`, `fuentes`, `descripcion`). Las etiquetas pedagógicas (`introduce/amplía/aplica/sistematiza/contrasta`) viven en fase 2, no aquí. **Registry `verbos-canonicos.json`** con shape parcialmente distinto, alineación pendiente Paso 3 (ver Apéndice §A.3 del schema). |
| 3 | Categorías de `gramatica` | 🔄 Reabierta 2026-05-12 — scaffold cerrado, registry PCIC en curso | **Estado:** la lista de 15 categorías cerrada el 2026-05-11 quedó superada porque excluía categorías PCIC válidas (pronombres personales, conjunciones, adverbios afirmación/negación). **Nueva estrategia (§14.0):** la lista de pieza 3 funciona como scaffold de alto nivel. Las categorías reales del registry vienen de `fases/1-extraccion-inventario/pcic-a1-gramatica.json` (PCIC A1 oficial). Procedimiento de asignación: scaffold → resolución PCIC específica → naming PCIC literal. `Conjunciones`, `Pronombres personales` y `Adverbios de afirmación/negación` SÍ entran ahora con respaldo PCIC. La materialización del `gramatica-canonica.json` se hace tomando categorías PCIC A1. |
| 4 | Estructura de `pronunciacion_ortografia` | ✅ Decidido (alcance + lista exacta) | **Alcance:** sonidos individuales + correspondencias ortográficas + entonación + acentuación + signos de puntuación interrogativos/exclamativos + mayúsculas + vocales + letras homófonas. **Lista exacta materializada en §16 con matriz de cobertura cruzada contra las 9 entradas de `pronunciacion_ortografia[]` de `nc1-curso.json`** (más la entrada de mayúsculas reasignada de pieza 3). 7 categorías con estructura `{categoría → subcategoría → items}` de dos niveles. |
| 5 | Canon — forma | ✅ Decidido | **(a) con matiz:** canon léxico actual intacto + 3 registries paralelos por bloque (`verbos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`). Reutilizan la misma lógica de `scripts/canon.py`. Rechazado mega-canon único heterogéneo. Para gramática puede bastar enum cerrado más pequeño que canon rico. |
| 6 | Canon — alcance PCIC A1 | ✅ Decidido | Consumo completo de los inventarios A1 disponibles. |
| 7 | Output fase 2 — validación cruzada | ✅ Decidido | **(c) combinada con orden (a):** validador propio `scripts/validar_inventarios_cross.py` como autoridad formal + reflejo en dashboard como helper de lectura. Ejecutar primero el validador, después el reflejo. Solo dashboard sería insuficiente. |
| 8 | Output fase 2 — relaciones | ✅ Decidido | **(b)** artefacto separado `unidades/nc1-relaciones.json`. NO embebido en `nc1-reciclaje.json` (timeline lineal vs red de relaciones — topologías distintas). |
| 9 | Relación actividad ↔ top-level | ✅ Decidido (refinado tras dictamen revisor) | Top-level es derivado; actividad es fuente. 4 listas canónicas en cada actividad. **Trazabilidad explícita obligatoria:** cada entrada consolidada del top-level lleva campo `fuentes` con referencias mínimas (página + `actividad_id` o `cuadro_id`) a los sitios concretos del inventario donde aparece. Permite validación bidireccional: si la actividad referencia un canónico, ese canónico debe listarla como fuente; y al revés. Cierre de §3-§4. |
| 10 | Estado de `contenido_linguistico` | ✅ Decidido | Se elimina del schema. |
| 11 | Estado de `campo_semantico` | ✅ Decidido | Se elimina del schema (sustituido por `actividad.vocabulario`). |
| 12 | Estado de `enfoque` | ✅ Decidido | Se mantiene como **informativo, no clasificatorio**. Se usa solo cuando `destreza` MCER no basta. |
| 13 | Saneamiento de U0-U9 | ✅ Decidido | Se le pide al ejecutor 2 cuando todo esté definido. No es solo renombrar — es re-extraer las 423 actividades con la nueva estructura. |
| 14 | Cambio de modelo (carriles tipados vs bolsa libre) | ✅ Decidido | La actividad deja de describir contenido lingüístico en prosa libre (`contenido_linguistico`); pasa a referenciarlo por carriles tipados (4 listas con canónicos). Formulado explícitamente en §3 para que no parezca simple supresión. |
| 15 | Campos `datos.*` codificados | ✅ Decidido | Se eliminan `datos.reglas_foneticas` (2 actividades) y `datos.palabras_modelo` (7 actividades). El resto de `datos.*` (`items_libro`, `texto_completo`, etc.) se mantiene como contenido verbatim del libro. Cero codificación intermedia. |
| 16 | Relación cuadros ↔ bloques top-level | ✅ Decidido | Doble fuente: actividades + cuadros aportan paralelamente. Los cuadros llevan referencias canónicas + `contenido` detallado. `tipo_cuadro` mantiene 5 valores (gramatical, lexical, pronunciacion_ortografia, cultural, comunicativo; `fonetico` renombrado a `pronunciacion_ortografia` el 2026-05-12 para alinear con el bloque top-level). `comunicativo` y `cultural` se mantienen pero no alimentan los 4 bloques top-level. |
| 17 | Procedencia (principal/recurrente) | ✅ Decidido | NO se declara en la actividad. Se deriva por el script de agregación al top-level: `principal` por comparación con índice del libro; `recurrente` por análisis de frecuencia cross-actividades + filtro de anticipación (regla 7). **`comprension` retirado del modelo el 2026-05-12** (ver §0.D). Las definiciones detalladas viven en §0.D. |

> **Decisión a tomar / Estado actual de la Parte G:**
>
> - **17 piezas cerradas.** Pieza 3 cerrada el 2026-05-11 con matriz de cobertura cruzada en §14.
> - **Validar:** que el estado coincide con lo discutido. Si alguna pieza requiere reabrirse, se vuelve a su parte correspondiente.

---

# Parte H — Impacto operativo

> **Propósito:** aprobar el plan de implementación. Define qué se reescribe, en qué orden, con qué riesgo. Esta parte solo se aborda después de cerrar la Parte G — si las decisiones cambian, el plan cambia.

---

## §9 — Impacto e implicaciones

### Archivos que se reescriben

**Fase 1:**

- `schema-inventario.md` — §3 actividad sin `contenido_linguistico` ni `campo_semantico`, con 4 listas nuevas (incluida `tiempos_y_verbos` con su shape compacto de 3 campos). §9 reformulada para los 4 bloques top-level derivados (incluido el shape **plano por entrada verbal** de `tiempos_y_verbos_consolidado` — pieza 2 de §8).
- `reglas-operativas.md` — §5.6 reescrita (canon ampliado a 4 tipos, doble fuente con prioridad). Política nueva. Sección sobre jerarquía verbal.
- `prompt.md` — pasos de extracción adaptados: el ejecutor identifica el contenido lingüístico real, referencia al canon, y registra verbos con tiempo + formas_trabajadas.
- `convenciones-y-casos.md` — convenciones nuevas para los 4 tipos.
- **Nuevo:** script de fase 1 que regenera los 4 bloques top-level a partir de actividades + cuadros del propio inventario (cierra el principio de "consolidados son derivados"). Vive con los demás scripts de fase 1 — no en fase 2.
- `validar_inventario.py` — validación estructural de las 4 listas. Restricciones nuevas (referencias a canon válido por tipo). Validación específica del shape `tiempos_y_verbos`.
- `campos-semanticos-canonicos.json` — **se mantiene intacto** como registry de léxico semántico (decisión cerrada de pieza 5). Se añaden 3 registries paralelos nuevos: `verbos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`. No hay ampliación a 4 tipos en un único archivo. La metadata PCIC asociada a cada entrada verbal (tiempo, modo, rasgo verbal) vive en `verbos-canonicos.json`.

**Fase 2:**

- `regenerar_reciclaje_mapa.py` y `regenerar_reciclaje_vocabulario.py` — sustituidos por scripts nuevos. **Importante:** la derivación de los bloques consolidados top-level es responsabilidad de **fase 1** (script de regeneración que vive con el resto de fase 1 y se ejecuta al cerrar cada inventario unitario; los top-level se guardan dentro de `UX-nc1-inventario.json`). Fase 2 **solo consume** los top-level ya derivados — no los recalcula. Los scripts nuevos de fase 2 leen los top-level + los datos de actividad de los inventarios cerrados y proyectan hilos al reciclaje (capa 2) y relaciones (capa 3). Esto preserva el principio de §2: fase 2 deja de producir datos editoriales.
- `validar_inventarios_cross.py` (nuevo) — validación cruzada cross-unidad (capa 1).
- Script o módulo nuevo para la capa 3 (relaciones).

**Datos:**

- `nc1-reciclaje.json` — schema ampliado con 5 tipos de hilo + posible campo `relaciones`. Hilos `tiempos_y_verbos` reaparecen con su jerarquía v10.95.
- 10 inventarios U0-U9 — recodificación: ejecutor 2 procesa las 423 actividades con el nuevo schema, incluyendo identificación de verbos con `tiempo` + `formas_trabajadas`.

### Lo que se mantiene

- `tipo` (taxonomía de 20).
- `destreza` (enum MCER de 6).
- `enfoque` (enum de 6) como informativo.
- `tipo_cuadro` (5 valores) y la estructura de cuadros.
- `seccion` del libro (7 valores).
- Estructura de páginas, autoevaluación, IDs.
- Marca `_pendiente_canon` (v10.108) con su semántica.
- Distinción `principal` / `recurrente` en `vocabulario_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada` (`comprension` retirado del modelo el 2026-05-12, ver §0.D).

### Estimación del trabajo — plan revisado por el revisor (5 etapas)

| Etapa | Trabajo | Riesgo |
|---|---|---|
| **E1** — Cierre arquitectónico | Las 8 piezas + pieza 9 cerradas con el revisor (este documento). | Bajo |
| **E1.5** — Spike empírico | Aplicar el shape propuesto manualmente sobre **U3 y U7** (las dos unidades más ricas en variedad lingüística: cubren léxico + verbos regulares e irregulares con cambio vocálico + fonética del /θ/ + ortografía + gramática). Detectar problemas antes de comprometer el contrato. Trabajo desechable si no se necesita ajuste. | Bajo |
| **E2** — Reescritura contractual fase 1 | Schema + reglas + prompt + validador endurecido + canon ampliado (registries paralelos). Batch único **con la forma probada en E1.5**. | Medio |
| **E3** — Saneamiento U0-U9 | Ejecutor 2 procesa las 423 actividades con el nuevo schema y los 4 bloques consolidados con trazabilidad de fuentes. | Alto (trabajo editorial extenso) |
| **E4a** — Reactivar fase 2 (proyección + validación cruzada) | Scripts nuevos para la **capa 1 (validación cruzada autoridad) y capa 2 (proyección)**. `validar_inventarios_cross.py` + reescritura del regenerador de reciclaje. | Medio |
| **E4b** — Capa de relaciones | Script y artefacto `nc1-relaciones.json` (capa 3). **No se hace en el mismo batch que E4a**: la capa de relaciones es la menos estable y depende de que los datos consolidados estén maduros. | Medio-alto |

**Justificación del cambio respecto al plan original de 4 etapas:**

- **E1.5 añadida**: validación empírica antes del compromiso contractual. El coste de un spike sobre 2 unidades es menor que el coste de descubrir problemas en E3 (saneamiento de 10 unidades con shape mal cerrado).
- **E4 dividida en E4a + E4b**: la capa de relaciones depende de que la proyección y la validación cruzada hayan madurado. Diseñarla sobre datos aún sucios produciría un shape mal calibrado.

> **Decisión a tomar / Estado actual de la Parte H:**
>
> - Plan de 5 etapas (E1, E1.5, E2, E3, E4a, E4b) — ✅ propuesto y razonado.
> - **Validar:** que el plan es razonable y sin huecos. Aprobación necesaria antes de pasar a implementación.

---

# Parte I — Estado del repo (referencia, sin decisión)

> **Propósito:** dar al lector el contexto técnico del repo en el momento de redactar este documento. No se decide nada — es solo punto de referencia para entender de dónde se parte.

---

## §10 — Estado actual del repo (referencia para el revisor)

- HEAD: `addf5b1` (v10.110 — pasada C de claridad cerrada).
- Working tree: solo este documento + `fases/2-reciclaje/REDISEÑO-EN-CURSO.md` (ambos artefactos locales untracked).
- Fase 1: canon léxico activado en rollout R1, validador con 3 canales operativo.
- Fase 2: oficialmente pausada desde v10.108d, scripts viejos inertes por defecto.

> **Estado de la Parte I:** referencia. No requiere decisión.

---

# Parte J — Renegociaciones con el repo vigente

> **Propósito:** identificar explícitamente las decisiones vigentes del repo que entran en conflicto con esta propuesta y planificar cómo se renegocian. La aprobación de la propuesta NO basta — cada conflicto necesita commit dedicado en la etapa correspondiente. Esta parte garantiza trazabilidad y evita arrastre silencioso.

---

## §11 — Conflictos con decisiones vigentes a renegociar explícitamente

Si esta propuesta se aprueba, **NO puede entrar por arrastre**. Cuatro decisiones vigentes del repo entran en conflicto y deben renegociarse de forma explícita, con commit dedicado y referencia cruzada a esta propuesta:

### §11.1 — Pausa formal de fase 2 y congelado de `nc1-reciclaje.json`

**Decisión vigente:**
- `README.md:157` declara fase 2 pausada y `nc1-reciclaje.json` congelado.
- `REVIEW.md:48` repite la pausa en el estado de bloque B.
- `PROCESO-MAESTRO.md:661` (decisión 36) declara la pausa hasta cerrar canon de fase 1.
- `integrar_unidad.py:9` documenta que la regeneración del reciclaje queda detrás del flag `--regenerar-reciclaje` mientras dure la pausa.

**Conflicto con la propuesta:** la fase 2 se reactiva con un nuevo pipeline (capas 1, 2, 3). El reciclaje deja de estar "congelado" y pasa a ser "regenerable desde el modelo nuevo".

**Acción de renegociación:** en el batch de E2 (reescritura contractual), reformular explícitamente:
- `README.md:157` → "fase 2 reactivada con modelo nuevo según decisión X de PROCESO-MAESTRO".
- `REVIEW.md:48` → estado de bloque B actualizado.
- `PROCESO-MAESTRO.md` → entrada formal nueva que **supera** la decisión 36, con justificación.
- `integrar_unidad.py` → revisar si el flag `--regenerar-reciclaje` sigue teniendo sentido o cambia de semántica (ver §11.4).

### §11.2 — Contrato actual de fase 2 basado en mapa + auto

**Decisión vigente:**
- `fases/2-reciclaje/CLAUDE.md:5` describe el contrato actual: scripts `regenerar_reciclaje_mapa.py` + `regenerar_reciclaje_vocabulario.py` proyectando desde `nc1-curso.json` y `vocabulario_consolidado`.
- `fases/2-reciclaje/reglas-reciclaje.md` documenta la lógica vigente.

**Conflicto con la propuesta:** el nuevo modelo de fase 2 no es mapa + auto. Es:
- Capa 1: validación cruzada con autoridad formal (`validar_inventarios_cross.py`).
- Capa 2: proyección con taxonomía nueva de 5 tipos.
- Capa 3: relaciones en artefacto separado (`nc1-relaciones.json`).

**Acción de renegociación:** en E4a, **reescribir completamente** `fases/2-reciclaje/CLAUDE.md` y `reglas-reciclaje.md`. Los scripts viejos (`regenerar_reciclaje_mapa.py`, `regenerar_reciclaje_vocabulario.py`) se sustituyen por los nuevos. Conservarlos como referencia histórica en `docs/historico/` si la trazabilidad lo justifica.

### §11.3 — Taxonomía vigente que colapsa pronunciación dentro de gramática

**Decisión vigente:**
- `scripts/regenerar_reciclaje_mapa.py:29` mapea `pronunciacion_ortografia` (de `nc1-curso.json`) hacia hilos de tipo `contenido_gramatical`. Lo absorbe.
- Esto da un `nc1-reciclaje.json` con tipos `vocabulario` + `contenido_gramatical` + `estrategia` (3 tipos, sin separación gramática/pronunciación).

**Conflicto con la propuesta:** la nueva taxonomía es de **5 tipos explícitos**: `vocabulario`, `tiempos_y_verbos`, `gramatica`, `pronunciacion_ortografia`, `estrategia`. La pronunciación deja de estar absorbida.

**Acción de renegociación:** en E4a, el nuevo script de proyección de fase 2 emite los 5 tipos directos. `pronunciacion_ortografia` deja de colapsar dentro de `contenido_gramatical`. Es cambio funcional con migración del JSON existente (los 39 hilos `contenido_gramatical` actuales se redistribuyen entre `gramatica` y `pronunciacion_ortografia` según contenido).

### §11.4 — Semántica del flag `--regenerar-reciclaje` en `integrar_unidad.py`

**Decisión vigente:**
- `integrar_unidad.py:35` documenta el flag `FLAG_REGENERAR_RECICLAJE` como mecanismo opcional para regenerar el reciclaje en una integración concreta mientras dure la pausa de fase 2.
- Mientras la pausa esté activa, regenerar es la excepción consciente.

**Conflicto con la propuesta:** si fase 2 vuelve a ser activa con un nuevo pipeline, el flag pierde su sentido de "excepción durante pausa". Tendría dos posibles destinos:
- (a) **Eliminarse**: el reciclaje vuelve a regenerarse siempre al integrar una unidad (comportamiento pre-v10.108d). Más simple, encaja con fase 2 activa.
- (b) **Resemantizarse**: el flag pasa a indicar regeneración completa (capas 1+2+3) vs regeneración mínima (solo proyección, capa 2). Útil si la capa 3 es costosa.

**Acción de renegociación:** decisión a tomar en E4a o E4b según cómo evolucionen los costes computacionales de las capas. Lo importante: declarar explícitamente la nueva semántica del flag o su eliminación, con commit dedicado y entrada en PROCESO-MAESTRO.

### §11.5 — Resumen de renegociaciones

| Conflicto | Archivos a renegociar | Etapa |
|---|---|---|
| Pausa fase 2 y congelado reciclaje | `README.md`, `REVIEW.md`, `PROCESO-MAESTRO.md` (decisión 36), `integrar_unidad.py` | E2 |
| Contrato actual fase 2 (mapa + auto) | `fases/2-reciclaje/CLAUDE.md`, `fases/2-reciclaje/reglas-reciclaje.md`, scripts viejos | E4a |
| Taxonomía colapsada (3 tipos) | Migración de `nc1-reciclaje.json` actual (3 tipos → 5 tipos) | E4a |
| Flag `--regenerar-reciclaje` | `integrar_unidad.py`, PROCESO-MAESTRO | E4a o E4b |

**Cada renegociación es commit dedicado**, no entra como cambio incidental en otro batch. Esto preserva trazabilidad y evita la regresión doc que ya hemos visto antes (v10.99e/f/g, v10.108c, etc.).

> **Decisión a tomar / Estado actual de la Parte J:**
>
> - 4 conflictos identificados con plan de renegociación.
> - **Validar:** que los 4 son los únicos conflictos vigentes que entran en conflicto con la propuesta. Si falta alguno, ampliar la lista.

---

# Cierre del documento

## §12 — Estado y preguntas residuales al revisor

Tras el dictamen del revisor sobre las 8 piezas estructurales (todas cerradas, con enmiendas integradas en §3-§6 y reflejadas en la tabla §8), quedan estas cuestiones abiertas:

1. **¿El cambio de naturaleza de fase 1 declarado en §2.1** (de "extracción + normalización ligera" a "extracción + modelado lingüístico completo") tiene alguna implicación que no se haya considerado, más allá de las actualizaciones documentales obligatorias listadas (`CLAUDE.md:28`, `schema-inventario.md:1`, PROCESO-MAESTRO, REVIEW)?

2. **¿El cierre como entrada plana del bloque verbal** (§E del diccionario y §4) resuelve la objeción del revisor sobre jerarquía profunda como shape de inventario unitario? ¿Detecta alguna pieza de la metadata original que se pierda al aplanar?

3. **¿La lista cerrada de gramática propuesta** (clases de palabra + contenidos estructurales como concordancia) requiere especificación más detallada antes de implementar, o basta con cerrar el alcance conceptual y fijar la lista exacta durante el batch de implementación?

4. **¿La arquitectura de registries paralelos del canon** (§5: canon léxico intacto + 3 archivos nuevos hermanos, reutilizando `scripts/canon.py`) tiene coste oculto en mantenimiento, o es la forma que el revisor tenía en mente?

5. **¿El plan revisado de 5 etapas (E1, E1.5 spike, E2, E3, E4a, E4b)** queda definitivamente cerrado, o falta algún ajuste de secuencia antes de pasar a implementación?

6. **¿La decisión de eliminar `contenido_linguistico` y `campo_semantico`** tiene algún coste oculto que merezca preservar parcialmente alguno de los dos?

7. **Los 4 conflictos identificados en §11 y su plan de renegociación** ¿están completos? ¿Falta algún conflicto adicional que se haya pasado por alto?

8. **¿El refinamiento de pieza 9 (trazabilidad bidireccional con campo `fuentes`)** cumple la objeción del revisor sobre "el sistema duplicará información sin poder comprobar coherencia"? ¿Detecta algún coste oculto del shape extendido `{categoria: {palabras, fuentes}}` para los bloques consolidados léxicos?

---

Esperando dictamen sobre estos puntos residuales antes de pasar a implementación (etapa E2).

---

## §13 — Cierre de cuestión 1 (validada por revisor 2026-05-11)

**Veredicto del revisor:** "el documento ha pasado el umbral de consistencia interna para esta cuestión. La primera cuestión puede darse por cerrada a nivel arquitectónico."

**Trazabilidad del cierre — pasadas aplicadas tras dictamen profundo del revisor:**

1. **Pasada de saneamiento de 6 contradicciones internas:**
   - Modelo verbal unificado como plano por entrada verbal (§4 línea 359, §8 pieza 2, §9 línea 657).
   - Canon unificado en arquitectura de registries paralelos (§5 alcance + forma, §9 plan de impacto). Eliminada la bifurcación "ampliado a 4 tipos o sustituido por 4 archivos".
   - Enum de `destreza` alineado con `schema-inventario.md:185-191` (`mediacion` en lugar del erróneo `interaccion_escrita`).
   - Autoridad de los top-level vuelve a fase 1 (§9 plan de impacto fase 1 + fase 2 explícita como consumidora).
   - Invariante 3 limpiada (`reglas_foneticas` retirado del ejemplo).
   - Tabla de cierre corregida (17 piezas, no 13; pieza 3 reclasificada en ámbar).

2. **Pasada de 3 ajustes de precisión exigidos por el revisor:**
   - Objeto verbal contractualizado por campo (§7 regla 1): `lema` y `tiempo` canónicos; `formas_trabajadas` literal del libro con validación por paradigma.
   - Registry verbal descrito como plano en §5 (no jerárquico).
   - Pieza 1 de §8 corregida: "doble fuente: actividades + cuadros" con `fuentes` obligatorio.

**Riesgos residuales reconocidos (no contradicciones — riesgos normales de implementación):**

- Pieza 3 cerrada el 2026-05-11 con matriz + lista + excepciones en §14.
- Validación de `formas_trabajadas` contra paradigma: operabilidad real se prueba en el spike E1.5.
- Propagación de los cambios a los contratos vivos (`schema-inventario.md`, `reglas-operativas.md`, `prompt.md`, `validar_inventario.py`, `PROCESO-MAESTRO.md`, `REVIEW.md`, `CHANGELOG.md`): pertenece a E2, no a esta cuestión.

**Política de operativa hasta cerrar el documento completo:** mientras quedan cuestiones abiertas (2, 3, …), todas las decisiones viven **solo** en este documento. No se tocan CHANGELOG, REVIEW, PROCESO-MAESTRO, schema, reglas-operativas, prompt ni validador. Una sola pasada de propagación al final, cuando todas las cuestiones estén validadas.

---

## §14 — Pieza 3 (registry gramatical) — REABIERTA Y REVISADA 2026-05-12

> **AVISO IMPORTANTE — cambio de enfoque tras revisión 2026-05-12:**
>
> La pieza 3 fue cerrada el 2026-05-11 con una **lista resumida de 15 categorías** derivada solo de `gramatica[]` de `nc1-curso.json`. Esa decisión resultó **demasiado gruesa y excluyó categorías que SÍ están en PCIC A1** (pronombres personales, conjunciones copulativas/disyuntivas, adverbios de afirmación/negación, etc.).
>
> **Decisión revisada 2026-05-12:** la lista de 15 categorías de pieza 3 queda como **scaffold conceptual de alto nivel**, NO como enum cerrado vinculante. Las categorías reales del registry gramatical se toman de **PCIC A1**, no de pieza 3.
>
> La sección §14.2 con las 15 categorías "finales" del 2026-05-11 se conserva más abajo como **registro histórico del primer intento** (estado superado), pero no es vinculante. El registry real se materializará a partir de PCIC.

### §14.0 — Estrategia híbrida vigente (decisión 2026-05-12)

**Fuente vinculante del registry gramatical:** `fases/1-extraccion-inventario/pcic-a1-gramatica.json` (copia local del Plan Curricular del Instituto Cervantes, sección Gramática A1, 15 categorías principales con varias subcategorías y contenidos generales más finos).

**Procedimiento para asignar categoría a un contenido gramatical detectado en una unidad:**

1. **Scaffold de alto nivel** — pieza 3 §14.2 (lista de 15) sirve como mapa conceptual orientativo: artículos, demostrativos, posesivos, pronombres, interrogativos, conjunciones, preposiciones, adverbios, concordancia, etc.
2. **Resolución específica con PCIC** — para cada contenido detectado, el sistema baja al árbol de PCIC y elige la **categoría más específica que aplique**. Ejemplos:
   - `yo`, `tú`, `él`... → PCIC §7.1.1 `Pronombre sujeto`.
   - `y` → PCIC §14.1 `Copulativas`.
   - `o` → PCIC §14.2 `Disyuntivas`.
   - `sí`, `no` → PCIC §8 `Adverbios de afirmación y negación`.
   - `muy` (intensificador) → PCIC §8 `Cuantificadores comparativos / intensificadores`.
   - `el`, `la`, `los`, `las` → PCIC §3.1 `El artículo definido`.
3. **Naming** — el nombre de la categoría en el JSON consolidado es el nombre PCIC tal cual o adaptado mínimamente para legibilidad. Se documenta el código PCIC en la descripción.
4. **Fallback** — si el contenido no encaja en ninguna categoría PCIC A1, marcar con `_pendiente_canon` y escalar al autor (regla 5).

**Forma del registry resultante:** diccionario `{categoria_PCIC: [items_canonicos]}`. Mismas reglas de shape que antes (regla 10: cada item con sus fuentes; regla 13: cada categoría con descripción PCIC por unidad).

---

### §14.1 — [REGISTRO HISTÓRICO 2026-05-11] Matriz de cobertura cruzada contra `gramatica[]` de `nc1-curso.json`

> **Estado:** superada por §14.0 (estrategia híbrida vigente). Se conserva como trazabilidad del primer intento. La matriz sigue siendo útil para entender qué entradas del índice editorial mapean a qué bloque del modelo (verbal, gramática, léxico, ortografía), pero las categorías destino se renombran ahora siguiendo PCIC (ver §14.0).

Las 32 entradas del índice editorial cubiertas, con destino y motivo explícitos:

| Unidad | Entrada del índice | Registry destino | Canónico final | Motivo |
|---|---|---|---|---|
| U1 | Verbos ser, llamarse y tener (singulares) | verbal | `ser`, `llamarse`, `tener` | Paradigma → verbal |
| U1 | Artículos determinados (el, la, los, las) | gramatical | `Artículos determinados → [el, la, los, las]` | Nombre del índice respetado |
| U1 | Masculino y femenino | gramatical | `Concordancia de género → [masculino, femenino]` | Renombrado por claridad descriptiva (decisión declarada) |
| U1 | Colores | léxico | (registry léxico) | Contenido léxico, no gramatical |
| U2 | Verbos ser y tener (plurales) | verbal | `ser`, `tener` (amplía paradigma) | Paradigma → verbal |
| U2 | Plural de nombres y adjetivos | gramatical | `Concordancia de número → [singular, plural]` | Renombrado (decisión declarada) |
| U2 | Demostrativos | gramatical | `Demostrativos → [este, esta, estos, estas]` | Granularidad calibrada al libro: U2 solo serie *este* |
| U2 | Uso de las mayúsculas | pronunciación/ortografía | (registry orto) | Contenido ortográfico |
| U3 | Presente de los verbos regulares | verbal | (rasgo "regular" + lemas) | Paradigma → verbal |
| U3 | Interrogativos | gramatical | `Interrogativos → [qué, quién, quiénes, dónde, cuándo, cómo, cuánto/-a/-os/-as, cuál, cuáles, con quién, por qué]` | Calibrado: `cuál` por índice/cuadro U3, `cuáles` por flexión productiva, `por qué` por evidencia de actividad (ver §14.3) |
| U3 | Posesivos | gramatical | `Posesivos → [mi, tu, su, nuestro/-a, vuestro/-a, mis, tus, sus, nuestros/-as, vuestros/-as]` | Desglose estándar A1 |
| U4 | Verbo gustar | verbal + gramatical | verbal: `gustar` · gramatical: `Construcción gustar/doler` | Doble dimensión (cuestión 1) |
| U4 | Artículos indeterminados (un, una, unos, unas) | gramatical | `Artículos indeterminados → [un, una, unos, unas]` | Nombre del índice respetado |
| U4 | Nombres contables e incontables | gramatical | `Nombres contables e incontables → [contable, incontable]` | Sin cambio |
| U4 | Hay | gramatical | `Hay → [hay]` | Nombre del índice respetado. Va a gramatical (no se enseña paradigma de *haber*) |
| U4 | Verbo querer | verbal | `querer` | Paradigma → verbal |
| U5 | Verbo estar | verbal | `estar` | Paradigma → verbal |
| U5 | Posición: encima, debajo, detrás, delante, al lado | gramatical | `Posición → [encima, debajo, detrás, delante, al lado]` | Nombre del índice respetado (no "Adverbios de lugar") |
| U5 | Oposición ser / estar | gramatical | `Oposición ser / estar → [ser (identidad, características), estar (ubicación, estado)]` | Punto gramatical, no morfología |
| U6 | Presente de irregulares: cerrar, ir, venir, hacer, jugar, dormir | verbal | 6 lemas | Paradigma → verbal |
| U6 | Imperativo (tú) | verbal | (tiempo `Imperativo` + lemas) | Paradigma → verbal |
| U7 | Verbos reflexivos: ducharse, acostarse, sentarse, ponerse, vestirse | verbal | 5 lemas | Paradigma → verbal |
| U7 | Oposición salir / volver | verbal | `salir`, `volver` (rasgo "oposición léxica") | Contraste de uso, no construcción gramatical |
| U7 | Preposiciones: a, de, por, con, en | gramatical | `Preposiciones → [a, de, por, con, en]` | Sin cambio |
| U8 | Verbo doler: Me duele la cabeza / Me duelen los pies | verbal + gramatical | verbal: `doler` · gramatical: `Construcción gustar/doler` (extiende) | Doble dimensión |
| U8 | Verbos doler y gustar | gramatical (consolidación) | (referencia repetida a `Construcción gustar/doler`) | Repaso, no nueva entrada |
| U8 | Adverbios de cantidad | gramatical | `Adverbios de cantidad → [muy, mucho, bastante, un poco, nada]` | Política "items enseñados" (ver §14.3) |
| U8 | Muy, mucho/-a/-os/-as | gramatical (**fusionado**) | (absorbido en `Adverbios de cantidad`) | Decisión de normalización declarada: dos entradas paralelas del mismo punto pedagógico |
| U9 | Pretérito indefinido de ir y estar | verbal | `ir`, `estar` (tiempo `Pretérito indefinido`) | Paradigma → verbal |
| U9 | Marcadores temporales del pasado: ayer por la mañana, el año pasado, hace una... | gramatical | `Marcadores temporales del pasado → [ayer, ayer por la mañana, el año pasado, hace + tiempo]` | Sin cambio |
| U9 | Interrogativos: dónde, qué, cuándo, quién, con quién | gramatical | (amplía `Interrogativos`: añade `con quién`) | No nueva categoría — amplía la de U3 |

**Cobertura:** 32/32 entradas con destino explícito. Cero categorías sin respaldo en índice o evidencia de inventario.

### §14.2 — [REGISTRO HISTÓRICO 2026-05-11] Lista de 15 categorías (superada)

> **Estado:** superada por §14.0 (estrategia híbrida vigente). Esta lista resumida queda como **scaffold conceptual**, no como enum cerrado vinculante. Las categorías reales del registry vienen de PCIC A1 — pueden ser más finas (p. ej. PCIC §3.1 "El artículo definido" en vez de "Artículos determinados"; PCIC §7.1.1 "Pronombre sujeto" sí existe aunque pieza 3 no la incluía).

```jsonc
"gramatica-canonica.json": {
  "Artículos determinados": ["el", "la", "los", "las"],
  "Artículos indeterminados": ["un", "una", "unos", "unas"],
  "Demostrativos": ["este", "esta", "estos", "estas"],
  "Posesivos": ["mi", "tu", "su", "nuestro/-a", "vuestro/-a", "mis", "tus", "sus", "nuestros/-as", "vuestros/-as"],
  "Interrogativos": ["qué", "quién", "quiénes", "dónde", "cuándo", "cómo", "cuánto/-a/-os/-as", "cuál", "cuáles", "con quién", "por qué"],
  "Preposiciones": ["a", "de", "por", "con", "en"],
  "Posición": ["encima", "debajo", "detrás", "delante", "al lado"],
  "Adverbios de cantidad": ["muy", "mucho", "bastante", "un poco", "nada"],
  "Marcadores temporales del pasado": ["ayer", "ayer por la mañana", "el año pasado", "hace + tiempo"],
  "Concordancia de género": ["masculino", "femenino"],
  "Concordancia de número": ["singular", "plural"],
  "Nombres contables e incontables": ["contable", "incontable"],
  "Hay": ["hay"],
  "Construcción gustar/doler": ["me/te/le/nos/os/les + gusta(n)", "me/te/le/nos/os/les + duele(n)"],
  "Oposición ser / estar": ["ser (identidad, características)", "estar (ubicación, estado)"]
}
```

15 categorías.

### §14.3 — Excepciones y normalizaciones de ítem

1. **`por qué` en `Interrogativos`** — entra **por evidencia de actividades/cuadros**, no por `gramatica[]` de `nc1-curso.json`. Aparece trabajado en `U9-nc1-inventario.json:618`. Marcado como excepción documentada hasta que E1.5 lo confirme o lo retire.

2. **`cuál/cuáles` en `Interrogativos`** — `cuál` (singular) entra por índice editorial + cuadro de U3 (`U3-nc1-inventario.json:34`). `cuáles` (plural) se admite por **flexión productiva y ocurrencias de uso** (`U9-nc1-inventario.json:546` y otras). `quién/quiénes` no usa este criterio: ambos están explícitamente presentes en material e índice editorial.

3. **`Adverbios de cantidad` — política "items enseñados"** (no "lemas/realizaciones canónicas"). La lista refleja lo que el libro presenta en U8 (`U8-nc1-inventario.json:29`, `:801`): `["muy", "mucho", "bastante", "un poco", "nada"]`. Las flexiones de *mucho* (`mucha`/`muchos`/`muchas`) no se enumeran como entradas separadas — se asumen por concordancia, fenómeno ya cubierto por `Concordancia de género`/`Concordancia de número`.

4. **Fusión U8** — `Muy, mucho/-a/-os/-as` se absorbe dentro de `Adverbios de cantidad`. El índice presenta dos entradas paralelas del mismo punto pedagógico — la segunda enumera los items concretos de la primera.

5. **Renombrados respecto al índice** (declarados, no implícitos):
   - `Masculino y femenino` → `Concordancia de género` (claridad descriptiva del fenómeno).
   - `Plural de nombres y adjetivos` → `Concordancia de número` (idem).
   - El resto de categorías mantiene el naming literal del índice (`Artículos determinados`, `Artículos indeterminados`, `Hay`, `Posición`, etc.).

6. **`Conjunciones` retirada** de la lista candidata inicial. No aparece en `gramatica[]` de `nc1-curso.json`. Si E1.5 detecta contenido trabajado en actividades concretas, se reabre como excepción (regla 3 de la jerarquía de naming).

### §14.4 — Doble dimensión verbal + gramatical

Un verbo puede aparecer simultáneamente en `verbos-canonicos.json` (como lema con paradigma) y en `gramatica-canonica.json` (como construcción). No es redundancia: dos dimensiones del mismo verbo (morfología vs estructura/función).

- **Casos de doble dimensión confirmados** (paradigma en verbal + construcción en gramatical): `ser`, `estar`, `gustar`, `doler`.
- **Caso gramatical sin paradigma verbal en NC1**: `haber` aparece **solo** en `gramatica-canonica.json` como `Hay → [hay]`. NC1 no enseña el paradigma de *haber*, por lo que no figura en `verbos-canonicos.json`. Si en una unidad futura se enseñara el paradigma, se añadiría al verbal y entraría en doble dimensión.

> **Nota:** la "doble dimensión" se generaliza en §15.8 como **regla** (no excepción) para cualquier verbo trabajado con explicación pedagógica concreta en el libro. Esta sección §14.4 documenta los casos confirmados hasta el cierre de pieza 3; la lista se amplía durante la extracción exhaustiva de pieza 2.

---

## §15 — Cierre de pieza 2 (diseño del registry verbal, 2026-05-11)

**Estado:** diseño cerrado. Materialización (JSON poblado) pendiente de extracción exhaustiva de las 423 actividades de U0-U9.

### §15.1 — Forma del registry — bloques paralelos

```jsonc
"verbos-canonicos.json": {
  "verbos":           { /* lemas con metadata, §15.2 */ },
  "tiempos_verbales": { /* enum cerrado, §15.3 */ },
  "perifrasis":       { /* enum cerrado, §15.4 */ },
  "usos_por_tiempo":  { /* metadata pedagógica por unidad, §15.5 */ }
}
```

**Tiempos verbales y perífrasis viven en bloques separados** (decisión del autor): las perífrasis no son tiempos; tienen su propio registro paralelo.

### §15.2 — Bloque `verbos` — cada lema vive una sola vez (revisado 2026-05-12)

Cada lema es un objeto con cinco campos:

```jsonc
"hacer": {
  "tipo_de_verbo": ["transitivo"],
  "tiempos": ["Presente", "Pretérito indefinido", "Imperativo"],
  "rasgo_por_tiempo": {
    "Presente": "irregularidad 1ª persona",
    "Pretérito indefinido": "raíz irregular",
    "Imperativo": "irregular (haz)"
  },
  "lo_que_se_trabaja": {
    "U6": "paradigma del Presente + forma imperativa tú (haz)"
  },
  "apariciones": {
    "U6": ["PRE", "IMP"]
  }
}
```

```jsonc
"ducharse": {
  "tipo_de_verbo": ["reflexivo"],
  "tiempos": ["Presente"],
  "rasgo_por_tiempo": {
    "Presente": "regular -ar"
  },
  "lo_que_se_trabaja": {
    "U7": "paradigma del Presente con pronombre reflexivo (me ducho, te duchas, ...)"
  },
  "apariciones": {
    "U7": ["PRE"]
  }
}
```

- **`tipo_de_verbo`** (lista) — clasificación **sintáctica/gramatical** del verbo. Enum cerrado: `transitivo`, `intransitivo`, `reflexivo`, `pronominal`, `impersonal`, `copulativo`, `tipo gustar`. Un verbo puede tener varios tipos a la vez (ej: `ser` = `copulativo, intransitivo`). **Sustituye al antiguo booleano `reflexivo`** (decisión 2026-05-12): `reflexivo` deja de ser marca ortogonal y pasa a ser uno de los valores posibles de este enum, junto con los otros tipos de verbo.
- **`tiempos`** (lista) — los tiempos verbales donde el lema se conjuga en NC1. Enum cerrado: `Presente`, `Pretérito indefinido`, `Imperativo`, más `Perífrasis` cuando el verbo participa en una.
- **`rasgo_por_tiempo`** — clasificación **morfológica** (cómo se comporta el verbo) por cada tiempo. Un mismo lema puede tener rasgo distinto en Presente / Indefinido / Imperativo (ej: `ser` es `totalmente irregular` en Presente y comparte paradigma con `ir` en Indefinido).
- **`lo_que_se_trabaja`** (diccionario por unidad) — **texto libre** descriptivo de qué aspecto del verbo se practica en cada unidad. Lo redacta Claude Code o el agente extractor durante fase 1. Ejemplos: `"formas singulares"`, `"paradigma completo"`, `"construcción me/te/le + V"`, `"contraste con estar"`. No hay enum cerrado.
- **`apariciones`** — datos crudos: en qué unidad aparece y bajo qué códigos de tiempo (`PRE`, `IND`, `IMP`, `PER`). **Sin etiqueta pedagógica** (eso vive en fase 2; ver §15.10).

### §15.3 — Enum cerrado de `tiempos_verbales` (3 valores en NC1)

```
Presente
Pretérito indefinido
Imperativo
```

`Infinitivo` y `Participio` **no entran** como tiempos del enum: son formas no personales sin uso propio en NC1 fuera de perífrasis.

> **Decisión revisada (2026-05-12):** `Infinitivo` **sí entra** como valor del enum para cubrir la categoría "forma no personal del verbo" cuando se trabaja pedagógicamente fuera de perífrasis (listas de verbos en infinitivo, ejercicios de identificación, etc.). `Participio` y `Gerundio` siguen fuera del enum por inexistencia en el corpus NC1. Si NC2 los introduce, se amplían por expansión controlada. Ver `schema-inventario.md` §5d y Apéndice transitorio §A.3.

### §15.4 — Enum cerrado de `perifrasis` (candidatos para NC1, a verificar en extracción)

```
ir a + infinitivo     → "Expresar futuro próximo o inmediato"
querer + infinitivo   → "Expresar deseo o intención"
poder + infinitivo    → "Expresar posibilidad o permiso"
```

`tener que + infinitivo` queda pendiente: no aparece en `gramatica[]` del índice. Se incorpora solo si la extracción lo encuentra trabajado.

### §15.5 — Bloque `usos_por_tiempo` — metadata del tiempo, no del lema

Los usos canónicos por tiempo se declaran a nivel del tiempo y se marca en qué unidad se trabaja cada uno. **No se asocian al lema individual.**

```jsonc
"usos_por_tiempo": {
  "Presente": {
    "U1": ["Presente caracterizador o descriptivo"],
    "U3": ["Presente actual", "Presente habitual"]
  },
  "Pretérito indefinido": {
    "U9": ["Acciones puntuales y terminadas en el pasado"]
  },
  "Imperativo": {
    "U6": ["Dar instrucciones", "Dar consejos"]
  }
}
```

### §15.6 — Taxonomía canónica de usos por tiempo (filtrada a NC1)

Fuentes consultadas: RAE / Nueva gramática básica · marcoELE · ProfedeELE · DeleAhora · HablaCultura.

**Presente** — la tradición ELE distingue 8 valores: `actual`, `habitual`, `caracterizador o descriptivo`, `gnómico`, `histórico`, `narrativo`, `prospectivo`, `de mandato`. NC1 A1.1 trabaja únicamente:

```
Presente actual
Presente habitual
Presente caracterizador o descriptivo
```

(Se descartan `gnómico`, `histórico`, `narrativo coloquial`, `prospectivo` con valor de futuro puro y `de mandato` — propios de niveles B. El "presente prospectivo" con `ir a + inf` no entra aquí: vive en `perifrasis`.)

**Pretérito indefinido** — la tradición ELE distingue 3 valores: `acciones puntuales y terminadas`, `secuenciación narrativa`, `acciones habituales delimitadas`. NC1 U9 trabaja únicamente:

```
Acciones puntuales y terminadas en el pasado
```

**Imperativo** — la tradición ELE distingue 4 valores: `dar órdenes`, `dar instrucciones`, `dar consejos`, `hacer peticiones`. NC1 U6 trabaja únicamente:

```
Dar instrucciones
Dar consejos
```

### §15.7 — Códigos de tiempo en `apariciones` (enum cerrado de 4)

```
PRE = Presente
IND = Pretérito indefinido
IMP = Imperativo
PER = Perífrasis
```

Son **datos crudos** sin interpretación. Fase 2 etiqueta sobre ellos con enum cerrado de 5 acciones pedagógicas (`introduce`, `amplía`, `aplica`, `sistematiza`, `contrasta` — no hay "otra"). Esa capa **no vive en fase 1**.

### §15.8 — Categorías morfológicas por tiempo (enums cerrados de `rasgo_por_tiempo`)

**Presente** (9 categorías):
- `regular -ar` · `regular -er` · `regular -ir`
- `irregularidad vocálica e→ie` · `irregularidad vocálica o→ue` · `irregularidad vocálica e→i`
- `irregularidad 1ª persona`
- `totalmente irregular`
- `tipo gustar`

**Pretérito indefinido** (4 categorías):
- `regular`
- `raíz irregular` (`tener`, `hacer`, `estar`)
- `totalmente irregular (mismo paradigma ser/ir)`
- `ortográfico / ver, dar`

**Imperativo (tú)** (2 categorías):
- `regular 2ª persona singular`
- `irregular` (`haz`, `ve`, `ven`, `pon`, `sal`, `di`, `sé`, `ten`)

**Sobre reflexivo:** **decisión 2026-05-12: el booleano `reflexivo` se elimina del modelo**. `reflexivo` pasa a ser uno de los valores del enum `tipo_de_verbo` (junto con `transitivo`, `intransitivo`, `pronominal`, `impersonal`, `copulativo`, `tipo gustar`). Reflexivo no es categoría morfológica; es clasificación sintáctica.

### §15.9 — Doble dimensión sistemática (regla general, no excepción)

Cualquier verbo trabajado en el libro con **explicación pedagógica concreta** (uso, oposición, construcción) debe estar referenciado **simultáneamente** en:

- `verbos-canonicos.json` — como lema con su paradigma.
- `gramatica-canonica.json` — como punto gramatical (construcción, oposición, función).

**Verbos confirmados con doble dimensión hasta U9:** `ser`, `estar`, `haber` (`hay`), `gustar`, `doler`, `querer`, `ir`. La extracción exhaustiva puede sumar más.

Esto **generaliza la decisión que pieza 3 dejó como caso particular** (`gustar`/`doler`/oposición `ser/estar`): la doble dimensión deja de ser excepción y pasa a ser **regla cuando hay explicación pedagógica en el libro**.

### §15.10 — Política de ingreso al registry — exhaustiva

Decisión: **opción B (exhaustiva)** — pasada completa por las 423 actividades de U0-U9 para extraer todos los verbos trabajados:

- Lemas explícitos del índice (`gramatica[]` con etiqueta "Verbo X" / "Tiempo X").
- Verbos regulares trabajados sin nombre en el índice (los que U3 enseña como "presente de los verbos regulares" — `hablar`, `comer`, `vivir`, `estudiar`, `merendar`, `trabajar`, etc.).
- Cualquier otro verbo que aparezca en actividades o cuadros del libro.

**Justificación:** igual que pieza 3 cerró con matriz cruzada de las 32 entradas de `gramatica[]`, pieza 2 cierra con matriz cruzada de **todos los verbos** extraídos de inventarios. Sin extracción exhaustiva el registry no tiene cierre real.

**Resultado:** `verbos-canonicos.json` poblado + matriz cruzada de cobertura que se anexa a este documento como §15.11 cuando la extracción concluya.

### §15.11 — Límite explícito fase 1 / fase 2

| Capa | Fase |
|---|---|
| Lemas + clasificación morfológica + `reflexivo` + `apariciones` por unidad con código de tiempo | **Fase 1** (este registry) |
| Usos canónicos por tiempo declarados por unidad | **Fase 1** (en `usos_por_tiempo`) |
| Etiquetas pedagógicas `introduce / amplía / aplica / sistematiza / contrasta` sobre las apariciones | **Fase 2** (análisis) |
| Relaciones cross-unidad (progresión, redes de coocurrencia, contraste de verbos) | **Fase 2** (capa 3 del pipeline) |
| Modal / UI que cruza usos por unidad con tabla de verbos | **Fase 2** (vista del dashboard) |

### §15.12 — Estado y siguiente paso operativo

- **Diseño:** ✅ cerrado el 2026-05-11.
- **Materialización:** ✅ cerrada el 2026-05-11 con extracción base (ver §15.13). El JSON poblado vive en `fases/1-extraccion-inventario/verbos-canonicos.json`. Cualquier ajuste fino se hace por edición incremental sobre ese archivo.
- **Política de operativa preservada:** los cambios viven solo en este documento hasta cerrar todas las cuestiones. CHANGELOG, REVIEW, PROCESO-MAESTRO, schema, reglas-operativas, prompt y validador se actualizan en una sola pasada al final.

### §15.13 — Materialización: extracción de verbos por categoría morfológica

**Fuente de extracción:** `vocabulario_consolidado` de U0-U9 + `gramatica[]` del índice editorial (`nc1-curso.json`) + imperativos de aula trabajados en U6.

**Total: 48 lemas** (13 reflexivos).

#### Regulares -ar (20)

| Lema | Reflexivo | Apariciones |
|---|---|---|
| `afeitarse` | sí | U7=PRE |
| `ahorrar` | no | U5=PRE |
| `bañarse` | sí | U7=PRE |
| `completar` | no | U6=IMP |
| `contaminar` | no | U5=PRE |
| `contestar` | no | U6=IMP |
| `deslizarse` | sí | U8=PRE |
| `ducharse` | sí | U7=PRE |
| `escuchar` | no | U6=IMP |
| `estudiar` | no | U3=PRE |
| `hablar` | no | U3=PRE, U6=IMP |
| `lavarse` | sí | U7=PRE |
| `levantarse` | sí | U7=PRE |
| `llamar` | no | U7=PRE |
| `llamarse` | sí | U1=PRE |
| `llegar` | no | U7=PRE |
| `mirar` | no | U6=IMP |
| `preguntar` | no | U6=IMP |
| `quedarse` | sí | U7=PRE |
| `trabajar` | no | U3=PRE |

#### Regulares -er (3)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `comer` | no | U3=PRE |
| `leer` | no | U1=PRE, U3=PRE, U6=IMP |
| `responder` | no | U6=IMP |

#### Regulares -ir (3)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `abrir` | no | U6=IMP |
| `escribir` | no | U3=PRE, U6=IMP |
| `vivir` | no | U3=PRE |

#### Irregularidad vocálica e→ie (5)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `cerrar` | no | U6=PRE |
| `despertarse` | sí | U7=PRE |
| `merendar` | no | U3=PRE |
| `querer` | no | U4=PRE, PER |
| `sentarse` | sí | U7=PRE |

#### Irregularidad vocálica o→ue (3)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `acostarse` | sí | U7=PRE |
| `dormir` | no | U6=PRE |
| `volver` | no | U7=PRE |

#### Irregularidad vocálica e→i (2)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `repetir` | no | U6=IMP |
| `vestirse` | sí | U7=PRE |

#### Irregularidad vocálica u→ue (1)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `jugar` | no | U6=PRE, U7=PRE |

#### Irregularidad 1ª persona (3)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `hacer` | no | U6=PRE (+ IND raíz irregular + IMP `haz`) |
| `ponerse` | sí | U7=PRE |
| `salir` | no | U7=PRE (+ IMP `sal`) |

#### Irregularidad 1ª persona + cambio vocálico e→ie (1)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `venir` | no | U6=PRE, U7=PRE (+ IMP `ven`) |

#### Totalmente irregular (5)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `decir` | no | U6=IMP (`di`) |
| `estar` | no | U5=PRE, U9=IND (raíz irregular) |
| `ir` | no | U6=PRE, U7=PRE, U9=IND (paradigma mismo que ser) + IMP `ve` |
| `ser` | no | U1=PRE, U2=PRE, U3=PRE, U5=PRE (+ IND paradigma mismo que ir) |
| `tener` | no | U1=PRE, U2=PRE |

#### Tipo gustar (2)
| Lema | Reflexivo | Apariciones |
|---|---|---|
| `gustar` | no | U4=PRE, U8=PRE |
| `doler` | no | U8=PRE (+ irregularidad vocálica o→ue) |

#### Resumen

| Rasgo morfológico (Presente) | Lemas |
|---|---|
| Regular -ar | 20 |
| Regular -er | 3 |
| Regular -ir | 3 |
| Irregularidad vocálica e→ie | 5 |
| Irregularidad vocálica o→ue | 3 |
| Irregularidad vocálica e→i | 2 |
| Irregularidad vocálica u→ue | 1 |
| Irregularidad 1ª persona | 3 |
| Irregularidad 1ª persona + cambio vocálico | 1 |
| Totalmente irregular | 5 |
| Tipo gustar | 2 |
| **Total** | **48** |

**Reflexivos:** 13 lemas (ortogonal al rasgo morfológico).

**Doble dimensión confirmada** (verbos también en `gramatica-canonica.json`): `ser`, `estar`, `gustar`, `doler`, `querer`, `ir`. (`haber` solo en gramatical como `Hay`, sin paradigma en NC1.)

**Refinamiento incremental:** esta materialización es la base. Cualquier ajuste fino (variantes léxicas, lemas no detectados, reclasificación) se hace por edición directa de `verbos-canonicos.json` sin reabrir el diseño.

---

## §16 — Cierre de pieza 4 (lista exacta del registry de pronunciación/ortografía, 2026-05-11)

**Forma del registry:** estructura de dos niveles `{categoría → subcategoría → items}`. Misma lógica que `verbos-canonicos.json` y `gramatica-canonica.json`: solo lo que NC1 trabaja, no se reproduce el inventario PCIC A1 entero (101 entradas en ortografía PCIC, NC1 toca un subconjunto pequeño).

### §16.1 — Matriz de cobertura cruzada contra `pronunciacion_ortografia[]` de `nc1-curso.json`

Las 9 entradas del índice editorial cubiertas + 1 entrada reasignada de pieza 3:

| Unidad | Entrada del índice | Categoría destino | Canónico final |
|---|---|---|---|
| U1 | Interrogativos | Signos de puntuación + Entonación | `Signos de interrogación → [¿, ?]` (apertura y cierre obligatorios) + `Entonación interrogativa básica` (preparación para U7) |
| U2 | Las vocales (a, e, i, o, u) | Vocales | `Vocales españolas → [a, e, i, o, u]` |
| U2 | Uso de las mayúsculas *(reasignado de `gramatica[]`, pieza 3)* | Mayúsculas | `Uso general de mayúsculas` con lista A1 (ver §16.2) |
| U3 | El sonido /θ/ (za, zo, zu, ce, ci) | Sonidos y correspondencias ortográficas | `/θ/ → [za, zo, zu, ce, ci]` |
| U4 | El sonido /r/ y el sonido /rr/ | Sonidos y correspondencias ortográficas | `/r/ → [r-]` · `/rr/ → [rr, r-]` |
| U5 | El sonido /x/ (ja, je, ji, jo, ju, ge, gi) | Sonidos y correspondencias ortográficas | `/x/ → [ja, je, ji, jo, ju, ge, gi]` |
| U6 | La b = v | Letras homófonas | `b = v → [b, v]` |
| U7 | Entonación interrogativa y exclamativa | Entonación + Signos de puntuación | `Entonación interrogativa` (amplía U1) + `Entonación exclamativa` + `Signos de exclamación → [¡, !]` |
| U8 | El sonido /k/ (ca, co, cu, que, qui) | Sonidos y correspondencias ortográficas | `/k/ → [ca, co, cu, que, qui]` |
| U9 | Acentuación: agudas, llanas, esdrújulas | Acentuación | `Tipos según sílaba tónica → [agudas, llanas, esdrújulas]` |

**Cobertura:** 10/10 entradas (9 de `pronunciacion_ortografia[]` + 1 reasignada). Cero entradas sin destino.

### §16.2 — Lista final del registry

```jsonc
"pronunciacion-ortografia-canonica.json": {
  "Sonidos y correspondencias ortográficas": {
    "/θ/": ["za", "zo", "zu", "ce", "ci"],
    "/r/": ["r-"],
    "/rr/": ["rr", "r-"],
    "/x/": ["ja", "je", "ji", "jo", "ju", "ge", "gi"],
    "/k/": ["ca", "co", "cu", "que", "qui"]
  },
  "Letras homófonas": {
    "b = v": ["b", "v"]
  },
  "Vocales": {
    "vocales españolas": ["a", "e", "i", "o", "u"]
  },
  "Entonación": {
    "interrogativa": ["entonación ascendente al final"],
    "exclamativa": ["entonación enfática"]
  },
  "Acentuación": {
    "tipos según sílaba tónica": ["agudas", "llanas", "esdrújulas"]
  },
  "Signos de puntuación": {
    "interrogación (apertura y cierre obligatorios)": ["¿", "?"],
    "exclamación (apertura y cierre obligatorios)": ["¡", "!"]
  },
  "Mayúsculas": {
    "uso general": [
      "inicial de oración",
      "después de punto",
      "inicio de párrafo",
      "nombres propios de persona",
      "nombres propios de lugar",
      "nombres propios de instituciones",
      "siglas"
    ]
  }
}
```

7 categorías. 5 subcategorías en `Sonidos y correspondencias` + el resto con 1-2 subcategorías cada una.

### §16.3 — Decisiones explícitas

1. **U1 "Interrogativos" desambiguado** — se refiere al modo de preguntar: introducción de la entonación interrogativa + obligatoriedad de los signos `¿?` al inicio y al final. U1 introduce, U7 amplía con exclamativa.

2. **Naming respeta el índice editorial cuando existe.** "El sonido /θ/", "El sonido /r/", "Acentuación: agudas, llanas, esdrújulas" mantienen su naming literal. Solo se reformulan ligeramente para encajar en el shape de dos niveles.

3. **`Mayúsculas` con alcance A1 completo** — el libro de U2 cubre lo básico; la lista A1 PCIC (inicial de oración, después de punto, inicio de párrafo, nombres propios de persona/lugar/institución, siglas) se incluye entera como referencia canónica, aunque NC1 trabaje activamente solo una parte.

4. **Reasignación de pieza 3 confirmada** — `Uso de las mayúsculas` del `gramatica[]` de U2 entra aquí, no en `gramatica-canonica.json`. Coherente con la matriz de pieza 3.

5. **Entonación interrogativa aparece en U1 y U7** — no es duplicación: U1 introduce, U7 amplía con la exclamativa. En el registry vive una sola entrada `interrogativa`; la trazabilidad de "qué unidad introduce vs amplía" es trabajo de fase 2.

6. **PCIC A1 ortografía no se importa entera** — el inventario PCIC A1 tiene 101 entradas (6 áreas: abreviaturas, acentuación, ortografía de palabras, ortografía de letras, puntuación, símbolos). NC1 A1.1 trabaja un subconjunto pequeño. El registry refleja **solo lo trabajado**, no el universo PCIC.

### §16.4 — Doble dimensión (si aplica)

A diferencia de piezas 2 y 3, **pieza 4 no tiene doble dimensión sistemática**: las categorías ortográficas/fonéticas no se solapan con verbos ni con puntos gramaticales. Cada entrada vive solo en `pronunciacion-ortografia-canonica.json`.

Excepción potencial: la `entonación interrogativa` podría referenciarse desde una construcción gramatical (interrogación), pero no es necesario duplicarla — los `Interrogativos` de `gramatica-canonica.json` cubren la dimensión sintáctica; la entonación es solo fonética.

### §16.5 — Cierre

Pieza 4 cerrada el 2026-05-11 con matriz de cobertura (10 entradas) + lista final (7 categorías) + 6 decisiones explícitas. No requiere extracción exhaustiva de inventarios (las categorías ortográficas no aparecen dispersas en actividades como los verbos; son punto pedagógico identificable de forma directa en cada unidad).

**Estado tras §16:** todas las piezas arquitectónicas en ✅, salvo materialización exhaustiva de pieza 2 (única tarea pendiente antes del spike E1.5).