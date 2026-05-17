# Reglas operativas — Decisión, clasificación, población

> **Responsabilidad:** cómo se decide y cómo se puebla durante la extracción. Una IA aplica estas reglas para clasificar, asignar y rellenar campos cuyo shape ya está fijado en `schema-inventario.md`.
>
> **No contiene:** forma del JSON (vive en `schema-inventario.md`), qué significa cada cosa (vive en `glosario.md`), ni convenciones de transcripción del libro al JSON (vive en `convenciones-y-casos.md`).
>
> **Triángulo de coherencia.** Este archivo, `schema-inventario.md`, `glosario.md` y `prompt.md` forman cadena cerrada. Si una regla operativa contradice cualquiera de los otros tres → primero se corrige la divergencia. PROHIBIDO introducir regla operativa que contradiga al schema, al glosario o al prompt sin antes resolver la divergencia.
>
> **Principio IA-first.** La IA decide, el código comprueba, el humano cierra. Cada regla se redacta como instrucción operativa: verbo imperativo + condición + acción + cuándo escalar. Casos frontera como ejemplos concretos, no como narrativa.
>
> **Single source de precedencias.** Las reglas de precedencia (qué clasificar como actividad / cuadro / nota / autoevaluación, en qué orden, con qué excepciones) viven **exclusivamente aquí**. Cualquier otro archivo que las invoque lo hace por referencia, no por copia.
>
> **Precedencia entre contratos vivos en caso de conflicto:** `schema-inventario.md` > `reglas-operativas.md` > `convenciones-y-casos.md`.
>
> **Numeración con huecos por estabilidad de referencias.** §5 conserva la numeración `§5.1`, `§5.2`, `§5.6`, `§5.9` (sin `§5.3`–`§5.5`, `§5.7`–`§5.8`); §8 no existe (se salta de §7 a §9). Los huecos se mantienen porque docs vivos externos referencian directamente las secciones presentes (`§5.6`, `§5.9`, `§9`, `§10`); renumerar consecutivo rompería esas refs sin aportar valor. No es descuido; es conservación deliberada.

---

## §0. Política operativa transversal

### §0.0. Principio de literalidad

**Aplica a:** toda transcripción del libro al JSON.

**Regla obligatoria.** La IA transcribe el contenido visible al alumno **verbatim** del libro: enunciados, ítems, textos, diálogos, opciones, ejemplos, respuestas dadas, formas verbales conjugadas. No parafrasea, no resume, no normaliza, no traduce, no completa. Conserva puntuación, mayúsculas/minúsculas, nombres propios, huecos (`_____`) y marcas tipográficas tal cual aparecen impresos.

**Aplicaciones operativas en este archivo:**
- `formas_trabajadas` en actividad/cuadro: literalidad estricta del libro (incluida la mayúscula inicial cuando la forma abre frase). Ver §6.4 para la normalización opuesta en el consolidado (minúscula).
- Barrido del input para detección léxica/gramatical/pron-orto: se hace sobre texto verbatim de `datos.*`. Ver §0.3.A/B/C.
- `instruccion_original`, `dialogo_completo`, `texto_completo`, `items_libro`: transcripción literal. Las convenciones de transcripción concretas (primer ítem resuelto, marcadores editoriales, textos atribuidos a personajes, etc.) viven en `convenciones-y-casos.md` §1.

**Errores prohibidos:**
- PROHIBIDO sustituir el enunciado original por la respuesta esperada.
- PROHIBIDO transcribir lo que la IA "interpreta" en lugar de lo que el libro escribe.
- PROHIBIDO normalizar mayúsculas/puntuación/ortografía en `actividad.tiempos_y_verbos[].formas_trabajadas`, `instruccion_original`, `datos.*` (la normalización aplica solo al agregar en consolidado: §6.4).

**Cuándo escalar:** si la transcripción literal produce ambigüedad operativa (¿es esto un ítem o un ejemplo modelo?, ¿este marcador es respuesta o metalengua?), aplicar §0.1 (propuesta-en-chat) consultando `convenciones-y-casos.md` §1 para los patrones conocidos.

### §0.1. Propuesta-en-chat ante toda decisión no clara

**Aplica a:** todo el flujo de poblado.

**Regla obligatoria.** Dudas, marcas bloqueantes y decisiones no triviales **DEBEN manifestarse en el chat ANTES de escribirse en el JSON**. PROHIBIDO dejarlas silenciosas dentro de marcas internas o decisiones implícitas.

**Casos cubiertos:**
- Toda marca `_pendiente_canon` que la IA esté tentada a escribir → primero plantear en chat qué canónico falta y qué opciones tiene el autor.
- Toda marca `_funcion_ambigua` → primero plantear la ambigüedad y las opciones de desambiguación.
- Toda decisión de inclusión/exclusión que requiera criterio (qué entra en `recurrente`, qué cuenta como "trabajado" vs "soporte", qué nombre canónico aplicar) → primero plantear con opciones razonables.
- Toda anticipación detectada (léxico que apunta a unidad posterior) → plantear antes de anotarla.

**Cómo formular la pregunta en chat (3 partes obligatorias):**
1. **Contexto:** página, actividad, cuadro, campo.
2. **Hallazgo:** qué léxico/categoría/forma motiva la duda.
3. **Opciones:** 2-4 alternativas etiquetadas (a), (b), (c) con implicación operativa de cada una.

**Errores prohibidos:**
- PROHIBIDO escribir `_pendiente_canon` o `_funcion_ambigua` sin haber preguntado antes.
- PROHIBIDO asumir "lo más probable" cuando el contrato no fija el caso.
- PROHIBIDO confiar en que el autor revisará el JSON crudo para detectar decisiones silenciosas. La corrección se hace desde el dashboard; el JSON no es bandeja silenciosa de pendientes.

### §0.2. Construcción iterativa de `recurrente` (propuesta + decisión + aprendizaje)

**Aplica a:** construcción de categorías de `recurrente` en cualquiera de los tres bloques consolidados.

**Regla operativa.** Las categorías de `recurrente` no se sacan de reglas duras. Se construyen iterativamente: Claude propone, el autor decide, los agentes aprenden con el uso.

**Procedimiento:**
1. Ejecutar el barrido sistemático de §0.3.
2. Proponer en chat el nombre canónico tentativo, items, fuentes y justificación de cada candidato.
3. Para candidatos que sean **síntesis** de varias categorías de unidades anteriores (ej. "Concordancia artículo-sustantivo en género y número" sintetizando "Artículos determinados" + "Concordancia de género" de U1), explicitar qué categorías se sintetizan, si la síntesis sustituye o coexiste con las originales, y el respaldo PCIC si aplica.
4. Esperar decisión del autor.
5. Aplicar al JSON solo tras decisión explícita.
6. Registrar la decisión en `_decisiones_ia` con detalle suficiente para reconocer el patrón en sesiones futuras.

**Por qué no hay regla dura de síntesis.** La síntesis es un fenómeno editorial cualitativo dependiente del libro concreto. Codificar reglas duras antes de tener varios casos crea reglas frágiles. El patrón propuesta→decisión→aprendizaje deja que la regla emerja de los datos.

**Errores prohibidos:**
- PROHIBIDO aplicar síntesis silenciosamente sin proponerla en chat.
- PROHIBIDO rechazar síntesis sin proponer las categorías separadas que la sustituyen.
- PROHIBIDO suponer que una categoría que era principal en U(n-1) entra automáticamente como recurrente en U(n) sin verificar los 3 criterios (§5.1.1).

### §0.3. Procedimiento OBLIGATORIO de poblado de `recurrente`

**Aplica a:** poblar `recurrente` en `vocabulario_consolidado`, `gramatica_consolidada` y `pronunciacion_ortografia_consolidada`. El procedimiento es el mismo en estructura para las tres dimensiones; la **detección** y el **cruce** son específicos por dimensión (§0.3.A, §0.3.B, §0.3.C).

**Regla obligatoria.** Antes de declarar un sub-bloque `recurrente` vacío o casi vacío, ejecutar el procedimiento completo. Ningún paso es opcional.

**Procedimiento sistemático (8 pasos comunes):**
1. Identificar el foco principal de la actividad/cuadro y rellenar `principal`.
2. Identificar los verbos trabajados (van a `tiempos_y_verbos`, no a las otras listas).
3. **Barrer el input verbatim** de la actividad/cuadro buscando elementos por dimensión (ver §0.3.A/B/C).
4. **Cruzar los elementos detectados** contra los registries canónicos e índices de unidades anteriores (ver §0.3.A/B/C).
5. Listar TODOS los matches. PROHIBIDO omitir por sesgo de "foco pedagógico".
6. Aplicar los 3 criterios de §5.1.1 (frecuencia, posición, valor pedagógico).
7. **Surgir en chat** los candidatos que cumplen los criterios (regla §0.1). El autor decide; la IA propone.
8. Aplicar la decisión al JSON. Anotar en `_decisiones_ia`.

#### §0.3.A — Detección y cruce para `vocabulario_consolidado.recurrente` (léxico)

**Detección (paso 3):** barrer texto verbatim de TODOS los campos `datos.*` de cada actividad — `items_libro`, `ejemplo_libro`, `texto_completo`, `dialogo_completo`, `textos_personajes`, `palabras_recuadro`, `preguntas`, `texto_modelo`, `nombres_dados`, `frases`, `expresiones_dadas`, `afirmaciones_a_corregir`, `texto_correo`, `ejemplos_modelo`. Extraer las palabras léxicas (sustantivos, adjetivos, adverbios léxicos, expresiones léxicas).

**Cruce (paso 4):**
- `campos-semanticos-canonicos.json` — catálogo de campos canónicos disponibles.
- `unidades/nc1-curso.json` → `unidades[N].vocabulario[]` para cada N ≠ unidad actual — qué campos son canónicos en otras unidades.
- `pcic-a1-vocabulario.json` — apoyo de naming si el match exige refinamiento PCIC.

#### §0.3.B — Detección y cruce para `gramatica_consolidada.recurrente` (estructuras gramaticales)

**Detección (paso 3):** barrer el input buscando estructuras gramaticales (no palabras sueltas):
- Marcadores morfológicos: artículos, posesivos, demostrativos, interrogativos, preposiciones de uso gramatical.
- Concordancias visibles: art+sust en género/número, adj+sust, sujeto+verbo cuando reaparece tras unidad anterior.
- Paradigmas reapareciendo: si un paradigma verbal o pronominal canónico en otra unidad aparece aplicado.
- Estructuras sintácticas marcadas: orden de palabras, negación, interrogación, comparativos, perífrasis.

**Cruce (paso 4):**
- `gramatica-canonica.json` (registry poblado con 17 categorías canónicas, v10.117).
- `unidades/nc1-curso.json` → `unidades[N].gramatica[]` para cada N ≠ unidad actual.
- `pcic-a1-gramatica.json` para confirmar respaldo PCIC y construir nombres canónicos sintéticos (ver §0.2).

**Cuándo proponer síntesis:** si dos o más categorías canónicas de unidades anteriores se presentan integradas e indistinguibles (ej. art+sust+adj concordando), proponer categoría sintética + categorías separadas como opciones (regla §0.2).

#### §0.3.C — Detección y cruce para `pronunciacion_ortografia_consolidada.recurrente`

**Detección (paso 3):** la pronunciación/ortografía rara vez se infiere del texto puro; viene señalada por convenciones tipográficas o por tipo de actividad. Buscar:
- Convenciones tipográficas: sílaba tónica subrayada/marcada, transcripciones fonéticas, ortografía resaltada.
- Tipos de actividad indicadores: `escucha_y_repite` con foco fonético, deletreo, dictado.
- Cuadros con `tipo_cuadro: pronunciacion_ortografia`.
- Campo `audio.transcripcion` cuando aplica (ver §6.6).

**Cruce (paso 4):**
- `pronunciacion-ortografia-canonica.json` (registry poblado con 7 categorías canónicas, v10.117).
- `unidades/nc1-curso.json` → `unidades[N].pronunciacion_ortografia` para cada N ≠ unidad actual.
- `pcic-a1-pronunciacion-ortografia.json` (sub-bloques `pronunciacion` y `ortografia`).

**Nota sobre convenciones del libro:** la sílaba tónica marcada con subrayado en NC1 es convención de transcripción, no contenido enseñado. Solo entra como recurrente si una unidad anterior la introdujo formalmente como categoría enseñada.

**Errores prohibidos:**
- PROHIBIDO asumir que una página de gramática no aporta al vocabulario_consolidado, o que una página de vocabulario no aporta al gramatica_consolidada.
- PROHIBIDO recortar el análisis para que una fixture "salga cerrable".
- PROHIBIDO aplicar la regla "input incidental vs contenido enseñado" solo a la unidad actual; la mitad referida a otras unidades es la que más se omite.
- PROHIBIDO declarar `pronunciacion_ortografia_consolidada.recurrente` vacío sin haber inspeccionado convenciones tipográficas ni tipos de actividad indicadores.

---

## §1. Precedencia entre actividad / cuadro / nota / autoevaluación

Para cada elemento visible en una página del libro, decidir en este orden:

1. ¿Tiene número de actividad (1, 2, 3...) y pide producción del alumno (escuchar, repetir, escribir, relacionar...)? → **actividad** con `tipo` de la taxonomía cerrada (§2).
2. ¿Es "Para aprender"? → ver §4: actividad solo si pide producción al alumno; cuadro si es solo informativo.
3. ¿Es "Observa"? → siempre **nota**. Nunca es actividad ni cuadro. Si acompaña a una actividad va en `datos._nota`; si acompaña a un cuadro va en `cuadro.observaciones`.
4. ¿Es una tabla o recuadro de referencia sin número ni instrucción de producción? → **cuadro** con `tipo_cuadro` apropiado (§3).
5. ¿Es el bloque "Mis resultados en esta unidad son: ..." al pie de la última página, con tres opciones y emoticonos? → bloque `autoevaluacion` top-level (no actividad, no cuadro, no nota).

**Precedencia:** las excepciones (reglas 2, 3, 5) tienen prioridad sobre la regla general (1). La regla general solo aplica cuando ninguna excepción encaja.

---

## §2. Asignación de `tipo` a una actividad (taxonomía cerrada de 20 valores)

**Regla operativa central:** `tipo` = la acción específica que el enunciado del libro pide al alumno. Si el enunciado encadena varias acciones, `tipo` lo determina **la última acción que pide producción concreta**. Si el enunciado solo pide absorber input (leer, escuchar, mirar) sin acción posterior, `tipo` refleja literalmente esa absorción.

`tipo` es independiente de `destreza` y `enfoque` (ver §2.3).

### §2.1. Tabla canónica de los 20 tipos

| `tipo` | Acción del enunciado |
|---|---|
| `escucha` | "Escucha" / "Mira X y escucha" — input puro auditivo, sin acción posterior. |
| `lee_y_escucha` | "Lee y escucha" — input combinado lectura + audio. |
| `ver_video` | "Mira el vídeo" — input con video. |
| `escucha_y_repite` | "Escucha y repite" — input auditivo + producción oral repetitiva. |
| `escucha_y_responde` | "Escucha y responde" oralmente, sin texto delante. |
| `completa_huecos` | Huecos predefinidos, celdas o slots a rellenar. |
| `relaciona` | Emparejar elementos de dos conjuntos. |
| `ordena` | Poner elementos en una secuencia. |
| `clasifica` | Agrupar elementos en categorías dadas. |
| `seleccion_multiple` | Subrayar / marcar / elegir entre alternativas. |
| `verdadero_falso` | Marcar V o F sobre afirmaciones. |
| `responder_preguntas_cerradas` | Responder con info que sale del input (texto, audio, video). |
| `responder_preguntas_abiertas` | Responder libre/personal sin texto-fuente. |
| `interaccion_oral` | "En parejas", "Pregunta y contesta a tu compañero". |
| `expresion_oral_libre` | "Preséntate", "Presenta a tu compañero a la clase". |
| `produccion_escrita_guiada` | Escribir frases con modelo/regla; sin huecos predefinidos. |
| `expresion_escrita_libre` | "Escribe un correo", "Escribe sobre…". |
| `busqueda_informacion` | "Busca información sobre…". |
| `tarea_final` | Tarea colaborativa de cierre que integra varios contenidos. |
| `juego` | Actividad con mecánica lúdica explícita. |

### §2.2. Reglas de desempate cuando el enunciado encadena varias acciones

1. **Si el enunciado contiene acción de manipulación** (`completa`, `marca`, `relaciona`, `ordena`, `clasifica`, `subraya`) **en cualquier punto** → la manipulación manda. Ej.: "Lee y completa" → `completa_huecos`. "Escucha y marca" → `seleccion_multiple`. "Mira el vídeo y completa" → `completa_huecos`. "Completa, escucha y repite" → `completa_huecos`.
2. **Si solo pide ver/mirar el video** sin manipulación posterior → `ver_video`.
3. **Si pide responder preguntas:**
   - Respuesta concreta que sale del input → `responder_preguntas_cerradas`.
   - Respuesta personal/libre **individual** → `responder_preguntas_abiertas`.
   - Respuesta personal/libre **en parejas** → `interaccion_oral` (la interacción manda sobre "responder").
4. **Si solo pide input** (leer/escuchar/mirar) sin acción posterior → `lee_y_escucha` o `ver_video` según medio.
5. **`completa_huecos` vs `produccion_escrita_guiada`** (frontera frecuente):
   - Huecos predefinidos (frase con `_____`, tabla con celdas vacías, ficha con campos) → `completa_huecos`.
   - El alumno construye frases o etiquetas desde un modelo, imagen o regla, sin huecos predefinidos → `produccion_escrita_guiada` (ej. "Coloca el artículo el/la a estos nombres", "Forma frases", "Describe estos objetos").

### §2.3. `destreza` y `enfoque` (dos ejes independientes de `tipo`)

Toda actividad se clasifica en **tres ejes ortogonales**: `tipo` (mecánica), `destreza` (habilidad MCER), `enfoque` (dominio de contenido).

**`destreza`** — lista de mínimo 1 valor de 6, orden alfabético, sin duplicados:
- `comprension_auditiva` — escuchar (audio o video).
- `comprension_lectora` — leer texto/diálogo/preguntas/items.
- `expresion_escrita` — producir texto propio.
- `expresion_oral` — producir habla propia (monólogo).
- `interaccion_oral` — intercambio oral con compañero.
- `mediacion` — reformular, resumir, traducir, explicar.

**Reglas de asignación de `destreza`:**
- Si hay texto a leer → `comprension_lectora`.
- Si hay audio o video a escuchar → `comprension_auditiva`.
- Output del alumno → la destreza correspondiente (escribir / hablar solo / interaccionar / mediar).
- Cero "destrezas de contenido". `gramatica` y `vocabulario` NO son destrezas; son `enfoque`.

**Regla específica de `expresion_escrita`:**
- SÍ se asigna cuando el alumno produce contenido escrito propio (frase, párrafo, correo, lista evocada).
- NO se asigna en mecánicas de manipulación de elementos dados (completa_huecos, relaciona, ordena, clasifica, seleccion_multiple, verdadero_falso): la destreza es la **comprensión** que permite la elección correcta.
- NO se asigna en transcripciones de input (dictado, "escucha y escribe"): la destreza dominante es `comprension_auditiva`.
- NO se asigna en respuestas cerradas con palabra del texto: solo `comprension_lectora`.

**`enfoque`** — string único de 6 valores:
- `gramatica` — manipulación de formas gramaticales (artículos, conjugación, género/número, concordancia).
- `vocabulario` — manipulación de léxico (banco temático, palabra-imagen, clasificar campo semántico).
- `comunicacion` — funciones comunicativas / fórmulas pragmáticas (saludos, presentarse, pedir información).
- `pronunciacion_ortografia` — pronunciación, ortografía relacionada con sonido, acento, entonación, deletreo, dictado.
- `cultura` — contenido sociocultural (ciudades, costumbres, gastronomía, calendarios).
- `transversal` — actividad sin foco de dominio específico, solo ejercita habilidades (lectura/escucha de comprensión genérica, tarea final que cruza dominios).

**Regla de asignación de `enfoque`:** un único `enfoque` por actividad — el dominante. Si una actividad mezcla varios, elegir el que el enunciado prioriza. Ante duda real, escalar al autor por §0.1.

**`enfoque` NO se hereda de `seccion`.** Antipatrón frecuente: copiar `enfoque` de la sección editorial donde vive la página. Una página `seccion: gramatica` puede contener una actividad `enfoque: transversal` (lectura comprensiva sin foco gramatical) y otra `enfoque: gramatica` (cloze de artículos). Capturar el foco real, no el de la página.

**Heurística `vocabulario` vs `pronunciacion_ortografia` en "escucha y repite" / "escucha y escribe":**
- Palabras agrupadas por **campo léxico** y el aprendizaje es saber qué significan o reconocerlas → `vocabulario`.
- Palabras o sonidos agrupados por **dificultad fonética** (alfabeto, c/qu, j/g, z/c) → `pronunciacion_ortografia`.
- **Deletrear** → siempre `pronunciacion_ortografia`.
- **Dictado** ("escucha y escribe") → siempre `pronunciacion_ortografia` (la habilidad ejercitada es reconstruir grafía a partir del sonido), incluso si el contenido dictado es léxico.

**Ejemplos canónicos (los tres ejes):**
- "Lee y escucha el diálogo" → `lee_y_escucha` + `[comprension_auditiva, comprension_lectora]` + `transversal`.
- "Completa con el artículo el/la/los/las" → `completa_huecos` + `[comprension_lectora]` + `gramatica`.
- "Escucha y completa con la palabra del recuadro" → `completa_huecos` + `[comprension_auditiva, comprension_lectora]` + `vocabulario`.
- "Escribe un correo a tu amigo" → `expresion_escrita_libre` + `[expresion_escrita]` + `comunicacion`.
- "Lee el texto y contesta a las preguntas" → `responder_preguntas_cerradas` + `[comprension_lectora]` + `transversal`.
- "Escucha y repite" (sobre vocales) → `escucha_y_repite` + `[comprension_auditiva, expresion_oral]` + `pronunciacion_ortografia`.
- "Pregunta a tu compañero por su familia" → `interaccion_oral` + `[interaccion_oral]` + `comunicacion`.

---

## §3. Asignación de `tipo_cuadro` (5 valores)

Cuando una página tiene un cuadro de referencia (clasificado por §1 regla 4), asignar `tipo_cuadro` según su naturaleza pedagógica:

- **`gramatical`** — tablas de conjugación, paradigmas morfológicos (artículos, género, posesivos, interrogativos, demostrativos), reglas ortográficas de uso gramatical.
- **`lexical`** — listas ilustradas de vocabulario, tablas de campos semánticos, colores, familias de palabras.
- **`pronunciacion_ortografia`** — cuadros de pronunciación u ortografía relacionada con sonido (c/qu, z/c, g/gu, entonación, acento).
- **`cultural`** — información sociocultural (saludos, costumbres, fórmulas sociales).
- **`comunicativo`** — uso pragmático (registro, formalidad, turnos de conversación, cortesía).

**Ortogonalidad:** `seccion` de la página y `tipo_cuadro` son independientes. Un cuadro fonético puede aparecer en sección `gramatica`; un cuadro léxico puede estar en `vocabulario`. No forzar coincidencia.

**Capturar todo el contenido visible del cuadro** (filas, columnas, celdas, ejemplos) en `cuadro.contenido`.

---

## §4. Casos límite: "Para aprender" y "Observa"

### "Para aprender"

Cajas etiquetadas con "Para aprender" en el libro. Pueden tener dos naturalezas:

| Naturaleza | Indicador | Clasificación |
|---|---|---|
| Con tarea | Verbo imperativo dirigido al alumno ("haz", "escribe", "completa") | **Actividad** con `tipo: produccion_escrita_guiada` y `datos.subtipo: "para_aprender"` |
| Solo informativa | Lista de reglas o referencia sin instrucción | **Cuadro** con `tipo_cuadro` apropiado |

**Criterio decisional:** ¿el bloque contiene verbo imperativo dirigido al alumno? Sí → actividad. No → cuadro.

### "Observa"

Notas que llaman la atención sobre aspectos del idioma. Son **notas**, no actividades ni cuadros, aunque usen el imperativo "Observa".
- Si acompaña a una **actividad** → `datos._nota`.
- Si acompaña a un **cuadro** → `cuadro.observaciones`.

---

## §5. Población de campos del schema

### §5.1. Criterios pedagógicos para la población de listas tipadas (sección paraguas)

Esta sección agrupa los criterios pedagógicos que la IA aplica al rellenar las 4 listas tipadas por actividad/cuadro y los bloques top-level consolidados. Tres ejes operativos:

#### §5.1.1. Criterios `principal` vs `recurrente` + lógica de 3 pasos

Una categoría entra en `principal` cuando es contenido nuevo declarado en el índice de la unidad actual (`nc1-curso.json` → `unidades[N].vocabulario[]` / `gramatica[]` / `pronunciacion_ortografia`).

Una categoría entra en `recurrente` cuando **cumple los tres criterios**:

1. **Frecuencia.** Aparece con suficiente recurrencia en la unidad y/o a lo largo del curso como para merecer consolidarse.
2. **Posición.** O bien (a) ya fue principal en una unidad anterior, o bien (b) no forma parte del principal declarado en unidades posteriores pero es relevante para comprender textos y ejercicios de esta unidad.
3. **Valor pedagógico.** Su reaparición tiene función didáctica clara: consolidación, ampliación, contraste o apoyo a la comprensión.

Si un término no cumple los tres criterios, NO entra como recurrente. En particular:
- Léxico de input incidental que no es lo que la actividad enseña → no entra como vocabulario de la actividad ni como recurrente, salvo que coincida con un campo canónico declarado en otra unidad y cumpla los 3 criterios.
- Léxico que es canónico en una **unidad posterior** y aparece como anticipación → NO se codifica como recurrente. Se anota como anticipación para fase 2 (ver §6.3).

**Excepción autorizada por §0.1 (rara y estrecha).** El autor puede autorizar por §0.1 que una anticipación se conserve en `recurrente` cuando: (a) no sea input incidental y (b) funcione como **soporte pedagógico explícito del principal de la unidad actual** (no mero input rico). En ese caso, la entrada conserva su sitio en `recurrente` y debe llevar: (1) `descripcion` que declare explícitamente la anticipación y la unidad principal posterior; (2) entrada en `_decisiones_ia` que registre la excepción, su motivo y la autorización del autor. PROHIBIDO aplicar esta excepción silenciosamente; siempre vía §0.1 propuesta-en-chat.

#### §5.1.2. Criterios pedagógicos por tiempo verbal

El campo `tiempo` del enum cerrado (`Presente`, `Pretérito indefinido`, `Imperativo`, `Infinitivo`) se asigna según qué use el libro en la actividad/cuadro:

- **`Presente`** — formas conjugadas en presente de indicativo. Es el tiempo dominante en NC1.
- **`Pretérito indefinido`** — formas en pretérito perfecto simple. Si aparece, va aquí.
- **`Imperativo`** — formas imperativas (afirmativo y/o negativo).
- **`Infinitivo`** — forma no personal del verbo cuando se trabaja pedagógicamente **fuera de perífrasis** (listas de verbos en infinitivo, ejercicios de identificación de la forma léxica). En NC1, único representante no personal real.

`Perífrasis` **no es valor del enum** (las perífrasis no son tiempos verbales). Cuando un verbo aparece como auxiliar de una perífrasis (`ir a + inf.`, `querer + inf.`, `tener que + inf.`, etc.), se codifica con su **tiempo real** en `tiempo` (típicamente `Presente`) y la estructura perifrástica se declara en el campo opcional `estructura_perifrastica` del objeto verbal (ver schema §3.2). El infinitivo complemento NO se registra como entrada verbal separada. Detalle de la codificación en §5.2.

**Regla de cierre operativa:** un verbo entra en `tiempos_y_verbos` solo si la actividad/cuadro hace que sus formas concretas aparezcan (ver §5.2). Mera mención léxica del infinitivo en una lista de palabras va a `vocabulario`, no a `tiempos_y_verbos`.

#### §5.1.3. Redacción de `descripcion` por unidad

Cada entrada de los bloques consolidados lleva un campo `descripcion: { "U<n>": <texto> }` con texto libre por unidad. Reglas:

- **Obligatoria** en cada entrada de `principal` de cada bloque consolidado.
- **Opcional** en `recurrente`.
- El texto explica qué se enseña del campo en esa unidad, con referencia PCIC cuando aplique (`pcic-a1-vocabulario.json`, `pcic-a1-gramatica.json`, `pcic-a1-pronunciacion-ortografia.json`).
- Formato sugerido para principal: `"PCIC A1 §X.Y.Z — [descripción breve del fenómeno y de cómo lo trabaja la unidad]."`
- Para recurrente: descripción breve que justifique los 3 criterios cumplidos (frecuencia + posición + valor pedagógico).

### §5.2. Verbo soporte vs paradigma trabajado

**Aplica a:** poblar `actividad.tiempos_y_verbos` y `cuadro.tiempos_y_verbos`.

**Regla operativa.** Un verbo entra en `tiempos_y_verbos` cuando **sus formas concretas aparecen** en la actividad/cuadro **Y** el lema está canonizado en la unidad actual o en una unidad anterior del curso (según `verbos-canonicos.json` y/o `nc1-curso.json`).

**Regla de anticipación (no se registra hacia adelante).** Si el lema es canónico de una unidad **posterior**, sus formas que aparezcan en la unidad actual son **input incidental** y NO se registran como entrada verbal en `tiempos_y_verbos`. Su trabajo pedagógico ocurre después; no se anticipa en el inventario. La decisión se toma siempre **por el lema**, no por la forma concreta visible. Esto aplica por igual a:
- Formas conjugadas aisladas (`hacemos pasta` en U4, con `hacer` canónico de U6 PRE → no entra).
- Formas auxiliares de perífrasis (`vamos a preparar` en U4, con `ir` canónico de U6+ → no entra).
- Infinitivos sueltos cuyo lema es canónico de unidad posterior.

Casos típicos cuando el lema SÍ pertenece a la unidad actual o anterior:
- Verbo cuya conjugación se trabaja explícitamente (completar formas, transformar, conjugar) → entra. Foco directo.
- Verbo recurrente que aparece en frases del input para ilustrar OTRO contenido (demostrativos, posesivos, vocabulario) → entra. Refuerza paradigma ya conocido.
- Verbo en infinitivo dentro de una lista de palabras a aprender léxicamente (sin conjugación posterior) → NO entra en `tiempos_y_verbos`. Va a `vocabulario`.

**Codificación de perífrasis (alineado con schema §3.2 y §5d).** Cuando el verbo entra y aparece como **auxiliar de una perífrasis** (`ir a + inf.`, `querer + inf.`, `tener que + inf.`...), se codifica con su **tiempo real** (típicamente `Presente`) en el campo `tiempo` y la estructura se declara en el campo opcional `estructura_perifrastica`. **El infinitivo complemento NO se registra como entrada verbal separada**: queda implícito en `estructura_perifrastica`. `Perífrasis` no es valor del enum `tiempo`.

Ejemplo: en *"Quieres comer carne"*, `querer` entra con `tiempo: "Presente"`, `formas_trabajadas: ["Quieres"]`, `estructura_perifrastica: "querer + infinitivo"`. `comer` **no** se registra como entrada separada en esa actividad (queda implícito); si `comer` tiene apariciones conjugadas propias en otras actividades de la unidad, esas sí entran con su `tiempo: "Presente"` correspondiente.

**Cuándo escalar al autor:** si una forma aparece pero el contexto no deja claro si es verbo soporte trabajado o mención léxica suelta, escalar por §0.1.

**Regla de exclusión por metalengua de instrucción (transversal a las 4 dimensiones).** Las palabras (formas verbales, lemas léxicos, marcadores gramaticales, fenómenos pron/orto) que aparecen **únicamente en la metalengua de instrucción** del libro **NO se codifican** en las 4 listas tipadas de `actividad`/`cuadro` (`vocabulario`, `tiempos_y_verbos`, `gramatica`, `pronunciacion_ortografia`), **NO propagan apariciones** en los 4 bloques consolidados (`vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`) ni en los 4 registries canónicos (`campos-semanticos-canonicos.json`, `verbos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`).

**Qué cuenta como metalengua (excluida):**

- `actividad.instruccion_original` — enunciado del libro dirigido al alumno como acción (*"Lee y escucha"*, *"Escribe"*, *"Completa con…"*, *"Marca verdadero o falso"*, *"Representa el diálogo delante de la clase"*).
- `cuadro.titulo` cuando es etiqueta editorial metalingüística: verbos imperativos del tipo *"Observa"*, *"Para aprender"*, *"Recuerda"*, *"¡Atención!"*, *"Fíjate"*. Sus formas verbales y los lemas léxicos que figuren ahí son metalengua, no contenido.

**Qué cuenta como contenido didáctico (sí codifica):**

- Cuerpo de cuadros: reglas explícitas, paradigmas, listas, tablas, ejemplos modelados al alumno.
- En actividades: `datos.*`, `dialogo`, `dialogo_completo`, `texto`, `texto_completo`, `respuestas`, `audio.transcripcion`, `items_libro`, `muestra_de_lengua`, opciones de selección.

**Aplicación:**

- Aplica a cualquier lema/palabra/categoría, incluidos los que también son canónicos en alguna unidad del curso.
- Aplica con independencia del modo verbal (imperativo *Lee*, presente *Comprueba*, infinitivo *Repetir*).
- Solo se codifican formas/palabras que aparecen en el **contenido didáctico** según la tabla anterior.
- Lista provisional (no exhaustiva) de verbos imperativos típicos de enunciado en NC1: *Lee, Mira, Escucha, Repite, Escribe, Completa, Subraya, Marca, Relaciona, Ordena, Clasifica, Contesta, Responde, Pregunta, Continúa, Imagina, Crea, Habla, Piensa, Comprueba, Busca, Forma, Señala, Elige, Adivina, Representa, Practica*.

**Casos ambiguos (escalar §0.1):**

- Un mismo lema aparece en el enunciado Y en el contenido didáctico de la misma actividad. Codificar **solo** desde el contenido didáctico; descartar el enunciado aunque coincida léxicamente. Si la instrucción cita literalmente el contenido (*"Lee este texto: 'Mi padre lee el periódico'"*), proponer en chat antes de codificar.
- Un cuadro entero formulado como instrucción (*"Observa cómo se forman los gentilicios:"* + patrón debajo): el patrón es contenido; el verbo del título (*"Observa"*) es metalengua.
- Marcadores espaciales o léxico de contexto que aparecen solo en una instrucción de aula (*"Representa el diálogo delante de la clase"* — *delante* no es léxico atestado de la unidad). No codificar; escalar si el caso es prototípico nuevo.

### §5.6. Canon semántico léxico — asignación del nombre canónico

**Aplica a:** asignar el nombre canónico de **campos semánticos léxicos**, que aparecen como:
- **Clave** dentro de los sub-bloques `principal`/`recurrente` de `vocabulario_consolidado`.
- **Referencia** en `actividad.vocabulario` y `cuadro.vocabulario`.

**No aplica a:**
- `tiempos_y_verbos_consolidado` (lista plana de lemas; el lema canónico vive en `verbos-canonicos.json` con política propia — forma de diccionario).
- `gramatica_consolidada` y `pronunciacion_ortografia_consolidada` (naming canónico de categorías gramaticales o fonético-ortográficas vive en sus propios registries `gramatica-canonica.json` (17 categorías) y `pronunciacion-ortografia-canonica.json` (7 categorías), poblados en v10.117; aplican política análoga al léxico: naming canónico literal del registry, fallback a `_pendiente_canon` con escalado al autor si no hay categoría que aplique).

**Universo válido para léxico.** `campos-semanticos-canonicos.json` (fuente única). Naming canónico literal, no `snake_case` ni invenciones.

- ✅ `"Parientes"`, `"Profesiones y cargos"`, `"Asignaturas"` (canónicos literales del registry).
- ❌ `"parientes"`, `"campo_familia"`, `"vocabulario_familiar"`, `"Profesiones"` (variantes con minúscula, snake_case o canónicos no literales).

**Árbol de decisión cuando aparece un campo léxico:**

```
¿El canónico ya existe en `campos-semanticos-canonicos.json` (literal)?
├── Sí → usar el canónico literal.
└── No →
    ¿El contenido viene del índice del libro (`nc1-curso.json` → `vocabulario[]` / `contenido_general[]`)?
    ├── Sí → escalar en chat (§0.1): el autor decide si se añade al registry como nueva entrada del índice editorial.
    └── No →
        ¿Está cubierto por una sección PCIC A1 aplicable (`pcic-a1-vocabulario.json`)?
        ├── Sí → escalar en chat: el autor decide si se añade al registry con origen PCIC.
        └── No → escalar en chat (§0.1). Solo si la decisión queda bloqueada, marcar `_pendiente_canon` (ciclo de vida en §5.9).
```

**Regla de cierre operativa:** PROHIBIDO inventar un nombre canónico en caliente. Si no hay canónico seguro, primero escalar en chat. Solo si la decisión queda explícitamente bloqueada, escribir `_pendiente_canon` (su ciclo de vida está en §5.9).

### §5.7. Heterogeneidad semántica intraejercicio

**Aplica a:** actividades que reúnen léxico semánticamente heterogéneo en un mismo ejercicio (POS distintos, campos semánticos distintos, dominios no homogéneos).

**Regla operativa.** Cuando una sola actividad contiene léxico que **no encaja bajo un único campo canónico**, NO forzar agrupación artificial en un campo único. Tampoco inventar un campo paraguas que no exista en el registry.

**Procedimiento:**
1. Aplicar §0.1 (propuesta-en-chat): plantear al autor la naturaleza heterogénea con los términos concretos detectados y 2-3 opciones razonables (ej. (a) distribuir entre campos existentes; (b) abrir un canónico nuevo en el registry; (c) marcar como ambigua).
2. Si tras la propuesta el autor decide distribuir el léxico entre varios campos canónicos existentes, la actividad referencia múltiples campos en `actividad.vocabulario`. Cero contradicción.
3. Si la heterogeneidad es estructural y el autor no autoriza canónico nuevo, marcar la actividad con `_funcion_ambigua: true` Y declarar `_pendiente_canon` en las claves de los campos semánticos no resueltos. Ambas marcas bloquean cierre (§5.9.1/§5.9.2).

**Errores prohibidos:**
- PROHIBIDO forzar todo el léxico bajo un campo canónico que solo cubre parte real.
- PROHIBIDO inventar un canónico paraguas ad hoc ("Léxico mixto", "Vocabulario diverso", etc.).
- PROHIBIDO codificar la heterogeneidad silenciosamente como `_pendiente_canon` sin propuesta-en-chat previa.

**Ejemplo histórico (fixture U2-propuesta p30-act3):** *descanso, distintas, alrededor de, extraescolares, optativas* — POS distintos (sustantivo, adjetivo, locución), campos distintos. Resolución: la actividad se marca `_funcion_ambigua: true` y los términos no resueltos quedan como `_pendiente_canon` en sus respectivas referencias; el autor escala caso por caso.

### §5.9. Ciclo de vida de marcas internas

**Aplica a:** las marcas internas declaradas en `schema-inventario.md` §14: `_pendiente_canon`, `_funcion_ambigua`, `_decisiones_ia`.

#### §5.9.1. `_pendiente_canon`

- **Cuándo se permite escribirla:** solo si el autor ha sido consultado por §0.1 y la duda no se ha resuelto a tiempo o exige investigación posterior. PROHIBIDO escribirla por defecto sin consulta previa.
- **Dónde puede aparecer en el JSON:** (a) como valor de un campo de categoría canónica, (b) como clave transitoria dentro de un sub-bloque `principal`/`recurrente` de cualquier bloque consolidado.
- **Cómo se resuelve antes del cierre:** el autor decide el canónico real (vía Claude Code en chat), la marca se sustituye por el canónico, el inventario puede cerrar.
- **Bloquea cierre:** sí. Error duro del validador.

#### §5.9.2. `_funcion_ambigua`

- **Cuándo se permite escribirla:** solo si el autor ha sido consultado por §0.1 y la ambigüedad no se ha resuelto. PROHIBIDO escribirla por defecto sin consulta previa.
- **Dónde puede aparecer:** como campo booleano dentro de una entrada de categoría en cualquier bloque consolidado, o dentro de una actividad. Forma exacta: `"_funcion_ambigua": true`.
- **Cómo se resuelve antes del cierre:** el autor decide la función real (vía Claude Code en chat), la marca se elimina del JSON, el inventario puede cerrar.
- **Bloquea cierre:** sí. Error duro del validador.

#### §5.9.3. `_decisiones_ia`

- **Cuándo se escribe:** durante toda la corrida. Cada decisión no trivial que la IA toma o que el autor resuelve en chat se registra aquí con suficiente detalle.
- **Dónde aparece:** como array de strings en top-level del inventario, o dentro de una actividad concreta. Ambas instancias coexisten.
- **Bloquea cierre:** no. Es auditoría persistente.

**Gatillo común de escalada (regla §0.1 aplicada a estas marcas):**
- Antes de escribir `_pendiente_canon` → preguntar en chat con opciones.
- Antes de escribir `_funcion_ambigua: true` → exponer la ambigüedad y opciones.
- `_decisiones_ia` no requiere gatillo de chat; registra decisiones que ya se tomaron.

### §5.10. Aparición material como condición de codificación

**Aplica a:** la evidencia que justifica las apariciones codificadas en las listas tipadas de actividad/cuadro y, por derivación, en los bloques consolidados. **No regula** el valor literal del label canónico almacenado en la lista tipada (que sigue siendo nombre del registry).

#### Distinción A / B

**Categoría A — superficie textual.** Exige **aparición literal** en el contenido didáctico definido en §5.2.

- `vocabulario_consolidado.{...}.items[].palabra` — lemas léxicos (`huevo`, `mexicano`).
- `tiempos_y_verbos_consolidado[].formas_trabajadas` — formas verbales (`tengo`, `gustas`).
- `gramatica_consolidada.{...}.items[].palabra` cuando es realización superficial: interrogativos (`qué`), pronombres (`tú`, `me`), alternancias (`un/una`), secuencias modelo cortas.

**Categoría B — etiqueta / paradigma editorial.** No exige literalidad, pero exige **justificación pedagógica explícita en la evidencia de la unidad**; cuando haya `descripcion` (obligatoria en `principal`, opcional en `recurrente` por §5.1.3), debe recogerla.

- Claves de categoría de cualquier bloque.
- `gramatica_consolidada.{...}.items[].palabra` cuando es fórmula condensada o paradigma editorial (`A mí me gusta(n)`, `cuánto/-a/-os/-as`).
- `pronunciacion_ortografia_consolidada.{...}.items[].palabra` íntegro (notación técnica).

#### Criterio discriminante para gramática

¿El alumno lo lee, escribe, dice o ve literal en el material (incluido el cuadro)? → A. ¿Es descripción editorial del fenómeno? → B.

#### Errores prohibidos

- PROHIBIDO codificar categoría A por inferencia, anticipación, elisión o paradigma completado.
- PROHIBIDO codificar categoría B sin justificación pedagógica explícita en la evidencia de la unidad.

> **Nota de remitencia (no novedad de §5.10).** La exclusión de `instruccion_original` y de cualquier metalengua definida como tal en §5.2 ya está vigente. §5.10 no introduce esa prohibición; se apoya en ella: ninguna fuente A puede sustentarse en metalengua de instrucción excluida por §5.2.

#### Efecto operativo sobre fuentes

- Ítem A: si una fuente no verifica aparición literal, se retira esa fuente. Si ninguna verifica, se retira el ítem completo.
- Ítem B: la fuente se mantiene si la actividad/cuadro trabaja el fenómeno; la justificación va en `descripcion` cuando exista.

#### Cuándo escalar

Si dudas si un ítem es A o B, o si una fuente A roza el límite, aplicar §0.1 propuesta-en-chat antes de codificar o retirar.

### §5.11. Unificación de flexiones en `vocabulario_consolidado`

**Aplica a:** items de `vocabulario_consolidado.{principal,recurrente}.<categoria>.items`.

**Regla obligatoria.** Cuando **dos o más flexiones** (masc/fem, sing/plural, y combinaciones) **del mismo lema están atestadas** en la unidad (cada una aparece literalmente según §5.10), se unifican en **una sola entrada** con **lema canónico singular**:

- en **adjetivos y gentilicios** que flexionan en género, el lema canónico es la **forma masculina singular** (`argentino`, `mexicano`, `francés`, `primero`);
- en **sustantivos**, el lema canónico es la **forma singular conservando su género léxico** (`manzana`, `pizza`, `huevo`, `tomate`).

Las fuentes de todas las flexiones atestadas se fusionan en esa entrada única.

**Cuando solo una forma está atestada en la unidad** (sin par flexivo atestado), el item se **mantiene verbatim** con la forma que aparece. No se infiere ni se genera la otra forma del lema. Ejemplos: si en la unidad solo aparece `argentina` y nunca `argentino`, el item del consolidado es `argentina`. Si solo aparece `colombianas`, el item es `colombianas`. Si solo aparece `madrileño`, el item es `madrileño`.

**Ejemplos con 2+ formas atestadas (se unifican):**
- Adjetivos/gentilicios: `argentino` + `argentina` + `argentinos` + `argentinas` → `"argentino"`.
- Adjetivos/gentilicios: `mexicano` + `mexicana` → `"mexicano"`.
- Adjetivos/gentilicios: `francés` + `francesa` + `franceses` + `francesas` → `"francés"`.
- Ordinales: `primero` + `primera` → `"primero"`.
- Sustantivos masculinos: `huevo` + `huevos` → `"huevo"`; `tomate` + `tomates` → `"tomate"`.
- Sustantivos femeninos: `manzana` + `manzanas` → `"manzana"`; `pizza` + `pizzas` → `"pizza"`; `zanahoria` + `zanahorias` → `"zanahoria"`.

**Ejemplos con una sola forma atestada (verbatim):**
- Solo `argentina` (no `argentino`) → item `"argentina"`.
- Solo `colombianas` (no `colombiano`/`colombiana`/`colombianos`) → item `"colombianas"`.
- Solo `madrileño` → item `"madrileño"`.
- Solo `patatas` (no `patata`) → item `"patatas"`.

**Excepciones (no se unifican aunque haya varias formas):**
- **Compuestos multi-token con identidad propia**: `huevo frito`, `zumo de naranja`, `pollo a la catalana`.
- **Nombres propios**.

**Aplicación retroactiva:** unidades existentes con dos items separados (`argentino` y `argentina`, ambos atestados) se colapsan al lema canónico según la regla anterior. Items con notación `lema/-a` en notación verbatim de registry (ej. `argentino/-a`) se reescriben: al masculino singular **solo si esa forma está atestada** en la unidad; si solo una forma flexiva está atestada, el item pasa a esa forma verbatim. Validador 0/0/0 obligatorio.

**No aplica a** `tiempos_y_verbos_consolidado` (un lema verbal ya es masculino infinitivo por contrato), `gramatica_consolidada` ni `pronunciacion_ortografia_consolidada` (sus items no son palabras flexionables sino categorías/patrones).

**Relación con §5.10:** §5.11 opera sobre items que ya cumplen §5.10 (aparición material). Nunca crea formas inferidas — la condición de unificación es que al menos dos flexiones del lema estén atestadas.

**Relación con §6.4** (formas verbales): §6.4 normaliza a minúscula en `tiempos_y_verbos_consolidado.formas_trabajadas`; §5.11 unifica flexiones atestadas en `vocabulario_consolidado.items`. Paralelas pero distintas.

---

## §6. Derivación de los 4 bloques top-level consolidados

Los 4 bloques (`vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`) son **derivados** del agregado de las 4 listas tipadas de actividades y cuadros de la unidad. No se rellenan a mano de forma independiente.

### §6.1. Construcción de `principal` vs `recurrente`

Cada categoría candidata pasa por el filtro de §5.1.1.
- **`principal`:** categorías que coinciden con el índice editorial de la unidad (`nc1-curso.json` → `unidades[N].vocabulario[]`/`gramatica[]`/`pronunciacion_ortografia`).
- **`recurrente`:** categorías que cumplen los 3 criterios y no son principales de la unidad actual.

El barrido sistemático que detecta los candidatos es §0.3.

### §6.2. Síntesis de categorías recurrentes

Cuando dos o más categorías canónicas de unidades anteriores se presentan **integradas e indistinguibles** en la unidad actual (ej. art+sust+adj concordando), proponer en chat una categoría sintética + categorías separadas. Decide el autor (regla §0.2). PROHIBIDO aplicar síntesis silenciosamente.

### §6.3. Anticipación

Un término que aparece como input incidental en la unidad N pero es **canónico en una unidad posterior** N+k (declarado en `nc1-curso.json` → `unidades[N+k]`) NO se codifica como `recurrente` en U(N).

- En **migración real** de inventarios viejos al nuevo modelo: se anota en `_migracion_rediseno.anticipaciones_detectadas_para_fase_2`.
- En **fixtures exploratorias**: se anota en `_fixture_exploratoria.hallazgos.anticipaciones_detectadas_para_fase_2`.
- En **inventarios canónicos en producción**: la anticipación se reporta a fase 2 (capa 1, R1) como alerta cross-unidad.

Para que un término entre como `recurrente`, debe cumplir los 3 criterios de §5.1.1 Y **no ser canónico en una unidad posterior**.

**Excepción autorizada por §0.1 (alineada con §5.1.1).** El autor puede autorizar por §0.1 que una anticipación se conserve en `recurrente` cuando: (a) no sea input incidental y (b) funcione como **soporte pedagógico explícito del principal de la unidad actual** (no mero input rico). Requisitos formales: `descripcion` declara la anticipación y la unidad principal posterior; `_decisiones_ia` registra la excepción y su motivo. PROHIBIDO aplicar silenciosamente. Esta salvedad es la misma que §5.1.1 y aplica por simetría a este §6.3.

### §6.4. Normalización de `formas_trabajadas` en el consolidado

**Aplica a:** derivación del bloque top-level `tiempos_y_verbos_consolidado` (shape §9.2 del schema).

**Política dual según nivel:**
- **En actividad y cuadro** (`actividad.tiempos_y_verbos[].formas_trabajadas`, `cuadro.tiempos_y_verbos[].formas_trabajadas`): literalidad estricta del libro. Si el libro escribe *"Tengo 13 años..."* en una frase de mensaje, la forma se transcribe como `"Tengo"` (con mayúscula inicial). Actividad/cuadro es transcripción.
- **En el bloque consolidado** (`tiempos_y_verbos_consolidado[].formas_trabajadas`): minúscula al agregar. La forma `"Tengo"` de actividad se acumula como `"tengo"` en consolidado. Consolidado es derivado canónico, no transcripción.

**Razón:** evitar duplicados artificiales entre `["Tengo", "tengo"]` que serían la misma forma con capitalización accidental.

**Excepción:** nombres propios o siglas dentro de una forma compleja (raro en verbos A1) — escalar en chat por §0.1 antes de normalizar.

### §6.5. Sufijo `@R` en fuentes — marcador de localización

**Aplica a:** elementos de `fuentes` en cualquier entrada de los bloques consolidados.

**Regla operativa (v10.145).** Una palabra del consolidado lleva sufijo `@R` en su fuente si y solo si esa palabra **aparece únicamente en el campo `respuestas[]`** de la actividad citada y no en su input (`instruccion_original`, `datos.*`, `audio.transcripcion`, `items_libro`, `dialogo`, `texto`, `muestra_de_lengua`, opciones, etc.).

**`@R` es marcador de localización**, no de naturaleza pedagógica. Aplica a **cualquier `tipo` de actividad** (productivo o no): `completa_huecos`, `escucha_y_responde`, `relaciona`, `responder_preguntas_cerradas`, `seleccion_multiple`, `produccion_escrita_guiada`, `interaccion_oral`, etc. La dimensión pedagógica (productividad) vive en `actividad.tipo` y se cruza en runtime cuando hace falta — **no se codifica en el sufijo**.

> **Cambio de contrato v10.145.** El contrato anterior restringía `@R` a 5 tipos productivos (`produccion_escrita_guiada`, `expresion_escrita_libre`, `expresion_oral_libre`, `tarea_final`, `interaccion_oral`), lo que generaba falsos negativos sistemáticos en actividades no-productivas con la palabra revelada únicamente en respuestas (audio + completa_huecos, relaciona donde el lema vive en la columna-respuesta, etc.). El "Chequeo previo OBLIGATORIO contra los 5 productivos" queda retirado.

**Cuándo NO aplica:** las fuentes de cuadro (`cuadro@pNN` o `cuadro@pNN#K`) nunca llevan `@R`. Los cuadros no tienen campo `respuestas`.

**Ejemplo:**
- Palabra `"cocina"` aparece solo en `respuestas[]` de `p59-act4` (`completa_huecos`, no productivo). Fuente: `"p59-act4@R"`.
- Palabra `"cocina"` aparece en `datos.items_libro` Y en `respuestas[]` de `p52-act3` (`clasifica`, no productivo). Dual-tracking: dos fuentes `"p52-act3"` + `"p52-act3@R"`.
- Palabra que el alumno produce como respuesta esperada en un correo (`expresion_escrita_libre`) y no aparece previamente en el input → fuente `"pNN-actMM@R"`.

**Dual-tracking (input + respuesta en la misma actividad).** Si la palabra aparece **tanto en el input** (cualquier campo de input enumerado arriba) **como en `respuestas[]`** (ya sea forma idéntica o variante única), la fuente se codifica **dos veces** en la misma lista de `fuentes`: una vez sin sufijo (`pNN-actMM`) y una vez con `@R` (`pNN-actMM@R`). El dual-tracking refleja que la actividad aporta material por dos vías distintas (input + respuesta). Auditoría posterior puede usar esta doble entrada para reconstruir qué fue input y qué fue respuesta. Aplica a cualquier tipo de actividad.

**Solucionario "Posibles respuestas:" cuenta como respuesta.** Cuando el libro pone *"Posibles respuestas:"*, *"Modelo:"*, *"Solución:"* en la zona de respuestas (típico en mediación, interaccion_oral con búsqueda de información, expresión libre, tareas finales), el **marcador** se descarta (convenciones-y-casos §1.5) pero el **contenido subsiguiente** se transcribe a `respuestas[]` del JSON. Ese contenido cuenta como respuesta a efectos de §6.5: si una palabra aparece únicamente ahí, **lleva `@R`** (con independencia del `tipo`).

**Caso prototípico de input escueto + solucionario rico.** Actividades de `interaccion_oral` o `tarea_final` con subtipo de **mediación** o **búsqueda de información** suelen tener input escueto (solo enunciado + temas abstractos) y solucionario con la información concreta que el alumno construye. Todo lo que aparece únicamente en ese solucionario lleva `@R`. Ejemplo material en NC1: U4 `p49-act9` (`interaccion_oral`, subtipo `busqueda_informacion_y_mediacion`) tiene 12 ítems léxicos que aparecen solo en el solucionario y por tanto llevan `@R`. Bajo el contrato v10.145, este caso ya no es excepción a una regla por tipo — es un ejemplo del patrón general.

### §6.6. Regla 11 — `audio.transcripcion` como condición de fuente válida

**Aplica a:** decisión de si el contenido auditivo de una actividad aporta léxico/verbos/gramática/pronunciación a los bloques consolidados.

**Regla operativa.** El contenido de un audio cuenta como fuente válida para los bloques consolidados **solo si** `audio.transcripcion` está presente y no vacío. Sin transcripción, lo que el alumno escucha no es texto recuperable y NO genera entradas en `vocabulario`, `tiempos_y_verbos`, `gramatica` ni `pronunciacion_ortografia`.

**Cómo se aplica:**
- Si la actividad tiene `audio.presente: true` y `audio.transcripcion` presente → el contenido del audio cuenta. Las palabras/lemas/categorías extraídas de él entran a las listas tipadas de la actividad y, agregadas, a los bloques consolidados.
- Si la actividad tiene `audio.presente: true` pero sin `audio.transcripcion` → el contenido auditivo NO cuenta como fuente. Las listas tipadas se pueblan solo desde texto verbatim del libro (items_libro, ejemplo_libro, etc.). El audio queda registrado en el shape de la actividad pero no aporta léxico al consolidado.

**Razón:** la trazabilidad léxica exige texto recuperable. Sin transcripción, la palabra escuchada no se puede citar como fuente verificable.

---

## §7. Unidades atípicas

Algunas unidades NO tienen las 5 secciones canónicas (vocabulario / gramatica / comunicacion / destrezas / cultura). Caso típico: la unidad introductoria U0 "Punto de partida" (pre-A1).

**Cuando ocurra:**
1. Mapear todo el contenido a la sección que más se ajuste (en U0: `vocabulario`, porque todo es léxico-fonético).
2. Las demás secciones canónicas quedan vacías: `{ "paginas": [], "actividades_ids": [] }`.
3. Añadir clave top-level `_nota_unidad_atipica` con explicación de por qué es atípica y cómo se mapeó.
4. En `contenidos_indice`, las secciones que no aplican llevan el valor `"(no aplica en esta unidad introductoria)"`.

---

## §9. Política PCIC — cuándo y cómo apoyarse en los archivos PCIC

**Aplica a:** consulta de los archivos `pcic-a1-*.json` durante la corrida.

**Cuatro archivos PCIC disponibles** en `fases/1-extraccion-inventario/`:
- `pcic-a1-vocabulario.json` — apoyo para naming de campos léxicos.
- `pcic-a1-gramatica.json` — apoyo para naming de categorías gramaticales + respaldo de síntesis.
- `pcic-a1-pronunciacion-ortografia.json` — apoyo para categorías de pron/ort (sub-bloques `pronunciacion` y `ortografia`).
- `pcic-a1-comunicacion.json` — recurso disponible fuera de las 4 dimensiones del schema. Útil para descripciones que requieran apoyo pragmático-comunicativo.

**Cuándo consultar PCIC:**
- Al asignar el nombre canónico de una categoría que no existe en el registry (§5.6) → verificar si PCIC la respalda.
- Al redactar `descripcion` por unidad (§5.1.3) → el formato sugerido es `"PCIC A1 §X.Y.Z — ..."`.
- Al proponer una categoría sintética (§6.2) → confirmar respaldo PCIC del fenómeno integrado.

**Lo que PCIC NO hace:**
- PCIC no es autoridad estructural. No fija el shape del JSON (lo hace el schema).
- PCIC no fija reglas operativas (las fija este archivo).
- PCIC es **apoyo** de naming y descripción, no contrato de decisión.

---

## §10. Política de mejora continua

Cuando una extracción real revela un caso no contemplado por el sistema:

1. El autor lo señala.
2. La IA y/o el autor identifican qué archivo del sistema necesita actualización:
   - Shape del JSON → `schema-inventario.md` + alineación de `scripts/validar_inventario.py` (regla de no-divergencia).
   - Decisión / clasificación / población → este archivo.
   - Convención de transcripción o caso editorial → `convenciones-y-casos.md`.
   - Significado terminológico → `glosario.md`.
3. La actualización se hace en una sola sesión, manteniendo el triángulo de coherencia.
4. La siguiente extracción ya lo cubre sin volver a fallar.

**Estos artefactos son fuente viva.** Cada caso documentado mejora el sistema.

---

## Banner de follow-ups (lista viva pendiente)

Reglas operativas detectadas durante el rediseño que aún esperan integración formal en el cuerpo:

- ~~**Heterogeneidad semántica dentro de un mismo ejercicio.**~~ → **integrada en §5.7** (2026-05-15, v10.118).
- ~~**Suite automatizada de verificación global de integridad.**~~ → **implementada en `scripts/verificar_integridad.py`** (2026-05-15, v10.118). Alcance original detallado en `schema-inventario.md` §A.3.
