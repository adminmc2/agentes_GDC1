# Convenciones de transcripción y casebook — Fase 1

## §0. Naturaleza del archivo

Este archivo es la **tercera capa viva de soporte** de fase 1, junto a `schema-inventario.md` (shape canónico) y `reglas-operativas.md` (autoridad de decisión).

**Precedencia explícita en caso de conflicto:**

```
schema-inventario.md  >  reglas-operativas.md  >  convenciones-y-casos.md
```

Si una convención de este archivo contradice schema o reglas, **prevalecen ellas**. Esta capa nunca prevalece sobre las dos primeras.

**Naturaleza operativa:**

- Es **lookup puntual durante la corrida**, no lectura obligatoria. Schema y reglas son lectura obligatoria; convenciones se consulta cuando la IA encuentra un caso de transcripción concreto.
- **§1** contiene convenciones de transcripción del PDF al JSON (cómo se rellenan los campos de `datos.*` y de `respuestas` desde el contenido visible del libro).
- **§2** contiene ejemplos canónicos por tipo de actividad.
- **§3** contiene el ejemplo canónico de unidad atípica (la autoridad decisional vive en `reglas-operativas.md` §7).
- **§4** es el **casebook**: casos resueltos en extracciones reales. Sirve para localizar "¿hubo un caso similar antes?", no es autoridad de decisión.
- **§5** es puntero a la política de mejora continua de `reglas-operativas.md` §10.

---

## §1. Convenciones de transcripción del libro al JSON

### §1.1 Literalidad obligatoria

La IA transcribe el contenido del libro **verbatim** al JSON: enunciados, ítems, textos, diálogos, opciones, respuestas dadas. No parafrasea, no resume, no normaliza. Conserva puntuación, mayúsculas, nombres propios y huecos tal cual aparecen.

> Regla operativa anclada en `reglas-operativas.md` §0.0 (principio de literalidad). Esta sección concentra los casos prácticos de transcripción.

### §1.2 Patrón "primer ítem resuelto como ejemplo"

Muy frecuente en el libro: en actividades numeradas, el libro da el **primer ítem ya resuelto** como modelo. Después comienzan los ítems numerados que el alumno debe resolver.

Casos disparadores en U0: act 3 (relacionar) con `banco — h` dado y después `1. león — k`...; act 7 (deletrear) con `Colombia: ce–o–ele–o–eme–be–i–a` dado y después `1. España`...; act 8 (escucha y escribe) con `1. F-ú-t-b-o-l` dado y después `2. _____`...

**Convención al transcribir:**

- El ítem resuelto → `datos.ejemplo_libro` (string) o `datos.ejemplos_modelo` (lista, si hay varios modelos).
- Los ítems numerados restantes → `datos.items_libro` (lista).
- Las soluciones de los ítems numerados → `respuestas`.

El ejemplo no se duplica en `respuestas` ni en `items_libro`: vive solo en `datos.ejemplo_libro` / `ejemplos_modelo`.

### §1.3 Textos del libro: tres campos canónicos

El libro puede presentar contenido textual en tres formatos distintos. La IA decide entre tres campos de `datos`:

| Patrón del libro | Campo `datos` |
|---|---|
| Un texto seguido (carta, artículo, descripción, lectura) | `texto_completo` |
| Diálogo con turnos atribuidos a hablantes alternados | `dialogo_completo` |
| N textos cortos, cada uno atribuido a un personaje distinto | `textos_personajes` |

#### §1.3.1 `texto_completo`

Cuando la actividad presenta un texto largo (carta, descripción, artículo, lectura) como bloque seguido, va en `datos.texto_completo` como **un único string** que reproduce el texto íntegro. Se conservan puntuación, mayúsculas y nombres propios tal cual.

Casos disparadores: lecturas Javier/Lucía de U3 p35 acts 6 y 8.

#### §1.3.2 `dialogo_completo`

Cuando hay un diálogo (de vídeo, audio o lectura) con turnos atribuidos a hablantes que se alternan, va en `datos.dialogo_completo` como **lista de strings, una por turno**:

```jsonc
"dialogo_completo": [
  "PABLO: Son las once. ¡Por fin el recreo!",
  "GRACIELA: ¡Sí! Julia, ¿[1] _____ hermanos?",
  "JULIA: No, soy hija única ¿y tú?"
]
```

**Huecos del diálogo:** se transcriben como `[1]`, `[2]`... (números entre corchetes). La lista de palabras del recuadro asociado va en `datos.palabras_recuadro`.

**Formato canónico de `respuestas` — regla decisional única:** `respuestas` mirror el marcado del input.

- Si el input visible (típicamente `dialogo_completo`) tiene huecos numerados explícitamente con `[N]`, cada entrada de `respuestas` lleva el formato `"[N] valor"` (ej. `"[1] tienes"`). Esto preserva el anclaje hueco→solución.
- Si el input visible (típicamente `items_libro`) lista ítems numerados (`"1. …"`, `"2. …"`), cada entrada de `respuestas` va solo con el valor (`"tienes"`), porque la correspondencia es posicional.
- **No mezclar** ambas variantes en la misma actividad.

Casos disparadores: U3 p38 act1 (diálogo con vídeo y 7 huecos); fixture U4-propuesta p43-act5 (diálogo Rosa/Alberto con 8 huecos).

#### §1.3.3 `textos_personajes`

Cuando el libro presenta **varios textos cortos, cada uno atribuido a un personaje distinto** (típico de actividades de presentación, fichas de personajes, autorretratos paralelos), no se unifican en `texto_completo` ni se transcriben como diálogo. Se usa `datos.textos_personajes` preservando la atribución:

```jsonc
"textos_personajes": [
  { "personaje": "Carmen", "texto": "Hola, me llamo Carmen. Tengo 15 años y vivo en Madrid…" },
  { "personaje": "Luis",   "texto": "Yo soy Luis, soy de Sevilla y tengo 14 años…" },
  { "personaje": "María",  "texto": "¡Hola! Soy María. Vivo en Barcelona con mi familia…" }
]
```

Los nombres se preservan tal cual aparecen en el libro (sin normalizar mayúsculas). El orden refleja el orden visual.

Caso disparador histórico: U5-p58-act01 (cuatro descripciones breves en Destrezas, una por personaje). Convención genérica aplicable a cualquier unidad con el mismo patrón.

### §1.4 Sopas de letras y juegos de cuadrícula

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

`cuadricula` es lista de listas de strings de una letra (mayúscula). `objetivo_palabras` es el número total de palabras a localizar. `respuestas` lista las palabras encontradas.

Caso disparador: U3 p43 act5 (cuadrícula 10×9, 6 palabras de familia).

### §1.5 Marcadores editoriales del libro: NO van en `respuestas`

Cuando el solucionario o el enunciado del libro precede al contenido con un marcador editorial como **`Posibles respuestas:`**, **`Ejemplo:`**, **`Modelo:`**, **`Solución:`**, ese marcador NO se transcribe como ítem de `respuestas`. La regla es:

- El marcador en sí (`Posibles respuestas:`, `Ejemplo:`...) **se descarta**. Es metalengua del libro, no contenido del alumno.
- El contenido que sigue al marcador:
  - Si es **un ejemplo modelo del libro** (típicamente la primera respuesta dada como muestra) → `datos.ejemplo_libro` (string) o `datos.ejemplos_modelo` (lista). Ver §1.2.
  - Si son **respuestas reales** (ej. lista de "posibles respuestas" sugeridas por el solucionario) → `respuestas` **sin el marcador**.

**Ejemplos correctos / incorrectos:**

```jsonc
// ❌ INCORRECTO — el marcador entra como respuesta
"respuestas": ["Posibles respuestas:", "Está en la cocina", "Está encima de la mesa"]

// ✅ CORRECTO — solo las respuestas reales
"respuestas": ["Está en la cocina", "Está encima de la mesa"]

// ❌ INCORRECTO — duplica un ejemplo que ya está en datos.ejemplo_libro
"datos": { "ejemplo_libro": "están" }
"respuestas": ["ejemplo: están", "estamos", "estoy"]

// ✅ CORRECTO — el ejemplo vive solo en datos.ejemplo_libro
"datos": { "ejemplo_libro": "están" }
"respuestas": ["estamos", "estoy"]
```

Casos disparadores históricos: U5-p54-act03 (`Posibles respuestas:` coló como ítem), U5-p55-act02 (`ejemplo: están` duplicó `datos.ejemplo_libro`), U5-p61-act02 (`ejemplo: Encima de la mesa.` idem). Convención genérica aplicable a cualquier unidad con el mismo patrón.

---

## §2. Ejemplos canónicos de `items_libro` por tipo de actividad

> Regla de literalidad obligatoria: ver §1.1 + `reglas-operativas.md` §0.0. Aquí van los ejemplos concretos por tipo.

### §2.1 Cloze (completa_huecos)

```jsonc
"items_libro": [
  "1. Pablo y Jorge (estudiar) _____ en el mismo colegio.",
  "2. Yo (comer) _____ a las dos y veinte."
]
```

### §2.2 Selección múltiple

```jsonc
"items_libro": [
  "1. ¿Dónde / Cuál viven tus abuelos? — En Marbella.",
  "2. ¿Cómo / Cuál os llamáis vosotras? — Yo me llamo Rosa y ella, Alicia."
]
```

### §2.3 Cuestionario con opciones

```jsonc
"datos": {
  "preguntas_opciones": [
    {
      "pregunta": "¿Qué es el cómic?",
      "opciones": {
        "a": "Una fotografía",
        "b": "Una novela",
        "c": "Una mezcla de dibujo y texto"
      }
    }
  ]
}
```

### §2.4 ⚠ Ejemplos INCORRECTOS — lo que NO se hace

❌ Solo poner `respuestas` sin `items_libro` para actividades de cloze:

```jsonc
"respuestas": ["1. Pablo y Jorge estudian en el mismo colegio."]
"datos": {}   // ← MAL: no se ve el enunciado original
```

❌ Inventar el enunciado:

```jsonc
"items_libro": ["1. Conjuga el verbo estudiar para Pablo y Jorge"]
// ← MAL: no es lo que pone el libro
```

❌ Sustituir el hueco por la respuesta:

```jsonc
"items_libro": ["1. Pablo y Jorge estudian en el mismo colegio."]
// ← MAL: la respuesta nunca sustituye al hueco en items_libro
```

---

## §3. Ejemplo canónico de unidad atípica

> Reglas decisionales sobre cuándo añadir `_nota_unidad_atipica` y cómo mapear secciones inaplicables: **autoridad en `reglas-operativas.md` §7**. Aquí va el JSON canónico.

```jsonc
"_nota_unidad_atipica": "Punto de partida (U0) es introductoria pre-A1.1. No sigue la estructura canónica de 5 secciones. Su contenido (países, abecedario, ortografía, números, saludos, instrucciones de aula) se mapea íntegramente a la sección 'vocabulario' por ser principalmente léxico."
```

---

## §4. Casebook — casos resueltos en extracciones reales

Lookup secundario para localizar "¿hubo un caso similar antes?". No es autoridad de decisión.

### §4.1 Errores detectados y corregidos

**"Para aprender" confundido con cuadro gramatical.** En extracción real de una unidad, la caja "Para aprender" de la sección de Gramática (con verbo imperativo dirigido al alumno) fue clasificada inicialmente como `cuadros` con `tipo_cuadro: gramatical`. **Era incorrecto en ese caso** porque tenía tarea: se reclasificó como actividad. La regla bifurca por naturaleza (ver `reglas-operativas.md` §4): con verbo imperativo → actividad; solo informativa → cuadro.

### §4.2 Casos resueltos por unidad

#### §4.2.1 U3

- **Sopa de letras (p.43 act.5):** cuadrícula 10×9, palabras a buscar como respuestas. → §1.4.
- **Diálogo con vídeo y huecos (p.38 act.1):** `dialogo_completo` con marcadores `[1]`...`[7]`, `palabras_recuadro` con la lista, `respuestas` con `"[1] tienes"`. → §1.3.2.
- **Programación TV (p.41 act.4):** `programas_tv` + `horarios_digitales` + `respuestas` con relación `"1→d"`, `"2→c"`, etc.
- **Pronunciación con z/c (p.39 act.9):** `items_libro` con `"c/zine"`, `"on c/ze"`, etc.
- **Correo electrónico (p.40 act.1):** `texto_correo` con el correo entero + `afirmaciones_a_corregir` como lista + `respuestas` con la corrección de cada una.
- **Lecturas Javier/Lucía (p.35 acts.6 y 8):** `texto_completo` con el texto íntegro de cada lectura. → §1.3.1.

### §4.3 Casos pendientes de confirmación con el shape nuevo

Convenciones del modelo viejo cuyo único anclaje material está en unidades aún no extraídas con shape v10.115. Se conservan aquí como referencia hasta que una extracción real las materialice; entonces se promueven a §1.

#### §4.3.1 `columnas_relaciona` (anclaje U6 modelo viejo)

Cuando el libro presenta una actividad de relacionar con **dos columnas visuales separadas** (columna A y columna B con elementos a unir), el modelo viejo proponía `datos.columnas_relaciona` en lugar de `datos.items_libro`:

```jsonc
"datos": {
  "columnas_relaciona": {
    "izquierda": ["1 Juan", "2 Ángel", "3 Roberto", "4 Alba"],
    "derecha": ["a parque", "b museo", "c polideportivo", "d biblioteca"]
  }
}
"respuestas": ["1→a", "2→c", ...]
```

Anclaje material histórico: U6-p63-act05 y U6-p63-act08 (personas → lugares de trabajo). **Pendiente verificación material** con extracción real de U6 bajo shape v10.115. Hasta entonces, no se promueve a §1.

---

## §5. Política de mejora continua

**→ `reglas-operativas.md` §10.**

Cuando una extracción real revela un caso de transcripción no contemplado en este archivo, el procedimiento (señalado por el autor + actualización del archivo apropiado) vive en reglas §10. Si el caso es una convención de transcripción nueva, se añade a §1 de este archivo. Si es un caso editorial concreto, se añade a §4.
