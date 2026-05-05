# Proceso Maestro — Documento de trabajo

> **Estado:** documento temporal. Consolida el proceso completo de producción de una unidad didáctica, lo que está definido y lo que falta por definir. Sirve de fuente para reorganizar el repositorio y, una vez integrada esta información en CLAUDE.md, README.md y los documentos de cada sección, **se eliminará**.
>
> **Origen:** conversación con el autor el 2026-05-05 para evitar perder el proceso completo descrito en chat.
>
> **Cómo se usa:** lectura obligada antes de cualquier reorganización del repo. Se actualiza conforme se rellenan huecos o se cierran decisiones.

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
3. Validación automática del JSON con `scripts/validar_inventario.py` (a escribir).
4. Validación visual fuente vs JSON (revisión de 2-3 páginas al azar).
5. `python scripts/importar_inventario.py unidades/UX/UX-nc1-inventario.json` → carga a BD (idempotente, DELETE CASCADE).
6. Tras desarrollar la unidad, regenerar `nc1-tarjetas.json` y `nc1-pildoras.json` con scripts Python deterministas.
7. Cierre de unidad: actualizar `nc1-reciclaje.json` manualmente con ayuda de Claude Code en chat (no automático).
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

**D) `nc1-reciclaje.json` — mapping de reciclaje cross-unidad** ⚠ **IMPORTANTE: manual, no automático**
- **Quién:** Claude Code en chat, ayudando al autor. **NO se genera con script Python**, **NO se infiere automáticamente, NO se "regenera"**.
- **Cómo:** el autor abre chat al cerrar cada unidad y dice "añade los reciclajes de UX". Claude Code pregunta qué contenido se reutiliza, lo añade a las entradas existentes del JSON. El archivo es **acumulativo**: cada cierre de unidad lo amplía.
- **Por qué manual:** el reciclaje es un mapping editorial (qué contenido de una unidad se reutiliza en otra) que requiere criterio humano. Un script no puede inferirlo de forma fiable.
- **Coste:** mínimo, ~5.000 tokens por unidad.
- **Futuro:** cuando los agentes CrewAI estén configurados, se podrá evaluar si un agente propone reciclajes (que el autor valida). Hoy: solo manual con Claude Code.

---

**Validación post-generación:**
- Después de cada extracción, `scripts/validar_inventario.py` (a escribir) verifica estructura: campos obligatorios, tipos, códigos de actividad únicos, JSON parseable. Esto SÍ es trabajo de Python (validación estructural pura, sin riesgo de fallar).

---

---

**Esquema canónico del `UX-nc1-inventario.json` (CERRADO en chat 2026-05-05):**

Estructura top-level (10 claves):
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
- `paginas_detalle` (array): lista de páginas con su detalle.

Estructura por página:
- `pagina` (int).
- `seccion` (str): clave normalizada (vocabulario, gramatica, comunicacion, destrezas, cultura, evaluacion, reflexion).
- `actividades` (array).
- `cuadros_gramaticales` (array, opcional).

**REGLA DURA — Literalidad del contenido visible al alumno.** Cada actividad debe contener el **texto exacto** que el alumno lee en el libro, no resúmenes ni referencias. La instrucción va en `instruccion_original` (literal). Todo el contenido visible adicional (frases con huecos, listas de items, opciones múltiples, diálogos completos, textos de lectura, definiciones, palabras dadas en recuadro, ejemplos del libro) va en `datos` con campos descriptivos (`items_libro`, `frases`, `dialogo_completo`, `texto_completo`, `opciones`, `palabras_recuadro`, etc.). **Nunca reemplazar texto del libro por una descripción** ("el alumno lee 4 frases"); siempre incluir las 4 frases literales. Si la actividad presenta huecos, marcarlos con `_____`. Razón: la fidelidad al libro es la base de toda explotación didáctica posterior; sin ella, el agente no puede generar contenido coherente.

Estructura por actividad:
- `id` (str): único, formato `UX-pYY-actNN`.
- `numero` (int): orden en la unidad.
- `tipo` (str): de la **taxonomía cerrada de 17 tipos** (lista provisional, se revisa al cerrar cada unidad nueva):
  ```
  escucha_y_repite, escucha_y_responde, completa_huecos, relaciona, ordena, clasifica,
  seleccion_multiple, verdadero_falso, produccion_oral_pareja, produccion_oral_libre,
  produccion_escrita_guiada, produccion_escrita_libre, comprension_lectora,
  comprension_auditiva, busqueda_informacion, tarea_final, juego
  ```
- `destreza` (str): destreza(s) trabajada(s).
- `instruccion_original` (str): texto literal del libro.
- `contenido_linguistico` (array de strings).
- `campo_semantico` (str, opcional): cuando aplica (actividades de vocabulario).
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
- **Acumulativo y secuencial:** cada unidad analiza qué reutiliza de las anteriores, NO se recicla todo, **solo 5-6 elementos clave** de mayor impacto.
- **Basado en contenido**, no en actividades.
- **Se decide al cerrar cada unidad** (al final). Manual con Claude Code en chat.
- **Revisable y editable desde el dashboard.**
- Top-level: `curso`, `actualizado`, `reciclajes_por_unidad`, `indice_por_tipo`.
- Por unidad: `_meta` (fecha cierre, total) + `elementos` (lista de objetos con `id`, `tipo`, `origen`, `uso_en_unidad_actual`, `impacto`).
- Tipos cerrados (provisionales, ampliables):
  - `vocabulario`
  - `estrategia` (de aprendizaje)
  - `contenido_gramatical`
  - `forma_verbal`
  - `estrategia_comunicativa`
- Niveles de impacto: `alto` / `medio` / `bajo`.

---

**Por definir todavía:**
- Contenido del prompt `fases/1-extraccion-inventario/prompt.md` (escrito y operativo).
- Scripts Python: `validar_inventario.py`, `regenerar_tarjetas_globales.py`, `regenerar_pildoras_globales.py`.
- Protocolo formal de validación visual PDF vs JSON.
- **Plantilla HTML del informe por unidad** y su integración en el dashboard.
  - **Tarea formal pendiente:** definir la plantilla HTML (estructura, secciones, colores, qué muestra). Integrar como sección nueva del dashboard (`web/index.html`). Se aborda en el paso B del plan de trabajo (después de cerrar los esquemas de los 3 JSONs globales).
  - **Debe mostrar:** JSON de cada unidad (vocabulario consolidado, secciones, actividades) + los 3 JSON globales (tarjetas, píldoras, reciclaje) + propuestas de reciclaje al cerrar una unidad (revisables y editables).
  - **Responsable:** Claude Code en chat con el autor.
  - **Estado:** abierta, sin empezar.
- **Categorías de píldoras formativas:** definir cuando se trabaje en las primeras píldoras nuevas. Pendiente de revisión en este documento.

**Cambios físicos** (HISTÓRICO — ya ejecutados):
- ✅ Inventario de U03 promocionado a `unidades/U3/U3-nc1-inventario.json` (raíz). El `viejo/unidades/U03/inventario.json` se conserva como archivo.
- ✅ PDF promocionado a `unidades/U3/fuente/U3-nc1.pdf` (raíz, gitignored).
- ✅ Las 10 referencias internas del JSON ya apuntan a la nueva ruta.
- 📋 PENDIENTE (cuando proceda): el resto del contenido editorial de U03 (tarjetas/, pildoras/, secciones MD) sigue solo en `viejo/unidades/U03/` y se evaluará migrar al sistema activo cuando se construyan las fases 3-7.
- Actualizar referencias en scripts (`importar_inventario.py`, `crear_crew_agents.py`, `diagrama.py`), CLAUDE.md, README.md, .gitignore, .dockerignore.
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

> **NOTA:** esta sección es una **vista viva** del árbol del repositorio. Se actualiza con cada cambio físico. Última actualización: 2026-05-05 (disolución de `nuevo/`: el sistema activo vive en raíz).

### Árbol actual (estado físico real, hoy)

```
guia-didactica-profesor-IA/
│
├── unidades/                                ← SISTEMA ACTIVO (nuevo)
│   └── U3/                                  (única poblada)
│       ├── U3-nc1-inventario.json           (47 actividades, schema canónico)
│       ├── fuente/U3-nc1.pdf                (gitignored)
│       └── (resto pendiente de migrar de viejo si procede)
│
├── fases/                                   ← una carpeta por fase con CLAUDE.md + prompt
│   └── 1-extraccion-inventario/
│       ├── CLAUDE.md                        (contexto operativo de la fase)
│       └── prompt.md                        (instrucciones detalladas)
├── scripts/                                 ← código activo
│   └── validar_inventario.py                (validación estructural sin LLM)
│
├── eval/                                    ← evaluación (heredado, en uso)
├── web/                                     ← dashboard (heredado, en uso)
├── diagrama.py                              ← servidor (heredado, en uso)
│
├── viejo/                                   ← ARCHIVO CrewAI v5.0 (intocable)
│   ├── unidades/U03/                        (contenido editorial original)
│   ├── materiales/, agentes/, repertorios/, referencias/, diseno/, _template/
│   ├── scripts/                             (importar_inventario.py, crewai/, etc.)
│   ├── CLAUDE-anterior.md                   (CLAUDE.md anterior)
│   ├── marco-teorico-metodologico.md, 00-curso-general.md
│   └── material-complementario/             (gitignored)
│
├── .claude/rules/                           (meta-reglas técnicas: agent-prompt-design, tool-design, etc.)
├── README.md, CHANGELOG.md, ROADMAP.md, GITHUB-MANIFEST.md
├── PROCESO-MAESTRO.md                       ← este documento (temporal)
├── Dockerfile, railway.toml, requirements.txt, .env.example
└── .gitignore, .dockerignore
```

### Árbol intermedio (estado anterior — pre-disolución de `nuevo/`)

```
guia-didactica-profesor-IA/
│
├── viejo/                                       ← contenido editorial actual sin tocar
│   ├── unidades/U03/                            (única poblada en aquel momento)
│   ├── materiales/                              (1 archivo: especificaciones-diseno-tarjetas.md)
│   ├── agentes/                                 (7 ag-*.md + 4 resumen-configuracion-*.md)
│   ├── repertorios/                             (6 bancos por sección)
│   ├── referencias/                             (12 documentos de técnicas)
│   ├── diseno/                                  (propuestas con versiones)
│   ├── material-complementario/                 (gitignored, ~21 MB)
│   ├── _template/                               (origen desconocido)
│   ├── marco-teorico-metodologico.md
│   └── 00-curso-general.md
│
├── nuevo/                                       ← estructura definitiva en construcción
│   ├── README.md
│   ├── unidades/U3/                             (vacía, esperando migración)
│   └── scripts/prompts/                         (vacía, pendiente extraccion-inventario.md)
│
├── scripts/                                     ← código activo (raíz)
│   ├── importar_inventario.py
│   ├── crear_crew_agents.py
│   ├── probar_modelos.py
│   └── crewai/{recurvo.py, tools.py, tool_versions.json}
│
├── web/                                         ← dashboard activo (raíz)
│   ├── index.html (90 KB)
│   └── favicon.svg
├── diagrama.py                                  ← servidor del dashboard (raíz, mal nombrado)
│
├── eval/                                        ← evaluación (raíz)
│   ├── evaluar_tarjetas.py
│   ├── provider_crewai.py
│   └── promptfoo.yaml
│
├── .claude/
│   ├── rules/{agent-prompt-design.md, tool-design.md, criterios-generacion-tarjetas.md, criterios-generacion-texto.md}
│   └── settings.json
│
├── README.md, CLAUDE.md, CHANGELOG.md, ROADMAP.md, GITHUB-MANIFEST.md
├── PROCESO-MAESTRO.md                           ← este documento (temporal)
├── Dockerfile, railway.toml, requirements.txt, .env.example
└── .gitignore, .dockerignore
```

### Árbol antes del split (referencia histórica — anterior a 2026-05-05 12:15, NO ES EL ESTADO ACTUAL)

```
guia-didactica-profesor-IA/
├── unidades/
│   ├── U03/                                    ← única unidad poblada
│   │   ├── inventario.json                     (pendiente renombrar a U3-nc1-inventario.json)
│   │   ├── fuente/
│   │   │   └── U03-libro.pdf                   (pendiente renombrar a U3-nc1.pdf)
│   │   ├── tarjetas/{csv,diseno,validacion}/
│   │   ├── pildoras/                           (10 PDFs + 10 TEX)
│   │   └── U03-{vocabulario,gramatica,...}.md  (16 MDs por sección + variantes)
│   ├── U01/, U02/                              (solo placeholder MD; carpetas internas creadas)
│   └── U04/, U05/, ... U09/                    (solo placeholder MD; carpetas internas creadas)
│
├── .claude/
│   ├── rules/
│   │   ├── agent-prompt-design.md              (meta-regla técnica, protegida)
│   │   ├── tool-design.md                      (meta-regla técnica, protegida)
│   │   ├── criterios-generacion-tarjetas.md    (criterio editorial — mezcla mal con meta-reglas)
│   │   └── criterios-generacion-texto.md       (criterio editorial — mezcla mal con meta-reglas)
│   └── settings.json
│
├── agentes/                                     ← 7 archivos: especificaciones operativas vivas
│   ├── ag-vocabulario.md                       (35 KB — incluye banco de píldoras)
│   ├── ag-gramatica.md                         (18 KB — incluye banco de píldoras)
│   ├── ag-comunicacion.md                      (29 KB)
│   ├── ag-destrezas.md                         (30 KB)
│   ├── ag-cultura.md                           (22 KB)
│   ├── ag-evaluacion.md                        (16 KB)
│   ├── orquestador.md                          (7.5 KB)
│   └── resumen-configuracion-*.md              (4 archivos, 24-31 KB cada uno)
│
├── repertorios/                                 ← 6 bancos de técnicas por sección
│   ├── vocabulario.md, gramatica.md, comunicacion.md
│   ├── destrezas.md, cultura.md, evaluacion.md
│
├── referencias/                                 ← 12 documentos de técnicas detalladas
│   ├── repertorio-120-tecnicas-EIO.md
│   ├── repertorio-124-tecnicas-CA.md
│   ├── analisis-100-tecnicas-CL.md
│   ├── analisis-84-estrategias-EE.md
│   └── ... (8 más)
│
├── materiales/                                  ← solo 1 archivo (queda casi vacía)
│   └── especificaciones-diseno-tarjetas.md     (162 líneas, desactualizado desde abril)
│
├── scripts/
│   ├── importar_inventario.py                  (JSON → BD)
│   ├── crear_crew_agents.py
│   ├── probar_modelos.py
│   ├── crewai/
│   │   ├── recurvo.py                          (orquestador CrewAI)
│   │   ├── tools.py                            (6 tools, protegida)
│   │   └── tool_versions.json
│   └── resultados_prueba/                      (basura: salidas viejas)
│
├── web/
│   ├── index.html                              (dashboard Material Design 3)
│   └── favicon.svg
├── diagrama.py                                  ← servidor web mal nombrado, suelto en raíz
│
├── eval/
│   ├── evaluar_tarjetas.py                     (5 métricas DeepEval)
│   ├── provider_crewai.py                      (wrapper promptfoo)
│   └── promptfoo.yaml
│
├── diseno/                                      ← propuestas con versiones (poco claro qué es vigente)
│
├── material-complementario/                     (gitignored, solo local, ~21 MB)
├── _template/                                   (sin trackear, propósito desconocido)
│
├── marco-teorico-metodologico.md                ← suelto en raíz
├── 00-curso-general.md                          ← suelto en raíz
├── README.md, CLAUDE.md, CHANGELOG.md, ROADMAP.md, GITHUB-MANIFEST.md
├── PROCESO-MAESTRO.md                           ← este documento (temporal)
├── Dockerfile, railway.toml, requirements.txt, .env.example
├── .gitignore, .dockerignore
└── BASURA TÉCNICA: texput.log, __pycache__/, .DS_Store, eval/__pycache__/
```

### Notas históricas adicionales (anteriores al split)

> Lo siguiente describe cambios previos al split de zonas `viejo/` + `nuevo/`. Ya está reflejado en el árbol actual de arriba. Se conserva como contexto.

```
guia-didactica-profesor-IA/
├── unidades/                       ← contenido editorial (U03 migrado, resto placeholders)
├── .claude/rules/                  ← 4 archivos: 2 meta-reglas + 2 criterios editoriales (mezcla)
├── materiales/                     ← solo 1 archivo (especificaciones-diseno-tarjetas.md)
├── scripts/                        ← código Python
├── web/                            ← dashboard
├── eval/                           ← evaluación
├── repertorios/                    ← 6 repertorios por sección
├── referencias/                    ← 12 documentos de técnicas
├── agentes/                        ← 11 prompts MD de agentes (referencia, no ejecutable)
├── diseno/                         ← documentos de diseño con versiones
├── pedagogia/                      ← (no existe todavía)
├── _template/                      ← carpeta sin trackear, propósito desconocido
├── material-complementario/        ← solo local (gitignored)
├── marco-teorico-metodologico.md   ← suelto en raíz
├── 00-curso-general.md             ← suelto en raíz
├── diagrama.py                     ← servidor web suelto en raíz (mal nombrado)
├── README.md, CLAUDE.md, CHANGELOG.md, ROADMAP.md, GITHUB-MANIFEST.md
└── Dockerfile, railway.toml, requirements.txt, .env.example
```

### Problemas conocidos

- `.claude/rules/` mezcla meta-reglas técnicas con criterios editoriales.
- `materiales/` quedó casi vacía (1 archivo).
- `repertorios/` y `referencias/` solapan parcialmente sin jerarquía.
- **`agentes/*.md` son especificaciones operativas vivas, no "prompts viejos".** Contienen protocolos por sección (banco de píldoras, criterios de selección, ciclo de fases). Son referencia activa para Claude Code, no material a archivar. Esto invalida la idea anterior de moverlos a `pedagogia/agentes-prompts-referencia/`.
- Marco teórico y curso general están sueltos en raíz.
- `diagrama.py` es realmente el servidor web (mal nombrado).
- Hay basura técnica: `texput.log`, `__pycache__/`, `.DS_Store`, `scripts/resultados_prueba/`.
- `_template/` sin trackear, propósito por confirmar.

### Hallazgo importante sobre los archivos `agentes/*.md`

Tras revisar contenido, los 7 archivos `ag-*.md` (vocabulario, gramática, comunicación, destrezas, cultura, evaluación, orquestador) **son los documentos más densos del proyecto en cuanto a protocolo operativo**. Cada uno mezcla:

- Configuración de un agente CrewAI (rol, objetivo, tarea).
- Criterios pedagógicos de su sección (qué hacer, en qué orden, con qué técnicas).
- Bancos de acciones reutilizables (la Fase 5 vive aquí, dispersa).
- Referencias a marcos teóricos (Conti, MARS EARS, Gagné, VanPatten).

Esto significa que la **especificación por sección** que estábamos buscando ya existe parcialmente: está dentro de `ag-*.md`. La reorganización debe **separar dos cosas mezcladas en cada archivo**:
- La parte que es **especificación operativa de la sección** (criterios, protocolos, bancos) → debe ir a `especificaciones/SECCION/`.
- La parte que es **configuración del agente CrewAI** (rol, prompt, tools) → debe ir a `scripts/crewai/` o a la BD `crew_agents`.

Esto es una decisión de diseño todavía no tomada. Va a la Parte 5 como pendiente nueva.

---

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
17. **Esquema del inventario JSON cerrado**: `vocabulario_consolidado` con 3 bloques (principal/recurrente/comprensión), `secciones` como índice top-level, `tipo` con taxonomía cerrada de 17 valores (provisional, revisable cada unidad), `datos` como saco genérico, `respuestas` siempre presente, sub-objetos consistentes para audio/imagen/video, `registro` eliminado (va a CHANGELOG).
18. **Esquema de `nc1-tarjetas.json`**: solo vocabulario y estrategia (no gramática). `por_unidad` + `indice_palabras` + `indice_estrategias`.
19. **Esquema de `nc1-pildoras.json`**: `por_unidad` + `indice_global`. Categorías como `null` por ahora — se definen cuando se trabajen píldoras nuevas.
20. **Esquema de `nc1-reciclaje.json`**: acumulativo y secuencial; limitado a 5-6 elementos clave por unidad; basado en contenido (vocabulario, estrategia, contenido_gramatical, forma_verbal, estrategia_comunicativa); con niveles de impacto (alto/medio/bajo); revisable y editable desde el dashboard.

### Sobre la generación de los JSONs
21. **`UX-nc1-inventario.json`**: lo genera **Claude Code** en chat con un **prompt versionado** (`fases/1-extraccion-inventario/prompt.md`, operativo). NO Python autónomo.
22. **`nc1-tarjetas.json`** y **`nc1-pildoras.json`**: scripts Python deterministas (`regenerar_tarjetas_globales.py`, `regenerar_pildoras_globales.py`, a escribir). Cero tokens.
23. **`nc1-reciclaje.json`**: **manual con Claude Code** en chat al cerrar cada unidad. NO automático, NO inferido por script. Acumulativo.
24. **Validación post-extracción** del inventario: script Python `validar_inventario.py` (a escribir).

### Sobre el dashboard y el informe HTML
25. **Cada extracción de inventario genera además un informe HTML visual** integrado como sección nueva del dashboard existente (`web/index.html`).
26. **El dashboard debe mostrar** todos los JSON (inventario por unidad + 3 globales) y permitir revisar/editar las propuestas de reciclaje al cerrar cada unidad.

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

### Decisiones cerradas adicionales (post-creación inicial)

**Decisión 27 — Arquitectura datos+instrucciones (cerrada 2026-05-05).**
- **Datos centralizados** en `unidades/UX/` — única ubicación canónica de inventario, tarjetas, píldoras, secciones de cada unidad.
- **Instrucciones modulares** en `fases/N-X/` — cada fase tiene su `CLAUDE.md` (contexto operativo) + `prompt.md` (instrucciones detalladas).
- **NO se duplican datos por fase**, aunque se busque ahorro de tokens. Razones: (1) viola Regla de Oro #5 (una fuente única); (2) CLAUDE.md modular ya carga solo el contexto relevante; (3) los datos no se cargan automáticamente, solo cuando Claude Code los lee explícitamente con `Read`.
- **Optimizaciones de tokens reales:** prompts compactos con ejemplos, `Read` con offset/limit en JSONs grandes, sesiones limpias por fase.

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

### Bugs conocidos / deuda técnica (bloqueantes del paso C, no del paso B)

Detectados por revisor el 2026-05-05. Decisión del autor: **NO arreglar ahora**, abordar todos juntos al inicio del paso C cuando los paths definitivos estén fijados.

- **B1 — `tools.py:346` escribe a path inexistente.** La tool `exportar_csv` (en `viejo/scripts/crewai/tools.py`) intenta escribir en `datos/tarjetas/U{XX}-vocabulario.csv`. Esa carpeta no existe en el repo. Bug preexistente desde v9.0. **Funcionalmente: `exportar_csv` está rota en producción.** Como el sistema activo no usa esta tool (vive en `viejo/`), el bug es inerte. Requiere decisión cuando se evalúe si reactivar parte de CrewAI.

- **B2 — Railway: `viejo/repertorios/` no existe en el repo remoto.** `repertorios/` está gitignored. El dashboard (`diagrama.py`) lee `viejo/repertorios/X.md` para mostrar líneas en algunos diagramas. En Railway no funciona. Decisión pendiente: trackear los repertorios en git, desactivar esa lectura en producción, o migrar al sistema activo en raíz.

- **B3 — `diagrama.py:715` tiene path hardcoded.** Verificar tras disolución de `nuevo/`: la línea debería apuntar a `unidades/U3/U3-nc1-inventario.json` (raíz). Si todavía apunta a `viejo/unidades/U03/inventario.json`, actualizar.

- **B4 — `_normSeccion` en `web/index.html` no fusiona secciones `(cont.)`.** La función parte por "—" y toma la primera parte. Con strings como "Comunicación (cont.) — La hora", el "(cont.)" va antes del separador, así que se genera una pestaña aparte de "Comunicación". Resultado: 7 pestañas en lugar de 5 para U3, con "Comunicación" / "Comunicación (cont.)" y "Destrezas" / "Destrezas (cont.)" separadas. **Cosmético, no bloqueante.** Se resuelve solo en paso C cuando las secciones pasan a claves normalizadas (`vocabulario`, `gramatica`, `comunicacion`...) en el nuevo schema y `_normSeccion` se elimina.

### Sobre la implementación (a escribir cuando lleguemos)
- (Eliminado: el prompt `fases/1-extraccion-inventario/prompt.md` ya está escrito y operativo.)
- Scripts Python: `validar_inventario.py`, `regenerar_tarjetas_globales.py`, `regenerar_pildoras_globales.py`.
- Plantilla HTML del informe por unidad e integración en dashboard (paso B del plan).
- (Eliminado: la migración de U3 al nuevo schema ya se hizo en raíz; no aplica).
- Protocolo formal de validación visual PDF vs JSON.

---

---

## Parte 5.bis — Histórico de la estrategia de migración (CERRADA)

**Cronología:**
- **2026-05-05 12:15** — Split ejecutado: contenido editorial movido a `viejo/`; carpeta `nuevo/` creada como zona de construcción.
- **2026-05-05 16:00** — `nuevo/` **disuelta**: su contenido se promocionó a raíz directamente (decisión del autor para evitar futuros renombrados).

### Estado actual del repositorio (post-disolución)
- **`viejo/`** existe en la raíz. Contiene el sistema CrewAI v5 anterior y materiales editoriales originales. Solo local (gitignored). Intocable hasta su eliminación final.
- **El sistema activo vive en raíz**: `unidades/`, `scripts/`, `fases/`, `web/`, `diagrama.py`, `eval/`.
- **Documentos en raíz**: `CLAUDE.md`, `README.md`, `CHANGELOG.md`, `PROCESO-MAESTRO.md`, `REVIEW.md`, `ROADMAP.md`, `GITHUB-MANIFEST.md`.
- **Config en raíz**: `Dockerfile`, `railway.toml`, `requirements.txt`, `.env.example`, `.gitignore`, `.dockerignore`.

### Limpieza final pendiente (cuando todas las fases estén operativas)
Ver bloque E del `REVIEW.md`. En resumen:
1. Migrar de `viejo/` lo aprovechable (criterio caso por caso).
2. Eliminar `viejo/`.
3. Eliminar `PROCESO-MAESTRO.md` y `REVIEW.md` (integrar su contenido en `CLAUDE.md`, `README.md` y CLAUDE.md por fase).

---

## Parte 6 — Pasos siguientes (estado y plan)

### Hitos cerrados (cronológico — actualizado 2026-05-05 19:00)
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

- ✅ **Bloques operativos cerrados:** esquemas JSON, vista HTML, extracción de U3 con nuevo schema, prompt versionado, validador, disolución de `nuevo/`, CLAUDE.md modular.
- 📋 **Bloque A pendiente** (REVIEW): estabilizar fase 1 (validar U3, probar U4, resolver bugs B1-B4).
- 📋 **Bloque B pendiente:** infraestructura JSONs globales del curso.
- 📋 **Bloque C pendiente:** construir fases 2-8 (una a una).
- 📋 **Bloque D pendiente:** sistema de lecciones de Claude Code.
- 📋 **Bloque E pendiente** (al cierre del curso): limpieza final, eliminar `viejo/`, eliminar `PROCESO-MAESTRO.md` y `REVIEW.md`.

Detalle paso a paso con condiciones de cierre: ver `REVIEW.md`.

---

## Bitácora del documento

- **2026-05-05** — Creación inicial. Consolida la conversación sobre el proceso de producción y el estado del repositorio.
- **2026-05-05** — Actualización con hallazgos del repaso del repositorio: los archivos `agentes/*.md` son especificaciones operativas vivas (no prompts a archivar). Protocolo de píldoras (Fase 5) localizado en `ag-vocabulario.md` y `ag-gramatica.md`. Confirmado que NO existe registro de no-repetición de tarjetas de estrategia (Fase 4).
- **2026-05-05** — Cierre de Fase 1: convención de naming (`UX-nc1-`, `nc1-` para globales, carpetas sin cero), material fuente reducido al PDF del libro del alumno, salidas (1 inventario por unidad + 3 globales del curso), modelo de globales = índice/proyección. Pendiente: esquema canónico del inventario y de los globales.
- **2026-05-05** — Añadida vista viva del árbol del repositorio (Parte 3). Definida estrategia de generación de los 4 JSONs: inventario por Claude Code con prompt versionado (no Python autónomo); tarjetas y píldoras globales por scripts Python deterministas; **reciclaje manual con Claude Code, NO automático**. Validación post-extracción por script Python.
- **2026-05-05** — Esquema canónico del `UX-nc1-inventario.json` cerrado. Cambios principales: `vocabulario_consolidado` con 3 bloques (principal/recurrente/comprensión), `secciones` como índice top-level, `tipo` con taxonomía cerrada de 17 valores (provisional, revisable), `datos` como saco genérico para datos específicos por actividad, `respuestas` siempre presente, eliminado `registro`. Cada extracción genera además un **informe HTML visual** integrado en el dashboard existente (`web/index.html`).
- **2026-05-05** — Estrategia de migración cerrada: zonas `nuevo/` (estructura definitiva en construcción, U3 como piloto) y "viejo" (resto del repo intacto). El dashboard NO se duplica.
- **2026-05-05** — Correcciones del revisor: (1) número de tipos de actividad corregido de "12" a "17" (lista real); (2) añadido caveat sobre la convención `UX` sin cero (válida solo para cursos de ≤9 unidades); (3) tarea HTML del informe anclada formalmente como pendiente abierta con responsable.
- **2026-05-05** — Esquemas de los 3 JSONs globales cerrados. Cambios respecto a borradores iniciales: `nc1-tarjetas.json` solo vocabulario y estrategia (sin gramática); `nc1-pildoras.json` con categorías marcadas como `null` para definir cuando se trabajen píldoras nuevas; `nc1-reciclaje.json` rediseñado como modelo acumulativo-secuencial, limitado a 5-6 elementos clave por unidad, basado en contenido (no en actividades), con tipos cerrados (vocabulario, estrategia, contenido_gramatical, forma_verbal, estrategia_comunicativa) y niveles de impacto. Anotado: el dashboard debe mostrar todos los JSON y permitir revisar/editar propuestas de reciclaje.
- **2026-05-05 12:15** — **Split físico ejecutado.** Todo el contenido editorial actual movido a `viejo/` (unidades, materiales, agentes, repertorios, referencias, diseno, material-complementario, _template, marco-teorico-metodologico.md, 00-curso-general.md). En raíz quedan: código (scripts, web, eval, diagrama.py), docs (README, CLAUDE, CHANGELOG, ROADMAP, GITHUB-MANIFEST, PROCESO-MAESTRO), config (Dockerfile, railway.toml, requirements.txt, .env.example), y la zona `nuevo/` (en construcción). Eliminada basura técnica: `texput.log`, `__pycache__/`, `.DS_Store`. Actualizadas referencias a paths nuevos en: `.gitignore`, `.dockerignore`, `scripts/importar_inventario.py`, `scripts/crear_crew_agents.py`, `diagrama.py` (8 referencias a repertorios), `README.md`, `CLAUDE.md`.
- **2026-05-05 12:30** — Commit `c5e08e9` "v10.0: split repo en zonas viejo/ y nuevo/ + PROCESO-MAESTRO" pusheado a `main`.
- **2026-05-05 14:00** — Dictamen del revisor sobre paso B (commit `67db6a4`): implementación correcta y completa, sin bloqueantes. Hallazgo cosmético registrado como B4 (`_normSeccion` no fusiona pestañas `(cont.)`); se resuelve en paso C sin acción separada.
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
