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

1. Leer todas las páginas del PDF (`unidades/UX/fuente/UX-nc1.pdf`). Las unidades regulares tienen ~10 páginas; **las unidades introductorias atípicas son más cortas** (U0 "Punto de partida" tiene 4 páginas).
2. Identificar el rango de páginas del libro (ej: 34-43), título, nivel.
3. Identificar las **secciones del índice de contenidos**:
   - **Caso normal** (U1-U9): 5 secciones canónicas — vocabulario, gramática, comunicación, destrezas, cultura.
   - **Caso atípico** (U0 y otras unidades introductorias): el índice no sigue las 5 secciones canónicas. Aplicar la sección "**Reglas para unidades atípicas (introductorias)**" de este prompt antes de continuar.
4. Para cada página: identificar la sección, las actividades (numeradas o identificadas como tales — ver sección "Reglas para cuadros"), los cuadros (con `tipo_cuadro`) y las notas "Observa" si los hay.
5. Para cada actividad: extraer todos los campos del esquema (ver abajo). En U0-U3, observar la convención editorial de sílaba tónica subrayada (ver sección dedicada). Detectar el patrón de "primer ítem resuelto como ejemplo" (ver sección dedicada).
6. Construir `vocabulario_consolidado` con los 3 bloques.
7. Construir el índice top-level `secciones`.
8. Validar JSON.
9. Escribir a `unidades/UX/UX-nc1-inventario.json`.
10. Avisar al autor para validación visual de 2-3 páginas al azar.

---

## Esquema y schema del JSON

> **Movido a `schema-inventario.md` en A4.2a.** Forma del JSON, schema top-level (10 claves obligatorias + 1 opcional), schema por página, por actividad, por cuadro, schema del bloque de autoevaluación, schema de `_nota_unidad_atipica`, taxonomía cerrada de 17 tipos, enumeración de 5 valores de `tipo_cuadro`, enumeración de 7 secciones canónicas, estructura de `vocabulario_consolidado`, estructura de `respuestas` / `campo_semantico` / `audio`/`imagen`/`video`, estructura de `datos.items_libro`. Single source of truth con `scripts/validar_inventario.py`.
>
> Las **reglas de población semántica** (cuándo aplica `campo_semantico`, qué cuenta como `principal/recurrente/comprension`, contenido de `respuestas`, cuándo marcar `presente=true`, criterios canónicos para asignar cada uno de los 17 tipos de actividad) se **migrarán a `reglas-operativas.md` en A4.2b**. Hasta entonces, el estado real de cada bloque decisional es:
>
> - **Distinción `completa_huecos` vs `produccion_escrita_guiada`:** el único bloque decisional **explícito** que vive en este `prompt.md` (ver sección "Reglas decisionales provisionales" más abajo, restaurada en v10.51 tras detectarse pérdida en A4.2a). Mientras viva aquí, **este es su source of truth**.
> - **Resto de criterios para los 17 tipos** (qué cuenta como `escucha_y_repite`, `clasifica`, `tarea_final`, etc.): **implícitos del dominio editorial**, no canonizados todavía en ningún archivo del repo. Se documentarán por primera vez al construir `reglas-operativas.md` en A4.2b. Hasta entonces, el oráculo de facto son los inventarios trackeados (U0/U1/U3) — qué tipo se asignó a qué actividad allí.
> - **Reglas de población de `vocabulario_consolidado`, `respuestas`, `campo_semantico`, `audio/imagen/video`:** los 3 fragmentos absorbidos en v10.49 viven en `reglas-operativas.md`; el resto vive provisionalmente en este `prompt.md` en sus secciones específicas (más abajo).

---

## Reglas decisionales

> **Migradas a `reglas-operativas.md` en A4.2b.** Allí viven ahora: precedencias entre actividad/cuadro/nota/autoevaluación, criterios de asignación de `tipo` y `tipo_cuadro`, "Para aprender" / "Observa", reglas de población de cada campo, cuándo se incluye el bloque `autoevaluacion`, y reglas para unidades atípicas. Single source of truth de precedencias.

---

## Reglas para `datos.items_libro`

> **Regla de literalidad migrada a `reglas-operativas.md` §5.7.** La obligatoriedad de incluir `items_libro` con el texto literal del libro (no las respuestas) vive ahora en reglas-operativas.
>
> Los ejemplos correctos e incorrectos siguen aquí abajo provisionalmente — se migrarán a `convenciones-y-casos.md` en A4.2c.

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

## Reglas para unidades atípicas (introductorias)

> **Reglas migradas a `reglas-operativas.md` §7.** Allí vive el procedimiento de 4 pasos (mapear contenido a sección que se ajuste, secciones inaplicables vacías, añadir `_nota_unidad_atipica`, valor especial en `contenidos_indice`).
>
> El ejemplo JSON canónico de U0 sigue aquí abajo provisionalmente — se migrará a `convenciones-y-casos.md` en A4.2c.

Ejemplo (U0):
```jsonc
"_nota_unidad_atipica": "Punto de partida (U0) es introductoria pre-A1.1. No sigue la estructura canónica de 5 secciones. Su contenido (países, abecedario, ortografía, números, saludos, instrucciones de aula) se mapea íntegramente a la sección 'vocabulario' por ser principalmente léxico."
```

---

## Convención editorial: sílaba tónica subrayada hasta U3

El libro indica explícitamente (nota a pie en U0 p.9): *"Para facilitar el aprendizaje de la pronunciación, se subraya la sílaba tónica de las palabras de la sección Vocabulario hasta la unidad 3."*

Esto significa:
- **U0, U1, U2, U3:** las palabras de las actividades de vocabulario aparecen con la sílaba tónica subrayada en el libro (ej: `<u>be</u>`, `bo<u>lí</u>grafo`).
- **U4, U5...U9:** sin subrayado en las actividades.

Cuando aparezca esta marca tipográfica en el libro:
- En `datos.items_libro`, marcar la sílaba subrayada con guiones bajos: `_palabra_`. Ejemplo: `"_be_ bolígrafo"` o `"bo_lí_grafo"`.
- Añadir clave `datos._nota` aclarando: `"Las palabras tienen la sílaba tónica subrayada en el libro (convención hasta U3)."`

Nota separada: en las **tarjetas de vocabulario** (output de fase 3), la sílaba tónica está marcada en TODO el libro, no solo hasta U3. Esa convención aplica a fase 3, no a esta fase.

---

## Patrón "primer ítem resuelto como ejemplo"

Muy frecuente en el libro: en actividades numeradas, el libro da el **primer ítem ya resuelto** como modelo, después comienzan los items numerados que el alumno debe resolver.

Ejemplos en U0:
- Act 3 (relacionar): `banco — h` (dado), después `1. león — k`, etc.
- Act 7 (deletrear): `Colombia: ce–o–ele–o–eme–be–i–a` (dado), después `1. España`...
- Act 8 (escucha y escribe): `1. F-ú-t-b-o-l` (dado), después `2. _____`...

Cuando aparezca este patrón:
- El ítem resuelto va a `datos.ejemplo_libro` (string) — el alumno lo ve resuelto, no lo tiene que hacer.
- Los items numerados restantes van a `datos.items_libro` (lista) — el alumno los resuelve.
- Las soluciones de los items numerados van a `respuestas`.

---

## Reglas para cuadros

> **Migrado a `reglas-operativas.md` en A4.2b.** Allí vive todo lo decisional sobre cuadros: cómo asignar `tipo_cuadro` (§3 — los 5 valores con sus criterios), qué NO es un cuadro ("Para aprender" → actividad, "Observa" → nota; §4) y la precedencia general entre actividad/cuadro/nota/autoevaluación (§1).
>
> La enumeración cerrada de los 5 valores de `tipo_cuadro` vive en `schema-inventario.md` §7.

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

## Casos resueltos en extracción real

### Error detectado: "Para aprender" confundido con cuadro gramatical
En extracción real de una unidad, la caja "Para aprender" de la sección de Gramática fue clasificada como `cuadros` con `tipo_cuadro: gramatical`. **Es incorrecto.** "Para aprender" es una **actividad** (ver sección anterior). Esta es la corrección que diferencia los dos elementos.

### Casos resueltos en U3

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
