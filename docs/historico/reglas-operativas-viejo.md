# Reglas operativas — Decisión, clasificación, población y unidades atípicas

> 🗄️ **ARCHIVO HISTÓRICO — NO USAR OPERATIVAMENTE (cerrado 2026-05-13, movido a `docs/historico/` el 2026-05-15 con v10.116).**
>
> Este documento es el **reservorio histórico** del modelo anterior al rediseño IA-first de fase 1. **No es autoridad operativa.** La autoridad operativa vigente vive en `fases/1-extraccion-inventario/reglas-operativas.md` (reescrita desde cero el 2026-05-13 bajo el modelo IA-first, con el shape del schema nuevo y los 4 bloques consolidados).
>
> **Reglas para este archivo:**
> - **No consultar** durante una corrida de extracción. Consultar el archivo vivo.
> - **No editar** salvo para corregir referencias claramente rotas o para extraer contenido que se vaya a absorber en el archivo vivo (en cuyo caso el cambio se hace allí, no aquí).
> - **No referenciar desde docs vivos.** Si un doc vivo (schema, glosario, prompt, CLAUDE) cita una sección de este archivo, es bug: la cita debe redirigirse a la sección equivalente del archivo nuevo.
> - **Archivado a `docs/historico/`** el 2026-05-15 tras cierre del lote v10.116 (reset de `convenciones-y-casos.md`), que era la condición de archivado diferida.
>
> ⚠️ **Aviso original (pre-cierre, conservado por trazabilidad):** contenido del modelo v1 pre-rediseño. Las decisiones refinadas (lógica de `recurrente` en 3 pasos, ciclo de vida de marcas internas, política PCIC, etc.) **no viven aquí**.

> 🗄️ **Follow-ups del modelo viejo — CERRADOS (2026-05-13).** Esta lista se conserva por trazabilidad histórica. **Su contenido está obsoleto** y no debe usarse como guía operativa. Resolución de cada entrada en el archivo vivo `reglas-operativas.md`:
>
> - ~~Regla del sufijo `@R` en fuentes (decía "6 tipos productivos")~~ → **cerrada en `reglas-operativas.md` §6.5 con 5 tipos productivos** (taxonomía alineada con schema §9.5 y glosario). `produccion_escrita_libre` no existe en la taxonomía.
> - ~~Regla 11 sobre `audio.transcripcion`~~ → **cerrada en `reglas-operativas.md` §6.6** con el enunciado exacto.
> - ~~Input incidental vs contenido enseñado~~ → **cerrada** en `reglas-operativas.md` §5.1.1 (criterios pedagógicos paraguas) y §5.6 (canon semántico léxico).
> - ~~Anticipación vs recurrente~~ → **cerrada en `reglas-operativas.md` §6.3** (Anticipación).
> - ~~Heterogeneidad semántica dentro de un mismo ejercicio~~ → sigue como follow-up vivo en el banner de `reglas-operativas.md`.
> - ~~Suite automatizada de verificación global de integridad~~ → sigue como follow-up vivo (banner de `reglas-operativas.md` + `schema-inventario.md` §A.3).
>
> **Reglas que ya estaban en el cuerpo de este archivo viejo:** *Verbo soporte vs paradigma* y *Normalización de `formas_trabajadas`* — absorbidas en el archivo vivo (§5.2 y §6.4 respectivamente).

> 🗄️ **Boilerplate heredado — DESACTIVADO.** Los tres párrafos que originalmente seguían aquí declaraban la responsabilidad, el alcance y el "single source of truth de precedencias" de este archivo como autoridad operativa. **Esa autoridad ya no aplica:** la guía de decisión, el alcance operativo y el single source of truth de precedencias viven hoy en `reglas-operativas.md` (archivo vivo, reescrito 2026-05-13 bajo modelo IA-first). Cualquier afirmación normativa que aparezca en el cuerpo de este reservorio histórico debe leerse como **descripción del modelo viejo**, nunca como regla vigente.

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
- `pronunciacion_ortografia` — pronunciación, ortografía relacionada con sonido, acento, entonación, deletreo, dictado.
- `cultura` — contenido sociocultural (ciudades, costumbres, gastronomía, calendarios, personajes culturales).
- `transversal` — actividad sin foco de dominio específico, solo ejercita habilidades (lectura/escucha de comprensión genérica, tarea final que cruza dominios). Nombre intencionalmente distinto del valor `destrezas` de `seccion` para evitar pegar el eje a la clasificación editorial de la página.

**Regla de asignación:** un único `enfoque` por actividad — el dominante. Si una actividad mezcla varios (ej. completar diálogo + repasar léxico), elegir el que el enunciado prioriza. Ante duda real, consultar al autor.

**Relación con `seccion` (nivel página):** `seccion` clasifica la página según el índice editorial; `enfoque` clasifica la actividad concreta. Pueden divergir: una página `seccion: gramatica` puede contener una actividad `enfoque: transversal` (lectura comprensiva sin foco gramatical) y otra `enfoque: gramatica` (cloze de artículos). Capturar el foco real, no el de la página.

> **Antipatrón frecuente — copiar `enfoque` de `seccion` por proximidad editorial.** Heredar el `enfoque` de la sección donde vive la página es un error recurrente, sea cual sea la sección (`gramatica`, `vocabulario`, `comunicacion`, `cultura`, `destrezas`, `evaluacion`). Una actividad de comprensión lectora/auditiva **genérica** (responder preguntas sobre un texto, V/F sobre un input, marcar lo que se escucha) NO toma el `enfoque` de la sección que la aloja; es `transversal` salvo que el ejercicio fuerce un foco específico (cloze gramatical, repaso léxico, función comunicativa explícita). Casos disparadores reales: U5-p60-act03 (sección Cultura, asignó `enfoque: cultura` cuando era comprensión lectora `transversal`) y U5-p61-act04 (sección Evaluación, asignó `enfoque: comunicacion` cuando también era `transversal`). Verificar siempre el foco pedagógico real del ejercicio, no la sección de la página.

#### Regla de asignación de `expresion_escrita`

`expresion_escrita` se asigna cuando el alumno **produce contenido escrito propio** — es decir, cuando lo que escribe sale de su memoria, conocimiento o criterio, no de un input dictado o de un banco dado. Aplica tanto a textos elaborados (frase, párrafo, correo, presentación, respuesta abierta) como a **listas de palabras evocadas** (ej. "escribe los países que recuerdas").

`expresion_escrita` **NO** se asigna en:
- **Mecánicas de manipulación de elementos dados** (`completa_huecos`, `relaciona`, `ordena`, `clasifica`, `seleccion_multiple`, `verdadero_falso`, marcar, subrayar, unir con flechas): la destreza es la **comprensión** que permite hacer la elección correcta. Aplica también a "Completa con el artículo" (dada la frase, el alumno deduce el artículo: aplica regla, no produce contenido propio) y a "Completa con la palabra del recuadro" (transcribe del banco).
- **Transcripciones de input** (dictado, "Escucha y escribe"): el alumno transcribe lo escuchado, no produce contenido propio. La destreza dominante es `comprension_auditiva`.
- **Respuestas cerradas con palabra del texto**: el alumno copia/extrae del input. Solo `comprension_lectora`.

Resumen del criterio: **¿el alumno está produciendo contenido propio o transcribiendo/aplicando reglas a partir de un input dado?** Si es lo primero, `expresion_escrita`. Si es lo segundo, no.

#### Heurística `vocabulario` vs `pronunciacion_ortografia` para "escucha y repite" / "escucha y escribe"

Casos donde el alumno trabaja palabras pero también pronunciación:

- Si las palabras están agrupadas por **campo léxico** (cognados, países, profesiones, números como léxico) y el aprendizaje es saber qué significan o reconocerlas → `enfoque: vocabulario`.
- Si las palabras o sonidos están agrupados por **dificultad fonética** (alfabeto, combinaciones c/qu, j/g, z/c) y el aprendizaje es la pronunciación o la ortografía relacionada con sonido → `enfoque: pronunciacion_ortografia`.
- **Deletrear** (en voz alta o por escrito) → siempre `pronunciacion_ortografia`.
- **Dictado** ("escucha y escribe") → siempre `pronunciacion_ortografia` (la habilidad ejercitada es reconstruir la grafía a partir del sonido), incluso si el contenido dictado es léxico (ej. dictado de números).

#### Ejemplos canónicos (tres ejes a la vez)

- "Lee y escucha el diálogo" → `tipo: lee_y_escucha` + `destreza: [comprension_auditiva, comprension_lectora]` + `enfoque: transversal`.
- "Completa con el artículo el/la/los/las" → `tipo: completa_huecos` + `destreza: [comprension_lectora]` + `enfoque: gramatica`.
- "Escucha y completa con la palabra adecuada del recuadro" → `tipo: completa_huecos` + `destreza: [comprension_auditiva, comprension_lectora]` + `enfoque: vocabulario`.
- "Escribe un correo a tu amigo" → `tipo: expresion_escrita_libre` + `destreza: [expresion_escrita]` + `enfoque: comunicacion`.
- "Lee el texto y contesta a las preguntas" (cerradas, respuesta del texto) → `tipo: responder_preguntas_cerradas` + `destreza: [comprension_lectora]` + `enfoque: transversal`.
- "Escribe sobre tu rutina diaria" (respuesta abierta elaborada) → `tipo: responder_preguntas_abiertas` + `destreza: [expresion_escrita]` + `enfoque: comunicacion`.
- "Escucha y repite" → `tipo: escucha_y_repite` + `destreza: [comprension_auditiva, expresion_oral]` + `enfoque: pronunciacion_ortografia`.
- "Pregunta a tu compañero por su familia" → `tipo: interaccion_oral` + `destreza: [interaccion_oral]` + `enfoque: comunicacion`.
- "Relaciona los relojes con los horarios digitales" (con escucha previa) → `tipo: relaciona` + `destreza: [comprension_auditiva, comprension_lectora]` + `enfoque: vocabulario`.

### 2.4 Política de la enumeración

- La enumeración de 20 valores es **provisional y revisable a nivel global del proyecto**. No se amplía ni se cambia ad hoc por unidad. Cualquier modificación del set requiere decisión cerrada en PROCESO-MAESTRO antes de aplicarse en `schema-inventario.md` y en `validar_inventario.py` (regla de no-divergencia).
- Ante un caso ambiguo durante una extracción nueva: marcar como TODO en el JSON y consultar al autor antes de cerrar el inventario.

### 2.5 Cómo elegir entre los 3 campos canónicos de texto (`texto_completo`, `dialogo_completo`, `textos_personajes`)

Tres patrones, tres campos. No mezclar:

| Patrón del libro | Campo |
|---|---|
| Un texto seguido (carta, artículo, descripción, narración) | `datos.texto_completo` (string único) |
| Diálogo con turnos atribuidos a hablantes (A: …, B: …) | `datos.dialogo_completo` (lista de strings, una por turno) |
| N textos cortos, cada uno atribuido a un personaje distinto (autorretratos, fichas, presentaciones múltiples) | `datos.textos_personajes` (lista de objetos `{personaje, texto}`) |

> **No fusionar para forzar `texto_completo` cuando hay atribución por personaje.** La atribución es información estructural y debe preservarse. Ver `convenciones-y-casos.md` §1.4-bis.

---

## 3. Cómo asignar `tipo_cuadro` (5 valores)

Enumeración cerrada en `schema-inventario.md` §7.

Cuando una página tiene un cuadro de referencia (clasificado según §1 regla 4), asignar `tipo_cuadro` según su naturaleza pedagógica:

- **`gramatical`** — tablas de conjugación, paradigmas morfológicos (artículos, género, posesivos, interrogativos, demostrativos), reglas ortográficas de uso gramatical.
- **`lexical`** — listas ilustradas de vocabulario, tablas de campos semánticos, colores, familias de palabras.
- **`pronunciacion_ortografia`** — cuadros de pronunciación u ortografía relacionada con sonido (c/qu, z/c, g/gu, entonación, acento...).
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

### 5.6 `campo_semantico` y claves de `vocabulario_consolidado`: canon semántico

Estructural en schema (`schema-inventario.md` §9.1, §10).

**Universo válido.** Los nombres permitidos para `actividad.campo_semantico` y para las claves de `vocabulario_consolidado.{principal,recurrente,comprension}` viven en `campos-semanticos-canonicos.json` (fuente única). Aplica a cualquier sección, no solo vocabulario. Sustituye la decisión "liberal" anterior.

**Naming:** canónico literal del canon, no `snake_case` ni invenciones.

- ✅ `"Objetos de clase"`, `"Establecimientos"`, `"Higiene"`.
- ❌ `"objetos_de_clase"`, `"lugares_publicos"`, `"verbos"`.

#### Frontera entre `aliases_indice` y `aliases_auto`

Procedencia estricta. No son intercambiables:

- **`aliases_indice`** → literales que aparecen en `nc1-curso.json` (`vocabulario[]` o `contenido_general[]`). Solo entradas con `origen: "indice"` pueden tener esta lista poblada. Sirve a las herramientas para reconocer el contenido del índice editorial cuando se referencia con su nombre largo (ej. `"Establecimientos: cine, restaurante, farmacia..."` → canónico `"Establecimientos"`).
- **`aliases_auto`** → variantes detectadas en inventarios (codificaciones legacy del extractor, normalizaciones diferentes, formas con `snake_case` halladas en saneamiento). Aplica a cualquier `origen`. Nunca se usan para reconocer contenido del índice.

#### Árbol de decisión cuando aparece un campo léxico

```
¿El canónico ya existe en el canon (literal o alias)?
├── SÍ → usar el canónico literal en el inventario.
│         Si la forma hallada era un alias, registrarla en el canon:
│           · si proviene de nc1-curso.json → aliases_indice
│           · si proviene de un inventario o codificación del extractor → aliases_auto
│         (edición del canon vía Claude Code).
└── NO →
    ¿El contenido viene del índice del libro (vocabulario[] / contenido_general[] de nc1-curso.json)?
    ├── SÍ → crear entrada nueva en el canon con origen: "indice".
    │        El texto literal del índice queda como aliases_indice
    │        si el canonico se normalizó.
    └── NO →
        ¿Está cubierto por subcategoría PCIC A1 aprobada?
        ├── SÍ → crear entrada con origen: "pcic_a1". aliases_indice vacía.
        └── NO →
            ¿Es ruido del extractor (snake_case, "_descripcion", etc.)
            o parche contextual ("Vocabulario del diálogo", "Otros", "Texto X")?
            ├── SÍ → no se amplía canon. Sanear el inventario:
            │        decidir el canónico real (humano), renombrar el campo en el JSON.
            │        La forma errónea no se conserva como alias (es ruido, no semántica útil).
            └── NO → caso de excepción justificada:
                     crear entrada con origen: "excepcion" + nota obligatoria.
```

#### Marca transitoria `_pendiente_canon`

Si durante extracción el agente no puede asignar un canónico con seguridad razonable, debe escribir literalmente `"_pendiente_canon"` (como `campo_semantico` o como clave de `vocabulario_consolidado`) y dejar el contenido provisional. **Nunca inventar un nombre nuevo en caliente.**

`_pendiente_canon` es estado transitorio de worktree. **Bloquea cierre del inventario.** Antes de la integración, el humano resuelve cada marca aplicando el árbol de decisión (vía Claude Code en chat) y la marca desaparece.

#### Rollout del endurecimiento (canales del validador)

El validador (`scripts/validar_inventario.py`) tiene tres canales: **errores** (bloquean cierre), **avisos** (no bloquean), **auditoría legacy** (informativos, contador propio). Iteración activa en la constante `ROLLOUT_CANON_ITERACION`. Paso de iteración: decisión explícita del autor, registrada en `PROCESO-MAESTRO.md`.

**R1 — entrada en vigor.** Unidades en `LEGACY_UNIDADES_R1`:
- cualquier valor fuera de canon (alias o desconocido) → auditoría legacy (no bloquea).

Unidades nuevas o re-extracciones explícitas:
- cualquier valor que no sea canónico literal → error duro.

**R2 — tras saneamiento de U0-U9** (`LEGACY_UNIDADES_R1` vacía):
- canónico literal → OK silencioso.
- `aliases_indice` → OK silencioso (nomenclatura editorial legítima del libro).
- `aliases_auto` → aviso (deuda de actualización).
- sin match → error duro.

**R3 — endurecimiento final:**
- solo canónico literal → OK.
- cualquier alias → error duro. `aliases_*` queda como referencia histórica.

**`_pendiente_canon` → error duro siempre, en todas las iteraciones.** Bloquea cierre del inventario.

### 5.7 `datos.items_libro`: literalidad obligatoria

Estructural en schema (`schema-inventario.md` §12): lista de strings, obligatoria en actividades de cierto tipo (lista canónica en `validar_inventario.py:TIPOS_QUE_REQUIEREN_ITEMS`).

**Regla de literalidad (la más importante):** `items_libro` debe contener **el texto literal del libro**, con los huecos marcados como `_____` (5 guiones bajos). Nunca sustituir el enunciado por la respuesta. Nunca inventar el enunciado.

**Para qué tipos aplica:** completar huecos, opción múltiple, ordenar, clasificar, verdadero/falso, y similares.

**Excepción para `relaciona` con dos columnas explícitas:** si el libro presenta dos columnas visuales separadas (columna A y columna B con elementos a unir), usar `datos.columnas_relaciona` en lugar de `items_libro`. Ver `convenciones-y-casos.md` §1.8.

> Ejemplos correctos e incorrectos → `convenciones-y-casos.md`.

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

> Ejemplo JSON canónico de U0 → `convenciones-y-casos.md`.

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
| Convenciones de transcripción del libro al JSON (sílaba tónica, primer ítem resuelto, marcadores de diálogos, formato de sopas de letras) | `convenciones-y-casos.md` |
| Ejemplos correctos/incorrectos de `items_libro` | `convenciones-y-casos.md` |
| Casos históricos resueltos | `convenciones-y-casos.md` |

---

## 5.10. Verbos en `actividad.tiempos_y_verbos` y `cuadro.tiempos_y_verbos` *(integrada del rediseño 2026-05-13)*

> **Aplica a:** poblar `actividad.tiempos_y_verbos` y `cuadro.tiempos_y_verbos` (shape §3.2 del schema).

**Regla operativa:** un verbo entra en `tiempos_y_verbos` cuando **sus formas concretas aparecen** en la actividad o cuadro, **independientemente de que su paradigma sea el foco principal pedagógico**. La aparición de formas conjugadas — aunque sea como soporte sintáctico de otro contenido — es suficiente para registrar el verbo.

**Único caso en que NO entra:**
- El verbo se menciona **solo como infinitivo léxico** en una lista de palabras (sin conjugación trabajada y sin formas en frases): esa mención léxica va a `vocabulario`, no a `tiempos_y_verbos`. Ver §5d del schema (enum `tiempo`) para los criterios de cuándo cabe `Infinitivo` aquí.

**Ejemplo de inclusión (caso real U2 p24#3):** el cuadro de **Demostrativos** trae ejemplos como *"Este **es** Juan"* o *"Estas **son** Laura y Rosa"*. Aunque el paradigma de foco son los demostrativos, las formas `es` y `son` están presentes y se registran en `cuadro@p24#3.tiempos_y_verbos` como `{ "lema": "ser", "tiempo": "Presente", "formas_trabajadas": ["es", "son"] }`. El consolidado top-level acumula estas fuentes en la entrada de `ser`.

**Implicación operativa:** el consolidado `tiempos_y_verbos_consolidado` recoge la **distribución real de formas** del libro, no solo el paradigma trabajado. La distinción "foco principal vs soporte" se conserva en el campo `descripcion` por unidad: la descripción explica qué fuentes son foco y cuáles son soporte.

> **Cuándo escalar al autor:** si el verbo no aparece literalmente con formas conjugadas pero la actividad lo evoca de forma indirecta (ej. paráfrasis), marcar `_funcion_ambigua: true` y escalar.

---

## 5.11. Normalización de `formas_trabajadas` en el consolidado *(integrada del rediseño 2026-05-13)*

> **Aplica a:** derivación del bloque top-level `tiempos_y_verbos_consolidado` (shape §9.2 del schema).

**Regla operativa:** las formas conjugadas concretas se almacenan con **dos políticas distintas según el nivel**:

- **En actividad y cuadro** (`actividad.tiempos_y_verbos[].formas_trabajadas`, `cuadro.tiempos_y_verbos[].formas_trabajadas`): **literalidad estricta del libro**. Si el libro escribe *"Tengo 13 años..."* en una frase de mensaje, la forma se transcribe como `"Tengo"` (con mayúscula inicial). La actividad/cuadro es transcripción.
- **En el bloque consolidado** (`tiempos_y_verbos_consolidado[].formas_trabajadas`): **minúscula** al agregar. La forma `"Tengo"` de la actividad se acumula como `"tengo"` en el consolidado. El consolidado es derivado canónico, no transcripción.

**Razón:** evitar duplicados artificiales entre `["Tengo", "tengo"]` que serían la misma forma con distinta capitalización accidental.

**Ejemplo discriminativo (caso real U2 p24-act3):** la actividad presenta *"Me llamo Cristina, [1] _____ 13 años..."* con respuesta `"Tengo"`. La actividad guarda `"formas_trabajadas": ["Tengo"]`. El consolidado, al agregar este lema con las apariciones de otros sitios, guarda `"formas_trabajadas": ["tengo", "tienes", "tiene", ...]` — sin duplicar `"Tengo"` y `"tengo"`.

**Política de conservación de mayúsculas en consolidado:** la única excepción serían nombres propios o siglas dentro de una forma compleja (raro en verbos A1). Por defecto, **todo lo del consolidado va en minúscula**.

> **Cuándo escalar al autor:** si una forma del libro tiene mayúscula NO por inicio de frase sino por razón distinta (nombre propio dentro, sigla), marcar y consultar antes de normalizar.


---

## 5.12. Procedimiento OBLIGATORIO de poblado de `recurrente` *(añadida tras error 2026-05-13)*

> **Aplica a:** poblar los sub-bloques `recurrente` de `vocabulario_consolidado`, `gramatica_consolidada` y `pronunciacion_ortografia_consolidada`. El procedimiento es **el mismo en estructura** para las tres dimensiones; la **detección** y el **cruce** son específicos por dimensión (§5.12.A, §5.12.B, §5.12.C).

**Regla obligatoria.** Antes de declarar un sub-bloque `recurrente` vacío o casi vacío en cualquiera de las tres dimensiones, el operador **DEBE** ejecutar el procedimiento sistemático. Ningún paso es opcional.

### Procedimiento sistemático (8 pasos, comunes a las 3 dimensiones)

1. **Identificar el foco principal** de la actividad/cuadro y rellenar el sub-bloque `principal` correspondiente.
2. **Identificar los verbos trabajados** (rama propia: van a `tiempos_y_verbos`, no a las otras listas).
3. **Barrer el input verbatim** de la actividad/cuadro buscando elementos de cada dimensión (ver §5.12.A para léxico, §5.12.B para gramática, §5.12.C para pronunciación/ortografía).
4. **Cruzar los elementos detectados** contra los registries canónicos y los índices de unidades anteriores (ver §5.12.A/B/C para los archivos concretos).
5. **Listar TODOS los matches** encontrados. No omitir ninguno por sesgo de "foco pedagógico".
6. **Aplicar los 3 criterios de recurrente** a cada match:
   - Frecuencia (agregada en la página o unidad).
   - Posición (canónico en unidad anterior, o no canónico en posterior pero relevante).
   - Valor pedagógico (consolidación, ampliación, contraste, apoyo a la comprensión).
7. **Surgir en chat los candidatos** que cumplen los criterios. PROHIBIDO asumir silenciosamente que un candidato no entra. La decisión la toma el autor; el operador propone.
8. **Aplicar la decisión del autor** al JSON. Anotar la decisión en `_decisiones_ia` con suficiente detalle.

### §5.12.A — Detección y cruce para `vocabulario_consolidado.recurrente` (léxico)

**Detección (paso 3):** barrer texto verbatim de TODOS los campos `datos.*` de cada actividad: `items_libro`, `ejemplo_libro`, `texto_completo`, `dialogo_completo`, `textos_personajes`, `palabras_recuadro`, `preguntas`, `texto_modelo`, `nombres_dados`, `frases`, `expresiones_dadas`, `afirmaciones_a_corregir`, `texto_correo`, `ejemplos_modelo`. Extraer las palabras léxicas (sustantivos, adjetivos, adverbios léxicos, expresiones léxicas).

**Cruce (paso 4):**
- `fases/1-extraccion-inventario/campos-semanticos-canonicos.json` (catálogo de campos canónicos disponibles).
- `unidades/nc1-curso.json` → `unidades[N].vocabulario[]` para cada N ≠ unidad actual (qué campos son canónicos en otras unidades).
- `fases/1-extraccion-inventario/pcic-a1-vocabulario.json` como apoyo de naming si el match exige refinamiento PCIC.

### §5.12.B — Detección y cruce para `gramatica_consolidada.recurrente` (estructuras gramaticales)

**Detección (paso 3):** barrer el input buscando **estructuras gramaticales** (no palabras sueltas):
- **Marcadores morfológicos**: artículos (el/la/los/las/un/una/unos/unas), posesivos (mi/tu/su/nuestro...), demostrativos (este/ese/aquel...), interrogativos (qué/quién/cuál/dónde...), preposiciones de uso gramatical.
- **Concordancias visibles**: art+sust en género y número, adj+sust, sujeto+verbo (cuando reaparece tras introducirse en unidad anterior).
- **Paradigmas reapareciendo**: si un paradigma verbal o pronominal ya canónico en otra unidad aparece aplicado en la unidad actual.
- **Estructuras sintácticas marcadas**: orden de palabras específico, negación, oraciones interrogativas/exclamativas, comparativos, perífrasis, etc.

**Cruce (paso 4):**
- `fases/1-extraccion-inventario/gramatica-canonica.json` (registry; hoy esqueleto, pero debe consultarse).
- `unidades/nc1-curso.json` → `unidades[N].gramatica[]` para cada N ≠ unidad actual.
- `fases/1-extraccion-inventario/pcic-a1-gramatica.json` para confirmar respaldo PCIC del fenómeno y para construir el nombre canónico de candidatos sintéticos (ver §5.14).

**Cuándo proponer síntesis** (combinado con §5.14): si dos o más categorías canónicas de unidades anteriores se presentan **integradas e indistinguibles** en la actividad/cuadro (ej. art+sust+adj concordando), proponer una categoría sintética + las categorías separadas como opciones, no decidir silenciosamente.

### §5.12.C — Detección y cruce para `pronunciacion_ortografia_consolidada.recurrente`

**Detección (paso 3):** barrer el input buscando **marcas explícitas** de fenómenos fonético-ortográficos. La pronunciación/ortografía rara vez se infiere del texto puro; suele venir señalada por convenciones tipográficas o por el tipo de actividad:
- **Convenciones tipográficas del libro**: sílaba tónica subrayada/marcada, letras destacadas, transcripciones fonéticas, ortografía con resalte.
- **Tipos de actividad indicadores**: `escucha_y_repite` con foco fonético, deletreo, dictado (escucha y escribe), ejercicios de identificación de sonidos.
- **Cuadros con `tipo_cuadro: pronunciacion_ortografia`**: contenido sistemático sobre acento, entonación, ortografía, correspondencia sonido-grafía.
- **Campos `datos.*` específicos**: si existen campos como `transcripcion` en audio, ejercicios de letras/sílabas, etc.

**Cruce (paso 4):**
- `fases/1-extraccion-inventario/pronunciacion-ortografia-canonica.json` (registry; hoy esqueleto, pero debe consultarse).
- `unidades/nc1-curso.json` → `unidades[N].pronunciacion_ortografia` para cada N ≠ unidad actual.
- `fases/1-extraccion-inventario/pcic-a1-pronunciacion-ortografia.json` (sub-bloques `pronunciacion` y `ortografia`) para confirmar respaldo PCIC.

**Nota sobre convenciones del libro**: la sílaba tónica marcada con subrayado en NC1 es **convención de transcripción** del libro, no contenido enseñado por sí mismo. Solo entra como recurrente si una unidad anterior la introdujo formalmente como categoría enseñada (no por mera aparición tipográfica).

### Errores prohibidos (los que motivaron esta regla)

- **PROHIBIDO** asumir que una página de gramática no aporta a `vocabulario_consolidado`, o que una página de vocabulario no aporta a `gramatica_consolidada`. El input lleva elementos de las tres dimensiones independientemente del foco pedagógico.
- **PROHIBIDO** recortar el análisis para que la fixture "salga cerrable". Una prueba diseñada para no fallar pierde valor diagnóstico. El análisis debe ser completo; lo que el contenido dé, eso es lo que entra.
- **PROHIBIDO** aplicar la regla "Input incidental vs contenido enseñado" solo a la primera mitad (matches con el principal de la unidad actual). La segunda mitad — matches con campos canónicos de otras unidades — es la que más se omite y la que esta regla obliga a cubrir.
- **PROHIBIDO** declarar `pronunciacion_ortografia_consolidada.recurrente` vacío sin haber inspeccionado convenciones tipográficas del input ni tipo de actividad. La detección fonética es no-evidente y exige un paso explícito.

> **Resultado esperado del paso 7:** una lista de candidatos a recurrente con su justificación (campo canónico, fuentes, criterios cumplidos, dimensión a la que pertenece), pegada en el chat. El autor decide cuáles entran. Solo entonces el operador aplica al JSON.

---

## 5.13. Política de propuesta-en-chat ante toda decisión no clara *(añadida tras error 2026-05-13)*

> **Aplica a:** todo el flujo de poblado de inventario y fixture, no solo a `recurrente`.

**Regla obligatoria.** Dudas, marcas bloqueantes y decisiones no triviales **DEBEN manifestarse en el chat ANTES de escribirse en el JSON**. PROHIBIDO dejarlas silenciosas dentro de marcas internas, comentarios o decisiones implícitas.

### Casos cubiertos por la regla

- Toda **marca `_pendiente_canon`** que el operador esté tentado de escribir → primero plantear en chat la duda concreta (qué campo canónico falta, qué opciones tiene el autor).
- Toda **marca `_funcion_ambigua`** → primero plantear en chat qué ambigüedad encuentra el operador y qué opciones de desambiguación tiene el autor.
- Toda **decisión de inclusión/exclusión** que requiera criterio (qué entra en `recurrente`, qué se considera "trabajado" vs "soporte", qué nombre canónico aplicar) → primero plantear en chat con opciones razonables.
- Toda **anticipación detectada** (léxico que apunta a unidad posterior) → plantear en chat antes de anotarla en `_migracion_rediseno.anticipaciones_detectadas_para_fase_2` o en `_fixture_exploratoria.hallazgos`.

### Cómo formular la pregunta en chat

Una pregunta correcta tiene tres partes:
1. **Contexto**: dónde aparece la duda (página, actividad, cuadro, campo).
2. **Hallazgo concreto**: qué léxico/categoría/forma motiva la duda.
3. **Opciones razonables**: 2-4 alternativas etiquetadas (a), (b), (c) con sus implicaciones operativas.

### Errores prohibidos

- **PROHIBIDO** escribir `_pendiente_canon` en el JSON antes de haber preguntado al autor.
- **PROHIBIDO** escribir `_funcion_ambigua: true` antes de exponer la ambigüedad en chat.
- **PROHIBIDO** "asumir lo más probable" sin consultar cuando el contrato no fija el caso.
- **PROHIBIDO** confiar en que el autor revisará el JSON crudo para detectar decisiones silenciosas. La corrección se hace desde el dashboard; el JSON no debe ser bandeja silenciosa de pendientes.

---

## 5.14. Construcción iterativa de `recurrente`: propuesta de Claude + decisión del autor *(añadida tras error 2026-05-13)*

> **Aplica a:** construcción de categorías de `recurrente` en cada unidad.

**Regla obligatoria.** Las categorías de `recurrente` no se sacan automáticamente de reglas duras. Se construyen iterativamente: Claude **propone**, el autor **decide**, los agentes **aprenden con el uso**.

### Procedimiento (combinado con §5.12)

1. Claude ejecuta el barrido sistemático (§5.12) y lista candidatos.
2. Claude propone en chat el nombre canónico tentativo, items, fuentes y justificación de cada candidato.
3. Para candidatos que son **síntesis de varias categorías** de unidades anteriores (ej. "Concordancia artículo-sustantivo en género y número" sintetizando "Artículos determinados" + "Masculino y femenino" de U1), Claude debe explicitar:
   - Qué categorías de qué unidades se sintetizan.
   - Si la síntesis sustituye o coexiste con las categorías originales.
   - Respaldo PCIC si aplica.
4. El autor decide: aceptar tal cual, modificar nombre/items, rechazar, o convertir en categorías separadas.
5. Claude aplica al JSON únicamente tras decisión explícita.
6. La decisión queda registrada en `_decisiones_ia` con suficiente detalle para que sesiones futuras puedan reconocer el patrón.

### Por qué no hay regla dura de síntesis

La síntesis de categorías es un fenómeno editorial cualitativo que depende del libro concreto. Codificar reglas duras antes de tener varios casos crea reglas frágiles. El patrón propuesta→decisión→aprendizaje permite que la regla emerja de los datos.

### Errores prohibidos

- **PROHIBIDO** aplicar síntesis silenciosamente sin proponerla en chat primero.
- **PROHIBIDO** rechazar síntesis sin proponer las categorías separadas que la sustituyen.
- **PROHIBIDO** suponer que una categoría que era principal en U(n-1) entra automáticamente como recurrente en U(n) sin verificar los 3 criterios.

