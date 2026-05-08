# Reglas operativas — Decisión, clasificación, población y unidades atípicas

> **Responsabilidad:** guía de decisión compacta y priorizada. Reúne lo que el modelo necesita decidir durante la extracción: qué tipo asignar, qué clasificar como cuadro/actividad/nota, cómo poblar campos cuyo shape ya está fijado en `schema-inventario.md`, cómo tratar unidades atípicas.
>
> **No contiene:** forma del JSON (vive en `schema-inventario.md`), convenciones de transcripción específicas (sílaba tónica, "primer ítem resuelto", marcadores de diálogos, formato de sopas de letras), ni casos históricos resueltos. Esos viven en `convenciones-y-casos.md` (a poblar en A4.2c).
>
> **Single source of truth de precedencias:** las reglas de precedencia (qué clasificar como actividad / cuadro / nota / autoevaluación, en qué orden, con qué excepciones) viven **exclusivamente aquí**. Cualquier otro archivo que necesite invocarlas lo hace por referencia, no por copia. Si una precedencia aparece reescrita en `prompt.md`, `CLAUDE.md` o cualquier otro artefacto, es un bug del refactor.

---

## 1. Precedencia entre actividad / cuadro / nota / autoevaluación

Para cada elemento visible en una página del libro, determinar en este orden qué es:

1. **¿Tiene número de actividad** (1, 2, 3...) **y pide producción del alumno** (escuchar, repetir, escribir, relacionar...)? → **Actividad** con `tipo` de la taxonomía cerrada (§2).
2. **¿Es "Para aprender"?** → Es **actividad** solo si pide producción al alumno (verbo imperativo); si es **puramente informativo** (lista de reglas o referencia, sin instrucción), es **cuadro**. Ver §4 para la bifurcación con criterio decisional.
3. **¿Es "Observa"?** → Siempre **nota**, aunque use el imperativo "Observa". Excepción explícita: "Observa" no pide producción del alumno; llama la atención sobre información de referencia. Nunca se convierte en actividad. **Dónde va según su contexto:**
   - Si acompaña a una **actividad**: en `datos._nota` de esa actividad.
   - Si acompaña a un **cuadro**: en `cuadro.observaciones` (campo opcional del schema del cuadro, ver `schema-inventario.md` §4).
4. **¿Es una tabla o recuadro de referencia sin número ni instrucción de producción?** → `cuadro` con `tipo_cuadro` apropiado (§3).
5. **¿Es el bloque "Mis resultados en esta unidad son: …"** que aparece al pie de la última página de cierre con tres opciones y emoticonos? → **bloque `autoevaluacion` top-level** (no actividad, no cuadro, no nota). Ver §6.

**Precedencia:** las excepciones explícitas (reglas 2, 3, 5) tienen prioridad sobre la regla general (regla 1). La regla general solo aplica cuando ninguna excepción encaja.

---

## 2. Cómo asignar `tipo` a una actividad (taxonomía cerrada de 20 valores)

Enumeración cerrada en `schema-inventario.md` §5.

### 2.1 Regla operativa: `tipo` = la acción específica del enunciado

> **El `tipo` describe la acción que el enunciado del libro pide al alumno.** Si el enunciado encadena varias acciones, el tipo lo determina **la última acción que pide producción concreta**. Si el enunciado solo pide absorber input (leer, escuchar, mirar) sin acción posterior, el tipo refleja literalmente esa absorción.
>
> El `tipo` es independiente de `destreza` y `enfoque`. `destreza` describe **qué habilidad lingüística ejercita el alumno** (lista de valores MCER); `enfoque` describe **qué dominio de contenido pedagógico** trabaja (string). Ver §2.3 para los tres ejes.

### 2.2 Tabla canónica de los 20 tipos

| `tipo` | Acción del enunciado | Ejemplos del libro |
|---|---|---|
| `escucha` | "Escucha" / "Mira X y escucha" — input puro auditivo, sin lectura de texto extenso ni acción posterior. Apoyo visual no textual (mapa, imagen, foto) admisible | "Mira el mapa y escucha el nombre de los países. Observa la pronunciación." |
| `lee_y_escucha` | "Lee y escucha" / "Lee y escucha el diálogo" — input combinado lectura + audio, sin acción posterior | "Lee y escucha." (fichas de presentación, diálogos) |
| `ver_video` | "Mira el vídeo" — input con video, con o sin texto/audio acompañante | "Mira el vídeo o lee y escucha el diálogo." |
| `escucha_y_repite` | "Escucha y repite" — input auditivo + producción oral repetitiva | vocabulario, abecedario, interrogativos |
| `escucha_y_responde` | "Escucha y responde" oralmente, sin texto delante | (genérico) |
| `completa_huecos` | "Completa", "Completa con palabras del recuadro", "Lee y completa", "Escucha y completa la tabla/ficha" | rellenar huecos en frases, fichas, tablas |
| `relaciona` | "Relaciona X con Y" (típicamente con líneas conectoras) | números↔palabras, preguntas↔respuestas |
| `ordena` | "Ordena estos elementos" | (genérico) |
| `clasifica` | "Clasifica X en categorías" | (genérico) |
| `seleccion_multiple` | "Subraya el verbo correcto", "Marca", "Elige", "Escucha y marca" | subrayar entre alternativas, marcar bingo |
| `verdadero_falso` | "Marca verdadero o falso" | (genérico) |
| `responder_preguntas_cerradas` | "Contesta a las preguntas" cuando la respuesta es **concreta y sale del input** (texto leído, audio, video) | "Lee y contesta a las preguntas" sobre un texto |
| `responder_preguntas_abiertas` | "Contesta a las preguntas" cuando la respuesta es **personal/libre del alumno** | "Contesta: ¿Cómo te llamas? ¿De dónde eres?" |
| `interaccion_oral` | "En parejas", "Pregunta y contesta a tu compañero", "Saluda a tu compañero" | diálogo en parejas con estructura |
| `expresion_oral_libre` | "Preséntate", "Practica con palabras nuevas", "Presenta a tu compañero a la clase" | producción oral sin guion cerrado |
| `produccion_escrita_guiada` | "Escribe frases con…", "Forma frases", "Coloca el artículo", "Realiza las sumas y escribe", "Describe X con sus colores" | producción escrita siguiendo modelo/regla, sin huecos predefinidos |
| `expresion_escrita_libre` | "Escribe a tu amigo sobre…", "Escribe un correo", "Escribe un texto sobre…" | redacción libre sobre un tema |
| `busqueda_informacion` | "Busca información sobre…" | (genérico) |
| `tarea_final` | "Cread vuestro propio diálogo" + pasos en grupo (tarea colaborativa final) | crear y representar un diálogo |
| `juego` | "Juega a…" | "Juega al veo, veo" (cuando la actividad es jugar como tal, no como interacción genérica) |

**Reglas de desempate cuando el enunciado encadena varias acciones:**

1. **Si el enunciado solo pide ver/mirar el video** sin acción posterior (ej. "Mira el vídeo") → `ver_video`. **Si hay manipulación posterior** ("Mira el vídeo y completa", "Mira el vídeo o lee el diálogo y marca verdadero/falso") → la regla 2 se impone (la manipulación manda), aunque el video esté presente.
2. **Si el enunciado contiene una acción de manipulación** (completa, marca, relaciona, subraya, ordena, clasifica) **en cualquier punto del enunciado** → el tipo es esa acción, no el input ni las acciones de salida (repetir, contar, etc.). La manipulación manda sobre input previo y sobre producción posterior. Ej.: "Lee y completa" → `completa_huecos`; "Escucha y marca" → `seleccion_multiple`; "Mira el vídeo y completa" → `completa_huecos`; "Completa, escucha y repite" → `completa_huecos` (el completar tiene mayor impacto pedagógico aunque le siga repetir).
3. **Si el enunciado pide responder preguntas:**
   - Respuesta concreta que sale del input (texto leído, audio, video) → `responder_preguntas_cerradas`. Destreza: solo `comprension_lectora` (o `comprension_auditiva` si el input es audio); SIN `expresion_escrita` aunque el alumno escriba la respuesta.
   - Respuesta personal/libre del alumno, **individual** (sin compañero), sin texto-fuente → `responder_preguntas_abiertas`. Destreza: `expresion_escrita` si el libro pide escribir; `expresion_oral` si el libro pide responder oralmente. Verificar contra el enunciado real.
   - Respuesta personal/libre **en parejas** (pregunta y responde a tu compañero) → `interaccion_oral`. Destreza: `[interaccion_oral]`. La interacción oral con compañero prevalece sobre la formulación "responder preguntas".
4. **Si el enunciado solo pide input** (leer, escuchar, mirar) sin acción posterior → `lee_y_escucha` o `ver_video` según el medio.
5. **`completa_huecos` vs `produccion_escrita_guiada`** (frontera frecuente):
   - Si el ejercicio presenta **huecos, celdas o slots predefinidos** que el alumno rellena (frase con `_____`, tabla con celdas vacías, ficha con campos a completar) → `completa_huecos`. Ejemplos: "Completa las frases con la forma del verbo ser", "Completa la tabla con el masculino/femenino", "Escucha y completa la ficha".
   - Si el ejercicio NO tiene huecos predefinidos y el alumno **construye** frases o etiquetas a partir de un modelo, una imagen o una regla → `produccion_escrita_guiada`. Ejemplos: "Coloca el artículo el/la a estos nombres" (no hay hueco, el alumno escribe el artículo delante), "Forma frases tomando un elemento de cada columna", "Escribe frases con el verbo ser", "Describe estos objetos con sus colores", "Escribe el nombre de estos objetos".

### 2.3 Sobre `destreza` y `enfoque` (dos ejes independientes de `tipo`)

Toda actividad se clasifica en **tres ejes ortogonales**:

| Eje | Pregunta que responde | Forma | Schema |
|---|---|---|---|
| `tipo` | ¿Qué acción pide el enunciado? (mecánica) | string (1 valor de 20) | §5 |
| `destreza` | ¿Qué habilidad lingüística ejercita el alumno? | lista (≥1 valores de 6, orden alfabético) | §5b |
| `enfoque` | ¿Cuál es el dominio de contenido pedagógico? | string (1 valor de 6) | §5c |

Los tres ejes son independientes. Una misma `tipo: completa_huecos` puede tener distintas combinaciones `destreza`/`enfoque` según qué ejercicio sea.

#### `destreza` — eje habilidad MCER pura (lista, 6 valores, orden alfabético)

- `comprension_auditiva` — escuchar (audio o video).
- `comprension_lectora` — leer un texto/diálogo/preguntas/items.
- `expresion_escrita` — producir texto propio.
- `expresion_oral` — producir habla propia (turno solo, monólogo, descripción oral).
- `interaccion_oral` — intercambio oral con compañero.
- `mediacion` — reformular, resumir, traducir, explicar a otro lo entendido.

**Regla de asignación:**

1. **Inputs presentes → siempre se declaran.** Si hay texto que leer → `comprension_lectora`. Si hay audio o video que escuchar → `comprension_auditiva`. Pueden coexistir.
2. **Output del alumno → la destreza correspondiente.** Si escribe → `expresion_escrita`. Si habla solo → `expresion_oral`. Si intercambia con compañero → `interaccion_oral`. Si reformula/resume/traduce → `mediacion`.
3. **Cero "destrezas de contenido".** `gramatica` y `vocabulario` no son destrezas; son `enfoque` (ver siguiente bloque).

#### `enfoque` — eje dominio de contenido (string, 6 valores)

- `gramatica` — manipulación de formas gramaticales (artículos, conjugación, género/número, concordancia, orden de palabras).
- `vocabulario` — manipulación de léxico (banco temático, palabra-imagen, sopa de letras, clasificar por campo semántico, definiciones).
- `comunicacion` — funciones comunicativas / fórmulas pragmáticas (saludos, presentarse, preguntar la hora, pedir información).
- `fonetica` — pronunciación, ortografía fonética, acento, entonación.
- `cultura` — contenido sociocultural (ciudades, costumbres, gastronomía, calendarios, personajes culturales).
- `transversal` — actividad sin foco de dominio específico, solo ejercita habilidades (lectura/escucha de comprensión genérica, tarea final que cruza dominios). Nombre intencionalmente distinto del valor `destrezas` de `seccion` para evitar pegar el eje a la clasificación editorial de la página.

**Regla de asignación:** un único `enfoque` por actividad — el dominante. Si una actividad mezcla varios (ej. completar diálogo + repasar léxico), elegir el que el enunciado prioriza. Ante duda real, consultar al autor.

**Relación con `seccion` (nivel página):** `seccion` clasifica la página según el índice editorial; `enfoque` clasifica la actividad concreta. Pueden divergir: una página `seccion: gramatica` puede contener una actividad `enfoque: transversal` (lectura comprensiva sin foco gramatical) y otra `enfoque: gramatica` (cloze de artículos). Capturar el foco real, no el de la página.

#### Regla de asignación de `expresion_escrita`

`expresion_escrita` se asigna cuando el alumno **produce contenido escrito propio** — es decir, cuando lo que escribe sale de su memoria, conocimiento o criterio, no de un input dictado o de un banco dado. Aplica tanto a textos elaborados (frase, párrafo, correo, presentación, respuesta abierta) como a **listas de palabras evocadas** (ej. "escribe los países que recuerdas").

`expresion_escrita` **NO** se asigna en:
- **Mecánicas de manipulación de elementos dados** (`completa_huecos`, `relaciona`, `ordena`, `clasifica`, `seleccion_multiple`, `verdadero_falso`, marcar, subrayar, unir con flechas): la destreza es la **comprensión** que permite hacer la elección correcta. Aplica también a "Completa con el artículo" (dada la frase, el alumno deduce el artículo: aplica regla, no produce contenido propio) y a "Completa con la palabra del recuadro" (transcribe del banco).
- **Transcripciones de input** (dictado, "Escucha y escribe"): el alumno transcribe lo escuchado, no produce contenido propio. La destreza dominante es `comprension_auditiva`.
- **Respuestas cerradas con palabra del texto**: el alumno copia/extrae del input. Solo `comprension_lectora`.

Resumen del criterio: **¿el alumno está produciendo contenido propio o transcribiendo/aplicando reglas a partir de un input dado?** Si es lo primero, `expresion_escrita`. Si es lo segundo, no.

#### Heurística `vocabulario` vs `fonetica` para "escucha y repite" / "escucha y escribe"

Casos donde el alumno trabaja palabras pero también pronunciación:

- Si las palabras están agrupadas por **campo léxico** (cognados, países, profesiones, números como léxico) y el aprendizaje es saber qué significan o reconocerlas → `enfoque: vocabulario`.
- Si las palabras o sonidos están agrupados por **dificultad fonética** (alfabeto, combinaciones c/qu, j/g, z/c) y el aprendizaje es la pronunciación o la ortografía fonética → `enfoque: fonetica`.
- **Deletrear** (en voz alta o por escrito) → siempre `fonetica` (es ortografía fonética).
- **Dictado** ("escucha y escribe") → siempre `fonetica` (la habilidad ejercitada es reconstruir la grafía a partir del sonido), incluso si el contenido dictado es léxico (ej. dictado de números).

#### Ejemplos canónicos (tres ejes a la vez)

- "Lee y escucha el diálogo" → `tipo: lee_y_escucha` + `destreza: [comprension_auditiva, comprension_lectora]` + `enfoque: transversal`.
- "Completa con el artículo el/la/los/las" → `tipo: completa_huecos` + `destreza: [comprension_lectora]` + `enfoque: gramatica`.
- "Escucha y completa con la palabra adecuada del recuadro" → `tipo: completa_huecos` + `destreza: [comprension_auditiva, comprension_lectora]` + `enfoque: vocabulario`.
- "Escribe un correo a tu amigo" → `tipo: expresion_escrita_libre` + `destreza: [expresion_escrita]` + `enfoque: comunicacion`.
- "Lee el texto y contesta a las preguntas" (cerradas, respuesta del texto) → `tipo: responder_preguntas_cerradas` + `destreza: [comprension_lectora]` + `enfoque: transversal`.
- "Escribe sobre tu rutina diaria" (respuesta abierta elaborada) → `tipo: responder_preguntas_abiertas` + `destreza: [expresion_escrita]` + `enfoque: comunicacion`.
- "Escucha y repite" → `tipo: escucha_y_repite` + `destreza: [comprension_auditiva, expresion_oral]` + `enfoque: fonetica`.
- "Pregunta a tu compañero por su familia" → `tipo: interaccion_oral` + `destreza: [interaccion_oral]` + `enfoque: comunicacion`.
- "Relaciona los relojes con los horarios digitales" (con escucha previa) → `tipo: relaciona` + `destreza: [comprension_auditiva, comprension_lectora]` + `enfoque: vocabulario`.

### 2.4 Política de la enumeración

- La enumeración de 20 valores es **provisional y revisable a nivel global del proyecto**. No se amplía ni se cambia ad hoc por unidad. Cualquier modificación del set requiere decisión cerrada en PROCESO-MAESTRO antes de aplicarse en `schema-inventario.md` y en `validar_inventario.py` (regla de no-divergencia).
- Ante un caso ambiguo durante una extracción nueva: marcar como TODO en el JSON y consultar al autor antes de cerrar el inventario.

---

## 3. Cómo asignar `tipo_cuadro` (5 valores)

Enumeración cerrada en `schema-inventario.md` §7.

Cuando una página tiene un cuadro de referencia (clasificado según §1 regla 4), asignar `tipo_cuadro` según su naturaleza pedagógica:

- **`gramatical`** — tablas de conjugación, paradigmas morfológicos (artículos, género, posesivos, interrogativos, demostrativos), reglas ortográficas de uso gramatical.
- **`lexical`** — listas ilustradas de vocabulario, tablas de campos semánticos, colores, familias de palabras.
- **`fonetico`** — cuadros de pronunciación u ortografía fonética (c/qu, z/c, g/gu, entonación, acento...).
- **`cultural`** — cuadros con información sociocultural (saludos, costumbres, diálogos en contexto cultural, fórmulas sociales).
- **`comunicativo`** — cuadros de uso pragmático (registro, formalidad/informalidad, turnos de conversación, cortesía).

> **Ortogonalidad:** `seccion` de la página y `tipo_cuadro` son independientes. Un cuadro fonético puede aparecer en la sección `gramatica`; un cuadro léxico puede estar en `vocabulario`. No forzar que coincidan.

**Capturar todo el contenido visible del cuadro** (filas, columnas, celdas, ejemplos al pie) en `cuadro.contenido`.

---

## 4. Casos límite: "Para aprender" y "Observa"

**"Para aprender"** — Cajas que el libro destaca con esa etiqueta. Pueden ser de dos naturalezas:

| Naturaleza | Ejemplo | Clasificación |
|---|---|---|
| **Con tarea** (verbo imperativo dirigido al alumno: "haz", "escribe", "completa") | U3-p37 "Hacer un cuaderno de vocabulario" — *"Mira el cuaderno de Ronaldo... Escribe palabras nuevas y tradúcelas"* | **Actividad** con `tipo: produccion_escrita_guiada`, `datos.subtipo: "para_aprender"` |
| **Solo informativa** (lista de reglas o referencia, sin verbo imperativo) | U2-p25 "Uso de las mayúsculas" — solo lista de reglas con ejemplos, sin instrucción al alumno | **Cuadro** con `tipo_cuadro` apropiado según contenido (`gramatical`, `lexical`, etc.) |

**Criterio decisional:** ¿el bloque contiene verbo imperativo dirigido al alumno? Si sí → actividad. Si solo es información de referencia → cuadro.

**"Observa"** — Notas que llaman la atención sobre aspectos del idioma. Son **notas**, no actividades ni cuadros:
- Si acompaña a una **actividad** → `datos._nota`.
- Si acompaña a un **cuadro** → `cuadro.observaciones`.

---

## 5. Reglas de población de campos (shape en schema, contenido aquí)

### 5.1 `vocabulario_consolidado`: distribución entre los 3 bloques

Tres bloques, cada uno agrupado por categoría/campo semántico:

- **`principal`** — Vocabulario **declarado en el índice de la unidad** (ej: si el índice dice "Vocabulario: Parientes", aquí va el léxico de parentesco trabajado en la sección Vocabulario). Agrupado por campo semántico (Familia, Profesiones, Lugares, etc.).
- **`recurrente`** — Vocabulario que aparece en **varias secciones** de la unidad (no solo Vocabulario). Por ejemplo, si "merendar" aparece en Vocabulario Y en Comunicación Y en Destrezas, va aquí. Agrupado por categoría temática.
- **`comprension`** — Léxico que **aparece y afecta la comprensión** del estudiante aunque no se trabaje explícitamente. Por ejemplo, palabras del cómic en la sección Cultura, asignaturas mencionadas, conectores básicos. Agrupado por categoría.

**`_descripcion`** dentro de cada bloque explica de qué va. Útil al revisar el JSON.

### 5.2 `secciones` (top-level): construcción del índice

- **Si una sección no existe en la unidad**, dejarla con `{ "paginas": [], "actividades_ids": [] }` (no omitir la clave).
- **`actividades_ids`** lista los IDs de actividad de cada sección, **en orden de aparición**. Permite acceso directo sin recorrer todas las páginas.

### 5.3 `seccion` por página: cómo determinarla

Mapeo canónico avalado por la práctica actual (oráculo: inventarios trackeados U0, U1, U3):

| Header del libro | Valor normalizado | Avalado en |
|---|---|---|
| Vocabulario | `vocabulario` | U1, U3 |
| Gramática | `gramatica` | U1, U3 |
| Comunicación | `comunicacion` | U1, U3 |
| Destrezas | `destrezas` | U1, U3 |
| Cultura | `cultura` | U1, U3 |
| Página de cierre de unidad con bloque `autoevaluacion` (U1-p21, U3-p43) | `evaluacion` | U1-p21, U3-p43 |

**Sobre `reflexion`:** está incluido en la enumeración cerrada de `seccion` (`schema-inventario.md` §8) pero **no tiene uso documentado en los inventarios actuales** (U0, U1, U3 no asignan `reflexion` a ninguna página). El criterio para distinguir `evaluacion` vs `reflexion` se documentará cuando aparezca el primer caso real. Hasta entonces, **usar `evaluacion` por consistencia con el oráculo**.

**Páginas que continúan una sección anterior** (típicamente con etiqueta visual tipo "(cont.)"): se les asigna **la misma clave normalizada** que la página origen. La etiqueta "(cont.)" del libro NO va al JSON; la sección sigue siendo la misma.

**Caso unidades atípicas:** ver §7.

### 5.4 `respuestas`: contenido y formato

Estructural en schema (`schema-inventario.md` §10): siempre presente como lista, vacía si no aplica.

**Cuando aplica:** recoge la respuesta esperada tal como aparece en el libro del profesor (suele estar marcada en color o en el margen). Cada respuesta como un string en la lista.

**Formatos:**
- **Selección múltiple:** indicar la opción correcta junto con su texto: `"3. → c) Una mezcla de dibujo y texto"`.
- **Verdadero/Falso:** `"1. La frase X — V"`.
- **Cloze / completar:** la respuesta completa o la palabra que va en el hueco, según convenga reproducir el ítem original (ver `convenciones-y-casos.md` para ejemplos).

### 5.5 `audio`, `imagen`, `video`: cuándo `presente=true`

Estructural en schema (`schema-inventario.md` §10): siempre presentes como sub-objetos.

**Marcar `presente=true`** cuando la actividad realmente requiere ese medio: hay un ícono de audio/video junto a la actividad, hay una imagen visible que el alumno consulta, hay un video referenciado. En caso contrario `presente=false`.

**`imagen.descripcion`:** obligatoria si `imagen.presente=true` (la restricción la aplica el validador). Suficientemente detallada para que un agente que no ve la imagen pueda entender qué muestra.

### 5.6 `campo_semantico`: cuándo aplica

Estructural en schema (`schema-inventario.md` §10): str opcional.

**Cuándo se usa:** cuando el contenido lingüístico de la actividad pertenece a un campo semántico identificable (Familia, Profesiones, Lugares, etc.).

**Decisión pendiente del autor:** ¿solo en sección vocabulario o en cualquier sección que toque vocabulario? Por ahora, **liberal**: cualquier actividad cuyo contenido pertenezca a un campo semántico lo lleva.

### 5.7 `datos.items_libro`: literalidad obligatoria

Estructural en schema (`schema-inventario.md` §12): lista de strings, obligatoria en actividades de cierto tipo (lista canónica en `validar_inventario.py:TIPOS_QUE_REQUIEREN_ITEMS`).

**Regla de literalidad (la más importante):** `items_libro` debe contener **el texto literal del libro**, con los huecos marcados como `_____` (5 guiones bajos). Nunca sustituir el enunciado por la respuesta. Nunca inventar el enunciado.

**Para qué tipos aplica:** completar huecos, opción múltiple, ordenar, clasificar, relacionar, verdadero/falso, y similares.

> Ejemplos correctos e incorrectos → `convenciones-y-casos.md` (a migrar en A4.2c).

---

## 6. Cuándo se incluye u omite el bloque `autoevaluacion`

`autoevaluacion` es opcional a nivel top-level (forma del campo en `schema-inventario.md` §6).

**Regla de decisión:**
- **Unidad regular (U1-U9):** el bloque está presente. Aparece al pie de la última página con tres opciones canónicas y emoticonos.
- **Unidad atípica sin bloque (ej. U0 "Punto de partida"):** el campo `autoevaluacion` se omite por completo (no se pone `null` ni vacío; simplemente no aparece la clave).

**Indicadores en el libro:**
- Si la última página de la unidad muestra el bloque "Mis resultados en esta unidad son: …" con tres opciones y emoticonos → presente.
- Si no aparece visualmente → omitido.

---

## 7. Reglas para unidades atípicas (introductorias)

Algunas unidades NO tienen las 5 secciones canónicas (vocabulario / gramática / comunicación / destrezas / cultura). Caso típico: la unidad introductoria **U0 "Punto de partida"** que es pre-A1.

**Cuando ocurra:**
1. Mapear todo el contenido a la sección que más se ajuste (en U0: `vocabulario`, porque todo el contenido es léxico-fonético).
2. Las demás secciones canónicas quedan vacías: `{ "paginas": [], "actividades_ids": [] }`.
3. Añadir clave top-level `_nota_unidad_atipica` con explicación de por qué es atípica y cómo se mapeó (forma de la clave en `schema-inventario.md` §11).
4. En `contenidos_indice`, las secciones que no aplican llevan el valor `"(no aplica en esta unidad introductoria)"`.

> Ejemplo JSON canónico de U0 → `convenciones-y-casos.md` (a migrar en A4.2c).

---

## 8. Estado del source of truth de las reglas decisionales

Tras A4.2b, el reparto entre archivos queda así:

| Tipo de regla | Archivo |
|---|---|
| Forma del JSON (estructura, tipos, enumeraciones, restricciones validables) | `schema-inventario.md` |
| Precedencias entre actividad/cuadro/nota/autoevaluación | **este archivo** (§1) |
| Distinción `completa_huecos` vs `produccion_escrita_guiada` | **este archivo** (§2.1) — antes en `prompt.md`, restaurado en v10.51, migrado aquí en A4.2b |
| Criterios para asignar cada uno de los 20 tipos | **canonizados en §2** (regla operativa: el `tipo` = la acción específica del enunciado del libro) |
| Cómo asignar `tipo_cuadro` | **este archivo** (§3) |
| "Para aprender" / "Observa" | **este archivo** (§4) |
| Reglas de población de cada campo | **este archivo** (§5) |
| Bloque `autoevaluacion`: cuándo presente/omitido | **este archivo** (§6) |
| Unidades atípicas: cuándo y cómo aplicar | **este archivo** (§7) |
| Convenciones de transcripción del libro al JSON (sílaba tónica, primer ítem resuelto, marcadores de diálogos, formato de sopas de letras) | `convenciones-y-casos.md` (a poblar en A4.2c) |
| Ejemplos correctos/incorrectos de `items_libro` | `convenciones-y-casos.md` (a poblar en A4.2c) |
| Casos históricos resueltos | `convenciones-y-casos.md` (a poblar en A4.2c) |
