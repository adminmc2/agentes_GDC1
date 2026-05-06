# Propuesta de refactorización documental — Fase 1 (Extracción de inventario)

> **Estado:** propuesta a revisar antes de ejecutar. Nada se ha tocado todavía.
> **Origen:** dictamen del revisor sobre la arquitectura documental + verificación cuantitativa del estado actual + segunda ronda de revisión incorporada (split por capa, no por campo).
> **Audiencia:** revisor + autor (decidir) + ejecutor (Claude Code, con instrucciones explícitas de no tocar nada hasta aprobación).

---

## 1. Diagnóstico

`fases/1-extraccion-inventario/prompt.md` está acumulando funciones que deberían vivir en archivos distintos. No es un problema de longitud; es un problema de **mezcla de capas**: prompt de ejecución, especificación de schema, casebook de errores, manual de mantenimiento y bitácora histórica conviven en un único artefacto.

### Estado medido (no opinión)

| Archivo | Líneas | Secciones top-level |
|---|---|---|
| `fases/1-extraccion-inventario/prompt.md` | **547** | **34** |
| `fases/1-extraccion-inventario/CLAUDE.md` | 111 | 7 |

`prompt.md` actualmente lleva en una sola pieza:
- Regla de oro
- Pasos operativos de la extracción
- Schema canónico (10 claves top-level)
- Schema por página, por actividad, por cuadro
- Schema del bloque de autoevaluación
- Taxonomía cerrada de 17 tipos de actividad
- 10 bloques de reglas semánticas (`vocabulario_consolidado`, `secciones`, `respuestas`, `audio/imagen/video`, `campo_semantico`, `items_libro`, etc.)
- 3 bloques de convenciones de transcripción (textos de lectura, diálogos, sopas de letras)
- Reglas para unidades atípicas (U0)
- Convención de sílaba tónica subrayada hasta U3
- Patrón "primer ítem resuelto como ejemplo"
- Reglas para cuadros + tipo_cuadro + qué NO es cuadro
- Sección de validación post-extracción
- Casos resueltos históricos
- Coste estimado
- Política de mejora continua

Son **siete artefactos disfrazados de uno**.

### Síntomas concretos del diagnóstico

1. **Orden de reglas malo para un modelo literal.** Se le pide decidir actividad/cuadro/nota muy pronto, pero la precedencia que evita errores aparece mucho después.
2. **Duplicación entre `CLAUDE.md` (fase) y `prompt.md`.** Reglas críticas aparecen en ambos con redacción ligeramente distinta. Sin fuente de verdad única.
3. **Mezcla de normas cerradas con cosas abiertas o pendientes.** Lo abierto contamina la adherencia a lo cerrado.
4. **Excepciones y casos especiales incrustados en el flujo principal**, en vez de estar separados como conocimiento auxiliar.
5. **Carga contextual excesiva en cada invocación.** El modelo recibe todo cada vez aunque solo necesite parte.

### Caso real registrado en esta misma conversación

Al renombrar la sección "Reglas para cuadros gramaticales" → "Reglas para cuadros" en `prompt.md`, la referencia interna del paso 4 quedó vieja (apuntaba al título antiguo). Esto es exactamente el síntoma de no tener single source of truth: cuando una regla aparece en dos sitios y solo se actualiza uno, las contradicciones aparecen sin que nadie las vea.

---

## 2. Por qué Anthropic respalda esta separación

Tres puntos concretos de la documentación de Anthropic / Claude Code que aplican directamente:

### 2.1. CLAUDE.md auto-cargado debe ser conciso

En este proyecto ya se aplicó al CLAUDE.md raíz (ver bitácora `REVIEW.md`, 18:30 de 2026-05-05: *"CLAUDE.md raíz reducido a 85 líneas (Anthropic best practices)"*). El CLAUDE.md de la fase tiene 111 líneas y duplica reglas que ya están en `prompt.md`. Es exactamente el anti-patrón que se corrigió a nivel raíz, replicado a nivel de fase.

### 2.2. Skills (`.claude/skills/<nombre>/SKILL.md`) están diseñadas para workflows especializados que no deben cargarse persistentemente

Cita literal de la docs de Claude Code: *"skills encapsulate domain knowledge as on-demand instructions"*. La extracción de inventario es un workflow concreto, no contexto que deba pesar en cada sesión. Pero con 9 ejecuciones en NC1, el coste de mantener una skill no compensa frente al beneficio. **Skill queda fuera de v1.**

### 2.3. Best practices: be explicit + separate concerns

Un prompt monolítico mezcla "qué hacer" (acción) con "qué es" (schema) con "qué decidir" (clasificación) con "cómo escribir" (convenciones). El modelo tiene que reconstruir la jerarquía sobre la marcha en cada ejecución; eso degrada adherencia.

A esto se suma el principio de ingeniería **single source of truth**: hoy una regla puede estar en `CLAUDE.md`, en `prompt.md` y en `PROCESO-MAESTRO.md` con redacción ligeramente distinta. Cuando se modifica una y no las otras, aparecen contradicciones.

---

## 3. Arquitectura documental propuesta — 5 archivos en v1

Cada archivo tiene **una sola responsabilidad**, estable, fácilmente cargable según el momento de trabajo. Cinco archivos en la primera iteración. Si tras v1 alguno crece o se mezcla, se separa entonces, no antes.

### 3.1. `CLAUDE.md` — contrato de fase

**Responsabilidad:** capa estable y breve que se auto-carga al trabajar en la fase.

**Contiene:**
- Qué produce esta fase.
- Dónde están input y output.
- Cómo validar.
- 4-5 reglas críticas que deben sobrevivir siempre.
- Tabla de "para X, ver archivo Y" (mapa de navegación).

**No contiene:**
- Reexplicación detallada del schema.
- Ejemplos extensos.
- Reglas ya desarrolladas en el prompt.
- Casuística histórica.

**Norte de tamaño:** 40-60 líneas. No es gate; si el contenido limpio requiere más y sigue siendo claro, se acepta.

---

### 3.2. `prompt.md` — prompt core de ejecución

**Responsabilidad:** instrucción ejecutable cuando alguien dice "extrae UX siguiendo este prompt".

**Contiene:**
- Objetivo de la tarea.
- Input y output exactos.
- Definición de éxito.
- Pasos secuenciales mínimos.
- **Referencia al orden de decisión:** cuando haya que clasificar elementos del libro, aplicar la precedencia definida en `reglas-operativas.md`. El prompt core **no reexplica precedencias; las invoca**.
- Sección **"Cierre y validación"** (lo que antes era "Validación post-extracción", absorbido aquí).
- Referencias breves al resto de artefactos cuando hagan falta.

**No contiene:**
- Historia de errores anteriores.
- Coste estimado.
- Mantenimiento del sistema.
- Discusión futura sobre CrewAI.
- Ejemplos marginales que no afecten a la decisión principal.
- Explicaciones largas del schema (viven en `schema-inventario.md`).

**Norte de tamaño:** 80-120 líneas. No es gate.

---

### 3.3. `schema-inventario.md` — contrato de datos puro

**Responsabilidad:** definir la **forma** del JSON. Solo estructura, tipos, obligatoriedad y restricciones validables sin contexto editorial.

**Contiene:**
- Schema top-level (10 claves obligatorias + 1 opcional) con tipos.
- Schema por página, por actividad, por cuadro, por autoevaluación: **forma**.
- Enumeración cerrada de los 17 tipos de actividad (los valores válidos, no cuándo usarlos).
- Enumeración cerrada de los 5 valores de `tipo_cuadro`.
- Restricciones de tipos (int/str/bool/list-of-str).
- Restricciones condicionales validables mecánicamente (ej. `imagen.descripcion` obligatoria si `imagen.presente == true`).
- Política de extensibilidad de `datos`.
- **Claves opcionales contractuales:**
  - `autoevaluacion`: presente cuando la unidad tiene bloque de cierre (todas excepto atípicas).
  - `_nota_unidad_atipica`: str, presente solo en unidades atípicas (ej. U0). **Tratamiento estricto:** es contractual, no "tolerada-no-canónica". El validador debe reconocerla como opcional sin emitir aviso. El estado actual del validador (ver `validar_inventario.py:CLAVES_TOP_OPCIONALES`) **no la incluye**, por lo que U0 produce un aviso espurio. Esta divergencia entra como hallazgo obligatorio del paso 5.5 y se resuelve antes del merge alineando el validador en commit aparte.

**No contiene:**
- Cuándo aplica cada campo (decisión).
- Cómo elegir el valor (decisión editorial).
- Reglas de población semántica (qué cuenta como `principal` vs `recurrente` vs `comprension`).
- Workflow de extracción.
- Ejemplos pedagógicos.
- Casos históricos.

**Source-of-truth con el validador:** `schema-inventario.md` y `scripts/validar_inventario.py` son contratos paralelos del mismo shape. No pueden divergir sin revisión cruzada explícita (ver sección 8 — scope).

---

### 3.4. `reglas-operativas.md` — decisión, clasificación, población y unidades atípicas

**Responsabilidad:** guía de decisión compacta y priorizada. Reúne lo que el modelo necesita decidir durante la extracción: qué tipo asignar, qué clasificar como cuadro/actividad/nota, cómo poblar campos cuyo shape ya está fijado en el schema.

Este es probablemente el artefacto más importante después del prompt core, porque los errores reales no vienen del schema sino de la clasificación.

**Contiene:**
- **Precedencia** entre actividad / cuadro / nota / autoevaluación.
- "Para aprender" → actividad.
- "Observa" → nota; cuándo va en `datos._nota`, cuándo en `cuadro.observaciones`.
- Cómo asignar `tipo_cuadro` (qué cuenta como gramatical / lexical / fonetico / cultural / comunicativo).
- Distinción `completa_huecos` vs `produccion_escrita_guiada`.
- Reglas de población de cada campo cuyo shape vive en `schema-inventario.md`:
  - Cuándo `respuestas` lleva contenido y qué formato.
  - Cuándo `campo_semantico` aplica.
  - Distribución de vocabulario entre `principal` / `recurrente` / `comprension`.
  - Cómo construir el índice `secciones` (mapeo página↔sección, IDs de actividad).
  - Cuándo asignar cada uno de los 17 tipos de actividad.
  - Cuándo marcar `audio/imagen/video.presente=true`.
- **Unidades atípicas:** definición, reglas específicas, cuándo añadir `_nota_unidad_atipica`, qué hacer con secciones vacías.
- Reglas de literalidad de `datos.items_libro` (texto exacto del libro, huecos como `_____`).

**No contiene:**
- Forma del JSON (vive en schema).
- Convenciones de transcripción específicas (sílaba tónica, "primer ítem resuelto") — viven en `convenciones-y-casos.md`.
- Casos históricos resueltos — viven en `convenciones-y-casos.md`.

**Single source of truth de precedencias:** las reglas de precedencia (qué clasificar como actividad / cuadro / nota / autoevaluación, en qué orden, con qué excepciones) viven **exclusivamente aquí**. Cualquier otro archivo que necesite invocarlas lo hace por referencia, no por copia. Si una precedencia aparece reescrita en `prompt.md`, `CLAUDE.md` o cualquier otro artefacto, es un bug del refactor.

---

### 3.5. `convenciones-y-casos.md` — transcripción + casebook

**Responsabilidad:** convenciones de transcripción del libro al JSON + memoria editorial de casos resueltos en extracciones reales.

**Contiene:**
- Sílaba tónica subrayada hasta U3 + cómo se representa en JSON.
- Patrón "primer ítem resuelto como ejemplo".
- Reglas para textos de lectura.
- Reglas para diálogos (marcadores `[1]`, `[2]`).
- Reglas para sopas de letras y juegos.
- Ejemplos correctos e incorrectos de `items_libro`.
- Casos históricos resueltos (errores reales encontrados + corrección adoptada + precedencia fijada).
- Política de mejora continua del prompt.

**No contiene:**
- Reglas estables de clasificación (viven en `reglas-operativas.md`).
- Schema (vive en `schema-inventario.md`).

**Nota de mantenimiento:** este archivo mezcla deliberadamente convenciones estables con casebook append-only. En v1 caben juntos sin perjudicar la navegación. Si en el futuro el casebook crece y empieza a competir con las convenciones por visibilidad, se separan entonces.

---

### Skill (`.claude/skills/...`) — fuera del alcance de v1

Razón: la fase se ejecuta ~9 veces (una por unidad NC1). El coste de mantener una skill no compensa frente al beneficio en una única curva de uso. Reabrir solo si tras v1 se observa un patrón de uso repetido que justifique la encapsulación.

---

## 4. Mapeo previo — sección actual de `prompt.md` → archivo destino

El criterio de mapeo es **por capa, no por campo**. Para cada regla actual, se decide:
- **Estructural** (forma del JSON, tipos, obligatoriedad, restricciones validables sin contexto) → `schema-inventario.md`
- **Decisional / población** (cuándo aplica, cómo elegir el valor, criterio editorial) → `reglas-operativas.md`
- **Convenciones de transcripción** (cómo escribir contenido del libro) → `convenciones-y-casos.md`
- **Casos históricos** → `convenciones-y-casos.md`

Muchas filas se parten en dos destinos (capa estructural + capa decisional). Es el comportamiento deseado: el split por capa es lo que evita reconstruir el monolito con piel nueva.

| Líneas | Sección actual de `prompt.md` | Destino |
|---|---|---|
| 10-26 | Regla de oro | `prompt.md` core |
| 27-43 | Pasos de la extracción | `prompt.md` core |
| 44-84 | Esquema canónico (10+1 claves top-level) | `schema-inventario.md` |
| 85-97 | Esquema por página | `schema-inventario.md` |
| 98-145 | Esquema por actividad (forma) | `schema-inventario.md` |
| 146-171 | Esquema por cuadro (forma + enum 5 valores) | `schema-inventario.md` |
| 172-185 | Autoevaluación (forma) | `schema-inventario.md` |
| 186-200 | Autoevaluación (precedencia, cuándo se omite) | `reglas-operativas.md` |
| 201-233 | Taxonomía 17 tipos | enum → `schema-inventario.md` · cuándo cada uno → `reglas-operativas.md` |
| 234-251 | `vocabulario_consolidado` | forma (3 bloques) → `schema-inventario.md` · qué cuenta como cada bloque → `reglas-operativas.md` |
| 252-261 | `secciones` (top-level) | forma → `schema-inventario.md` · construcción del índice → `reglas-operativas.md` |
| 262-269 | `seccion` por página | enum → `schema-inventario.md` · cómo determinar la sección → `reglas-operativas.md` |
| 270-281 | `respuestas` | siempre presente, lista → `schema-inventario.md` · contenido y formato → `reglas-operativas.md` |
| 282-300 | `audio` / `imagen` / `video` | forma + condicional `imagen.descripcion` → `schema-inventario.md` · cuándo marcar `presente=true` → `reglas-operativas.md` |
| 301-308 | `campo_semantico` | str opcional → `schema-inventario.md` · cuándo aplica + cómo elegir → `reglas-operativas.md` |
| 309-312 | `datos.items_libro` (regla) | lista de strings en `datos` → `schema-inventario.md` · literalidad obligatoria + huecos → `reglas-operativas.md` |
| 313-339 | Ejemplos correctos `items_libro` | `convenciones-y-casos.md` |
| 340-354 | Ejemplos incorrectos `items_libro` | `convenciones-y-casos.md` |
| 355-360 | Reglas para textos de lectura | `convenciones-y-casos.md` |
| 361-376 | Reglas para diálogos | `convenciones-y-casos.md` |
| 377-394 | Reglas para sopas de letras y juegos | `convenciones-y-casos.md` |
| 395-411 | Reglas para unidades atípicas | `reglas-operativas.md` |
| 412-427 | Sílaba tónica subrayada hasta U3 | `convenciones-y-casos.md` |
| 428-443 | Patrón "primer ítem resuelto como ejemplo" | `convenciones-y-casos.md` |
| 444-489 | Reglas para cuadros (`tipo_cuadro`, qué NO es cuadro) | enum 5 valores → `schema-inventario.md` · precedencia + cómo asignar → `reglas-operativas.md` |
| 490-507 | Validación post-extracción | `prompt.md` core (sección "Cierre y validación") |
| 508-515 | Salida | `prompt.md` core |
| 516-531 | Casos resueltos en extracción real (U3) | `convenciones-y-casos.md` |
| 532-538 | Coste estimado | eliminar (no añade valor operativo) |
| 539-547 | Política de mejora continua | `convenciones-y-casos.md` (intro) |

**Regla del mapeo:** ninguna línea de contenido editorial actual desaparece. Cada una tiene un destino — y muchas se parten en dos destinos (capa estructural + capa decisional). El refactor mueve y separa por capa, no inventa ni borra.

---

## 5. Plan de ejecución paso a paso

### Paso 0 — Congelar la base y trabajar en rama
- Crear tag git `pre-refactor-prompt-fase1` sobre HEAD actual (marcador inmutable).
- Crear rama `refactor/prompt-fase-1` y trabajar en ella.
- `main` queda intacto durante el refactor; sigue funcionando con el `prompt.md` actual.
- **Si rollback:** `git checkout main` (sin reset destructivo). Opcionalmente `git branch -D refactor/prompt-fase-1` si la rama se descarta.
- **Razón de no normalizar `git reset --hard`:** este repo tiene carriles paralelos (`unidades/U2/`, `viejo/_template/`) sin trackear. Un reset destructivo sobre main podría afectarlos sin que sea evidente.
- **Verificación:** `git tag` muestra el tag; `git branch` muestra la rama; `main` y la rama divergen solo en commits del refactor.

### Paso 1 — Crear los archivos vacíos con sus headers
- Crear `schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md` con solo `# Título` y un comentario de responsabilidad (copiado del bloque "Responsabilidad" de la sección 3 correspondiente).
- **Verificación:** los 3 archivos existen, identidad clara, ningún contenido movido todavía.

### Paso 2 — Migrar contenido por archivo, aplicando split por capa
- Por cada fila del mapeo (sección 4), copiar la sección al archivo destino. Cuando la fila se parte en dos destinos (estructural + decisional), marcar **explícitamente** en cada destino qué parte le corresponde.
- En `prompt.md` dejar **placeholders con enlace** *("Schema: ver `schema-inventario.md`")* para que no quede roto durante el proceso.
- **Verificación tras cada archivo (semántica, no por conteo):**
  - Marcar la fila correspondiente en el mapeo de la sección 4 como hecha (checklist).
  - **Búsqueda de anclas semánticas:** identificar 2-3 frases canónicas únicas por sección antes de moverla (ej. "principio de género no marcado", "literalidad del contenido visible al alumno"). Después del movimiento, `grep` cada ancla: debe aparecer en exactamente un archivo nuevo.
- `wc -l` queda como sanity check informal, **no como gate**.

### Paso 3 — Reescribir `prompt.md` core desde cero
- Una vez todo el contenido editorial está en sus archivos destino, **borrar `prompt.md` y reescribirlo** con la estructura mínima:
  - Objetivo
  - Input/output
  - Definición de éxito
  - Pasos secuenciales (con referencias *cortas* a los demás archivos cuando hagan falta)
  - **Sección "Cierre y validación"** (la antigua "Validación post-extracción" absorbida aquí).
- **Norte de tamaño:** 80-120 líneas. No es gate.
- **Verificación:** comparar prompt.md nuevo vs lista de pasos del flujo. Sin desviaciones.

### Paso 4 — Reescribir `CLAUDE.md` de fase en modo contrato
- Reducir a contrato corto:
  - Qué produce esta fase
  - Dónde están input y output
  - Las **4-5 reglas críticas** que sobreviven siempre (no las repetidas del prompt; solo las que un humano debe recordar al trabajar en esta fase)
  - Tabla de "para X, ver archivo Y"
- **Norte de tamaño:** 40-60 líneas. No es gate.
- **Verificación:** sin reglas duplicadas con `prompt.md`. Grep cruzado de frases largas.

### Paso 5 — Prueba empírica de reextracción
**No es simulacro mental.** Es ejecución real, controlada y comparable. La selección debe cubrir las reglas que el refactor *acaba de mover*, no solo las páginas más complejas (sesgo "test-where-the-light-is").

- **Selección obligatoria — 3 casos:**
  1. **Una página rica:** U3-p36 (cuadros gramaticales + actividades de varios tipos + ejemplos resueltos) **o** U1-p20 (cuadros culturales + comunicativos + diferentes registros). Cubre clasificación general y `tipo_cuadro`.
  2. **U0 completa** (no una página suelta — la unidad atípica entera). Cubre las reglas de unidades atípicas y `_nota_unidad_atipica` que se acaban de mover a `reglas-operativas.md`. **U0 también cubre el caso "autoevaluación ausente"** (atípica sin bloque).
  3. **U1-p21** (cierre de unidad con bloque `autoevaluacion` presente). Cubre la regla de autoevaluación top-level y su precedencia, también recién movidas.
- **Procedimiento:**
  - Abrir sesión limpia de Claude Code.
  - Reextraer cada caso siguiendo **solo** los nuevos artefactos (`CLAUDE.md`, `prompt.md` core, `schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md`). El prompt viejo no se consulta.
- **Verificación — oráculo de regresión (estado de cierre / pre-merge):**
  - **Oráculo único para los tres casos: 0 errores y 0 avisos** en `python3 scripts/validar_inventario.py X`.
  - **Implicación para U0:** alcanzar 0 avisos requiere que el validador reconozca `_nota_unidad_atipica` como opcional contractual (ver sec. 3.3). El estado actual del validador trata esa clave como no-canónica y produce un aviso. **Esa divergencia es exactamente lo que el paso 5.5 está obligado a detectar y a resolver alineando el validador en commit aparte antes del merge.** El oráculo "0/0" se refiere al estado final pre-merge, no al estado durante la ejecución del paso 5 si todavía no se ha alineado el validador.
  - **Diff vs el JSON existente:** ninguna decisión semántica cerrada se pierde (tipo de actividad, `tipo_cuadro`, contenido literal de `items_libro`, presencia/ausencia de `_nota`, presencia/ausencia y contenido de `autoevaluacion`, presencia de `_nota_unidad_atipica`, etc.).
  - Cualquier divergencia (validador o diff semántico) → **indica laguna en algún artefacto**. Se corrige antes de mergear a `main`.
- **Coste estimado:** ~10-12k tokens en total (página rica ~3-4k + U0 ~5-6k + U1-p21 ~2-3k). Aceptable.

### Paso 5.5 — Cross-check `schema-inventario.md` ↔ `validar_inventario.py`

La afirmación "contratos paralelos del mismo shape" (secciones 3.3 y 8) requiere un control operativo, no solo una regla escrita. Sin este paso, una deriva preexistente entre prompt viejo y validador se copia silenciosamente al nuevo schema.

- **Procedimiento:** recorrer `schema-inventario.md` campo por campo y contrastar contra `scripts/validar_inventario.py`:
  - Para cada clave declarada **obligatoria** en el schema → verificar que el validador la chequea como obligatoria.
  - Para cada **enumeración cerrada** (17 tipos de actividad, 5 valores de `tipo_cuadro`, 7 secciones canónicas, 3 opciones canónicas de autoevaluación NC1) → verificar que el validador rechaza valores fuera de la enum.
  - Para cada **restricción condicional** (ej. `imagen.descripcion` obligatoria si `imagen.presente=true`, `autoevaluacion` con valores fijos NC1 cuando `curso=="nc1"`) → verificar que el validador la aplica.
  - Para cada **clave opcional** declarada (`autoevaluacion`, `_nota_unidad_atipica`) → verificar que el validador no la exige y la valida si está.
- **Producir un acta corta:** "X campos chequeados, Y divergencias detectadas".
- **Si Y > 0: no se mergea mientras haya divergencia real**, sin excepciones. La regla "schema y validador no pueden divergir" (sec. 3.3 + sec. 8) es estricta y se cumple en el momento del cierre. La divergencia se resuelve por una de dos vías antes del merge:
  1. **Corregir el schema documental** si la divergencia se debe a error de copia desde el prompt viejo.
  2. **Corregir el validador** en commit aparte, fuera del scope nominal de este refactor, *antes* de mergear el refactor a `main`. (Es decir: el refactor se mergea con el validador ya alineado, aunque el ajuste del validador sea técnicamente un commit distinto.)
- **No es opción aceptar la divergencia como estado válido de cierre.** Registrar la deuda como issue o nota es complementario, no sustitutivo: el estado "schema y validador divergen" no convive con el merge.
- **El paso 5.5 es solo de detección.** La modificación del validador, si hace falta, ocurre en commit aparte antes del merge — no se hace dentro de este refactor.

### Paso 6 — Sincronizar CHANGELOG, REVIEW, PROCESO-MAESTRO y mergear
- Una sola entrada vN.M en CHANGELOG documentando el refactor con el mapeo de la sección 4.
- PROCESO-MAESTRO: actualizar el listado de archivos por fase.
- REVIEW: bitácora.
- Merge `refactor/prompt-fase-1` → `main` solo cuando **todos los pasos previos están cumplidos sin excepciones: 0, 1, 2, 3, 4, 5 y 5.5**. El paso 5.5 (cross-check schema ↔ validador) es **gate obligatorio**, igual que el resto. Si el paso 5.5 detecta divergencia, el validador se alinea en commit aparte antes del merge (es la consecuencia operativa de la regla "schema y validador no pueden divergir", no una excepción).

---

## 6. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Pérdida silenciosa de contenido en la migración | Mapeo explícito como checklist + búsqueda de anclas semánticas + prueba empírica del paso 5 |
| Contradicciones entre archivos nuevos | Single source of truth: cada regla solo en su capa (forma o decisión). `CLAUDE.md` y `prompt.md` *referencian*, no copian |
| Inconsistencia transitoria (medio prompt nuevo, medio viejo) | Refactor en rama; `main` sigue funcionando con el prompt actual hasta que el merge esté limpio |
| Inventarios ya generados (U0/U1/U3) podrían no encajar con un schema reinterpretado | El paso 5 (prueba empírica) los toma como caso de regresión. Si el nuevo schema dice algo distinto del JSON validado, hay un error en el refactor |
| Sesgo del ejecutor a "rellenar" archivos nuevos | Los archivos destino se llenan **copiando** secciones del prompt actual, no reescribiéndolas. El refactor no es excusa para reabrir decisiones cerradas |
| Esquema documental se desincroniza del validador | Regla explícita de scope: `schema-inventario.md` y `scripts/validar_inventario.py` no pueden divergir sin revisión cruzada (ver sección 8). **Paso 5.5 lo convierte en control operativo** antes del merge, no solo regla escrita |
| Deriva preexistente entre prompt viejo y validador se copia silenciosamente al nuevo schema | Paso 5.5 (cross-check schema ↔ validador campo por campo) detecta divergencias antes del merge. **No se mergea con divergencia activa**: o se corrige el schema, o se ajusta el validador en commit aparte antes del merge. Aceptar la divergencia como cierre no es opción |
| Reaparición de duplicación de precedencias en formato pequeño (prompt + reglas-operativas restablecen la misma precedencia) | Single source of truth explícito en sección 3.4: las precedencias viven solo en `reglas-operativas.md`. El prompt core invoca por referencia, no copia. Verificable con grep cruzado en paso 4 |

---

## 7. Decisiones del autor antes de ejecutar

1. **¿Empezamos por el paso 0 (tag + rama de refactor)** ahora, o quieres revisar antes algún punto del documento?
2. **¿La frontera schema/reglas-operativas tal como está descrita en secciones 3.3 y 3.4** es la correcta? En particular: ¿restricciones condicionales validables mecánicamente (ej. `imagen.descripcion` obligatoria si `imagen.presente == true`) van en `schema-inventario.md`, o prefieres que vayan en `reglas-operativas.md`?
3. **¿Convenciones y casos resueltos juntos o separados?** En v1 propongo unirlos en `convenciones-y-casos.md`; si prefieres mantenerlos separados desde el principio (`convenciones-editoriales.md` + `casos-resueltos.md`), aviso y se separan.

---

## 8. Lo que NO se va a hacer en este refactor (scope explícito)

Para evitar que el refactor crezca:
- No se reabre ninguna decisión editorial cerrada (taxonomía, schema, valores fijos NC1).
- No se renombra ningún campo del JSON. El schema se mueve de archivo, no se modifica.
- No se modifican los inventarios U0, U1, U3. Solo se verifica que siguen siendo legítimamente generables con los nuevos artefactos.
- No se aborda la disciplina de cierre de commits (CHANGELOG/versión obligatorios) — frente paralelo distinto.
- **No se toca `scripts/validar_inventario.py`.** Pero queda escrita la regla de scope: `schema-inventario.md` y el validador son **contratos paralelos del mismo shape**. Cualquier cambio en uno requiere revisión cruzada del otro. Si en el futuro se detecta divergencia, se trata como bug, no como diferencia legítima.

---

## 9. Conclusión

El problema no es que `prompt.md` esté largo. Es que mezcla siete funciones distintas en un solo archivo, lo cual contradice las recomendaciones de Anthropic sobre instrucciones modulares, concisas y con separación clara de responsabilidades.

La solución correcta es separar artefactos por función — pero por **capa funcional**, no por campo del JSON, para no reconstruir el monolito con piel nueva.

**Cinco archivos en v1** (CLAUDE de fase, prompt core, schema puro, reglas operativas, convenciones-y-casos), validación empírica antes de mergear, scope explícito de no-divergencia con el validador. Esto está alineado con Anthropic y con buenas prácticas de ingeniería documental, y es verificable paso a paso, no cosmético.
