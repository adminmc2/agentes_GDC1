# Prompt: extracción del inventario JSON de una unidad

> **Quién lo usa:** Claude Code en chat, cada vez que se extrae el inventario de una unidad nueva del libro.
> **Quién lo mantiene:** el autor + Claude Code (entre los dos, conforme aparecen casos nuevos o errores).
> **Cómo se invoca:** `Extrae el inventario de UX siguiendo fases/1-extraccion-inventario/prompt.md.`

---

## Objetivo

A partir del PDF del libro de una unidad concreta, generar un único archivo JSON estructurado que capture todo el contenido editorial visible al alumno (actividades, cuadros de referencia, vocabulario, bloque de autoevaluación) según el contrato de datos del proyecto.

## Input

`unidades/UX/fuente/UX-nc1.pdf` — PDF del libro del alumno con texto embebido.

## Output

`unidades/UX/UX-nc1-inventario.json` — un único archivo, formato JSON.

## Definición de éxito

Tras la extracción, las 4 condiciones se cumplen a la vez:

1. `python3 scripts/validar_inventario.py X` devuelve **0 errores y 0 avisos** (o 1 aviso intencional si la unidad es atípica con `_nota_unidad_atipica`).
2. Cada actividad contiene el contenido visible al alumno **exactamente como aparece en el libro**, no como referencia ni como interpretación.
3. El autor revisa visualmente 2-3 páginas al azar en el dashboard y confirma conformidad.
4. Cualquier caso no contemplado en los archivos de soporte (`schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md`) se ha consultado al autor antes de cerrar el JSON.

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

## Artefactos de soporte consultados durante la extracción

Este prompt no contiene el schema ni las reglas decisionales ni las convenciones de transcripción. Esos viven en archivos hermanos en esta misma carpeta:

- **`schema-inventario.md`** — Forma del JSON (estructura, tipos, enumeraciones cerradas, restricciones validables sin contexto editorial). Single source of truth con `scripts/validar_inventario.py`.
- **`reglas-operativas.md`** — Reglas decisionales (precedencias actividad/cuadro/nota/autoevaluación, criterios de `tipo` y `tipo_cuadro`, criterios para "Para aprender" y "Observa", reglas de población de cada campo, bloque `autoevaluacion` cuándo presente/omitido, unidades atípicas). Single source of truth de precedencias.
- **`convenciones-y-casos.md`** — Convenciones de transcripción del libro al JSON (sílaba tónica subrayada hasta U3, patrón "primer ítem resuelto", textos de lectura, diálogos con marcadores, sopas de letras), ejemplos canónicos de `items_libro` por tipo de actividad, ejemplos INCORRECTOS, ejemplo JSON de unidad atípica U0, casebook de extracciones reales, política de mejora continua.

Y un cuarto archivo, no en esta carpeta:

- **`scripts/validar_inventario.py`** — Validador estructural ejecutable. Contrato paralelo del schema; no debe divergir.

---

## Pasos de la extracción

1. Leer todas las páginas del PDF (`unidades/UX/fuente/UX-nc1.pdf`). Las unidades regulares tienen ~10 páginas; **las unidades introductorias atípicas son más cortas** (U0 "Punto de partida" tiene 4 páginas).
2. Identificar el rango de páginas del libro (ej: 34-43), título, nivel.
3. Identificar las **secciones del índice de contenidos**:
   - **Caso normal** (U1-U9): 5 secciones canónicas — vocabulario, gramática, comunicación, destrezas, cultura.
   - **Caso atípico** (U0 y otras unidades introductorias): el índice no sigue las 5 secciones canónicas. Aplicar `reglas-operativas.md` §7 (unidades atípicas) antes de continuar.
4. Para cada página: identificar la sección, las actividades (numeradas o identificadas como tales — ver `reglas-operativas.md` §1 precedencia), los cuadros (con `tipo_cuadro`, ver `reglas-operativas.md` §3) y las notas "Observa" si las hay (`reglas-operativas.md` §4).
5. Para cada actividad: extraer todos los campos del esquema (ver `schema-inventario.md` §3). Cada actividad sale con los **3 ejes ortogonales obligatorios**: `tipo` (string, taxonomía de 20), `destreza` (lista de valores MCER, orden alfabético, sin duplicados — schema §5b), `enfoque` (string del enum de 6 — schema §5c). Criterios de asignación en `reglas-operativas.md` §2.3. En U0-U3, observar la convención editorial de sílaba tónica subrayada (`convenciones-y-casos.md` §1.1). Detectar el patrón "primer ítem resuelto como ejemplo" (`convenciones-y-casos.md` §1.2). Al asignar `campo_semantico`, usar siempre un canónico del canon (`campos-semanticos-canonicos.json`) — si no hay canónico seguro, escribir literalmente `"_pendiente_canon"` (no inventar nombres, ver `reglas-operativas.md` §5.6).
6. Construir `vocabulario_consolidado` con los 3 bloques (criterios en `reglas-operativas.md` §5.1). **Las claves de cada bloque (`principal`/`recurrente`/`comprension`) deben ser canónicos del canon semántico** (`campos-semanticos-canonicos.json`). Aplicar el árbol de decisión de `reglas-operativas.md` §5.6: si un contenido no encaja en ningún canónico seguro, emitirlo bajo la clave literal `"_pendiente_canon"` y escalarlo al autor antes del cierre. Nunca inventar nombres en `snake_case`.
7. Construir el índice top-level `secciones` (`reglas-operativas.md` §5.2).
8. Si la unidad tiene bloque de autoevaluación al pie de la última página, capturarlo como campo top-level `autoevaluacion` (`reglas-operativas.md` §6).
9. Validar JSON (ver "Cierre y validación" abajo).
10. Escribir a `unidades/UX/UX-nc1-inventario.json`.
11. Avisar al autor para validación visual de 2-3 páginas al azar.

---

## Cierre y validación

> **Convención de comandos:** todos los comandos en esta sección son **root-relative** — se ejecutan desde la raíz del repo, no desde la carpeta de fase.

Antes de dar el JSON por bueno, comprobar manualmente y con el validador.

### Comprobaciones manuales

1. **Esquema:** todas las claves obligatorias presentes (10 top-level + por página + por actividad). Ver `schema-inventario.md` §1-4.
2. **IDs únicos:** ningún `id` de actividad repetido.
3. **Tipos válidos:** todos los `tipo` de la taxonomía cerrada (20 valores). Ver `schema-inventario.md` §5.
4. **Destrezas válidas:** `destreza` es lista, valores del enum cerrado de 6 (schema §5b), orden alfabético, sin duplicados, mínimo 1 elemento — en cada actividad.
5. **Enfoque válido:** `enfoque` es string del enum cerrado de 6 (schema §5c) — en cada actividad.
6. **Secciones:** valor de `seccion` en cada página es una de las 7 claves normalizadas.
7. **`respuestas` siempre presente** en cada actividad (lista, aunque vacía).
8. **`audio`/`imagen`/`video` siempre presentes** como sub-objetos.
9. **`items_libro` o equivalente** en toda actividad de completar/elegir/relacionar.
10. **`descripcion` de imagen** obligatoria si `imagen.presente=true`.
11. **`datos.ejemplo_libro` no duplicado en `respuestas`** — el ejemplo del libro va solo en `datos.ejemplo_libro`, nunca como ítem de `respuestas`. Ver `convenciones-y-casos.md` §1.6.
12. **Cardinalidad literal de `items_libro`** — el número de ítems debe coincidir exactamente con los del PDF. No inventar ni completar la serie. Ver `reglas-operativas.md` §5.7.
13. **`campo_semantico` y claves de `vocabulario_consolidado` son canónicos** — todos los nombres usados existen en `fases/1-extraccion-inventario/campos-semanticos-canonicos.json` o son aliases conocidos. Ver `reglas-operativas.md` §5.6.
14. **Cero marcas `_pendiente_canon` en el JSON final** — esa marca es estado transitorio de worktree y bloquea cierre. Antes de declarar el inventario listo, resolver cada marca aplicando el árbol de decisión de §5.6 (vía Claude Code) y reemplazarla por el canónico correspondiente.
15. **JSON parseable** (validar con Python: `json.loads(open(...).read())`).

### Validador automático

```bash
python3 scripts/validar_inventario.py X
```

Esperado: 0 errores y 0 avisos. Si la unidad es atípica con `_nota_unidad_atipica`, 1 aviso intencional es aceptable.

El validador puede emitir un tercer bloque informativo de **auditoría legacy** durante el rollout R1 del canon semántico (`reglas-operativas.md` §5.6). Ese contador no bloquea el cierre — refleja deuda histórica de unidades pre-canon. Para unidades nuevas o re-extracciones explícitas, cualquier campo no canónico produce error duro.

### Salida

Escribir el JSON en `unidades/UX/UX-nc1-inventario.json`. Si la carpeta `unidades/UX/` no existe, crearla. Si `unidades/UX/fuente/` no contiene el PDF, abortar y avisar al autor.
