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
   - **Caso atípico** (U0 y otras unidades introductorias): el índice no sigue las 5 secciones canónicas. Aplicar `reglas-operativas.md` §7 (unidades atípicas) antes de continuar.
4. Para cada página: identificar la sección, las actividades (numeradas o identificadas como tales — ver `reglas-operativas.md` §1 precedencia), los cuadros (con `tipo_cuadro`, ver `reglas-operativas.md` §3) y las notas "Observa" si las hay (`reglas-operativas.md` §4).
5. Para cada actividad: extraer todos los campos del esquema (ver `schema-inventario.md` §3). En U0-U3, observar la convención editorial de sílaba tónica subrayada (`convenciones-y-casos.md` §1.1). Detectar el patrón "primer ítem resuelto como ejemplo" (`convenciones-y-casos.md` §1.2).
6. Construir `vocabulario_consolidado` con los 3 bloques.
7. Construir el índice top-level `secciones`.
8. Validar JSON.
9. Escribir a `unidades/UX/UX-nc1-inventario.json`.
10. Avisar al autor para validación visual de 2-3 páginas al azar.

---

## Schema, reglas y convenciones — archivos externos

> **Schema del JSON** (forma, tipos, enumeraciones cerradas, restricciones validables sin contexto editorial): `schema-inventario.md`. Single source of truth con `scripts/validar_inventario.py`.
>
> **Reglas decisionales** (precedencias actividad/cuadro/nota/autoevaluación, criterios de `tipo` y `tipo_cuadro`, "Para aprender" → actividad / "Observa" → nota, reglas de población de cada campo, bloque `autoevaluacion` cuándo presente/omitido, unidades atípicas): `reglas-operativas.md`.
>
> **Convenciones de transcripción y casebook** (sílaba tónica subrayada hasta U3, patrón "primer ítem resuelto como ejemplo", ejemplos canónicos de `items_libro` por tipo de actividad, ejemplos INCORRECTOS, formato de diálogos y sopas de letras, ejemplo JSON de unidad atípica U0, casos resueltos en U3, política de mejora continua): `convenciones-y-casos.md`.

---

## Reglas decisionales

> **Migradas a `reglas-operativas.md` en A4.2b.** Allí viven ahora: precedencias entre actividad/cuadro/nota/autoevaluación, criterios de asignación de `tipo` y `tipo_cuadro`, "Para aprender" / "Observa", reglas de población de cada campo, cuándo se incluye el bloque `autoevaluacion`, y reglas para unidades atípicas. Single source of truth de precedencias.

---

## Convenciones de transcripción y ejemplos canónicos

> **Migrados a `convenciones-y-casos.md` en A4.2c.** Allí viven: convenciones de transcripción (sílaba tónica subrayada hasta U3, patrón "primer ítem resuelto como ejemplo", textos de lectura, diálogos con marcadores `[1]`/`[2]`, sopas de letras y juegos), ejemplos canónicos de `items_libro` por tipo de actividad (cloze, selección múltiple, cuestionario con opciones), y ejemplos INCORRECTOS de qué no hacer.

---

## Convenciones específicas y ejemplo canónico de unidad atípica

> **Migrados a `convenciones-y-casos.md` en A4.2c.** Allí viven: ejemplo JSON canónico de U0 (§3), convención de sílaba tónica subrayada hasta U3 (§1.1), patrón "primer ítem resuelto como ejemplo" (§1.2). Las reglas decisionales asociadas (cuándo añadir `_nota_unidad_atipica`, qué hacer con secciones vacías) viven en `reglas-operativas.md` §7.

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

## Casos resueltos y mejora continua

> **Migrados a `convenciones-y-casos.md` en A4.2c.** Allí vive el casebook (errores detectados como "Para aprender" confundido con cuadro, casos resueltos en U3) y la política de mejora continua del sistema (cómo se añade un caso nuevo y a qué archivo según su tipo).
