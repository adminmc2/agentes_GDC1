# Changelog — Guía Didáctica del Profesor (IA)
## Sistema de Agentes v5.0 — Nuevo Compañeros 1

---

## [v10.74b — 2026-05-07] — Cierre del pase de coherencia tras dictamen del revisor sobre v10.74

Hallazgos del revisor sobre v10.74: la actualización fue parcial en 2 sitios:

**1. PROCESO-MAESTRO.md líneas 163-180 (estructura por actividad).** v10.74 actualizó el titular a "20 tipos" pero la enumeración debajo seguía listando 17 valores (faltaban `escucha`, `lee_y_escucha`, `ver_video`, `responder_preguntas_cerradas`, `responder_preguntas_abiertas`); además el shape de actividad seguía describiendo `destreza` como string sin mencionar el nuevo campo `enfoque` introducido en v10.60. Drift incompleto del corazón del contrato.

**Fix:** enumeración real de 20 tipos completa; `destreza` reescrita como "lista de strings, alfabética, sin duplicados" con enum cerrado de 6 valores y referencia a schema §5b; **`enfoque` añadido** como nuevo bullet con su enum cerrado de 6 y referencia a schema §5c. Cita de qué cambió en cada versión (v10.25, v10.59, v10.60, v10.64).

**2. PROCESO-MAESTRO.md línea 779 ("Sobre la implementación a escribir cuando lleguemos").** Seguía diciendo "Plantilla HTML del informe por unidad e integración en dashboard (paso B del plan)", reabriendo el modelo viejo de informe estático que v10.71 había cerrado.

**Fix:** sección renombrada a "Sobre la implementación pendiente" (sin "a escribir" que sugería que nada está hecho); el bullet del informe HTML reescrito a "Refinamiento visual de la **vista HTML dinámica**" — la vista existe y funciona, lo pendiente es refinamiento visual y extensión a los 3 JSON globales.

**Efecto:** v10.74 ahora cerrada limpia. Archivos vivos sin drift sobre Fase 1 ni sobre la vista HTML.

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

**Próximo:** v10.75 (archivar CHANGELOG pre-v10.40). Paralelización de extracciones autorizada con base documental ya limpia.

---

## [v10.74 — 2026-05-07] — Pase de coherencia documental: drift en PROCESO-MAESTRO + REVIEW

Bloqueante para la limpieza/compactación posterior (v10.75-77) y para la apertura de chats paralelos de extracción. Mientras los archivos vivos describan el sistema con datos obsoletos, cualquier compactación consolida información incorrecta y los chats nuevos heredan drift.

**Drift identificado por el revisor + auditoría propia:**

- `PROCESO-MAESTRO.md` línea 88: `validar_inventario.py` "a escribir" — el validador es operativo desde antes del refactor.
- `PROCESO-MAESTRO.md` línea 128: misma redacción "a escribir".
- `PROCESO-MAESTRO.md` línea 163: "taxonomía cerrada de **17 tipos**" — son **20** desde v10.64 (+ `escucha`).
- `PROCESO-MAESTRO.md` línea 231: "Plantilla HTML del informe por unidad" como tarea pendiente — v10.71 cerró que es vista HTML dinámica del dashboard, no plantilla estática.
- `PROCESO-MAESTRO.md` línea 701 (Parte 4, decisión 24): mismo "validar_inventario.py (a escribir)".
- `REVIEW.md` línea 45 (fila estado global Fase 1): "🔄 A4 refactor documental en curso" — A4 cerrado en v10.69.
- `REVIEW.md` línea 112 (encabezado bloque A4): "🔄 EN CURSO" — idem.

**Cambios aplicados:**

- 5 actualizaciones a estado real en `PROCESO-MAESTRO.md` (líneas 88, 128, 163, 231, 701). Parte 2 de Fase 1 actualizada a estado real, **NO reducida a puntero** — la reducción a puntero pertenece a un paso de compactación estructural posterior.
- 2 correcciones de estado en `REVIEW.md` (línea 45 fila tabla y línea 112 encabezado bloque).

**Lo que NO se toca** (legítimo, no es drift):
- Líneas 107 y 113 de `PROCESO-MAESTRO.md`: `regenerar_tarjetas_globales.py` y `regenerar_pildoras_globales.py` siguen siendo tareas pendientes reales (verificado: solo `validar_inventario.py` existe en `scripts/`).
- Bitácora histórica de `PROCESO-MAESTRO.md` (líneas 860, 865) que mencionan "17 tipos" — describen estado en el momento del commit, no se reescriben.

**Sin cambios funcionales en código.** Validador U0/U1/U3 → 0/0 post-cambios.

**Próximo:** v10.75 (archivar CHANGELOG pre-v10.40), ya en worktree `docs/cleanup`. La paralelización de chats de extracción se puede abrir tras el push de v10.74.

---

## [v10.73 — 2026-05-07] — Cierre de referencias rotas en `schema-inventario.md` tras v10.72

Hallazgo del revisor sobre v10.72: el archivado de `REFACTOR-PROPUESTA.md` a `docs/historico/` dejó dos referencias rotas en `fases/1-extraccion-inventario/schema-inventario.md` (líneas 7 y 377). Ambas decían *"ver REFACTOR-PROPUESTA.md paso 5.5"* en un archivo vivo del producto operativo.

**Decisión:** en lugar de re-apuntar al nuevo path histórico, el revisor sugirió formulación estable y atemporal — el schema describe contrato vigente del JSON, no debería encadenarse a un artefacto del proceso de refactor que ya cumplió su función.

**Fix quirúrgico (2 líneas):**
- Línea 7: *"...se resuelve antes del merge en commit aparte (ver REFACTOR-PROPUESTA.md paso 5.5)."* → *"...se resuelve antes del merge en commit aparte."*
- Línea 377: *"La divergencia no es un estado válido de cierre del refactor (ver REFACTOR-PROPUESTA.md paso 5.5)."* → *"La divergencia no es un estado válido de cierre."*

**Verificación:** sin más referencias vivas a `REFACTOR-*.md` fuera de `docs/historico/`. Las menciones que quedan en CHANGELOG y bitácora REVIEW siguen siendo históricas (no se reescriben).

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

**Próximo:** push de `main` a `origin` con autorización del autor + reextracción de U2 en rama nueva (no directamente sobre main).

---

## [v10.72 — 2026-05-07] — Archivado de documentos del refactor cerrado en `docs/historico/`

Limpieza post-refactor: los dos artefactos del **proceso** del refactor de fase 1 (no del producto vivo) se archivan en `docs/historico/refactor-prompt-fase1/` para que `fases/1-extraccion-inventario/` contenga solo lo operativo (CLAUDE.md, prompt.md, schema, reglas, convenciones).

**Movidos con `git mv` (preserva historial):**
- `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md` → `docs/historico/refactor-prompt-fase1/REFACTOR-PROPUESTA.md` — plan ejecutable del refactor, cerrado al 100% en v10.69.
- `fases/1-extraccion-inventario/REFACTOR-WORKTREE.md` → `docs/historico/refactor-prompt-fase1/REFACTOR-WORKTREE.md` — documentación del worktree dedicado usado durante la ejecución.

**Creado:**
- `docs/historico/refactor-prompt-fase1/README.md` — explica qué hay archivado, por qué se movió fuera de la carpeta de fase, y cuándo conviene consultar el archivo (planificación de futuros refactores, reapertura de decisiones, plantilla de proceso).

**Cross-references vivas actualizadas:**
- `PROCESO-MAESTRO.md` decisión 34 (línea 727).
- `REVIEW.md` paso A4 sección viva (líneas 118, 120, 124, 135, 142, 150).

**Cross-references históricas NO tocadas** (entradas de bitácora en REVIEW.md y CHANGELOG.md anteriores que mencionan los paths originales): describen el estado del repo en el momento del commit; reescribirlas sería revisionismo.

**`viejo/` no se toca** (regla del proyecto: intocable hasta autorización explícita del autor).

**Sin cambios funcionales en código.** Validador U0/U1/U3 → 0/0 post-archivado (sanity check).

---

## [v10.71 — 2026-05-07] — Ajuste de redacción en PROCESO-MAESTRO sobre informe HTML / vista dinámica del dashboard

Observación post-merge: la decisión 25 de `PROCESO-MAESTRO.md` (línea 705) y la entrada de bitácora del 2026-05-05 (línea 845) hablaban de "**generar además un informe HTML visual**" como si la fase 1 produjera un segundo artefacto HTML estático. La implementación real (verificada por el revisor en `diagrama.py:245/980/983` y `web/index.html:341/595/647`) confirma que **el JSON es el único output de la fase**, y que la "vista HTML" es una **renderización dinámica** que el dashboard genera al vuelo desde el JSON. No existe ningún paso de generación de HTML estático por unidad.

**Drift detectado:** el lenguaje "genera además" en PROCESO-MAESTRO sugería un segundo artefacto que en realidad nunca existió como archivo. Los archivos de fase 1 (CLAUDE.md, prompt.md) ya estaban correctos declarando un único output JSON.

**Fix quirúrgico (2 líneas en PROCESO-MAESTRO.md):**

- **Decisión 25 (línea 705)** — reescrita: *"Cada extracción de inventario produce un JSON por unidad. Ese JSON queda además disponible como vista HTML dinámica integrada en el dashboard existente (`web/index.html`), sin generar por ahora un archivo HTML independiente."*
- **Bitácora 2026-05-05 (línea 845)** — final reescrito: *"El dashboard ofrece una vista HTML dinámica integrada del inventario JSON (`web/index.html`); no existe actualmente un artefacto HTML estático adicional por unidad."*

**Sin tocar:** archivos de fase 1 (ya fieles al sistema real), líneas 232/680/815 de PROCESO-MAESTRO (coherentes con la nueva redacción).

**Sin cambios funcionales en código.** Solo coherencia documental.

---

## [v10.70 — 2026-05-07] — Regla 3 de `CLAUDE.md` de fase reformulada para que describa la realidad del sistema

Observación post-merge del revisor: la regla 3 ("Single source of truth por capa") prohibía duplicación entre `prompt.md`, `schema-inventario.md`, `reglas-operativas.md` y `convenciones-y-casos.md` — pero **excluía tácitamente al propio `CLAUDE.md` de fase**. La duplicación contractual real entre `CLAUDE.md` y `prompt.md` (objetivo, input/output, invocación, validación mínima, literalidad, convención root-relative, framing SSoT) sobrevivía al refactor sin estar contemplada en la regla.

**Auditoría previa (sin cambios de código):**
- **Grupo A — duplicación contractual aceptable** entre los 2 entry points: 7 bloques (objetivo, paths, invocación, validación, literalidad, convención root-relative, framing SSoT). Todos contractuales, ninguno operativo.
- **Grupo B — duplicación operativa peligrosa**: 0 hallazgos. Verificado que NO aparecen valores concretos de `tipo`, `destreza`, `tipo_cuadro`, opciones fijas NC1, categorías de `vocabulario_consolidado` ni reglas de desempate fuera de su archivo canónico. La lógica decisional vive solo en `reglas-operativas.md`; el shape solo en `schema-inventario.md`; las convenciones solo en `convenciones-y-casos.md`.

**Fix quirúrgico (1 línea):** regla 3 reescrita según la formulación del revisor:

> "Single source of truth por capa — las reglas estructurales, decisionales y convenciones viven una sola vez en los archivos de soporte (`schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md`). `CLAUDE.md` y `prompt.md` pueden repetir hechos y reglas mínimas de contrato de fase (objetivo, input/output, invocación, validación, literalidad) por ser entry points complementarios. Si lógica operativa o reglas de clasificación aparecen duplicadas fuera de su archivo canónico, es un bug."

**Sin tocar `prompt.md` ni los archivos de soporte ni el validador.** No es problema arquitectónico profundo: la regla mal formulada simplemente no describía la realidad ya implementada.

**Próximo:** ninguno por ahora. Refactor cerrado y revisor sin bloqueantes pendientes.

---

## [v10.69 — 2026-05-07] — A4.6 cerrado: merge `refactor/prompt-fase-1` → `main` (cierre del refactor de fase 1)

Merge ejecutado con `git merge --no-ff` (commit `110e722`) para preservar el rastro completo del refactor de fase 1 (v10.40 → v10.68, 29 commits intermedios).

**Diff del merge:** 14 archivos, +2555 / –838 líneas.

**Archivos creados en `main`:**
- `fases/1-extraccion-inventario/schema-inventario.md` (contrato de datos puro).
- `fases/1-extraccion-inventario/reglas-operativas.md` (reglas decisionales — single source of truth de precedencias).
- `fases/1-extraccion-inventario/convenciones-y-casos.md` (transcripción + casebook).
- `fases/1-extraccion-inventario/REFACTOR-WORKTREE.md` (documentación del worktree dedicado).

**Archivos modificados:**
- `fases/1-extraccion-inventario/prompt.md` (547 → 111 líneas, –80%).
- `fases/1-extraccion-inventario/CLAUDE.md` (de fase, modo contrato corto, 60 líneas).
- `scripts/validar_inventario.py` (validador estructural, contrato paralelo del schema).
- `unidades/U0/U0-nc1-inventario.json`, `unidades/U1/U1-nc1-inventario.json`, `unidades/U3/U3-nc1-inventario.json` (los 3 oráculos reclasificados al contrato actualizado).
- `CHANGELOG.md`, `REVIEW.md`, `PROCESO-MAESTRO.md` (bitácoras).

**Validador en `main` post-merge:** U0 ✅, U1 ✅, U3 ✅, todos 0 errores y 0 avisos.

**Gate A4 entero cerrado:** los 5 sub-gates del bloque "Gate de cierre de A4 entero" en `REVIEW.md` ya en ✅ (sub-pasos cerrados, A4.5 acta empírica, A4.5.5 0 divergencias, merge ejecutado, bitácoras sincronizadas).

**Sin push automático.** Push a remoto queda como decisión del autor.

**Branch `refactor/prompt-fase-1` y worktree** `/Users/armandocruz/Desktop/guia-didactica-refactor/` **se mantienen intactos** por si se necesita inspeccionar el rastro del refactor.

**Refactor de fase 1 cerrado.**

---

## [v10.68 — 2026-05-07] — Cierre formal de A4.5 (acta empírica) y A4.5.5 (cross-check schema↔validador)

Actas formales de los dos gates pre-merge tras el dictamen positivo del revisor sobre v10.67:

**A4.5 — Acta de prueba empírica:** los 3 oráculos U0/U1/U3 reclasificados al contrato actualizado (3 ejes ortogonales `tipo`/`destreza`/`enfoque`) en 4 commits iterativos con dictamen del revisor:
- v10.64 — U0 piloto (10 actividades) + ampliación taxonomía 19→20 (`escucha`).
- v10.65 — U1 (42 actividades) + 3 fixes A1/A2/A3 del revisor + regla nueva de desempate §2.2 punto 5 (`completa_huecos` vs `produccion_escrita_guiada`).
- v10.66 — U3 (47 actividades) + 3 refinamientos de §2.2 (puntos 1, 2 y 3: video sin manipulación posterior, manipulación manda en cualquier punto, criterio explícito destreza para `responder_preguntas_*`).
- v10.67 — cierre de bloqueante sobre `escucha_y_responde` (3 reclasificaciones).

Validador U0/U1/U3 → 0/0. Sin pérdida de decisiones semánticas. Conteos coherentes (10 + 42 + 47 = 99 actividades).

**A4.5.5 — Acta de cross-check schema↔validador:** script de paridad ejecutado sobre las 5 enumeraciones cerradas → **5/5 idénticas, 0 divergencias**:
- `tipo`: 20 valores (`busqueda_informacion`, `clasifica`, `completa_huecos`, `escucha`, `escucha_y_repite`, `escucha_y_responde`, `expresion_escrita_libre`, `expresion_oral_libre`, `interaccion_oral`, `juego`, `lee_y_escucha`, `ordena`, `produccion_escrita_guiada`, `relaciona`, `responder_preguntas_abiertas`, `responder_preguntas_cerradas`, `seleccion_multiple`, `tarea_final`, `ver_video`, `verdadero_falso`).
- `destreza`: 6 valores (`comprension_auditiva`, `comprension_lectora`, `expresion_escrita`, `expresion_oral`, `interaccion_oral`, `mediacion`).
- `enfoque`: 6 valores (`comunicacion`, `cultura`, `fonetica`, `gramatica`, `transversal`, `vocabulario`).
- `tipo_cuadro`: 5 valores (`comunicativo`, `cultural`, `fonetico`, `gramatical`, `lexical`).
- `seccion`: 7 valores (`comunicacion`, `cultura`, `destrezas`, `evaluacion`, `gramatica`, `reflexion`, `vocabulario`).

El gate ineludible de no-divergencia schema↔validador queda cumplido.

**Sin cambios funcionales en este commit.** Solo cierre documental de actas en REVIEW.md (tabla de sub-pasos A4.5 y A4.5.5 marcadas ✅) y CHANGELOG.

**Próximo:** A4.6 — merge `refactor/prompt-fase-1` → `main` (pendiente de confirmación explícita del autor por ser acción visible y hard-to-reverse).

---

## [v10.67 — 2026-05-07] — Cierre de bloqueante del revisor: `escucha_y_responde` mal usado en 3 oráculos

Hallazgo bloqueante del revisor sobre v10.66: la definición de `escucha_y_responde` en `reglas-operativas.md` §2.2 ("Escucha y responde oralmente, sin texto delante") no se alineaba con el uso real en los oráculos. Tres actividades estaban clasificadas con ese tipo cuando en realidad encajan en mecánicas más específicas:

- **U0-p11-act08** "Escucha y escribe" (dictado deletreado, items_libro con slots `_____`): conflicto con regla 5 nueva (con slots predefinidos → `completa_huecos`). **Fix:** `escucha_y_responde` → `completa_huecos`.
- **U0-p11-act09** "Escucha y escribe los números 0-10" (items_libro con slots `_____`): mismo conflicto. **Fix:** `escucha_y_responde` → `completa_huecos`.
- **U3-p39-act06** "Escribe las horas y, después, escucha y comprueba": no es respuesta a estímulo auditivo (el alumno escribe ANTES de escuchar; el audio es comprobación). Tampoco hay slots predefinidos (relojes digitales como estímulo visual). **Fix:** `escucha_y_responde` → `produccion_escrita_guiada`.

**Definición de `escucha_y_responde` se mantiene intacta** — es un nicho legítimo para respuesta oral genuina sin manipulación de slots ni producción escrita.

**Estado del branch:** U0 ✅, U1 ✅, U3 ✅. Cross-check informal del revisor para A4.5.5 confirma alineación schema↔validador en 20 tipos / 6 destrezas / 6 enfoques. Sin otros hallazgos bloqueantes.

**Próximo:** A4.5 (acta) + A4.5.5 (cross-check formal) + A4.6 (merge a `main`).

---

## [v10.66 — 2026-05-07] — Cierre de U3 y refinamiento de desempates en §2.2

- U3 reclasificada: 47 actividades con destrezas normalizadas en listas alfabéticas y enfoque completo.
- 11 cambios de tipo: 10 casos "Completa..." pasan de `produccion_escrita_guiada` a `completa_huecos`, y U3-p39-act05 pasa de `escucha_y_repite` a `completa_huecos`.
- U3-p41-act05 se mantiene en `produccion_escrita_guiada` por tratarse de producción propia sobre relojes vacíos (sin `items_libro`).
- §2.2 se refina en tres puntos:
  - **Regla 1 (`ver_video`)**: solo cuando no hay manipulación posterior. "Mira el vídeo y completa" → `completa_huecos`, no `ver_video`.
  - **Regla 2 (manipulación manda)**: la manipulación domina **en cualquier punto** del enunciado, no solo "posterior". "Completa, escucha y repite" → `completa_huecos` aunque le siga "repite".
  - **Regla 3 (`responder_preguntas_*`)**: distingue explícitamente destreza con texto-fuente (`comprension_lectora` o `comprension_auditiva`, sin `expresion_escrita`) frente a respuesta libre del alumno sin texto-fuente (`expresion_escrita`).

**Estado del branch:** U0 ✅, U1 ✅, U3 ✅. Los 3 oráculos validan 0/0 con el contrato completo. Branch listo para A4.5 (acta) / A4.5.5 (cross-check) / merge a `main`.

---

## [v10.65 — 2026-05-07] — U1 reclasificada + 3 fixes del revisor + regla nueva de desempate `completa_huecos` vs `produccion_escrita_guiada`

Reclasificación de U1 (42 actividades) tras prueba empírica de v10.64. Validación del revisor sobre la primera pasada detectó 3 desajustes contractuales reales:

**A1 (Bloqueante) — U1-p12-act3:** la actividad encadenaba "Escucha y repite vocabulario / Después, escucha y escribe" — el contrato (§2.2 regla de desempate 2: "última acción que pide producción concreta") obliga a clasificar por la fase final (asignación numérica), no por la primera (repetición). Tampoco corresponde `expresion_escrita` (escribir un número es transcripción/manipulación). **Fix:** tipo `escucha_y_repite` → `relaciona`; destreza `[comprension_auditiva, comprension_lectora, expresion_oral]` (sin `expresion_escrita`).

**A2 (Alto) — Frontera ambigua `completa_huecos` vs `produccion_escrita_guiada`:** la primera pasada congeló 4 actividades en `produccion_escrita_guiada` por solapamiento de descripciones en §2.2 (ambos tipos ejemplificaban "Coloca el artículo / Completa la tabla"). El revisor señaló que la ambigüedad existe pero no justifica el congelamiento — y propuso una **regla de desempate explícita**:
> Con huecos/celdas/slots predefinidos → `completa_huecos`. Sin huecos predefinidos, el alumno construye frases/etiquetas a partir de modelo/imagen/regla → `produccion_escrita_guiada`.

**Fix de regla:** §2.2 punto 5 nuevo en `reglas-operativas.md` con la formulación.

**Fix de JSON:** 5 actividades cambian de tipo siguiendo la nueva regla:
- U1-p14-act2 "Completa los huecos con la forma del verbo tener" → `completa_huecos`
- U1-p14-act4 "Completa la tabla con el masculino/femenino" → `completa_huecos`
- U1-p21-act1 "Completa las frases con el verbo ser" → `completa_huecos`
- U1-p21-act3 "Completa la tabla [género]" → `completa_huecos`
- U1-p21-act4 "Completa con el verbo ser/llamarse/tener" → `completa_huecos`

Mantienen `produccion_escrita_guiada` (sin huecos predefinidos): U1-p21-act2 "Coloca el artículo", U1-p14-act5 "Forma el femenino", U1-p15-act6/7, U1-p17-act6, U1-p21-act5.

**A3 (Alto) — U1-p14-act3 "Forma frases tomando un elemento de cada columna":** el contrato (§2.2 ejemplo explícito de `produccion_escrita_guiada`: "Forma frases") obliga a clasificarlo como producción guiada. La primera pasada lo dejó en `relaciona`, lo cual además entraba en conflicto con asignar `expresion_escrita` a una mecánica de relación (regla anti-sobreasignación). **Fix:** tipo `relaciona` → `produccion_escrita_guiada`; destreza `[comprension_lectora, expresion_escrita]` mantenida.

**Resumen del commit:**
- 7 actividades de U1 con `tipo` corregido (1 por A1, 5 por A2 incl. consistencia, 1 por A3).
- 1 regla nueva en `reglas-operativas.md` §2.2 punto 5.
- Validador U1 → 0/0.

**Estado del branch:**
- U0: ✅ verde
- U1: ✅ verde (tras estos fixes)
- U3: ❌ rojo (legacy, pendiente — siguiente)

**Próximo:** reclasificar U3 con la regla de desempate ya cerrada y aplicada.

---

## [v10.64 — 2026-05-07] — U0 reclasificada (piloto) + taxonomía `tipo` 19→20 (añadido `escucha`) + refinamiento §2.3

**Prueba empírica del nuevo contrato `destreza`/`enfoque`** con U0 como piloto. El sistema funciona: 10 actividades reclasificadas, validador 0/0.

**Decisiones tomadas durante la prueba:**

1. **Taxonomía `tipo` ampliada de 19 → 20:** añadido valor `escucha` (input puro auditivo sin lectura de texto extenso ni acción posterior; apoyo visual no textual admisible: mapa, imagen, foto). Caso disparador: U0-p8-act01 ("Mira el mapa y escucha el nombre de los países. Observa la pronunciación.") no encajaba en `escucha_y_repite` (no pide repetir) ni en `lee_y_escucha` (no hay texto extenso para leer). Decisión cerrada en PROCESO-MAESTRO bitácora cumpliendo la regla §2.4 de `reglas-operativas.md`. Aplicado en schema §5, validador `TIPOS_VALIDOS`, reglas-operativas §2.2 (nueva fila + descripciones afinadas de `lee_y_escucha` y `escucha_y_repite`), todas las cross-references `19 → 20` (4 archivos).

2. **Regla `expresion_escrita` reformulada (§2.3):** la versión inicial de v10.60 era estricta ("solo si produce texto lingüístico propio: frase elaborada, párrafo, correo, presentación"). Tras prueba con U0 se decide ampliarla a "produce contenido escrito propio" — incluye tanto textos elaborados como **listas de palabras evocadas** (ej. "escribe los países que recuerdas"). Distinción honesta entre **contenido propio** (memoria/criterio/conocimiento → `expresion_escrita`) y **transcripción/aplicación de regla** (dictado, completar artículo, completar palabra del banco → NO `expresion_escrita`).

3. **Heurística `vocabulario` vs `fonetica` documentada (§2.3):** para "escucha y repite" / "escucha y escribe" — agrupación por campo léxico → `vocabulario`; agrupación por dificultad fonética → `fonetica`; deletrear → siempre `fonetica`; **dictado** → siempre `fonetica` (incluso si el contenido dictado es léxico, ej. dictado de números).

4. **U0 reclasificada en bloque (10 actividades):** asignados `destreza` (lista alfabética) y `enfoque` (string) según las reglas refinadas. U0-p8-act01 cambia de `escucha_y_repite` → `escucha` (nuevo tipo). Validador U0 → 0/0.

**Estado actual del branch:**
- U0: ✅ verde (formato nuevo + taxonomía nueva)
- U1, U3: ❌ rojos (formato legacy de destreza, sin enfoque, posibles tipos a revisar) — pendientes de reclasificar siguiendo el mismo patrón.

**Próximo:** reclasificar U1 (~33 actividades) con el mismo procedimiento.

---

## [v10.63 — 2026-05-07] — Fix de drift post-v10.60 en CLAUDE.md de fase

Hallazgo durante la re-revisión del componente 1: la tabla "Para qué consultar qué archivo" (línea 45) listaba las decisiones que viven en `reglas-operativas.md` mencionando solo `tipo` y `tipo_cuadro`. Tras v10.60 hay 4 ejes decisionales (`tipo`/`destreza`/`enfoque`/`tipo_cuadro`); un usuario que llegaba buscando "¿cómo decido la destreza?" no encontraba puntero claro.

**Fix quirúrgico:** una línea — añadidos `destreza` y `enfoque` a la enumeración de decisiones que el archivo `reglas-operativas.md` cubre.

**Las 5 "Reglas críticas" del CLAUDE de fase (líneas 29-35) NO se tocan.** Verificadas como reglas de contrato (no operativas) tanto por el revisor como por re-revisión propia: literalidad del libro, no inventar, single source of truth, validar antes de cerrar, no divergencia schema/validador. Pasan ambos tests (Anthropic + decisión de proyecto sobre single source of truth).

**Sin cambios en otros archivos.** CLAUDE.md de fase: 60 líneas (norte 40-60 cumplido).

**Próximo:** componente 4 — `reglas-operativas.md`.

---

## [v10.62 — 2026-05-07] — Cierre del componente 3 (schema-inventario.md): 3 fixes accionables del revisor

Revisión del componente 3 con 3 hallazgos accionables cerrados en este commit.

**F0 (Bloqueante) — Divergencia real schema↔validador en `_nota_unidad_atipica`.** El schema §11 declara la clave como contractual y opcional, y exige que el validador la incluya en `CLAVES_TOP_OPCIONALES`. El validador solo tenía `{"autoevaluacion"}`, por lo que U0 emitía aviso "Claves top-level no canónicas: ['_nota_unidad_atipica']" — divergencia real con el schema. **Fix:** añadido `_nota_unidad_atipica` a `CLAVES_TOP_OPCIONALES`. U0 ahora valida sin avisos espurios. Schema y validador alineados.

**F1 (Medio) — §13 desactualizada tras v10.60.** La sección "Source of truth con validar_inventario.py" listaba las enumeraciones cerradas (19 tipos / 5 tipo_cuadro / 7 secciones / 3 opciones autoevaluación) pero no mencionaba `destreza` (6 valores) ni `enfoque` (6 valores) introducidos en v10.60. Tampoco listaba la restricción condicional de orden alfabético de `destreza`. **Fix:** §13 reescrita con las 6 enumeraciones cerradas explícitas, los 3 ejes obligatorios por actividad nombrados, y la restricción de orden alfabético añadida a la lista de restricciones condicionales validables.

**F3 (Bajo) — Ambigüedad contractual de `numero`.** El schema §3 declaraba `"numero": <int>` sin especificar obligatoriedad. El validador no lo chequeaba. Algunas actividades del libro NO tienen número visible (ej. "Para aprender", cuadros clasificados como actividad por reglas §1, autoevaluación a pie de página). **Decisión:** `numero` es **opcional**. **Fixes:** schema §3 actualizado a `<int opcional — ver §3.1>` con nueva sub-sección §3.1 explicando cuándo se omite y puntero a `reglas-operativas.md` §1. Validador añade check: si `numero` está presente, debe ser int (no chequea presencia, alineado con la decisión opcional).

**Sin cambios en otros archivos del refactor.** Branch sigue rojo por la migración pendiente de destreza/enfoque per-unidad (gate v10.60).

**Próximo:** revisión del componente 4 — `reglas-operativas.md`.

---

## [v10.61 — 2026-05-07] — Fix de drift documental post-v10.60 en `prompt.md`

Hallazgo del revisor durante la revisión componente-a-componente del refactor: tras v10.60 el contrato exige `destreza` y `enfoque` obligatorios en cada actividad, pero el `prompt.md` no los reflejaba. El paso 5 de "Pasos de la extracción" solo mencionaba "extraer todos los campos del esquema" genéricamente, y el checklist manual de "Cierre y validación" listaba `tipo` entre los enums cerrados pero omitía los dos ejes nuevos.

**Cambios quirúrgicos:**
- Paso 5 ampliado con recordatorio explícito de los **3 ejes ortogonales obligatorios** (`tipo`/`destreza`/`enfoque`) con punteros al schema (§5b/§5c) y a `reglas-operativas.md` §2.3.
- Checklist manual de 9 → 11 items: insertados "Destrezas válidas" e "Enfoque válido" después de "Tipos válidos".

**Métrica:** prompt.md 109 → 111 líneas (sigue dentro del norte 80-120).

**Sin cambios en otros archivos.** Componente 1 (CLAUDE.md de fase) aprobado por el revisor sin findings materiales antes de este commit.

**Próximo:** revisión del componente 3 — `schema-inventario.md`.

---

## [v10.60 — 2026-05-07] — Contrato `destreza`/`enfoque`: separación de ejes habilidad ↔ dominio (commit intermedio rompedor de contrato)

> ⚠️ **Estado intermedio:** este commit deja el branch en rojo intencionadamente. El validador rechaza U0/U1/U3 (~250 errores: `destreza` en formato string legacy + ausencia del nuevo campo `enfoque`). La reclasificación per-unidad de las 97 actividades a destreza-lista-canónica + enfoque se hará en otro chat antes de A4.5.

Hallazgo en revisión durante la primera pasada del rediseño de `destreza`: la versión inicial (lista de 8 valores incluyendo `gramatica`/`vocabulario`) mezclaba dos ejes — habilidad lingüística (MCER) y dominio de contenido (gramática, léxico, etc.). El revisor lo señaló como bloqueante. Decisión: separar en dos campos ortogonales.

**Cambios:**

- **Nuevo eje `destreza` (eje habilidad MCER pura, schema §5b):** lista de strings, enum cerrado de 6 valores: `comprension_auditiva`, `comprension_lectora`, `expresion_escrita`, `expresion_oral`, `interaccion_oral`, `mediacion`. Orden alfabético obligatorio (validable mecánicamente, evita variantes equivalentes con orden distinto). Mínimo 1 elemento, sin duplicados.
- **Nuevo campo `enfoque` (eje dominio de contenido, schema §5c):** string único, enum cerrado de 6 valores: `gramatica`, `vocabulario`, `comunicacion`, `fonetica`, `cultura`, `transversal`. Obligatorio en cada actividad. Independiente de `seccion` (que clasifica la página entera según el índice editorial); `enfoque` clasifica la actividad concreta según su foco pedagógico real. El valor `transversal` reemplaza la propuesta inicial `destrezas` (que reutilizaba el nombre de una sección editorial y pegaba el eje al layout de página, justo lo que la separación intentaba evitar).
- **Validador:** nuevas constantes `DESTREZAS_VALIDAS` (6) y `ENFOQUES_VALIDOS` (6). Bloque de validación por actividad: `destreza` debe existir, ser lista no vacía, valores del enum, orden alfabético, sin duplicados; `enfoque` debe existir, ser string, valor del enum.
- **`reglas-operativas.md` §2.3 reescrita íntegra:** tabla de los 3 ejes ortogonales (`tipo`/`destreza`/`enfoque`), definición de cada valor en ambos ejes, reglas de asignación, relación `enfoque` vs `seccion`, **regla anti-sobreasignación de `expresion_escrita`** (las mecánicas de manipulación de elementos dados — completar, relacionar, ordenar, marcar — NO añaden por sí mismas `expresion_escrita`; solo se añade cuando el alumno produce texto lingüístico propio), 9 ejemplos canónicos con los 3 ejes.
- **Decisiones semánticas registradas:**
  - `comprension_auditiva` es el nombre canónico (no alias). `comprension_oral` y `comprension_auditiva` se consideran sinónimos en este proyecto; en la migración per-unidad, `comprension_oral` legacy se normaliza a `comprension_auditiva`.
  - `produccion_*` → `expresion_*` (terminología MCER moderna).
  - `gramatica`/`vocabulario` salen del eje `destreza` (no son habilidades) y entran como valores de `enfoque` (dominios).
  - `interaccion_escrita` queda fuera del enum (no aparece en NC1 A1.1; ampliación futura como decisión cerrada en PROCESO-MAESTRO si surge un caso).
- **Referencia colgada `§2b` corregida:** el schema apuntaba a `reglas-operativas.md §2b` que no existía; ahora apunta a §2.3 (donde realmente vive el contenido).

**Impacto sobre los oráculos:** U0/U1/U3 quedan en formato legacy (string con `+`) y sin `enfoque`. El validador los rechaza sistemáticamente — estado intermedio aceptado y documentado, no estado de cierre.

**Gates pendientes (en orden):**
1. Reclasificación per-unidad de U0/U1/U3 (otro chat, una unidad por sesión). Asignar `destreza` (lista canónica) y `enfoque` (string) a las 97 actividades. Validador 0/0 al cierre de cada unidad.
2. A4.5 — prueba empírica de reextracción (solo después de gate 1).
3. A4.5.5 — cross-check schema↔validador (antes del merge).

**Próximo:** revisión componente-a-componente del refactor (en curso) + reclasificación per-unidad.

---

## [v10.59 — 2026-05-07] — Taxonomía de `tipo` rediseñada (17 → 19) por acción imperativa del enunciado

Hallazgo durante el inicio de A4.5 (reextracción empírica de U1 con oráculo): la taxonomía de 17 tipos mezclaba `tipo` (formato/mecánica que pide el enunciado) con `destreza` (habilidad ejercitada). Tipos como `comprension_lectora` o `comprension_auditiva` describían destrezas, no acciones; provocaban ambigüedad real (una actividad "Lee y escucha el diálogo. Después, marca verdadero o falso" podía clasificarse como `comprension_lectora`, `comprension_auditiva` o `verdadero_falso`).

**Decisión:** `tipo` y `destreza` son dimensiones independientes. `tipo` = la acción específica que pide el enunciado (cómo se manipulan los elementos). `destreza` = qué habilidad ejercita el alumno (campo separado, próximo trabajo).

**Cambios:**

- **Schema (§5):** taxonomía cerrada reescrita a 19 valores, agrupados en 7 familias por acción: input puro (`lee_y_escucha`, `ver_video`); orales reproductivas/responsivas (`escucha_y_repite`, `escucha_y_responde`); manipulación de elementos dados (`completa_huecos`, `relaciona`, `ordena`, `clasifica`, `seleccion_multiple`, `verdadero_falso`); responder preguntas (`responder_preguntas_cerradas`, `responder_preguntas_abiertas`); producción oral (`interaccion_oral`, `expresion_oral_libre`); producción escrita (`produccion_escrita_guiada`, `expresion_escrita_libre`); otros (`busqueda_informacion`, `tarea_final`, `juego`).
- **Eliminados:** `comprension_lectora`, `comprension_auditiva` (eran destrezas, no acciones).
- **Validador:** `TIPOS_VALIDOS` y `TIPOS_QUE_REQUIEREN_ITEMS` actualizados. Añadidas `ejemplos_modelo`, `programas_tv`, `horarios_digitales` a `CONTENIDOS_VISIBLES` (claves ya documentadas en schema pero ausentes del validador — divergencia schema↔validador detectada y cerrada como adelanto parcial de A4.5.5).
- **`reglas-operativas.md` §2:** reescrita íntegra. §2.1 regla operativa "tipo = la acción específica del enunciado". §2.2 tabla canónica de los 19 tipos con disparadores de enunciado y ejemplo de oráculo. §2.3 nota sobre la separación `tipo` vs `destreza` (campo separado, no tocado en este commit).
- **Reasignaciones aplicadas:** 16 actividades reclasificadas en U1 (9) y U3 (7); U0 sin cambios. Mapeo completo registrado en la bitácora del REVIEW.
- **Validación:** `python3 scripts/validar_inventario.py 0/1/3` → 0 errores en los tres (U0 con 1 aviso intencional `_nota_unidad_atipica`).

**Efecto sobre A4.5:** las divergencias detectadas en la primera pasada empírica de U1 (7 tipos no coincidentes con el oráculo + análogas en U3) eran reales pero la causa raíz no era una mala clasificación — era ambigüedad de la propia taxonomía. Resuelto el origen, las clasificaciones convergen.

**Próximo:** trabajar la dimensión `destreza` como campo separado (segundo eje pedagógico, no afecta a `tipo`).

---

## [v10.58 — 2026-05-07] — Sincronización de fila-resumen A4.4 con la bitácora

Hallazgo Bajo del revisor sobre `590fd96` (v10.57): la fila-resumen de A4.4 en la tabla de sub-pasos de `REVIEW.md` se quedó desactualizada. Decía *"✅ 2026-05-07 02:30 (57 líneas, 7 secciones)"* mientras que CHANGELOG v10.57 y la propia bitácora REVIEW ya reflejaban el cierre limpio a las 03:00 con **59 líneas** (tras añadir la convención root-relative). Doble verdad menor entre tabla y bitácora.

**Resolución:** fila reescrita a *"✅ cerrado limpio 2026-05-07 03:00 en v10.57 (59 líneas tras añadir convención root-relative explícita; 7 secciones; norte 40-60 cumplido; cero duplicaciones literales con prompt.md)"*. Tabla y bitácora ahora dicen lo mismo.

**Adicional registrado:** el revisor confirma que ejecutó el validador desde la raíz del repo con la convención root-relative ahora explícita y devuelve JSON válido y 0 avisos para U1. Es una **primera verificación funcional informal externa al ejecutor**, no sustituye A4.5 (la prueba funcional oficial sigue pendiente como reextracción de los 3 casos seleccionados, ver REFACTOR-PROPUESTA §5 paso 5).

**Sin cambios de código.** Solo coherencia documental.

**Próximo:** A4.5.

---

## [v10.57 — 2026-05-07] — Cierre limpio de A4.4: convención root-relative explícita antes de A4.5

Hallazgo Medio del revisor sobre `278144a` (v10.56, A4.4): los comandos en `CLAUDE.md` de fase no son ejecutables tal como están escritos en el contexto que el propio archivo declara.

**El defecto:** `CLAUDE.md` de fase se auto-carga al trabajar dentro de `fases/1-extraccion-inventario/`. Pero los comandos `python3 scripts/validar_inventario.py X` y `python3 diagrama.py` son rutas root-relative — ejecutados literalmente desde la carpeta de fase, fallan con "No such file or directory" porque `scripts/` y `diagrama.py` solo existen desde la raíz del repo.

La convención implícita del proyecto sí es root-relative (el `CLAUDE.md` raíz también prescribe `python3 scripts/validar_inventario.py 3` así). Pero el CLAUDE de fase, al auto-cargarse en otro `cwd`, sugiere otro contexto. Ambigüedad documental real, no funcional.

**Por qué se resuelve antes de A4.5:** A4.5 es la primera prueba funcional oficial del refactor. El procedimiento incluye ejecutar el validador. Si el documento que se carga a la sesión (CLAUDE de fase) describe comandos que no funcionan literalmente, el sub-paso arranca con confusión innecesaria.

**Resolución:** nota explícita "Convención de comandos: root-relative — se ejecutan desde la raíz del repo, no desde la carpeta de fase" añadida al inicio de:

- `CLAUDE.md` de fase, sección "Cómo validar".
- `prompt.md`, sección "Cierre y validación".

La nota del CLAUDE es más extensa (incluye el matiz de que aunque se auto-cargue en la fase, los comandos asumen `cwd = raíz`). La nota del prompt es más breve porque el prompt no se auto-carga.

**Métricas:**

| Archivo | Pre-v10.57 | Post-v10.57 |
|---|---|---|
| `CLAUDE.md` fase | 57 | 59 |
| `prompt.md` | 107 | 109 |

Ambos siguen dentro de su norte de tamaño respectivo (40-60 y 80-120).

**Sin cambios en otros archivos.** Sin cambios de código.

**Próximo:** A4.5 — primera prueba funcional oficial del refactor.

---

## [v10.56 — 2026-05-07] — A4.4: reescritura de `CLAUDE.md` de fase en modo contrato corto

Séptimo sub-paso del refactor. `CLAUDE.md` de fase reescrito según `REFACTOR-PROPUESTA.md` §3.1: contrato corto, no manual.

**Estructura final** (57 líneas, 7 secciones — dentro del norte 40-60):

1. Qué produce esta fase (1 párrafo).
2. Input y output (2 bullets).
3. Cómo se invoca (1 línea).
4. Cómo validar (validador automático + revisión visual del autor).
5. **Reglas críticas (las que un humano nunca debe olvidar al trabajar en esta fase)** — 5 reglas en 1 línea cada una:
   - Texto verbatim del libro (la regla de oro como recordatorio breve).
   - No inventar contenido editorial.
   - Single source of truth por capa.
   - Validar antes de cerrar.
   - Schema documental ↔ validador no divergen.
6. **Tabla "Para qué consultar qué archivo"** — 7 preguntas mapeadas a su archivo: prompt, schema, reglas-operativas, convenciones-y-casos. Mapa de navegación operativo.
7. Documentos relacionados (lista breve).

**Eliminados respecto al pre-refactor (cc1f18b: 111 líneas, 9 secciones):**

- **Sección "Reglas operativas críticas (resumen — detalle en `prompt.md`)"** de 22 líneas que reescribía contenido ahora migrado a `reglas-operativas.md` y `schema-inventario.md`. Violaba single source of truth: las mismas reglas vivían en CLAUDE como "resumen" y en los archivos de soporte como "fuente". Sustituida por 5 reglas críticas en 1 línea cada una (las que el humano debe recordar, no las que el modelo consulta para ejecutar).
- **"Coste estimado"** (no operativo, ya eliminado del prompt en A4.3).
- **"Mejora continua"** (vive ahora en `convenciones-y-casos.md` §5).
- **"Contexto futuro (cuando esta fase sea un agente CrewAI)"** — especulación sobre el futuro, no contrato operativo. CrewAI sigue bloqueado en este proyecto; reabrir solo cuando aplique.
- Sub-bloque "Lo que hace Claude Code" (4 pasos numerados duplicaban los pasos del prompt).
- Sub-sección "Errores detectados en extracción real" (4 bullets que duplican casos resueltos en `convenciones-y-casos.md` §4 + reglas decisionales en `reglas-operativas.md` §1, §3, §4, §6).

**Verificación:**

```
grep "Texto verbatim del libro|10 claves obligatorias|Taxonomía cerrada de tipos|Mis resultados en esta unidad son|produccion_escrita_guiada"
→ ningún match duplicado entre CLAUDE.md y prompt.md.
```

La única regla que aparece en CLAUDE como recordatorio ("Texto verbatim del libro") está formulada distinto del prompt ("El JSON debe contener el contenido EXACTAMENTE COMO APARECE EN EL LIBRO"). El detalle operativo de la regla vive en `prompt.md` Regla de oro; el CLAUDE solo la nombra. Es la jerarquía correcta según el plan: CLAUDE marca **lo que un humano debe recordar**, prompt expande para **ejecutar**.

**Métricas:**

| Versión | Líneas | Secciones |
|---|---|---|
| Pre-refactor (`cc1f18b`) | 111 | 9 |
| Post-A4.4 (este commit) | **57** | **7** |

Reducción 49% sobre el CLAUDE de fase pre-refactor.

**Métricas globales del refactor tras A4.4:**

| Archivo | Pre-refactor | Post-A4.4 |
|---|---|---|
| `prompt.md` | 547 | 107 |
| `CLAUDE.md` (fase) | 111 | 57 |
| `schema-inventario.md` | — | 308 |
| `reglas-operativas.md` | — | 208 |
| `convenciones-y-casos.md` | — | 165 |
| Total operativo | 658 | 845 |

El total crece (+187 líneas) porque ahora hay 5 archivos en lugar de 2, **pero cada uno tiene una responsabilidad única y no se duplican entre sí**. El prompt y el CLAUDE — los archivos que se leen en cada extracción — han bajado de 658 a 164 líneas (–75%). Los 681 líneas adicionales viven en archivos de soporte que solo se consultan cuando hace falta.

**Próximo:** A4.5 — **primera prueba funcional oficial.** Reextracción empírica de 3 casos seleccionados (página rica + U0 completa + U1-p21) usando solo los nuevos artefactos. Diff vs JSON existente. Validador con 0 errores y 0 avisos. Es el primer test de que los nuevos archivos sirven realmente para extraer.

---

## [v10.55 — 2026-05-07] — A4.3: reescritura desde cero de `prompt.md` core

Sexto sub-paso del refactor. `prompt.md` reescrito íntegramente según `REFACTOR-PROPUESTA.md` §5 paso 3, no solo consolidación.

**Estructura final del prompt core** (107 líneas, 9 secciones):

1. Header con quién/output/invocación.
2. Objetivo (1 párrafo describiendo qué produce la fase).
3. Input (PDF en `unidades/UX/fuente/`).
4. Output (1 archivo JSON).
5. Definición de éxito — **sección nueva**, no existía en pre-refactor. 4 condiciones explícitas (validador 0/0, contenido literal del libro, revisión visual del autor, casos no contemplados consultados al autor).
6. Regla de oro (no negociable) — sin cambios respecto al pre-refactor.
7. Artefactos de soporte consultados durante la extracción — cabecera global con 1 bullet por archivo hermano (`schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md`, y el validador como contrato paralelo). Reemplaza los 4-5 placeholders intermedios redundantes que tenía la versión anterior.
8. Pasos de la extracción — 11 pasos numerados (10 del pre-refactor + 1 nuevo paso 8 que captura el bloque `autoevaluacion` explícitamente). Cada paso con referencias cortas a los archivos de soporte.
9. Cierre y validación — absorbe la antigua "Validación post-extracción" + "Salida" en una sola sección con sub-encabezados (comprobaciones manuales, validador automático, salida).

**Cambios respecto a la versión post-A4.2c (108 líneas, 10 placeholders dispersos):**

- **Eliminados los 5 placeholders intermedios redundantes** que decían "Migrado a X" en zonas específicas: ya no había contenido editorial allí, solo etiquetas que la cabecera global ya cubría. Eran ruido para el lector y para el modelo.
- **Definición de éxito añadida** como sección nueva, alineada con el lenguaje del plan ("Objetivo", "Definición de éxito" en `REFACTOR-PROPUESTA.md` §3.2 y §5 paso 3).
- **Pasos enriquecidos** con un nuevo paso 8 explícito sobre el bloque `autoevaluacion` (antes implícito).
- **"Cierre y validación" absorbe Salida** en una sola sección, como pide el plan.
- **Norte de tamaño cumplido:** 107 líneas (rango 80-120 según REFACTOR-PROPUESTA §3.2).

**Verificación:**

```
grep -E "Migrado a |Migradas a |migrar a |migrarán a |migrará a |en construcción|A4.2[abc]" prompt.md
→ 0 (ningún marcador transitorio residual)

grep -E "ver sección \"|sección dedicada|de este prompt antes" prompt.md
→ 0 (ninguna referencia interna huérfana)
```

**Métricas finales del prompt core:**

| Versión | Líneas | Secciones | Estado |
|---|---|---|---|
| Pre-refactor (`cc1f18b`) | 547 | 34 | monolito mezclando 7 funciones |
| Post-A4.2c | 108 | 10 | contenido editorial migrado pero con placeholders intermedios |
| **Post-A4.3 (este commit)** | **107** | **9** | **prompt core mínimo, sin placeholders, alineado con el plan** |

**Reducción total desde inicio del refactor:** 547 → 107 líneas (–80%). Las 9 secciones del prompt core son ahora estrictamente operativas: cómo invocar, qué produce, qué condiciones de éxito, regla de oro inviolable, dónde están los artefactos de soporte, qué pasos seguir, cómo cerrar y validar.

**Próximo:** A4.4 — reescribir `CLAUDE.md` de fase en modo contrato corto. Hoy tiene 111 líneas con duplicación de reglas que ya viven en `prompt.md` y en los archivos de soporte. Objetivo: 40-60 líneas según REFACTOR-PROPUESTA.md §3.1.

---

## [v10.54 — 2026-05-07] — A4.2c: migración a `convenciones-y-casos.md` + cierre completo de A4.2

Quinto sub-paso del refactor (parte c de A4.2). Movido a `convenciones-y-casos.md` todo el contenido editorial residual del prompt: convenciones de transcripción, ejemplos canónicos por tipo de actividad, ejemplo JSON de unidad atípica, casebook de extracciones reales, política de mejora continua.

**Estructura final de `convenciones-y-casos.md`** (5 secciones, 165 líneas):

1. Convenciones de transcripción del libro al JSON (sílaba tónica subrayada hasta U3, patrón "primer ítem resuelto como ejemplo", textos de lectura, diálogos con marcadores `[1]`/`[2]`, sopas de letras y juegos).
2. Ejemplos canónicos de `items_libro` por tipo de actividad (cloze, selección múltiple, cuestionario con opciones) + ejemplos INCORRECTOS.
3. Ejemplo canónico de unidad atípica (U0 con `_nota_unidad_atipica` literal).
4. Casebook — casos resueltos en extracciones reales ("Para aprender" confundido con cuadro + 6 casos resueltos en U3).
5. Política de mejora continua (cómo se añade un caso nuevo y a qué archivo según su tipo: schema, reglas-operativas o convenciones-y-casos).

**Cambios en `prompt.md`:**
- 4 secciones movidas reemplazadas por placeholders cortos.
- Sección "Coste estimado" eliminada (no aporta valor operativo).
- Cabecera "Schema, reglas y convenciones — archivos externos" actualizada: ya no dice "convenciones-y-casos.md — en construcción".

**Lección de v10.53 aplicada proactivamente** (verificar la zona reemplazada como enlace limpio, no solo anclas movidas): detectadas y corregidas **3 referencias huérfanas** en los pasos de la extracción que apuntaban a secciones eliminadas:

- Paso 3: *"Aplicar la sección 'Reglas para unidades atípicas' de este prompt"* → `reglas-operativas.md` §7.
- Paso 4: *"ver sección 'Reglas para cuadros'"* → `reglas-operativas.md` §1 / §3 / §4.
- Paso 5: *"(ver sección dedicada)"* (sílaba tónica + primer ítem resuelto) → `convenciones-y-casos.md` §1.1 / §1.2.

Esto demuestra que la lección de "verificar zona limpia, no solo grep de anclas" está internalizada — se aplicó **antes** de que el revisor lo señalara.

**Verificación de anclas semánticas** (8 frases canónicas):

| Ancla | convenciones | prompt |
|---|---|---|
| `Pablo y Jorge (estudiar)` | 1 | 0 |
| `PABLO: Son las once` | 1 | 0 |
| `PRIMO` | 1 | 0 |
| `Punto de partida... introductoria pre-A1` | 1 | 0 |
| `se subraya la sílaba tónica` | 1 | 0 |
| `primer ítem resuelto` | 1 | 4 (referencias legítimas en pasos + cabeceras) |
| `Pronunciación con z/c` | 1 | 0 |
| `Lecturas Javier/Lucía` | 1 | 0 |

La única ancla con cuenta > 0 en prompt es "primer ítem resuelto", y todas sus apariciones son **referencias legítimas** (paso 5 + cabecera + placeholder) — no contenido editorial duplicado.

**Métricas finales A4.2c:**
- `prompt.md`: 260 → 108 líneas (–58% solo en este sub-paso; –80% desde el inicio del refactor en v10.42).
- `schema-inventario.md`: 308 (sin cambios desde A4.2a).
- `reglas-operativas.md`: 208 (sin cambios desde A4.2b).
- `convenciones-y-casos.md`: 10 → 165 líneas (recibió todo el contenido editorial residual).

**Estado del paso A4.2:** ✅ **cerrado al 100%** — (a) ✅ schema · (b) ✅ reglas-operativas · (c) ✅ convenciones-y-casos.

**Sobre A4.3:** el prompt actual de 108 líneas ya está dentro del norte de tamaño 80-120 que define la propuesta. A4.3 ("reescribir prompt.md core desde cero") podrá enfocarse más en consolidar la estructura (fusionar placeholders contiguos, ajustar la cabecera del archivo, añadir la sección "Cierre y validación" absorbida) que en reducir tamaño.

**Próximo:** A4.3.

---

## [v10.53 — 2026-05-07] — Cierre real de A4.2b: reescritura de la cabecera transicional residual

El revisor sobre `ddd9879` (v10.52, "A4.2b cerrado"): el cierre **no era válido**. Tres hallazgos.

**1 (Bloqueante) — Cabecera transicional residual reabría la contradicción.**

`prompt.md` líneas 44-52 (cabecera "Esquema y schema del JSON") seguían describiendo literalmente el estado **pre-A4.2b**:

> *"Las reglas de población semántica (...) se migrarán a `reglas-operativas.md` en A4.2b. Hasta entonces, el estado real de cada bloque decisional es: (...) Distinción crítica vive provisionalmente en este `prompt.md`... Resto de criterios... se documentarán por primera vez al construir `reglas-operativas.md` en A4.2b... Reglas de población... el resto vive provisionalmente en este `prompt.md`..."*

Mientras el resto del prompt y `reglas-operativas.md` ya describían el estado **post-A4.2b** (todo migrado y vivo en reglas-operativas). Tres afirmaciones falsas convivían con la realidad migrada en el mismo archivo. Eso reabre exactamente la contradicción de source of truth que v10.50/v10.51 cerraron.

Causa raíz: la cabecera había sido escrita en v10.51 como puente provisional pre-A4.2b. v10.52 (A4.2b) corrigió las secciones específicas pero **olvidó reescribir esta cabecera global**. Quedó "viva" describiendo un estado anterior.

**2 (Medio) — Verificación de anclas sobredeclarada.**

v10.52 verificó que 7 frases canónicas movidas estaban en `reglas-operativas.md` y ausentes de `prompt.md`. Pero el criterio real del paso 2 del plan (`REFACTOR-PROPUESTA.md` §5 paso 2) es más fuerte: **la zona reemplazada del prompt debe quedar reducida a un enlace limpio**, no solo libre de las frases concretas movidas. Esa cabecera transicional incumplía el criterio aunque ninguna frase individual exacta apareciera duplicada.

**3 (Bajo) — Cabecera REVIEW desincronizada.**

REVIEW decía "Última actualización: 2026-05-06 22:30" pero el commit `ddd9879` fue a las 23:58 (1.5 h de retraso documental).

---

**Resolución (todo en este commit):**

- **Cabecera transicional reescrita** como puente corto y verdadero (3 bullets, alineada con el estado actual): schema → `schema-inventario.md`; reglas decisionales → `reglas-operativas.md`; convenciones → `convenciones-y-casos.md` (en construcción, A4.2c).
- **Verificación reforzada con el criterio del plan:** `grep` de afirmaciones pre-A4.2b en `prompt.md` (`"se migrarán a reglas-operativas"`, `"Hasta entonces"`, `"vive provisionalmente en este .prompt"`, `"el único bloque decisional explícito"`, `"oráculo de facto"`) → todos 0. Las 3 referencias residuales a "A4.2c" son legítimas (esperan ese sub-paso, cuyas migraciones todavía no se han hecho).
- **Cabecera REVIEW** sincronizada al timestamp de este commit.
- **A4.2b vuelve a ✅ pero como "cerrado limpio en v10.53"** — el CHANGELOG y la bitácora REVIEW reconocen que v10.52 había declarado el cierre prematuramente.

**Lección aplicada (lente Anthropic-first):** la regla "cada placeholder debe ser enlace limpio" requiere verificar **toda la zona reemplazada**, no solo las frases nominalmente movidas. Cuando una cabecera describe un proceso transicional, hay que reescribirla en cuanto la transición se completa — si no, el archivo entero queda contradiciéndose. La causa raíz es la misma de A4.2a: tratar la verificación como "buscar lo que sí debería estar fuera" en vez de "comprobar que la zona está limpia y solo es enlace".

**Sin cambios de código.**

---

## [v10.52 — 2026-05-06] — A4.2b: migración del contenido decisional a `reglas-operativas.md`

Cuarto sub-paso del refactor (parte b de A4.2). Movido a `reglas-operativas.md` todo el contenido decisional del prompt: precedencias entre tipos de elemento, criterios de asignación, reglas de población de cada campo, unidades atípicas.

**Estructura final de `reglas-operativas.md`** (8 secciones, 208 líneas):

1. Precedencia entre actividad / cuadro / nota / autoevaluación.
2. Cómo asignar `tipo` (Distinción crítica `completa_huecos` vs `produccion_escrita_guiada` + nota sobre criterios implícitos del resto + política de la enumeración).
3. Cómo asignar `tipo_cuadro` (5 valores con criterios + nota de ortogonalidad seccion/tipo_cuadro).
4. Qué NO es un cuadro: "Para aprender" → actividad; "Observa" → nota.
5. Reglas de población de cada campo: `vocabulario_consolidado` (criterios para los 3 bloques), `secciones` top-level (construcción del índice), `seccion` por página (tabla con oráculo), `respuestas` (contenido y formato), `audio/imagen/video` (cuándo `presente=true`), `campo_semantico` (cuándo aplica), `items_libro` (literalidad obligatoria).
6. Cuándo se incluye u omite `autoevaluacion`.
7. Reglas para unidades atípicas (procedimiento de 4 pasos).
8. Estado del source of truth de las reglas decisionales tras A4.2b.

**Hallazgo importante durante la ejecución:** A4.2a fue **más extensiva en pérdidas** de lo identificado en v10.51. Además de la "Distinción crítica" (la única que v10.51 detectó), el placeholder grande de A4.2a había absorbido también:

- Reglas decisionales de `vocabulario_consolidado` (qué cuenta como `principal` / `recurrente` / `comprension`).
- Reglas decisionales de `respuestas` (formatos para selección múltiple, V/F, cloze).
- Reglas decisionales de `campo_semantico` (cuándo aplica + nota "liberal por ahora").
- Reglas decisionales de `secciones` top-level (construcción del índice, secciones inexistentes vacías, `actividades_ids` en orden).

Verificado con `grep` cruzado: estas frases existían en `cc1f18b` y no estaban en el prompt actual. **A4.2b las recupera todas** tomando como fuente `cc1f18b` (estado pre-refactor) y las migra directamente a `reglas-operativas.md`.

**Cambios en `prompt.md`:** sección "Reglas decisionales provisionales" (Distinción crítica) reemplazada por línea-puente. Sección "Reglas para `datos.items_libro`" pierde solo la regla de literalidad (línea-puente a §5.7) — los ejemplos correctos/incorrectos siguen aquí provisionalmente, esperando A4.2c. Sección "Reglas para unidades atípicas" pierde los 4 pasos (línea-puente a §7) — el ejemplo JSON sigue, esperando A4.2c. Sección "Reglas para cuadros" entera reemplazada por línea-puente (todo era decisional). Total: prompt pasa de 290 → 260 líneas.

**Verificación de anclas semánticas** (7 frases canónicas, todas pasan):

| Ancla | reglas-operativas | prompt |
|---|---|---|
| Distinción crítica `completa_huecos` | 1 | 0 |
| escribe texto nuevo | 1 | 0 |
| vocabulario que aparece en varias secciones | 1 | 0 |
| Selección múltiple, indicar la opción correcta | 1 | 0 |
| campo semántico identificable | 1 | 0 |
| "Para aprender" Cajas con consejos | 1 | 0 |
| "Observa" Notas que llaman la atención | 1 | 0 |

**Métricas finales A4.2b:**
- `prompt.md`: 290 → 260 líneas (−30, total desde inicio del refactor: −287).
- `schema-inventario.md`: 308 (sin cambios desde A4.2a).
- `reglas-operativas.md`: 81 → 208 líneas (recibió todo el contenido decisional + recuperación).
- `convenciones-y-casos.md`: 10 (esperando A4.2c).

**Lección aplicada del riesgo operativo señalado por el revisor:** A4.2b incluye **canonización por primera vez** de criterios que estaban implícitos antes del refactor. Pero **no he inventado criterios nuevos**: solo he migrado lo que ya estaba explícito (en prompt actual o en `cc1f18b`) o he marcado como "no canonizado todavía, oráculo de facto en U0/U1/U3" lo que sigue implícito (resto de criterios para los 17 tipos más allá de `completa_huecos` vs `produccion_escrita_guiada`). La canonización progresiva ocurre por el flujo del paso A4.5 + casos editoriales nuevos, no aquí.

**Estado del paso A4.2:** (a) ✅ schema · (b) ✅ reglas-operativas · (c) 📋 convenciones-y-casos.

**Próximo:** A4.2c — migrar a `convenciones-y-casos.md` los ejemplos correctos/incorrectos de `items_libro`, las convenciones de transcripción (textos de lectura, diálogos, sopas de letras), sílaba tónica subrayada hasta U3, patrón "primer ítem resuelto como ejemplo", casos resueltos en U3, política de mejora continua, y el ejemplo JSON canónico de unidades atípicas.

---

## [v10.51 — 2026-05-06] — Cleanup pre-A4.2b parte 2: restaurar bloque decisional perdido en A4.2a

El revisor sobre `68799b6` (v10.50): el hallazgo del source of truth de la taxonomía no quedó cerrado, solo reformulado. v10.50 alineó `prompt.md` y `reglas-operativas.md` para decir lo mismo, pero **lo que decían era falso**: ambos afirmaban "el contenido decisional canónico vive provisionalmente en `prompt.md`" cuando en el archivo real ese contenido **ya no estaba**. Verdad única alineada, pero sobre una premisa que el repo no sostenía.

**Causa raíz:** el placeholder grande que metí en A4.2a (commit `668572f`, v10.47) absorbió por error de scope el bloque "Distinción crítica `completa_huecos` vs `produccion_escrita_guiada`" del prompt pre-refactor (`cc1f18b:227-230`). Ese bloque era el **único contenido decisional explícito** sobre la taxonomía que tenía el prompt. Al sustituirlo por placeholder, dejé el archivo afirmando un source of truth que ya no existía físicamente.

**Resolución (opción A del revisor):** restaurar la verdad para que la declaración sea verdadera.

- **Bloque "Distinción crítica" recuperado** del commit pre-refactor `cc1f18b` y reinsertado en `prompt.md` como nueva sección **"Reglas decisionales provisionales (a migrar en A4.2b)"**. Texto idéntico al original, sin reescritura.
- **Placeholder grande reformulado con honestidad sobre el estado real:**
  - Distinción `completa_huecos` vs `produccion_escrita_guiada`: source of truth = `prompt.md` (sección restaurada).
  - Resto de criterios para los 17 tipos: **no canonizados todavía en ningún archivo**, implícitos del dominio editorial; oráculo de facto = inventarios trackeados U0/U1/U3. Se canonizarán al construir `reglas-operativas.md` en A4.2b.
  - 3 fragmentos absorbidos en v10.49 (autoevaluación opcional, mapeo de secciones, taxonomía revisable) viven en `reglas-operativas.md`.
- **`reglas-operativas.md` alineado simétricamente** con la misma descripción del estado.

**Verificación:**
- `grep "Distinción crítica.*completa_huecos.*produccion_escrita_guiada" prompt.md` → línea 60 (presente).
- `grep "escribe texto nuevo" prompt.md` → línea 62.
- `grep "Regla práctica.*alumno tiene que escribir" prompt.md` → línea 64.

El bloque restaurado coincide caracter por caracter con `cc1f18b`.

**Por qué se hace ahora:** A4.2b va a migrar exactamente este contenido. Si arranca con la afirmación falsa de "ya está aquí" cuando no está, el sub-paso pierde su anclaje. Restaurar la verdad antes de migrar es prerequisito para que la migración signifique algo.

**Lección registrada:** los placeholders de A4.2a fueron demasiado amplios. En A4.2b habrá que ser más quirúrgico al sustituir bloques por enlaces — verificar siempre que cada parte del bloque viejo tiene destino antes de borrarla del origen.

**Sin cambios de código.** Solo restauración de contenido editorial perdido + alineación de redacciones.

**Estado A4.2 tras este commit:** (a) ✅ schema migrado + frontera limpia · (b) 📋 reglas-operativas con adelanto parcial + bloque "Distinción crítica" pendiente de migrar desde prompt · (c) 📋 convenciones-y-casos.

---

## [v10.50 — 2026-05-06] — Cleanup pre-A4.2b: dos correcciones del revisor antes de arrancar

Dos hallazgos del revisor sobre el commit anterior `40e123c` (v10.49). Ambos resueltos antes de tocar A4.2b para que el sub-paso arranque sin inconsistencias.

**1 (Medio) — Doble verdad sobre source of truth de la taxonomía.**

Tras v10.49, el placeholder de `prompt.md` decía:
> *"Las reglas de población semántica (...distinción completa_huecos vs produccion_escrita_guiada) viven en reglas-operativas.md (se migran en A4.2b)."*

Mientras `reglas-operativas.md` decía:
> *"El criterio canónico para cada uno de los 17 tipos vive aún en prompt.md y se moverá aquí en el siguiente sub-paso."*

Los dos archivos hablaban del mismo contenido en sentidos opuestos. La realidad: el contenido decisional canónico **sigue en `prompt.md`** hasta que A4.2b lo migre.

**Resolución:** ambos archivos alineados a la verdad operativa. `prompt.md` ahora dice *"siguen viviendo provisionalmente en este `prompt.md` y se migrarán a `reglas-operativas.md` en A4.2b. Hasta que A4.2b cierre, el source of truth de esas reglas decisionales es este archivo"*. `reglas-operativas.md` confirma simétricamente *"vive provisionalmente en `prompt.md`... source of truth = `prompt.md`"*.

**2 (Bajo) — Tabla de mapeo de secciones no alineada con la práctica.**

En el adelanto parcial de v10.49, escribí en `reglas-operativas.md` la fila *"Reflexión / Autoevaluación / cierre → reflexion"*. Verificado contra los inventarios reales: las páginas de cierre con bloque `autoevaluacion` (U1-p21, U3-p43) usan `seccion: evaluacion`, no `reflexion`. Mi fila era una regla inventada sin avalar.

Verificación programática:
```
U1 p21 (con bloque autoevaluacion top-level): seccion=evaluacion
U3 p43 (con bloque autoevaluacion top-level): seccion=evaluacion
```

**Resolución:** tabla reescrita con una columna nueva "Avalado en" que cita los inventarios oráculo. La fila inventada se sustituye por *"Página de cierre de unidad con bloque `autoevaluacion` (U1-p21, U3-p43) → `evaluacion`"*. Sobre `reflexion` (que está en el enum del schema pero ningún inventario actual lo usa), se añade nota explícita: decisión diferida hasta primer caso real o hasta que A4.2b traiga la regla canónica desde el `prompt.md` actual. Mientras tanto, "usar `evaluacion` por consistencia con el oráculo".

**Por qué se hace antes de A4.2b:** ambos defectos contaminan el sub-paso siguiente. La doble verdad sobre la taxonomía es exactamente el contenido que A4.2b va a migrar — arrancar sin alinear primero significaría arrastrar la inconsistencia. La regla inventada de `reflexion` se vería confirmada al ejecutar el smoke test post-A4.4 si no se corrige ahora.

**Sin cambios de código.** Solo coherencia documental + alineación con el oráculo.

---

## [v10.49 — 2026-05-06] — Cleanup de A4.2a: 3 fugas decisionales retiradas de schema + métrica corregida

Dos hallazgos del revisor sobre el commit `668572f` (v10.47, cierre de A4.2a). Ambos se aceptan:

**1 (Medio) — Frontera schema/reglas no quedó limpia.** El revisor identificó 3 fragmentos decisionales que se habían colado en `schema-inventario.md` violando el principio "split por capa, no por campo":

- **Fuga 1, §6 (autoevaluación):** "se omite en unidades atípicas que no tienen bloque (ej. U0)". El "cuándo se omite" es decisional según el mapeo de la sección 4 de `REFACTOR-PROPUESTA.md`. La forma "el bloque es opcional a nivel top-level" sí pertenece a schema.
- **Fuga 2, §8 (enumeración seccion):** "Las páginas que continúan una sección usan la misma clave normalizada". Es regla de cómo determinar la sección, no parte de la enumeración cerrada.
- **Fuga 3, §5 (taxonomía):** la nota "Provisional y revisable... Si aparece un caso que no encaja, se marca y se consulta al autor". Workflow editorial, no contrato de datos puro.

**Resolución:** los 3 fragmentos se retiran de `schema-inventario.md` y se absorben en `reglas-operativas.md` como adelanto parcial de A4.2b. Donde antes había contenido decisional en schema queda ahora solo:
- La forma estructural correspondiente.
- Una **línea-puente** explícita del estilo "Cuándo / Cómo … → `reglas-operativas.md`".

Verificación: grep del contenido decisional concreto → `reglas=1, schema=0` en cada uno de los 3 casos. La línea-puente sí aparece en schema, pero es referencia al destino, no contenido decisional.

**2 (Bajo) — Métrica desalineada.** El CHANGELOG v10.47 y la bitácora REVIEW dijeron "300 líneas" para `schema-inventario.md` cuando el dato real era **302**. Repetición del patrón "cifras duras por aproximación" que ya se había marcado antes (v10.37). Métrica corregida en esta entrada con el valor exacto del momento de cierre de v10.49: `schema-inventario.md` 308 líneas (creció con las líneas-puente), `prompt.md` 290 (no cambia), `reglas-operativas.md` 75 (antes 8).

**Cómo se documentó honestamente A4.2a:** el "cerrado limpio" de A4.2a queda matizado retroactivamente. La fila de la tabla de sub-pasos en REVIEW.md ahora dice "(a) ✅ schema migrado + 3 fugas decisionales absorbidas en v10.49"; refleja que A4.2a fue sustancialmente correcto pero requirió este cleanup para sostener la frontera. La lección recurrente: el revisor pidió en v10.37 verificar todas las filas de cualquier "evidencia dura"; aplicado aquí significa verificar también que la frontera por capas se respetó en todo el archivo, no solo en las anclas semánticas.

**Estado A4.2 tras este commit:** (a) ✅ schema migrado + frontera limpia · (b) 📋 reglas-operativas con adelanto parcial ya hecho · (c) 📋 convenciones-y-casos.

**Próximo:** A4.2b — continuar la migración de `reglas-operativas.md` con el resto del contenido decisional del prompt (ya enumerado al final del propio archivo en sección "Pendiente de A4.2b").

---

## [v10.48 — 2026-05-06] — Regla de tipología de verificaciones por sub-paso

Antes de arrancar A4.2b, se documenta de forma explícita qué tipo de verificación corresponde a cada sub-paso del refactor. Sin esta regla, cabía la ambigüedad de tratar las verificaciones de anclas (locales, documentales) como si fueran pruebas funcionales, lo cual debilita el gate real de A4.5.

**La regla, no negociable:**

- **A4.2 → A4.4:** **solo checks locales de integridad documental.** Anclas semánticas, mapeo como checklist externo, ausencia de contenido movido en el origen, presencia en el destino, no-duplicación entre archivos. NO son pruebas funcionales — el inventario no se reextrae todavía. Estos checks atrapan errores de migración (perder texto, duplicarlo, mal asignar capa) pero no validan que los nuevos artefactos sirvan para extraer.
- **A4.5:** **primera prueba funcional oficial.** Reextracción empírica de los 3 casos seleccionados (página rica + U0 completa + U1-p21) usando solo los nuevos artefactos. Diff vs JSON existente. Validador con 0 errores y 0 avisos.
- **A4.5.5:** cross-check `schema-inventario.md` ↔ `scripts/validar_inventario.py`. Gate obligatorio antes del merge.

**Smoke test opcional tras A4.4:** se permite hacer una comprobación temprana en chat para atrapar roturas obvias antes de A4.5 (archivo que no se carga, sección huérfana, referencia muerta). **NO cuenta como gate formal ni sustituye la prueba funcional de A4.5.**

**Aplicado en:**
- `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md` §5: nota destacada al inicio del plan, antes del paso 0.
- `REVIEW.md` bloque A4: eco breve tras la tabla de sub-pasos, con referencia al detalle en REFACTOR-PROPUESTA.md.

**Por qué se documenta ahora:** la regla no es nueva en sustancia (ya estaba implícita en el diseño del paso A4.5 como prueba empírica), pero hacerla explícita evita que en sub-pasos posteriores alguien (incluido el ejecutor) confunda un check de ancla con un OK funcional. Es exactamente el patrón que el revisor pidió blindar con la "lente Anthropic-first": cada artefacto debe declarar qué tipo de validación lo respalda.

Sin cambios de código.

---

## [v10.47 — 2026-05-06] — A4.2a: migración del contenido estructural a `schema-inventario.md`

Tercer sub-paso del refactor (parte (a) de A4.2). Movido al nuevo `schema-inventario.md` todo el contenido del `prompt.md` actual cuya capa es **estructural** (forma del JSON, tipos, obligatoriedad, enumeraciones, restricciones validables sin contexto editorial).

**Contenido migrado a `schema-inventario.md`** (300 líneas, 13 secciones):

1. Estructura top-level (10 claves obligatorias + 1 opcional `_nota_unidad_atipica`).
2. Schema por página.
3. Schema por actividad (incluye declaración del saco `datos`).
4. Schema por cuadro + nota canónica `tipo_cuadro` (categoría pedagógica) vs `contenido.tipo` (estructura interna).
5. Taxonomía cerrada de 17 tipos de actividad.
6. Schema del bloque de autoevaluación (top-level opcional) con valores fijos NC1.
7. Enumeración cerrada de `tipo_cuadro` (5 valores).
8. Enumeración cerrada de `seccion` (7 valores).
9. Estructura de `vocabulario_consolidado` (3 sub-bloques con `_descripcion`).
10. Estructura de `respuestas`, `campo_semantico`, `audio`/`imagen`/`video` con la restricción condicional `imagen.descripcion` obligatoria si `presente=true`.
11. Schema de `_nota_unidad_atipica` como clave opcional contractual.
12. Estructura de `datos.items_libro` (lista de strings, obligatoriedad por tipo de actividad — contrato paralelo con `validar_inventario.py:TIPOS_QUE_REQUIEREN_ITEMS`).
13. Source of truth con `scripts/validar_inventario.py` (regla de no-divergencia explícita).

**Frontera respetada:** todo el contenido de cuándo aplicar / cómo elegir / cómo poblar permaneció en su zona del prompt para migrar en A4.2b a `reglas-operativas.md`. Ej: la enumeración de los 17 tipos vive ahora en schema, pero la "Distinción crítica `completa_huecos` vs `produccion_escrita_guiada`" sigue en prompt esperando A4.2b.

**Cambios en `prompt.md`:** 9 secciones consecutivas (Esquema canónico, Esquema por página, por actividad, por cuadro, Bloque de autoevaluación, Taxonomía 17 tipos, Reglas para `vocabulario_consolidado`, `secciones`, `seccion`, `respuestas`, `audio/imagen/video`, `campo_semantico`) reemplazadas por **un único placeholder con enlace** al schema. `prompt.md` pasa de 547 → 290 líneas.

**Verificación de anclas semánticas** (todas pasan):

| Ancla | schema | prompt |
|---|---|---|
| `Taxonomía cerrada de tipos de actividad` | 1 | 0 |
| `tipo_cuadro describe la categoría pedagógica` | 1 | 0 |
| `Mis resultados en esta unidad son` | 2 | 0 |
| `MUY BUENOS / BUENOS / NO MUY BUENOS` | 1 | 0 |

**Estado del paso A4.2:** 🔄 (a) ✅ schema · (b) 📋 reglas-operativas · (c) 📋 convenciones-y-casos.

**Próximo:** A4.2b — migrar a `reglas-operativas.md` (precedencias entre actividad/cuadro/nota/autoevaluación, reglas de población, distinción `completa_huecos` vs `produccion_escrita_guiada`, unidades atípicas, literalidad de `items_libro`).

---

## [v10.46 — 2026-05-06] — A4.1: tres archivos auxiliares creados con headers de identidad

Segundo sub-paso del refactor documental de fase 1 (ver paso A4 en `REVIEW.md` y `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md` sección 5 paso 1).

**Archivos creados** en `fases/1-extraccion-inventario/`:

- `schema-inventario.md` (8 líneas) — Contrato de datos puro. Forma del JSON, tipos, obligatoriedad, restricciones validables sin contexto editorial. Contrato paralelo con `scripts/validar_inventario.py`.
- `reglas-operativas.md` (8 líneas) — Decisión, clasificación, población y unidades atípicas. **Single source of truth de precedencias.**
- `convenciones-y-casos.md` (10 líneas) — Transcripción del libro al JSON + casebook de casos resueltos.

Cada archivo lleva solo el header de responsabilidad: qué SÍ contiene, qué NO contiene, y referencia al mapeo de la sección 4 de `REFACTOR-PROPUESTA.md` para identificar qué se moverá en A4.2.

**Ningún contenido editorial movido todavía.** `prompt.md` sigue intacto en 547 líneas. Eso es A4.2.

**Verificación:** los 3 archivos existen físicamente (`ls fases/1-extraccion-inventario/`), tienen identidad clara y citan su origen. El `prompt.md` actual no se ha tocado — la migración fila por fila es el próximo sub-paso.

**Próximo:** A4.2 (migrar contenido del `prompt.md` actual a los 3 destinos según el mapeo de la sección 4, aplicando split por capa, con verificación de anclas semánticas tras cada movimiento).

---

## [v10.45 — 2026-05-06] — Limpieza cosmética del setup de worktree

Dos residuos bajos detectados por el revisor en el commit v10.44 (`a9f710e`). Ninguno bloqueante.

**1. Tabla de estado del CHANGELOG con HEAD desfasado.** La tabla decía `guia-didactica-refactor/ ... e3ed91d` como HEAD del worktree, pero el propio commit v10.44 lo elevó a `a9f710e`. Es el problema clásico de documentar en un commit el estado tras ese mismo commit. Actualizado a `a9f710e` y añadida aclaración explícita: ese SHA es el HEAD "al cerrar v10.44"; el HEAD vivo cambia con cada commit del refactor — referencia a `git worktree list` para el estado actual del momento.

**2. `REFACTOR-WORKTREE.md` con redacción residual.** Cerraba con "commit posterior bumpeará la versión a v10.44", redactado en futuro cuando ese commit ya había ocurrido. Reescrito como referencia retrospectiva al commit `a9f710e`/v10.44.

Sin cambios operativos. Solo coherencia documental.

---

## [v10.44 — 2026-05-06] — A4.0 refinado: migración a worktree dedicado

Tras dictamen del revisor con lente Anthropic-first: la rama `refactor/prompt-fase-1` se mueve de "checked out en el directorio original" a un **worktree dedicado** en `/Users/armandocruz/Desktop/guia-didactica-refactor/`. El directorio original vuelve a `main`.

**Por qué esto es relevante (no es ceremonia):** la docs oficial de git establece que `git worktree add` crea un **checkout fresco** que **NO copia los archivos sin trackear** del checkout originante. En este repo eso se traduce en un beneficio concreto:

- En el directorio original quedan los untracked de carriles paralelos: `unidades/U2/` y `viejo/_template/`.
- En el worktree del refactor **no existen físicamente esos paths** (verificado con `ls`).
- El trabajo de A4.1-A4.6 sucede en un árbol limpio, sin riesgo de mezcla accidental con esos untracked.

Esto está alineado con la guía de Anthropic sobre Claude Code, que recomienda worktrees como mecanismo de aislamiento cuando el árbol principal acumula ruido.

**Operaciones git ejecutadas:**
- `git -C guia-didactica-profesor-IA checkout main` (devuelve el directorio original a `main`).
- `git worktree add /Users/armandocruz/Desktop/guia-didactica-refactor refactor/prompt-fase-1` (crea el directorio del refactor en hermano).
- Verificación: `git worktree list` muestra dos entradas; `ls` confirma ausencia de los untracked en el worktree.

**Estado tras la migración:**

| Directorio | Branch | HEAD | Untracked |
|---|---|---|---|
| `guia-didactica-profesor-IA/` | `main` | `cc1f18b` | `unidades/U2/`, `viejo/_template/` |
| `guia-didactica-refactor/` | `refactor/prompt-fase-1` | `a9f710e` (HEAD al cerrar v10.44; vivo cambia con cada commit del refactor — ver `git worktree list`) | (ninguno) |

**Documentación nueva:** `fases/1-extraccion-inventario/REFACTOR-WORKTREE.md` explica el setup paso a paso para que el autor pueda recuperar contexto si vuelve más tarde — incluye reglas de uso, comandos de verificación, procedimiento de cierre (merge + `git worktree remove`) y procedimiento de aborto.

**Política operativa a partir de ahora:** todos los commits de A4.1 → A4.6 se hacen en el worktree (`guia-didactica-refactor/`). El directorio original solo se toca para inspeccionar `main` o trabajar en otros frentes (Bloque B, etc.).

**Sin cambios en archivos editoriales del refactor.** Solo metadata git + documentación del setup.

---

## [v10.43 — 2026-05-06] — A4.0: tag pre-refactor + rama refactor/prompt-fase-1

Primer sub-paso del refactor documental de fase 1 (ver paso A4 en `REVIEW.md` y `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md` sección 5 paso 0).

**Operaciones ejecutadas:**
- `git tag pre-refactor-prompt-fase1` sobre HEAD del `main` (`cc1f18b`). Marcador inmutable de la base pre-refactor.
- `git checkout -b refactor/prompt-fase-1`. Rama de trabajo creada y activa.
- Verificación: `git rev-parse pre-refactor-prompt-fase1` y `git rev-parse HEAD` coinciden en `cc1f18b` (rama aún sin commits propios, parten del mismo punto).

**Política de aislamiento:**
- Todos los commits del refactor (A4.1 → A4.6) se hacen en `refactor/prompt-fase-1`, no en `main`.
- `main` queda intacto en `cc1f18b` durante todo el refactor; el dashboard en producción (Railway) y el sistema activo siguen funcionando con el `prompt.md` viejo hasta que se mergee.
- Si rollback: `git checkout main` (sin operaciones destructivas). La rama puede descartarse con `git branch -D refactor/prompt-fase-1` si no llegamos a mergear.

**No hay cambios en archivos editoriales** todavía. Solo metadata git (tag + rama) + actualización de bitácoras.

**Próximo:** A4.1 (crear los 3 archivos auxiliares vacíos con headers: `schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md`).

---

## [v10.42 — 2026-05-06] — Limpieza grep: anotaciones inline en entradas históricas con rango "27-33"

Hallazgo bajo no bloqueante del revisor: tras v10.41 (renumeración 27-33 → 28-34), dos entradas históricas seguían siendo grep-ables con el rango viejo "27-33" sin que el contexto del fix apareciera en la misma línea:

- `REVIEW.md` bitácora del 14:30 v10.40.
- `CHANGELOG.md` v10.40 sección "1. PROCESO-MAESTRO".

**Decisión:** anotación inline (opción B, propuesta al autor). Se mantiene el texto histórico porque describe lo que hizo v10.40 en su momento (fidelidad histórica), pero se le pega un inciso del tipo *"renumeradas a 28-34 en v10.41 por colisión con la Decisión 27 preexistente"*. Así, una búsqueda textual de "27-33" siempre encuentra a la vez la nota de cierre.

**Lo que NO se hace:** reescribir las entradas históricas para que digan "28-34". Eso sería revisionismo del CHANGELOG y de la bitácora — describirían lo que NO se hizo en v10.40.

**Sin cambios de código.** Todo en working tree antes de A4.0.

---

## [v10.41 — 2026-05-06] — Fix de coherencia documental: numeración duplicada en PROCESO-MAESTRO + cabecera REVIEW

Dos defectos detectados por el revisor en el commit anterior (v10.40, `e2fbfa2`).

**1 (Medio) — Numeración duplicada de "Decisión 27" en PROCESO-MAESTRO.md.**

Cuando v10.40 amplió Parte 4 con decisiones nuevas, las numeré 27-33 sin verificar que ya existía una "Decisión 27 — Arquitectura datos+instrucciones" en Parte 5 (bajo un subheader "Decisiones cerradas adicionales (post-creación inicial)" que paradójicamente vivía dentro de la sección "Decisiones pendientes"). Quedaban dos defectos:
- "Decisión 27" pasaba a ser referencia ambigua.
- Una decisión cerrada vivía bajo "Decisiones pendientes".

Resolución:
- El bloque "Arquitectura datos+instrucciones" se mueve de Parte 5 a Parte 4 (donde corresponde por estar cerrada) como nueva subsección "Sobre la arquitectura datos + instrucciones (decidida 2026-05-05)", **preservando su número 27 por antigüedad**.
- Las 7 decisiones del refactor de fase 1 que v10.40 había numerado 27-33 se **renumeran a 28-34**. La nota del CHANGELOG v10.40 que decía "decisiones 27-33" queda obsoleta como dato de cierre — la entrada actual la corrige.
- El subheader "Decisiones cerradas adicionales (post-creación inicial)" se elimina (era el síntoma de no haber consolidado en su momento).

**2 (Bajo) — Cabecera "Última actualización" de REVIEW.md desactualizada.**

Decía `2026-05-06 12:00` cuando la bitácora ya tenía entradas a las 14:30. Sincronizada a `15:00` (timestamp de este fix).

**Por qué corrección antes de A4.0:** el revisor lo trató como bloqueante ligero del paso siguiente porque PROCESO-MAESTRO se usa como ancla canónica del plan; arrancar el refactor sobre numeración ambigua propaga la ambigüedad a todos los commits del refactor.

---

## [v10.40 — 2026-05-06] — Refactor de fase 1 documentado como plan ejecutable

Antes de empezar la ejecución del refactor (v10.35-v10.39 cerraron solo la propuesta), trazo el plan en los dos artefactos canónicos para evitar el patrón "trabajo solo en bitácora, no en plan" que el revisor ya señaló con Railway.

**1. `PROCESO-MAESTRO.md` — Parte 4 ampliada con 7 decisiones cerradas (27-33, *renumeradas a 28-34 en v10.41 por colisión con la Decisión 27 preexistente — ver entrada v10.41*)**

Nueva subsección "Sobre la arquitectura documental de las fases (refactor de fase 1, decidido 2026-05-06)":
- Decisión 27: refactor aprobado tras 6 rondas.
- Decisión 28: arquitectura objetivo de 5 archivos.
- Decisión 29: frontera de capas no negociable (forma vs decisión).
- Decisión 30: single source of truth de precedencias en `reglas-operativas.md`.
- Decisión 31: skill fuera de v1.
- Decisión 32: schema y validador como contratos paralelos sin divergencia en el merge.
- Decisión 33: REFACTOR-PROPUESTA.md como source of truth operativa; PROCESO-MAESTRO no duplica detalle.

Bitácora del documento actualizada con la entrada de cierre de propuesta.

**2. `REVIEW.md` — Paso A4 insertado en bloque A**

Nuevo paso A4 "Refactor documental de fase 1" con 8 sub-pasos enumerados (A4.0 → A4.6 + A4.5.5 cross-check obligatorio). Tabla de sub-pasos como marcador interno; cada commit del refactor citará su sub-paso en el mensaje. Gate de cierre con 5 condiciones explícitas (incluida cero divergencia schema↔validador).

Estado global del bloque A actualizado: `🔄 A4 refactor documental en curso`.

**Por qué este commit antes de tocar código:** sin paso formal en REVIEW + decisión registrada en PROCESO-MAESTRO, cada commit del refactor no tendría dónde anclarse en el plan, repitiendo el patrón Railway / fix Mermaid / build slim que el revisor ya criticó. Esto se hace una vez, antes de empezar.

**No hay cambios de código.** Solo documentación del plan ejecutable.

---

## [v10.39 — 2026-05-06] — REFACTOR-PROPUESTA: dos rastros residuales tras v10.38

Dos hallazgos bajos del revisor, ambos consecuencia incompleta de las correcciones de v10.38.

**1. Tabla de riesgos seguía hablando de "checklist".** En v10.38 reformulé el paso 2 para no exigir un checklist (la sección 4 es una tabla simple) y sustituirlo por marcador externo de progreso. Pero la mitigación correspondiente en la tabla de riesgos seguía diciendo "Mapeo explícito como checklist". Sustituido por la formulación coherente con paso 2: "Mapeo de la sección 4 como referencia inmutable + marcador externo de progreso (PR description o comentario fijado de sesión) + búsqueda de anclas semánticas + prueba empírica del paso 5".

**2. Verificación de anclas asumía un estado que no existe en paso 2.** El subpaso decía que tras mover una sección, el `grep` del ancla "debe aparecer en exactamente un archivo nuevo y **desaparecer del prompt core**". El problema: el prompt core como tal no existe hasta el **paso 3** (reescritura desde cero). Durante el paso 2, `prompt.md` contiene una mezcla de placeholders (donde ya se movió contenido) y secciones aún no migradas. Reformulado para respetar la secuencia:

- Tras mover la sección S → archivo destino D, `grep` de cada ancla debe aparecer en D.
- `grep` en la zona de `prompt.md` que se sustituyó por placeholder NO debe encontrarla.
- En otras zonas de `prompt.md` aún no migradas, el ancla puede seguir apareciendo (se verifica al procesar su fila).
- La comprobación final "ancla solo en un sitio" se completa al cerrar el **paso 3**, no el paso 2.

Estos dos defectos son del mismo tipo que ya señalamos en v10.37: cuando una corrección toca una zona del documento, hay que verificar las **referencias cruzadas** que pudieran haber quedado obsoletas. Lección registrada también en v10.37.

---

## [v10.38 — 2026-05-06] — REFACTOR-PROPUESTA: cuatro correcciones de coherencia interna

Cuatro defectos detectados por el revisor en la propuesta de refactor (tres bajos + uno medio). Todos eran defectos del propio documento, no del trabajo subyacente.

**1 (Medio) — Mapeo de unidades atípicas violaba la frontera por capas.** El propio documento declara "split por capa, no por campo" (sección 4 cabecera + sección 3.3 + sección 3.4), pero la fila del mapeo "395-411 Reglas para unidades atípicas" mandaba el bloque entero a `reglas-operativas.md`, ignorando que el bloque del prompt mezcla:
- *Forma:* declaración de `_nota_unidad_atipica` como clave opcional contractual del top-level → debe ir a `schema-inventario.md`.
- *Decisión:* cuándo añadirla, cómo mapear secciones vacías, valor especial de `contenidos_indice` → `reglas-operativas.md`.
- *Ejemplo canónico:* el JSON literal de U0 → `convenciones-y-casos.md`.

Fila reescrita con los tres destinos. Línea de paso 5 sobre el caso U0 también corregida (decía "se acaban de mover a reglas-operativas.md", lo cual era impreciso).

**2 (Bajo) — Subpaso de "checklist" no era ejecutable literalmente.** El paso 2 decía "marcar la fila correspondiente en el mapeo de la sección 4 como hecha (checklist)", pero la sección 4 es una tabla simple, no un checklist con casillas. Reformulado para describir una mecánica realmente ejecutable: la tabla queda como referencia inmutable, el progreso se anota en un marcador externo (descripción del PR de la rama o comentario fijado de la sesión).

**3 (Bajo) — Anclas semánticas inventadas.** Los ejemplos de anclas que cito ("principio de género no marcado", "literalidad del contenido visible al alumno") **no aparecen en `prompt.md` actual**. La primera está en otro artefacto del proyecto; la segunda en `PROCESO-MAESTRO.md`. Sustituidas por frases que sí están en el prompt y son distintivas: *"Taxonomía cerrada de tipos de actividad"*, *"tipo_cuadro describe la categoría pedagógica"*, *"primer ítem resuelto como ejemplo"*.

**4 (Bajo) — Cifra de ejecuciones inexacta.** El argumento contra encapsular la fase como skill se apoyaba en "9 ejecuciones en NC1". El scope real es **10 unidades (U0-U9)**: U0 atípica + U1-U9 regulares (verificado contra `CLAUDE.md` raíz y `README.md`). La conclusión (skill fuera de v1) no cambia, pero la cifra ahora es exacta. Aplicado en las dos referencias del documento (cabecera de sección sobre skill + sección 3.5 final).

Los datos cuantitativos restantes (547/27/37 para `prompt.md`, 111/9/10 para `CLAUDE.md` fase, conjuntos 17/5/7/3 del validador, casos U3-p36 y U1-p21) ya estaban correctos y no cambian.

---

## [v10.37 — 2026-05-06] — REFACTOR-PROPUESTA: fix completo de la tabla "Estado medido"

La corrección de v10.36 fue **parcial**: arregló la fila de `prompt.md` (34→27/37) pero dejó intacta la fila de `fases/1-extraccion-inventario/CLAUDE.md`, que decía `7 | 11` cuando el conteo real es **9 | 10** (`grep -cE "^## "` y `grep -cE "^#{1,6} "`). El error de origen viene de cuando creé la primera tabla mezclando `^## ` y `^### ` en un grep combinado.

Ahora la tabla "Estado medido (no opinión)" es íntegramente reproducible contra el filesystem.

**Verificación cruzada del resto de cifras del documento** (no se han modificado, todas correctas hoy):
- `TIPOS_VALIDOS` (17), `TIPOS_CUADRO_VALIDOS` (5), `SECCIONES_CANONICAS` (7), `NC1_OPCIONES` (3) — confirmadas contra `scripts/validar_inventario.py`.
- `prompt.md`: 547 líneas, 27 `##`, 37 totales.
- `CLAUDE.md` fase: 111 líneas, 9 `##`, 10 totales.

**Aviso de proceso:** la afirmación de cierre del CHANGELOG v10.36 ("la cifra 34 era un cálculo intermedio mal etiquetado, tabla reescrita") era demasiado fuerte: solo se había corregido una fila. Esta entrada cierra el conteo entero. La lección queda: cuando una tabla es "evidencia dura", verificar **todas** sus filas, no solo la que motiva la revisión.

---

## [v10.36 — 2026-05-06] — REFACTOR-PROPUESTA: dos correcciones tras dictamen del revisor

Dos defectos detectados en `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md` justo después de commitear v10.35. Ambos corregidos ahora, sin tocar el código de producción.

**1. Conteo de secciones de `prompt.md` incorrecto.** La tabla "Estado medido (no opinión)" afirmaba 34 secciones top-level. La medición real es **27 secciones `##`** (37 si se cuentan todos los headings `#` a `######`). La cifra 34 era un cálculo intermedio mal etiquetado. Tabla reescrita con dos columnas claras (`##` vs total) + nota sobre cómo se reproduce el conteo (`grep -cE "^## "`). Cuando un dato se presenta como "evidencia dura", debe ser exactamente reproducible.

**2. Contradicción interna sobre el validador.** Las secciones 3.3, 5.5 y 6 reconocían una divergencia presente entre `schema-inventario.md` y `validar_inventario.py` (la clave `_nota_unidad_atipica` declarada opcional contractual en el schema vs. tratada como no-canónica por el validador) y exigían alinear el validador antes del merge. Pero la sección 8 (scope) afirmaba "No se toca `scripts/validar_inventario.py`" y hablaba de "si en el futuro se detecta divergencia", como si la divergencia fuese hipotética. Sec. 8 reescrita para eliminar la ambigüedad:

- El refactor nominal es documental (no toca el validador en sus commits propios).
- La divergencia conocida hoy (no futura) será detectada por el paso 5.5.
- La alineación del validador se hace en **commit aparte antes del merge**, técnicamente fuera del refactor nominal pero **prerequisito ineludible del merge a `main`**.

Lo que aclara la frontera: "fuera del scope nominal" no equivale a "opcional o aplazable"; es prerequisito del cierre del refactor.

**Aviso de proceso:** estos dos defectos estaban en `REFACTOR-PROPUESTA.md` cuando se commiteó en v10.35 (commit `d15a0dd`). El commit anterior fijó la contradicción en `main` antes de cazarla. Esta entrada cierra el ciclo.

---

## [v10.35 — 2026-05-06] — Sincronización REVIEW con trabajo real + propuesta de refactor de fase 1

Dos cambios documentales que cierran inconsistencias de larga data, sin tocar código de producción.

**1. `REVIEW.md` — sincronización del plan con el trabajo realmente ejecutado**

Tras dictamen del revisor, el documento tenía doble verdad operativa: la bitácora apuntaba a Railway como "próximo paso" pero el plan no contenía paso/gate para ese trabajo (que ya estaba hecho). Y la nota del bloque B decía que `nc1-reciclaje.json` requería "definir antes de implementar" pero B2 lo asumía diseñado. Aplicado:

- Insertado **B1.5** (diseño formal de `nc1-reciclaje.json` con gate propio, ubicado entre B1 y B2 porque B1 no depende del reciclaje). B2 declara pre-condición explícita "B1 cerrado + B1.5 cerrado".
- Insertado **B5** como ✅ CERRADO 2026-05-06, marcado explícitamente como carril paralelo ejecutado fuera del orden B1-B4. Documenta retroactivamente Railway + build slim + fix ortográfico Mermaid (commits `5024914`, `3611bd7`, `b3b07e2`).
- Tabla de Contenido editorial reestructurada (formato híbrido: U0/U1/U3 individuales con estado real verificado contra filesystem; **U2 con estado real reportado** — solo working tree, no trackeado, no valida con 2 errores de `autoevaluacion.emoticonos`; U4-U9 agrupadas como carpetas vacías).
- Cabecera "Última actualización" corregida (estaba 22h atrás respecto a la bitácora real).
- Conteo "(196 líneas)" de `CLAUDE.md` retirado por volátil — ahora son 100 líneas.
- "A3 (verificar bug B3)" como próxima modificación de `diagrama.py` retirada (A3/B3 cerrados desde hace tiempo).
- Bitácora del 11:00 reescrita: ya no afirma "Próximo paso: crear proyecto Railway..." (contradecía el estado real).
- Estado global del bloque B refleja el nuevo árbol de pasos (B1.5 en diseño, B5 cerrado fuera de orden).

**2. `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md` — propuesta aprobable**

Documento autocontenido de 5 archivos como objetivo (CLAUDE.md fase, prompt.md core, schema-inventario.md puro, reglas-operativas.md, convenciones-y-casos.md). Skill fuera de v1. Tras 4 rondas de revisión, incorpora:

- Split por capa (estructural vs decisional), no por campo, para no reconstruir el monolito con piel nueva.
- Mapeo línea-a-línea del prompt.md actual a destinos.
- Rollback no destructivo (tag + rama, sin `git reset --hard`).
- Verificación semántica (anclas + checklist) en vez de `wc -l`.
- Prueba empírica de reextracción de 3 casos (página rica + U0 completa + U1-p21), no simulacro mental.
- Cross-check schema ↔ validador como gate obligatorio antes del merge (paso 5.5).
- Tratamiento estricto de `_nota_unidad_atipica` como opcional contractual (implica alineación del validador en commit aparte antes del merge).
- Oráculo de regresión por caso (0 errores + 0 avisos en estado pre-merge).
- Single source of truth de precedencias en `reglas-operativas.md`.
- Merge gate enumerado explícitamente (pasos 0-5.5 sin excepciones).

La propuesta queda **aprobada documentalmente** pero **no ejecutada todavía**. La ejecución del refactor se hará en rama propia cuando el autor dé luz verde.

**Nota sobre commits previos sin bumpeo de versión:** la entrada v10.33 (commit `b3b07e2`) ya regularizó el commit `5024914` que no había bumpeado. Esta entrada v10.35 es de cierre limpio: cubre exactamente el trabajo aplicado en este commit.

---

## [v10.34 — 2026-05-06] — Build slim para Railway: quitadas deps no usadas

Preparación del despliegue del dashboard en Railway. Eliminadas las dependencias que el dashboard no usa:

- **`requirements.txt`:** quitados `crewai[litellm]==1.9.3`, `langfuse==2.60.10` y `deepeval==3.8.9`. Quedan solo `psycopg2-binary` (BD lazy) y `python-dotenv` (.env). Verificado que ningún módulo activo (fuera de `viejo/`) los importa.
- **`Dockerfile`:** quitada la instalación de `curl`, `nodejs` y `promptfoo` (CLI no usada por el dashboard). Mantengo `gcc` y `libpq-dev` para que `psycopg2-binary` compile en Debian slim.

Impacto esperado: build de Railway ~3× más rápido y ~5× menos RAM en el contenedor. Las páginas del dashboard que dependen de BD (tarjetas, correcciones, reglas, agentes, trazas) seguirán sin BD configurada — los endpoints fallarán cuando se invoquen, pero las vistas de Inventarios y Proyecto, que es lo que se va a compartir con el equipo, funcionan sin BD ni Langfuse.

---

## [v10.33 — 2026-05-06] — Tildes y eñes en etiquetas de los diagramas Mermaid

Corregida la ortografía en las etiquetas visibles de los 3 diagramas Mermaid del dashboard (commit `5024914`, pusheado antes de bumpear versión — entrada retroactiva del CHANGELOG):

- **Nivel 1 (Arquitectura activa):** Compañeros, extracción, revisión, raíz.
- **Nivel 2 (Flujo de fase 1):** Validación (×2), añaden.
- **Nivel 3 (8 fases):** Extracción, Análisis, Píldoras, Generación, sección, versión.

El ERD no se toca (nombres de tablas/columnas en convención SQL sin acentos). Las rutas de archivo reales (`fases/1-extraccion-inventario/`) tampoco se acentúan porque son paths del filesystem.

---

## [v10.32 — 2026-05-05] — Bloque de autoevaluación como campo top-level

**Decisión de diseño:** el bloque "Mis resultados en esta unidad son: MUY BUENOS / BUENOS / NO MUY BUENOS" del cierre de unidad NO es actividad ni cuadro ni nota. Es un elemento estructural recurrente y va como campo top-level `autoevaluacion` del JSON. Opcional (omitir en unidades atípicas).

**Schema:**
```jsonc
"autoevaluacion": {
  "pagina": <int>,
  "instruccion_original": "Mis resultados en esta unidad son:",
  "opciones": ["MUY BUENOS", "BUENOS", "NO MUY BUENOS"],
  "emoticonos": true
}
```

**Archivos modificados:**
- `unidades/U1/U1-nc1-inventario.json` — añadido top-level `autoevaluacion` (p21); eliminado `_nota` redundante de p21-act6 que solo describía el bloque.
- `unidades/U3/U3-nc1-inventario.json` — añadido top-level `autoevaluacion` (p43), antes no estaba capturado.
- `unidades/U0/U0-nc1-inventario.json` — sin cambios (unidad atípica, no tiene bloque).
- `scripts/validar_inventario.py` — `CLAVES_TOP_OPCIONALES` + validación estricta del campo si existe: presencia de los 4 sub-campos (`pagina`, `instruccion_original`, `opciones`, `emoticonos`), tipos correctos, lista de 3 strings, y valores fijos NC1 cuando `curso == "nc1"` (instrucción literal, opciones canónicas, emoticonos=true).
- `fases/1-extraccion-inventario/prompt.md` — schema top-level + sección dedicada "Bloque de autoevaluación".
- `fases/1-extraccion-inventario/CLAUDE.md` — regla añadida al resumen operativo.
- `diagrama.py` — ERD: nueva entidad `autoevaluaciones(unidad_id, pagina, instruccion_original, opciones, emoticonos)`.
- `web/index.html` — bloque renderizado en el dashboard entre el índice y las pestañas de páginas.
- `PROCESO-MAESTRO.md` — schema top-level documentado.

**Validación post-migración:** U0 → 1 aviso intencional; U1, U3 → 0 avisos.

---

## [v10.31 — 2026-05-05] — Schema cuadros: cuadros_gramaticales → cuadros + tipo_cuadro

**Decisión de diseño:** los cuadros de referencia de una página no son siempre gramaticales. La clave `cuadros_gramaticales` se reemplaza por `cuadros` con discriminador `tipo_cuadro`.

**Valores de `tipo_cuadro`:** `gramatical | lexical | fonetico | cultural | comunicativo`.

**Archivos modificados:**
- `unidades/U0/U0-nc1-inventario.json` — 1 cuadro migrado (Saludos → `cultural`, fórmulas sociales según taxonomía).
- `unidades/U1/U1-nc1-inventario.json` — 10 cuadros migrados: 4 `gramatical` (p14), 1 `lexical` (Los colores, p15), 1 `fonetico` (Pronunciación y ortografía, p15), 2 `cultural` (Saludos y despedidas + Mini-diálogos ilustrados, p20), 2 `comunicativo` (¿Tú o usted? + Estilo informal/formal, p20).
- `unidades/U3/U3-nc1-inventario.json` — 3 cuadros migrados (todos `gramatical`).
- `scripts/validar_inventario.py` — `TIPOS_CUADRO_VALIDOS` + validación de `tipo_cuadro` + detector de clave obsoleta.
- `fases/1-extraccion-inventario/prompt.md` — schema de página, schema de cuadro (renombrado), sección de reglas reescrita con 5 valores y nota de ortogonalidad sec/tipo.
- `fases/1-extraccion-inventario/CLAUDE.md` — reglas operativas: añadida la regla de cuadros no gramaticales.
- `diagrama.py` — ERD: entidad `cuadros_gramaticales` → `cuadros` con campo `tipo_cuadro`.
- `web/index.html` — clave `.cuadros`, título "Cuadros", badge `tipo_cuadro` visible.
- `PROCESO-MAESTRO.md` — esquema por página actualizado.

**Validación post-migración:** `python3 scripts/validar_inventario.py 0/1/3` → U0: 1 aviso intencional; U1: 0 avisos; U3: 0 avisos.

---

## [v10.30 — 2026-05-05] — Pasada exhaustiva completa_huecos → produccion_escrita_guiada

**18 actividades recategorizadas en total:** 4 en v10.29 y 14 en este commit (6 en U1, 8 en U3).

Criterio aplicado:
- El alumno **escribe aplicando una regla** → `produccion_escrita_guiada`.
- El alumno **selecciona de un banco dado** ("palabras del recuadro") → `completa_huecos`.

Quedan **3 casos legítimos como `completa_huecos`**: U1-p13-act8, U1-p18-act2, U3-p38-act01.
Los JSON tocados en esta pasada (U1 y U3) validan con 0 avisos. U0 conserva 1 aviso intencional (`_nota_unidad_atipica`).

---

## [v10.29 — 2026-05-05] — Recategorizar escritura guiada + alinear regla Observa (commit fbcf523)

4 actividades recategorizadas a `produccion_escrita_guiada`:
- U1-p13-act7: escucha y escribe letras (g/j, b/v, h).
- U3-p39-act09: completar palabras con z/c.
- U3-p43-act01: completar formas verbales.
- U3-p37-act09: "Para aprender" — de `expresion_escrita_libre` a `produccion_escrita_guiada`.

Regla "Observa" alineada en prompt.md y CLAUDE.md con split actividad/cuadro.
Distinción explícita `completa_huecos` vs `produccion_escrita_guiada` añadida en prompt.md con regla práctica.

---

## [v10.28 — 2026-05-05] — SERVER_VERSION automático desde CHANGELOG + prefijo v (commit 56fd923)

- `SERVER_VERSION` ya no está hardcodeado en `diagrama.py`. Se lee automáticamente de la primera línea `## [vX.Y...]` del `CHANGELOG.md` al arrancar el servidor.
- Cada nuevo commit con entrada en CHANGELOG actualiza la versión del dashboard sin intervención manual.
- `/api/version` devuelve el número de versión sin prefijo "v" (el JS del dashboard lo añade).
- CHANGELOG: añadidas entradas v10.26 y v10.27 que faltaban al inicio.

---

## [v10.27 — 2026-05-05] — Schema cuadro_gramatical + campo observaciones

- Campo opcional `observaciones` añadido al schema de cuadro gramatical para representar la caja "Observa" cuando acompaña a un cuadro (no a una actividad).
- Regla "Observa" ahora distingue dos casos: actividad → `datos._nota`; cuadro → `cuadro.observaciones`.
- CHANGELOG v10.22 actualizado para distinguir correctamente "Para aprender" (actividad) de "Observa" (nota).

---

## [v10.26 — 2026-05-05] — Terminología ELE completa — U1 + docs actualizados

- Completar v10.25: U1 faltaba. 6x `interaccion_oral`, 3x `expresion_oral_libre`, 2x `expresion_escrita_libre` en U1.
- CLAUDE.md fase 1: "Para aprender" tipo corregido a `produccion_escrita_guiada`.
- PROCESO-MAESTRO, REVIEW, CHANGELOG actualizados.

---

## [v10.25 — 2026-05-05] — Terminología ELE correcta en taxonomía de tipos

Renombres en los 3 JSONs (U0, U1, U3), validador, prompt y CLAUDE.md de fase 1:
- `produccion_oral_pareja` → **`interaccion_oral`** (parejas/grupos = interacción)
- `produccion_oral_libre` → **`expresion_oral_libre`**
- `produccion_escrita_libre` → **`expresion_escrita_libre`**
- `produccion_escrita_guiada` se mantiene (correcto para escribir con guía)

Nueva regla: `completa_huecos` cuando el alumno ESCRIBE → `produccion_escrita_guiada`. `completa_huecos` queda para seleccionar/encajar sin producir texto.
Regla de precedencia oral añadida: 2+ personas → `interaccion_oral`; alumno solo → `expresion_oral_libre`.

---

## [v10.24 — 2026-05-05] — Alinear Observa/Para aprender — dictamen del revisor (commit 183a151)

3 correcciones de coherencia documental tras dictamen:

1. `fases/1-extraccion-inventario/CLAUDE.md` resumen operativo: corregido. "Observa" y "Para aprender" no son ambas actividades — "Observa" es nota, no actividad aunque use imperativo.
2. `prompt.md` regla práctica: precedencia explícita entre los 4 casos. Las excepciones "Para aprender" (actividad) y "Observa" (nota) tienen prioridad sobre la regla general de numeración.
3. `prompt.md` paso 4 flujo principal: "actividades (numeradas)" → "actividades (numeradas o identificadas como tales — ver reglas)".

---

## [v10.23 — 2026-05-05] — Coherencia documental A1/A3 — dictamen del revisor (commit 411ac8b)

3 correcciones de coherencia documental tras dictamen:

- `PROCESO-MAESTRO.md` bugs B1-B4: sección reescrita de "bloqueantes del paso C pendientes" a "CERRADOS 2026-05-05" con las 4 decisiones explícitas del autor.
- `REVIEW.md` A1: paso reescrito de "pendiente como tarea independiente" a "CERRADO 2026-05-05" (47 actividades validadas por el autor, validador OK, prompt con casos resueltos en U3).
- `REVIEW.md` cabecera: 21:30 → 22:00; estado global Bloque B: "Pendiente" → "Parcial — reciclaje en diseño; tarjetas espera fase 2; píldoras espera fase 5".
- CHANGELOG: añadidas entradas v10.21 y v10.22 que faltaban.

---

## [v10.22 — 2026-05-05] — Regla "Para aprender" vs cuadros_gramaticales en prompt fase 1

Error detectado en extracción real de otra unidad: la caja "Para aprender" de páginas de Gramática fue clasificada como `cuadros_gramaticales`. Corregido en `fases/1-extraccion-inventario/prompt.md` y `CLAUDE.md` con distinción explícita: cuadros gramaticales = tablas de referencia sin número ni instrucción; **"Para aprender" = actividad**; **"Observa" = nota** (en `datos._nota` si acompaña actividad, o en `cuadro.observaciones` si acompaña cuadro gramatical).

---

## [v10.21 — 2026-05-05] — Cierre Bloque A + decisiones Bloque B

- **A1 cerrado:** autor validó 47 actividades de U3 sin errores.
- **A3 cerrado** con 4 decisiones: B1 pospuesto (CrewAI bloqueado), B2 aceptado (viejo sin trackear), B3 resuelto (v10.15), B4 sin acción (cosmético).
- **Bloque B parcializado:** tarjetas espera fase 2, píldoras espera U3 vocabulario, `nc1-reciclaje.json` en diseño.

---

## [v10.20 — 2026-05-05] — REVIEW cabecera fecha sincronizada (commit ccb19ee)

- `REVIEW.md` cabecera "Última actualización": 18:30 → 21:30. La bitácora ya tenía entradas a 21:00 y 21:30 pero la cabecera seguía en 18:30. Sincronizada.

---

## [v10.19 — 2026-05-05] — Rebajar afirmación "arquitectura limpia" en CHANGELOG v10.17 (commit 569b775)

Hallazgo del revisor: el título "arquitectura limpia" era demasiado fuerte. Lo que se limpió fue solo el diagrama mermaid_level1 (eliminada caja `viejo/`). El código sigue conteniendo referencias legacy a `viejo/repertorios/*.md` en `diagrama.py:550-557` (dict `AGENTS`).

- `CHANGELOG.md` v10.17 título: "arquitectura limpia" → "diagrama activo sin caja viejo".
- Nota explícita de alcance añadida en la entrada v10.17.
- `PROCESO-MAESTRO.md` y `REVIEW.md`: bitácoras actualizadas con la rebaja documentada.

Lo que el revisor sí valida: cero hardcoded U01-U09 en la UI, sidebar con AGENTES bloqueado, zoom mermaid implementado, A2 cerrado con reserva (reproducibilidad pendiente explícita).

---

## [v10.18 — 2026-05-05] — Actualizar SERVER_VERSION a 10.17 (commit aac85bf)

- `diagrama.py` `SERVER_VERSION`: corregido de `"8.5"` (congelado desde hace varios commits) a `"10.17"`.
- Verificación: `/api/version` devuelve `{"version": "10.17"}`.

---

## [v10.17 — 2026-05-05] — Dashboard refinado: sidebar reorganizado + zoom diagramas + diagrama activo sin caja viejo

> **Honestidad sobre el alcance:** este commit limpia el **diagrama mermaid_level1 (Arquitectura activa)** quitándole la caja `viejo/`. NO es una "arquitectura limpia" general: el código sigue conteniendo referencias legacy a `viejo/repertorios/*.md` en `diagrama.py:550-557` (dict `AGENTS`), usadas por el flujo de agentes que está bloqueado pero no eliminado. La migración completa de esas referencias está documentada como pendiente en `PROCESO-MAESTRO.md` Parte 5 (estructura física) y bug B2.

### Sidebar
- 3 botones top-level en MAYÚSCULAS: **INVENTARIOS**, **PROYECTO**, **AGENTES**.
- AGENTES marcado como **BLOQUEADO** (visible pero deshabilitado, no se usa por ahora).
- Selector "Unidad" y lista de secciones del flujo viejo de agentes ocultos (`display:none`), no eliminados, por si se reactivan en el futuro.

### Diagramas
- Diagrama "Arquitectura activa": eliminada la caja `viejo/`. El diagrama ahora refleja solo el sistema activo.
- Añadidos botones **−** / **+** / **100%** + indicador de porcentaje sobre cualquier diagrama Mermaid (transform scale). Resuelve diagramas que se veían pequeños.

### Limpieza UI
- Eliminadas 3 referencias residuales a `padStart(2,'0')` en vistas del flujo de agentes (líneas 1089, 1119, 1182). Aunque AGENTES está bloqueado, el código queda consistente con la convención sin cero. **Cero referencias hardcoded a U01-U09 en la UI.**

---

## [v10.16 — 2026-05-05] — Arquitectura del dashboard refleja solo lo verificado

Reescritos los 5 diagramas Mermaid del panel "Proyecto":
- **mermaid_level1 (Arquitectura activa):** Libro → PDF → Claude Code (con prompt) → JSON → Validador/Dashboard → Autor.
- **mermaid_level2 (Flujo fase 1):** 8 pasos del pipeline real con bucle de aprendizaje.
- **mermaid_level3 (8 fases con estado):** F1 OPERATIVA (verde), F2-F8 PENDIENTE (gris).
- **mermaid_level4 (Estado por unidad):** U0..U9, verde si JSON existe, gris si no.
- DIAGRAM_LABELS actualizadas.

---

## [v10.15 — 2026-05-05] — Dashboard real con U0-U9 + A2 cerrado con reserva

- `web/index.html`: selector línea 499, status grid línea 791, título sección línea 808 — todos sin `padStart(2,'0')`.
- `diagrama.py`: línea 749 hardcoded `U03` → `U3`. Línea 758 path corregido.
- REVIEW.md: A2 reformulado como "CERRADO CON RESERVA" (reproducibilidad pendiente).

---

## [v10.14 — 2026-05-05] — Cierre real de A2 (5 ajustes tras dictamen del revisor)

- REVIEW: A1/A2 sin contradicciones, paralelismo documentado.
- CHANGELOG: añadidas v10.12, v10.13.
- Prompt fase 1: excepción U0 integrada en flujo principal (pasos 1, 3, 5).
- README: estado actual menciona U0.
- diagrama.py: UNITS = U0..U9.

---

## [v10.13 — 2026-05-05] — Convención U0 en docs + 3 reglas nuevas en prompt fase 1

Tras validación del autor de v10.12, se aplican las mejoras detectadas durante la primera extracción de una unidad nueva (U0):
- **CLAUDE.md, README.md, PROCESO-MAESTRO.md:** convención de naming actualizada a `U0/, U1/, U2/...U9/` (U0 reservado a unidad introductoria atípica "Punto de partida").
- **`fases/1-extraccion-inventario/prompt.md`:** 3 secciones nuevas — (1) "Reglas para unidades atípicas (introductorias)"; (2) "Convención editorial: sílaba tónica subrayada hasta U3"; (3) "Patrón primer ítem resuelto como ejemplo".
- **REVIEW.md:** A2 marcado cerrado (Fase 1 operativa con U3 y U0).
- Bitácoras de PROCESO-MAESTRO y REVIEW actualizadas.

Pendiente del autor: confirmar con la editora si "limón" duplicado en U0 p.11 act.8 (items 7 y 8) es errata real del libro.

---

## [v10.12 — 2026-05-05] — Extracción de U0 (Punto de partida) + fix renderer dashboard

Cierra el gate **A2** del REVIEW (probar el sistema con una unidad nueva) — primer test del prompt versionado de fase 1 con un PDF distinto a U3.

### Movimientos físicos
- `unidades/U0/U0-nc1-inventario.json` (10 actividades, 4 páginas).
- `unidades/U0/fuente/U0-nc1.pdf` (gitignored).

### Convención unificada
- Sin cero a la izquierda incluyendo U0 (no U00). El dígito 0 en U0 NO es cero a la izquierda, es el número.

### Fix de bug
- `web/index.html` renderInventario: distingue cuadrícula (sopa de letras, celdas de ≤1 char) vs tabla de pares (letras_y_ejemplos del abecedario). Antes superponía letra y ejemplo.

### Casos nuevos detectados (aplicados en v10.13)
1. Convención U0 explícita en docs.
2. Unidades atípicas sin las 5 secciones canónicas.
3. Convención editorial: sílaba tónica subrayada hasta U3.
4. Patrón "primer ítem resuelto como ejemplo".

### Verificación
- `python3 scripts/validar_inventario.py 0` → ✅ JSON válido, 1 aviso intencional.
- Autor validó visualmente.

---

## [v10.3 — 2026-05-05] — Disolución de `nuevo/`: el sistema activo vive en raíz

### Motivo
Tras validar la fase 1 (extracción del JSON con el nuevo schema), el autor decide promocionar directamente el contenido de `nuevo/` a la raíz. Esto evita futuros renombrados de paths cuando el sistema esté maduro: el "sistema activo" ES el repositorio, y `viejo/` queda como archivo de referencia hasta su eliminación final.

### Movimientos físicos
- `nuevo/unidades/U3/` → `unidades/U3/`
- `nuevo/scripts/prompts/` → `scripts/prompts/`
- `nuevo/scripts/validar_inventario.py` → `scripts/validar_inventario.py`
- Carpeta `nuevo/` eliminada.
- `CLAUDE.md` (raíz, CrewAI v5 antiguo) → `viejo/CLAUDE-anterior.md`.
- `scripts/importar_inventario.py`, `scripts/crear_crew_agents.py`, `scripts/probar_modelos.py`, `scripts/crewai/`, `scripts/resultados_prueba/` → `viejo/scripts/`.

### Lo que se queda en raíz
- `unidades/`, `scripts/` (con solo lo nuevo).
- `web/`, `diagrama.py`, `eval/` — infraestructura activa que sirve a ambas zonas.
- `PROCESO-MAESTRO.md`, `README.md`, `CHANGELOG.md`, `ROADMAP.md`, `GITHUB-MANIFEST.md`.
- `Dockerfile`, `railway.toml`, `requirements.txt`, `.env.example`.
- `.gitignore`, `.dockerignore`.

### Actualización de referencias
- `unidades/U3/U3-nc1-inventario.json`: `fuente.archivo` actualizado a `unidades/U3/fuente/U3-nc1.pdf`.
- `scripts/prompts/extraccion-inventario.md`: paths internos actualizados (sin `nuevo/`).
- `scripts/validar_inventario.py`: `PROJECT` recalculado, paths actualizados.
- `diagrama.py`: zona "nuevo" renombrada a "activo", lee de `unidades/` (raíz) en vez de `nuevo/unidades/`.
- `web/index.html`: tag `NUEVO` → `ACTIVO`.
- `.gitignore`, `.dockerignore`: paths actualizados.
- `README.md`: árbol del proyecto actualizado.
- `PROCESO-MAESTRO.md`: vista del árbol actualizada, bitácora.

### Estado de validación
- `python3 scripts/validar_inventario.py 3` → ✅ JSON válido, 0 avisos.
- Dashboard (http://localhost:8080) → tarjeta U3 ACTIVO + tarjeta U3 VIEJO visibles.

---

## [v9.0 — 2026-05-05] — Reorganización: todo el contenido por unidad bajo `unidades/UXX/`

### Motivo
Hasta hoy, el contenido de una misma unidad estaba disperso en seis raíces (`unidades/`, `datos/fuente/`, `datos/inventarios/`, `datos/tarjetas/`, `tarjetas/unidadX/`, `materiales/U03-*`). Para tocar U03 había que saltar entre seis carpetas. Se consolida todo en `unidades/UXX/` para que cada unidad tenga un único hogar.

### Movimientos (U03)
- `datos/inventarios/U03-inventario.json` → `unidades/U03/inventario.json`
- `datos/fuente/U03/U03-libro.pdf` → `unidades/U03/fuente/U03-libro.pdf`
- `datos/tarjetas/U03-*.csv` y `*-indesign.txt` → `unidades/U03/tarjetas/csv/` (sin prefijo `U03-`)
- `datos/tarjetas/U03-recurvo-output.json` → `unidades/U03/tarjetas/csv/recurvo-output.json`
- `tarjetas/unidad3/vocabulario/` (PSDs, PNGs, INDD) → `unidades/U03/tarjetas/diseno/vocabulario/`
- `materiales/U03-tarjetas-vocabulario-validacion-editorial.*` → `unidades/U03/tarjetas/validacion/`
- `materiales/U03-tarjetas-vocabulario-poker.*` → `unidades/U03/tarjetas/validacion/`
- `materiales/U03-tarjetas-vocabulario.tex`, `U03-tarjetas-gramatica.tex`, `U03-tarjetas-familias-ficticias.md` → `unidades/U03/tarjetas/validacion/`
- `materiales/U03-pildora-3.*.{pdf,tex}` → `unidades/U03/pildoras/` (sin prefijo `U03-`)
- `unidades/U03/U03-vocabulario-tarjetas.csv` → `unidades/U03/tarjetas/csv/vocabulario-tarjetas.csv`
- Eliminadas carpetas vacías: `datos/`, `tarjetas/`

### Actualización de referencias
- `unidades/U03/inventario.json`: 10 ocurrencias de `datos/fuente/U03/U03-libro.pdf` → `unidades/U03/fuente/U03-libro.pdf`
- `scripts/importar_inventario.py`: ejemplo de uso en docstring
- `scripts/crear_crew_agents.py`: ejemplo en `task_expected_output` del agente Escritor
- `diagrama.py`: nodos `FUENTE` e `INV` del Mermaid
- `.gitignore`, `.dockerignore`: rutas viejas reemplazadas (`unidades/` ya cubre todo)
- `README.md`: árbol de carpetas
- `CLAUDE.md`: bloque "Estructura por unidad", proceso de generación, flujo de producción

### Pendiente
- Aplicar la misma reorganización a U01-U02 y U04-U09 cuando tengan contenido real (hoy son plantillas vacías).
- `materiales/` queda como carpeta para especificaciones generales (`especificaciones-diseno-tarjetas.md`) que no son de ninguna unidad.

---

## [v8.26 — 2026-05-04] — Actor/actriz: desdoblamiento en dos tarjetas (moción irregular)

### Modificado — Tratamiento editorial de actor/actriz
- **Motivo:** la moción de actor → actriz es **irregular** (cambio de raíz + plural irregular *actrices* con z→c). A diferencia de las profesiones con moción regular (camionero, enfermero, agricultor, iluminador, decorador, maquillador), donde una sola tarjeta enseña el patrón económicamente, la moción irregular es léxica (la palabra hay que aprenderla, no se deduce). Se desdobla en **dos tarjetas independientes**, igual que los pares de Familia (padre/madre, hermano/hermana). También coherente con la decisión visual: actor y actriz se ilustran en imágenes separadas porque no son una "pareja profesional".
- **Cambios estructurales:**
  - 1 tarjeta única `actor` (4 formas) → **2 tarjetas separadas**: `actor` (M) y `actriz` (F)
  - Color de fondo: actor → azul celeste `#95CDEA` · actriz → salmón cálido `#EAA095` (mismos colores que padre/madre, hermano/hermana)
  - Salen del grupo "moción de género PENDIENTE": ya no esperan decisión de color
  - Total tarjetas profesiones: 9 → 10
  - Total tarjetas U03 (todas): 32 → 33
- **Gramapops:**
  - actor: `el/un actor | los/unos actores | Femenino: actriz | El femenino es irregular: actriz`
  - actriz: `la/una actriz | las/unas actrices | Masculino: actor | Plural irregular: actrices (la z cambia a c)`
- **Ejemplos:**
  - actor: *"Javier Bardem es actor."*
  - actriz: *"Penélope Cruz es actriz."*
- **Aplicado en:**
  - `datos/tarjetas/U03-profesiones.csv` + `-indesign.txt` (línea 10 desdoblada en 10+11)
  - `unidades/U03/U03-itinerarios.md` (count 9 → 10)
  - `unidades/U03/U03-cultura.md` (count 6 → 7 + nota sobre desdoblamiento)
  - `.claude/rules/criterios-generacion-tarjetas.md` sección 4 reestructurada en 4.1 (moción regular: 1 tarjeta) y 4.2 (moción irregular: 2 tarjetas) con razonamiento pedagógico
  - `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex`: tarjeta actor desdoblada + tabla colores 6.4 y 6.5 actualizadas + sección 4 (10 tarjetas) + sección 7 (actor/actriz fuera de la decisión PENDIENTE)
  - PDF recompilado (21 pp., +1 por la tarjeta nueva)

---

## [v8.25 — 2026-05-04] — Corrección lingüística: lema "gemelo" (singular), no "gemelos"

### Modificado — Lema de la tarjeta de gemelos
- **Motivo:** revisión en RAE/WordReference confirma que **`gemelo, -la`** es un sustantivo regular con par -o/-a, NO un sustantivo plural-only. El singular es uso natural y normativo: *"Tengo un hermano gemelo"*, *"Mi hermano es gemelo"*. La tarjeta anterior con lema *gemelos* + nota *"Usado siempre en plural"* era lingüísticamente errónea.
- **Cambios:**
  - Lema: `gemelos` → **`gemelo`** (artículo `el`, sílaba tónica `ge-ME-lo`)
  - Gramapop: `el/un gemelo | los/unos gemelos | Femenino: gemela` (sin nota de "plural-only")
  - Ejemplo: *"Mi hermano es gemelo."* (sustituye al ejemplo plural anterior)
  - Combos: `ser gemelo / gemela`, `mi/tu/su [parentesco] es gemelo/gemela`, `[nombre] y [nombre] son gemelos / gemelas` (este último mantiene plural por concordancia natural)
  - Traducciones a 9 idiomas en singular: twin, jumeau, gêmeo, Zwilling, bliźniak, tweelingbroer, δίδυμος, ikiz, dvojče
- **Recategorización en `criterios-generacion-tarjetas.md`:**
  - Movido de sección 8 (sustantivos plural-only) a sección 1 (regulares con par -o/-a)
  - Añadida nota explicativa al final de sección 8 documentando la decisión
- **Aplicado en:**
  - `datos/tarjetas/U03-familia.csv` + `-indesign.txt` (línea 21 completa)
  - `unidades/U03/U03-itinerarios.md` (lista de vocab: `gemelos` → `gemelo/a`)
  - `.claude/rules/criterios-generacion-tarjetas.md` (sec 1, sec 8, principio de género no marcado)
  - `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex` (tarjeta + tablas + principio) + PDF recompilado (20 pp.)

---

## [v8.24 — 2026-05-04] — Principio de género no marcado: hijo único / gemelos como tarjeta principal

### Modificado — Inversión de género en pares con moción
- **Motivo:** la tarjeta principal de un par con moción debe construirse siempre sobre la **forma masculina** (género no marcado en español), también en expresiones compuestas y plurales-only. Se invierten los dos casos donde la femenina era la principal:
  - `hija única` → **`hijo único`** (tarjeta principal, color azul celeste #95CDEA, ejemplo "Jorge es hijo único")
  - `gemelas` → **`gemelos`** (tarjeta principal, color azul celeste #95CDEA, ejemplo "Los hijos de Carlos son gemelos")
- La forma femenina queda en la fila `Femenino:` del gramapop y como variante en los combos
- **Aplicado en:**
  - `datos/tarjetas/U03-familia.csv` + `-indesign.txt` (líneas 20-21: artículo, palabra, sílaba tónica, color de fondo, ejemplo, gramapop, 3 combos, 9 traducciones)
  - `unidades/U03/U03-itinerarios.md` (lista de vocabulario)
  - `.claude/rules/criterios-generacion-tarjetas.md` (nueva regla "Principio de género no marcado" + ejemplos sec. 7 y 8 invertidos)
  - `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex` (tarjetas + tabla colores 6.4/6.5 + nuevo principio en sección 2) + PDF recompilado (20 pp.)
- **No tocado:** las citas literales del libro SGEL en `U03-comunicacion.md`, `U03-pildora-3.5.tex`, `U03-destrezas.md` y `U03-pildora-3.9.tex` mantienen "hija única" y "gemelas" porque son contenido pedagógico que reproduce el libro impreso, no tarjetas

---

## [v8.23 — 2026-05-04] — Simplificación de etiquetas del gramapop (sin Sing./Pl., "Femenino:"/"Masculino:")

### Modificado — Etiquetas del gramapop en todas las tarjetas
- **Motivo:** las etiquetas `Sing. M:`, `Pl. M:`, `Sing. F:`, `Pl. F:`, `Sing.:`, `Pl.:`, `M. sing.:`, `M. pl.:`, `F. sing.:`, `F. pl.:` no aportaban información (el artículo ya marca género y número) y saturaban el espacio. Se eliminan todas. Ejemplo: `Sing. M: el/un padre | Pl. M: los/unos padres` → `el/un padre | los/unos padres`
- **Etiqueta del par del otro género:** `Forma F:` → `Femenino:` y `Forma M:` → `Masculino:` (más natural, sin metalenguaje)
- **Formato final del gramapop de Familia:** `el/un padre | los/unos padres | Femenino: madre | "Padres" también = padre + madre`
- **Formato final del gramapop de Profesiones con moción:** `el/un camionero | los/unos camioneros | la/una camionera | las/unas camioneras` (4 formas con artículo, sin etiquetas)
- **Aplicado en:**
  - `datos/tarjetas/U03-familia.csv` + `-indesign.txt` (20 tarjetas)
  - `datos/tarjetas/U03-profesiones.csv` + `-indesign.txt` (9 tarjetas)
  - `datos/tarjetas/U03-lugares.csv` + `-indesign.txt`
  - `datos/tarjetas/U03-escuela.csv` + `-indesign.txt`
  - `unidades/U03/U03-vocabulario.md` (gramapops + texto explicativo)
  - `.claude/rules/criterios-generacion-tarjetas.md` (principios + reglas + ejemplos)
  - `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex` + PDF recompilado (20 pp.)

---

## [v8.22 — 2026-05-04] — Sustitución "Contrario" por "Forma F"/"Forma M" (U03 Familia)

### Modificado — Etiqueta del par de género en tarjetas de Familia
- **Motivo:** "Contrario" es semánticamente impreciso (padre y madre no son contrarios; son las dos formas del mismo término). Tras presentar 3 propuestas, se elige la **Propuesta 3**: etiqueta dependiente del género de la tarjeta
  - Tarjeta masculina → `Forma F: [femenino]`
  - Tarjeta femenina → `Forma M: [masculino]`
- **Aplicado en:**
  - `datos/tarjetas/U03-familia.csv` y `U03-familia-indesign.txt` (20 tarjetas)
  - `unidades/U03/U03-vocabulario.md` (gramapops + texto explicativo)
  - `.claude/rules/criterios-generacion-tarjetas.md` (reglas + ejemplos)
  - `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex` + PDF recompilado (20 pp.)

---

## [v8.21 — 2026-04-15] — Rediseño esquema comunicativo Decir la hora (U03)

### Modificado — Tarjeta "Decir la hora" (U03-comunicacion.md, Caja 2)
- **Rediseñado completo** del esquema comunicativo. Formato anterior: diagrama de reloj ASCII + fórmulas con metalenguaje (`Es la una (+ y/menos + fracción)`). Formato nuevo: tarjeta de 2 caras coherente con "Hablar de la familia"
- **CARA A:** modelo de frases completas + reglas mínimas (Propuesta 3 de las 3 presentadas). Incluye explicación visual de las dos zonas del reloj (Y / MENOS), regla Es/Son, 6 ejemplos de horas reales y lista de opciones con bullets
- **CARA B:** estructura integrada con diálogo modelo + 3 momentos de interacción con sus bullets de opciones propios:
  1. Decir la hora actual (con opciones de números y fracciones)
  2. Preguntar por un evento (con opciones de eventos: recreo, clase, película, comida, partido, concierto)
  3. Quedar con un amigo (con respuestas alternativas)
  Cierre con bloque "¡Atención!" que ataja la dificultad previsible documentada (distinción Es/Son + A la/A las)
- **Añadidos metadatos técnicos** en cursiva: colores (fondo verde pastel, recuadro azul acero Tiempo, badge teal Interacción oral), base teórica (Sentence Builder Conti/EPI, Protocolo A C1-C5, worked example, weaning off)
- **Base pedagógica:** Píldora formativa 3.6 (diapositivas 1-5), especialmente diapositivas 2 (contraste es/son), 3 (Sentence Builder) y 4 (¿A qué hora es...?)

---

## [v8.20 — 2026-04-11] — Revertido lila como decisión + restaurada sección 7 (decisión pendiente) en el PDF

### Corrección de un error de la v8.14 y v8.18
En versiones anteriores se integró el color lila claro `#D4B5E0` como solución única para las profesiones con moción de género, eliminando la sección 7 "Decisión pendiente" del PDF. Eso fue un error: la elección del color es una **decisión editorial pendiente** con dos propuestas (A: lila / B: banda lateral), no una decisión tomada.

### Cambios

**1. En los archivos de datos y documentación: color marcado como `PENDIENTE`**
- `datos/tarjetas/U03-profesiones.csv` + espejo: campo `color_fondo` de las 7 profesiones con moción (camionero, enfermero, agricultor, iluminador, decorador, maquillador, actor) cambiado de `#D4B5E0` a `PENDIENTE`.
- `unidades/U03/U03-vocabulario.md`: columna "Género" de las 3 profesiones con moción ahora dice `M (moción — color PENDIENTE)` en lugar de `M (lila)`.
- `.claude/rules/criterios-generacion-tarjetas.md`: sección 4 "Profesiones con moción de género" indica que el color está pendiente de decisión editorial y que el campo `color_fondo` aparece como `PENDIENTE` en las CSVs hasta que se tome la decisión.

**2. En el PDF editorial: restaurada sección 7 con las dos propuestas**
- **Sección 6.4** rediseñada: la fila de "Moción de género" ya no muestra lila como color asignado, sino "PENDIENTE" con referencia a la sección 7.
- **Sección 6.5** (aplicación a tarjetas de U03): las 7 profesiones con moción tienen fondo marcado como "PENDIENTE".
- **Sección 7 restaurada:** decisión pendiente entre Propuesta A (lila `#D4B5E0`) y Propuesta B (color principal + banda lateral del género opuesto). Incluye ventajas, desventajas y tabla comparativa.
- **Portada actualizada:** 4 acciones a realizar (contenido, nomenclatura, sistema de colores, decisión de color para moción).
- **Caja de validación final:** añadida la pregunta de decisión entre propuesta A o B con casillas de verificación.
- **PDF regenerado:** 19 páginas (incluye la sección 7 de nuevo).

### Sin cambios
- La estructura del gramapop con 4 filas para profesiones con moción (v8.18) se mantiene: está decidida y es correcta.
- La asignación de colores de las demás tarjetas (azul celeste solo M, salmón cálido solo F, gris azulado género común, verde menta verbos) también se mantiene.

---

## [v8.19 — 2026-04-11] — Etiquetas abreviadas del gramapop con marca de género

### Cambio — Propuesta A: etiquetas abreviadas con marca de género
Las etiquetas de las filas del gramapop se abrevian para ocupar menos espacio en la tarjeta. Las filas de caso 1 (Familia) y caso 3 (sin moción) ahora incluyen la marca de género (M/F) que antes faltaba.

**Moción de género (profesiones con 4 filas):**
| Antes | Ahora |
|---|---|
| `Masculino singular:` | `M. sing.:` |
| `Masculino plural:` | `M. pl.:` |
| `Femenino singular:` | `F. sing.:` |
| `Femenino plural:` | `F. pl.:` |

**Sin moción (Familia y resto), con indicación de género:**
| Antes | Ahora |
|---|---|
| `Singular: el/un X` | `Sing. M: el/un X` |
| `Plural: los/unos X` | `Pl. M: los/unos X` |
| `Singular: la/una X` | `Sing. F: la/una X` |
| `Plural: las/unas X` | `Pl. F: las/unas X` |

**Género común (-ista, -ante), sin marca de género:**
| Antes | Ahora |
|---|---|
| `Singular: el/la/un/una X` | `Sing.: el/la/un/una X` |
| `Plural: los/las/unos/unas X` | `Pl.: los/las/unos/unas X` |

### Archivos actualizados
- Los 5 CSV de `datos/tarjetas/` y sus espejos `*-indesign.txt`
- `unidades/U03/U03-vocabulario.md`
- `.claude/rules/criterios-generacion-tarjetas.md`
- `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex` + PDF regenerado

---

## [v8.18 — 2026-04-11] — Rediseño del gramapop: Contrario solo en Familia + 4 filas de moción en Profesiones + eliminación total de "Nota:"

### Cambios estructurales

**1. La fila `Contrario` es ahora exclusiva del campo semántico Familia**
Solo las tarjetas de parentesco (padre/madre, hermano/hermana, hija única/hijo único, gemelas/gemelos, etc.) la usan. En Profesiones, Lugares, Escuela y Acciones cotidianas se elimina completamente.

**2. Profesiones con moción de género: 4 filas fijas en lugar de Contrario**
Las 7 profesiones con moción (camionero, enfermero, agricultor, iluminador, decorador, maquillador, actor) ahora tienen 4 filas en el orden fijo:
- `Masculino singular` → `Masculino plural` → `Femenino singular` → `Femenino plural`
- El color de fondo interior es lila claro `#D4B5E0` (moción de género).
- Siempre empieza por la forma masculina, aunque la tarjeta principal sea femenina.

**3. `enfermera` renombrada a `enfermero`**
La tarjeta ahora es masculina como las demás profesiones con moción. El campo `articulo` pasa de `la` a `el`, `silaba_tonica` de `en-fer-ME-ra` a `en-fer-ME-ro`, `color_fondo` de `#EAA095` (salmón) a `#D4B5E0` (lila). El ejemplo contextualizado mantiene `"La madre de Javier es enfermera."` porque así aparece en el libro.

**4. La palabra "Nota:" desaparece del gramapop**
Ya no hay etiqueta `Nota:` en ningún lugar del campo `gramapop`. La observación final va como texto libre al final del campo, separada por `|`, empezando con mayúscula y sin punto final. Solo aparece la palabra "Nota" en la descripción del principio en el PDF editorial.

**5. El contenido del texto libre final se centra en lo llamativo morfológico u ortográfico**
Ejemplos:
- `actor`: `El femenino es irregular: actriz · En el plural, la z cambia a c: actrices`
- `agricultor`: `Plural masculino en -es`
- `deberes`: `Usado siempre en plural · singular raro`
- `curso`: `Aquí significa año escolar` (sin `= course` en inglés)

Las notas en inglés residuales se eliminaron:
- `hotel`: antes `Plural en -es · ≠ hospital` → ahora `Plural en -es`
- `hospital`: antes `Plural en -es · ≠ hotel` → ahora `Plural en -es`
- `curso`: antes `aquí = año escolar (también = course)` → ahora `Aquí significa año escolar`

### Archivos actualizados
- **`.claude/rules/criterios-generacion-tarjetas.md`:** toda la sección "Reglas de Gramapop" reescrita (nuevas reglas 1-8 con 8 casos cubiertos, orden fijo masculino primero, Contrario solo en Familia, 4 filas en profesiones con moción)
- **`datos/tarjetas/U03-profesiones.csv`:** 9 tarjetas con el nuevo formato. `enfermera` → `enfermero`. Color `color_fondo` cambiado a `#D4B5E0` en las 7 profesiones con moción
- **`datos/tarjetas/U03-familia.csv`:** se elimina "Nota:" en todas las notas, capitalizando la primera letra (`"Padres" también = padre + madre`, etc.)
- **`datos/tarjetas/U03-lugares.csv`:** hotel y hospital sin advertencia `≠`
- **`datos/tarjetas/U03-escuela.csv`:** curso sin `(también = course)`, deberes sin `Nota:`
- **Archivos `*-indesign.txt`:** regenerados desde las CSVs
- **`unidades/U03/U03-vocabulario.md`:** tabla de tarjetas actualizada con las 3 profesiones de moción (4 filas, color lila), enfermero en vez de enfermera. Tabla de plurales mixtos sin columna "Significado" en inglés. Corrección del texto explicativo al profesor que mencionaba "woman/wife"
- **`datos/tarjetas/U03-vocabulario.csv`:** archivo antiguo marcado como DEPRECATED (usaba esquema obsoleto con columnas Frecuencia/Irregularidad/4 combos y contenía inglés residual)
- **`materiales/U03-tarjetas-vocabulario-validacion-editorial.tex`:** sección 1 reescrita con 3 ejemplos (Familia con Contrario, Profesiones con 4 filas, sin moción). Las 9 tarjetas de profesiones actualizadas. Hotel/hospital sin `≠`. Curso sin inglés
- **PDF regenerado con xelatex:** 19 páginas (antes 17)

---

## [v8.17 — 2026-04-11] — Eliminación de todo texto en inglés en notas del gramapop de familia

### Cambio — Nota de la tarjeta `mujer`
Última nota en inglés en las tarjetas de familia. Cambiada a descripción en español:

| Antes | Ahora |
|---|---|
| `Nota: también = woman` | `Nota: también significa mujer adulta (no solo esposa)` |

Con este cambio, ninguna nota del gramapop en el campo semántico Familia contiene texto en inglés. Los 6 plurales mixtos (v8.15) y la nota de doble significado de mujer (v8.17) están todos en español.

### Archivos actualizados
- `datos/tarjetas/U03-familia.csv` + espejo `-indesign.txt`
- `unidades/U03/U03-vocabulario.md`
- `.claude/rules/criterios-generacion-tarjetas.md`
- `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex` + PDF regenerado (17 páginas)

---

## [v8.16 — 2026-04-11] — Slot de parentesco diferenciado por género en combos de familia

### Cambio — Combos 1 y 3 de las tarjetas de familia
En los combos que empiezan con artículo definido, el slot `[parentesco]` se sustituye por `[parentesco masculino]` o `[parentesco femenino]` según el género del artículo:

| Antes | Ahora |
|---|---|
| `el [parentesco] de [nombre]` | `el [parentesco masculino] de [nombre]` |
| `la [parentesco] de [nombre]` | `la [parentesco femenino] de [nombre]` |
| `[nombre] es el [parentesco] de [nombre]` | `[nombre] es el [parentesco masculino] de [nombre]` |
| `[nombre] es la [parentesco] de [nombre]` | `[nombre] es la [parentesco femenino] de [nombre]` |

El combo 2 `mi/tu/su [parentesco]` no cambia: los posesivos son neutros en género.

### Archivos actualizados
- `datos/tarjetas/U03-familia.csv` + espejo `-indesign.txt`
- `.claude/rules/criterios-generacion-tarjetas.md` (sección "Por campo semántico — Familia")
- `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex` + PDF regenerado (17 páginas)

---

## [v8.15 — 2026-04-11] — Traducciones en español y renombrado de slot [persona] → [nombre]

### Cambio 1 — Notas del gramapop: plurales mixtos en español en vez de inglés
Los plurales mixtos de términos de parentesco se expresaban con su equivalente en inglés. Ahora se expresan en español usando el patrón `X + Y`:

| Antes | Ahora |
|---|---|
| `"padres" también = parents` | `"padres" también = padre + madre` |
| `"hermanos" también = brothers + sisters` | `"hermanos" también = hermano + hermana` |
| `"hijos" también = children` | `"hijos" también = hijo + hija` |
| `"abuelos" también = grandparents` | `"abuelos" también = abuelo + abuela` |
| `"tíos" también = uncle(s) and aunt(s)` | `"tíos" también = tío + tía` |
| `"nietos" también = grandchildren` | `"nietos" también = nieto + nieta` |

### Cambio 2 — Renombrado del slot `[persona]` a `[nombre]`
En la nomenclatura de combos, el slot `[persona]` se renombra a `[nombre]` (más claro: se refiere a un nombre propio, no a "una persona" como categoría).

### Archivos actualizados
- `datos/tarjetas/U03-familia.csv` + espejo `-indesign.txt` (ambos cambios)
- `unidades/U03/U03-vocabulario.md` (ambos cambios)
- `.claude/rules/criterios-generacion-tarjetas.md` (nomenclatura de combos y reglas de gramapop por tipo)
- `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex` (ambos cambios)
- PDF regenerado con xelatex (17 páginas)

Los archivos de profesiones, lugares, escuela y acciones cotidianas no requerían cambios: no usaban `[persona]` (siempre usaban nombres propios directamente en los ejemplos) ni plurales mixtos en inglés.

---

## [v8.14 — 2026-04-10] — Sistema de colores unificado en PDF de validación editorial

### Modificado — `materiales/U03-tarjetas-vocabulario-validacion-editorial.tex`
- **Portada:** "Se pide al director editorial" → "Acciones a realizar" (3 puntos: validar contenido lingüístico, nomenclatura de combos y sistema de colores)
- **Sección 6 rediseñada como "Sistema de colores propuesto":** presenta el sistema completo con los 4 niveles de color de forma unificada en lugar de dos propuestas en conflicto:
  - 6.1. Fondo de la tarjeta según caja (3 colores: Caja 1 rosa, Caja 2 verde, Caja 3 amarillo)
  - 6.2. Badge de campo semántico (6 colores: Familia, Profesiones, Lugares, Escuela, Acciones cotidianas, Tiempo)
  - 6.3. Badge de destreza (6 colores: las 6 destrezas del MCER)
  - 6.4. Fondo interior según género (6 colores: masculino, femenino, género común, moción de género, verbos, invariables)
  - 6.5. Aplicación a las tarjetas de U03
- **Color lila claro \#D4B5E0** integrado como solución única para sustantivos con moción de género. Eliminadas las dos propuestas en conflicto (A/B) y la comparativa
- **Sección 7 eliminada** (era "Decisión pendiente"): el sistema de colores ya no presenta alternativas, es una propuesta única
- **Caja de validación final** reescrita con checklists de 3 acciones (contenido lingüístico / nomenclatura de combos / sistema de colores) en vez de decisión entre propuestas
- **PDF regenerado:** 17 páginas con xelatex

---

## [v8.13 — 2026-04-10] — Nomenclatura genérica de combos de vocabulario

### Nuevo — Sistema de notación para combos
- **Introducida nomenclatura específica** para el campo `combo_estructura`:
  - `[ ]` = slot sustituible por cualquier palabra de la categoría (`[profesión]`, `[persona]`, `[lugar]`)
  - `( )` = elemento opcional (`(+ [parentesco])`, `(mi/tu/su)`)
  - `/` = alternativas cerradas dentro de la misma categoría (`de/como`, `mi/tu/su`)
  - `+` = concatenación obligatoria entre elementos (`ser + [profesión]`)
- **Categorías de slot:** `[persona]`, `[parentesco]`, `[profesión]`, `[lugar]`, `[evento]`, `[materia]`, `[ordinal]`, `[verbo]`, `[número]`, `[hora]`

### Modificado — Los combos ahora son genéricos, no específicos
- **Antes:** `ser + camionero`, `el padre de [nombre]`, `ir a + instituto`
- **Ahora:** `ser + [profesión]`, `el [parentesco] de [persona]`, `ir a + [lugar]`
- El campo `combo_ejemplo` sigue siendo una frase real con palabras concretas; solo la `combo_estructura` es ahora genérica

### Modificado — Archivos actualizados
- **`.claude/rules/criterios-generacion-tarjetas.md`:** nueva sección "Nomenclatura de combos" con la tabla de símbolos, categorías de slot y patrones genéricos por campo semántico
- **`datos/tarjetas/U03-familia.csv`:** 20 tarjetas con combos genéricos (`el [parentesco] de [persona]`, etc.)
- **`datos/tarjetas/U03-profesiones.csv`:** 9 tarjetas con `ser + [profesión]`, `trabajar en + [lugar]`, `trabajar de/como + [profesión]`
- **`datos/tarjetas/U03-lugares.csv`:** 2 tarjetas con `estar en + [lugar]`, `ir a + [lugar]`, `hay + un/una + [lugar]`
- **`datos/tarjetas/U03-escuela.csv`:** 4 tarjetas con patrones genéricos diferenciados (`[lugar]`, `[materia]`, `[ordinal]`, `[evento]`)
- **`datos/tarjetas/U03-acciones-cotidianas.csv`:** merendar con `[verbo] + a las + [hora]`, etc.
- **Archivos `*-indesign.txt`:** regenerados automáticamente desde las CSVs

### Modificado — PDF de validación editorial
- **`materiales/U03-tarjetas-vocabulario-validacion-editorial.tex`:**
  - Nueva sección 2 "Nomenclatura de combos" con tabla de símbolos, categorías y ejemplos antes/después
  - Nuevo comando LaTeX `\tarjetacombos` que muestra los 3 combos de cada tarjeta (estructura genérica + ejemplo concreto)
  - Todas las tarjetas del PDF actualizadas al nuevo formato con combos visibles
  - Secciones renumeradas: Familia (3), Profesiones (4), Otros campos (5), Sistema de colores (6), Decisión pendiente (7)
  - Eliminada columna "Frec." del header de cada tarjeta (coherente con v8.12)
- **PDF regenerado** con xelatex: 17 páginas (antes 13)

---

## [v8.12 — 2026-04-10] — Eliminación del campo Frecuencia en tarjetas de vocabulario

### Modificado — Se elimina el campo "Frecuencia" / "Frec." del esquema de tarjetas de vocabulario
- **`unidades/U03/U03-vocabulario.md`:** columna "Frec." eliminada de la tabla markdown. El CSV embebido obsoleto se reemplazó por una referencia al CSV canónico en `datos/tarjetas/`
- **`unidades/U03/U03-destrezas.md`:** columna "Frec." eliminada. CSV embebido reemplazado por referencia
- **`agentes/ag-vocabulario.md`:** eliminadas las referencias a Frecuencia en tabla template, instrucciones y formato CSV. Sustituida columna "Regla" por "Gramapop" en el template
- **`agentes/ag-destrezas.md`:** actualizada la descripción del template para quitar Frecuencia/Irregularidad y añadir Gramapop
- **`agentes/ag-cultura.md`:** misma actualización
- **`diseno/crewai-memoria-aprendizaje.md`:** tabla de campos actualizada (eliminado campo Frecuencia y sección "Criterios de cálculo de frecuencia" completa). Tabla de campos actualizada al esquema canónico con articulo, palabra, silaba_tonica, gramapop, combos y 9 traducciones
- **`unidades/U03/U03-vocabulario-tarjetas.csv`:** archivo antiguo marcado como DEPRECATED con comentario apuntando a los CSVs canónicos en `datos/tarjetas/`
- **`materiales/U03-tarjetas-vocabulario.tex`:** eliminada la nota "Frec: 3=alta, 2=media, 1=baja" del título de sección. Corregido conteo de tarjetas (18 → 20)
- **`materiales/U03-tarjetas-vocabulario-poker.tex`:** añadido comentario de DEPRECATED (usa el sistema antiguo con barras de frecuencia)

### Sin cambios
- Las CSVs canónicas en `datos/tarjetas/*.csv` no tenían columna Frecuencia, así que no requirieron cambios
- El LaTeX de validación editorial (`materiales/U03-tarjetas-vocabulario-validacion-editorial.tex`) NO se ha tocado por petición del usuario. Se actualizará cuando se hayan hecho todos los cambios al sistema
- `repertorios/evaluacion.md` mantiene su uso del término "Frecuencia" porque ahí se refiere a frecuencia de errores en actividades, no a tarjetas

---

## [v8.11 — 2026-04-10] — Nueva estructura del gramapop de sustantivos (U03)

### Modificado — Reglas de gramapop (`.claude/rules/criterios-generacion-tarjetas.md`)
- **Reemplazada la sección "Reglas de Gramapop"** completa. Estructura nueva:
  - Gramapop de sustantivos con **filas etiquetadas separadas por `|`** dentro del mismo campo de la CSV
  - 4 etiquetas posibles: `Singular`, `Plural`, `Contrario`, `Nota`
  - **Reglas de omisión:** si el sustantivo no tiene contrario, la fila se omite completamente (no se pone `—`); si no hay nota, se omite; si es solo plural, se omite la fila Singular
  - **Artículos determinados + indeterminados** visibles siempre: `el/un hermano`, `los/unos hermanos`, `la/una hermana`, `las/unas hermanas`
  - **Género común** (-ista, -ante): `el/la/un/una guionista`
  - **Sin metalenguaje** ("Masculino terminado en -o" eliminado)
- **Gramapop de verbos simplificado:** la terminación ya está en el infinitivo, así que no se repite. Solo queda tipo de verbo + conjugación + irregularidad
  - Regular: `Verbo regular · 1.ª conjugación`
  - Irregular: `Verbo irregular · 1.ª conjugación | Cambio: e → ie (meriendo)`
- **Reglas por tipo de sustantivo:** 9 casos cubiertos (regulares -o/-a, heterónimos, doble significado, -tor/-dor, género común, consonante, sin par, expresiones compuestas, solo plural)
- **No aplica a adjetivos todavía** — pendiente de definir en futura versión

### Modificado — Datos de tarjetas (datos/tarjetas/)
- **`U03-familia.csv`:** 20 tarjetas actualizadas con el nuevo gramapop
- **`U03-profesiones.csv`:** 9 tarjetas actualizadas
- **`U03-lugares.csv`:** 2 tarjetas actualizadas (hotel, hospital)
- **`U03-escuela.csv`:** 4 tarjetas actualizadas (instituto, curso, deberes, recreo)
- **`U03-acciones-cotidianas.csv`:** 1 tarjeta actualizada (merendar, nuevo formato de verbo)
- **Espejos InDesign (`*-indesign.txt`):** los 5 archivos actualizados en paralelo

### Modificado — Documentación (unidades/U03/)
- **`U03-vocabulario.md`:** tabla de 21 tarjetas reestructurada. Eliminadas columnas "Regla" e "Irregularidad", sustituidas por una sola columna "Gramapop" con el nuevo formato. Eliminadas traducciones de la tabla (siguen en el CSV de producción)
- **`U03-destrezas.md`:** tabla de 9 tarjetas contextuales actualizada. Las tarjetas de adjetivos (mayor, pequeño) mantienen el formato antiguo con nota explicativa "formato de adjetivos pendiente de definir — v8.11 aplica solo a sustantivos"

---

## [v8.10 — 2026-04-09] — Rediseño esquema comunicativo Hablar de la familia (U03)

### Modificado — Tarjeta B: HABLAR DE LA FAMILIA (U03-comunicacion.md, Caja 2)
- **Rediseñado completo** del esquema comunicativo. Formato anterior: diagrama de flujo PREGUNTAR→RESPONDER con metalenguaje (+ número, + nombre, + adjetivo / profesión). Formato nuevo: líneas de flujo con slots sustituibles marcados como listas de opciones con bullet (·)
- **Ampliado de 4 a 10 parentescos:** El esquema anterior solo cubría hermanos. Ahora incluye padre, madre, hermano, hermana, abuelo, abuela, tío, tía, primo, prima — todos los parentescos trabajados en Vocabulario (p.34-35)
- **Eliminado metalenguaje:** "Tiene(n) + número + años", "Se llama(n) + nombre", "Es + adjetivo / profesión" sustituidos por slots vacíos con opciones concretas
- **Eliminada sección Invitar/Aceptar/Rechazar:** No es "hablar de la familia". Contenía además "poder" (irregular no enseñado)
- **CARA A:** Describir familia (se llama, tiene años, es/trabaja en, tengo hermanos, vive en) con bullets de opciones
- **CARA B:** Preguntar (5 preguntas con interrogativos conocidos) + Presentar (Este/Esta es mi...)
- **Añadidos metadatos técnicos** en cursiva: colores (fondo verde pastel, recuadro violeta Familia, badge teal Interacción oral), base teórica (sentence builder Conti/EPI, worked example, weaning off)

---

## [v8.9 — 2026-04-08] — Reglas de color por tipo de tarjeta + esquema comunicativo Hablar de la familia

### Nuevo — Especificaciones de diseño (especificaciones-diseno-tarjetas.md)
- **Añadida sección "Reglas de color por tipo de tarjeta"** que documenta el sistema completo de colores para los 4 tipos de tarjeta: vocabulario (Caja 1), gramática (Caja 2), esquema comunicativo (Caja 2) y estrategia (Caja 3)
- **Tarjetas de esquema comunicativo:** fondo verde pastel #D4EDDA (Caja 2), recuadro superior = color del campo semántico del vocabulario que trata, badge/icono = Interacción oral Teal #1A7A7A (fijo)

---

## [v8.8 — 2026-04-08] — Rediseño tarjeta de estrategia de mediación (U03)

### Modificado — Tarjeta D: CUENTA LO QUE OYES (antes "Cuenta lo que dice otra persona") (U03-destrezas.md)
- **Renombrada** de "Cuenta lo que dice otra persona" a "Cuenta lo que oyes" — más corto, cabe en tarjeta de 63×88mm
- **Reorganizada en CARA A / CARA B** para formato de tarjeta física
- **CARA A:** Introducción + instrucciones de anotación en cuaderno (no en tarjeta — la tarjeta es reutilizable) + tabla de cambio de persona ampliada de 6 a 7 pares (añadidos: Me llamo→Se llama, Tengo ___ años→Tiene ___ años, Estoy en→Está en; agrupados verbos regulares en una fila)
- **CARA B:** Fórmulas del mediador reescritas para nivel A1.1 real. Eliminadas: "Dice que..." (verbo irregular no enseñado), "Básicamente..." (no A1), "Lo más importante es..." (superlativo no enseñado), "Quiere decir que..." (querer irregular no enseñado), "¿Puedes repetir?" (poder irregular no enseñado), sección "Para simplificar" (un A1.1 ya está en el nivel más simple), sección "Para expandir" (demasiado compleja). Sustituidas por fórmulas con verbos y estructuras que el estudiante ya conoce
- **Eliminadas 7 citas académicas** del cuerpo de la tarjeta
- **Eliminado el "Truco del traductor de personas"** — redundante con la tabla y la introducción
- **Eliminada la autoevaluación de 3 preguntas** — es momento del profesor, no cabe en tarjeta
- **Añadidos metadatos técnicos** en cursiva (badge, color, base teórica) separados del contenido del alumno
- **Actualizadas todas las referencias** en U03-destrezas.md (fase 10, instrucciones del profesor), U03-destrezas-paginas.md y U03-itinerarios.md
- **Base teórica preservada:** MCER Companion Volume 2020, Piccardo & North (2019), Stathopoulou (2015), Nied Curcio & Katelhön (2020), Long (1996), Pica (1994), repertorio de mediación (124 técnicas, principios-guía 3 y 4)

---

## [v8.7 — 2026-04-06] — Rediseño tarjeta de estrategia de comprensión auditiva (U03)

### Modificado — Tarjeta C: ESCUCHA EN TRES MODOS (U03-destrezas.md)
- **Eliminadas 7 citas académicas** del cuerpo de la tarjeta (material del profesor, no del alumno)
- **Eliminada la columna "Ejemplo"** de la tabla de modos — redundante con las instrucciones
- **Añadida frase introductoria** antes de la tabla: el estudiante entiende para qué sirve la tarjeta antes de ver los modos
- **Reorganizada en CARA A / CARA B** para formato de tarjeta física (63 × 88 mm)
- **CARA A:** Introducción + 3 modos (Express, Rastreador, Detective) + ANTES de escuchar + MIENTRAS escuchas
- **CARA B:** ENTRE ESCUCHAS — ciclo de verificación y focalización (basado en la Secuencia Pedagógica Metacognitiva de Vandergrift): revisar notas → comparar con compañero → identificar laguna → escucha focalizada. Cierre: "El audio desaparece. Tu nota se queda."
- **Eliminado el Truco del rastreador** como sección independiente — solo funcionaba para un modo; la cara B ahora cubre los tres modos
- **Añadidos metadatos técnicos** en cursiva (badge, color, base teórica) separados del contenido del alumno
- **Justificación:** Coherencia con los criterios de diseño aplicados a las tarjetas B (ESCRIBE UN EMAIL) y D (CUENTA LO QUE OYES): sin citas, sin metalenguaje, lenguaje directo para A1, formato de dos caras, transferible
- **Base teórica preservada:** Solmecke (1993) tres Hörstile, Protocolo CO (CO1-CO3), Vandergrift & Goh (2012) MPS, O'Malley & Chamot (1990), Field (2008)

---

## [v8.5h — 2026-03-19] — Optimización consultar_inventario para vocabulario

### Modificado — Tool `consultar_inventario` (tools.py)
- **Campos eliminados del SELECT:** `tipo`, `destreza`, `instruccion`, `ejemplo_libro`, `numero_actividad`
- **Campos que se mantienen:** `numero_pagina`, `seccion`, `contenido_linguistico`, `texto_completo`, `respuestas`, `contenidos_indice`
- **Justificación:** Los campos eliminados son metadatos pedagógicos (formato de ejercicio, habilidad, instrucciones al alumno) que no contienen vocabulario extraíble. El vocabulario está en `texto_completo` y `respuestas`; la clasificación semántica viene de `contenido_linguistico` y `contenidos_indice`
- **GROUP BY simplificado:** solo 4 campos en vez de 9
- **description actualizada:** refleja los campos que realmente devuelve
- **Reducción estimada:** ~60% menos tokens por ejecución del inventario
- **Nota:** Este cambio aplica solo al crew Recurvo (vocabulario). Crews futuros tendrán sus propias herramientas

---

## [v8.5g — 2026-03-19] — Editor de código fuente de herramientas + versionado

### Nuevo — Backend (diagrama.py)
- Función `get_tool_versions()`: lee/inicializa versiones por tool desde sidecar JSON
- Función `save_tool_source()`: edita una clase en `tools.py` con validación de sintaxis (`compile()`), backup automático y verificación de estructura
- Endpoint `POST /api/tool_sources/update` → guarda código editado, incrementa versión
- Constantes `TOOL_VERSIONS_FILE`, `TOOLS_BACKUP`

### Modificado — Backend (diagrama.py)
- `GET /api/tool_sources` ahora retorna `{name: {source, version, updated_at}}` en vez de `{name: source_string}`

### Nuevo — Dashboard (web/index.html)
- **Editor de código por tool**: textarea monoespaciado con botones "Editar código" / "Guardar" / "Cancelar"
- **Badge de versión** (`vN`) visible junto al nombre de cada herramienta, se actualiza al guardar
- **Mensajes de error**: errores de sintaxis del backend se muestran en rojo bajo el editor
- CSS: `.tool-source-edit`, `.tool-version-badge`, `.tool-error-msg`
- JS: `toggleToolView()`, `startToolEdit()`, `cancelToolEdit()`, `saveToolSource()`

### Seguridad
- Validación de sintaxis Python (`compile()`) antes de escribir al disco
- Backup automático (`tools.py.backup`) antes de cada escritura
- Verificación de que el nº de clases no cambia tras la reconstrucción

---

## [v8.5f — 2026-03-19] — Visor de código fuente de herramientas

### Nuevo — Backend (diagrama.py)
- Función `get_tool_sources()`: parsea `scripts/crewai/tools.py`, extrae cada clase `BaseTool` indexada por `name`
- Endpoint `GET /api/tool_sources` → JSON con el código fuente de cada herramienta
- `SERVER_VERSION` → `"8.5"`

### Modificado — Dashboard (web/index.html)
- Sección Herramientas rediseñada: cada tool es clicable con chevron colapsable
- Al expandir, muestra el código fuente completo de la herramienta en bloque monoespaciado
- CSS: `.tool-chevron`, `.tool-source` (Material Design 3, max-height 400px con scroll)

---

## [v8.5d — 2026-03-18] — Rediseño escritor + fix UPSERT

### Modificado — BD crew_agents (escritor)
- **goal** reescrito: de proceso ("persist and export") a resultado ("safely stored and available")
- **backstory** reestructurado: 4 partes (data persistence specialist, pipeline secuencial con input trusted, reliability crítica, ejecutar sin modificar)
- **task_description** reescrito aplicando 8 principios:
  - Eliminado STEP 1 innecesario (limpiar `_verificacion`): la tool ya ignora campos desconocidos (P3)
  - Añadido INPUT FORMAT con ejemplo del JSON que recibe del verificador (P4)
  - Añadidos ejemplos de tool calls: `escribir_tarjetas(tarjetas_json=...)` y `exportar_csv(unidad=...)` (P3, P4)
  - Error handling ampliado: cubre fallo de `exportar_csv` además de `escribir_tarjetas` (P3)
  - 2 steps (no 3), cada uno con WHY (P5)
- **task_expected_output** mejorado: ejemplo success + ejemplo partial failure con array de errores (P4)

### Corregido — Bug UPSERT en `escribir_tarjetas` (tools.py)
- **Antes:** `ON CONFLICT` solo actualizaba `frecuencia` → correcciones del verificador se perdían al re-ejecutar
- **Ahora:** actualiza los 18 campos editables (genero, silaba_tonica, regla, combos, traducciones, etc.)
- Impacto: sin este fix, el pipeline verificador→escritor no tenía efecto real sobre tarjetas existentes

### Modificado — Documentación
- `.claude/rules/agent-prompt-design.md`: escritor goal y backstory actualizados en sección de referencia

---

## [v8.5c — 2026-03-18] — UX ciclo de aprendizaje: reglas, revisión y patrones

### Nuevo — BD
- Columna `estado_revision` (sin_revisar/revisada) en `tarjetas_vocabulario`

### Nuevo — Backend (diagrama.py)
- Endpoint `GET /api/correcciones/stats` — correcciones agrupadas por tipo_error
- `estado_revision` añadido a SELECT y allowed fields

### Nuevo — Dashboard (web/index.html)
- **Sección Revisión**: barra de progreso, contador, panel de patrones
- **Badge de revisión por tarjeta** + botón "marcar como revisada"
- **Modal corrección**: checkbox "Crear regla general" con campos regla + ejemplos
- **Modal regla independiente**: crear/editar reglas con tipo, regla, ejemplos, activa
- **Sección Reglas aprendidas**: CRUD completo de reglas desde la interfaz
- **Panel de patrones**: correcciones agrupadas, botón "Crear regla" cuando 3+ correcciones

---

## [v8.5b — 2026-03-18] — Rediseño verificador + consultar_reglas

### Modificado — BD crew_agents (verificador)
- **goal** reescrito: outcome-oriented, sin referencia a "database"
- **backstory** reestructurado: 4 partes (dominio ELE/A1.1, pipeline secuencial, tolerancia cero, verificar contra datos)
- **task_description** reescrito: consultar_inventario + consultar_reglas, checks con WHY y ejemplos ✓/✗, terminología actualizada (construcciones gramaticales, tildes preservadas, 23 campos)
- **expected_output** mejorado: ejemplos completos de tarjeta ok y corregida

### Modificado — Código
- `scripts/crewai/recurvo.py`: añadido `ConsultarReglas()` a tools del verificador
- `scripts/crear_crew_agents.py`: verificador simplificado a referencia BD (seed script)
- `.claude/rules/agent-prompt-design.md`: verificador goal y backstory actualizados

### Documentado — CLAUDE.md
- Pendiente UX ciclo de aprendizaje (5 mejoras para facilitar escritura de reglas y revisión)
- `reglas_aprendidas`: distingue tipo 1 (especificaciones de producto) vs tipo 2 (patrones aprendidos, futuro)

---

## [v8.5 — 2026-03-18] — Rediseño task_description generador + eliminación irregularidad

### Modificado — BD crew_agents (generador)
- **task_description** reescrito completo: definiciones de campos con ejemplos, formato combo (estructura → ejemplo), política plurales colectivos, cada forma = 1 tarjeta, preservar tildes en sílaba tónica
- **task_expected_output** actualizado: 23 campos (sin irregularidad), ejemplo con nuevos combos y regla
- Eliminada referencia a "Nuevo Compañeros 1" (agente no atado a libro específico)
- Eliminada sección CRITICAL RULES (duplicaba reglas_aprendidas, P7)

### Modificado — BD reglas_aprendidas
- Regla id=1 (silaba_tonica): añadido "preserve accent marks" → maMÁ, paPÁ
- Regla id=2 (combo): redefinido como construcciones gramaticales (estructura → ejemplo)
- Regla id=3 (genero): cada forma = 1 tarjeta (profesor ≠ profesora), regla solo describe la palabra

### Modificado — Código (eliminación de irregularidad)
- `diagrama.py`: eliminado de SELECT y allowed fields
- `scripts/crewai/tools.py`: eliminado de tool description, INSERT, CSV SELECT, headers y row builder
- `scripts/crear_crew_agents.py`: simplificado a referencia a BD (seed script)
- `eval/provider_crewai.py`: actualizado a 23 campos y nueva terminología

### Modificado — Documentación
- `materiales/especificaciones-diseno-tarjetas.md`: combos redefinidos como construcciones gramaticales con formato estructura → ejemplo
- `.claude/rules/agent-prompt-design.md`: terminología combos actualizada, referencia a especificaciones actualizada

---

## [v8.4b — 2026-03-17] — CLAUDE.md condensado (334 → 171 líneas)

### Modificado — CLAUDE.md
- Reducido de 334 a 171 líneas (−49%)
- **Eliminado:** Preguntas resueltas (1, 3, 4, 9), esquema SQL crew_agents (ya en BD), árbol local completo (derivable del filesystem), sección "GitHub y Railway" duplicada, nota redundante "Paso 6"
- **Condensado:** Preguntas pendientes (59→15 líneas), tabla CrewAI (20→10 filas), ciclo de trabajo, flujo de producción
- **Actualizado:** crew_agents de "pendiente" a "implementado" (4 sitios), dashboard v8.3→v8.4, tabla BD 9→10 tablas, checkbox crew_agents marcado como completado
- **Eliminado:** "No hay build/test" de restricciones (hay agentes ejecutables)

---

## [v8.4 — 2026-03-17] — crew_agents en BD: config de agentes editable y persistente

### Nuevo — tabla `crew_agents` (Neon PostgreSQL)
- Tabla creada con esquema: id, crew, agent_key, agent_order, role, goal, backstory, task_description, task_expected_output, max_iter, updated_at
- Poblada con los 3 agentes de Recurvo (generador, verificador, escritor)
- Script de creación: `scripts/crear_crew_agents.py` (idempotente, ON CONFLICT DO UPDATE)

### Modificado — `scripts/crewai/recurvo.py`
- **Lee config de agentes desde BD** en lugar de tenerla hardcodeada
- Nueva función `cargar_config_bd("recurvo")`: consulta crew_agents y devuelve lista de configs
- Nueva función `crear_crew(unidad)`: construye agentes, tareas y Crew dinámicamente desde BD
- `_render()`: reemplaza placeholders `{unidad}` y `{unidad:02d}` en templates de BD
- Tools y LLM params siguen en código/env vars (TOOLS_MAP, LLM_KEY_MAP, LLM_CFG)

### Modificado — `diagrama.py`
- `SERVER_VERSION = "8.4"`
- Nuevas funciones: `get_crew_agents(crew)`, `update_crew_agent(id, data)`
- Nuevos endpoints: `GET /api/crew_agents?crew=X`, `POST /api/crew_agents/update`

### Modificado — `web/index.html`
- **Nueva sección Pipeline**: reemplaza las secciones separadas de Prompt y Tareas
- Pipeline carga datos desde `/api/crew_agents` (BD) — muestra role, goal, backstory, task_description, task_expected_output, max_iter por agente
- Editar/Guardar persiste cambios en BD via `/api/crew_agents/update`
- Eliminado role/goal/backstory hardcodeado del objeto AGENTES JS
- Nueva variable global `crewAgents` para cache de datos de BD

---

## [v8.2 — 2026-03-17j] — Pulido: tildes restantes + logo header + botones legibles

### Corregido — `web/index.html`
- **Tildes**: Sílaba tónica, Traducción, Género (select de correcciones), Sílaba (tabla tarjetas), Métricas (título gráfico)
- **Logo inline**: favicon Agentia ELE visible en header junto al título
- **Botones tabla tarjetas**: "Corr"/"Elim" → "Corregir"/"Eliminar" con tooltips

---

## [v8.0 — 2026-03-17h] — Rediseño completo: navegación multi-nivel + tema Material Design

### Rediseño completo — `web/index.html`
- **Navegación multi-nivel**: Unidad → Sección → Agente → Ejecución
  - Inspirado en LangSmith, Langfuse, Braintrust
- **Sidebar por secciones** (no por agentes): Toda la unidad, Vocabulario, Gramática, Comunicación, Cultura, Destrezas, Reflexión, Evaluación
  - Cada sección muestra cuántos agentes tiene asignados
  - Secciones sin agentes muestran "Sin agentes asignados"
- **6 vistas**: Proyecto, Sección, Agente (config), Nueva ejecución, Detalle ejecución, Comparar
- **Vista Agente (config)**: secciones colapsables con prompt (role/goal/backstory), tareas, herramientas, métricas de evaluación, parámetros
- **Separación agente vs ejecución**: config del agente (prompt, tools, tasks) es estable; parámetros de ejecución (modelo, temperatura, max_tokens, top-p) son variables por run
- **Vista Ejecución**: consola, evaluación (score + métricas + radar), tarjetas, trazas LLM — todo colapsable
- **Comparación**: checkbox en lista de ejecuciones → comparar métricas lado a lado
- **Material Design 3**: fuente Inter (Google Fonts), elevación por sombras, botones pill (border-radius: 20px), focus ring en inputs
  - Paleta dorado-oliva/crema: primary #7D7432, surface #FFFDF6, surface-variant #F5F0DC
  - Cards interactivas = elevated (sombra), cards de texto = outlined (borde, sin sombra)
  - Reemplaza completamente el tema oscuro anterior
- **Favicon**: logo Agentia ELE (`web/favicon.svg`) servido desde `diagrama.py`
- **Header y sidebar sin separación**: mismo color, sin sombra en header → bloque sólido
- **Tildes corregidas**: 19+ instancias en textos visibles (Gramática, Comunicación, Evaluación, Reflexión, ejecución, métricas, parámetros, sílabas, etc.)

### Modificado — `diagrama.py`
- `SERVER_VERSION = "8.0"`
- Nuevo endpoint: `/favicon.svg`, `/favicon.ico` → sirve `web/favicon.svg`

### Modelo de datos JS
- `SECCIONES[]`: 8 secciones con agentes asignados
- `AGENTES{}`: definición completa de cada agente (Recurvo) con role, goal, backstory, tasks, tools, eval_metrics, params
- Datos sincronizados con `recurvo.py` real

### Patrón de diseño
- Todo gira alrededor de la ejecución (run-centric)
- Agentes se aplican a secciones, no se navegan directamente
- Modelo LLM pertenece a la ejecución, no al agente (permite comparar modelos)

---

## [v7.0 — 2026-03-17g] — Fix Langfuse definitivo + versión visible en dashboard

### Corregido — `requirements.txt`
- `langfuse==3.14.5` → `langfuse==2.60.10` — única versión compatible con litellm 1.82.2 (bundled en crewai 1.9.3)
- langfuse 3.x/4.x eliminaron `.trace()` y `sdk_integration` que litellm necesita
- Probado localmente: 0 errores Langfuse, trazas enviadas correctamente

### Añadido — Versión del servidor en dashboard
- `SERVER_VERSION = "7.0"` en `diagrama.py` — formato `major.minor`
- Endpoint `/api/version` para consultar versión
- Dashboard muestra "En vivo v7.0 — HH:MM:SS" junto al indicador de estado
- major se incrementa en cambios sustanciales, minor en deploys pequeños

---

## [2026-03-17f] — Fix: langfuse 4.0 incompatible con litellm, bajar a 3.14.5

### Corregido — `requirements.txt`
- `langfuse==4.0.0` → `langfuse==3.14.5` — litellm pasa `sdk_integration` a `Langfuse()`, que v4.0 eliminó
- Con v3.14.5, `litellm.success_callback = ["langfuse"]` funciona correctamente

---

## [2026-03-17e] — Langfuse: reemplazar integración rota por litellm callback

### Corregido — `scripts/crewai/recurvo.py`
- Eliminada integración anterior con `@observe` + TracerProvider (25 líneas, 0 datos útiles)
- Nueva integración: `litellm.success_callback = ["langfuse"]` (4 líneas)
- Captura automática de cada llamada LLM: tokens, coste, modelo, latencia, prompt, respuesta
- Sin conflicto OTel (no usa TracerProvider ni @observe)

---

## [2026-03-17c] — Actualizar catálogo de modelos Groq

### Modificado — `diagrama.py` (AVAILABLE_MODELS)
- 6 modelos Groq (antes 2): GPT-OSS 120B, GPT-OSS 20B, Llama 3.3 70B, Llama 4 Scout 17B, Kimi K2 (nueva versión -0905), Qwen 3 32B
- Eliminado `kimi-k2-instruct` viejo (131K ctx) — reemplazado por `-0905` (262K ctx)
- Añadidos campos `ctx` y `nota` a cada modelo para el dashboard
- Claude Sonnet 4 mantenido como opción de pago

### Modificado — `.env.example`
- Documentados los 6 modelos Groq con contexto y output máximo

---

## [2026-03-17b] — Fix: añadir litellm para soporte multi-modelo en CrewAI

### Corregido — `requirements.txt`
- `crewai==1.9.3` → `crewai[litellm]==1.9.3` — instala litellm como extra para routing de modelos no nativos (Groq, etc.)
- CrewAI 1.9.3 eliminó litellm de sus dependencias core (ahora es extra opcional). Sin él, el string `groq/openai/gpt-oss-120b` no se resuelve y el agente no arranca
- Verificado: crewai 1.10.1+ no es instalable (requiere `lancedb>=0.29.2` inexistente en PyPI). 1.9.3 es la última estable funcional

---

## [2026-03-17] — Dashboard reescrito: navegación por pestañas + tabla tarjetas + comparación

### Reescrito — `web/index.html` con patrones de mercado (Langfuse/LangSmith)
- Navegación por pestañas: Evaluación, Tarjetas, Trazas, Consola, Historial (sustituye scroll vertical)
- Tarjetas: tabla ordenable con búsqueda (`sortTarjetas(col)` + `filterTarjetas()`) — columnas: Palabra, Nivel, Gen, Sílaba, Campo, Regla, traducciones (IT/FR/PT/EN/CS/PL/TR), Combos, Acciones
- Comparación de evaluaciones: selección con checkbox de 2 runs, vista side-by-side de métricas
- Badges con contadores en pestañas (tarjetas, trazas, historial)
- Auto-switch: consola al ejecutar agente, evaluación al completar
- Preservada toda la funcionalidad existente: vista proyecto (grid + Mermaid), sidebar, ejecución con Popen streaming, modal de correcciones, todas las APIs

---

## [2026-03-16d] — Repo organizado + GitHub + Railway desplegado

### Reorganización del repositorio para GitHub
- Repo publicado en https://github.com/adminmc2/agentes_GDC1.git (rama `main`)
- Solo código funcional del sistema de agentes (18 archivos). Todo el contenido editorial excluido vía `.gitignore`
- Creado `GITHUB-MANIFEST.md` con lista detallada de archivos incluidos/excluidos y justificación
- Excluidos por ahora (pendientes de rediseño): `agentes/`, `repertorios/`, `datos/tarjetas/`, `scripts/resultados_prueba/`, `diseno/`

### Deploy en Railway
- URL pública: https://agentiaelegd.up.railway.app
- Dashboard y API funcionando en producción
- Creados: `Dockerfile` (Python 3.12 + Node.js 20), `railway.toml`, `.dockerignore`

### Dependencias añadidas
- `deepeval==3.8.9` añadido a `requirements.txt`
- `promptfoo` instalado vía npm global en Dockerfile (Node.js 20)
- `.env.example` creado con todas las variables documentadas (sin secrets)

### Correcciones
- Fix GitGuardian: placeholders en `.env.example` cambiados de patrones reales (`sk-ant-...`) a texto genérico
- Fix: `LANGFUSE_BASE_URL` renombrado a `LANGFUSE_HOST` (nombre correcto para SDK v4)

---

## [2026-03-16c] — Dashboard con dos vistas (Proyecto + Agentes) + tema claro

### Reescrito — `web/index.html` con navegación sidebar entre dos vistas
- **Vista Proyecto**: grid de estado 9 unidades × 8 secciones + 5 diagramas Mermaid (arquitectura, flujo, dependencias, estado agentes, BD)
- **Vista Agentes**: evaluación (score+radar+historial), tarjetas, errores, trazas Langfuse, consola, historial evaluaciones
- Sidebar: botón "Proyecto" + lista de 6 agentes + controles de ejecución + historial de runs
- Tema claro (#f5f6fa fondo, #fff tarjetas) — sustituye el tema oscuro

### Añadido — Ejecución de agentes desde la web (`diagrama.py`)
- `start_agent()`: subprocess.Popen en thread daemon con timeout 600s
- `get_agent_status()`: polling del estado de ejecución
- Endpoints: `/api/agente/run` (POST), `/api/agente/status` (GET), `/api/agente/output` (GET), `/api/modelos` (GET)
- Variable `RECURVO_LLM` para seleccionar modelo desde la web

### Añadido — Trazas Langfuse en la web
- `get_trazas()` y `get_traza_detalle()`: consultan Langfuse API directamente
- Endpoints: `/api/trazas` (GET), `/api/trazas/{id}` (GET)
- Trazas expandibles en el dashboard con observaciones detalladas

### Limpieza
- Eliminadas sustituciones SECTIONS_JSON/LABELS_JSON en `diagrama.py` (ya no necesarias)
- El frontend carga toda la configuración de agentes y modelos internamente

---

## [2026-03-16b] — Sistema de evaluación y trazabilidad integrado

### Implementado — Stack de evaluación completo
- **Langfuse** (v4.0.0): trazabilidad integrada en `recurvo.py` via OTel. Se activa automáticamente al configurar `LANGFUSE_PUBLIC_KEY` en `.env`. Stub transparente cuando no está configurado.
- **DeepEval** (v3.8.9): métricas automáticas de calidad para tarjetas de vocabulario.
- **promptfoo** (ya instalado): config YAML para comparar modelos (GPT-OSS-120B vs Kimi K2 vs Claude Sonnet).

### Creado — Script de evaluación (`eval/evaluar_tarjetas.py`)
- 5 métricas rule-based: plurales, sílaba tónica, combos, traducciones, reglas
- Score global ponderado (0-100)
- Detección de errores con detalle por tarjeta
- Tabla `evaluaciones` en BD para historial
- Modo terminal con informe visual + modo JSON
- Integrado con la web via API `/api/evaluaciones`

### Creado — Pestaña "Evaluación" en la web
- Score global con indicador visual (verde/amarillo/rojo)
- Gráfico radar con las 5 métricas (Chart.js)
- Gráfico de línea con historial de scores
- Lista de errores detectados con badges por tipo
- Historial de evaluaciones con barras de progreso
- Botón "Evaluar ahora" (ejecuta evaluación y guarda en BD)
- Enlace directo a Langfuse cloud

### Creado — Config promptfoo (`eval/promptfoo.yaml`)
- 2 providers configurados: GPT-OSS-120B y Kimi K2 (Groq, gratis)
- Claude Sonnet comentado (coste ~$0.13/ejecución)
- 5 assertions: tarjetas_suficientes, sin_plurales, nivel_1_minimo, traducciones_completas, combos_variados
- Usa `eval/provider_crewai.py` como wrapper del agente

### Mejorado — Ciclo de feedback
- Backstory del generador reforzado: prioriza correcciones previas sobre cualquier otra instrucción
- Ciclo completo: corrección en web → BD → tool consultar_correcciones → agente lee → no repite error

### Infraestructura
- `.env`: añadidas variables Langfuse (LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_BASE_URL)
- `diagrama.py`: añadidos endpoints `/api/evaluaciones` (GET), `/api/evaluaciones/run` (POST)
- `web/index.html`: Chart.js CDN añadido, pestaña Evaluación con ~200 líneas de JS
- Tabla `evaluaciones` creada en BD Neon PostgreSQL

---

## [2026-03-16] — Primera ejecución exitosa del agente Recurvo + Web de gestión

### Implementado — Agente Recurvo funcional (CrewAI)
- `scripts/crewai/tools.py`: 5 herramientas custom contra Neon PostgreSQL (consultar_inventario, consultar_tarjetas_previas, consultar_correcciones, escribir_tarjetas, exportar_csv)
- `scripts/crewai/recurvo.py`: arquitectura de 2 tareas secuenciales (generador + escritor) para resolver que el LLM no llamaba a las tools de escritura
- Bug corregido: `**kwargs` en las firmas de `_run()` rompía el `args_schema` de CrewAI (las herramientas no exponían parámetros)
- Primera ejecución completa: 5/5 tools ejecutados, 19 tarjetas escritas en BD, CSV exportado
- Modelo: GPT-OSS-120B en Groq (gratis). Coste: $0.00

### Creado — Web de gestión del proyecto
- `diagrama.py`: servidor web con APIs REST para tarjetas y correcciones (GET/POST)
- `web/index.html`: frontend separado con hot reload (no requiere reiniciar servidor para ver cambios)
- Título: "Sistema de gestión proyecto Guía didáctica"
- 7 pestañas: Estado, Arquitectura, Flujo generación, Dependencias, Agentes U03, Base de datos, Correcciones
- Pestaña Correcciones: visualiza tarjetas de la BD, permite corregir campos individuales, eliminar tarjetas, y registra todo en tabla `correcciones`

### Auditoría — Calidad de las 19 tarjetas U03
- 5 plurales incorrectos (abuelos, padres, hijos, nietos, nietas) → deben eliminarse
- 6 errores de sílaba tónica (mujer, padres, nietos, nietas, primo, prima)
- 19 reglas en formato incorrecto
- 19 combos repetitivos
- Faltan: nieto, nieta, sobrino, sobrina, niveles 2 y 3
- Pendiente de corrección

### Investigación — Feedback y evaluación de agentes
- Documentado: `crewai train`, Knowledge System, `@human_feedback` en Flows
- Evaluación: Langfuse (tracing), DeepEval (métricas), promptfoo (comparar modelos)
- Pendiente de instalar e integrar

### Limpieza
- `diagrama.py`: eliminado HTML embebido (418 líneas), extraído a `web/index.html`
- `.gitignore`: añadidos `*.pkl`, `datos/fuente/**/*.pdf`
- Eliminadas JPGs de `datos/imagenes/U03/` (reemplazadas por PDF embebido)
- Renombrado `datos/U03-inventario.json` → `datos/inventarios/U03-inventario.json`

---

## [2026-03-15] — Documento de diseño: memoria, aprendizaje y agente Recurvo

### Creado — `diseno/crewai-memoria-aprendizaje.md`
- Análisis de los 4 tipos de memoria de CrewAI y su aplicabilidad real a este proyecto
- Definición completa del agente Recurvo (primer agente de Fase 1): identidad, inputs, output JSON, 16+2 campos, tools, modelo, lógica de extracción
- Plan de construcción corregido (10 fases) con dependencias
- Preguntas pendientes antes de implementar (7 preguntas en 3 categorías)
- Conclusiones clave: entity memory de CrewAI no es fiable para vocabulario (usar tool custom con búsqueda exacta), feedback del editor es el mecanismo de aprendizaje más valioso (prioridad alta)

---

## [2026-03-15] — Arquitectura de dos fases: Agentes de Recursos → Agentes de Sección

### Decisión arquitectónica — Agentes de Recursos como preprocesadores
- Los agentes de material (Tarjetas, Gramatips, Estrategias) trabajan ANTES e independientemente de los agentes de sección
- Extraen contenido desde la fuente (inventario), no desde la interpretación de otro agente
- Justificación: Context Engineering (Anthropic), Multi-Agent Framework (Google), reducción de propagación de errores
- Añadida meta-regla en CLAUDE.md: decisiones justificadas por especialistas, no por criterio personal
- Actualizada propuesta de diseño en `diseno/sistema-agentes-propuesta.md`

---

## [2026-03-15] — Rediseño sistema de agentes + Prueba comparativa de modelos

### Decisión — Sistema v5.0 descartado como sistema funcional
- Los 7 prompts .md + orquestador NO eran agentes autónomos: eran instrucciones cargadas manualmente en Claude
- Sin automatización, memoria, orquestación ni aprendizaje
- Decisión: rediseño completo con framework de agentes reales

### Seleccionado — CrewAI como framework
- Alternativas evaluadas y descartadas: n8n (automatización, no agentes), Python custom (riesgo), LangGraph (excesivo)
- CrewAI ofrece: agentes con herramientas, memoria persistente, orquestación secuencial, soporte multi-modelo
- Pendiente: diseño detallado de la arquitectura antes de implementar

### Añadido — Prueba comparativa de 3 modelos LLM
- Script `scripts/probar_modelos.py`: genera misma sección (Vocabulario U03) con 3 modelos
- Resultados en `scripts/resultados_prueba/` (claude-sonnet.md, kimi-k2.md, qwen3-32b.md)
- Claude Sonnet 4.6: mejor calidad, español editorial impecable ($0.13/sección)
- Kimi K2 (Groq): aceptable con revisión, errores menores ortográficos ($0.03/sección)
- Qwen 3 32B (Groq): descartado — errores factuales en traducciones y sílabas tónicas ($0.008/sección)

### Añadido — APIs y configuración
- `.env` con API keys de Anthropic y Groq (gitignored)
- `.gitignore` actualizado: `.env`, `__pycache__/`, `*.pyc`
- CLAUDE.md actualizado: estado, sistema de agentes, preguntas pendientes 7-8, estructura, restricciones

---

## [2026-03-15] — Contenidos índice en BD + Script importación + Validación inventario U03

### Añadido — `contenidos_indice` JSONB en tabla `unidades`
- Campo JSONB añadido a la tabla `unidades` con ALTER TABLE
- Poblado para las 10 unidades (U00-U09) desde el índice general del libro
- Contiene: vocabulario, gramática, comunicación, cultura por unidad
- Solución parcial al reciclaje inter-unidad: permite consultar contenidos de cualquier unidad previa
- **Pendiente:** verificar y completar con detalle real cuando se generen inventarios completos
- Diagrama ER actualizado en `diagrama.py`

### Añadido — Script de importación JSON → PostgreSQL
- `scripts/importar_inventario.py`: importa inventario JSON a Neon PostgreSQL
- Idempotente: borra la unidad existente (CASCADE) y reimporta
- Diseñado para cualquier unidad (U01-U09), recibe el JSON como argumento
- U03 importada: 10 páginas, 47 actividades, 184 respuestas, 3 cuadros gramaticales
- CLAUDE.md actualizado: script marcado como completado, `scripts/` añadido a estructura

### Eliminado — Tabla `dependencias_seccion`
- Eliminada de Neon PostgreSQL (estaba vacía, nunca se pobló)
- Motivo: redundante — el orden de secciones y la lógica de reciclaje ya están definidos en los prompts de cada agente
- Esquema pasa de 10 a 9 tablas
- Añadida pregunta pendiente 6 en CLAUDE.md: cómo instrumentar el proceso de reciclaje de contenidos

---

## [2026-03-15] — Validación inventario U03 contra PDF + Material fuente

### Corregido — Inventario U03 (validación contra PDF embebido)
- 6 errores corregidos tras comparación visual página a página (10 páginas, 34-43):
  1. `contenidos_indice.gramatica`: "Verbo tener" → "Interrogativos"
  2. p35 act5 texto_modelo: "seis años" → "ocho años"
  3. p35 act7 respuesta 4: "hermano" → "hermanos" (plural)
  4. p36 cuadro Interrogativos, ejemplo Qué: "¿Qué hora comes?" → "¿Qué comes?"
  5. p36 act3 ítem 4: "¿Dónde / Cuál" → "¿Cómo / Dónde"
  6. p43 act5 sopa de letras: cuadrícula completa reescrita, respuestas "padre, sobrina" → "hijo, tío"

---

## [2026-03-15] — Material fuente PDF y limpieza de JPGs

### Modificado — Material fuente U03
- PDF embebido generado desde InDesign: `datos/fuente/U03/U03-libro.pdf` (4 MB, texto seleccionable)
- 10 JPGs eliminadas de `datos/fuente/U03/` (git rm, ya no necesarias)
- Carpeta residual `datos/imagenes/` eliminada
- Fichero residual `datos/U03-inventario.json` eliminado (duplicado del que está en `datos/inventarios/`)
- Referencias en inventario JSON actualizadas: apuntan al PDF en vez de a JPGs individuales
- CLAUDE.md actualizado: tarea de PDF marcada como completada

---

## [2026-03-14] — Reorganización de datos/, base de datos Neon y diagrama de procesos

### Añadido — Base de datos (Neon PostgreSQL)
- Esquema creado en Neon (neon.tech) con 10 tablas
- Tablas de contenido: unidades (con campo curso), paginas, actividades, respuestas, cuadros_gramaticales
- Tablas de relaciones: reciclaje, dependencias_seccion
- Tablas Layer 3: profesores (nombre, centro, país, nivel escolar), grupos (cantidad estudiantes, NEE, horas/semana, duración clase, horas/año), personalizaciones (vinculada a grupo, no a profesor)
- Decisión de diseño: profesores y grupos separados porque un profesor puede tener varios grupos con contextos distintos
- Índices para consultas frecuentes
- Diagrama ER añadido como nueva pestaña en diagrama de procesos

### Modificado — Estructura del proyecto
- `datos/` reorganizado: separación de material fuente (`datos/fuente/`) e inventarios extraídos (`datos/inventarios/`)
- `datos/imagenes/U03/*.jpg` → `datos/fuente/U03/*.jpg` (git mv, historial preservado)
- `datos/U03-inventario.json` → `datos/inventarios/U03-inventario.json` (git mv, historial preservado)
- Todas las referencias actualizadas en: inventario JSON, diagrama.py, unidades U03, audit.md, diseño

### Modificado — CLAUDE.md
- Estructura del repositorio actualizada con nueva organización de `datos/`
- Añadida sección "Proceso de generación del inventario": PDF embebido → Claude → JSON → PostgreSQL
- Añadida sección "Base de datos (Neon PostgreSQL)"
- Tareas pendientes documentadas: generar PDF embebido U03, script importación JSON → PostgreSQL

### Añadido — Diagrama de procesos (`diagrama.py`)
- Servidor local (python3, zero deps) en http://127.0.0.1:8080
- 4 diagramas Mermaid: arquitectura general, flujo de generación, dependencias entre secciones, agentes U03
- Tabla de estado con escaneo en tiempo real del proyecto (polling cada 3 seg)
- Arquitectura corregida: Libro → Material fuente → Inventario JSON → Agentes (flujo secuencial)

### Modificado — Diagrama de procesos
- Tildes corregidas en todos los textos (Gramática, Comunicación, Evaluación, etc.)
- Labels de tabla con nombres correctos en español
- Actualización en tiempo real de todos los diagramas (no solo la tabla)

---

## [2026-02-20] — Píldoras Formativas, mejoras estructurales de agentes y reescritura U03

### Modificado — Agentes (mejoras estructurales derivadas de la revisión de U03)
- `agentes/ag-vocabulario.md` — §9 ampliada con transiciones anticipatorias entre fases (CLT: carga extrínseca). Regla de posición de píldora formativa añadida al template: ANTES de la fase que la necesita (VanPatten). Añadidas §10 (Nivel de detalle y confianza en el profesor), §11 (Integración de estación de servicio en fases, MCER aprender a aprender), §12 (Dinámicas de gestión de aula: banco de 7 dinámicas para práctica oral, solo en F2b y práctica libre).
- `agentes/ag-gramatica.md` — Template de output actualizado: eliminadas cajas ASCII, píldora reposicionada ANTES de la fase, doble título (técnico + funcional). Añadidas §7-§11 (versiones comprimidas de §9-§12 de ag-vocabulario.md con referencia cruzada).

### Modificado — Píldoras Formativas
- `agentes/ag-vocabulario.md` — Sección "Notas Lingüísticas" reescrita completamente como "Píldoras Formativas". Añadido banco de acciones con 6 categorías y ~40 acciones concretas. Lógica de selección con 4 variables contextuales.
- `agentes/ag-gramatica.md` — Sección "Notas Lingüísticas" renombrada a "Píldoras Formativas". Referencia al banco de acciones compartido en ag-vocabulario.md.
- `unidades/U03-familia.md` — 4 "NOTA LINGÜÍSTICA" renombradas a "PÍLDORA FORMATIVA". Encabezado §2 actualizado.
- `unidades/U01-U09` — Encabezado §2 "Notas lingüísticas para el profesor" → "Píldoras formativas para el profesor" en todos los templates.

### Modificado — U03 Familia (Bloque 1 Vocabulario)
- `datos/inventarios/U03-inventario.json` — Reescritura completa contra imágenes del libro del profesor: añadido campo `respuestas` a todas las actividades, pistas de audio 31-42, corrección p.38 (4 personajes + vídeo), corrección p.36 act.1 tipo y act.2 nueva, p.37 act.5 ampliada a 9 ítems, recuadros naranjas como campos separados.
- `unidades/U03-familia.md` — Fases 4, 5 y 6 reescritas según propuesta del autor: Fase 4 simplificada (escucha activa + transición tarjetas), Fase 5 con píldora proyectada ANTES + alumnos preguntan con libros cerrados + tarjetas como comprobación autónoma, Fase 6 con instrucción marco + 4 dinámicas opcionales (palmada, doble palmada, sí/no, L1→L2).

---

## [2026-02-16] — Revisión completa, JSON actualizado y "escucha y repite"

### Modificado
- `datos/inventarios/U03-inventario.json` — Actualizado Vocabulario (p.34-35) para nueva edición del libro: act. 2 cambia de "relaciona" a "forma frases"; act. 5 texto modelo corregido (Ana tiene 6 años, no 8); act. 6 texto de Javier actualizado (Getafe = ciudad, no pueblo; añadida edad Alejandra y fútbol); acts. 7-10 reorganizadas (7 = completa frases sobre Javier, 8 = texto de Lucía Alonso de Cantabria en lugar de Leonora arahuaca de Colombia, 9 = preguntas sobre Lucía, 10 = síntesis comparativa Javier/Lucía con 6 frases); reducido de 11 a 10 actividades.
- `unidades/U03-familia.md` — Fase 2 reescrita: "escucha y repite" es ahora el eje central de la fase, como pide la actividad 1 del libro. Secuencia: (1) el profesor señala brevemente las 3 generaciones del árbol, (2) primera escucha global del audio, (3) segunda escucha con repetición oral de cada término, (4) refuerzo con el árbol de la pizarra. Antes: la presentación oral del profesor era el eje y el audio era accesorio al final.
- `unidades/U03-familia.md` — Título funcional de Fase 2 actualizado: de "PRESENTE EL VOCABULARIO CON EL ÁRBOL GENEALÓGICO" a "ESCUCHE Y REPITA LOS TÉRMINOS DE PARENTESCO".
- `unidades/U03-familia.md` — Texto corrupto de act. 6 corregido (duplicación "Madrid. La madre, Catalina, estudia..." eliminada).
- `unidades/U03-familia.md` — Etiquetas internas restantes eliminadas: "Weaning off —" en Fase 6, "(F4)" en Reflexión final, "(F5)" en Consolidación distribuida, "F1a del Ciclo de 5 fases: modelling" y "Agente Gramática" en notas lingüísticas. Sustituidas por lenguaje neutro para el profesor.
- `unidades/U03-familia.md` — Frase 2 de act. 10 corregida (punto espurio eliminado).
- `unidades/U03-familia.md` — Fase 3 reescrita completamente: de "Descubra el patrón de género -o/-a" a "Active la conciencia gramatical". Cambios principales: (1) el descubrimiento del patrón -o/-a pasa a la píldora formativa gramatical (inductiva, enfoque VanPatten/Conti) que se proyecta; (2) se introduce el posesivo "su" con la estructura "Su + parentesco se llama ___"; (3) los alumnos clasifican los 11 nombres del árbol en masculinos/femeninos en sus cuadernos ANTES de la escucha, como estrategia de comprensión; (4) el género funciona como herramienta para la Actividad 2, no como conocimiento abstracto. Fase 4 ajustada: eliminada pre-escucha redundante (los alumnos ya tienen los nombres clasificados desde Fase 3), la escucha 1 conecta con las hipótesis previas. Eliminado refuerzo post-corrección (ya innecesario). Nota lingüística simplificada.

---

## [2026-02-16] — Formato de output, formulación de objetivos y fundamentación teórica

### Añadido
- `referencias/formulacion-objetivos.md` — Documento de referencia v2 para formulación de objetivos. Incorpora: 3 tipos de objetivos (comunicativo/lingüístico/gramatical), objetivos de procesamiento del input (VanPatten), regla del "no 2 por 1", correspondencia ACTFL-MCER (A1 ≈ Novice High), modelo SMART completo (5 componentes con temporalización), regla del 40% para número de objetivos, 5 errores frecuentes, matiz de Conti sobre Bloom en lenguas. Fuentes: MCER, PCIC, ACTFL, VanPatten, Canale y Swain, Long, Ellis, Dörnyei, Deci y Ryan, Vygotsky, Marzano, Wiggins y McTighe.
- `unidades/U03-vocabulario-tarjetas.csv` — Archivo CSV independiente (18 palabras, delimitador punto y coma, UTF-8) listo para importar en InDesign mediante data merge.

### Modificado
- `agentes/ag-vocabulario.md` — Eliminadas todas las cajas ASCII (┌─┐│└─┘) del formato de output. Sustituidas por encabezados markdown en negrita. Concepto de "Caja" preservado como instrucción funcional para el profesor (qué material preparar/imprimir). Añadida referencia a `formulacion-objetivos.md` para verbos observables.
- `unidades/U03-familia.md` — Reescritura completa de §3.1 Vocabulario ajustada al contenido real de la nueva versión del libro (p.34-35). 10 actividades en 3 bloques (B1: acts. 1-4, B2: acts. 5-7, B3: acts. 8-10), 13 fases. Nombres del árbol genealógico corregidos (Carmen, Roberto, Carlos, Alicia, María, Nacho, Juana, Luis, Álvaro, Paloma, Pilar). Segundo personaje: Lucía Alonso (Cantabria) en lugar de Leonora (arahuaca, Colombia). Nota intercultural actualizada (contraste urbano/rural en España). Textos del libro transcritos. Objetivos verificados contra `formulacion-objetivos.md` v2. CSV y tabla de tarjetas actualizados.
- `unidades/U03-vocabulario-tarjetas.csv` — Ejemplos actualizados con personajes reales del libro (David, Javier, Lucía, Alicia, Luis, Carmen, etc.).
- `unidades/U03-familia.md` — Objetivo Bloque 1 reformulado a nivel macro: "Reconocer y nombrar los términos de parentesco básicos en español" (eliminada referencia al árbol genealógico como medio de aprendizaje).
- `referencias/formulacion-objetivos.md` — Añadida §7.6: confundir medio de aprendizaje con objetivo + formular a nivel de actividad individual. Regla para agentes: el objetivo describe el resultado macro del bloque.
- `agentes/ag-vocabulario.md` — Añadida instrucción de §7.6 en formato de objetivo de bloque.
- `unidades/U03-familia.md` — Gamificación simplificada: insignia renombrada de "GENEALOGISTA" a "Esa es la familia mía". Eliminado sistema de puntos por bloque. Obtención descrita en términos generales. Eliminados bloques de "Gamificación — Bloque X". Cierre de sección sin recuento de puntos.
- `agentes/ag-vocabulario.md` — Template de gamificación actualizado: nuevo formato (Objetivo + Imprimir + Insignia y obtención general). Eliminado desglose de puntos por bloque. El profesor decide el mecanismo de evaluación.
- `unidades/U03-familia.md` — Gamificación confirmada como UNA por sección: eliminadas 2 referencias a "Reto GENEALOGISTA" en actividades 4 y 9 (sustituidas por "¡Reto!" genérico). Justificación de act. 9 clarificada ("elemento lúdico competitivo", no "gamificación").
- `agentes/ag-vocabulario.md` — Gamificación clarificada como UNA por sección en §6 Decisiones y en template de output. 3 reglas explícitas: (1) una gamificación por sección, (2) obtención general, (3) retos en actividades ≠ gamificación (no llevan nombre de insignia).
- `unidades/U03-familia.md` — Fase 1 reescrita: explotación de foto introductoria (p.34 izquierda) como punto de partida obligatorio. Versión limpia instruccional sin justificaciones teóricas. Preguntas con reciclaje de vocabulario conocido. Modelado inicial de 3 pares señalando la foto.
- `agentes/ag-vocabulario.md` — Añadida §7: Foto introductoria como punto de partida obligatorio (regla general para todas las secciones de vocabulario). Función pedagógica: pre-input simplificado (CLT), activación de conocimientos previos (reciclaje 70/30), modelado F1a de 2-3 pares, conexión personal sin preguntas intrusivas. Restricciones explícitas.
- `agentes/ag-vocabulario.md` — Añadida §8: Separación documento / agente. Regla general: el output para el profesor contiene solo instrucciones operativas; las justificaciones teóricas y anotaciones internas no aparecen en el producto final.
- `unidades/U03-familia.md` — Fase 1: corregido modelado (padre/madre + hijo/hija en lugar de abuelo/a, ajustado a lo visible en la foto). Doble título añadido a TODAS las fases (1-13) + cierre de sección: título técnico (trazabilidad) + TÍTULO FUNCIONAL EN MAYÚSCULAS para el profesor.
- `agentes/ag-vocabulario.md` — Template de fases actualizado con sistema de doble título: (1) Fase N técnica para trazabilidad, (2) TÍTULO FUNCIONAL EN MAYÚSCULAS para el profesor. Nota explicativa con ejemplos.
- `unidades/U03-familia.md` — Secuencialidad entre fases: eliminadas instrucciones redundantes (abrir libro cuando ya está abierto, preparar lo que ya está preparado). Eliminadas etiquetas internas del agente: *F1a — Modelling:*, *F1b — Awareness:*, Segmentación léxica (CLT), Reciclaje 70/30, (worked example obligatorio en A1), (CLT §5.7), "fomenta la metacognición".
- `agentes/ag-vocabulario.md` — §8 ampliada con lista explícita de etiquetas internas prohibidas en el output. Añadida §9: Secuencialidad entre fases (no repetir instrucciones ya ejecutadas).

---

## [2026-02-01] — Generación de U03 Vocabulario

### Añadido
- `unidades/U03-familia.md` §3.1 — Explotación completa de Vocabulario (Parientes, p.34-35) generada por Agente Vocabulario v5.0. 11 actividades en 3 bloques, 14 fases, 4 notas lingüísticas, insignia GENEALOGISTA, reciclaje 70/30 integrado.
- `pruebas/U03-vocabulario-razonamiento.md` — Documento de trazabilidad con las 10 secciones de decisiones del agente.

---

## [2025-02-01] — Sistema de agentes v5.0

### Añadido
- `propuesta-v5-sistema-agentes.md` — Propuesta completa del sistema de 14 agentes (7 de sección + 7 de soporte).
- `agentes/ag-vocabulario.md` — Prompt operativo del Agente Vocabulario.
- Repertorios de explotación por tipo de actividad.

### Modificado
- `unidades/U03-familia.md` — Actualizado de v4.0 a v5.0: eliminada explotación manual, preparado para generación por agentes.

---

## [2025-01-31] — Estructura inicial del proyecto

### Añadido
- `unidades/U03-familia.md` — Creación inicial con contenidos extraídos del índice y contexto secuencial.
- `00-curso-general.md` — Descripción general del curso.
- `marco-teorico-metodologico.md` — Fundamentación teórica (CLT, VanPatten, Bloom, MCER).
