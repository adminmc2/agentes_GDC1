# Proceso Maestro — Documento de trabajo

> **Estado:** documento temporal. Consolida el proceso completo de producción de una unidad didáctica, lo que está definido y lo que falta por definir. Sirve de fuente para reorganizar el repositorio y, una vez integrada esta información en CLAUDE.md, README.md y los documentos de cada sección, **se eliminará**.
>
> **Origen:** conversación con el autor el 2026-05-05 para evitar perder el proceso completo descrito en chat.
>
> **Cómo se usa:** lectura obligada antes de cualquier reorganización del repo. Se actualiza conforme se rellenan huecos o se cierran decisiones.

> **Nota de migración (v11.13):** este documento contiene numerosas referencias a rutas `viejo/...` (material del sistema CrewAI v5 anterior y del sistema de trabajo: `viejo/agentes/`, `viejo/materiales/`, `viejo/repertorios/`, `viejo/unidades/U03/`, etc.). Tras la separación en dos repositorios, **todo ese material vive ahora en el repo B** (`temporal-antiguo-guia-ia`, en `~/Desktop/`). Las rutas `viejo/...` de este documento son **punteros históricos**: sustituir mentalmente `viejo/` → raíz de repo B. La reescritura completa de estas referencias queda pendiente de una pasada posterior dedicada a PROCESO-MAESTRO.

---

## Parte 1 — Modelo conceptual del repositorio

### Tres tipos de contenido (no mezclar)

1. **Producto editorial** — la guía, las tarjetas, los textos, las píldoras. Lo que recibe el lector final.
2. **Sistema técnico** — código Python, agentes CrewAI, dashboard, BD.
3. **Especificaciones** — los criterios y reglas que conectan a 1 y 2: cómo debe ser el producto, qué reglas siguen los agentes, qué reglas sigue Claude Code.

### Dos audiencias para las especificaciones (tipo 3)

- **Claude Code** (presente operativo) — yo, leyendo archivos `.md` en chat.
- **Agentes CrewAI** (futuro automatizado) — leyendo desde la BD (tabla `reglas_aprendidas`).

**Decisión cerrada:** fuente única. Las reglas viven una sola vez (en archivo MD) y la BD se rellena automáticamente desde ahí con un script de sincronización (`sincronizar-reglas.py`, aún no escrito). No se escribe directamente en BD.

**Nota del autor:** la BD no se puebla ahora; los agentes se configuran después. Pero el diseño actual debe pensarse ya con los agentes en mente para evitar errores futuros.

### El ciclo de aprendizaje de Claude Code

Hoy, cuando el autor corrige a Claude Code en chat, esa lección se pierde al cerrar la sesión. **Falta** un mecanismo para capturar errores y correcciones, y que las siguientes sesiones de Claude Code los respeten.

**Decisión cerrada:** las lecciones serán **específicas por sección**, no un único archivo global. Cada sección de trabajo (vocabulario, gramática, comunicación, etc.) tiene su propio archivo de lecciones porque la forma de trabajo en cada sección es distinta.

**Pendiente:** definir el formato exacto de las lecciones y el mecanismo de activación (ver Parte 4).

---

## Parte 2 — Las 8 fases del proceso de producción de una unidad

### Fase 1 — Input del PDF y creación del inventario

**Qué pasa:** el autor exporta el PDF embebido del libro de texto. Claude Code lee el PDF y extrae las actividades a un JSON estructurado (`UX-nc1-inventario.json`). El JSON se importa a BD con `scripts/importar_inventario.py`. Al cerrar la unidad se actualizan los JSONs globales del curso.

**Definido (Fase 1 — CERRADA en chat 2026-05-05):**

**Convención de naming:**
- Carpetas de unidad sin cero: `U0/`, `U1/`, `U2/`, `U3/` ... `U9/` (U0 es la unidad introductoria atípica "Punto de partida").
- Prefijo de archivo por unidad: `UX-nc1-` (donde X = número de unidad sin cero, NC1 = "Nuevo Compañeros 1"). Ejemplo: `U3-nc1-inventario.json`.
- Prefijo de archivo global del curso: `nc1-`. Ejemplo: `nc1-reciclaje.json`.
- **⚠ Restricción de la convención sin cero:** válida para cursos de exactamente 9 unidades o menos (Nuevo Compañeros 1 tiene 9). Si en el futuro se trabaja con un curso de 10+ unidades, los nombres `U10/` ordenarían **antes** que `U2/` en cualquier sistema de archivos. Para esos cursos habría que reintroducir el cero (`U01`...`U10`) o usar otro esquema (`U-1`, `U-10`). Decisión revisable cuando aplique.

**Material fuente (entrada):**
- Por ahora **solo el PDF del libro del alumno**: `unidades/UX/fuente/UX-nc1.pdf`.
- Requisito: PDF con texto embebido (no escaneado). El autor lo garantiza.
- Versionado: si el PDF se actualiza, se genera una **versión nueva** y se registra el cambio en CHANGELOG.md.
- Otras fuentes (cuaderno de ejercicios, libro del profesor original, audios) **descartadas por ahora**.

**Salidas (outputs):**

*Por unidad* (en `unidades/UX/`):
- `UX-nc1-inventario.json` — extracción del PDF de la unidad.

*Globales del curso* (en `unidades/`, junto a las carpetas de unidad):
- `nc1-reciclaje.json` — mapping de reciclaje cross-unidad. Se va completando conforme se desarrolla cada unidad.
- `nc1-tarjetas.json` — índice global de todas las tarjetas del curso. Se actualiza al cerrar cada unidad.
- `nc1-pildoras.json` — índice global de todas las píldoras del curso. Se actualiza al cerrar cada unidad.

**Modelo de los globales: A — el global es ÍNDICE / PROYECCIÓN.** El dato vive en su unidad (CSVs de tarjetas, archivos de píldoras). Un script `regenerar-globales.py` (aún no escrito) lee todas las unidades y regenera los JSONs globales. **No se editan a mano** — si se editan, se pierde al regenerar.

**Estructura física resultante:**
```
unidades/
├── nc1-reciclaje.json              ← global (regenerado)
├── nc1-tarjetas.json               ← global (regenerado)
├── nc1-pildoras.json               ← global (regenerado)
├── U3/
│   ├── U3-nc1-inventario.json
│   ├── fuente/U3-nc1.pdf
│   ├── tarjetas/...
│   ├── pildoras/...
│   └── U3-{seccion}.md (varios)
└── (U1, U2, U4-U9 con la misma estructura)
```

**Pipeline definido:**
1. Autor exporta PDF embebido → `unidades/UX/fuente/UX-nc1.pdf`.
2. **Extracción del inventario por Claude Code en chat con prompt versionado** (ver bloque "Estrategia de generación" abajo) → genera `UX-nc1-inventario.json`.
3. Validación automática del JSON con `scripts/validar_inventario.py` (operativo; alineado con `fases/1-extraccion-inventario/schema-inventario.md` hasta v10.62 — cross-check A4.5.5; tras el rediseño v10.115-117 la alineación queda transitoriamente declarada como deuda en el Apéndice §A.1 del schema, con validación manual sustitutiva mientras dure).
4. Validación visual fuente vs JSON (revisión de 2-3 páginas al azar).
5. `python scripts/importar_inventario.py unidades/UX/UX-nc1-inventario.json` → carga a BD (idempotente, DELETE CASCADE).
6. Tras desarrollar la unidad, regenerar `nc1-tarjetas.json` y `nc1-pildoras.json` con scripts Python deterministas.
7. Cierre de unidad: actualización de `nc1-reciclaje.json`. *(Histórico: en el pipeline original era manual con Claude Code en chat. Estado vigente desde v10.108d: fase 2 pausada; `integrar_unidad.py` no regenera reciclaje por defecto, requiere el flag explícito `--regenerar-reciclaje` cuando se justifique. Ver decisión 36.)*
8. Si el PDF cambia, repetir desde el paso 1 con versión nueva + entrada en CHANGELOG.

---

**Estrategia de generación de los 4 JSONs (CERRADA en chat 2026-05-05):**

**A) `UX-nc1-inventario.json` — extracción del PDF de la unidad**
- **Quién:** Claude Code en chat. NO Python autónomo (no se confía en scripts disfuncionales para PDFs irregulares).
- **Cómo:** mediante un prompt versionado en `fases/1-extraccion-inventario/prompt.md`. El prompt contiene esquema JSON exacto, reglas de extracción detalladas, casos especiales resueltos y ejemplos basados en U03.
- **Reproducibilidad:** el prompt fijo asegura resultados prácticamente idénticos entre extracciones. La varianza propia del LLM se minimiza con prompt detallado y temp=0.
- **Coste estimado:** ~25.000 tokens por unidad (10 páginas). Se hace una sola vez por unidad. Para las 9 unidades restantes: ~225.000 tokens totales.
- **Mejora continua:** cada caso raro encontrado se añade al prompt. Para la siguiente unidad, ya no es raro.

**B) `nc1-tarjetas.json` — índice global de tarjetas del curso**
- **Quién:** script Python determinista `scripts/regenerar_tarjetas_globales.py` (a escribir).
- **Cómo:** lee todos los CSVs en `unidades/U*/tarjetas/csv/*.csv` (estructura fija con cabecera conocida), agrupa por unidad y campo semántico, escribe el JSON.
- **Coste:** cero tokens.
- **Cuándo se ejecuta:** al cerrar cada unidad o cuando se modifican los CSVs.

**C) `nc1-pildoras.json` — índice global de píldoras del curso**
- **Quién:** script Python determinista `scripts/regenerar_pildoras_globales.py` (a escribir).
- **Cómo:** lista los archivos PDF en `unidades/U*/pildoras/`, parsea el TEX correspondiente para extraer el título (regex sobre `\title{...}`), escribe el JSON.
- **Coste:** cero tokens.
- **Cuándo se ejecuta:** al cerrar cada unidad.

**D) `nc1-reciclaje.json` — mapping de reciclaje cross-unidad**

> ⚠ **Modelo descrito a continuación SUPERADO.** Esta entrada se conserva como referencia histórica del modelo manual original (decisión 23). Estado vigente: ver decisión 36 (fase 2 pausada hasta cierre de canon de fase 1; `integrar_unidad.py` no regenera reciclaje por defecto desde v10.108d; flag `--regenerar-reciclaje` para forzar).

- **Quién (modelo histórico):** Claude Code en chat, ayudando al autor. **NO se generaba con script Python**, **NO se infería automáticamente, NO se "regeneraba"**.
- **Cómo (modelo histórico):** el autor abría chat al cerrar cada unidad y decía "añade los reciclajes de UX". Claude Code preguntaba qué contenido se reutiliza, lo añadía a las entradas existentes del JSON. El archivo era **acumulativo**.
- **Por qué manual (motivación original):** el reciclaje es un mapping editorial que requería criterio humano. Un script no podía inferirlo de forma fiable en aquella fase.
- **Coste:** mínimo, ~5.000 tokens por unidad.
- **Evolución:** v10.97 introdujo scripts de regeneración automatizada (mapa + auto); v10.108 pausó fase 2 y v10.108d desacopló la regeneración del flujo de integración por defecto.

---

**Validación post-generación:**
- Después de cada extracción, `scripts/validar_inventario.py` (operativo) verifica estructura: campos obligatorios, tipos, destreza (lista alfabética del enum cerrado), enfoque, códigos de actividad únicos, JSON parseable. Esto SÍ es trabajo de Python (validación estructural pura, sin riesgo de fallar).

---

---

**Esquema canónico del `UX-nc1-inventario.json` (CERRADO en chat 2026-05-05):**

Estructura top-level (10 claves obligatorias + 1 opcional):
- `unidad` (int): número de unidad, sin cero. Ej: 3.
- `curso` (str): identificador del curso. Ej: "nc1".
- `titulo` (str): título de la unidad. Ej: "La Familia".
- `paginas_libro` (str): rango de páginas en el libro. Ej: "34-43".
- `nivel` (str): nivel MCER. Ej: "A1.1".
- `fuente` (object): `{ archivo, version_extraccion }`.
- `contenidos_indice` (object): las 5 secciones canónicas — vocabulario, gramatica, comunicacion, destrezas, cultura. Texto descriptivo de cada una.
- `vocabulario_consolidado` (object): vista agregada del vocabulario de toda la unidad, organizada en **3 bloques**:
  - **`principal`** — Vocabulario declarado en el índice de la unidad. La sección Vocabulario lo trabaja explícitamente. Agrupado por campo semántico.
  - **`recurrente`** — Vocabulario que aparece en varias secciones de la unidad, no solo en la sección Vocabulario. Agrupado por categoría temática.
  - **`comprension`** — Léxico que aparece y afecta la comprensión del estudiante aunque no se trabaje explícitamente. Agrupado por categoría.
- `secciones` (object): índice top-level con 7 claves fijas (vocabulario, gramatica, comunicacion, destrezas, cultura, evaluacion, reflexion). Cada una: `{ paginas, actividades_ids }`. Mapea de sección a páginas y a IDs de actividad. Permite acceso directo sin recorrer todo.
- `autoevaluacion` (object, opcional): bloque estructural de cierre de unidad. `{ pagina, instruccion_original, opciones (3 fijas), emoticonos }`. Se omite en unidades atípicas (ej. U0). En NC1: `["MUY BUENOS", "BUENOS", "NO MUY BUENOS"]` con emoticonos.
- `paginas_detalle` (array): lista de páginas con su detalle.

Estructura por página:
- `pagina` (int).
- `seccion` (str): clave normalizada (vocabulario, gramatica, comunicacion, destrezas, cultura, evaluacion, reflexion).
- `actividades` (array).
- `cuadros` (array, opcional) — cada cuadro lleva `tipo_cuadro`: `gramatical | lexical | fonetico | cultural | comunicativo`.

**REGLA DURA — Literalidad del contenido visible al alumno.** Cada actividad debe contener el **texto exacto** que el alumno lee en el libro, no resúmenes ni referencias. La instrucción va en `instruccion_original` (literal). Todo el contenido visible adicional (frases con huecos, listas de items, opciones múltiples, diálogos completos, textos de lectura, definiciones, palabras dadas en recuadro, ejemplos del libro) va en `datos` con campos descriptivos (`items_libro`, `frases`, `dialogo_completo`, `texto_completo`, `opciones`, `palabras_recuadro`, etc.). **Nunca reemplazar texto del libro por una descripción** ("el alumno lee 4 frases"); siempre incluir las 4 frases literales. Si la actividad presenta huecos, marcarlos con `_____`. Razón: la fidelidad al libro es la base de toda explotación didáctica posterior; sin ella, el agente no puede generar contenido coherente.

Estructura por actividad:
- `id` (str): único, formato `UX-pYY-actNN`.
- `numero` (int): orden en la unidad.
- `tipo` (str): de la **taxonomía cerrada de 20 tipos** (lista provisional, se revisa al cerrar cada unidad nueva; source of truth: `fases/1-extraccion-inventario/schema-inventario.md` §5):
  ```
  escucha, escucha_y_repite, escucha_y_responde, lee_y_escucha, ver_video,
  completa_huecos, relaciona, ordena, clasifica,
  seleccion_multiple, verdadero_falso,
  responder_preguntas_cerradas, responder_preguntas_abiertas,
  interaccion_oral, expresion_oral_libre,
  produccion_escrita_guiada, expresion_escrita_libre,
  busqueda_informacion, tarea_final, juego
  ```
  Cambios desde v10.25: terminología ELE (`interaccion_oral`, `expresion_oral_libre`, `expresion_escrita_libre`); v10.59 reescribió taxonomía con regla "tipo = acción específica del enunciado" y separó `responder_preguntas_cerradas`/`abiertas`; v10.64 añadió `escucha` (input puro auditivo, ampliación 19→20).
- `destreza` (lista de strings, alfabética, sin duplicados): habilidad(es) MCER puras de la enumeración cerrada de 6 valores (`comprension_auditiva`, `comprension_lectora`, `expresion_escrita`, `expresion_oral`, `interaccion_oral`, `mediacion`). Ver `schema-inventario.md` §5b. Reformulada en v10.60 (separación habilidad/dominio) y refinada en v10.64.
- `enfoque` (str): dominio de contenido pedagógico de la enumeración cerrada de 6 valores (`gramatica`, `vocabulario`, `comunicacion`, `pronunciacion_ortografia`, `cultura`, `transversal`). Eje ortogonal a `destreza` y a `seccion`. Ver `schema-inventario.md` §5c. Introducido en v10.60 con la separación de ejes. (En v10.115 el valor `fonetica` se renombró a `pronunciacion_ortografia`.)
- `instruccion_original` (str): texto literal del libro.
- **4 listas tipadas** (añadidas v10.111, siempre presentes; lista vacía si la actividad no trabaja la dimensión): `vocabulario` (array de strings con referencias canónicas léxicas), `tiempos_y_verbos` (array de objetos `{lema, tiempo, formas_trabajadas, estructura_perifrastica?}`), `gramatica` (array de strings con referencias canónicas gramaticales), `pronunciacion_ortografia` (array de strings con referencias canónicas pron-orto). Sustituyen al antiguo `contenido_linguistico` + `campo_semantico` eliminados en v10.115. Ver `schema-inventario.md` §3.
- `audio` (object): `{ presente: bool, pista: int (opcional) }`.
- `imagen` (object): `{ presente: bool, descripcion: str (obligatoria si presente=true) }`.
- `video` (object): `{ presente: bool }`.
- `respuestas` (array): **siempre presente**. Lista vacía si no aplica. Importante para la mayoría de actividades.
- `datos` (object abierto): saco genérico para datos específicos por tipo de actividad. Aquí caben subtipos (sopa_de_letras, programacion_tv, dialogo, etc.) sin inventar campos top-level por actividad.

Estructura por cuadro gramatical:
- `titulo` (str).
- `contenido` (object): estructura libre según el cuadro.

**Eliminado:** el campo `registro` que llevaba bitácora de cambios. Ahora va a CHANGELOG.md.

---

---

**Esquemas de los 3 JSONs globales (CERRADOS en chat 2026-05-05):**

**`nc1-tarjetas.json`** — índice global de tarjetas del curso.
- Solo dos tipos: **vocabulario** y **estrategia**. (No habrá tarjetas de gramática.)
- Top-level: `curso`, `actualizado`, `totales`, `por_unidad`, `indice_palabras`, `indice_estrategias`.
- Por unidad:
  - `vocabulario`: total, agrupación por campo semántico (lista de palabras), referencia al CSV origen.
  - `estrategia`: lista de objetos con `id`, `titulo`, `destreza`, `caja`, `archivo_origen`.
- Índices invertidos para búsqueda rápida (palabras y estrategias por unidad).
- Generación: script Python determinista que lee CSVs y archivos de sección.

**`nc1-pildoras.json`** — índice global de píldoras del curso.
- Top-level: `curso`, `actualizado`, `total_pildoras`, `por_unidad`, `indice_global`.
- Por píldora: `id`, `titulo`, `tematica`, `ubicacion_en_unidad`, archivos PDF/TEX/brief, `categoria`.
- **`categoria` queda como `null` por ahora.** Las categorías de píldoras se definirán cuando se trabaje en píldoras nuevas (no se reusa la lista de 6 categorías de `ag-vocabulario.md` porque su aplicación a píldoras está por validar).
  - **Pendiente revisar posteriormente** en este documento maestro cuando se aborden las píldoras.
- Generación: script Python determinista que lista PDFs y parsea TEX.

**`nc1-reciclaje.json`** — mapping editorial de reciclaje cross-unidad.

> ⚠ **Modelo descrito a continuación ANULADO el 2026-05-11.** Reformulación pendiente tras cierre de canon semántico de fase 1 (propuesta E-final). Ver decisión 36 (Parte 4) y bitácora 2026-05-11. La descripción que sigue se conserva como referencia histórica del modelo viejo (mapa+auto paralelos + pase 1/2 + niveles jerárquicos).

**Schema cerrado en B1.5 (v10.89), refinado a modelo de hilos en v10.92 (2026-05-09)** para soportar fan-out y cascada que el modelo punto-a-punto original no representaba.
- **Acumulativo y secuencial:** cada unidad analiza qué reutiliza de las anteriores, NO se recicla todo, **solo los hilos clave** de mayor impacto.
- **Basado en contenido**, no en actividades.
- **Manual con Claude Code en chat**, revisable y editable desde el dashboard.
- **Top-level:** `curso`, `actualizado`, `_nota`, `_acciones_validas`, `hilos[]`.
- **Por hilo:** `id` (slug, ej. `hilo-numeros`), `titulo`, `tipo`, `nivel_analisis` (`mapa` | `detalle`), `eventos[]`.
- **Por evento:** `unidad` (int), `seccion` (string), `accion`, `descripcion`, `impacto`.
- **Acciones válidas:** `introduce` · `amplia` · `aplica` · `sistematiza` · `contrasta`.
- **Tipos cerrados (4):** `vocabulario` · `tiempos_y_verbos` · `contenido_gramatical` · `estrategia`. El tipo `estrategia` cubre cualquier tipo de estrategia (comunicativa, de aprendizaje, metacognitiva…) asociada a las destrezas de la lengua. El matiz va en la descripción del hilo, no en el tipo.
- **Niveles de impacto:** `alto` / `medio` / `bajo`.
- **Secciones válidas para `seccion`:** `vocabulario`, `gramatica`, `comunicacion`, `destrezas`, `cultura`, `pronunciacion_ortografia`, `para_aprender`, `contenido_general` (solo U0).
- **Multiplicidad:** se permiten múltiples eventos del mismo hilo en la misma unidad (ej. una unidad puede `amplia` y `aplica` el mismo hilo). El dashboard renderiza todos.
- **Criterio de disparador** (adoptado de `viejo/marco-teorico-metodologico.md` §6): entra un hilo si tiene conexión natural con el contenido nuevo y lo refuerza o es requisito.
- **Pase 1 (mapa):** hilos detectados desde `nc1-curso.json` sin abrir inventarios. **Pase 2 (detalle):** validación contra inventarios + vocabulario complementario de frecuencia.
- **Estado actual (v10.94):** archivo poblado con pase 1 — 23 hilos / 70 eventos cubriendo U0-U9 (índice completo).
- **Endpoint runtime:** `/api/reciclaje` (`diagrama.py:get_reciclaje`).

---

**Por definir todavía:**
- Contenido del prompt `fases/1-extraccion-inventario/prompt.md` (escrito y operativo).
- Scripts Python: `validar_inventario.py`, `regenerar_tarjetas_globales.py`, `regenerar_pildoras_globales.py`.
- Protocolo formal de validación visual PDF vs JSON.
- **Vista HTML dinámica del inventario por unidad** integrada en el dashboard (`web/index.html`).
  - **Estado:** operativa. El servidor (`diagrama.py`) lee el JSON de cada unidad y el frontend lo renderiza al vuelo (no se genera artefacto HTML estático). Ver decisión 25 (Parte 4) y bitácora del 2026-05-07 sobre la aclaración de redacción en v10.71.
  - **Lo que sigue pendiente** (refinamiento, no implementación inicial): afinar la plantilla visual (estructura de secciones, colores, qué se muestra primero) y extender la vista a los 3 JSON globales (tarjetas, píldoras, reciclaje) cuando esos esquemas estén poblados. Se aborda en el paso B del plan de trabajo.
  - **Responsable:** Claude Code en chat con el autor.
- **Categorías de píldoras formativas:** definir cuando se trabaje en las primeras píldoras nuevas. Pendiente de revisión en este documento.

**Cambios físicos** (HISTÓRICO — ya ejecutados):
- ✅ Inventario de U03 promocionado a `unidades/U3/U3-nc1-inventario.json` (raíz). El `viejo/unidades/U03/inventario.json` se conserva como archivo.
- ✅ PDF promocionado a `unidades/U3/fuente/U3-nc1.pdf` (raíz, gitignored).
- ✅ Las 10 referencias internas del JSON ya apuntan a la nueva ruta.
- 📋 PENDIENTE (cuando proceda): el resto del contenido editorial de U03 (tarjetas/, pildoras/, secciones MD) sigue solo en `viejo/unidades/U03/` y se evaluará migrar al sistema activo cuando se construyan las fases 3-7.
- Actualizar referencias en scripts (`importar_inventario.py`, `crear_crew_agents.py`, `diagrama.py`), CLAUDE.md, README.md, .gitignore. _(Tarea histórica ya superada; `.dockerignore` se eliminó en v11.21.)_
- Crear los 3 JSONs globales vacíos en `unidades/` (con esquema mínimo cuando esté definido).

---

### Fase 2 — Análisis de vocabulario de la unidad

**Qué pasa:** se identifica qué vocabulario será materializado en tarjetas. Criterio doble: vocabulario declarado por el libro + campos semánticos más frecuentes.

**Definido:**
- Criterios editoriales completos en `.claude/rules/criterios-generacion-tarjetas.md` (raíz, regla protegida): estructura de campos, gramapop, moción de género, profesiones regulares vs irregulares, género común, verbos.
- Configuración del Agente Vocabulario del sistema antiguo en `viejo/agentes/ag-vocabulario.md` (35 KB) — incluye reglas CLT, Ciclo de 5 fases (Conti), 12 decisiones documentadas, criterios pedagógicos de selección.
- Marco metodológico de 5 fases en `viejo/00-curso-general.md` (Conti, EPI/MARS EARS).

**Por definir / por verificar:**
- Protocolo explícito de selección de **campos semánticos** (qué incluir, qué excluir, criterio de frecuencia mínima). El autor cree que está; está implícito en `viejo/agentes/ag-vocabulario.md` pero no formalizado como protocolo aislado.
- Cómo se documenta el análisis previo a generar las tarjetas.

**Archivos clave:**
- `.claude/rules/criterios-generacion-tarjetas.md` (raíz, regla protegida)
- `viejo/agentes/ag-vocabulario.md` ← contiene buena parte del protocolo operativo (sistema antiguo)
- `viejo/00-curso-general.md`

---

### Fase 3 — Tarjetas de vocabulario

**Qué pasa:** con el vocabulario seleccionado, se generan los CSVs de tarjetas (un CSV por campo semántico). Luego se construyen visualmente en InDesign con Data Merge + imágenes en Photoshop.

**Definido:**
- Criterios lingüísticos y editoriales completos (mismo archivo que Fase 2): 22 columnas en CSV, gramapop, combos con nomenclatura `[ ] ( ) / +`, traducciones a 9 idiomas.
- Especificaciones de diseño visual en `viejo/materiales/especificaciones-diseno-tarjetas.md` (162 líneas: tamaño 63×88 mm, colores, tipografía Proxima Nova, Data Merge).
- Pipeline de evaluación: `eval/evaluar_tarjetas.py` (DeepEval + promptfoo).
- Agente generador del sistema antiguo: Crew Recurvo v2.0 (3 agentes secuenciales) en `viejo/scripts/crewai/`.
- Caso real completo del sistema antiguo, todo bajo `viejo/unidades/U03/tarjetas/`: subcarpetas `csv/` (familia, profesiones, lugares, escuela, acciones cotidianas), `diseno/vocabulario/` (PSDs, PNGs, INDD), `validacion/` (PDFs editoriales).

**Por definir:**
- El archivo de diseño visual está **desactualizado** (última edición v8.9 abril; hoy v8.26). No refleja decisiones nuevas: nomenclatura combos, profesiones moción regular/irregular, color real de fondo (= color de género), verbos.
- Color de texto sobre fondo salmón (sigue marcado "Pendiente de definir").

**Archivos clave** (los del sistema antiguo en `viejo/`; el activo aún no produce tarjetas):
- `.claude/rules/criterios-generacion-tarjetas.md` (raíz, regla protegida)
- `viejo/materiales/especificaciones-diseno-tarjetas.md` ⚠ desactualizado
- `viejo/unidades/U03/tarjetas/`
- `viejo/scripts/crewai/recurvo.py` + `tools.py`
- `eval/evaluar_tarjetas.py` (raíz, heredado pero en uso)

---

### Fase 4 — Tarjetas de estrategia

**Qué pasa:** se definen 3 a 5 tarjetas de estrategia por unidad. Se analiza la unidad actual + lo que ya se ha hecho en unidades anteriores. **Regla: no repetir estrategias entre unidades.**

**Definido:**
- Sistema de colores por destreza: 6 destrezas (CO, CL, PO, PE, IO, MED) con un color cada una. En `viejo/materiales/especificaciones-diseno-tarjetas.md` (líneas 49-61).
- Caso real en U03 (sistema CrewAI v5 anterior, en `viejo/`): tarjetas de estrategia documentadas en `viejo/unidades/U03/U03-destrezas.md`, `U03-comunicacion.md` y `U03-cultura.md`.
- Tarjetas concretas de U03 ya creadas en el sistema antiguo: "Esquema comunicativo: Hablar de la familia" (Caja 2), "Escribir un correo" + Truco del semáforo (Caja 3), "Mediación oral: de yo a él/ella", "Comparar sin jerarquizar" (intercultural), "LEE EN TRES PASOS" (estrategia de lectura, reutilizable), "ESCUCHA EN TRES MODOS", "CUENTA LO QUE OYES", "Tres conjugaciones".
- Cantidad: 3-5 por unidad.

**Por definir:**
- **Protocolo de selección:** cómo se decide cuáles 3-5, cómo se valida la no-repetición con unidades anteriores.
- **Registro de no-repetición:** NO existe un índice/registro indexado (JSON, BD o markdown maestro) que liste qué estrategias se han usado en cada unidad. Hoy solo se sabe leyendo unidad por unidad.
- Validación de ortogonalidad (que no se solapen entre sí).
- Formato de archivo donde vivirán las tarjetas de estrategia (¿CSV como vocabulario?, ¿markdown?, ¿qué relación con la sección destrezas?).
- Si las tarjetas de esquema comunicativo (Caja 2) cuentan como tarjetas de estrategia o son otro producto.

**Archivos clave** (todos en `viejo/`, archivo del sistema CrewAI v5 anterior):
- `viejo/materiales/especificaciones-diseno-tarjetas.md` (sección destrezas)
- `viejo/agentes/ag-destrezas.md` (30 KB, contiene parte del protocolo)
- `viejo/agentes/ag-comunicacion.md` (29 KB)
- `viejo/unidades/U03/U03-destrezas.md`, `U03-comunicacion.md`, `U03-cultura.md`

---

### Fase 5 — Píldoras formativas

**Qué pasa:** se identifica dónde aplicar píldoras formativas en la unidad. Criterios: temáticas gramaticales más problemáticas o estrategias específicas. **El protocolo está distribuido en los archivos de agentes y construido en las distintas secciones de la unidad.**

**Definido (todo en `viejo/`, archivo del sistema CrewAI v5 anterior):**
- **Protocolo y banco de acciones en `viejo/agentes/ag-vocabulario.md`** (líneas 210-317): banco de 40+ acciones organizadas en 6 categorías:
  1. **DETECCIÓN** — pares mínimos, input saturado, realce.
  2. **MODELADO** — Sentence Builder, Read Aloud, TPR.
  3. **CONEXIÓN** — puentes con unidades anteriores.
  4. **APLICACIÓN ANTICIPADA** — predicción, estrategia de comprensión.
  5. **VERIFICACIÓN** — preguntas de cambio/patrón.
  6. **PROCESAMIENTO RECEPTIVO** — matching, discriminación auditiva.
- **Sección "PÍLDORAS FORMATIVAS" en `viejo/agentes/ag-gramatica.md`** (líneas 215-231): protocolo equivalente para gramática.
- Estructura editorial: MARS EARS + secuencia de Gagné. Documentada en `viejo/unidades/U03/brief-pildora-3.1-desarrollo.md`.
- Marca tipográfica: `**PÍLDORA FORMATIVA — [TÍTULO EN MAYÚSCULAS]**`.
- Componentes: (1) contenido para profesor + (2) propuesta de presentación.
- 10 píldoras producidas para U03 (PDF + TEX) en `viejo/unidades/U03/pildoras/`.
- Las píldoras se construyen **embebidas en las secciones** (vocabulario, gramática, comunicación) de cada unidad, no en un archivo aparte.

**Por definir:**
- Protocolo explícito de **selección temática** formalizado fuera de los archivos de agente (qué decide "problemático" vs "estrategia específica" como variable cuantificable).
- Plantilla canónica reutilizable del brief (hoy solo el 3.1 está desarrollado en formato extendido).
- Convenciones de naming consolidadas (pildora-X.Y.pdf donde X=unidad, Y=orden).
- Si los protocolos de píldora deben extraerse de los `viejo/agentes/ag-*.md` a un archivo único en raíz o quedarse distribuidos por sección.

**Archivos clave (todos en `viejo/`):**
- `viejo/agentes/ag-vocabulario.md` ← banco de píldoras de vocabulario
- `viejo/agentes/ag-gramatica.md` ← banco de píldoras de gramática
- `viejo/agentes/ag-comunicacion.md`, `ag-destrezas.md`, `ag-cultura.md`, `ag-evaluacion.md` ← posibles bancos por sección (revisión pendiente)
- `viejo/unidades/U03/brief-pildora-3.1-desarrollo.md`
- `viejo/unidades/U03/pildoras/`

---

### Fase 6 — Generación sección por sección

**Qué pasa:** se trabaja sección por sección de la guía: **vocabulario, gramática, comunicación, destrezas, cultura, evaluación, reflexión, itinerarios**. Cada sección tiene su lógica, criterios y repertorios específicos.

**Definido:**
- Listado completo de secciones (visible en `viejo/unidades/U03/`, sistema CrewAI v5 anterior):
  - `U03-vocabulario.md` (30 KB)
  - `U03-gramatica.md` (91 KB)
  - `U03-comunicacion.md` (89 KB)
  - `U03-destrezas.md` (58 KB)
  - `U03-cultura.md` (33 KB)
  - `U03-evaluacion.md` (16 KB)
  - `U03-itinerarios.md` (14 KB)
  - `U03-reflexion.md` (2 KB)
  - `U03-familia.md` (5 KB) — sección específica de U03 (no aplica a todas)
- Caso real completo solo para U03 en el sistema antiguo. **En el sistema activo (raíz)**, `unidades/U3/` tiene de momento solo `inventario.json` + `fuente/`.
- U01-U02, U04-U09: solo placeholders con `*pendiente*`.

**Por definir:**
- Para cada sección, qué criterios editoriales aplican (más allá de los de tarjetas, que solo cubren vocabulario).
- Para cada sección, qué repertorios técnicos aplican.
- Para cada sección, qué principios teórico-metodológicos aplican.
- Protocolo de orden: ¿se generan en este orden u otro? ¿Se pueden generar en paralelo? ¿Hay dependencias?

**Archivos clave** (caso real del sistema antiguo, en `viejo/`):
- `viejo/unidades/U03/*.md`

---

### Fase 7 — Doble versión por sección

**Qué pasa:** cada sección tiene **dos versiones**:
- **Versión completa y detallada** — incluye análisis de todo lo aplicado en la unidad.
- **Versión resumida** — cabe en 2 páginas.

**Definido:**
- Convención de naming: `UXX-seccion.md` (completa) y `UXX-seccion-paginas.md` (resumida).
- Caso real para U03 en el sistema antiguo (`viejo/unidades/U03/`):
  - `U03-vocabulario-paginas.md` (8.6 KB, ~1.700 palabras)
  - `U03-gramatica-paginas.md` (8.7 KB, ~2.550 palabras)
  - `U03-comunicacion-paginas.md` (9 KB, ~1.700 palabras)
  - `U03-destrezas-paginas.md` (9.1 KB, ~1.700 palabras)
  - `U03-cultura-paginas.md` (3.8 KB, ~850 palabras)
  - `U03-evaluacion-paginas.md` (0.7 KB, 1 página)

**Por definir:**
- Criterios editoriales explícitos para la versión resumida: qué se conserva, qué se omite, cómo se prioriza.
- Si las dos versiones se generan en paralelo o la resumida se deriva de la completa.
- Cómo se garantiza coherencia entre las dos versiones cuando se actualiza una.
- Tope de palabras / extensión exacta para "2 páginas" (varía por sección, según ejemplos: 850–2.550).

**Archivos clave** (caso real del sistema antiguo, en `viejo/`):
- `viejo/unidades/U03/U03-*-paginas.md` (todas)

---

### Fase 8 — Principios teórico-metodológicos + repertorios específicos por sección

**Qué pasa:** todo el material editorial debe aplicar principios teóricos y técnicas de los repertorios. Hay mucho material y se aplica de forma distinta según la sección.

**Definido (todo en `viejo/`, archivo del sistema CrewAI v5 anterior):**
- Principios teóricos:
  - `viejo/marco-teorico-metodologico.md` (100+ líneas: Merrill, Gagné, Ciclo 5 fases, EPI/MARS EARS).
  - `viejo/00-curso-general.md` (12 secciones: enfoque, temporalización, marcos teóricos, diferenciación, neurodidáctica).
- Repertorios por sección:
  - `viejo/repertorios/vocabulario.md`
  - `viejo/repertorios/gramatica.md`
  - `viejo/repertorios/comunicacion.md`
  - `viejo/repertorios/destrezas.md`
  - `viejo/repertorios/cultura.md`
  - `viejo/repertorios/evaluacion.md`
- Bancos de técnicas externas (más detallados):
  - `viejo/referencias/repertorio-120-tecnicas-EIO.md` (Expresión Interacción Oral)
  - `viejo/referencias/repertorio-124-tecnicas-CA.md` (Comprensión Auditiva)
  - `viejo/referencias/analisis-100-tecnicas-CL.md` (Comprensión Lectora)
  - `viejo/referencias/analisis-84-estrategias-EE.md` (Expresión Escrita)
  - Más archivos en `viejo/referencias/`.

**Por definir:**
- Mapeo claro de qué material teórico aplica a qué sección (hoy hay que rastrear).
- Mapeo claro de qué repertorio aplica a qué sección.
- Diferencia entre `viejo/repertorios/` y `viejo/referencias/`: solapan parcialmente, falta jerarquía.
- Cómo se decide qué técnicas usar en una sección concreta (criterios de selección).
- **Decidir qué de este material se promociona al sistema activo en raíz** y bajo qué estructura.

**Archivos clave (todos en `viejo/`):**
- `viejo/marco-teorico-metodologico.md`
- `viejo/00-curso-general.md`
- `viejo/repertorios/*.md`
- `viejo/referencias/*.md`

---

## Parte 3 — Estado del repositorio

> **NOTA:** esta sección es una **vista viva** del árbol del repositorio. Se actualiza con cada cambio físico. Última actualización: 2026-05-15 (rediseño operativo de fase 1 cerrado v10.115-117: reglas IA-first + convenciones reseteadas + 4 registries canónicos poblados + archivado de los `-viejo` a `docs/historico/`).

### Árbol actual (estado físico real, hoy)

```
guia-didactica-profesor-IA/
│
├── unidades/                                ← SISTEMA ACTIVO
│   ├── U[N]/                                (estructura por unidad — Opción B, v10.127)
│   │   ├── U[N]-nc1-inventario.json         (extracción fase 1, top-level)
│   │   ├── fuente/U[N]-nc1.pdf              (PDF embedido, gitignored)
│   │   ├── propuesta/                       (material editorial elaborado por sección)
│   │   │   ├── vocabulario.md               (sección Vocabulario)
│   │   │   ├── gramatica.md                 (sección Gramática)
│   │   │   ├── comunicacion.md              (sección Comunicación)
│   │   │   ├── destrezas.md                 (sección Destrezas)
│   │   │   ├── cultura.md                   (sección Cultura)
│   │   │   └── evaluacion.md                (sección Evaluación)
│   │   └── recursos/                        (CSVs de tarjetas, audios, imágenes, etc.)
│   │       └── tarjetas/*.csv
│   │
│   ├── U0  ├── inventario v10.117 (migrado v10.119)              + propuesta/ recursos/ (estructura creada v10.127, contenido pendiente)
│   ├── U1  ├── inventario v10.117 (migrado v10.121)              + propuesta/ recursos/ (idem)
│   ├── U2  ├── inventario shape v10.114 (pendiente migración)    + propuesta/ recursos/ vacíos
│   ├── U3  ├── inventario shape v10.114 (pendiente migración)    + propuesta/ recursos/ vacíos
│   ├── U4  ├── inventario shape v10.114 (pendiente migración)    + propuesta/ recursos/ vacíos
│   ├── U5  ├── inventario shape v10.114 (pendiente migración)    + propuesta/ recursos/ vacíos
│   ├── U6  ├── inventario shape v10.114 (pendiente migración)    + propuesta/ recursos/ vacíos
│   ├── U7  ├── inventario shape v10.114 (pendiente migración)    + propuesta/ recursos/ vacíos
│   ├── U8  ├── inventario shape v10.114 (pendiente migración)    + propuesta/ recursos/ vacíos
│   ├── U9  └── inventario shape v10.114 (pendiente migración)    + propuesta/ recursos/ vacíos
│   │
│   ├── nc1-curso.json                       (índice editorial global del curso)
│   └── nc1-reciclaje.json                   (mapa de reciclaje cross-unidad, fase 2 pausada)
│
├── fases/                                   ← una carpeta por fase con sus archivos operativos
│   ├── 1-extraccion-inventario/             (post-refactor v10.69 + rediseño v10.111-v10.117)
│   │   ├── CLAUDE.md                        (contrato corto de fase, auto-cargado)
│   │   ├── prompt.md                        (instrucciones ejecutables)
│   │   ├── schema-inventario.md             (contrato de datos puro)
│   │   ├── reglas-operativas.md             (decisiones, precedencias, criterios IA-first)
│   │   ├── glosario.md                      (diccionario operativo, añadido v10.111)
│   │   ├── convenciones-y-casos.md          (transcripción + casebook, reseteado v10.116)
│   │   ├── campos-semanticos-canonicos.json (registry léxico, 99 categorías canónicas)
│   │   ├── verbos-canonicos.json            (registry verbal, 48 lemas)
│   │   ├── gramatica-canonica.json          (registry gramatical, 23 categorías, registry v1.7)
│   │   ├── pronunciacion-ortografia-canonica.json (registry pron-orto, 7 categorías, poblado v10.117)
│   │   └── pcic-a1-{vocabulario,gramatica,pronunciacion-ortografia,comunicacion}.json (4 PCIC A1)
│   └── 2-reciclaje/                         (fase 2 pausada; REDISEÑO-EN-CURSO.md = documento único del rediseño IA-first. El viejo se archivó en docs/historico/ el 2026-05-20, v11.34)
│
├── scripts/                                 ← código activo
│   └── validar_inventario.py                (validador; alineación post-rediseño en deuda — §A.1 schema)
│
├── docs/historico/                          ← archivado de artefactos cerrados
│   ├── refactor-prompt-fase1/               (REFACTOR-PROPUESTA, REFACTOR-WORKTREE, README; v10.72)
│   ├── pruebas/                             (corrida U4-propuesta aprobada v10.115)
│   ├── pruebas-fallidas/                    (corrida U4-propuesta sobre v10.114 invalidada)
│   ├── CHANGELOG-pre-refactor.md            (entradas pre-v10.40, archivadas v10.75)
│   ├── PROCESO-MAESTRO-arboles-historicos.md (árboles antiguos, v10.76)
│   ├── PROCESO-MAESTRO-parte5bis-migracion.md (Parte 5.bis CERRADA, v10.76)
│   ├── REVIEW-bloque-A-cerrado.md           (detalle Bloque A cerrado, v10.77)
│   ├── B1.5-contrato-reciclaje.md           (contrato histórico de reciclaje)
│   ├── schema-inventario-viejo.md           (archivado v10.114)
│   ├── PROPUESTA-PIEZA-2-IA-FIRST.md        (archivado v10.114, absorbido en contratos vivos)
│   ├── REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md (archivado v10.115, todas piezas absorbidas)
│   ├── convenciones-y-casos-viejo.md        (archivado v10.116, reseteo cerrado)
│   ├── reglas-operativas-viejo.md           (archivado v10.116, reseteo cerrado)
│   ├── prompt-v1-antiguo.md                 (versión antigua, no usar)
│   └── prompt-v2-monolitico-NO-USAR.md      (versión antigua, no usar)
│
├── eval/                                    ← evaluación (heredado, en uso)
├── web/                                     ← dashboard (heredado, en uso)
├── diagrama.py                              ← servidor del dashboard (heredado, en uso)
│
├── viejo/                                   ← ARCHIVO CrewAI v5.0 (intocable hasta autorización)
│   ├── unidades/U03/                        (contenido editorial original)
│   ├── materiales/, agentes/, repertorios/, referencias/, diseno/, _template/
│   ├── scripts/                             (importar_inventario.py, crewai/, etc.)
│   ├── CLAUDE-anterior.md
│   ├── marco-teorico-metodologico.md, 00-curso-general.md
│   └── material-complementario/             (gitignored)
│
├── .claude/rules/                           (meta-reglas técnicas: agent-prompt-design, tool-design, etc.)
├── README.md, CHANGELOG.md, REVIEW.md
├── CLAUDE.md                                ← contrato global del proyecto (auto-cargado)
├── PROCESO-MAESTRO.md                       ← este documento (temporal)
├── requirements.txt, .env.example
└── .gitignore
```

### Árbol intermedio (estado anterior — pre-disolución de `nuevo/`)

Archivado en `docs/historico/PROCESO-MAESTRO-arboles-historicos.md`. Estructura de la fase de migración cuando `nuevo/` y `viejo/` coexistían como zonas separadas. NO ES EL ESTADO ACTUAL.

### Árbol antes del split (referencia histórica)

Archivado en `docs/historico/PROCESO-MAESTRO-arboles-historicos.md`. Estado del repo anterior a 2026-05-05 12:15, cuando todo el contenido editorial vivía en raíz antes del split a `viejo/`. NO ES EL ESTADO ACTUAL.

## Parte 4 — Decisiones cerradas en conversación

### Sobre el modelo conceptual
1. **Tres tipos de contenido**: producto editorial, sistema técnico, especificaciones.
2. **Fuente única para criterios editoriales**: archivo MD; BD se rellena por script. La BD no se puebla ahora pero el diseño debe contemplarla.
3. **Forma de captura de lecciones**: bidireccional — Claude Code propone cuando lo ve claro y el autor puede dictar manualmente.
4. **Estructura por sección**: las especificaciones, repertorios y lecciones deben organizarse por sección de trabajo (vocabulario, gramática, comunicación, destrezas, cultura, etc.), no solo por tipo de producto. *(Cerrada conceptualmente, falta diseñar carpetas concretas.)*
5. **No ejecutar nada hasta validar todo en chat** (excepto tareas explícitamente autorizadas como el split).

### Sobre la organización física del repositorio
6. **Split físico en `viejo/` + `nuevo/`** ejecutado el 2026-05-05 12:15 y **`nuevo/` posteriormente disuelto** el 2026-05-05 16:00. Estado actual: `viejo/` contiene el archivo del CrewAI v5 y el sistema activo vive directamente en raíz (`unidades/`, `scripts/`, `fases/`, `web/`, etc.).
7. **Código (`scripts/`, `web/`, `eval/`), dashboard (`diagrama.py`) y documentos (`README.md`, `CLAUDE.md`, etc.) se quedan en raíz**, NO se mueven a `viejo/`.
8. **El dashboard `web/` no se duplica.** La integración del informe HTML por unidad se hace como sección nueva del dashboard existente.

### Sobre las convenciones de naming
9. **Carpetas de unidad sin cero**: `U0/`, `U1/`, `U2/`...`U9/`. U0 reservado a la unidad introductoria atípica "Punto de partida". (Caveat: válido para cursos de ≤9 unidades. Para 10+ habría que reintroducir el cero o usar otro esquema.)
10. **Prefijo de archivo por unidad**: `UX-nc1-` (X = nº unidad, NC1 = curso "Nuevo Compañeros 1"). Ejemplo: `U3-nc1-inventario.json`.
11. **Prefijo de archivo global del curso**: `nc1-`. Ejemplo: `nc1-reciclaje.json`.

### Sobre los 4 JSONs (Fase 1 del proceso)
12. **Material fuente** por ahora limitado a PDF del libro del alumno. Si cambia, se versiona y se registra en CHANGELOG.
13. **Salidas por unidad**: 1 archivo (`UX-nc1-inventario.json`).
14. **Salidas globales del curso**: 3 archivos (`nc1-reciclaje.json`, `nc1-tarjetas.json`, `nc1-pildoras.json`).
15. **Modelo de los globales: A — índice/proyección.** El dato vive en su unidad; los globales se regeneran. NO se editan a mano (excepto reciclaje).
16. **Ubicación de los globales**: en `unidades/`, junto a las carpetas de unidad.
17. **Esquema del inventario JSON cerrado**: `vocabulario_consolidado` con **2 bloques** (principal/recurrente; el bloque `comprensión` se eliminó en v10.115), más los otros 3 bloques top-level consolidados `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada` (añadidos en v10.111), `secciones` como índice top-level, `tipo` con taxonomía cerrada de **20 valores** (source of truth: `fases/1-extraccion-inventario/schema-inventario.md` §5), `destreza` (lista MCER de 6 valores con orden alfabético, schema §5b) y `enfoque` (string del enum de 6, schema §5c) como ejes ortogonales independientes, `datos` como saco genérico, `respuestas` siempre presente, sub-objetos consistentes para audio/imagen/video, `registro` eliminado (va a CHANGELOG).
18. **Esquema de `nc1-tarjetas.json`**: solo vocabulario y estrategia (no gramática). `por_unidad` + `indice_palabras` + `indice_estrategias`.
19. **Esquema de `nc1-pildoras.json`**: `por_unidad` + `indice_global`. Categorías como `null` por ahora — se definen cuando se trabajen píldoras nuevas.
20. **Esquema de `nc1-reciclaje.json`**: modelo de hilos (refinado v10.92, taxonomía unificada v10.94). Tipos cerrados (4): `vocabulario`, `tiempos_y_verbos`, `contenido_gramatical`, `estrategia` (cubre cualquier tipo de estrategia asociada a las destrezas de la lengua). Niveles de impacto: alto/medio/bajo. Revisable y editable desde el dashboard.

### Sobre la generación de los JSONs
21. **`UX-nc1-inventario.json`**: lo genera **Claude Code** en chat con un **prompt versionado** (`fases/1-extraccion-inventario/prompt.md`, operativo). NO Python autónomo.
22. **`nc1-tarjetas.json`** y **`nc1-pildoras.json`**: scripts Python deterministas (`regenerar_tarjetas_globales.py`, `regenerar_pildoras_globales.py`, a escribir). Cero tokens.
23. **`nc1-reciclaje.json`** (decisión histórica): originalmente **manual con Claude Code** en chat al cerrar cada unidad, NO automático, NO inferido por script, acumulativo. **Superada por la decisión 36** (v10.108): scripts de regeneración existen, fase 2 actualmente pausada, `integrar_unidad.py` no regenera por defecto.
24. **Validación post-extracción** del inventario: script Python `scripts/validar_inventario.py` (operativo desde antes del refactor; alineado con `fases/1-extraccion-inventario/schema-inventario.md` hasta v10.62 — cross-check A4.5.5; tras el rediseño v10.115-117 la alineación queda transitoriamente declarada como deuda en el Apéndice §A.1 del schema, con validación manual sustitutiva mientras dure).

### Sobre el dashboard y el informe HTML
25. **Cada extracción de inventario produce un JSON por unidad.** Ese JSON queda además disponible como vista HTML dinámica integrada en el dashboard existente (`web/index.html`), sin generar por ahora un archivo HTML independiente.
26. **El dashboard debe mostrar** todos los JSON (inventario por unidad + 3 globales) y permitir revisar/editar las propuestas de reciclaje al cerrar cada unidad.

### Protocolo operativo del ejecutor 2 — extracciones en worktree paralelo (cerrado 2026-05-08, v10.90)

Cada nueva extracción de inventario (U4, U5…) se hace en un worktree dedicado, nunca en main.

**Pasos:**
1. Crear worktree desde main: `git worktree add ../guia-didactica-extract-U4 -b extract/U4`
2. Trabajar solo en ese worktree: extraer, corregir, iterar.
3. Validar con el venv y el validador del repo principal:
   ```bash
   cd /Users/armandocruz/Desktop/guia-didactica-profesor-IA
   source .venv/bin/activate
   python3 scripts/validar_inventario.py 4 --path ../guia-didactica-extract-U4/unidades/U4/U4-nc1-inventario.json
   ```
4. Revisar visualmente en el dashboard local arrancado desde main con `EXTRA_UNIDADES_PATHS` (ver README §"Arrancar el dashboard con worktrees paralelos").
5. No integrar a main. La integración va en paso posterior separado con receta `git merge --no-ff --no-commit`.

**Invariantes:**
- Nunca commitear en main desde el worktree de extracción.
- Los refinamientos de regla que dispare la extracción se registran en main (ejecutor 1), no en el worktree.
- Aplica a cualquier unidad nueva (U4, U5…). U3 ya integrada en v10.91 siguiendo este mismo protocolo.

---

### Sobre la arquitectura datos + instrucciones (decidida 2026-05-05)

27. **Datos centralizados** en `unidades/UX/` — única ubicación canónica de inventario, tarjetas, píldoras, secciones de cada unidad.
    - **Instrucciones modulares** en `fases/N-X/` — cada fase tiene su `CLAUDE.md` (contexto operativo) + `prompt.md` (instrucciones detalladas).
    - **NO se duplican datos por fase**, aunque se busque ahorro de tokens. Razones: (1) viola Regla de Oro #5 (una fuente única); (2) CLAUDE.md modular ya carga solo el contexto relevante; (3) los datos no se cargan automáticamente, solo cuando Claude Code los lee explícitamente con `Read`.
    - **Optimizaciones de tokens reales:** prompts compactos con ejemplos, `Read` con offset/limit en JSONs grandes, sesiones limpias por fase.

### Sobre la arquitectura documental de las fases (refactor de fase 1, decidido 2026-05-06)
28. **Refactor documental de fase 1 aprobado** tras 6 rondas de revisión (v10.35 → v10.39). El `prompt.md` actual mezcla siete funciones distintas (prompt de ejecución, schema, casebook, mantenimiento, etc.) en un único archivo de 547 líneas / 27 secciones. Va contra Anthropic best practices sobre instrucciones modulares y concisas, y crea contradicciones por falta de single source of truth.
29. **Arquitectura objetivo: 5 archivos** en `fases/1-extraccion-inventario/`:
    - `CLAUDE.md` — contrato de fase (40-60 líneas como norte).
    - `prompt.md` — prompt core de ejecución (80-120 líneas como norte).
    - `schema-inventario.md` — contrato de datos puro (forma del JSON, tipos, obligatoriedad).
    - `reglas-operativas.md` — decisión, clasificación, población, unidades atípicas.
    - `convenciones-y-casos.md` — transcripción del libro + casebook histórico.
30. **Frontera de capas (no negociable):** split por capa, no por campo. Forma → schema; decisión → reglas-operativas; transcripción/casos → convenciones-y-casos.
31. **Source of truth de precedencias:** vive exclusivamente en `reglas-operativas.md`. Otros archivos invocan por referencia, no copian.
32. **Skill de Claude Code (`.claude/skills/...`) fuera de v1.** Reabrir solo si tras v1 el patrón de uso justifica encapsular (≈10 ejecuciones en NC1 no compensan).
33. **Schema documental y validador (`scripts/validar_inventario.py`):** contratos paralelos del mismo shape. **No pueden divergir en el momento del merge.** Cualquier divergencia detectada por el cross-check del paso 5.5 se resuelve antes del merge en commit aparte (técnicamente fuera del refactor nominal, pero prerequisito ineludible).
34. **Source of truth operativa del plan ejecutable** (durante el refactor de fase 1, ahora cerrado): el plan vivió en `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md` y se ejecutó al 100% con el merge del 2026-05-07 (v10.69). El archivo se conserva en `docs/historico/refactor-prompt-fase1/` como referencia histórica. PROCESO-MAESTRO nunca duplicó el detalle del plan; lo invocaba. REVIEW.md llevó el progreso por sub-paso.

35. **Esquema de `nc1-curso.json` cerrado** (2026-05-08, v10.82, B1.4; refinada en v10.82b tras dictamen del revisor): índice editorial global del curso, derivado del **índice oficial del libro impreso (Scope and Sequence, páginas 6-7)**, no de meta-documentación pedagógica. Path canónico: `unidades/nc1-curso.json`.

  **Estructura top-level:**
  - `curso` ("nc1"), `titulo`, `editorial`, `nivel` ("A1.1")
  - `fuente` (objeto: descripción + páginas origen)
  - `estructura_libro` (objeto: totales)
  - `unidades` (array)
  - `apendice` (array)
  - `_nota` (string opcional para anotaciones contractuales y deuda técnica conocida)

  **Por unidad regular (U1-U9):** campos top-level `vocabulario` (lista), `gramatica` (lista), `para_aprender` (string o `null`), `pronunciacion_ortografia` (string), `comunicacion` (lista), `destrezas` (lista), `cultura` (lista), más `pagina_inicio` (int) y `paginas_libro` (string).

  **Por U0** (Punto de partida, atípica): solo `contenido_general` (lista).

  **Apéndice:** array de objetos con campos `seccion` (string) y `pagina_inicio` (int). Sin contenido detallado.

  **Contenido de las celdas:** literal del índice del libro, sin expansión MCER ni interpretación pedagógica.

  **Source of truth (regla refinada en v10.82b):** `nc1-curso.json` es **canónico para el índice editorial del curso** (qué se enseña en cada unidad). Los campos `paginas_libro` y `contenidos_indice` de cada inventario per-unidad reflejan lo extraído del PDF concreto y **pueden divergir legítimamente** cuando el libro tiene portadas/separadores no extraídos o cuando el PDF disponible no coincide exactamente con la edición oficial. Las divergencias detectadas se anotan como **deuda técnica conocida** en el campo `_nota` del propio JSON, **no bloquean el cierre** de B1.4 ni de B1.5. Se resuelven cuando se actualice el inventario afectado (re-extracción en su worktree paralelo).

  **Validador estructural:** sin checks propios todavía. Se decidirá si añadir a `validar_inventario.py` cuando aparezca el primer caso real de bug de schema.

---

### Sobre el canon semántico de fase 1 (decidido 2026-05-11)

36. **Canon semántico vive dentro de fase 1 — propuesta E-final** (cerrada tras 5 iteraciones revisor↔ejecutor). El universo cerrado de nombres válidos para `actividad.campo_semantico` y para las claves de `vocabulario_consolidado.{principal,recurrente,comprension}` se gobierna desde fase 1, sin crear archivos de documentación nuevos. Sustituye la decisión "liberal" antigua de `reglas-operativas.md` §5.6.

   **Artefactos nuevos (solo datos y código, no doc):**
   - `fases/1-extraccion-inventario/campos-semanticos-canonicos.json` — fuente única de verdad **solo de datos**. Estructura: `version`, `actualizado`, `campos[]` con entradas `{canonico, origen, [nota], aliases_indice, aliases_auto}`. La política (rollout R1/R2/R3, reglas de uso, árbol de decisión) NO vive embebida en el JSON; vive en `fases/1-extraccion-inventario/reglas-operativas.md`. La constante `LEGACY_UNIDADES_R1` vive en `scripts/validar_inventario.py` (es estado operativo del validador, no del canon).
   - `scripts/canon.py` — módulo compartido con 4 funciones: `cargar_canon()`, `validar_canon()`, `escribir_canon()` (atómico, con backup y lock), `detectar_pendientes()`.
   - `inicializar_canon_semantico.py` — one-off que pobló el JSON inicial desde `nc1-curso.json` (`origen: "indice"`) + subset PCIC A1 curado (`origen: "pcic_a1"`). Cumplido su cometido; archivado en `docs/historico/scripts-one-shot/` (v11.18).

   **Modificaciones a documentos de fase 1 (sin archivos doc nuevos):** `CLAUDE.md` (regla crítica + tabla de navegación), `prompt.md` (paso de extracción canónica desde origen + 2 ítems al checklist), `reglas-operativas.md` (sustituir §5.6 por política de canon + árbol de decisión + rollout), `schema-inventario.md` (§9 y §10 con restricción de naming + marca `_pendiente_canon`).

   **Endurecimiento del validador:** `scripts/validar_inventario.py` gana 3 canales de salida (errores, avisos, **auditoría legacy con contador propio**). Rollout R1 (auditoría legacy para U0-U9, error duro para nuevas) → R2 (legacy vaciada, error duro toda unidad) → R3 (endurecimiento final). Marca `_pendiente_canon` → error duro siempre.

   **Origen de las entradas:**
   - `indice`: viene de `nc1-curso.json`. El canónico (literal o vía alias en `aliases_indice`) debe existir en `vocabulario[]` o `contenido_general[]`.
   - `pcic_a1`: subcategoría curada del PCIC A1 Cervantes. Sin casos híbridos con índice.
   - `excepcion`: caso fuera de A1 con `nota` obligatoria.

   **Árbol de decisión** (vive una sola vez en `reglas-operativas.md`):
   ```
   ¿Canónico ya existe en el canon (literal o alias)?
   ├── SÍ → añadir alias si no estaba + renombrar en el inventario
   └── NO → ¿viene del índice del libro?
       ├── SÍ → crear entrada con origen: "indice"
       └── NO → ¿cubierto por PCIC A1?
           ├── SÍ → crear entrada con origen: "pcic_a1"
           └── NO → ¿ruido del extractor / parche contextual?
               ├── SÍ → no se amplía canon, solo se sanea inventario
               └── NO → caso excepción justificada (origen: "excepcion" + nota)
   ```

   **Dos carriles complementarios:**
   - **Carril A** — extracción canónica desde origen: el prompt de fase 1 instruye al extractor a agrupar `vocabulario_consolidado` directamente en nombres canónicos. Si no encuentra categoría segura, usa la marca literal `"_pendiente_canon"` como clave dentro del sub-bloque `principal`/`recurrente`. (La clave `campo_semantico` por actividad fue eliminada del schema en v10.115 junto con `contenido_linguistico`; el canon léxico se aplica ahora directamente sobre las referencias en `actividad.vocabulario` y sobre las claves de `vocabulario_consolidado`.) Estado transitorio de worktree, bloquea cierre.
   - **Carril B** — saneamiento retrospectivo de U0-U9: el validador en R1 lista los campos no canónicos como auditoría legacy; el dashboard los muestra; el humano resuelve uno a uno con Claude Code aplicando el árbol de decisión.

   **Dashboard:** solo lectura. Endpoint `GET /api/canon/pendientes` + vista UI mínima de cola. NO escribe en el canon. La edición la hace Claude Code (carril operativo del sistema).

   **Fase 2 pausada** hasta cierre del canon. El `nc1-reciclaje.json` actual queda congelado. La reformulación del reciclaje (modelo de hilos) entra como trabajo posterior. **`integrar_unidad.py` no regenera reciclaje por defecto** desde v10.108d: la llamada al regenerador está detrás del flag explícito `--regenerar-reciclaje` para que el comportamiento por defecto respete la pausa. Cuando fase 2 se reactive, ese flag puede dejar de ser necesario.

---

## Parte 5 — Decisiones pendientes

### Sobre la estructura física del repo
- Carpeta para las especificaciones por sección en raíz (probablemente `especificaciones/SECCION/`): nombre, ubicación, jerarquía interna.
- **Qué hacer con `viejo/agentes/*.md`** cuando se migren a raíz: cada archivo mezcla "especificación operativa de la sección" + "configuración del agente CrewAI". Hay que separar las dos partes. Posibilidades:
  - A) Extraer la parte de especificación operativa a `especificaciones/SECCION/` (raíz) y dejar la config del agente aparte.
  - B) Dejar los archivos como están en `viejo/` y referenciarlos desde la nueva estructura.
  - C) Renombrar a `especificaciones/X/protocolo-operativo.md` (raíz) y extraer la config CrewAI a un YAML/JSON técnico aparte.
- Qué hacer con `viejo/repertorios/`, `viejo/referencias/`, `viejo/marco-teorico-*`, `viejo/00-curso-general.md` al migrar a raíz.
- Qué hacer con `viejo/materiales/` (1 archivo: `especificaciones-diseno-tarjetas.md` — desactualizado desde abril, hay que reescribir).
- **Qué es `viejo/_template/`** (16 archivos sin trackear, parece scaffold de proyecto). Decisión: confirmar propósito o eliminar.
- Renombrar `diagrama.py` → `web/server.py` (o similar).

### Sobre el sistema de lecciones de Claude Code
- Formato exacto de cada lección.
- Mecanismo de activación: ¿README de cada sección las nombra? ¿CLAUDE.md tiene una regla global?
- Convención de naming de archivos.

### Sobre el sistema de sincronización con BD
- Cuándo se escribe el script `sincronizar-reglas.py` (no urgente, pero diseño actual debe contemplar).
- Qué archivos de criterios son "sincronizables" y cuáles son solo para Claude Code.

### Sobre las protecciones (qué archivos no se modifican sin autorización)
- Lista vigente: `viejo/.claude/rules/agent-prompt-design.md`, `tool-design.md`, `criterios-generacion-tarjetas.md`, `scripts/crewai/tools.py`.
- Tras la reorganización en raíz: la lista cambia (paths nuevos) y posiblemente se amplía (¿criterios por sección también protegidos?).

### Sobre el contenido (huecos editoriales)
- Protocolo de selección de campos semánticos (Fase 2).
- Protocolo de selección de tarjetas de estrategia y validación de no-repetición (Fase 4).
- Protocolo de selección temática para píldoras (Fase 5).
- **Categorías de píldoras formativas**: definir cuando se trabaje en píldoras nuevas. Hoy está como `null` en `nc1-pildoras.json`.
- Criterios de la versión resumida vs completa (Fase 7).
- Mapeo material teórico ↔ sección (Fase 8).

### Bugs conocidos / deuda técnica — ✅ CERRADOS 2026-05-05

Detectados por revisor el 2026-05-05. Decisiones tomadas por el autor el 2026-05-05 22:00 (cierre A3):

- **B1 — `tools.py:346` escribe a path inexistente.** ✅ **Pospuesto indefinidamente.** CrewAI bloqueado (AGENTES = BLOQUEADO en sidebar). Bug inerte hasta que se reactive el flujo CrewAI.

- **B2 — Railway: `viejo/repertorios/` no existe en el repo remoto.** ✅ **Aceptado.** Está en `viejo/` sin trackear. El flujo de agentes está bloqueado. Decisión: se queda así.

- **B3 — `diagrama.py` path hardcoded a inventario viejo.** ✅ **Resuelto en v10.15.** Verificado: apunta a `unidades/U3/U3-nc1-inventario.json`.

- **B4 — `_normSeccion` no fusiona pestañas `(cont.)`.** ✅ **Sin acción.** Cosmético. Se resuelve automáticamente cuando U3 migre al nuevo schema con claves normalizadas (`vocabulario`, `gramatica`...) y `_normSeccion` se elimine.

### Sobre la implementación pendiente
- Scripts Python: `regenerar_tarjetas_globales.py`, `regenerar_pildoras_globales.py` (a escribir; `validar_inventario.py` ya operativo).
- Refinamiento visual de la **vista HTML dinámica** del inventario en el dashboard (paso B del plan): afinar plantilla (estructura de secciones, colores, qué muestra primero) y extender la vista a los 3 JSON globales cuando esos esquemas estén poblados. La vista existe y funciona; lo pendiente es refinamiento, no implementación inicial. Ver decisión 25 (Parte 4) y la aclaración de redacción cerrada en v10.71.
- Protocolo formal de validación visual PDF vs JSON.

---

---

## Parte 5.bis — Histórico de la estrategia de migración (CERRADA)

Archivado en `docs/historico/PROCESO-MAESTRO-parte5bis-migracion.md`. La migración está cerrada; el estado actual del repo se ve en el árbol vivo de la Parte 3.

## Parte 6 — Pasos siguientes (estado y plan)

### Hitos cerrados (cronológico — actualizado 2026-05-07)
- ✅ Validación inicial del documento con el autor.
- ✅ Cierre de Fase 1 (esquemas JSON + estrategia de generación).
- ✅ Split físico `viejo/` + `nuevo/` ejecutado.
- ✅ Commit y push (`c5e08e9`) con el split.
- ✅ Vista HTML del informe integrada en el dashboard (paso B).
- ✅ Extracción real de U3 desde el PDF con el nuevo schema.
- ✅ Prompt versionado de la fase 1 escrito (`fases/1-extraccion-inventario/prompt.md`).
- ✅ Validador estructural escrito y funcionando (`scripts/validar_inventario.py`).
- ✅ Disolución de `nuevo/` — sistema activo en raíz, `viejo/` como archivo.
- ✅ CLAUDE.md global creado.
- 📋 REVIEW.md — plan detallado paso a paso de lo que queda (ver documento separado).

### Plan de trabajo

**El plan operativo vivo está en `REVIEW.md`** (bloques A–E con gates explícitos). Esta parte ya no se mantiene aquí para evitar duplicación. Resumen del estado:

- ✅ **Bloques operativos cerrados:** esquemas JSON cerrados, vista HTML dinámica del dashboard operativa, extracciones de U0/U1/U3 con contrato post-refactor (taxonomía 20 + destreza/enfoque) validando 0/0, prompt versionado, validador alineado con schema en cross-check A4.5.5, disolución de `nuevo/`, CLAUDE.md modular, refactor del prompt de fase 1 cerrado en v10.69.
- ✅ **Bloque A cerrado** (ver REVIEW): A1 (validar U3 con autor), A2 (probar con U0), A3 (bugs B1-B4), A4 (refactor documental de fase 1) — todos en ✅. Resumen vivo en `REVIEW.md` sección "Bloque A"; detalle íntegro (sub-pasos A4.0-A4.6, gates, riesgos) archivado en `docs/historico/REVIEW-bloque-A-cerrado.md`; bitácora cronológica general permanece viva en `REVIEW.md`.
- 🔄 **Bloque B parcial** (REVIEW): infraestructura JSONs globales del curso. B5 ✅ cerrado; B1.5 ✅ cerrado (v10.89); B2a.1 (pase 1) ✅ cerrado (v10.94) — `nc1-reciclaje.json` poblado con 23 hilos / 70 eventos cubriendo U0-U9, taxonomía 4 tipos; B2a.2 (pase 2 contra inventarios) pendiente; tarjetas bloqueadas por B1+fase 2; píldoras bloqueadas por fase 5.
- 📋 **Bloque C pendiente:** construir fases 2-8 (una a una).
- 📋 **Bloque D pendiente:** sistema de lecciones de Claude Code.
- 📋 **Bloque E pendiente** (al cierre del curso): limpieza final, eliminar `viejo/`, eliminar `PROCESO-MAESTRO.md` y `REVIEW.md`.

Detalle paso a paso con condiciones de cierre: ver `REVIEW.md`.

---

## Bitácora del documento

- **2026-05-20** — **Decisión de alcance de fase 2: `comunicacion` y `estrategia` pospuestas** (v11.33). El rediseño activo de fase 2 (`fases/2-reciclaje/REDISEÑO-EN-CURSO.md`) cubre solo los **bloques lingüísticos** del inventario — vocabulario, gramática, pronunciación/ortografía y verbal (más `perifrasis` derivado). Las **funciones comunicativas** y las **estrategias** quedan fuera del rediseño actual: son desarrollo **posterior**, a abordar más adelante como ampliación del modelo. **Roadmap:** cuando los bloques lingüísticos estén cerrados e implementados, se retoma el alcance para incorporar `comunicacion` y `estrategia` (hilos propios, etiquetas, granularidad y nivel `detalle` específicos de cada uno). Sincronizado: `REDISEÑO-EN-CURSO.md` §5 Nivel 1 (decisión registrada, pieza retirada de las pendientes) y `fases/2-reciclaje/CLAUDE.md` (contrato corto dejó de afirmar que fase 2 ya las modela).
- **2026-05-11** — **Decisión 36 implementada: canon semántico activado en fase 1** (v10.108 batch único, commit `46534c7`; v10.108b ajuste de wording del prompt, `5e963cd`; v10.108c sincronización documental autodocumentada). Validador endurecido con 3 canales (errores, avisos, auditoría legacy) en rollout R1. U0-U9 mantienen validación 0/0 con auditoría legacy informativa pendiente de saneamiento retrospectivo (carril B, paso futuro). Caso negativo verificado: marca `_pendiente_canon` y valor fuera de canon en unidad nueva producen error duro. Canon íntegro (98 entradas). Cero archivos doc nuevos, integración total en docs existentes de fase 1.
- **2026-05-11** — **Decisión 36 cerrada: canon semántico en fase 1 (E-final).** Tras 5 iteraciones revisor↔ejecutor: el universo de `campo_semantico` y claves de `vocabulario_consolidado` se gobierna mediante canon JSON dentro de fase 1, sin archivos doc nuevos. Artefactos nuevos: JSON canónico + `scripts/canon.py` + script de inicialización. Modificaciones quirúrgicas en docs de fase 1. Validador endurecido con 3 canales (errores, avisos, auditoría legacy) + rollout R1/R2/R3. Dos carriles: extracción canónica desde origen + saneamiento retrospectivo U0-U9. Marca `_pendiente_canon` transitoria que bloquea cierre. Fase 2 pausada hasta canon limpio; modelo viejo (mapa+auto+detalle) anulado en línea 213 con anotación. Implementación pendiente.
- **2026-05-11** — **U9 integrada a main** (v10.104) vía `integrar_unidad.py` (commit `ea4cb51`). 41 actividades, 6 cuadros, autoevaluación presente, validador 0/0. Reciclaje sin cambios respecto a post-U8 (92 mapa + 89 auto = 181 hilos): U9 no introduce campos semánticos nuevos. **Curso completo extraído — U0-U9 integradas y validando 0/0**. Refinamientos del extractor pendientes (canon semántico + doble superficie del validador) documentados localmente.
- **2026-05-11** — Sincronización documental v10.104b: CHANGELOG/REVIEW/PROCESO-MAESTRO/README actualizados al cierre extractivo de fase 1; entrada autodocumentada en el mismo commit para no reabrir la regresión de trazabilidad.
- **2026-05-10** — Sincronización documental U8 (v10.103b) + autodocumentación + retirada de referencia a `REDISEÑO-EN-CURSO.md` (artefacto local untracked) del estado comprometido del bloque B (v10.103c).
- **2026-05-10** — **U8 integrada a main** (v10.103) vía `integrar_unidad.py` (commit `3f3e626`). 46 actividades, 5 cuadros, validador 0/0. Reciclaje actualizado: 181 hilos (92 mapa + 89 auto). U0-U8 integradas y validando 0/0.
- **2026-05-10** — **U7 integrada a main** (v10.102) vía `integrar_unidad.py` (commit `590c9f3`). 46 actividades, 4 cuadros, validador 0/0. Reciclaje actualizado: 171 hilos (92 mapa + 79 auto). Segunda integración con el flujo automatizado, sin desviaciones del protocolo. U0-U7 integradas y validando 0/0.
- **2026-05-10** — Refuerzo del checklist de cierre en `prompt.md` de fase 1 (v10.101). Tras auditar U6: las reglas existen, los fallos eran invisibles al validador. Añadidos 2 ítems explícitos al checklist (ejemplo no duplicado en respuestas; cardinalidad literal). Sin cambios en reglas canónicas.
- **2026-05-10** — **U6 integrada a main** (v10.100) vía `integrar_unidad.py`. Primera integración con el flujo automatizado de v10.99. 44 actividades, 4 cuadros, autoevaluación presente, validador 0/0. Reciclaje actualizado: 161 hilos (92 mapa + 69 auto). Tres fixes de auditoría del ejecutor 2 en el inventario final: ejemplo duplicado eliminado en `respuestas` de U6-p64-act01 y U6-p64-act02; ítem inventado #9 eliminado en U6-p65-act04. U6 estrena el campo canónico `columnas_relaciona` (v10.98) en U6-p63-act05, U6-p63-act08, U6-p68-act02 y U6-p71-act05. U0-U6 integradas y validando 0/0.
- **2026-05-10** — Sincronización documental v10.99d-v10.99g (CHANGELOG, REVIEW, PROCESO-MAESTRO al día con commits v10.97-v10.99c). v10.99e corrigió cronología retroactiva en la entrada de v10.99; v10.99f cerró trazabilidad de v10.99e; v10.99g cerró la regresión "cada commit doc abre brecha" autodocumentándose junto a v10.99e/f, además de retirar atribución falsa en la entrada de v10.99e.
- **2026-05-10** — **Fase 2 reciclaje automatizada** (v10.97-v10.99c). Fase 2 creada como fase operativa con contrato completo (`fases/2-reciclaje/CLAUDE.md` + `reglas-reciclaje.md`). Scripts: `regenerar_reciclaje_mapa.py` genera nivel mapa desde `nc1-curso.json` (92 hilos, una sola vez); `regenerar_reciclaje_vocabulario.py` genera nivel auto desde inventarios aprobados (59 hilos), encadenado automáticamente por el script de integración. `integrar_unidad.py` automatiza el flujo completo de integración (copia, valida, actualiza reciclaje, commit aislado) con restauración de main en cualquier fallo. `nc1-reciclaje.json`: 92 mapa + 59 auto = 151 hilos. U5 integrada. Campo canónico `columnas_relaciona` añadido a fase 1; migración U1/U5.
- **2026-05-08** — **U2 integrada a main** (v10.87): primera integración del carril paralelo de extracciones tras la apertura del modelo de worktrees (v10.79). Receta `git merge --no-ff --no-commit` aplicada limpiamente. U2 (10 páginas, 52 actividades, 6 cuadros) con contrato post-refactor. Hallazgos del ejecutor 2 que dispararon refinamientos en main: bifurcación "Para aprender" (v10.83), schema cuadros con `texto_intro`/`titulo` nullable/`lista_reglas` (v10.84), `responder_preguntas_abiertas` con destreza condicional (v10.85), individual vs parejas (v10.86). U0/U1/U2/U3 todas validando 0/0.
- **2026-05-08** — **B1.4 cerrado**: creado `unidades/nc1-curso.json` con índice editorial canónico del curso (10 unidades + apéndice), schema decidido y registrado como decisión 35 (Parte 4). Fuente: Scope and Sequence oficial del libro impreso, no `viejo/00-curso-general.md` (que tenía datos imprecisos). Contenido literal sin expansión MCER. Hallazgos no bloqueantes: páginas erróneas en md viejo, `contenidos_indice` de U1/U3 con "PARA APRENDER" mezclado en gramática (fix futuro de inventarios). Próximo: B1.5 (`nc1-reciclaje.json`).
- **2026-05-07 19:55** — **Limpieza documental v10.72-v10.77b cerrada** (último commit: `becaa69`, v10.77b; commit principal de la serie: `40c8a4c`, v10.77; ver detalle en `CHANGELOG.md`). Serie de commits que reduce el peso documental vivo del repo en ~32K tokens (-37%) sin perder trazabilidad: archivado del CHANGELOG pre-v10.40 a `docs/historico/`, traslado de árboles históricos y Parte 5.bis a `docs/historico/`, cierre de drift vivo en Parte 4 (taxonomía 17→20), Parte 3 (árbol actualizado), Parte 6 (Bloque A cerrado), reformulación de `PROCESO-MAESTRO:648` y compactación del Bloque A vivo de REVIEW. Cabeceras de fecha actualizadas. Bitácora cronológica intocada.
- **2026-05-07** — **Taxonomía de `tipo` ampliada de 19 a 20 valores: añadido `escucha`** (decisión cerrada en cumplimiento de la regla §2.4 de `reglas-operativas.md`: cualquier ampliación del set requiere decisión cerrada antes de aplicarse en schema y validador). Caso disparador detectado durante la prueba empírica con U0: la actividad U0-p8-act01 ("Mira el mapa y escucha el nombre de los países. Observa la pronunciación.") es input puro auditivo sin lectura de texto extenso ni acción posterior. La taxonomía de 19 no tenía un tipo limpio: `escucha_y_repite` exige repetición que el enunciado no pide; `lee_y_escucha` está pensado para diálogos (input combinado lectura+audio). Decisión: añadir `escucha` para input puro auditivo con apoyo visual no textual admisible (mapa, imagen, foto). Diferencia con `lee_y_escucha`: `escucha` no implica leer texto extenso. Aplicado en `schema-inventario.md` §5, `validar_inventario.py:TIPOS_VALIDOS`, `reglas-operativas.md` §2.2 (tabla canónica), todas las cross-references "19 → 20". U0-p8-act01 reclasificada `escucha_y_repite` → `escucha`. Validador U0 → 0/0.
- **2026-05-05** — Creación inicial. Consolida la conversación sobre el proceso de producción y el estado del repositorio.
- **2026-05-05** — Actualización con hallazgos del repaso del repositorio: los archivos `agentes/*.md` son especificaciones operativas vivas (no prompts a archivar). Protocolo de píldoras (Fase 5) localizado en `ag-vocabulario.md` y `ag-gramatica.md`. Confirmado que NO existe registro de no-repetición de tarjetas de estrategia (Fase 4).
- **2026-05-05** — Cierre de Fase 1: convención de naming (`UX-nc1-`, `nc1-` para globales, carpetas sin cero), material fuente reducido al PDF del libro del alumno, salidas (1 inventario por unidad + 3 globales del curso), modelo de globales = índice/proyección. Pendiente: esquema canónico del inventario y de los globales.
- **2026-05-05** — Añadida vista viva del árbol del repositorio (Parte 3). Definida estrategia de generación de los 4 JSONs: inventario por Claude Code con prompt versionado (no Python autónomo); tarjetas y píldoras globales por scripts Python deterministas; **reciclaje manual con Claude Code, NO automático**. Validación post-extracción por script Python.
- **2026-05-05** — Esquema canónico del `UX-nc1-inventario.json` cerrado. Cambios principales: `vocabulario_consolidado` con 3 bloques (principal/recurrente/comprensión), `secciones` como índice top-level, `tipo` con taxonomía cerrada de 17 valores (provisional, revisable), `datos` como saco genérico para datos específicos por actividad, `respuestas` siempre presente, eliminado `registro`. El dashboard ofrece una **vista HTML dinámica integrada** del inventario JSON (`web/index.html`); no existe actualmente un artefacto HTML estático adicional por unidad.
- **2026-05-05** — Estrategia de migración cerrada: zonas `nuevo/` (estructura definitiva en construcción, U3 como piloto) y "viejo" (resto del repo intacto). El dashboard NO se duplica.
- **2026-05-05** — Correcciones del revisor: (1) número de tipos de actividad corregido de "12" a "17" (lista real); (2) añadido caveat sobre la convención `UX` sin cero (válida solo para cursos de ≤9 unidades); (3) tarea HTML del informe anclada formalmente como pendiente abierta con responsable.
- **2026-05-05** — Esquemas de los 3 JSONs globales cerrados. Cambios respecto a borradores iniciales: `nc1-tarjetas.json` solo vocabulario y estrategia (sin gramática); `nc1-pildoras.json` con categorías marcadas como `null` para definir cuando se trabajen píldoras nuevas; `nc1-reciclaje.json` rediseñado como modelo acumulativo-secuencial, limitado a 5-6 elementos clave por unidad, basado en contenido (no en actividades), con tipos cerrados (vocabulario, estrategia, contenido_gramatical, tiempos_y_verbos, estrategia_comunicativa) y niveles de impacto. Anotado: el dashboard debe mostrar todos los JSON y permitir revisar/editar propuestas de reciclaje.
- **2026-05-05 12:15** — **Split físico ejecutado.** Todo el contenido editorial actual movido a `viejo/` (unidades, materiales, agentes, repertorios, referencias, diseno, material-complementario, _template, marco-teorico-metodologico.md, 00-curso-general.md). En raíz quedan: código (scripts, web, eval, diagrama.py), docs (README, CLAUDE, CHANGELOG, ROADMAP, GITHUB-MANIFEST, PROCESO-MAESTRO), config (Dockerfile, railway.toml, requirements.txt, .env.example), y la zona `nuevo/` (en construcción). Eliminada basura técnica: `texput.log`, `__pycache__/`, `.DS_Store`. Actualizadas referencias a paths nuevos en: `.gitignore`, `.dockerignore`, `scripts/importar_inventario.py`, `scripts/crear_crew_agents.py`, `diagrama.py` (8 referencias a repertorios), `README.md`, `CLAUDE.md`.
- **2026-05-05 12:30** — Commit `c5e08e9` "v10.0: split repo en zonas viejo/ y nuevo/ + PROCESO-MAESTRO" pusheado a `main`.
- **2026-05-05 14:00** — Dictamen del revisor sobre paso B (commit `67db6a4`): implementación correcta y completa, sin bloqueantes. Hallazgo cosmético registrado como B4 (`_normSeccion` no fusiona pestañas `(cont.)`); se resuelve en paso C sin acción separada.
- **2026-05-05 23:00** — **Terminología ELE aplicada en taxonomía de tipos (v10.25).** Renombrados 3 tipos en los 3 JSONs existentes (U0, U1, U3), el validador, el prompt y el CLAUDE.md de fase 1: `produccion_oral_pareja` → `interaccion_oral`, `produccion_oral_libre` → `expresion_oral_libre`, `produccion_escrita_libre` → `expresion_escrita_libre`. `produccion_escrita_guiada` se mantiene (correcto). Añadida regla de precedencia oral y distinción `completa_huecos` vs `produccion_escrita_guiada`.
- **2026-05-05 22:00** — **Bloque A cerrado. Decisiones sobre Bloque B.** A1 validado por el autor (U3 correcta). A3 cerrado: B1 pospuesto (inerte con CrewAI bloqueado), B2 aceptado (viejo sin trackear), B3 resuelto, B4 sin acción (cosmético). Bloque B parcializado: tarjetas espera fase 2, píldoras espera U3 vocabulario, reciclaje se diseña antes de implementar. Próximo paso: definir nc1-reciclaje.json y su visualización en dashboard.
- **2026-05-05 21:30** — **Rebajada la afirmación "arquitectura limpia" en CHANGELOG v10.17 tras dictamen del revisor.** El título original "arquitectura limpia" era demasiado fuerte: solo se limpió el diagrama mermaid_level1 (eliminada la caja `viejo/`), pero el código de `diagrama.py:550-557` sigue conteniendo referencias legacy a `viejo/repertorios/*.md` en el dict `AGENTS` usado por el flujo de agentes (ahora bloqueado). Título corregido a "diagrama activo sin caja viejo" + nota explícita sobre el alcance honesto.
- **2026-05-05 21:00** — **Dashboard refinado y arquitectura saneada.** Cambios visuales y conceptuales del dashboard: (1) sidebar reorganizado con 3 botones top-level en MAYÚSCULAS (INVENTARIOS, PROYECTO, AGENTES); el botón AGENTES queda BLOQUEADO (no en uso por ahora); el selector "Unidad" y la lista de secciones del flujo viejo de agentes quedan ocultos (`display:none`, no eliminados, por si se reactivan). (2) Diagrama "Arquitectura activa" — eliminada la caja `viejo/` para que el diagrama refleje solo el sistema activo. (3) Botones zoom +/- y "100%" añadidos sobre cualquier diagrama Mermaid (resuelve que algunos diagramas se vean pequeños). (4) Eliminadas 3 referencias residuales a `padStart(2,'0')` en vistas del flujo de agentes (líneas 1089, 1119, 1182) — aunque AGENTES está bloqueado, el código queda consistente con la convención sin cero. Cero `padStart` restantes en web/index.html.
- **2026-05-05 20:00** — **U0 extraído + 4 mejoras al sistema tras casos detectados.** Aplicadas tras validación del autor de v10.12: (1) Convención de naming actualizada en CLAUDE.md raíz, README.md, PROCESO-MAESTRO.md (decisión 9 + estructura): ahora dice `U0/, U1/, U2/...U9/` con U0 reservado a unidad introductoria atípica. (2) Prompt de fase 1 ampliado con sección "Reglas para unidades atípicas (introductorias)" — caso Punto de partida documentado con ejemplo. (3) Prompt ampliado con sección "Convención editorial: sílaba tónica subrayada hasta U3" — formato `_palabra_` en items_libro + nota aclaratoria, con distinción explícita de que en tarjetas (fase 3) aplica en todo el libro. (4) Prompt ampliado con sección "Patrón primer ítem resuelto como ejemplo" — `ejemplo_libro` vs `items_libro` vs `respuestas`. Pendiente del autor: confirmar con la editora si "limón" duplicado en U0 p.11 act.8 (items 7 y 8) es errata real del libro.
- **2026-05-05 19:30** — **Segunda pasada de saneamiento tras dictamen del revisor del v10.6.** (1) Vista viva del árbol (línea 456) corregida: el prompt activo es `fases/1-extraccion-inventario/prompt.md`, no `scripts/prompts/...`. (2) Referencias operativas a `unidades/U03/` y archivos `U03-*.md` en Fases 4, 5 y 6 reescritas para reflejar que ese contenido vive en `viejo/unidades/U03/` (sistema antiguo); el sistema activo en raíz tiene `unidades/U3/` con solo inventario + fuente. (3) Línea colgante eliminada al final de Parte 6 (`- Eliminar viejo/ y PROCESO-MAESTRO.md.` que quedó tras simplificar). (4) "Cambios físicos pendientes" reescritos como histórico (los renombrados ya están hechos). El maestro ahora sí refleja el estado real del repositorio.
- **2026-05-05 19:00** — **Limpieza de contradicciones en PROCESO-MAESTRO.md tras dictamen del revisor.** Actualizadas referencias stale a `nuevo/` y a `scripts/prompts/extraccion-inventario.md` en Partes 4, 5, 5.bis y 6 (las que describen estado actual). Mantenidas las referencias en bitácora (cronológicas). Parte 5.bis reescrita reflejando que `nuevo/` se disolvió. Parte 6 simplificada: el plan vivo está en REVIEW.md, evitar duplicación. REVIEW.md timestamp actualizado a 18:30. Maestro vuelve a ser fuente de verdad operativa coherente.
- **2026-05-05 18:30** — **CLAUDE.md raíz reducido a 85 líneas (luego 99 con sección "Cómo invocar una fase").** Aplicado estrictamente Anthropic best practices: CLAUDE.md solo contiene reglas/convenciones/comandos para trabajar HOY en el repo. Eliminado: modelo conceptual abstracto (vive en PROCESO-MAESTRO Parte 1), tabla de 8 fases con estado (vive en README.md y PROCESO-MAESTRO Parte 2), "estado actual" (vive en REVIEW.md). Añadida regla explícita en "Lo que NO se hace": no añadir historia/estado/planes/meta-decisiones a CLAUDE.md.
- **2026-05-05 18:00** — **Arquitectura confirmada (datos centralizados + instrucciones modulares).** El autor pregunta si conviene duplicar datos por fase para ahorrar tokens. Se descarta basándose en buenas prácticas: viola la Regla de Oro #5 (una fuente única) y no aporta ahorro real (CLAUDE.md modular ya carga solo el contexto relevante; los datos no se cargan automáticamente, solo cuando Claude Code los lee explícitamente). Estructura confirmada: datos en `unidades/UX/` (única ubicación), instrucciones en `fases/N-X/CLAUDE.md` + `prompt.md` (modulares por fase). Optimizaciones reales de tokens disponibles: prompts compactos con ejemplos, `Read` con offset/limit en JSONs grandes, sesiones limpias por fase (Ctrl+L).
- **2026-05-05 16:30** — **CLAUDE.md global creado** en raíz. 196 líneas. Cubre: qué es el proyecto, estructura del repo, modelo conceptual, las 8 fases con estado, 6 reglas de oro (texto verbatim, no transformar, validar, no inventar, fuente única, no tocar viejo), convenciones de naming, esquema canónico del JSON resumido, taxonomía cerrada de 17 tipos, comandos útiles, cómo invocar la extracción, mejora continua, lo que NO se hace, estado actual. Sin referencias a viejo (solo para decir que no se toca).
- **2026-05-05 16:15** — **Validador funcionando desde raíz**: `python3 scripts/validar_inventario.py 3` → ✅ JSON válido. CONTENIDOS_VISIBLES ampliado con `expresiones_dadas` y `definiciones`. Dashboard limpio: una sola tarjeta U3 (sin tag ACTIVO/VIEJO, leyendo solo de `unidades/`).
- **2026-05-05 16:00** — **Disolución de `nuevo/`.** El contenido pasa a raíz directamente (decisión del autor: evitar futuros renombrados de path). Movimientos: `nuevo/unidades/U3/` → `unidades/U3/`; `nuevo/scripts/prompts/` → `scripts/prompts/`; `nuevo/scripts/validar_inventario.py` → `scripts/validar_inventario.py`. CLAUDE.md anterior movido a `viejo/CLAUDE-anterior.md`. Scripts antiguos del CrewAI v5 movidos a `viejo/scripts/` (`importar_inventario.py`, `crear_crew_agents.py`, `probar_modelos.py`, `crewai/`, `resultados_prueba/`). Dashboard (`diagrama.py`, `web/`, `eval/`) se mantiene en raíz como infraestructura activa que sirve a ambas zonas. Renombrada la zona "nuevo" a "activo" en el dashboard. Paths internos actualizados en JSON, scripts, .gitignore, .dockerignore, README.md.
- **2026-05-05 14:00** — Dictamen del revisor sobre paso B (commit `67db6a4`): implementación correcta y completa, sin bloqueantes. Hallazgo cosmético registrado como B4 (`_normSeccion` no fusiona pestañas `(cont.)`); se resuelve en paso C sin acción separada.
- **2026-05-05 13:30** — Hallazgos del revisor sobre el split aceptados. Documentados como bugs conocidos B1 (`tools.py:346` escribe a path inexistente), B2 (Railway: `repertorios/` ya estaba gitignored antes del split, dashboard llevaba roto), B3 (`diagrama.py:715` con path hardcoded a inventario antiguo). Decisión: NO arreglar ahora, abordar los 3 al inicio del paso C cuando los paths en `nuevo/` estén fijados.
- **2026-05-05 13:00** — Auditoría y actualización del documento. Correcciones: (1) entrada de bitácora con "12 tipos" → "17 tipos" (consistencia interna); (2) Parte 4 reescrita con las **26 decisiones cerradas** organizadas por categoría (modelo, organización, naming, JSONs, generación, dashboard); (3) Parte 5 (pendientes) limpiada — eliminados los esquemas JSON que ya estaban cerrados, añadida sección de "implementación pendiente"; (4) Parte 5.bis reescrita reflejando que el split YA está ejecutado (no es plan futuro); (5) Parte 6 reescrita con estado real de cada paso (A hecho, B próximo, C-F pendientes); (6) árbol "antes del split" marcado como histórico para evitar confusión.
- **2026-05-06 14:30** — **Refactor documental de fase 1 aprobado** tras 6 rondas de revisión sobre `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md` (v10.35→v10.39). Parte 4 ampliada con 7 nuevas decisiones cerradas (28-34) que fijan: arquitectura objetivo de 5 archivos, frontera de capas no negociable (forma vs decisión), single source of truth de precedencias en `reglas-operativas.md`, skill fuera de v1, contrato paralelo schema↔validador con prerequisito de no divergencia en el merge, y delegación del plan ejecutable a REFACTOR-PROPUESTA.md como source of truth operativa. La ejecución se trackea en REVIEW como paso A4 con sub-pasos A4.0→A4.6 (incluido A4.5.5 cross-check obligatorio). No se ha tocado código todavía.
- **2026-05-06 15:00** — **Fix de coherencia documental** tras dictamen del revisor: eliminada numeración duplicada de "Decisión 27" (existía una en Parte 4 nueva y otra en Parte 5 bajo "Decisiones cerradas adicionales (post-creación inicial)"). El bloque Arquitectura datos+instrucciones se ha movido a Parte 4 como subsección propia (donde corresponde por estar cerrada) preservando su número 27 por antigüedad; las decisiones del refactor de fase 1 se renumeran de 27-33 a 28-34. Eliminado el subheader "Decisiones cerradas adicionales (post-creación inicial)" de Parte 5 porque era contradictorio con el título "Decisiones pendientes" de la propia Parte 5.
