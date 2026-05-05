# Prompt: extracción del inventario JSON de una unidad

> **Quién lo usa:** Claude Code en chat, cada vez que se extrae el inventario de una unidad nueva del libro.
> **Quién lo mantiene:** el autor + Claude Code (entre los dos, conforme aparecen casos nuevos o errores).
> **Cómo se invoca:** `Extrae el inventario de UX siguiendo fases/1-extraccion-inventario/prompt.md.`
> **Output:** un único archivo `unidades/UX/UX-nc1-inventario.json`.

---

## Regla de oro (no negociable)

**El JSON debe contener el contenido de cada actividad EXACTAMENTE COMO APARECE EN EL LIBRO, no como referencia ni como interpretación.**

Esto incluye:
- Las frases con huecos (con `_____` marcando el hueco), no las respuestas en lugar del enunciado.
- Los textos de lectura completos (no resumidos).
- Los diálogos completos (con marcadores `[1]`, `[2]` para huecos).
- Las opciones de selección múltiple tal cual están redactadas.
- Las palabras del recuadro/banco tal cual.
- Las cuadrículas (sopa de letras, etc.) con todas sus celdas.
- Las imágenes descritas con detalle suficiente para reconstruir lo que ve el alumno.

Si en el libro hay un texto, el JSON debe poder regenerar el texto. Si en el libro hay una tabla, el JSON debe contener la tabla. **No basta con poner solo las respuestas.**

---

## Pasos de la extracción

1. Leer las 10 páginas del PDF (`unidades/UX/fuente/UX-nc1.pdf`).
2. Identificar el rango de páginas del libro (ej: 34-43), título, nivel.
3. Identificar las 5 secciones del índice de contenidos (vocabulario, gramática, comunicación, destrezas, cultura).
4. Para cada página: identificar la sección, las actividades (numeradas), los cuadros gramaticales si los hay.
5. Para cada actividad: extraer todos los campos del esquema (ver abajo).
6. Construir `vocabulario_consolidado` con los 3 bloques.
7. Construir el índice top-level `secciones`.
8. Validar JSON.
9. Escribir a `unidades/UX/UX-nc1-inventario.json`.
10. Avisar al autor para validación visual de 2-3 páginas al azar.

---

## Esquema canónico (10 claves top-level)

```jsonc
{
  "unidad": <int, sin cero>,
  "curso": "nc1",
  "titulo": <str>,
  "paginas_libro": <str, ej: "34-43">,
  "nivel": <str, ej: "A1.1">,
  "fuente": {
    "archivo": "unidades/UX/fuente/UX-nc1.pdf",
    "version_extraccion": "<YYYY-MM-DD>"
  },
  "contenidos_indice": {
    "vocabulario": <str>,
    "gramatica": <str>,
    "comunicacion": <str>,
    "destrezas": <str>,
    "cultura": <str>
  },
  "vocabulario_consolidado": {
    "principal": { "_descripcion": "...", "<Campo>": [palabras] },
    "recurrente": { "_descripcion": "...", "<Categoria>": [palabras] },
    "comprension": { "_descripcion": "...", "<Categoria>": [palabras] }
  },
  "secciones": {
    "vocabulario":  { "paginas": [int], "actividades_ids": [str] },
    "gramatica":    { "paginas": [int], "actividades_ids": [str] },
    "comunicacion": { "paginas": [int], "actividades_ids": [str] },
    "destrezas":    { "paginas": [int], "actividades_ids": [str] },
    "cultura":      { "paginas": [int], "actividades_ids": [str] },
    "evaluacion":   { "paginas": [int], "actividades_ids": [str] },
    "reflexion":    { "paginas": [int], "actividades_ids": [str] }
  },
  "paginas_detalle": [<página>, ...]
}
```

---

## Esquema por página

```jsonc
{
  "pagina": <int>,
  "seccion": <clave normalizada: vocabulario|gramatica|comunicacion|destrezas|cultura|evaluacion|reflexion>,
  "actividades": [<actividad>, ...],
  "cuadros_gramaticales": [<cuadro>, ...]   // opcional
}
```

---

## Esquema por actividad

```jsonc
{
  "id": "UX-pYY-actNN",
  "numero": <int>,
  "tipo": <de la taxonomía cerrada — ver abajo>,
  "destreza": <str: comprension_oral | produccion_oral | ... combinables con +>,
  "instruccion_original": <str literal del libro>,
  "contenido_linguistico": [str],
  "campo_semantico": <str opcional, solo cuando aplique — ver regla abajo>,
  "audio":  { "presente": <bool>, "pista": <int opcional> },
  "imagen": { "presente": <bool>, "descripcion": <str obligatorio si presente=true> },
  "video":  { "presente": <bool> },
  "respuestas": [str],   // SIEMPRE presente. Lista vacía si no aplica.
  "datos": {             // saco abierto para CONTENIDO LITERAL DEL LIBRO
    "subtipo": <str opcional — sopa_de_letras, dialogo_video, programacion_tv, ...>,
    "items_libro": [str],          // contenido tal cual con _____ donde haya huecos
    "texto_completo": <str>,       // texto de lectura completo
    "dialogo_completo": [str],     // líneas del diálogo con [1], [2] en huecos
    "preguntas": [str],            // lista literal de preguntas
    "preguntas_opciones": [{...}], // selección múltiple
    "cuadricula": [[str]],         // sopa de letras
    "frases": [str],               // listado de frases
    "ejemplo_libro": <str>,        // ejemplo entre comillas/cursiva
    "texto_modelo": <str>,         // texto que el alumno toma como modelo
    "nombres_dados": [str],        // listado de nombres/palabras del recuadro
    "palabras_recuadro": [str],
    "horarios_digitales": {<id>: <hora>},
    "programas_tv": [str],
    "peliculas_cartelera": [str],
    "personajes": [str],
    "titulo_dialogo": <str>,
    "pasos": [str],
    "reglas_foneticas": [str],
    "palabras_modelo": [str],
    "expresiones_dadas": [str],
    "afirmaciones_a_corregir": [str],
    "texto_correo": <str>,
    "ejemplos_modelo": [str],
    "objetivo_palabras": <int>
    // ... cualquier dato específico que NO encaje en los campos canónicos
  }
}
```

---

## Esquema por cuadro gramatical

```jsonc
{
  "titulo": <str>,
  "contenido": {
    "tipo": <str — tabla_conjugacion | tabla_interrogativos | tabla_posesivos | ...>,
    // estructura libre según el cuadro, capturando TODO el contenido visible
    "ejemplos": [str]
  }
}
```

---

## Taxonomía cerrada de tipos de actividad (17 valores, provisional)

Usar EXACTAMENTE uno de estos. Si no encaja ninguno, marcar y consultar al autor:

```
escucha_y_repite
escucha_y_responde
completa_huecos
relaciona
ordena
clasifica
seleccion_multiple
verdadero_falso
produccion_oral_pareja
produccion_oral_libre
produccion_escrita_guiada
produccion_escrita_libre
comprension_lectora
comprension_auditiva
busqueda_informacion
tarea_final
juego
```

**Ojo:** no existe `produccion_escrita` "a secas". Si la actividad da pista (relojes, esquema), es `produccion_escrita_guiada`. Si pide texto totalmente libre, `produccion_escrita_libre`.

---

## Reglas para `vocabulario_consolidado`

Tres bloques, cada uno agrupado por categoría/campo semántico:

### `principal`
Vocabulario **declarado en el índice de la unidad** (ej: si el índice dice "Vocabulario: Parientes", aquí va el léxico de parentesco trabajado en la sección Vocabulario).
Agrupado por campo semántico (Familia, Profesiones, Lugares, etc.).

### `recurrente`
Vocabulario que aparece en **varias secciones** de la unidad (no solo Vocabulario). Por ejemplo, si "merendar" aparece en Vocabulario Y en Comunicación Y en Destrezas, va aquí. Agrupado por categoría temática.

### `comprension`
Léxico que **aparece y afecta la comprensión** del estudiante aunque no se trabaje explícitamente. Por ejemplo, palabras del cómic en la sección Cultura, asignaturas mencionadas, conectores básicos. Agrupado por categoría.

**`_descripcion`** dentro de cada bloque explica de qué va. Útil al revisar el JSON.

---

## Reglas para `secciones` (índice top-level)

Las 7 claves son fijas: `vocabulario`, `gramatica`, `comunicacion`, `destrezas`, `cultura`, `evaluacion`, `reflexion`.

Si una sección no existe en la unidad, dejarla con paginas:[] y actividades_ids:[].

`actividades_ids` lista los IDs de actividad de cada sección, en orden de aparición. Permite acceso directo sin recorrer todas las páginas.

---

## Reglas para `seccion` dentro de cada página

Valor normalizado, una de las 7 claves. **NO** texto libre tipo "Vocabulario — Parientes" ni "Comunicación (cont.)".

Las páginas que continúan una sección (ej: p.39 sigue siendo `comunicacion` aunque el libro ponga "Comunicación (cont.)") usan la misma clave normalizada.

---

## Reglas para `respuestas`

**Siempre presente como lista**, vacía si no aplica.

Cuando aplica, recoge la respuesta esperada tal como aparece en el libro del profesor (suele estar marcada en color o en el margen). Cada respuesta como un string en la lista.

Si la respuesta es una opción de selección múltiple, indicar la opción correcta junto con su texto: `"3. → c) Una mezcla de dibujo y texto"`.

Si la respuesta es V/F, formato: `"1. La frase X — V"`.

---

## Reglas para `audio`, `imagen`, `video`

**Siempre presentes como sub-objetos.** Patrón:

```jsonc
"audio":  { "presente": false }
"audio":  { "presente": true, "pista": 31 }

"imagen": { "presente": false }
"imagen": { "presente": true, "descripcion": "<descripción detallada de qué se ve>" }

"video":  { "presente": false }
"video":  { "presente": true }
```

`descripcion` de imagen es **obligatoria** cuando `presente=true`. Suficiente para que un agente que no ve la imagen pueda entender qué muestra.

---

## Reglas para `campo_semantico`

Opcional. Se usa cuando el contenido lingüístico de la actividad pertenece a un campo semántico identificable (Familia, Profesiones, Lugares, etc.).

**Decisión pendiente del autor:** ¿solo en sección vocabulario o en cualquier sección que toque vocabulario? Por ahora, **liberal**: cualquier actividad cuyo contenido pertenezca a un campo semántico lo lleva.

---

## Reglas para `datos.items_libro` (LO MÁS IMPORTANTE)

Para actividades de **completar huecos, opción múltiple, ordenar, clasificar, relacionar y similares**, `items_libro` es **obligatorio** y debe contener **el texto literal del libro**, con los huecos marcados como `_____` (5 guiones bajos).

### Ejemplos correctos

Cloze:
```
"items_libro": [
  "1. Pablo y Jorge (estudiar) _____ en el mismo colegio.",
  "2. Yo (comer) _____ a las dos y veinte."
]
```

Selección múltiple (mostrar las opciones):
```
"items_libro": [
  "1. ¿Dónde / Cuál viven tus abuelos? — En Marbella.",
  "2. ¿Cómo / Cuál os llamáis vosotras? — Yo me llamo Rosa y ella, Alicia."
]
```

Cuestionario con opciones:
```
"datos": {
  "preguntas_opciones": [
    {"pregunta": "¿Qué es el cómic?", "opciones": {"a": "Una fotografía", "b": "Una novela", "c": "Una mezcla de dibujo y texto"}}
  ]
}
```

### Ejemplos INCORRECTOS (lo que hacíamos mal antes)

❌ Solo poner `respuestas` sin `items_libro` para actividades de cloze:
```
"respuestas": ["1. Pablo y Jorge estudian en el mismo colegio."]
"datos": {}   // ← MAL: no se ve el enunciado original
```

❌ Inventar el enunciado:
```
"items_libro": ["1. Conjuga el verbo estudiar para Pablo y Jorge"]   // ← MAL: no es lo que pone el libro
```

---

## Reglas para textos de lectura

Cuando la actividad es leer un texto largo (carta, descripción, artículo), va en `datos.texto_completo` como un único string que reproduce el texto íntegro, **conservando puntuación, mayúsculas y nombres propios tal cual**.

---

## Reglas para diálogos

Cuando hay un diálogo (de video, audio o lectura), va en `datos.dialogo_completo` como lista de strings, una por turno:

```jsonc
"dialogo_completo": [
  "PABLO: Son las once. ¡Por fin el recreo!",
  "GRACIELA: ¡Sí! Julia, ¿[1] _____ hermanos?",
  "JULIA: No, soy hija única ¿y tú?"
]
```

Los huecos van como `[1]`, `[2]`... (números) y la lista de palabras del recuadro va en `datos.palabras_recuadro`.

---

## Reglas para sopas de letras y juegos

Sopa de letras:
```jsonc
"datos": {
  "subtipo": "sopa_de_letras",
  "cuadricula": [
    ["P","R","I","M","O","A","G","E","H"],
    ["O","C","B","A","I","L","J","M","Z"],
    ...
  ],
  "objetivo_palabras": 6
}
"respuestas": ["PRIMO", "HIJO", "TÍO", "HERMANO", "ABUELO", "PADRE"]
```

---

## Reglas para cuadros gramaticales

Cuando una página tiene cuadros (tablas de conjugación, posesivos, interrogativos), van en `cuadros_gramaticales` de la página, **no** dentro de actividades.

Capturar **todo el contenido del cuadro** (filas, columnas, celdas, ejemplos al pie).

---

## Validación post-extracción

Antes de dar el JSON por bueno:

1. **Esquema:** todas las claves obligatorias presentes (10 top-level + por página + por actividad).
2. **IDs únicos:** ningún `id` de actividad repetido.
3. **Tipos válidos:** todos los `tipo` de la taxonomía cerrada (17 valores).
4. **Secciones:** valor de `seccion` en cada página es una de las 7 claves normalizadas.
5. **`respuestas` siempre presente** en cada actividad (lista, aunque vacía).
6. **`audio`/`imagen`/`video` siempre presentes** como sub-objetos.
7. **`items_libro` o equivalente** en toda actividad de completar/elegir/relacionar.
8. **`descripcion` de imagen** obligatoria si `imagen.presente=true`.
9. **JSON parseable** (validar con Python: `json.loads(open(...).read())`).

Cuando exista, ejecutar `python scripts/validar_inventario.py UX`.

---

## Salida

Escribir el JSON en `unidades/UX/UX-nc1-inventario.json`.

Si la carpeta `unidades/UX/` no existe, crearla. Si `unidades/UX/fuente/` no contiene el PDF, abortar y avisar al autor.

---

## Casos resueltos en U3 (referencia para la extracción)

- **Sopa de letras (p.43 act.5):** cuadrícula 10x9, palabras a buscar como respuestas.
- **Diálogo con video y huecos (p.38 act.1):** dialogo_completo con marcadores `[1]`...`[7]`, palabras_recuadro con la lista, respuestas con `"[1] tienes"`.
- **Programación TV (p.41 act.4):** programas_tv + horarios_digitales + respuestas con relación 1→d, 2→c, etc.
- **Pronunciación con z/c (p.39 act.9):** items_libro con `"c/zine"`, `"on c/ze"`, etc.
- **Correo electrónico (p.40 act.1):** texto_correo con el correo entero + afirmaciones_a_corregir como lista + respuestas con la corrección de cada una.
- **Lecturas Javier/Lucía (p.35 acts.6 y 8):** texto_completo con el texto íntegro de cada lectura.

---

## Coste estimado

~25-30k tokens por unidad (10 páginas + esquema + JSON resultante).
Una sola vez por unidad. Para las 9 unidades: ~225-270k tokens en total.

---

## Mejora continua

Cuando se haga una extracción y aparezca un caso no contemplado en este prompt:

1. El autor lo señala.
2. Se añade el caso a este archivo (en "Casos resueltos" o creando una sección nueva).
3. La siguiente extracción ya lo cubre sin volver a fallar.

**Este prompt es una fuente viva.** Cada error documentado mejora el sistema.
