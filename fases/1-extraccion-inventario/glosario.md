# Glosario de términos — Fase 1

> Diccionario que explica qué significa cada término del inventario y de dónde sale su valor. Pensado para no perdernos cuando el modelo crezca.
>
> **Ubicación en el schema:** `schema-inventario.md` → §1 (estructura top-level).

---

## `unidad`
Número de la unidad dentro del curso. Identifica cuál de las unidades del libro estamos inventariando.
- **Origen del valor:** `unidades/nc1-curso.json`, en la entrada de la unidad correspondiente.

## `curso`
Identificador del curso al que pertenece la unidad. En el proyecto actual solo hay un curso, `nc1` ("Nuevo Compañeros 1"). Sirve para que el sistema sepa contra qué metadatos globales se valida el inventario.
- **Origen del valor:** `unidades/nc1-curso.json`.

## `titulo`
Nombre de la unidad tal como aparece impreso en el libro del alumno. No es interpretación ni resumen: es transcripción literal.
- **Origen del valor:** `unidades/nc1-curso.json`, campo `titulo` de la unidad.

## `paginas_libro`
Intervalo de páginas que ocupa la unidad en el libro impreso. Se usa para localizar la unidad físicamente y para validar que las páginas del detalle caen dentro del rango.
- **Origen del valor:** `unidades/nc1-curso.json`.

## `nivel`
Nivel MCER del curso (por ejemplo `A1.1`). Aporta contexto pedagógico: indica qué se puede esperar como contenido y qué quedaría fuera de alcance.
- **Origen del valor:** `unidades/nc1-curso.json`.

## `fuente`
Conjunto de dos datos que permiten saber **de qué documento físico salió el inventario** y **cuándo se hizo la extracción**:
- la ruta al PDF que se ha procesado,
- la fecha en la que se ejecutó la corrida de extracción.

Permite trazabilidad: si dentro de un año el libro cambia de edición, podemos saber a partir de qué fuente se construyó este inventario.

## `contenidos_indice`
Cinco frases tomadas del **índice oficial del libro** (Scope & Sequence, páginas 6-7), una por cada bloque pedagógico: vocabulario, gramática, comunicación, destrezas y cultura.

No es un resumen de lo que la unidad enseña; es la **copia literal** de cómo el libro anuncia su contenido. Sirve como referencia de alto nivel contra la que la IA contrasta lo que después encuentra en la unidad página a página.
- **Origen del valor:** `unidades/nc1-curso.json`, dentro de la entrada de la unidad correspondiente.

---

> **Source of truth de la cabecera identificativa:** `unidades/nc1-curso.json` es el diccionario maestro del curso para los campos de identificación del inventario (`unidad`, `curso`, `titulo`, `paginas_libro`, `nivel`) y `contenidos_indice`. Esos campos deben coincidir exactamente con la entrada de la unidad correspondiente. **El resto del top-level no deriva de `nc1-curso.json`:** `fuente.archivo` es convención fija, `fuente.version_extraccion` es la fecha de la corrida, los 4 bloques consolidados se derivan de las actividades y cuadros, `secciones` se reconstruye recorriendo `paginas_detalle`, `paginas_detalle` viene de la extracción del PDF, y las claves opcionales (`autoevaluacion`, `_nota_unidad_atipica`, `_decisiones_ia`, `_migracion_rediseno`) tienen cada una su propio origen.

---

## Bloques consolidados

> **Ubicación en el schema:** `schema-inventario.md` → §1 (top-level), con detalle de forma en §9 (bloques en §9.1–§9.4).

Son cuatro grandes objetos al nivel raíz del inventario que **agregan**, por dimensión lingüística, todo lo que la unidad trabaja. Funcionan como "resumen estructurado" de la unidad: en lugar de tener que recorrer todas las actividades para saber qué léxico, qué verbos, qué gramática o qué pronunciación aparecen, se consultan estos cuatro bloques.

Cada uno se construye **a partir de las listas tipadas** que la IA rellena dentro de cada actividad y de cada cuadro de la unidad. No son entradas independientes que se escriban a mano: se obtienen por agregación.

## `vocabulario_consolidado`
Recoge **todo el léxico** trabajado en la unidad, organizado por categoría canónica (familia, profesiones, lugares, etc.).

Internamente se divide en dos sub-bloques:
- **`principal`**: categorías que la unidad introduce o trabaja como contenido nuevo. Llevan descripción por unidad obligatoria.
- **`recurrente`**: categorías que **no son principales de esta unidad** pero se registran por utilidad transversal. Tres criterios de inclusión (frecuencia, posición, valor pedagógico) → `reglas-operativas.md`.

- **Origen del valor:** la propia actividad y cada cuadro ya declaran, dentro de su campo `vocabulario`, las referencias a campos semánticos que trabajan. El bloque consolidado **reorganiza** esa información poniendo el campo semántico como clave y agrupando, debajo de cada campo, las palabras y fuentes de todas las actividades y cuadros de la unidad que lo trabajan. El diccionario `campos-semanticos-canonicos.json` fija qué campos semánticos existen y cómo se nombran.

### Shape de cada entrada (categoría)

> **Ubicación en el schema:** `schema-inventario.md` → §9.1.

Dentro de `principal` y de `recurrente`, **la clave es el nombre canónico del campo semántico** (`"Familia"`, `"Profesiones"`, `"Lugares"`...). El valor es un objeto con tres campos:

- **`items`** — lista de objetos `{ palabra, fuentes }`, una entrada por palabra léxica del campo. `palabra` es el término tal como aparece trabajado en la unidad; `fuentes` indica de qué actividad o cuadro proviene esa palabra.
- **`fuentes`** — lista agregada con la **unión de todas las fuentes** de los `items` del campo. Permite responder rápido "¿en qué actividades de esta unidad se trabaja Familia?" sin recorrer item por item.
- **`descripcion`** — diccionario `{ "U<n>": <texto> }` con texto libre por unidad. Explica qué se enseña del campo en cada unidad en la que aparece. **Obligatorio en `principal`**; **opcional en `recurrente`** (ver más abajo).

### Campo `descripcion` por unidad

> **Ubicación en el schema:** `schema-inventario.md` → §9.6.

Diccionario donde la clave es la unidad en la que la categoría aparece (`"U1"`, `"U3"`...) y el valor es un texto libre que explica qué se enseña concretamente del campo en esa unidad.

- **Obligatoriedad:** **obligatorio** en cada entrada de `principal`; **opcional** en `recurrente`.
- **Para qué sirve:** es el texto pedagógico que da contexto al inventario. Sin él, una entrada `principal` sería solo una lista de palabras sin explicación de qué aporta a la unidad.
- **Origen del valor:** redacción de la IA (o del autor) con apoyo del PCIC A1 (Cervantes). Cada dimensión tiene su archivo PCIC propio (paralelismo fuente↔registry):
  - **`gramatica_consolidada`:** se apoya en `pcic-a1-gramatica.json` (PCIC, inventario de Gramática). Registry: `gramatica-canonica.json`.
  - **`vocabulario_consolidado`:** se apoya en `pcic-a1-vocabulario.json` (PCIC, inventario de Nociones específicas: 417 entradas agrupadas en categorías y subcategorías). Registry: `campos-semanticos-canonicos.json`.
  - **`pronunciacion_ortografia_consolidada`:** se apoya en `pcic-a1-pronunciacion-ortografia.json` (PCIC, pronunciación + ortografía en sub-bloques). Registry: `pronunciacion-ortografia-canonica.json`.
  - **`tiempos_y_verbos_consolidado`:** no tiene archivo PCIC propio (el PCIC no aísla los verbos como inventario). Sus paradigmas viven distribuidos en `pcic-a1-gramatica.json` y los verbos léxicos en `pcic-a1-vocabulario.json`. Registry: `verbos-canonicos.json`.
- **Archivo PCIC adicional fuera de las 4 dimensiones:** `pcic-a1-comunicacion.json` (PCIC, Funciones comunicativas: 141 entradas). Se conserva como recurso disponible para descripciones que requieran apoyo pragmático-comunicativo, aunque `comunicacion` no es un bloque top-level consolidado.

**Ejemplo:**

```jsonc
"Pronombre sujeto": {
  "items": [...],
  "fuentes": [...],
  "descripcion": {
    "U1": "PCIC A1 §7.1.1 — Pronombres personales en función de sujeto..."
  }
}
```

> Criterios de qué entra en `principal` vs `recurrente`, cómo se redacta `descripcion` (referencia PCIC) y la lógica de 3 pasos para `recurrente` → `reglas-operativas.md` §5.1.

### Formato canónico de `fuentes`

> **Ubicación en el schema:** `schema-inventario.md` → §9.5.

Una **fuente** es un string que indica de qué pieza concreta de la unidad procede una palabra, lema, categoría o cualquier referencia recogida en los bloques consolidados. El formato es estricto y validable por expresión regular:

```
^(p\d+-act\d+(@R)?|cuadro@p\d+(#\d+)?)$
```

Tres tipos de fuente:

- **`pNN-actMM`** — fuente de actividad. `NN` es el número de página y `MM` el número de actividad dentro de la página. Puede llevar sufijo `@R`. Ejemplo: `"p13-act5"`.
- **`cuadro@pNN`** — fuente de cuadro. Indica que la palabra/categoría procede de un cuadro de la página `NN`. **No admite sufijo `@R`** (los cuadros no tienen campo `respuestas`). Ejemplo: `"cuadro@p14"`.
- **`cuadro@pNN#K`** — variante de la anterior cuando hay **varios cuadros en la misma página**. `K` es el orden del cuadro dentro de la página. Ejemplo: `"cuadro@p20#3"` = tercer cuadro de la página 20.

### Sufijo opcional `@R`

Se añade al final de una fuente **de actividad** para indicar que la palabra aparece **únicamente en el campo `respuestas`** de una actividad de **producción** del alumno, no en el input del libro. Las fuentes de cuadro nunca lo llevan.

- **Tipos de actividad de producción donde aplica (5 valores de la taxonomía cerrada §5 del schema):** `produccion_escrita_guiada`, `expresion_escrita_libre`, `expresion_oral_libre`, `tarea_final`, `interaccion_oral`.
- **Significado:** la palabra es **output esperado del alumno**, no contenido leído del libro. La distinción es importante para análisis posteriores (ej. saber qué léxico el alumno produce vs. qué léxico recibe como input).

### Ejemplos válidos
- `"p13-act5"` — quinta actividad de la página 13.
- `"cuadro@p14"` — único cuadro de la página 14.
- `"cuadro@p20#3"` — tercer cuadro de la página 20.
- `"p15-act6@R"` — palabra que aparece solo en `respuestas` de la sexta actividad de p15 (output del alumno).

> **Por qué este formato:** es **validable estructuralmente** (la regex lo verifica), **compacto** y **legible para el lector humano**. El validador rechaza cualquier string de `fuentes` que no encaje en el patrón.

## `tiempos_y_verbos_consolidado`

> **Ubicación en el schema:** `schema-inventario.md` → §9.2.

Recoge **todos los verbos trabajados** en la unidad. Es una **lista plana de objetos**, una entrada por lema verbal único. A diferencia de los otros tres bloques consolidados, **no se divide en `principal`/`recurrente`**.

### Campos de cada entrada (shape de §9.2)

Cada entrada del bloque tiene los siguientes campos:

- **`lema`** — la forma de diccionario del verbo (ej. `ser`, `llamarse`). Debe existir en el registry `verbos-canonicos.json`.
- **`tipo_de_verbo`** — lista de strings con la **categoría sintáctico-semántica** del verbo (`copulativo`, `transitivo`, `pronominal`, `reflexivo`...). Marca ortogonal a la morfología: un verbo puede ser a la vez transitivo y reflexivo, p. ej.
- **`rasgo_por_tiempo`** — objeto que describe el comportamiento morfológico del verbo en cada tiempo en el que aparece (`regular -ar`, `regular -er`, `regular -ir`, `irregularidad vocálica o→ue`, `totalmente irregular`, `regular 2ª persona singular`, etc.). Claves opcionales según el tiempo: `Presente`, `Pretérito indefinido`, `Imperativo`, `Infinitivo` (cubre la categoría "forma no personal del verbo" trabajada fuera de perífrasis).
- **`tiempos`** — lista de los tiempos en los que el lema se conjuga **en el curso**. Valores del enum cerrado de 4: `Presente`, `Pretérito indefinido`, `Imperativo`, `Infinitivo`. `Perífrasis` no es valor del enum (las perífrasis no son tiempos; ver schema §5d y §3.2 sobre `estructura_perifrastica`). `Participio` y `Gerundio` no entran (no aparecen en NC1).
- **`formas_trabajadas`** — lista plana con la **unión agregada** de todas las formas conjugadas concretas que aparecen en cualquier actividad o cuadro de la unidad (literales del libro, no canónicas).
- **`fuentes`** — lista de fuentes (formato canónico de §9.5) que indican de qué actividades y cuadros procede el lema.
- **`descripcion`** — diccionario `{ "U<n>": <texto> }` con texto libre por unidad, paralelo al de los otros tres bloques consolidados.

### Origen del valor

Cada actividad y cada cuadro ya declaran, dentro de su campo `tiempos_y_verbos`, los lemas verbales trabajados con su tiempo y sus formas. El bloque consolidado **reorganiza** esa información en una lista plana con **una entrada por lema único**, acumulando bajo cada entrada sus tiempos, formas trabajadas y fuentes a lo largo de toda la unidad.

### Desalineación actual con el registry (deuda Paso 3)

El **registry** `verbos-canonicos.json` (catálogo permanente de lemas válidos del curso) tiene hoy un shape parcialmente distinto del declarado en §9.2. `lema`, `tipo_de_verbo`, `rasgo_por_tiempo` y `tiempos` están alineados. Pendientes:

| Campo en §9.2 (inventario) | Equivalente en `verbos-canonicos.json` (registry) |
|---|---|
| `formas_trabajadas` (lista por unidad, formas concretas del libro) | (no existe; el registry no guarda formas concretas) |
| `descripcion` (`U<n>` → texto) | `lo_que_se_trabaja` (`U<n>` → texto explicativo) |
| `fuentes` (lista de pNN-actMM / cuadro@pNN) | `apariciones` (`U<n>` → lista de tiempos abreviados) |

La diferencia es **deuda explícita** registrada en el Apéndice transitorio §A.3 de `schema-inventario.md` y se resuelve en Paso 3 (alineación validador + registry con schema).

## `gramatica_consolidada`
Recoge **todos los contenidos gramaticales** trabajados en la unidad (artículos, género, número, posesivos, interrogativos, etc.), organizados por categoría canónica.

Internamente se divide en dos sub-bloques `principal` y `recurrente`, con la misma semántica que en `vocabulario_consolidado` (criterios de inclusión → `reglas-operativas.md`).

- **Origen del valor:** cada actividad y cada cuadro ya declaran, dentro de su campo `gramatica`, las categorías gramaticales que trabajan. El bloque consolidado **reorganiza** esa información poniendo la categoría gramatical como clave y agrupando bajo cada una las apariciones y fuentes en la unidad. El diccionario `gramatica-canonica.json` fija qué categorías existen y cómo se nombran.

### Shape de cada entrada (categoría) — §9.3

> **Ubicación en el schema:** `schema-inventario.md` → §9.3.

Dentro de `principal` y de `recurrente`, **la clave es el nombre canónico de la categoría gramatical** (`"Pronombre sujeto"`, `"Artículo determinado"`, `"Masculino y femenino"`...). El valor es un objeto con la misma forma que en `vocabulario_consolidado`:

- **`items`** — lista de objetos `{ palabra, fuentes }` con cada elemento gramatical concreto que aparece (cada forma o ejemplo trabajado en la unidad).
- **`fuentes`** — lista agregada de fuentes de todos los `items` de la categoría.
- **`descripcion`** — diccionario `{ "U<n>": <texto> }` con texto libre por unidad. **Obligatoria en `principal`**; **opcional en `recurrente`**.

Las reglas de formato de `fuentes` (§9.5) y de `descripcion` (§9.6) son **compartidas** con los otros tres bloques consolidados; se describen en una sola sección y aplican aquí igual.

## `pronunciacion_ortografia_consolidada`
Recoge **los contenidos de pronunciación y ortografía** trabajados en la unidad (acento, sílaba tónica, entonación, reglas ortográficas, etc.).

Internamente se divide en dos sub-bloques `principal` y `recurrente`, con la misma semántica que en `vocabulario_consolidado` (criterios de inclusión → `reglas-operativas.md`).

- **Origen del valor:** cada actividad y cada cuadro ya declaran, dentro de su campo `pronunciacion_ortografia`, las categorías de pronunciación u ortografía que trabajan. El bloque consolidado **reorganiza** esa información poniendo la categoría como clave y agrupando bajo cada una las apariciones y fuentes en la unidad. El diccionario `pronunciacion-ortografia-canonica.json` fija qué categorías existen y cómo se nombran.

### Shape de cada entrada (categoría) — §9.4

> **Ubicación en el schema:** `schema-inventario.md` → §9.4.

Dentro de `principal` y de `recurrente`, **la clave es el nombre canónico de la categoría de pronunciación u ortografía** (`"Sílaba tónica"`, `"Entonación interrogativa"`, `"Abecedario"`...). El valor es un objeto con la misma forma que en `vocabulario_consolidado`:

- **`items`** — lista de objetos `{ palabra, fuentes }` con cada elemento concreto que aparece (forma trabajada, regla aplicada, ejemplo del libro).
- **`fuentes`** — lista agregada de fuentes de todos los `items` de la categoría.
- **`descripcion`** — diccionario `{ "U<n>": <texto> }` con texto libre por unidad. **Obligatoria en `principal`**; **opcional en `recurrente`**.

Las reglas de formato de `fuentes` (§9.5) y de `descripcion` (§9.6) son **compartidas** con los otros tres bloques consolidados.

---

> **Principio común a los 4 bloques:** son **agregados**, no fuentes. La fuente real está en las listas tipadas dentro de cada actividad y cuadro. Si cambias una actividad, los bloques consolidados deben recalcularse.

---

## `secciones`

> **Ubicación en el schema:** `schema-inventario.md` → §1 (top-level) y §8 (enumeración cerrada de los 7 valores de `seccion`).

Es un **índice** que dice, para cada sección pedagógica de la unidad, en qué páginas vive y qué actividades contiene. No aporta contenido nuevo: reordena información que ya está dispersa en `paginas_detalle`.

Las **siete secciones** son fijas y normalizadas: `vocabulario`, `gramatica`, `comunicacion`, `destrezas`, `cultura`, `evaluacion`, `reflexion`. Es la enumeración cerrada definida en §8 del schema; ninguna unidad puede inventar secciones nuevas.

Para cada sección se guardan dos listas:
- **`paginas`** — las páginas del libro que pertenecen a esa sección dentro de esta unidad (ej. `[34, 35, 36]`).
- **`actividades_ids`** — los identificadores de las actividades que viven en esa sección (ej. `["U4-p34-act1", "U4-p35-act2"]`).

- **Origen del valor:** cada página del inventario (dentro de `paginas_detalle`) ya declara a qué sección pertenece (campo `seccion`). El bloque `secciones` **invierte ese índice**: en lugar de "página → sección", expone "sección → páginas + actividades". Es decir, se reconstruye recorriendo `paginas_detalle` y agrupando por el valor de `seccion`.

> Es una vista de navegación: permite responder rápido a preguntas tipo "¿qué actividades trabajan vocabulario en U4?" sin tener que recorrer todas las páginas.

---

## Opcionales canónicas

> **Ubicación en el schema:** `schema-inventario.md` → §1 (top-level), con detalle en §6, §11 y §14.

Son tres claves que **pueden** aparecer en el inventario, pero no son obligatorias. Forman parte estable del contrato (no son deuda de migración): existen porque cubren casos reales del sistema que solo se dan a veces.

## `autoevaluacion`

> **Ubicación en el schema:** `schema-inventario.md` → §6.

Bloque que recoge la **autoevaluación de pie de página** que cierra cada unidad. El alumno marca su autopercepción del aprendizaje en la unidad.

### Campos internos
- **`pagina`** — entero. Página del libro donde aparece el bloque.
- **`instruccion_original`** — string. Transcripción literal del enunciado del libro.
- **`opciones`** — lista de exactamente **3 strings**. Las tres opciones que se presentan al alumno.
- **`emoticonos`** — booleano. Indica si el libro acompaña las opciones con emoticonos visuales.

### Valores fijos en NC1
Por convención editorial del curso, las unidades de NC1 traen siempre los mismos textos:
- `instruccion_original`: `"Mis resultados en esta unidad son:"`.
- `opciones`: `["MUY BUENOS", "BUENOS", "NO MUY BUENOS"]`.
- `emoticonos`: `true`.

### Cuándo aparece
En las unidades del libro que llevan ese bloque. En NC1 es estándar; en cursos futuros (NC2, NC3...) los valores fijos pueden cambiar, pero el shape del bloque se mantiene canónico.

- **Origen del valor:** transcripción literal del bloque tal como aparece en el libro.

## `_nota_unidad_atipica`

> **Ubicación en el schema:** `schema-inventario.md` → §11.

Clave **opcional** del top-level del inventario. Lleva un único string con texto libre que marca que la unidad **se sale del patrón habitual** del curso y explica por qué.

- **Tipo:** string.
- **Obligatoriedad:** opcional. Se omite del JSON en unidades normales.
- **Cuándo aparece:** solo en unidades atípicas. En NC1, U0 ("Punto de partida") es atípica porque es una unidad pre-A1.1 introductoria, sin la estructura de 10 páginas y 7 secciones del resto.
- **Origen del valor:** decisión del autor durante la extracción, redactada como nota breve para el lector del inventario.

## `_decisiones_ia`
Lista de strings con **decisiones tomadas por la IA** durante la extracción o clasificación que merecen quedar registradas: ambigüedades resueltas, opciones descartadas, razonamientos no triviales.
- **Para qué sirve:** auditoría posterior. Si un humano revisa el inventario semanas más tarde y se pregunta "¿por qué aquí se clasificó como X y no como Y?", la respuesta está aquí.
- **Cuándo aparece:** siempre que la IA haya tenido que tomar una decisión no obvia. Si la extracción es totalmente directa, puede no estar.
- **Origen del valor:** la propia IA durante la corrida.

---

## Opcional transitoria

## `_migracion_rediseno`
Metadata que indica que el inventario fue **migrado del modelo viejo al modelo nuevo** durante el rediseño.
- **Estado:** clave **transitoria**, no forma parte del contrato canónico final. Detalle de su shape, ciclo de vida y condiciones de retirada → Apéndice transitorio de `schema-inventario.md`.
- **Cuándo aparece:** solo en inventarios que existían antes del rediseño y han sido reescritos al modelo nuevo. NC2 y unidades nuevas no la llevan: nacen ya en el modelo nuevo.

---

## `paginas_detalle`

> **Ubicación en el schema:** `schema-inventario.md` → §1 (top-level) y §2 (schema por página).

Es **el cuerpo real del inventario**: la lista, página por página, de todo lo que la unidad contiene. Mientras que los 4 bloques consolidados y `secciones` son vistas reorganizadas, `paginas_detalle` es la fuente primaria.

Para cada página guarda:
- el **número de página** del libro;
- a qué **sección** pertenece (uno de los 7 valores normalizados de §8);
- las **actividades** de esa página (con todo su contenido literal, sus 4 listas tipadas, sus audios/imágenes/vídeos y sus respuestas);
- los **cuadros** de esa página, si los hay.

- **Origen del valor:** lectura página a página del PDF de la unidad. Cada actividad y cada cuadro se transcribe respetando literalidad (texto, huecos, ítems del libro tal cual aparecen) y se enriquece con la clasificación canónica (tipo, destreza, enfoque y las 4 listas tipadas).

---

## Schema por actividad

> **Ubicación en el schema:** `schema-inventario.md` → §3 (campos), §3.1 (nota sobre `numero`), §3.2 (shape de `tiempos_y_verbos`), §5/§5b/§5c (enumeraciones), §10 (audio/imagen/video/respuestas), §14 (marcas internas).

Una **actividad** es cada ejercicio o propuesta del libro que el alumno realiza. Dentro de `paginas_detalle`, cada página contiene una lista de actividades. Cada actividad se describe con los siguientes campos:

### `id`
Identificador único de la actividad dentro del corpus, con formato `UX-pYY-actNN` (unidad, página, número de actividad dentro de la página). Por ejemplo, `U4-p35-act2` es la segunda actividad de la página 35 de la unidad 4.
- **Origen del valor:** se construye automáticamente a partir de la posición de la actividad.

### `numero`
Número de la actividad **tal como aparece impreso en el libro** (1, 2, 3...).
- **Opcional** (detalle en `schema-inventario.md` §3.1). La mayoría de actividades llevan número visible y entonces el campo se rellena con el entero del libro. Algunas no lo llevan — "Para aprender", cuadros que se clasifican como actividad por `reglas-operativas.md` §1, autoevaluación a pie de página — y en esos casos el campo se omite por completo.
- **Restricción:** si está presente, debe ser entero. El validador acepta su ausencia.
- **Origen del valor:** transcripción directa del número del libro.

### `tipo`
Categoría de la actividad según una **taxonomía cerrada de 20 valores** (§5 del schema).
- **Origen del valor:** la IA aplica las reglas canónicas de `reglas-operativas.md` §2.

### `destreza`
Lista de **habilidades MCER** que la actividad pone en juego. Enumeración cerrada de 6 valores (§5b del schema).
- **Reglas estructurales:** mínimo un valor, sin duplicados, orden alfabético.
- **Origen del valor:** la IA aplica las reglas canónicas de `reglas-operativas.md` §2.3.

### `enfoque`
**Dominio de contenido** principal de la actividad. Enumeración cerrada de 6 valores (§5c del schema).
- **Origen del valor:** la IA aplica las reglas canónicas de `reglas-operativas.md` §2.3.

### `instruccion_original`
Enunciado de la actividad **transcrito literalmente** del libro, sin reformular ni resumir.
- **Origen del valor:** transcripción literal del PDF.

### Las 4 listas tipadas (`vocabulario`, `tiempos_y_verbos`, `gramatica`, `pronunciacion_ortografia`)
Cuatro listas que declaran, para esta actividad concreta, qué contenidos lingüísticos trabaja en cada dimensión. Tres de ellas son listas de strings (referencias canónicas a los registries); `tiempos_y_verbos` es lista de objetos (ver más abajo).
- **Para qué sirven:** son la **fuente** de los 4 bloques top-level consolidados.
- **Origen del valor:** decisión de la IA tras analizar el contenido literal de la actividad.

### Shape de `actividad.tiempos_y_verbos`

> **Ubicación en el schema:** `schema-inventario.md` → §3.2.

A diferencia de las otras tres listas tipadas (que son listas de strings), `tiempos_y_verbos` es **lista de objetos**. Cada objeto declara que en esta actividad se trabaja un verbo concreto en un tiempo concreto, con unas formas concretas. Tres campos obligatorios:

- **`lema`** — la forma de diccionario del verbo (ej. `ser`, `llamarse`). Debe existir en el registry `verbos-canonicos.json`.
- **`tiempo`** — el tiempo o forma verbal trabajado. Valor del enum cerrado de §5d del schema (4 valores): `Presente`, `Pretérito indefinido`, `Imperativo`, `Infinitivo`. `Infinitivo` cubre la categoría "forma no personal del verbo" cuando se trabaja pedagógicamente fuera de perífrasis. `Perífrasis` no está en el enum (las perífrasis no son tiempos; ver schema §5d). `Participio` y `Gerundio` no aparecen en NC1 y no entran en el enum.
- **`formas_trabajadas`** — las formas conjugadas concretas que aparecen **en esta actividad**, transcritas **literalmente del libro** (no se canonizan). Lista no vacía. Ejemplo: `["soy", "eres", "es"]`.
- **`estructura_perifrastica`** *(opcional)* — string que describe la perífrasis cuando el verbo aparece como auxiliar de una (`"ir a + infinitivo"`, `"querer + infinitivo"`, etc.). El verbo conserva su `tiempo` real (típicamente `Presente`). El infinitivo complemento NO se registra como entrada verbal separada en `tiempos_y_verbos`; queda implícito aquí. Detalle normativo en reglas-operativas §5.2.

**Ejemplo completo:**
```jsonc
"tiempos_y_verbos": [
  { "lema": "ser",      "tiempo": "Presente", "formas_trabajadas": ["soy", "eres", "es"] },
  { "lema": "llamarse", "tiempo": "Presente", "formas_trabajadas": ["me llamo", "te llamas", "se llama"] }
]
```

**Casos especiales:**
- **Perífrasis** (`ir a + infinitivo`, `tener que + infinitivo`, `querer + infinitivo`, etc.): el verbo auxiliar se codifica con su **tiempo real** (típicamente `"Presente"`) en `tiempo` y las formas conjugadas reales en `formas_trabajadas` (ej. `["vamos a", "van a"]`); la estructura se declara aparte en `estructura_perifrastica` (ej. `"ir a + infinitivo"`). El infinitivo complemento NO se registra como entrada verbal separada. `Perífrasis` no es valor del enum `tiempo`.
- **Forma no personal del verbo trabajada pedagógicamente fuera de perífrasis**: se declara con `"tiempo": "Infinitivo"` y `formas_trabajadas` reflejando la forma del libro (ej. `["cantar"]`). Aplica a listas de verbos en infinitivo, ejercicios de identificación, etc.
- **Verbo sin paradigma trabajado** (mención léxica suelta del verbo, sin que la actividad pida nada sobre su conjugación o sobre la forma no personal): **no entra aquí**. Si procede, va a la lista `vocabulario`.

**Relación con el registry y con el bloque consolidado:**
- El **registry** `verbos-canonicos.json` lista todos los lemas válidos del curso con su metadata completa (rasgo por tiempo, tipo de verbo, apariciones, lo que se trabaja).
- La **actividad** solo declara el subconjunto de lemas que ella trabaja, con el tiempo concreto y las formas exactas que aparecen.
- El **bloque top-level** `tiempos_y_verbos_consolidado` agrega lo declarado en todas las actividades y cuadros de la unidad por lema único.

**Qué chequea el validador:** que cada `lema` exista en el registry, que cada `tiempo` esté en el enum, y que las `formas_trabajadas` pertenezcan al paradigma del lema declarado (validación estructural; el detalle de cómo se chequea vive en `reglas-operativas.md`).

### `audio`, `imagen`, `video`

> **Ubicación en el schema:** `schema-inventario.md` → §10.

Sub-objetos que indican si la actividad incluye material multimedia. Los tres **siempre están presentes** como sub-objetos en toda actividad, incluso cuando `presente=false`; el shape no se omite.

- **`audio`** — `{ "presente": <bool>, "pista": <int opcional>, "transcripcion": <str opcional> }`.
  - `pista`: número de pista cuando el libro lo indica.
  - `transcripcion`: opcional. Si está presente, contiene la transcripción literal del audio. Reglas operativas sobre cuándo el audio puede aportar a los bloques consolidados → `reglas-operativas.md` regla 11.
- **`imagen`** — `{ "presente": <bool>, "descripcion": <str — obligatoria si presente=true> }`.
  - **Restricción condicional:** si `imagen.presente == true`, `descripcion` debe estar presente y no vacía. Si `presente=false`, `descripcion` puede omitirse o ir vacía.
- **`video`** — `{ "presente": <bool> }`. No lleva ni `pista` ni `descripcion` ni `transcripcion` en el shape actual.

- **Origen del valor:** observación del PDF; `audio.transcripcion` se rellena cuando procede según `reglas-operativas.md` regla 11.

### `respuestas`

> **Ubicación en el schema:** `schema-inventario.md` → §10.

Lista de strings con las **respuestas esperadas** de la actividad.

- **Siempre presente** en cada actividad.
- Tipo: **lista de strings**.
- Puede ser **lista vacía** si la actividad no tiene respuesta esperada (ej. expresión oral o escrita libre, interacción oral abierta).
- **Origen del valor:** clave de soluciones del libro cuando existe; decisión de la IA cuando no, transcribiendo las respuestas que el contexto deja claras.

> Las palabras que **solo** aparecen en `respuestas` de una actividad de producción (no en el input del libro) llevan el sufijo `@R` en su fuente al alimentar los bloques consolidados (ver §9.5 "Sufijo opcional `@R`").

### `datos`
**Saco abierto** que contiene el **contenido literal del libro** específico de cada tipo de actividad: ítems de un completa-huecos, opciones de un test, texto íntegro de una lectura, columnas de un relaciona, cuadrícula de una sopa de letras, horarios, programas de TV, personajes, etc.
- **Por qué es saco abierto:** distintos tipos de actividad requieren distintos campos. En lugar de fijar un shape único, se admite cualquier campo necesario.
- **Política de extensibilidad:** cualquier campo nuevo se documenta y se añade al schema con la regla de población correspondiente en `reglas-operativas.md`.
- **Origen del valor:** transcripción literal del PDF.
- **Cómo decidir entre los 3 campos canónicos de texto** (`texto_completo` / `dialogo_completo` / `textos_personajes`) → `convenciones-y-casos.md` §1.4 (tabla decisional + sub-secciones §1.4.1, §1.4.2, §1.4.3).

#### `datos.items_libro`

> **Ubicación en el schema:** `schema-inventario.md` → §12.

Campo dentro de `datos` que recoge los **ítems literales del libro** que el alumno manipula: las frases con hueco de un cloze, los pares de un relaciona, las opciones de un test, las afirmaciones de un V/F, los elementos a clasificar...

- **Tipo:** lista de strings.
- **Ubicación:** siempre dentro de `actividad.datos`, no al nivel raíz de la actividad.
- **Literalidad obligatoria:** los strings se transcriben **palabra por palabra** del libro, incluidos huecos (`_____`), signos de puntuación y mayúsculas/minúsculas tal y como aparecen impresos.
- **Obligatoria en actividades de tipo:** `completa_huecos`, `ordena`, `clasifica`, `seleccion_multiple`, `verdadero_falso`. En otras tipologías puede aparecer si la actividad presenta una lista de ítems manipulables, pero no es obligatoria.
- **Origen del valor:** transcripción literal del PDF.

### Marcas internas opcionales

- **`_funcion_ambigua`** — booleano. Marca que la función de la actividad no se ha podido desambiguar. **Bloquea cierre.**
- **`_decisiones_ia`** — lista de strings. Auditoría de decisiones no obvias tomadas por la IA en esta actividad concreta (independiente del `_decisiones_ia` top-level).
- **Origen del valor:** la propia IA durante la corrida.

---

## Schema por cuadro

> **Ubicación en el schema:** `schema-inventario.md` → §4 (campos), §7 (enumeración cerrada de `tipo_cuadro`).

Un **cuadro** es una pieza didáctica del libro que **no es una actividad** (no la realiza el alumno como ejercicio), pero que aporta contenido lingüístico: tablas de conjugación, recuadros de gramática, esquemas, listas de vocabulario, notas culturales, etc. Aparecen dentro de una página, junto a las actividades, y aportan a los **4 bloques top-level consolidados** en igualdad de condiciones que las actividades.

Cada cuadro se describe con los siguientes campos:

### `tipo_cuadro`
Categoría pedagógica del cuadro. Enumeración cerrada de **5 valores** (§7 del schema): `gramatical`, `lexical`, `pronunciacion_ortografia`, `cultural`, `comunicativo`.
- **Origen del valor:** decisión de la IA según el contenido didáctico del cuadro.

### `titulo`
Título del cuadro tal como aparece impreso en el libro, o `null` si el cuadro no lleva título visible.
- **Origen del valor:** transcripción literal del PDF.

### `contenido`
Objeto que describe **qué hay dentro del cuadro**. Tiene una estructura semi-libre porque distintos cuadros tienen formas muy distintas (una tabla de conjugación no se modela igual que un recuadro de saludos), pero siempre lleva un campo `tipo` que identifica su estructura interna:
- **`tipo`** — string que nombra la estructura interna: `tabla_conjugacion`, `tabla_interrogativos`, `tabla_posesivos`, `recuadro_gramatical`, etc.
- **`texto_intro`** — opcional. Texto introductorio del cuadro si lo hay.
- **`ejemplos`** — lista de strings con ejemplos del cuadro.
- ... otros campos según el cuadro concreto (filas de tabla, columnas, etc.).

> **Diferencia con `tipo_cuadro`:** `tipo_cuadro` dice **qué tipo pedagógico es** (gramatical, lexical...). `contenido.tipo` dice **qué forma tiene por dentro** (una tabla de conjugación, un recuadro con ejemplos...). Son ejes complementarios.

- **Origen del valor:** transcripción literal del cuadro del PDF.

### `observaciones`
Texto libre con notas adicionales sobre el cuadro (opcional).
- **Origen del valor:** decisión del autor o de la IA si hay algo no evidente que merece registrarse.

### Las 4 listas tipadas en cuadro

Igual que en una actividad, un cuadro declara `vocabulario`, `tiempos_y_verbos`, `gramatica` y `pronunciacion_ortografia`. **Misma convención de presencia y vaciedad que en actividad** (§3 del schema): las cuatro listas están **siempre presentes**; pueden ser **lista vacía** si el cuadro no trabaja esa dimensión. La opcionalidad del cuadro como unidad vive en `página.cuadros` (§2 del schema), no en sus listas internas.

- **Para qué sirven:** los cuadros, igual que las actividades, son fuente de los 4 bloques top-level consolidados. Lo que un cuadro declara en estas listas se acumula en los agregados de la unidad.
- **Origen del valor:** decisión de la IA tras analizar el contenido literal del cuadro.
- **Shape de `tiempos_y_verbos` en cuadros:** idéntico al de actividades (ver "Shape de `actividad.tiempos_y_verbos`" más arriba).

---

## Taxonomía de `tipo` (20 valores)

> **Ubicación en el schema:** `schema-inventario.md` → §5 (enumeración cerrada). **Criterios y reglas operativas:** `reglas-operativas.md` → §2.

Enumeración cerrada de los **20 tipos de actividad** válidos. La IA elige uno por actividad aplicando la regla operativa central de `reglas-operativas.md` §2: ***`tipo` = la acción específica del enunciado del libro***.

### Familia: input multimedia (escucha / lectura / vídeo)
- **`escucha`** — el alumno solo escucha (audio sin tarea posterior explícita).
- **`escucha_y_repite`** — el alumno escucha y reproduce oralmente.
- **`escucha_y_responde`** — el alumno escucha y produce una respuesta oral o escrita corta.
- **`lee_y_escucha`** — texto escrito acompañado de audio; el alumno sigue la lectura.
- **`ver_video`** — el alumno ve un vídeo.

### Familia: manipulación de elementos dados
- **`completa_huecos`** — rellenar huecos, celdas o slots predefinidos (frases con `_____`, tablas con celdas vacías, fichas con campos a completar).
- **`relaciona`** — emparejar elementos de dos columnas o conjuntos.
- **`ordena`** — poner elementos en una secuencia.
- **`clasifica`** — agrupar elementos en categorías dadas.
- **`seleccion_multiple`** — elegir entre alternativas (subrayar, marcar, elegir entre opciones).
- **`verdadero_falso`** — decidir si una afirmación es verdadera o falsa.

### Familia: respuesta a preguntas
- **`responder_preguntas_cerradas`** — responder preguntas con respuesta única o cerrada.
- **`responder_preguntas_abiertas`** — responder preguntas con respuesta libre o abierta.

### Familia: producción oral
- **`interaccion_oral`** — diálogo o intercambio oral entre alumnos.
- **`expresion_oral_libre`** — el alumno se expresa oralmente sin un guion cerrado.

### Familia: producción escrita
- **`produccion_escrita_guiada`** — el alumno escribe siguiendo un modelo o pautas dadas.
- **`expresion_escrita_libre`** — el alumno escribe libremente.

### Familia: otros
- **`busqueda_informacion`** — el alumno busca información (en internet, libro, entorno).
- **`tarea_final`** — actividad de cierre que integra varias destrezas o contenidos de la unidad.
- **`juego`** — actividad con mecánica lúdica.

> **Regla de prioridad** (de `reglas-operativas.md` §2): si el enunciado contiene una acción de manipulación (completa, marca, relaciona, subraya, ordena, clasifica), el `tipo` es esa acción, no el input previo (lee, escucha) ni la producción posterior (repite, cuenta). Ej.: *"Lee y completa"* → `completa_huecos`; *"Escucha y marca"* → `seleccion_multiple`.

> **Política de la enumeración:** cerrada y **versionable por expansión controlada**. Ampliar la lista exige documentación explícita y actualización paralela del schema, del validador y de `reglas-operativas.md`.

---

## Enumeración de `destreza` (6 valores — eje habilidad MCER)

> **Ubicación en el schema:** `schema-inventario.md` → §5b. **Criterios:** `reglas-operativas.md` → §2.3 (eje independiente de `tipo` y `enfoque`).

Enumeración cerrada de las **6 habilidades MCER** que una actividad puede poner en juego. Es uno de los tres ejes de clasificación de cada actividad (junto a `tipo` y `enfoque`) y describe **qué habilidad lingüística ejercita el alumno**.

### Los 6 valores
- **`comprension_auditiva`** — entender lo que se escucha.
- **`comprension_lectora`** — entender lo que se lee.
- **`expresion_escrita`** — producir texto escrito propio.
- **`expresion_oral`** — producir habla propia.
- **`interaccion_oral`** — intercambiar habla con otra persona (diálogo, conversación).
- **`mediacion`** — explicar, parafrasear, traducir o servir de puente entre lenguas, registros o interlocutores.

### Restricciones estructurales
- **Es una lista**, no un string suelto: una actividad puede ejercitar varias destrezas a la vez.
- **Mínimo 1 elemento**.
- **Orden alfabético obligatorio** dentro de la lista.
- **Cero duplicados**.

### Cómo se decide
La IA aplica las reglas de `reglas-operativas.md` §2.3.

> **Política:** cerrada y **versionable por expansión controlada**, igual que el resto de enumeraciones.

---

## Enumeración de `seccion` (7 valores normalizados)

> **Ubicación en el schema:** `schema-inventario.md` → §8.

Enumeración cerrada de las **7 secciones pedagógicas normalizadas** que estructuran una unidad del libro. El campo `seccion` de cada página debe tener uno de estos valores; el bloque top-level `secciones` (descrito más arriba) agrupa páginas y actividades por este eje.

### Los 7 valores
- **`vocabulario`** — páginas dedicadas al léxico (presentación de campos semánticos, ejercicios de vocabulario).
- **`gramatica`** — páginas dedicadas a contenido gramatical (paradigmas, reglas, ejercicios formales).
- **`comunicacion`** — páginas dedicadas a funciones comunicativas (saludar, presentarse, pedir información...).
- **`destrezas`** — páginas que integran varias habilidades MCER (lectura larga, comprensión auditiva extensa, expresión escrita guiada...).
- **`cultura`** — páginas con contenido sociocultural (costumbres, lugares, personajes, realidades hispánicas).
- **`evaluacion`** — páginas de evaluación o repaso al cierre de la unidad.
- **`reflexion`** — páginas de reflexión sobre el aprendizaje (autoevaluación extendida, metacognición).

### Relación con el índice del libro
Las 7 secciones derivan de la estructura editorial del libro impreso. `contenidos_indice` (top-level) lleva las cinco etiquetas literales del índice oficial; `seccion` es su **normalización canónica** para uso interno del sistema, ampliada con `evaluacion` y `reflexion` que el libro suele incluir aunque no figuren en el índice principal.

> **Política:** cerrada y **versionable por expansión controlada**, igual que el resto de enumeraciones.

---

## Enumeración de `tiempo` (4 valores — eje verbal)

> **Ubicación en el schema:** `schema-inventario.md` → §5d. **Criterios pedagógicos:** `reglas-operativas.md` → §5.1 y §5.2.

Enumeración cerrada de los valores válidos para el campo `tiempo` dentro de `actividad.tiempos_y_verbos[]` (y de `cuadro.tiempos_y_verbos[]`). Cubre tanto **tiempos finitos** (formas conjugadas en persona y número) como la categoría **forma no personal del verbo**, cuando esta se trabaja pedagógicamente fuera de perífrasis.

### Los 4 valores

- **`Presente`** — paradigma del presente de indicativo.
- **`Pretérito indefinido`** — paradigma del pretérito indefinido (perfecto simple).
- **`Imperativo`** — paradigma del imperativo (afirmativo y/o negativo según se trabaje).
- **`Infinitivo`** — cubre la categoría "forma no personal del verbo" cuando se trabaja pedagógicamente fuera de perífrasis (listas de verbos en infinitivo, ejercicios de identificación, etc.).

### Por qué `Perífrasis` no está en el enum

Las perífrasis (`ir a + infinitivo`, `tener que + infinitivo`, `querer + infinitivo`, etc.) **no son tiempos verbales**: son estructuras sintácticas donde un verbo auxiliar (conjugado en un tiempo real, típicamente Presente) se combina con un infinitivo. El verbo auxiliar conserva su tiempo real en `tiempo`, y la estructura se declara aparte en el campo opcional `estructura_perifrastica` del objeto verbal (ver schema §3.2). El infinitivo complemento NO se registra como entrada verbal separada — queda implícito en `estructura_perifrastica`.

### Por qué solo cuatro valores

`Participio` y `Gerundio` **no entran** en el enum: no aparecen en el corpus NC1. La enumeración es **canónica pero versionable por expansión controlada**: si NC2 los introduce, se amplían con documentación explícita y actualización paralela del schema, del validador y de `reglas-operativas.md`.

### Cómo se decide

La IA aplica las reglas pedagógicas de `reglas-operativas.md` §5.1.

> **Política:** cerrada y **versionable por expansión controlada**, igual que el resto de enumeraciones.

---

## Enumeración de `enfoque` (6 valores — eje dominio de contenido)

> **Ubicación en el schema:** `schema-inventario.md` → §5c. **Criterios:** `reglas-operativas.md` → §2.3 (eje independiente de `tipo` y `destreza`).

Enumeración cerrada de los **6 dominios de contenido** que una actividad puede trabajar. Es el tercer eje de clasificación (junto a `tipo` y `destreza`) y describe **qué dominio pedagógico** trabaja la actividad — no qué hace el alumno (eso es `destreza`) ni qué mecánica usa (eso es `tipo`).

### Los 6 valores
- **`gramatica`** — la actividad trabaja contenido gramatical (artículos, género, conjugación, posesivos, interrogativos...).
- **`vocabulario`** — la actividad trabaja contenido léxico (campos semánticos, palabras nuevas, asociaciones).
- **`comunicacion`** — la actividad trabaja funciones comunicativas (saludar, presentarse, pedir información, expresar gustos...).
- **`pronunciacion_ortografia`** — la actividad trabaja pronunciación, entonación, sílaba tónica, deletreo, dictado u ortografía relacionada con sonido.
- **`cultura`** — la actividad trabaja contenido cultural (costumbres, lugares, personajes, realidades hispánicas).
- **`transversal`** — la actividad no tiene un dominio único dominante; integra varios sin que uno destaque.

### Diferencia con `destreza`
- **`destreza`** describe **qué habilidad lingüística ejercita el alumno** (escuchar, leer, escribir, hablar, interaccionar, mediar).
- **`enfoque`** describe **qué dominio pedagógico** trabaja la actividad (gramática, vocabulario, comunicación...).

Son ejes independientes: una misma combinación de `tipo` y `destreza` puede tener distintos `enfoque` según qué contenido trabaje. Ejemplo:
- `tipo: completa_huecos` + `destreza: [comprension_lectora]` + `enfoque: gramatica` → "Completa con el artículo".
- `tipo: completa_huecos` + `destreza: [comprension_auditiva, comprension_lectora]` + `enfoque: vocabulario` → "Escucha y completa con la palabra adecuada del recuadro".

### Cómo se decide
La IA aplica las reglas de `reglas-operativas.md` §2.3. Nota estructural: `enfoque` es un **string suelto** (no lista), una actividad tiene **un único dominio principal**.

> **Política:** cerrada y **versionable por expansión controlada**, igual que el resto de enumeraciones.

---

## Fuentes PCIC y registries canónicos

> **Ubicación:** carpeta `fases/1-extraccion-inventario/`.

Cada dimensión lingüística del sistema usa **dos artefactos paralelos**: una **fuente PCIC** (Plan Curricular del Instituto Cervantes, nivel A1) que conserva el contenido pedagógico íntegro, y un **registry canónico** que fija los nombres operativos usados por el schema y validables por código.

| Dimensión | Fuente PCIC | Registry canónico | Estado registry |
|---|---|---|---|
| Vocabulario | `pcic-a1-vocabulario.json` | `campos-semanticos-canonicos.json` | Existente, poblado |
| Gramática | `pcic-a1-gramatica.json` | `gramatica-canonica.json` | Esqueleto |
| Pronunciación / ortografía | `pcic-a1-pronunciacion-ortografia.json` | `pronunciacion-ortografia-canonica.json` | Esqueleto |
| Tiempos y verbos | *(sin PCIC propio: paradigmas en gramática, verbos léxicos en vocabulario)* | `verbos-canonicos.json` | Existente, poblado |

**Archivo PCIC adicional fuera de las 4 dimensiones:**
- `pcic-a1-comunicacion.json` — Funciones comunicativas PCIC A1 (141 entradas). No alimenta ningún bloque top-level del schema, pero se conserva como recurso disponible para descripciones que requieran apoyo pragmático-comunicativo, o para futuros bloques.

**Source of truth del eje curso↔unidad:** `unidades/nc1-curso.json` (descrito en la sección "Top-level del inventario").

### Forma de los archivos PCIC

Todos los archivos `pcic-a1-*.json` siguen la misma estructura:

```jsonc
{
  "fuente":      "PCIC A1 — Plan Curricular del Instituto Cervantes, <inventario>",
  "nivel":       "A1",
  "origen":      "<ruta a la fuente original>",
  "fecha_copia": "<YYYY-MM-DD>",
  "categorias":  { /* árbol jerárquico de categorías → subcategorías → entradas */ }
}
```

Cada entrada del árbol guarda `contenido` (el término o regla) y, si aplica, `descripcion` (texto pedagógico) y `ejemplo`. El trim aplicado sobre las fuentes CAES descarta metadatos operativos (`id_original`, `tipo_contenido`, `nivel`, `orden`, `campos_originales`, `metadata_original`).

### Política de expansión a NC2

Cuando llegue NC2 (A1.2 / A2), cada par fuente↔registry se amplía según necesidad:
- Las **fuentes PCIC** pueden ampliarse a nuevos niveles (`pcic-a2-*.json`) o extenderse con secciones A2 dentro de las existentes.
- Los **registries canónicos** se amplían con nuevas entradas marcadas por nivel o por origen, sin romper compatibilidad con NC1.

---

## Sincronía con el validador

> **Ubicación en el schema:** `schema-inventario.md` → §13.

`schema-inventario.md` y `scripts/validar_inventario.py` son **contratos paralelos**: el primero declara la forma del JSON; el segundo la comprueba ejecutando código. Cualquier divergencia entre ambos es un bug y se resuelve antes del cierre. El validador debe chequear cinco categorías de regla, sin excepción.

> **Nota transitoria.** El validador actual no está alineado con el schema nuevo. Hasta el cierre de la migración (Paso 3 del plan), la validación contra el shape canónico es manual: lectura del schema + revisión visual. Las cinco categorías que vienen a continuación describen el contrato canónico final, no el estado vigente. Estado vivo, deuda específica y condiciones de retirada → Apéndice transitorio del schema (§A.1, §A.3) y nota transitoria del prompt.

### Claves obligatorias

Toda clave que el schema declara como obligatoria tiene que estar presente en el JSON, y el validador la marca como error duro si falta. Especialmente importantes:
- Los **3 ejes por actividad**: `tipo`, `destreza`, `enfoque`. Ninguna actividad puede omitirlos.
- Los **4 bloques top-level consolidados**: `vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`.

### Enumeraciones cerradas

Para cada enumeración, el validador rechaza todo valor fuera del set. Las enumeraciones cerradas del schema son siete:
- `tipo` — taxonomía de 20 valores (§5).
- `destreza` — 6 habilidades MCER (§5b).
- `enfoque` — 6 dominios de contenido (§5c).
- `tiempo` — 5 valores verbales (§5d).
- `tipo_cuadro` — 5 categorías pedagógicas de cuadro (§7).
- `seccion` — 7 secciones pedagógicas normalizadas (§8).
- `autoevaluacion.opciones` — 3 valores fijos en NC1 (§6).

Las enumeraciones son canónicas pero **versionables por expansión controlada** (ver "Naturaleza del contrato" al inicio del schema).

### Restricciones condicionales

Reglas que dependen del estado de otros campos. Cada una se aplica por el validador:
- **`imagen.descripcion` obligatoria si `imagen.presente=true`** (§10). Si la actividad declara que tiene imagen, debe describirla.
- **`autoevaluacion` con valores fijos NC1 cuando `curso=="nc1"`** (§6). El bloque solo admite los tres strings canónicos del curso.
- **`destreza` en orden alfabético, sin duplicados** (§5b). La lista se ordena al guardar y se rechaza si contiene repetidos.
- **Referencias canónicas existentes en los registries** (`campos-semanticos-canonicos.json`, `verbos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`). Cualquier referencia canónica usada en el JSON tiene que existir en su registry.
- **Formato canónico de `fuentes`** (§9.5 regex). Toda fuente debe encajar en `^(p\d+-act\d+(@R)?|cuadro@p\d+(#\d+)?)$`.
- **`descripcion` obligatoria en cada entrada de `principal`** de cada bloque consolidado. En `recurrente` es opcional.

### Claves opcionales declaradas

Las claves opcionales **del top-level** del inventario (`autoevaluacion`, `_nota_unidad_atipica`, `_decisiones_ia`, `_migracion_rediseno`) deben figurar en la lista `CLAVES_TOP_OPCIONALES` del validador. Si no, el validador emite aviso al encontrarlas en el JSON aunque sean correctas. Las marcas internas `_pendiente_canon` y `_funcion_ambigua` **no son top-level**: solo viven dentro de una actividad o de una entrada de categoría en bloques consolidados (ver §14 del schema y sección "Marcas internas declaradas en el contrato" en este glosario).

### Marcas internas que bloquean cierre

Las marcas `_pendiente_canon` y `_funcion_ambigua` (ver §14 del schema) son **error duro** para el validador: su presencia impide declarar el inventario cerrado, independientemente del resto de chequeos. Las marcas `_decisiones_ia` y `_migracion_rediseno` no bloquean cierre (son auditoría y metadata respectivamente).

> Estado actual de la alineación validador↔schema → Apéndice transitorio del schema (§A.3).

---

## Marcas internas declaradas en el contrato

> **Ubicación en el schema:** `schema-inventario.md` → §14. **Detalle de ciclo de vida:** `reglas-operativas.md` → §5.9.

Las **marcas internas** son claves opcionales con prefijo `_` (subrayado) que el JSON puede llevar para señalar estados especiales. Tres están declaradas como permanentes en el contrato; la cuarta (`_migracion_rediseno`) es transitoria y vive en el Apéndice del schema.

### `_pendiente_canon`

- **Tipo:** string literal con el valor `"_pendiente_canon"`.
- **Dónde aparece:** dos ubicaciones distintas dentro del JSON, ambas en bloques top-level consolidados.
  - **(a) Como valor de un campo de categoría canónica.** Se usa cuando todavía no se ha decidido qué categoría canónica del registry asignar a un elemento. Ejemplo: `"categoria_canonica": "_pendiente_canon"`.
  - **(b) Como clave transitoria dentro de un sub-bloque `principal` o `recurrente`** de cualquiera de los 4 bloques top-level. Agrupa, bajo esa clave provisional, todas las palabras/elementos que aún no tienen canónico asignado. Ejemplo: `"recurrente": { "_pendiente_canon": { "items": [...] } }`.
- **¿Bloquea cierre?** **Sí** — error duro. Toda aparición de `_pendiente_canon` debe resolverse (asignándole canónico real) antes de declarar el inventario cerrado.
- **Para qué sirve:** permite avanzar la extracción sin parar cuando la IA no tiene aún canónico seguro, y obliga a cerrar la duda después.

### `_funcion_ambigua`

- **Tipo:** booleano (`true` o `false`; en la práctica solo se escribe cuando es `true`).
- **Dónde aparece:** como campo opcional dentro de una **entrada de categoría** en cualquier bloque consolidado, o dentro de una **actividad** concreta.
- **Forma exacta:** `"_funcion_ambigua": true`.
- **¿Bloquea cierre?** **Sí** — error duro. La ambigüedad funcional debe resolverse antes de declarar el inventario cerrado.
- **Para qué sirve:** marca que la IA detectó que la función pedagógica de un elemento o actividad no se ha podido desambiguar (ej. una palabra que podría pertenecer a dos campos semánticos, o una actividad cuyo `tipo` no encaja claramente en ninguno de los 20 valores). Fuerza revisión humana.

### `_decisiones_ia`

- **Tipo:** array de strings.
- **Dónde aparece:** dos ubicaciones posibles.
  - Como campo opcional **top-level del inventario** (decisiones globales de la corrida).
  - Como campo opcional **dentro de una actividad concreta** (decisiones tomadas mientras se procesaba esa actividad). Ambas instancias coexisten sin conflicto.
- **Forma exacta:** `"_decisiones_ia": ["U1-p13-act7: 'ella' descartado como sujeto tras preposición 'sin'", ...]`. Cada string es una decisión, con prefijo de localización si aplica.
- **¿Bloquea cierre?** **No.** Es persistente, sirve como auditoría posterior.
- **Para qué sirve:** dejar registro de decisiones no triviales (ambigüedades resueltas, opciones descartadas, razonamientos no obvios) que un humano podría querer revisar semanas más tarde.

### `_migracion_rediseno` *(transitoria)*

Clave opcional del top-level admitida **solo mientras dure la migración** del modelo viejo al nuevo. Marca que el inventario fue reescrito desde el modelo viejo y deja constancia de hallazgos relevantes para fase 2 (anticipaciones detectadas, etc.). **No bloquea cierre.** Detalle, shape exacto y condiciones de retirada → Apéndice transitorio del schema (§A.2).

### Reglas comunes

**El prefijo `_` es convención de naming, no clase contractual.** Indica "campo interno operativo no editorial": no es contenido pedagógico ni se muestra al alumno. Bajo esta convención conviven tres clases distintas:

- **Marcas internas §14** del schema: `_pendiente_canon`, `_funcion_ambigua`, `_decisiones_ia`. Tienen semántica de marca operativa con shape, ubicación y ciclo de vida definidos en §14.
- **Claves opcionales del top-level con nombre técnico** (no son marcas §14): `_nota_unidad_atipica` (§11) y `_migracion_rediseno` (§A.2, transitoria). Usan el prefijo `_` por convención de naming, pero no llevan reglas de marca §14.
- **Metadata extracontractual `_fixture_*`** (§A.5): claves usadas solo en fixtures exploratorias (`unidad: "Np"`). **No forman parte del contrato canónico**; el dashboard las tolera, el validador las ignora. Un inventario canónico (`unidad: N` entero) no debe llevar ninguna clave `_fixture_*`.

**Reglas específicas de las marcas §14:**

- **Bloqueantes vs no bloqueantes:** `_pendiente_canon` y `_funcion_ambigua` **bloquean cierre** — deben resolverse o eliminarse antes de declarar el inventario cerrado. `_decisiones_ia` no bloquea (es auditoría persistente).
- **Validador:** detecta las marcas bloqueantes como error duro (cuando el validador esté alineado, ver Apéndice transitorio del schema).

**Reglas comunes a ambas clases:**

- **Naming:** ningún otro campo del contrato puede empezar con `_`, salvo los explícitamente declarados (§11, §14, §A.2 del schema). Si aparece una nueva necesidad de campo `_*`, se documenta en la sección que corresponda.
