# Fase 1 — Extracción de inventario

> Auto-cargado por Claude Code cuando se trabaja dentro de `fases/1-extraccion-inventario/` o cuando el autor lo invoca explícitamente.
>
> Este CLAUDE.md + `prompt.md` constituyen el contexto operativo de esta fase. **Cuando esta fase se convierta en un agente CrewAI**, ambos archivos formarán su system prompt.

---

## Objetivo de la fase

Convertir el PDF del libro de una unidad en un JSON estructurado (`UX-nc1-inventario.json`) que captura toda la información editorial necesaria para las fases siguientes.

---

## Inputs y outputs

**Input:**
- `unidades/UX/fuente/UX-nc1.pdf` — PDF del libro del alumno con texto embebido (lo aporta el autor; gitignored).

**Output:**
- `unidades/UX/UX-nc1-inventario.json` — inventario estructurado siguiendo el esquema canónico definido en `prompt.md`.

---

## Cómo se invoca

El autor abre chat con Claude Code y dice:

> **Extrae el inventario de UX siguiendo `fases/1-extraccion-inventario/CLAUDE.md` y `fases/1-extraccion-inventario/prompt.md`.**

(Si ya estás trabajando dentro de `fases/1-extraccion-inventario/`, este CLAUDE.md ya está auto-cargado y basta con citar el prompt.)

Claude Code:
1. Lee `prompt.md` (instrucciones detalladas + esquema + taxonomía + casos resueltos).
2. Lee el PDF de `unidades/UX/fuente/UX-nc1.pdf`.
3. Genera el JSON aplicando todas las reglas del prompt.
4. Escribe a `unidades/UX/UX-nc1-inventario.json`.

---

## Validación post-extracción

Después de generar el JSON, ejecutar:

```bash
python3 scripts/validar_inventario.py X
```

Si falla, corregir antes de seguir.

Después, validación visual: el autor abre el dashboard (`python3 diagrama.py` → `http://localhost:8080` → Inventarios) y revisa 2-3 páginas al azar contrastando con el PDF.

---

## Reglas operativas críticas (resumen — detalle en `prompt.md`)

> **Error detectado en extracción real:** confundir el contenido de "Para aprender" con `cuadros_gramaticales`.
> - **"Para aprender"** → es una **actividad** (tipo `produccion_escrita_libre`, datos.subtipo `para_aprender`), no un cuadro gramatical.
> - **"Observa"** → NO es una actividad independiente. Es una **nota** que acompaña a otra actividad o cuadro; se captura en `datos._nota`. Aunque "Observa" es un imperativo, no debe tratarse como actividad: carece de número de actividad y no pide producción del alumno.
> Ver detalle completo y precedencia en `prompt.md` → "Reglas para cuadros gramaticales".

1. **Texto verbatim del libro.** El JSON debe contener el contenido de cada actividad **exactamente como aparece en el libro**. Para cloze, huecos como `_____`. Para textos, completos. Para diálogos, con marcadores `[1]`, `[2]`. **Nunca** poner solo respuestas como sustituto del enunciado.
2. **Taxonomía cerrada de tipos.** 17 valores posibles en `tipo`. Cualquier otro valor falla la validación. Lista en `prompt.md`.
3. **`respuestas` siempre presente** como lista (vacía si no aplica).
4. **`audio`/`imagen`/`video` siempre presentes** como sub-objetos con `presente: bool`.
5. **`imagen.descripcion` obligatoria** cuando `imagen.presente=true`.
6. **`vocabulario_consolidado`** con 3 bloques: `principal`, `recurrente`, `comprension`.
7. **`secciones`** como índice top-level con 7 claves normalizadas (vocabulario, gramatica, comunicacion, destrezas, cultura, evaluacion, reflexion).

---

## Coste estimado

~25-30k tokens por unidad (10 páginas + esquema + JSON resultante).
Una sola vez por unidad. Para las 9 unidades del curso: ~225-270k tokens.

---

## Mejora continua

Cuando aparezca un caso no contemplado en `prompt.md`:

1. El autor lo señala.
2. Se añade el caso/regla a `prompt.md` (en "Casos resueltos en U3" o creando una sección nueva).
3. La siguiente extracción ya lo cubre sin volver a fallar.

`prompt.md` es una fuente viva. Cada error documentado mejora el sistema.

---

## Contexto futuro (cuando esta fase sea un agente CrewAI)

- Este `CLAUDE.md` + `prompt.md` se cargan como system prompt del agente.
- El agente recibe la unidad `X` como parámetro de tarea.
- El agente devuelve el JSON.
- Las reglas de oro siguen siendo no negociables.

---

## Documentos relacionados

- `prompt.md` (en esta carpeta) — instrucciones operativas detalladas + esquema completo + casos resueltos.
- `../../CLAUDE.md` (raíz) — contexto global del proyecto y reglas de oro globales.
- `../../scripts/validar_inventario.py` — validador estructural del JSON.
- `../../PROCESO-MAESTRO.md` — decisiones acumuladas.
