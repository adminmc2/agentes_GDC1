# Glosario del proyecto — índice semántico transversal

> **Qué es:** punto de entrada a la terminología **transversal** del proyecto — los términos que cualquier sesión necesita entender con independencia de la fase. Orientación, no autoridad.
>
> **Qué NO es:** no es referencia de schema. El detalle campo por campo de cada fase vive en su glosario de fase (ver Bloque 3).

---

## Bloque 1 — Términos globales del proyecto

**repo A / repo B** — Repo A (`guia-didactica-profesor-IA`): el entregable publicado + infraestructura (inventarios canónicos, fases, scripts, dashboard). Repo B (`temporal-antiguo-guia-ia`): el sistema de trabajo donde sucede la redacción editorial. La redacción vive en B; A recibe el entregable. Ver `CLAUDE.md` § "Modelo de dos repositorios".

**inventario** — JSON estructurado por unidad (`UX-nc1-inventario.json`) que captura todo el contenido editorial visible al alumno en el libro. Producto de la fase 1. Ver detalle en `fases/1-extraccion-inventario/glosario.md`.

**registry canónico** — Archivo JSON que fija el universo cerrado de nombres válidos de una dimensión (léxico, gramática, pron/orto, verbal). Toda clave o referencia canónica que entra al inventario debe ser literal de su registry. Hay 4, en `fases/1-extraccion-inventario/`.

**PCIC** — Plan Curricular del Instituto Cervantes. Fuente de referencia externa para los contenidos de nivel A1; respalda los registries canónicos. Archivos `pcic-a1-*.json`.

**unidad / unidad atípica** — Unidad: cada capítulo del curso (`U0`–`U9`). Unidad atípica: una unidad que no sigue la estructura canónica de secciones — en NC1, `U0` ("Punto de partida"). Lleva la marca `_nota_unidad_atipica`.

**fase** — Cada uno de los 8 pasos del proceso editorial. Cada fase tiene su carpeta `fases/<N>-<nombre>/` con `CLAUDE.md` + `prompt.md` + artefactos, auto-cargada al trabajar dentro de ella.

**dashboard** — Herramienta local de visualización (`python3 diagrama.py` → `http://localhost:8081`) que renderiza inventarios, reciclaje y estado del proyecto. Infraestructura de repo A, sin despliegue en la nube.

**modelo IA-first** — Principio de trabajo: la IA decide, el código comprueba, el humano cierra. Las fases se diseñan para que el análisis lo haga la IA y la validación/cierre queden como gates.

**dry-run** — Pasada de extracción sin escribir el JSON final: la IA propone, el autor itera en chat y solo tras su OK se escribe el inventario candidato. Modo de trabajo de la fase 1.

**publicación canónica** — Acto de copiar el material editorial cerrado y validado desde repo B a la ruta versionada `unidades/UX/propuesta/` de repo A, con renaming sin prefijo. Ver `CLAUDE.md` § "Flujo de publicación canónica".

**mirror snapshot** — Naturaleza de la canónica `unidades/UX/` de repo A: es una copia publicada del trabajo, no la fuente. Las ediciones futuras se hacen en repo B y se re-publican.

**source of truth** — Fuente única de un criterio o dato. Cada criterio editorial vive en un único archivo (Regla de Oro 4); la duplicación lleva a desincronización.

---

## Bloque 2 — Términos de fase 2 (rediseño en curso)

> ⚠️ **En estabilización.** El rediseño de fase 2 está abierto (`fases/2-reciclaje/REDISEÑO-EN-CURSO.md`); estas definiciones pueden afinarse.

**hilo** — Unidad de análisis del reciclaje: el recorrido de un contenido editorial a lo largo del curso. Un hilo por contenido (campo semántico, categoría gramatical, lema, perífrasis). Ver `REDISEÑO-EN-CURSO.md` §2.2.

**evento** — Cada aparición de un contenido en una unidad concreta dentro de un hilo. Lleva una lista de etiquetas. Ver §2.4.

**etiqueta** — Marca que describe qué hace una unidad con un contenido en un evento: `introduce`, `amplia`, `aplica`, `sistematiza`, `contrasta`, `anticipacion` (+ `discrimina` en pron/orto). Coexisten. Ver §2.3.

**mapa** — Primer grado de población de un hilo: el esqueleto, desde el índice del curso (`nc1-curso.json`) — identidad del hilo + eventos básicos. Ver §4.2.

**auto** — Segundo grado de población de un hilo: enriquecimiento con los contenidos concretos por unidad desde los inventarios. Ver §4.2.

**detalle** — Tercer grado de población de un hilo: la justificación lingüístico-pedagógica del procedimiento didáctico (cadena de prerrequisitos). Ver §4.4.

**Capa 1** — Parte determinista de fase 2: un script Python que genera el esqueleto mecánico del reciclaje. Ver §1.3.

**Capa 2** — Parte enriquecedora de fase 2: una sesión IA que refina decisiones editoriales, valida cross-unidad y propone-en-chat al autor. Ver §1.3.

**reciclaje** — Recurrencia intencional de contenidos a lo largo del curso, y el catálogo acumulativo (`nc1-reciclaje.json`) que la modela. Producto de la fase 2.

**anticipación** — Contenido que aparece en una unidad como input incidental antes de ser canónico en una unidad posterior. Es a la vez una etiqueta de evento y un fenómeno cross-unidad. Ver §2.3.

**`procedencia_indice`** — Triaje de cada evento respecto al índice editorial del curso (`nc1-curso.json`). Eje ortogonal a `etiqueta` (`REDISEÑO-EN-CURSO.md` §9). Tres valores; el JSON conserva el técnico, el dashboard muestra el rótulo editorial:

| Valor (JSON) | Rótulo editorial | Significado |
|---|---|---|
| `declarado` | **contenido del índice** | El contenido aparece literal en el índice del curso para esa unidad. Lo escribe la Capa 1 por coincidencia mecánica. |
| `reconciliado` | **reconciliado según el PCIC** | El contenido corresponde a una entrada del índice del curso bajo otro nombre — la equivalencia se resuelve vía los registries canónicos respaldados por PCIC (el índice puede decir "Verbos ser, llamarse y tener" y el hilo ser "ser"). Lo escribe la Capa 2. |
| `nuevo` | **fuera del índice** | El contenido aparece en la unidad pero el índice del curso no lo anuncia; es contenido emergente. Lo escribe la Capa 2. |

---

## Bloque 3 — Glosarios de fase

Para el detalle terminológico interno de cada fase:

| Fase | Glosario | Cubre |
|---|---|---|
| Fase 1 — Extracción de inventario | `fases/1-extraccion-inventario/glosario.md` | Referencia campo por campo del schema del inventario: claves, enums, marcas internas. |
| Fase 2 — Reciclaje | *Pendiente* | Se creará cuando el rediseño de fase 2 cierre y la terminología se estabilice. |