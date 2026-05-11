# REVIEW — Plan de trabajo paso a paso (con gates de validación)

> **Qué es este documento:** plan operativo de las tareas pendientes. Cada paso tiene: objetivo, archivos involucrados, **condiciones de cierre (gate)**, y validación del revisor. **No se pasa al siguiente paso hasta que TODAS las condiciones se cumplen.** El revisor lee este documento en cada iteración y certifica el cumplimiento de cada gate.
>
> **Audiencia:** revisor (validar gates) + ejecutor (Claude Code) + autor (decidir).
>
> **Relación con `PROCESO-MAESTRO.md`:** maestro = decisiones cerradas + bitácora; REVIEW = plan ejecutable con gates pendientes.
>
> **Última actualización:** 2026-05-07 19:55 (commit `becaa69`, v10.77b — cierre de la serie de limpieza documental v10.72-v10.77b).

---

## Principio arquitectónico (no negociable)

**Datos centralizados + instrucciones modulares.**

- Los datos de cada unidad viven una sola vez: `unidades/UX/...`. Nunca se duplican por fase.
- Las instrucciones de cada fase viven en su carpeta: `fases/N-X/CLAUDE.md` + `fases/N-X/prompt.md`. Estas SÍ son modulares por fase.
- Razón: viola la Regla de Oro #5 (una fuente única) duplicar datos. CLAUDE.md modular ya carga solo el contexto relevante; los datos solo se cargan cuando Claude Code los lee con `Read`.
- Optimización de tokens cuando aplique: leer secciones específicas con offset/limit en lugar del archivo entero; sesiones limpias por fase (`Ctrl+L`).

---

## Reglas globales del proceso (aplican a TODOS los pasos)

Antes de declarar un paso como ✅ completado, se verifica que TODAS estas actualizaciones meta se hayan ejecutado:

| Archivo meta | Cuándo se actualiza |
|---|---|
| **`CLAUDE.md`** (raíz) | Si el paso introduce: nueva fase operativa, nueva regla de oro, nuevo comando útil, cambio en estructura de carpetas, cambio en convención de naming, nuevo archivo en lista de "documentos relacionados". |
| **`PROCESO-MAESTRO.md`** | Si el paso cierra una decisión nueva (entra en Parte 4) o resuelve una pendiente (sale de Parte 5). En cualquier caso, se añade entrada a la bitácora. |
| **`REVIEW.md`** (este archivo) | Siempre. Tras completar un paso: marcar ✅, registrar gate-met, añadir entrada a bitácora del propio REVIEW, insertar pasos nuevos si aparecieron. |
| **`CHANGELOG.md`** | Si el paso implica un commit relevante (cambio físico de archivos, código nuevo, documento nuevo). Una entrada por commit con motivo, movimientos, actualizaciones de referencias. |
| **`README.md`** | Si cambia estructura raíz, comandos, o instalación. |
| **`.gitignore` / `.dockerignore`** | Si se añaden/eliminan paths trackeables o se cambia política. |

**Si alguna actualización meta no se hizo, el gate del paso NO se considera cumplido**, aunque el trabajo principal esté hecho.

---

## Estado global

| Bloque | Estado |
|---|---|
| Fase 1 — Extracción de inventario | ✅ U0-U9 extraídas e integradas (0/0). Curso completo. Refinamientos del extractor pendientes (canon semántico + doble superficie del validador). 5 archivos operativos en `fases/1-extraccion-inventario/` |
| Infraestructura (dashboard, validador) | ✅ Activa local + ✅ desplegada en producción (Railway, B5 cerrado) |
| Documentación raíz (CLAUDE.md, README, PROCESO-MAESTRO, REVIEW) | ✅ Sincronizada (v10.104b) |
| Bloque B (cerrar infraestructura fase 1) | 🔄 Parcial — B1.5 ✅ · Fase 2 reciclaje **PAUSADA** hasta cerrar canon semántico de fase 1 (propuesta E-final aprobada por revisor 2026-05-11, pendiente de implementación). `nc1-reciclaje.json` actual (181 hilos) congelado · tarjetas dependen de B1+fase 2 · píldoras dependen de fase 5 · B5 ✅ |
| Bloque C (fases 2-8) | 📋 Pendiente |
| Bloque D (lecciones Claude Code) | 📋 Pendiente |
| Bloque E (limpieza final) | 📋 Pendiente |

---

## Bloque A — Estabilizar la fase 1 ✅ CERRADO 2026-05-07

**Sub-pasos:**
- **A1.** Validar U3 con el autor — ✅ cerrado 2026-05-05.
- **A2.** Probar el sistema con una unidad nueva — ✅ cerrado con reserva 2026-05-05 (probado con U0).
- **A3.** Resolver bugs B1-B4 — ✅ cerrado 2026-05-05.
- **A4.** Refactor documental de fase 1 — ✅ cerrado 2026-05-07 (merge `110e722`, v10.69; cierres post-merge v10.70-v10.76b).

**Resultado vivo:** U0/U1/U3 validan 0/0 con el contrato post-refactor (taxonomía 20 + destreza/enfoque); 5 archivos operativos en `fases/1-extraccion-inventario/`; validador alineado con schema en cross-check A4.5.5; refs históricas archivadas en `docs/historico/refactor-prompt-fase1/`.

**Detalle íntegro archivado** (sub-pasos A4.0-A4.6, gates, riesgos, plan ejecutable completo) en `docs/historico/REVIEW-bloque-A-cerrado.md`. La bitácora cronológica general permanece viva más abajo en este mismo archivo.

## Bloque B — Cerrar la infraestructura de fase 1 (parcial)

> **Decisiones del autor (2026-05-05):** el bloque B se ejecuta en partes:
> - **`nc1-tarjetas.json`**: requiere fase 2 primero. Sin tarjetas generadas, el global está vacío. Pendiente hasta cerrar fase 2.
> - **`nc1-pildoras.json`**: pendiente hasta trabajar U3 vocabulario (fase 5).
> - **`nc1-reciclaje.json`**: se puede discutir y diseñar ahora. El autor quiere definir cómo construirlo antes de implementar — formalizado como **B1.5** (gate de diseño previo a B2).

### B1. Escribir scripts Python para los JSONs globales del curso

**Objetivo:** poder regenerar `nc1-tarjetas.json`, `nc1-pildoras.json` con scripts deterministas (cero LLM).

**Pre-condición:** A1 + A2 cerrados (sin un sistema de extracción estable, los globales son prematuros). B3 (decidir migración del contenido editorial) idealmente cerrado.

**Archivos a crear:**
- `scripts/regenerar_tarjetas_globales.py` — lee `unidades/U*/tarjetas/csv/*.csv`, escribe `unidades/nc1-tarjetas.json` siguiendo el esquema de PROCESO-MAESTRO Parte 4 decisión 18.
- `scripts/regenerar_pildoras_globales.py` — lista `unidades/U*/pildoras/*.pdf`, parsea TEX para títulos, escribe `unidades/nc1-pildoras.json` siguiendo decisión 19.

**Archivos a modificar:**
- `CLAUDE.md` — sección "Comandos útiles": añadir los dos comandos nuevos.
- `fases/1-extraccion-inventario/prompt.md` — referenciar los scripts en la sección de pipeline.

**Actualizaciones meta requeridas:**
- `CLAUDE.md` ✓ (comandos).
- `PROCESO-MAESTRO.md` — bitácora.
- `REVIEW.md` — gate marcado.
- `CHANGELOG.md` — entrada por commit.
- `README.md` — si los scripts cambian la estructura visible.

**Gate de cierre:**
1. ✅ Los dos scripts creados y ejecutables.
2. ✅ Cada uno tiene docstring con uso.
3. ✅ Idempotencia verificada: ejecutar dos veces produce el mismo output.
4. ✅ Manejan el caso "carpeta vacía" sin fallar.
5. ✅ Documentados en CLAUDE.md.
6. ✅ Commit + CHANGELOG.

**Bloquea a:** B2 (parte tarjetas + píldoras).

---

### B1.4. Crear `nc1-curso.json` — índice editorial global del curso ✅ CERRADO 2026-05-08 (v10.82)

**Objetivo:** disponer del índice editorial canónico del curso como artefacto JSON consultable, antes de diseñar `nc1-reciclaje.json` (B1.5). Sin un mapa global de "qué enseña cada unidad", el reciclaje no se puede mapear de forma trazable.

**Fuente:** índice oficial del libro impreso (Scope and Sequence, páginas 6-7). NO se usa `viejo/00-curso-general.md`, que contenía datos imprecisos en páginas y mezclaba dato editorial con metadocumentación pedagógica.

**Decisiones de schema** (registradas como decisión 35 en PROCESO-MAESTRO Parte 4, refinada en v10.82b):
- Path: `unidades/nc1-curso.json`.
- Top-level: `curso`, `titulo`, `editorial`, `nivel`, `fuente`, `estructura_libro`, `unidades`, `apendice`, `_nota` (opcional).
- Por unidad regular (U1-U9): campos top-level `vocabulario`, `gramatica`, `para_aprender` (string o `null`), `pronunciacion_ortografia`, `comunicacion`, `destrezas`, `cultura`, `pagina_inicio`, `paginas_libro`.
- Por U0 (atípica): solo `contenido_general`.
- Apéndice: array de objetos con `seccion` y `pagina_inicio`, sin contenido detallado.
- Contenido de las celdas: **literal del índice del libro**, sin interpretación MCER añadida.
- **Source of truth refinada (v10.82b):** `nc1-curso.json` es canónico para el índice editorial; los inventarios per-unidad pueden divergir legítimamente y la divergencia se anota como deuda técnica en `_nota`, **no bloquea cierre**.

**Hallazgos durante la extracción del índice del libro:**
- Las páginas en `viejo/00-curso-general.md` estaban mal: U1=10-23 y U2=14-33 se solapaban. Las correctas según Scope and Sequence son U1=12-21, U2=22-31, ..., U9=92-101.
- **U3 paginación divergente:** Scope dice 32-41; el inventario actual de U3 dice 34-43. **Causa identificada por el autor:** el PDF actual de U3 tiene errores; la unidad se re-extraerá por el ejecutor 2 en un worktree paralelo cuando el autor proporcione un PDF correcto. Anotado en `_nota` de `nc1-curso.json`.
- Los `contenidos_indice` ya extraídos de U1 y U3 mezclan "PARA APRENDER" (estrategia metacognitiva) dentro del campo `gramatica` (ej. U3 "Hacer un cuaderno de vocabulario"). Anotado como fix futuro de los inventarios.

**Gate cerrado:**
1. ✅ `unidades/nc1-curso.json` creado con datos literales de las 10 unidades + apéndice.
2. ✅ JSON parseable.
3. ✅ Decisión 35 registrada en PROCESO-MAESTRO Parte 4.
4. ✅ Commit + CHANGELOG.

**Bloquea a:** B1.5.

---

### B1.5. Diseño de `nc1-reciclaje.json` — definir contrato antes de generar ✅ CERRADO (v10.89, 2026-05-08)

**Objetivo:** cerrar formalmente cómo se construye `nc1-reciclaje.json`.

**Gate de cierre:**
1. ✅ Disparadores, formato per-entrada, política de mantenimiento y esqueleto top-level cerrados con el autor.
2. ✅ Decisión registrada en PROCESO-MAESTRO.md (bloque `nc1-reciclaje.json`).
3. ✅ Esqueleto top-level confirmado — igual al que asume B2. Sin ajustes en B2.
4. ✅ `unidades/nc1-reciclaje.json` creado vacío.
5. ✅ Commit + CHANGELOG.

**Bloquea a:** B2 (parte reciclaje).

---

### B2. Completar los 3 JSONs globales del curso

**Objetivo:** tener `nc1-tarjetas.json`, `nc1-pildoras.json` y `nc1-reciclaje.json` en `unidades/` con contenido real. **U3 no ancla este paso.**

**Estado actual:**
- `nc1-reciclaje.json` — ✅ poblado pase 1 (v10.94): 23 hilos / 70 eventos cubriendo U0-U9 desde `nc1-curso.json`. Schema modelo de hilos, taxonomía 4 tipos (vocabulario, forma_verbal, contenido_gramatical, estrategia).
- `nc1-tarjetas.json` — 📋 no existe. Bloqueado por B1 (script) + fase 2 (vocabulario analizado).
- `nc1-pildoras.json` — 📋 no existe. Bloqueado por fase 5 (píldoras por unidad).

**Sub-pasos desacoplados:**

**B2a — Primera población de `nc1-reciclaje.json`** ⚠ **ANULADO (replanteamiento 2026-05-11)**

El modelo de hilos jerárquicos (mapa/auto/detalle, pase 1/pase 2) queda anulado por la propuesta E-final, que mueve la autoridad de naming de fase 2 a fase 1 mediante un canon semántico. Los hilos del `nc1-reciclaje.json` actual quedan **congelados** hasta que el canon esté limpio. La reformulación de fase 2 entra como trabajo posterior al cierre del canon.

- ~~B2a.1 — Pase 1 (mapa)~~: estado histórico (v10.94 cubría 23 hilos / 70 eventos). Se reformula tras canon.
- ~~B2a.2 — Pase 2 (detalle)~~: no se ejecutará en su forma original.

**B2b — Crear `nc1-tarjetas.json`** (bloqueado)
- Pre-condición: B1 (script `regenerar_tarjetas_globales.py`) + al menos una unidad con vocabulario analizado (fase 2).

**B2c — Crear `nc1-pildoras.json`** (bloqueado)
- Pre-condición: fase 5 (primera unidad con píldoras).

**Actualizaciones meta requeridas (por sub-paso):**
- `PROCESO-MAESTRO.md` — bitácora.
- `REVIEW.md` — gate.
- `CHANGELOG.md` — commit.

**Gate de cierre de B2 completo:**
1. ✅ Los 3 archivos existen y tienen contenido real.
2. ✅ Cada uno cumple su esquema (validable visualmente).
3. ✅ Commit + CHANGELOG.

**Bloquea a:** B4.

---

### B3. Decidir migración de tarjetas/pildoras/MDs de U3 a `unidades/U3/`

**Objetivo:** cerrar la cuestión de si solo el inventario de U3 está en el sistema activo, o todo el contenido editorial.

**Pre-condición:** ninguna (decisión del autor).

**Archivos involucrados (si se decide migrar):**
- Mover `viejo/unidades/U03/tarjetas/` → `unidades/U3/tarjetas/`.
- Mover `viejo/unidades/U03/pildoras/` → `unidades/U3/pildoras/`.
- Mover los markdowns de sección → `unidades/U3/<seccion>.md` (decidir naming).

**Actualizaciones meta requeridas:**
- `PROCESO-MAESTRO.md` — entrada en Parte 4 con la decisión.
- `CLAUDE.md` — actualizar estructura del repo si cambia.
- `REVIEW.md` — gate.
- `CHANGELOG.md` — entrada del movimiento.
- `.gitignore` — actualizar paths si aplica.

**Gate de cierre:**
1. ✅ Decisión cerrada y registrada en PROCESO-MAESTRO Parte 4.
2. ✅ Si se decide migrar: contenido movido y rutas internas actualizadas.
3. ✅ Si se decide NO migrar: anotado claramente que U3 activa = solo inventario, el resto vive en viejo y se aprovechará al final.
4. ✅ Commit + CHANGELOG.

---

### B4. Integrar visualización de los 3 JSONs globales en el dashboard

**Objetivo:** poder revisar los globales desde el dashboard.

**Pre-condición:** B2 cerrado.

**Archivos a modificar:**
- `diagrama.py` — endpoint `/api/reciclaje` ya existe (v10.92); pendientes `/api/tarjetas` y `/api/pildoras` cuando se generen los JSONs respectivos.
- `web/index.html` — vista RECICLAJE ya operativa (v10.92); pendientes vistas para tarjetas y píldoras.

**Actualizaciones meta requeridas:**
- `CLAUDE.md` — solo si introduce cambio en cómo invocar dashboard.
- `PROCESO-MAESTRO.md` — bitácora.
- `REVIEW.md` — gate.
- `CHANGELOG.md` — commit.

**Gate de cierre:**
1. ✅ Los 3 endpoints funcionan (verificar con `curl`).
2. ✅ La vista en el dashboard muestra los 3 globales legibles.
3. ✅ Schema-aware: si un global está vacío, se ve "vacío" sin errores.
4. ✅ Commit + CHANGELOG.

---

### B5. Despliegue público del dashboard — ✅ CERRADO 2026-05-06 (carril paralelo)

> **Contexto:** este paso se ejecutó **fuera del orden B1-B4**, como carril paralelo, a petición del autor para compartir el dashboard con el equipo editorial. Se documenta retroactivamente para que el plan refleje el trabajo real y se elimine la doble verdad operativa entre bitácora y plan.

**Objetivo:** dashboard accesible públicamente para el equipo editorial (consultar Inventarios + Proyecto), sin BD ni Langfuse.

**Decisión de scope (autor):** los módulos con BD (tarjetas, correcciones, reglas, agentes, trazas) se quedan inactivos en el despliegue porque corresponden a flujos no operativos hoy.

**Archivos involucrados:**
- `requirements.txt` — quitadas deps no usadas (`crewai`, `langfuse`, `deepeval`).
- `Dockerfile` — quitado nodejs y promptfoo CLI no usados.
- `diagrama.py` — fixes ortográficos en etiquetas Mermaid (Compañeros, Validación, Píldoras, etc.).
- `railway.toml` — sin cambios, ya existente.

**Gate cumplido:**
1. ✅ URL pública responde HTTP 200: `https://entornoeditorial.up.railway.app`.
2. ✅ `/api/version` devuelve la versión del CHANGELOG (auto-leída).
3. ✅ Build slim funcional (deps mínimas: `psycopg2-binary` + `python-dotenv`).
4. ✅ Diagramas Mermaid con ortografía corregida (tildes y eñes).
5. ✅ Commits referenciados: `5024914` (fix ortográfico v10.33), `3611bd7` (build slim v10.34), `b3b07e2` (CHANGELOG retroactivo). Pusheados a `origin/main`.

**Bloquea a:** ya nada operativo. Pendiente de decisión externa: si en el futuro se quiere control de acceso (basic auth o Cloudflare Access), se abre paso aparte.

---

## Bloque C — Diseñar y construir las fases 2-8

### Plantilla de pasos por cada fase

Para cada fase nueva (2 a 8), repetir la secuencia C.X.1 → C.X.6:

#### C.X.1 Cerrar criterios de la fase con el autor (chat)
**Pre-condición:** fase anterior cerrada (o decisión explícita de paralelismo).
**Archivos:** ninguno físico todavía.
**Meta:** `PROCESO-MAESTRO.md` — añadir decisiones a Parte 4.
**Gate:** autor confirma criterios cerrados.

#### C.X.2 Crear prompt versionado de la fase
**Archivos a crear:**
- `fases/<N>-<nombre>/prompt.md`
- *Opcional:* `fases/<N>-<nombre-fase>/CLAUDE.md` (CLAUDE.md específico que se carga al trabajar dentro de esa carpeta).

**Meta:**
- `CLAUDE.md` (raíz) — actualizar tabla de las 8 fases (Estado: 🛠 En construcción → ✅ Operativa cuando se cierre).
- `PROCESO-MAESTRO.md` — bitácora.
- `REVIEW.md` — gate.
- `CHANGELOG.md` — commit del prompt nuevo.

**Gate:** prompt completo, autor lo aprueba.

#### C.X.3 Implementar scripts auxiliares (si aplica)
**Archivos a crear:** según necesidad (`scripts/<accion>.py`).
**Meta:** `CLAUDE.md` (comandos), `CHANGELOG.md`, `REVIEW.md`.
**Gate:** scripts ejecutables, idempotentes, documentados.

#### C.X.4 Probar la fase con U3
**Archivos a crear:** outputs de la fase (CSVs, MDs en `unidades/U3/<seccion>/`).
**Meta:** `CHANGELOG.md`, `REVIEW.md`.
**Gate:** output validado por autor.

#### C.X.5 Iterar prompt según errores
**Archivos a modificar:** `fases/<N>-<nombre>/prompt.md`.
**Meta:** `CHANGELOG.md`, `REVIEW.md`.
**Gate:** sin errores nuevos en una segunda pasada.

#### C.X.6 Cierre de la fase
**Meta:**
- `CLAUDE.md` — fase marcada ✅ Operativa en la tabla, prompt en lista de "documentos relacionados".
- `PROCESO-MAESTRO.md` — bitácora final.
- `REVIEW.md` — bloque C.X marcado ✅, siguiente fase desbloqueada.
- `CHANGELOG.md` — commit "vX.X: fase <N> operativa".
- `README.md` — si cambia estructura visible.

**Gate:** TODOS los anteriores cumplidos.

### Orden recomendado de las fases

| Orden | Fase | Justificación |
|---|---|---|
| 1.º | Fase 2 — Análisis de vocabulario | Más simple, alimenta fase 3. |
| 2.º | Fase 3 — Tarjetas de vocabulario | Mucho material en `viejo/` aprovechable. |
| 3.º | Fase 5 — Píldoras formativas | Protocolo en `viejo/agentes/ag-vocabulario.md` y `ag-gramatica.md`. |
| 4.º | Fase 4 — Tarjetas de estrategia | Requiere ≥2 unidades para validar "no repetir". |
| 5.º | Fase 6 — Generación sección por sección | Cuando las anteriores estén estables. |
| 6.º | Fase 7 — Doble versión | Consume fase 6. |
| 7.º | Fase 8 — Principios + repertorios | Apoyo transversal, puede empezarse en paralelo. |

---

## Bloque D — Sistema de lecciones de Claude Code

### D1. Diseñar el formato y la activación de las lecciones
**Objetivo:** decidir cómo se registran y cargan los aprendizajes que evitan errores recurrentes.

**Pre-condición:** ninguna.

**Archivos a decidir (con autor):**
- ¿Un único archivo `lecciones-claude.md` en raíz, o uno por fase?
- ¿Cómo se activa? ¿Referenciado desde CLAUDE.md raíz, o auto-cargado?
- ¿Formato: cronológico, por sección, por tipo de error?

**Meta:** `PROCESO-MAESTRO.md` decisión cerrada en Parte 4.
**Gate:** decisión documentada.

### D2. Crear el contenedor y la primera lección
**Pre-condición:** D1 cerrado.

**Archivos a crear:** según D1 (ej. `lecciones-claude.md`).

**Primera lección a registrar:** "El contenido de cada actividad debe aparecer en `datos.items_libro` (o equivalente) **exactamente como en el libro**, no como referencia ni respuesta. Detectada el 2026-05-05 al revisar U3."

**Meta:**
- `CLAUDE.md` — añadir referencia a lecciones.
- `PROCESO-MAESTRO.md` — bitácora.
- `REVIEW.md` — gate.
- `CHANGELOG.md` — commit.

**Gate:**
1. ✅ Archivo creado con primera lección.
2. ✅ CLAUDE.md actualizado.
3. ✅ Commit + CHANGELOG.

---

## Bloque E — Limpieza final (al cerrar todo el curso)

**Pre-condición global:** todas las fases ✅ operativas, U1-U9 extraídas, JSONs globales completos, dashboard estable.

### E1. Decidir qué se conserva de `viejo/`
**Archivos:** revisar `viejo/` carpeta por carpeta.
**Meta:** `PROCESO-MAESTRO.md` con la decisión carpeta por carpeta.
**Gate:** lista cerrada de "qué se migra antes de borrar".

### E2. Migrar lo aprovechable
**Pre-condición:** E1 cerrado.
**Meta:** `CHANGELOG.md` con cada movimiento, `CLAUDE.md` actualizado.
**Gate:** todo lo de la lista E1 migrado y verificado.

### E3. Eliminar `viejo/`
**Pre-condición:** E2 cerrado + autor da OK explícito.
**Archivos a eliminar:** `viejo/` completo.
**Meta:** `CLAUDE.md`, `README.md`, `PROCESO-MAESTRO.md`, `.gitignore`, `.dockerignore` — eliminar todas las referencias.
**Gate:** sin referencias residuales en código ni docs.

### E4. Eliminar `PROCESO-MAESTRO.md` y `REVIEW.md`
**Pre-condición:** todo el contenido valioso integrado en `CLAUDE.md`, `README.md`, prompts.
**Meta:** `CLAUDE.md` ya integrado lo esencial; `CHANGELOG.md` registra la eliminación.
**Gate:** autor confirma que no se pierde información operativa.

### E5. Reescribir `README.md` y `CHANGELOG.md` con el estado final
**Meta:** documentación final coherente.
**Gate:** README explica el sistema de un solo vistazo, CHANGELOG cierra la migración.

---

## Tabla maestra de archivos por categoría

### Archivos del sistema (raíz, en uso)
| Archivo | Estado | Próxima modificación esperada |
|---|---|---|
| `CLAUDE.md` | ✅ Activo, conciso (Anthropic best practices) | Cada cierre de fase, cada cambio en estructura/comandos/reglas |
| `PROCESO-MAESTRO.md` | ✅ Activo | Cada decisión nueva o cierre de pendiente |
| `REVIEW.md` | ✅ Activo | Continuamente: cada paso completado, nuevos pasos detectados |
| `README.md` | ✅ Actualizado | Cuando cambia estructura raíz, comandos, instalación |
| `CHANGELOG.md` | ✅ Activo | En cada commit relevante (siempre que haya cambio físico) |
| `ROADMAP.md` | ⚠ Heredado, sin tocar | Cuando se decida si reescribir o eliminar |
| `GITHUB-MANIFEST.md` | ⚠ Heredado, sin tocar | Cuando se decida si reescribir o eliminar |
| `.gitignore` | ✅ Actualizado | Cuando cambien rutas trackeables |
| `.dockerignore` | ✅ Actualizado | Cuando cambien rutas trackeables |

### Código activo (raíz)
| Archivo | Estado | Próxima modificación esperada |
|---|---|---|
| `diagrama.py` | ✅ Activo, sirviendo en producción (Railway) | B4 (vista globales), nuevos endpoints si surgen |
| `web/index.html` | ✅ Vista Inventarios funcional | B4, mejoras estéticas |
| `eval/` | ⚠ Heredado | Bloque C cuando aplique |
| `fases/1-extraccion-inventario/prompt.md` | ✅ Operativo | A1 (con cada error nuevo en U3), A2 (con casos nuevos en otras unidades) |
| `scripts/validar_inventario.py` | ✅ Operativo | Cuando se añada un caso de validación |
| `scripts/regenerar_tarjetas_globales.py` | 📋 No existe | B1 |
| `scripts/regenerar_pildoras_globales.py` | 📋 No existe | B1 |

### Contenido editorial (raíz)
| Carpeta/Archivo | Estado | Próxima modificación |
|---|---|---|
| `unidades/U0/U0-nc1-inventario.json` | ✅ Validado · trackeado · unidad atípica (1 aviso intencional por `_nota_unidad_atipica`) | Ninguna prevista |
| `unidades/U1/U1-nc1-inventario.json` | ✅ Validado · trackeado | Ninguna prevista |
| `unidades/U2/U2-nc1-inventario.json` | ✅ Validado · trackeado (integrado en v10.87) | Ninguna prevista |
| `unidades/U3/U3-nc1-inventario.json` | ✅ Validado · trackeado (reintegrado en v10.91 con PDF correcto, 47 actividades, 32-41) | Ninguna prevista |
| `unidades/U3/fuente/U3-nc1.pdf` | ✅ PDF correcto (gitignored) | — |
| `unidades/U3/tarjetas/`, `pildoras/`, MDs | 📋 No migrados | B3 |
| `unidades/U4/U4-nc1-inventario.json` | ✅ Validado · trackeado (integrado v10.93, 49 actividades, 6 cuadros, 42-51) | Ninguna prevista |
| `unidades/U5/`...`U9/` | 📋 Carpetas vacías, sin inventario | Nuevas extracciones (U5 → ejecutor 2 en `extract/U5`) |
| `unidades/nc1-tarjetas.json` | 📋 No existe | B2 |
| `unidades/nc1-pildoras.json` | 📋 No existe | B2 |
| `unidades/nc1-reciclaje.json` | ✅ Poblado pase 1 (v10.94): 23 hilos / 70 eventos · U0-U9 · modelo de hilos · 4 tipos | B2a.2 — pase 2 contra inventarios |

### Archivo (`viejo/`, intocable hasta E)
| Carpeta | Estado |
|---|---|
| `viejo/CLAUDE-anterior.md` | Conservado |
| `viejo/unidades/U03/` | Contenido editorial original |
| `viejo/scripts/` | Scripts CrewAI v5 antiguos |
| `viejo/agentes/`, `viejo/repertorios/`, `viejo/referencias/`, `viejo/diseno/`, `viejo/_template/`, `viejo/materiales/`, `viejo/material-complementario/`, `viejo/marco-teorico-metodologico.md`, `viejo/00-curso-general.md` | Material editorial y de referencia |

---

## Cómo el revisor analiza este documento

En cada iteración:

1. Identifica el paso actual (el primero ⚠ o 📋 en el orden lógico).
2. Verifica que el ejecutor ha tocado los **archivos involucrados** que el paso lista.
3. Verifica que las **actualizaciones meta** (CLAUDE.md, PROCESO-MAESTRO, REVIEW, CHANGELOG, README, gitignore) se han hecho según corresponda.
4. Recorre el **gate de cierre** del paso, condición por condición.
5. Si TODAS las condiciones se cumplen: marca el paso como ✅ y libera el siguiente.
6. Si alguna falla: bloquea el paso, lista qué falta, devuelve al ejecutor.
7. Si en el proceso aparece un caso nuevo (bug, decisión inesperada): añade un paso nuevo en el bloque correspondiente.

---

## Bitácora de actualizaciones del REVIEW

- **2026-05-08** — Borrado de `unidades/U3/U3-nc1-inventario.json` (v10.88). El PDF de U3 que se había usado para la extracción inicial contenía errores (deuda técnica anotada en `nc1-curso.json:_nota`). El autor proporciona PDF correcto (gitignored, reemplazado en disco) y borra el JSON viejo. Main temporalmente sin inventario de U3 hasta la re-extracción por ejecutor 2 en worktree paralelo `extract/U3`. Validador U0/U1/U2 → 0/0.
- **2026-05-08** — **Integración de U2 a main** (v10.87, merge `--no-ff --no-commit` desde `extract/U2`). Primera integración del carril paralelo de extracciones tras v10.79. Contenido: `unidades/U2/U2-nc1-inventario.json` (10 páginas, 52 actividades, 6 cuadros, validador 0/0). Hallazgos cerrados antes de integrar: 7 correcciones del extractor original + 5 refinamientos de regla (v10.83-v10.86) + verificación final de U2-p29-act04 contra PDF (`expresion_escrita`, no oral). Estado: U0/U1/U2/U3 trackeadas y validando 0/0. Worktree `extract/U2` y rama se mantienen intactos. Próximo: B1.5 (ejecutor 1) + re-extracción de U3 (ejecutor 2 cuando llegue PDF).
- **2026-05-08** — Refinamiento §2.2 regla 3: individual vs parejas en respuesta a preguntas (v10.86). Caso disparador: riesgo residual del revisor sobre v10.85. Si U2-p29-act04 es intercambio en parejas, cambia tipo (no solo destreza). Decisión: bifurcar regla 3 en 3 casos: cerradas / individual / parejas. Las preguntas a verificar contra PDF de U2-p29-act04 ahora son 2 (solo o pareja; escribe o habla). 1 bullet añadido, 1 modificado, sin bloat. Single source of truth en §2.2. Validador 0/0.
- **2026-05-08** — Refinamiento §2.3: `responder_preguntas_abiertas` con destreza condicional al enunciado (v10.85). Caso disparador: hallazgo C en U2-p29-act04. Antes la regla decía siempre `expresion_escrita`; ahora bifurca: `expresion_escrita` si el libro pide escribir, `expresion_oral` si pide responder oralmente. 1 línea modificada en §2.3, 0 párrafos añadidos. Sin cambios en JSONs. U2-p29-act04 concreto pendiente de verificación contra PDF. Validador 0/0.
- **2026-05-08** — Cierre limpio de v10.83: alineación de 2 referencias vivas (v10.83b). El revisor detectó que `prompt.md:54` y `convenciones-y-casos.md:141` seguían diciendo "Para aprender → siempre actividad" sin la bifurcación, contradiciendo v10.83 desde otros entry points. Fix: `prompt.md` reescrito para nombrar los criterios sin reducirlos (la regla canónica vive en reglas-operativas §4); `convenciones-y-casos.md` §4.1 reescrita para contextualizar el caso histórico (tenía verbo imperativo) y citar la bifurcación actual. Single source of truth restablecida. Validador 0/0.
- **2026-05-08** — Schema §4 (cuadros): `texto_intro` documentado + `titulo` nullable + `lista_reglas` (v10.84). Hallazgos del ejecutor 2 en U2: (1) cuadros lista_reglas con encabezado verbatim no documentado; (2) cuadro p29 sin título; (3) tipo `lista_reglas` no en lista de ejemplos. Cambios quirúrgicos en schema-inventario.md §4 (3 líneas modificadas, 1 nueva, 0 párrafos añadidos): `titulo` ahora `<str | null>`; `lista_reglas` añadido a ejemplos de tipo; nueva línea `texto_intro: <str opcional>`. Resuelve también el hallazgo A previo (cuadro sin título). Sin cambios funcionales (contenido es estructura libre). Validador 0/0.
- **2026-05-08** — Refinamiento de regla "Para aprender" tras hallazgo del ejecutor 2 en U2 (v10.83). Caso disparador: U2-p25 "Uso de las mayúsculas" es puramente informativo (lista de reglas, sin verbo imperativo al alumno) → no encajaba en regla "siempre actividad". Decisión cerrada: bifurcar por naturaleza (con tarea → actividad; solo informativa → cuadro). Cambios en reglas-operativas.md: §1 regla 2 reformulada como índice + puntero; §4 reescrita con tabla de bifurcación + criterio decisional + ejemplos canónicos. Eliminada duplicación previa entre §1 y §4. **Sin añadir contenido** (reformulación). Auditoría U0/U1/U3: sin reclasificaciones necesarias (U3-p37-act09 "Mira el cuaderno de Ronaldo... Escribe..." tiene verbo imperativo, sigue siendo actividad legítima). U1 tiene gap de "Recursos para la clase" no extraído; fix futuro de inventario. Validador 0/0.
- **2026-05-08** — **Refinamiento de B1.4 tras dictamen del revisor** (v10.82b). 2 hallazgos cerrados: (1) schema documentado vs JSON real no coincidían (`apendice` usa `seccion` no `titulo`; `_nota` top-level no estaba documentado) → decisión 35 y B1.4 actualizados al schema real; (2) la regla "no divergencia antes de cerrar" contradecía el repo (U3 paginación 32-41 vs 34-43; U1/U3 mezclan PARA APRENDER en gramática) → regla refinada para hacer `nc1-curso.json` canónico y permitir divergencias legítimas anotadas como deuda técnica en `_nota`. Causa identificada del U3 paginación: PDF actual tiene errores, será re-extraído por ejecutor 2. No se toca JSON ni PDF de U3 ahora. Sin cambios funcionales. Validador 0/0.
- **2026-05-08** — **B1.4 cerrado**: creado `unidades/nc1-curso.json` (v10.82, decisión 35 en PROCESO-MAESTRO Parte 4). Índice editorial global del curso, derivado del Scope and Sequence oficial del libro impreso (no de meta-documentación). 10 unidades + apéndice. Contenido literal sin expansión MCER. Schema cerrado. Hallazgos anotados (no bloqueantes): páginas en `viejo/00-curso-general.md` eran imprecisas; `contenidos_indice` de U1/U3 mezclan "PARA APRENDER" con gramática (fix futuro). Próximo: B1.5 (diseño de `nc1-reciclaje.json`) con `nc1-curso.json` ya disponible para mapear flujos de reciclaje.
- **2026-05-08** — Dashboard: badge "extracción en curso" para unidades de worktrees paralelos (v10.81). Las unidades servidas vía `EXTRA_UNIDADES_PATHS` (`zona: "extra"`) ahora muestran un badge ámbar *"🔄 Extracción en curso (worktree paralelo)"* en lugar del path absoluto. Para unidades de main (`zona: ""`) se mantiene el path relativo. Al integrar una unidad a main, el cambio es automático: main gana sobre extras y el badge desaparece. Validador 0/0.
- **2026-05-08** — Dashboard: eliminado el badge de versión (v10.80b). v10.80 había hecho el badge dinámico, pero seguían apareciendo 2 indicadores en el header. Decisión del autor: dejar solo el indicador derecho que ya muestra versión + hora viva. Eliminados el span del badge y el JS que lo actualizaba. Una sola fuente visible de versión. Validador 0/0.
- **2026-05-08** — Dashboard: badge de versión dinámico (v10.80). Tras v10.79 el header mostraba dos versiones distintas: badge verde con `v10.78` hardcoded (desde v10.78) y el indicador derecho dinámico `v10.79 — hh:mm:ss`. Fix: badge ahora con `id="version-badge"` que se rellena en `init()` desde `/api/version`. Una sola fuente de verdad. Sin cambios funcionales. Validador 0/0.
- **2026-05-11** — **Decisión de diseño cerrada: canon semántico en fase 1 (propuesta E-final).** Tras 5 iteraciones revisor↔ejecutor y un giro arquitectónico, el canon de nombres permitidos para `campo_semantico` y claves de `vocabulario_consolidado` vive dentro de fase 1, integrado en sus documentos existentes sin crear archivos doc nuevos. Artefactos nuevos: `fases/1-extraccion-inventario/campos-semanticos-canonicos.json` (SoT de datos), `scripts/canon.py` (módulo compartido con 4 funciones: cargar, validar, escribir atómico, detectar pendientes), `scripts/inicializar_canon_semantico.py` (one-off poblando desde `nc1-curso.json` + subset PCIC A1). Modificaciones quirúrgicas en `CLAUDE.md`/`prompt.md`/`reglas-operativas.md`/`schema-inventario.md` de fase 1 + endurecimiento del validador con 3 canales (errores, avisos, **auditoría legacy**) + rollout R1/R2/R3 + carril A (extracción canónica desde origen) + carril B (saneamiento retrospectivo U0-U9). Dashboard solo lectura para cola de pendientes. Marca `_pendiente_canon` transitoria de worktree con triple defensa (schema, regla, validador) que bloquea cierre del inventario. Fase 2 **pausada** hasta cerrar canon. Implementación pendiente.
- **2026-05-11** — **U9 integrada a main** (v10.104) vía `integrar_unidad.py` (commit `ea4cb51`). 41 actividades, 6 cuadros, validador 0/0. Reciclaje sin cambios (92 mapa + 89 auto = 181) — U9 no introduce campos semánticos nuevos. **Curso completo extraído (U0-U9 integradas)**. Sincronización documental + autodocumentación en v10.104b.
- **2026-05-10** — Sincronización documental U8 (v10.103b) + autodocumentación + retirada de referencia a artefacto local (v10.103c).
- **2026-05-10** — **U8 integrada a main** (v10.103) vía `integrar_unidad.py` (commit `3f3e626`). 46 actividades, 5 cuadros, validador 0/0. Reciclaje actualizado: 181 hilos (92 mapa + 89 auto). Tercera integración limpia con el flujo automatizado.
- **2026-05-10** — **U7 integrada a main** (v10.102) vía `integrar_unidad.py` (commit `590c9f3`). 46 actividades, 4 cuadros, validador 0/0. Reciclaje actualizado: 171 hilos (92 mapa + 79 auto). Segunda integración limpia con el flujo automatizado, sin desviaciones.
- **2026-05-10** — Refuerzo del checklist de cierre en `fases/1-extraccion-inventario/prompt.md` (v10.101). Tras auditar los tres fixes de U6, análisis: reglas canónicas existen y son suficientes, fallos invisibles al validador. Añadidos 2 ítems al checklist (ejemplo no duplicado en respuestas; cardinalidad literal de items_libro). Sin cambios de reglas.
- **2026-05-10** — **U6 integrada a main** vía `integrar_unidad.py` (44 actividades, 4 cuadros, autoevaluación presente, validador 0/0). Primera integración con el flujo automatizado de v10.99. Reciclaje actualizado: 161 hilos totales (92 mapa + 69 auto). Tres fixes de auditoría del ejecutor 2 incluidos en el inventario final: ejemplo duplicado eliminado en `respuestas` de U6-p64-act01 y U6-p64-act02; ítem inventado #9 eliminado en U6-p65-act04. U6 usa `columnas_relaciona` (canónico desde v10.98) en U6-p63-act05, U6-p63-act08, U6-p68-act02 y U6-p71-act05.
- **2026-05-10** — Fase 2 reciclaje base automatizada + script de integración (v10.97-v10.99c). Fase 2 creada con contrato completo (`fases/2-reciclaje/CLAUDE.md` + `reglas-reciclaje.md`). Scripts: `regenerar_reciclaje_mapa.py` (nivel mapa desde `nc1-curso.json`, una vez) + `regenerar_reciclaje_vocabulario.py` (nivel auto, encadenado por `integrar_unidad.py`). Script `integrar_unidad.py` automatiza integración completa: copia, valida, actualiza reciclaje, commit aislado, con restauración de main en cualquier fallo. `nc1-reciclaje.json`: 92 hilos mapa + 59 auto = 151 hilos. U5 integrada (v10.97). Campo canónico `columnas_relaciona` añadido a fase 1 (v10.98), migración U1/U5.
- **2026-05-10** — Dashboard: `EXTRA_UNIDADES_PATHS` para servir worktrees paralelos (v10.79). Permite ver inventarios en working tree de extracciones en curso (ej. `extract/U2`) sin tener que integrarlos a main. Variable de entorno con paths separados por `:`. Main tiene prioridad; las unidades solo en extra se marcan `zona='extra'`. Refresco del navegador muestra cambios del worktree en tiempo real. Cuando la unidad se integra, automáticamente pasa a servirse desde main. Validador U0/U1/U3 → 0/0. Sin cambios en código de fase 1.
- **2026-05-08** — Dashboard: enfoque visible en inventarios + badge de versión (v10.78). Cambios pequeños alineados con el contrato post-refactor: badge `v10.78` en el header; campo `enfoque` añadido a cada actividad debajo de Destreza; renderizado correcto de `destreza` cuando es array (separador ` · `). Cambios en `web/index.html` solo. Sin afectar a worktrees de extracciones paralelas (los 5 archivos de fase 1 siguen idénticos). Necesario reiniciar `diagrama.py` desde el repo principal para que el dashboard sirva la versión nueva (el proceso anterior estaba sirviendo desde el worktree `extract/U2`).
- **2026-05-07 19:55** — Micro-fix de 2 imprecisiones tras dictamen del revisor sobre v10.77 (v10.77b, commit `becaa69`). (1) Timestamps con hora ficticia `14:00` corregidos al momento real del commit `40c8a4c` (19:20 +0200) en 4 sitios: REVIEW.md:9, REVIEW.md:434, PROCESO-MAESTRO.md:660, CHANGELOG.md:24. (2) Árbol vivo de PROCESO-MAESTRO.md:472 ampliado con `REVIEW-bloque-A-cerrado.md` que faltaba en el listado de `docs/historico/`. Sin cambios funcionales. Validador U0/U1/U3 → 0/0. Cierre real de la serie v10.72-v10.77b.
- **2026-05-07 19:20** — Compactación del Bloque A cerrado de REVIEW + 3 cabeceras desincronizadas (v10.77, commit `40c8a4c`). Última pieza de la serie de limpieza documental v10.72-v10.77. Aplicada la receta del revisor con sus 4 ajustes: (1) corte por encabezado `## Bloque A` hasta antes de `## Bloque B` (99 líneas, 8.022 chars) extraído literal a `docs/historico/REVIEW-bloque-A-cerrado.md` (111 líneas con cabecera); (2) sustitución en REVIEW vivo por resumen de 12 líneas con estado A1-A4, resultado vivo y referencias; (3) las 3 cabeceras desincronizadas absorbidas en este mismo commit (REVIEW.md:9, PROCESO-MAESTRO.md:448 y PROCESO-MAESTRO.md:630); (4) `PROCESO-MAESTRO.md:648` reformulado ("Detalle vivo y bitácora en REVIEW" → "Resumen vivo en REVIEW; detalle íntegro en docs/historico; bitácora cronológica general permanece en REVIEW"). REVIEW.md 580 → 493 líneas (-15%, ~2K tokens). Validador U0/U1/U3 → 0/0. Bitácora cronológica general intacta. Cierre de la serie. Ahorro acumulado v10.72-v10.77: ~32K tokens (-37%). Base limpia para extracciones paralelas en otros chats.
- **2026-05-07 13:45** — Cierre de drift vivo en PROCESO-MAESTRO tras dictamen del revisor sobre v10.76 (v10.76b). 3 zonas vivas seguían desactualizadas: (1) Decisión 17 Parte 4 con "17 valores" → 20 valores + mención explícita de los 3 ejes ortogonales tipo/destreza/enfoque; (2) Árbol actual Parte 3 con "U3 única poblada" → estado real con U0/U1/U3 todas validando 0/0, los 5 archivos vivos de fase 1 post-refactor, y `docs/historico/`; (3) Síntesis Parte 6 con "Bloque A pendiente (validar U3, probar U4, bugs B1-B4)" → Bloque A ✅ cerrado con detalle de A1-A4 y referencia a REVIEW. Bitácora del documento intacta (revisionismo prohibido). Validador U0/U1/U3 → 0/0. Próximo: v10.77 condicional con base documental viva limpia.
- **2026-05-07 13:30** — Archivado de árboles históricos y Parte 5.bis de PROCESO-MAESTRO (v10.76). Continuación de la limpieza documental tras v10.75. Tres bloques de PROCESO-MAESTRO.md auto-etiquetados como históricos en su propio contenido se trasladan a `docs/historico/`, dejando punteros cortos donde estaban: (1) Árbol intermedio (487-533, ~2.161 chars); (2) Árbol antes del split (535-668, ~3.960 chars); (3) Parte 5.bis "Histórico de la estrategia de migración (CERRADA)" (788-806, ~1.301 chars). Destinos: `docs/historico/PROCESO-MAESTRO-arboles-historicos.md` (los 2 árboles, 196 líneas) y `docs/historico/PROCESO-MAESTRO-parte5bis-migracion.md` (27 líneas). Árbol actual (vivo, Parte 3 línea 450), Decisiones cerradas (Parte 4), Decisiones pendientes (Parte 5) y Bitácora del documento intactos. PROCESO-MAESTRO 868 → 677 líneas (-22%). Validador U0/U1/U3 → 0/0. Próximo: v10.77 (compactar bloque A cerrado de REVIEW, decisión condicional).
- **2026-05-07 13:15** — Corrección de 2 inexactitudes menores en el acta de v10.75 (v10.75b). El revisor detectó que la verificación post-archivado había quedado registrada como `diagrama._read_version() = 10.74` cuando la real tras el commit es `10.75` (la primera entrada viva pasó a ser v10.75); y que la métrica final decía "977 líneas" cuando el archivo resultante tiene 1.004 (la diferencia es la propia entrada v10.75 + el puntero al histórico). Ambas corregidas en el acta de v10.75 (CHANGELOG líneas 23, 25 y bitácora REVIEW 13:00). El archivado en sí está bien hecho; solo precisión documental. Validador 0/0. Próximo: v10.76.
- **2026-05-07 13:00** — Archivado del CHANGELOG pre-v10.40 (v10.75). Limpieza documental autorizada por el revisor tras v10.74/v10.74b. Trasladadas 1.535 líneas (~112K chars) de la línea 978 al final del CHANGELOG a `docs/historico/CHANGELOG-pre-refactor.md`, sin reescribir. Puntero corto añadido bajo el título del CHANGELOG vivo. Verificaciones: 0 links internos rotos pre-edit; `diagrama._read_version()` devuelve `10.75` post-commit; validador U0/U1/U3 → 0/0. CHANGELOG vivo pasa de 2.512 a 1.004 líneas tras añadir entrada y puntero (-60%, ~28K tokens). Próximo: v10.76 (árboles históricos + Parte 5.bis de PROCESO-MAESTRO).
- **2026-05-07 12:30** — Cierre del pase de coherencia tras dictamen del revisor sobre v10.74 (v10.74b). v10.74 había sido parcial en 2 sitios reales: (1) la enumeración de 20 tipos seguía listando 17 y el shape de actividad seguía sin `enfoque` y con `destreza` como string en líneas 163-180 de PROCESO-MAESTRO; (2) la línea 779 reabría el modelo viejo de "Plantilla HTML del informe por unidad". Fix: enumeración completa de 20 tipos, `destreza` como lista alfabética con enum de 6, `enfoque` añadido con enum de 6, ambos con referencia a schema §5b/§5c y cita de versiones (v10.25/v10.59/v10.60/v10.64); línea 779 reescrita a "Refinamiento visual de la vista HTML dinámica". Validador U0/U1/U3 → 0/0. Pase de coherencia ahora cerrado limpio. Próximo: v10.75 con base documental limpia.
- **2026-05-07 12:00** — **Pase de coherencia documental** (v10.74). Bloqueante para la limpieza/compactación posterior y para la apertura de chats paralelos de extracción. Drift identificado en 7 sitios de PROCESO-MAESTRO (líneas 88, 128, 163, 231, 701) y REVIEW (líneas 45, 112): "validar_inventario.py a escribir" cuando es operativo, "taxonomía cerrada de 17 tipos" cuando son 20, "Plantilla HTML por unidad / tarea pendiente" cuando es vista dinámica del dashboard, A4 marcado como "EN CURSO" cuando cerró en v10.69. Todos corregidos a estado real. Parte 2 de Fase 1 actualizada a estado real, NO reducida a puntero (eso es paso futuro). Hits residuales legítimos confirmados: scripts globales (`regenerar_tarjetas_globales.py`, `regenerar_pildoras_globales.py`) que siguen pendientes y bitácora histórica intocable. Validador U0/U1/U3 → 0/0 sin cambios. Próximo: v10.75 (archivar CHANGELOG pre-v10.40) en worktree `docs/cleanup`. Paralelización de extracciones autorizada tras push de v10.74.
- **2026-05-07 11:30** — Cierre de referencias rotas en `schema-inventario.md` tras v10.72 (v10.73). Hallazgo del revisor: el archivado de v10.72 dejó 2 refs rotas en líneas 7 y 377 del schema apuntando a `REFACTOR-PROPUESTA.md` ya archivado. Decisión: formulación estable y atemporal (no re-apuntar al nuevo path) porque el schema describe contrato vigente del producto, no debería encadenarse a artefactos del proceso de refactor. Fix quirúrgico de 2 líneas. Validador U0/U1/U3 → 0/0. Sin más refs vivas a REFACTOR-*.md fuera de docs/historico. Próximo: push autorizado + re-extracción de U2 en rama nueva.
- **2026-05-07 11:00** — Archivado de documentos del refactor cerrado (v10.72). Los 2 artefactos del proceso (REFACTOR-PROPUESTA.md, REFACTOR-WORKTREE.md) movidos con `git mv` a `docs/historico/refactor-prompt-fase1/`, conservando historial. La carpeta `fases/1-extraccion-inventario/` queda solo con los 5 archivos operativos vivos (CLAUDE.md, prompt.md, schema, reglas, convenciones). Cross-references vivas actualizadas en PROCESO-MAESTRO.md decisión 34 y REVIEW.md sección A4 (líneas 118-150). Bitácora histórica y CHANGELOG anteriores NO se reescriben (mencionan los paths originales en su momento, no es revisionismo). Validador U0/U1/U3 → 0/0 post-archivado. `viejo/` sin tocar (regla del proyecto).
- **2026-05-07 10:30** — Ajuste de redacción en PROCESO-MAESTRO sobre informe HTML (v10.71). Drift detectado: la decisión 25 (línea 705) y la bitácora 2026-05-05 (línea 845) hablaban de "generar además un informe HTML visual" como si la fase 1 produjera un segundo artefacto. Implementación real (verificada en `diagrama.py` y `web/index.html`): el JSON es el único output de la fase; la "vista HTML" es renderización dinámica del dashboard al vuelo. Fix quirúrgico de 2 líneas en PROCESO-MAESTRO. Archivos de fase 1 sin tocar (ya correctos). Sin cambios funcionales.
- **2026-05-07 10:00** — Regla 3 de `CLAUDE.md` de fase reformulada (v10.70) tras observación post-merge del revisor sobre duplicación contractual entre entry points. La regla original prohibía duplicación entre `prompt.md`/schema/reglas/convenciones pero excluía tácitamente al propio `CLAUDE.md`. Auditoría previa: 7 bloques contractuales aceptables (Grupo A) + 0 hallazgos operativos (Grupo B). Fix quirúrgico de 1 línea: regla 3 reescrita según formulación del revisor (entry points pueden repetir hechos y reglas mínimas de contrato; lógica operativa duplicada fuera del archivo canónico sigue siendo bug). Sin tocar prompt.md ni archivos de soporte. Refactor totalmente cerrado.
- **2026-05-07 09:30** — **A4.6 cerrado: merge `refactor/prompt-fase-1` → `main` ejecutado** (commit `110e722`). Receta confirmada con el revisor: `git merge --no-ff` para preservar el rastro completo del refactor. Diff del merge: 14 archivos, +2555/–838 líneas. Archivos creados en `main`: `fases/1-extraccion-inventario/{schema-inventario,reglas-operativas,convenciones-y-casos}.md` + `REFACTOR-WORKTREE.md`. Archivos modificados: `prompt.md`, `CLAUDE.md` de fase, `validar_inventario.py`, los 3 oráculos U0/U1/U3, CHANGELOG, REVIEW, PROCESO-MAESTRO. **Validador en `main` post-merge:** U0 ✅, U1 ✅, U3 ✅, todos 0/0. **Gate A4 entero cerrado** (los 5 sub-gates del bloque "Gate de cierre de A4 entero" ya en ✅). Sin push automático — la decisión de empujar a remoto queda al autor. Branch `refactor/prompt-fase-1` y worktree `../guia-didactica-refactor/` se mantienen intactos por si hace falta inspeccionar el rastro. **Refactor de fase 1 cerrado.**
- **2026-05-07 09:00** — **Actas A4.5 y A4.5.5 cerradas (v10.68 docs).** **A4.5 — Prueba empírica:** los 3 oráculos U0/U1/U3 reclasificados al contrato actualizado (3 ejes ortogonales tipo/destreza/enfoque) en 4 commits iterativos con validación del revisor: v10.64 (U0 piloto, 10 act + ampliación taxonomía 19→20 con `escucha`), v10.65 (U1, 42 act + 3 fixes A1/A2/A3 del revisor + regla nueva de desempate §2.2.5), v10.66 (U3, 47 act + 3 refinamientos §2.2.1-3), v10.67 (cierre de bloqueante sobre `escucha_y_responde`, 3 reclasificaciones). Validador U0/U1/U3 → 0/0. Sin pérdida de decisiones semánticas cerradas. **A4.5.5 — Cross-check schema↔validador:** script de paridad ejecutado sobre las 5 enumeraciones cerradas → **5/5 idénticas, 0 divergencias** (`tipo` 20, `destreza` 6, `enfoque` 6, `tipo_cuadro` 5, `seccion` 7). El gate ineludible queda cumplido. Próximo: A4.6 (merge a main, requiere confirmación del autor).
- **2026-05-07 08:30** — **Cierre del bloqueante del revisor sobre uso de `escucha_y_responde` en 3 oráculos** (v10.67). Tras dictamen del revisor sobre v10.66: la definición de `escucha_y_responde` (respuesta oral, sin texto delante) chocaba con su uso real en U0-p11-act08, U0-p11-act09 (dictados con slots `_____`, deberían ser `completa_huecos` por regla 5) y U3-p39-act06 (alumno escribe antes de escuchar, no es respuesta a estímulo auditivo). 3 reclasificaciones aplicadas: U0-p11-act08/09 → `completa_huecos`, U3-p39-act06 → `produccion_escrita_guiada`. Definición de `escucha_y_responde` se mantiene (nicho legítimo). Cross-check informal del revisor confirma alineación schema↔validador en 20 tipos / 6 destrezas / 6 enfoques. U0/U1/U3 → 0/0. Sin otros hallazgos bloqueantes. Próximo: A4.5 (acta) + A4.5.5 (cross-check formal) + A4.6 (merge).
- **2026-05-07 08:00** — **Cierre de U3 (47 actividades) y refinamiento de desempates en §2.2** (v10.66). Reclasificación completa de U3: destrezas alfabéticas + enfoque + 11 cambios de tipo (10 "Completa..." → `completa_huecos` por regla nueva v10.65; U3-p39-act05 `escucha_y_repite` → `completa_huecos` tras decisión del autor en A1). U3-p41-act05 se mantiene en `produccion_escrita_guiada` por ambigüedad relojes-como-slots. **§2.2 refinada en 3 puntos** según decisiones del autor sobre A3 y A5: regla 1 (ver_video solo sin manipulación posterior), regla 2 (manipulación manda en cualquier punto del enunciado, no solo posterior), regla 3 (responder_preguntas_* con criterio explícito de destreza: texto-fuente → comprensión sin expresion_escrita; sin texto-fuente → expresion_escrita). Branch ahora con U0/U1/U3 todos ✅. Próximo: A4.5 (acta de prueba empírica) + A4.5.5 (cross-check schema↔validador) + merge a main.
- **2026-05-07 07:30** — **U1 reclasificada (42 actividades) + 3 fixes del revisor + regla nueva de desempate** (v10.65). Tras la primera pasada de U1, dictamen del revisor con 3 desajustes contractuales reales: (A1) U1-p12-act3 mal clasificada como `escucha_y_repite` cuando el enunciado encadena "escucha y repite + escucha y escribe número", obliga a `relaciona` por regla "última acción"; sin `expresion_escrita` por regla anti-sobreasignación. (A2) ambigüedad real en frontera `completa_huecos` vs `produccion_escrita_guiada` — el revisor propone regla explícita: huecos/celdas/slots predefinidos → `completa_huecos`; sin huecos, alumno construye → `produccion_escrita_guiada`. (A3) U1-p14-act3 "Forma frases" pertenece a `produccion_escrita_guiada` (ejemplo explícito en §2.2), no a `relaciona`. Fixes aplicados: 7 actividades con tipo corregido + regla nueva §2.2 punto 5 (desempate). Confirmación del autor: A1 = `relaciona`. Validador U1 → 0/0. Estado: U0 ✅, U1 ✅, U3 ❌ (pendiente). Próximo: U3.
- **2026-05-07 07:00** — **U0 reclasificada como piloto + taxonomía `tipo` 19→20** (v10.64). Prueba empírica del nuevo contrato destreza/enfoque sobre U0 (4 páginas, 10 actividades atípicas pre-A1.1). El sistema funciona end-to-end. Decisiones cerradas durante la prueba: (1) **`escucha` añadido a la taxonomía** (caso disparador U0-p8-act01: input puro auditivo sin lectura ni repetición; ningún tipo existente encajaba limpiamente). Decisión registrada en PROCESO-MAESTRO bitácora (regla §2.4). (2) **Regla `expresion_escrita` reformulada** — listas de palabras evocadas SÍ cuentan como `expresion_escrita` (caso U0-p8-act02 "escribe la lista de países que recuerdas"); distinción contenido propio vs transcripción. (3) **Heurística vocab/fonetica documentada** — agrupación por campo léxico → vocabulario, agrupación por dificultad fonética / deletrear / dictado → fonetica (dictado siempre fonetica incluso si es contenido léxico). U0-p8-act01 reclasificada `escucha_y_repite` → `escucha`. Validador U0 → 0/0. Branch sigue rojo en U1/U3 (pendientes de reclasificar). Próximo: U1.
- **2026-05-07 06:30** — Fix de drift post-v10.60 en CLAUDE.md de fase (v10.63). Re-revisión del componente 1 con criterio "contrato vs operativo": las 5 "Reglas críticas" pasan el test (literalidad, no inventar, single source of truth, validar antes de cerrar, no divergencia schema↔validador) — ninguna reescribe casuística migrable, no se tocan. Sí drift menor en la tabla de navegación: la columna "¿Cómo decido X?" listaba solo `tipo` y `tipo_cuadro`; tras v10.60 hay 4 ejes decisionales. Fix quirúrgico de una línea: añadidos `destreza` y `enfoque`. CLAUDE.md de fase 60 líneas (norte 40-60 cumplido). Próximo: componente 4 (reglas-operativas.md).
- **2026-05-07 06:00** — **Cierre del componente 3 (schema-inventario.md)** con 3 fixes accionables (v10.62). **F0 (Bloqueante)**: divergencia real schema↔validador en `_nota_unidad_atipica` — schema §11 la declara opcional contractual, validador no la tenía en `CLAVES_TOP_OPCIONALES`, U0 emitía aviso espurio. Fix: añadida al set; U0 valida sin avisos. **F1 (Medio)**: §13 desactualizada tras v10.60 — no listaba las 2 nuevas enumeraciones cerradas (`destreza` 6, `enfoque` 6) ni la restricción de orden alfabético de destreza. Fix: §13 reescrita con las 6 enumeraciones explícitas y restricciones condicionales completas. **F3 (Bajo)**: ambigüedad de `numero` — schema lo declaraba `<int>` sin obligatoriedad; algunas actividades ("Para aprender", autoevaluación) no tienen número visible. Decisión: opcional. Fix: schema §3 actualizado + nueva §3.1 explicativa; validador añade check de tipo si presente. Próximo: componente 4 — reglas-operativas.md.
- **2026-05-07 05:30** — Fix de drift documental post-v10.60 en `prompt.md` (v10.61). Revisión componente-a-componente: componente 1 (CLAUDE.md de fase) aprobado por el revisor sin findings materiales; componente 2 (prompt.md) con drift detectado — checklist manual y paso 5 no reflejaban `destreza`/`enfoque` obligatorios tras v10.60. Cambios quirúrgicos: paso 5 ampliado con los 3 ejes ortogonales y punteros a schema §5b/§5c; checklist 9 → 11 items con "Destrezas válidas" e "Enfoque válido" insertados. prompt.md 109 → 111 líneas (norte 80-120 cumplido). Próximo: componente 3, schema-inventario.md.
- **2026-05-07 05:00** — **Contrato `destreza`/`enfoque`: separación de ejes habilidad ↔ dominio** (v10.60, **commit intermedio rompedor de contrato**). Tras dos rondas con el revisor sobre cómo cerrar `destreza` (subespecificada en versiones previas), decisión final: separar en dos campos ortogonales. (1) `destreza` reescrita como **eje habilidad MCER puro**: lista de strings, enum cerrado de 6 valores (`comprension_auditiva`, `comprension_lectora`, `expresion_escrita`, `expresion_oral`, `interaccion_oral`, `mediacion`), orden alfabético obligatorio (cierra la deriva de serialización con orden libre que el revisor diagnosticó: 27 strings legacy colapsaban a 17 combos por orden/espacios), sin duplicados, mínimo 1 elemento. (2) **Nuevo campo `enfoque`** como **eje dominio de contenido**: string único, enum cerrado de 6 (`gramatica`, `vocabulario`, `comunicacion`, `fonetica`, `cultura`, `transversal`), obligatorio. El valor `transversal` reemplaza la propuesta inicial `destrezas` (que reutilizaba el nombre de una sección editorial y pegaba el eje al layout de página). (3) **Regla anti-sobreasignación de `expresion_escrita`**: mecánicas de manipulación (completar, relacionar, ordenar, marcar) NO añaden por sí mismas `expresion_escrita`; solo se añade cuando el alumno produce texto lingüístico propio. (4) Decisiones semánticas: `comprension_auditiva` canónico (no alias); `produccion_*` → `expresion_*` (MCER moderno); `gramatica`/`vocabulario` salen del eje destreza y entran en `enfoque`. (5) Validador: `DESTREZAS_VALIDAS` (6) + `ENFOQUES_VALIDOS` (6), validación de presencia/forma/enum/orden/no-duplicados. (6) Referencia colgada `§2b` → corregida a §2.3. **Estado intermedio aceptado:** branch en rojo, validador rechaza U0/U1/U3 (~250 errores: legacy string + ausencia de enfoque). La reclasificación per-unidad de las 97 actividades se hace en otro chat antes de A4.5. Gates en orden: reclasificación per-unidad → A4.5 → A4.5.5 → merge. Próximo: revisión componente-a-componente del refactor (en curso) + reclasificación per-unidad.
- **2026-05-07 04:00** — **Taxonomía de `tipo` rediseñada 17 → 19 por acción imperativa del enunciado** (v10.59), durante la primera pasada de A4.5. La pasada empírica sobre U1 con oráculo destapó 7 divergencias de `tipo` (más análogas en U3): la causa raíz no era mala clasificación sino ambigüedad de la taxonomía — `comprension_lectora`/`comprension_auditiva` mezclaban `tipo` (acción/formato) con `destreza` (habilidad). Decisión: separación de dimensiones. `tipo` = acción específica del enunciado; `destreza` = campo separado (próximo trabajo). Cambios: schema §5 reescrito con 19 valores agrupados en 7 familias; validador `TIPOS_VALIDOS`/`TIPOS_QUE_REQUIEREN_ITEMS` actualizados + 3 claves añadidas a `CONTENIDOS_VISIBLES` (`ejemplos_modelo`, `programas_tv`, `horarios_digitales` — divergencia schema↔validador cerrada como adelanto parcial de A4.5.5); `reglas-operativas.md` §2 reescrita íntegra (§2.1 regla operativa, §2.2 tabla canónica, §2.3 nota tipo vs destreza); 16 actividades reclasificadas (U1: 9; U3: 7; U0: 0). Validación: U0/U1/U3 → 0 errores. Mapeo de reasignaciones: U1-p12-act1 `comprension_lectora`→`lee_y_escucha`; U1-p13-act7 `produccion_escrita_guiada`→`completa_huecos`; U1-p13-act9 `comprension_lectora`→`responder_preguntas_cerradas`; U1-p16-act1 `comprension_auditiva`→`ver_video`; U1-p17-act7 `comprension_auditiva`→`completa_huecos`; U1-p18-act1 `comprension_lectora`→`completa_huecos`; U1-p19-act3 `comprension_auditiva`→`completa_huecos`; U1-p19-act4 `comprension_auditiva`→`seleccion_multiple`; U1-p21-act6 `expresion_escrita_libre`→`responder_preguntas_abiertas`; U3-p35-act06/08 `comprension_lectora`→`lee_y_escucha`; U3-p35-act09 `comprension_lectora`→`responder_preguntas_cerradas`; U3-p40-act01 `comprension_lectora`→`produccion_escrita_guiada`; U3-p40-act02 `comprension_lectora`→`responder_preguntas_cerradas`; U3-p41-act04 `comprension_auditiva`→`relaciona`; U3-p42-act01 `comprension_lectora`→`lee_y_escucha`. Próximo: trabajar la dimensión `destreza` como campo separado.
- **2026-05-07 03:15** — Sincronización de fila-resumen A4.4 con la bitácora (v10.58, hallazgo Bajo del revisor): la tabla de sub-pasos seguía diciendo "✅ 02:30 (57 líneas)" mientras CHANGELOG y bitácora ya reflejaban el cierre limpio en v10.57 con 59 líneas. Fila reescrita a "cerrado limpio 03:00 en v10.57 (59 líneas)". Adicional: el revisor confirma que ejecutó el validador desde la raíz del repo con la convención root-relative ahora explícita y devuelve JSON válido y 0 avisos para U1 — primera verificación funcional externa al ejecutor (informal, no sustituye A4.5). Próximo: A4.5.
- **2026-05-07 03:00** — **Cierre limpio de A4.4 tras dictamen del revisor** (v10.57): hallazgo Medio sobre ambigüedad de comandos. `CLAUDE.md` de fase se auto-carga al trabajar dentro de `fases/1-extraccion-inventario/`, pero los comandos `python3 scripts/validar_inventario.py X` y `python3 diagrama.py` son root-relative — fallan con "No such file or directory" si se ejecutan literalmente desde la carpeta de fase. La convención del repo es root-relative en todos los docs (CLAUDE.md raíz también lo es), pero no estaba declarada explícitamente. Resolución: nota explícita "Convención de comandos: root-relative" añadida al inicio de "Cómo validar" (CLAUDE de fase) y de "Cierre y validación" (prompt.md). Antes de A4.5 (primera prueba funcional oficial) la ambigüedad queda eliminada. CLAUDE 57 → 59, prompt 107 → 109 (ambos siguen dentro de su norte). Próximo: A4.5.
- **2026-05-07 02:30** — **A4.4 cerrado** (v10.56): `CLAUDE.md` de fase reescrito en modo contrato corto según REFACTOR-PROPUESTA §3.1. Estructura final 57 líneas, 7 secciones (Qué produce, Input/output, Cómo se invoca, Cómo validar, Reglas críticas, Para qué consultar qué archivo, Documentos relacionados). Eliminados 4 bloques redundantes del CLAUDE pre-refactor: (1) sección "Reglas operativas críticas (resumen)" de 22 líneas que reescribía contenido ya migrado a `reglas-operativas.md` y `schema-inventario.md` violando single source of truth; (2) "Coste estimado" (no operativo, ya eliminado del prompt en A4.3); (3) "Mejora continua" (vive ahora en `convenciones-y-casos.md` §5); (4) "Contexto futuro CrewAI" (especulación, no contrato operativo). Pre-refactor: 111 líneas, 9 secciones. Post-A4.4: 57 líneas, 7 secciones. Reducción del 49%. Próximo: A4.5 (prueba funcional empírica de reextracción — primera prueba funcional oficial del plan).
- **2026-05-07 02:00** — **A4.3 cerrado** (v10.55): `prompt.md` reescrito desde cero según REFACTOR-PROPUESTA §5 paso 3. Estructura mínima en 9 secciones (Objetivo, Input, Output, Definición de éxito, Regla de oro, Artefactos de soporte, Pasos de la extracción, Cierre y validación + Salida absorbida). Eliminados los 4 placeholders intermedios redundantes (Reglas decisionales, Convenciones de transcripción y ejemplos canónicos, Convenciones específicas, Reglas para cuadros, Casos resueltos y mejora continua) — la cabecera global "Artefactos de soporte" cubre todas las referencias a los archivos hermanos. Sección "Definición de éxito" añadida nueva (no estaba en pre-refactor) con 4 condiciones explícitas alineadas con el plan. "Cierre y validación" absorbe la antigua "Validación post-extracción" + Salida en una sola sección con sub-encabezados. Conteo: 107 líneas (dentro del norte 80-120). Próximo: A4.4 (reescribir CLAUDE.md de fase, hoy 111 líneas, objetivo 40-60).
- **2026-05-07 01:30** — **A4.2c cerrado y A4.2 cerrado al completo** (v10.54). Migrado a `convenciones-y-casos.md` todo el contenido residual del prompt: convenciones de transcripción (sílaba tónica subrayada hasta U3, patrón "primer ítem resuelto como ejemplo", textos de lectura, diálogos con marcadores `[1]`/`[2]`, sopas de letras), ejemplos canónicos de `items_libro` por tipo de actividad (cloze, selección múltiple, cuestionario), ejemplos INCORRECTOS, ejemplo JSON canónico de U0, casebook de U3, política de mejora continua. **Sección "Coste estimado" eliminada** del prompt (no aporta valor operativo). **Aplicada proactivamente la lección de v10.53** (verificar zona reemplazada como enlace limpio): detectadas y corregidas 3 referencias huérfanas en los pasos de la extracción que apuntaban a secciones eliminadas; redirigidas a los archivos externos (`reglas-operativas.md` §1/§3/§4/§7, `schema-inventario.md` §3, `convenciones-y-casos.md` §1.1/§1.2). 8 anclas semánticas verificadas: 7/8 perfectas (presentes en convenciones, ausentes de prompt); la única en prompt ("primer ítem resuelto") es referencia legítima dentro de los pasos. Métricas: prompt 108 (de 547 originales, –80%), schema 308, reglas-operativas 208, convenciones-y-casos 165. **A4.2 cerrado al 100%.** Próximo: A4.3 (reescribir prompt.md core desde cero — el prompt actual ya cumple norte de tamaño 80-120 líneas, A4.3 será revisión y consolidación de la estructura).
- **2026-05-07 00:30** — **Cierre real de A4.2b** (v10.53) tras dictamen del revisor: el v10.52 declaró ✅ prematuramente. Hallazgo bloqueante real: la cabecera transicional de `prompt.md` (líneas 44-52, "Esquema y schema del JSON") seguía describiendo el estado pre-A4.2b ("se migrarán en A4.2b", "Hasta entonces", "vive provisionalmente en este prompt"), mientras el resto del archivo y `reglas-operativas.md` ya describían el estado post-A4.2b. Reabría exactamente la contradicción de source of truth que v10.50/v10.51 cerraron. El criterio del paso 2 del plan (zona reemplazada del prompt = enlace limpio sin semántica residual) no se había aplicado a esa cabecera. Resolución: cabecera reescrita como puente corto y verdadero (3 bullets: schema → schema-inventario.md, reglas decisionales → reglas-operativas.md, convenciones → convenciones-y-casos.md "en construcción"). Verificación reforzada: grep de afirmaciones pre-A4.2b en prompt → 0. Las 3 referencias residuales a "A4.2c" son legítimas (esperan ese sub-paso). Cabecera REVIEW sincronizada (v10.52 había quedado en 22:30 cuando el commit fue a las 23:58). A4.2b queda ahora **cerrado limpio**. Próximo: A4.2c.
- **2026-05-06 22:30** — **A4.2b cerrado** (v10.52). Migrado a `reglas-operativas.md` todo el contenido decisional: precedencias actividad/cuadro/nota/autoevaluación, criterios de `tipo` (con la Distinción crítica `completa_huecos` vs `produccion_escrita_guiada` ahora canónica aquí), criterios de `tipo_cuadro`, "Para aprender" / "Observa", reglas de población de cada campo (`vocabulario_consolidado`, `secciones`, `seccion`, `respuestas`, `audio/imagen/video`, `campo_semantico`, `items_libro`), bloque `autoevaluacion` y unidades atípicas. **Hallazgo importante durante la ejecución:** A4.2a fue más extensiva en pérdidas de lo identificado en v10.51 — además de la "Distinción crítica" se habían perdido también las reglas decisionales de `vocabulario_consolidado` (criterios principal/recurrente/comprension), `respuestas` (formato selección múltiple, V/F), `campo_semantico` (cuándo aplica + nota "liberal por ahora") y `secciones` top-level (regla "actividades_ids en orden", regla "secciones inexistentes vacías"). A4.2b las restaura todas tomando como fuente `cc1f18b` (estado pre-refactor). Verificación de anclas: 7 frases canónicas presentes en `reglas-operativas.md` y ausentes de `prompt.md`. Métricas: prompt 260, schema 308, reglas-operativas 208, convenciones-y-casos 10. Próximo: A4.2c.
- **2026-05-06 21:30** — **Cleanup pre-A4.2b parte 2** (v10.51): el revisor señaló que v10.50 reformuló pero no cerró el hallazgo del source of truth de la taxonomía. Verdad única alineada entre `prompt.md` y `reglas-operativas.md`, pero **falsa**: el prompt afirmaba "el contenido vive aquí" cuando en realidad el bloque decisional había sido absorbido por error de scope en A4.2a (placeholder grande de v10.47). Pérdida real, no solo de redacción. Resolución: bloque "Distinción crítica `completa_huecos` vs `produccion_escrita_guiada`" recuperado de `cc1f18b` y restaurado en `prompt.md` como nueva sección "Reglas decisionales provisionales (a migrar en A4.2b)". Ambos archivos describen ahora con honestidad qué hay y qué no: distinción crítica explícita en prompt; resto de criterios para los 17 tipos = implícitos del dominio editorial + oráculo de facto en U0/U1/U3, a canonizar en A4.2b. El bajo (tabla de secciones) ya estaba bien resuelto en v10.50. Próximo: A4.2b ya con source of truth consistente.
- **2026-05-06 21:00** — **Cleanup pre-A4.2b tras dictamen del revisor** (v10.50). Dos correcciones antes de arrancar A4.2b: (a) eliminada doble verdad sobre source of truth de la taxonomía — el placeholder de `prompt.md` decía "viven en reglas-operativas (se migran en A4.2b)" cuando reglas-operativas decía "viven aún en prompt"; ambos archivos ahora alineados: source of truth provisional = `prompt.md` hasta que A4.2b cierre. (b) Tabla de mapeo de headers de sección en `reglas-operativas.md` corregida contra los inventarios reales: U1-p21 y U3-p43 (páginas con bloque `autoevaluacion` top-level) usan `seccion: evaluacion` en el JSON, no `reflexion`; mi tabla decía "Reflexión / Autoevaluación / cierre → reflexion" lo cual era una regla inventada sin avalar. Tabla reescrita con columna "Avalado en" citando los casos del oráculo, y nota explícita sobre `reflexion`: el valor existe en el enum pero ningún inventario actual lo usa, decisión diferida hasta primer caso real o cierre de A4.2b. Próximo: A4.2b.
- **2026-05-06 20:30** — **Cleanup de A4.2a tras dictamen del revisor** (v10.49). El cierre de A4.2a se había sobredeclarado: 3 fugas decisionales se habían colado en `schema-inventario.md` violando la frontera "split por capa": (1) "se omite en unidades atípicas" (cuándo, no forma); (2) "Las páginas que continúan una sección usan la misma clave normalizada" (cómo determinar, no enumeración); (3) workflow "se consulta al autor" en taxonomía (no contrato de datos puro). Los 3 fragmentos retirados de schema y absorbidos en `reglas-operativas.md` como adelanto parcial de A4.2b. Schema ahora contiene solo formas + enumeraciones + restricciones validables + líneas-puente a reglas-operativas. Verificación: grep del contenido decisional → reglas=1, schema=0 en cada caso. Métrica corregida: schema-inventario.md tiene **308 líneas** (no "300" como dijo v10.47 por aproximación), `prompt.md` 290 (correcto), `reglas-operativas.md` ahora 75 líneas (antes 8). Próximo: A4.2b (continuar la migración de reglas-operativas con el resto del contenido decisional del prompt).
- **2026-05-06 19:45** — Regla de tipología de verificaciones añadida (v10.48): A4.2-A4.4 = checks locales de integridad documental (no pruebas funcionales). A4.5 = primera prueba funcional oficial (reextracción empírica). A4.5.5 = cross-check schema↔validador antes del cierre. Smoke test opcional tras A4.4 permitido pero no es gate formal. Insertado en `REFACTOR-PROPUESTA.md` §5 como nota destacada al inicio del plan; eco breve en este REVIEW tras la tabla de sub-pasos. Próximo: A4.2b.
- **2026-05-06 19:30** — **A4.2a cerrado** (v10.47): contenido estructural migrado del `prompt.md` a `schema-inventario.md`. El nuevo schema-inventario.md (300 líneas, 13 secciones numeradas) contiene: estructura top-level (10+1 claves), schema por página/actividad/cuadro, schema del bloque autoevaluación, taxonomía cerrada de 17 tipos, enumeraciones de `tipo_cuadro` (5) y `seccion` (7), estructura de `vocabulario_consolidado` y demás campos, restricciones condicionales validables (ej. `imagen.descripcion` obligatoria si `presente=true`), y la nota de source-of-truth con `validar_inventario.py`. En `prompt.md` las 9 secciones movidas se reemplazaron por un único placeholder con enlace al schema. Verificación de anclas semánticas: 4 frases canónicas verificadas (`Taxonomía cerrada de tipos de actividad`, `tipo_cuadro describe la categoría pedagógica`, `Mis resultados en esta unidad son`, `MUY BUENOS / BUENOS / NO MUY BUENOS`) — todas presentes en schema, ausentes de prompt. `prompt.md` pasó de 547 a 290 líneas; el resto de migraciones bajará el tamaño hasta el norte ~80-120 líneas tras A4.3. Próximo: A4.2b (migrar a `reglas-operativas.md`).
- **2026-05-06 18:45** — **A4.1 cerrado** (v10.46): tres archivos auxiliares creados en `fases/1-extraccion-inventario/` con headers de identidad solo (sin contenido editorial todavía): `schema-inventario.md` (responsabilidad: contrato de datos puro, contrato paralelo con `validar_inventario.py`), `reglas-operativas.md` (responsabilidad: decisión + clasificación + población + unidades atípicas, single source of truth de precedencias), `convenciones-y-casos.md` (responsabilidad: transcripción + casebook). Cada header incluye qué SÍ contiene, qué NO contiene y referencia al mapeo de la sección 4 de `REFACTOR-PROPUESTA.md` para A4.2. `prompt.md` sigue intacto en 547 líneas — la migración de contenido es A4.2. Próximo: A4.2 (mover contenido fila por fila + verificación de anclas semánticas).
- **2026-05-06 17:00** — Limpieza de dos residuos cosméticos del commit v10.44 (v10.45). (a) Tabla de estado del CHANGELOG decía `e3ed91d` como HEAD del worktree, pero el propio commit v10.44 lo elevó a `a9f710e`; actualizado a `a9f710e` y aclarado que es el SHA "al cerrar v10.44" — el HEAD vivo cambia con cada commit del refactor (referencia a `git worktree list` para el estado actual). (b) `REFACTOR-WORKTREE.md` cerraba con "commit posterior bumpeará la versión a v10.44" cuando ese commit ya había ocurrido; reescrito como referencia retrospectiva al commit `a9f710e`/v10.44.
- **2026-05-06 16:30** — **Migración a worktree dedicado** (v10.44, refinamiento de A4.0). Tras dictamen del revisor con lente Anthropic-first: la rama `refactor/prompt-fase-1` se mueve a un worktree propio en `/Users/armandocruz/Desktop/guia-didactica-refactor/`. El directorio original (`/Users/armandocruz/Desktop/guia-didactica-profesor-IA/`) vuelve a `main`. **Verificación clave:** los untracked `unidades/U2/` y `viejo/_template/` NO existen físicamente en el worktree del refactor — git worktree crea checkout fresco que no copia untracked del checkout originante. Esto elimina ruido durante A4.1-A4.6. Documentado paso a paso en `fases/1-extraccion-inventario/REFACTOR-WORKTREE.md` (incluye comandos de verificación, cierre y aborto). El estado de A4.0 queda como ✅ cerrado con el sub-detalle del worktree. Próximo: A4.1 (crear los 3 archivos auxiliares vacíos: `schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md`).
- **2026-05-06 16:00** — **A4.0 cerrado** (v10.43): tag `pre-refactor-prompt-fase1` creado sobre HEAD del main pre-refactor (`cc1f18b`); rama `refactor/prompt-fase-1` creada y checkout activo. `main` queda intacto en `cc1f18b` durante todo el refactor. Si rollback: `git checkout main` (sin reset destructivo). Próximo: A4.1 (crear los 3 archivos auxiliares vacíos: `schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md`).
- **2026-05-06 15:30** — Limpieza grep tras dictamen del revisor (v10.42, hallazgo bajo no bloqueante): anotación inline *"(renumeradas a 28-34 en v10.41)"* añadida a las dos entradas históricas que seguían siendo grep-ables con el rango viejo "27-33" sin contexto en la misma línea (bitácora del 14:30 + CHANGELOG v10.40 sección 1). El texto histórico se mantiene íntegro (no se reescribe lo que sí hizo v10.40); solo se contextualiza inline. Próximo: A4.0 (tag + rama).
- **2026-05-06 15:00** — Fix de coherencia documental tras dictamen del revisor (v10.41): (a) PROCESO-MAESTRO Parte 4 — eliminada numeración duplicada de "Decisión 27"; el bloque "Arquitectura datos+instrucciones" se ha movido de Parte 5 a Parte 4 (donde corresponde por estar cerrada) preservando su número 27 por antigüedad; las decisiones del refactor de fase 1 (v10.40) se renumeran de 27-33 a 28-34. Eliminado el subheader "Decisiones cerradas adicionales (post-creación inicial)" de Parte 5 (contradecía el título "Decisiones pendientes" de la propia parte). (b) Cabecera "Última actualización" de REVIEW sincronizada con la bitácora.
- **2026-05-06 14:30** — Refactor de fase 1 documentado como plan ejecutable (v10.40). Antes de empezar la ejecución, plan trazado en los dos artefactos canónicos: PROCESO-MAESTRO Parte 4 ampliada con 7 decisiones cerradas (27-33 *— renumeradas a 28-34 en v10.41 por colisión con la "Decisión 27" preexistente; ver entrada del 15:00*: arquitectura, frontera de capas, source of truth, skill fuera, contrato schema↔validador, delegación operativa a REFACTOR-PROPUESTA.md); REVIEW bloque A con paso A4 nuevo y 8 sub-pasos enumerados (A4.0-A4.6 + A4.5.5 cross-check obligatorio). Estado global bloque A actualizado a "🔄 A4 en curso". Cero código tocado: solo documentación del plan ejecutable. Próximo: A4.0 (tag + rama).
- **2026-05-06 14:00** — REFACTOR-PROPUESTA: 2 rastros residuales tras v10.38 (v10.39). (a) Tabla de riesgos seguía hablando de "checklist" cuando el paso 2 ya usa marcador externo — mitigación reescrita en consonancia. (b) Verificación de anclas en paso 2 decía "desaparecer del prompt core" pero el prompt core no existe hasta el paso 3 — reformulado para respetar la secuencia: durante paso 2 se verifica que el ancla esté en destino y NO en la zona reemplazada por placeholder; la comprobación "ancla solo en un sitio" se cierra al terminar el paso 3.
- **2026-05-06 13:30** — REFACTOR-PROPUESTA: 4 correcciones de coherencia interna tras nuevo dictamen del revisor (v10.38). Fix Medio: mapeo de unidades atípicas (línea 246) repartido entre los 3 destinos según capa, en lugar de monolíticamente a `reglas-operativas.md` — coherente con el principio "split por capa" que el propio documento declara. Fix Bajos: (a) subpaso de "checklist" reformulado para no asumir un formato que la tabla no tiene; (b) anclas semánticas sustituidas por frases que sí existen en `prompt.md` actual ("Taxonomía cerrada de tipos de actividad", "tipo_cuadro describe la categoría pedagógica", "primer ítem resuelto como ejemplo"); (c) cifra "9 ejecuciones" corregida a "10 (U0-U9)" en las dos referencias del documento.
- **2026-05-06 13:00** — REFACTOR-PROPUESTA: fix completo de la tabla "Estado medido" (v10.37). El fix de v10.36 había sido parcial: solo corrigió la fila de `prompt.md` pero dejó la fila de `CLAUDE.md` fase con datos viejos (`7|11` cuando el real es `9|10`). Ahora íntegramente reproducible. Verificación cruzada del resto de cifras del documento (17 tipos, 5 tipo_cuadro, 7 secciones, 3 opciones, líneas de los dos archivos) — todas correctas. Lección registrada: cuando una tabla es "evidencia dura", verificar todas sus filas, no solo la que motiva la revisión.
- **2026-05-06 12:30** — REFACTOR-PROPUESTA: dos correcciones tras dictamen del revisor (v10.36). Conteo "34 secciones" sustituido por dato real (27 `##` / 37 totales) con nota de reproducibilidad. Sección 8 (scope) reescrita para eliminar la contradicción entre "no se toca el validador" y "alinear validador antes del merge": ahora dice explícitamente que la alineación es prerequisito ineludible del merge, en commit aparte, fuera del scope nominal pero no opcional. Documenta que los defectos estaban en el commit `d15a0dd` antes de detectarse.
- **2026-05-06 12:00** — Sincronización del plan con el trabajo real + propuesta de refactor de fase 1 (v10.35): insertado **B1.5** (diseño de `nc1-reciclaje.json` con gate propio, resuelve la doble verdad entre nota del bloque B y B2); insertado **B5** (despliegue público del dashboard como ✅ cerrado, marcado explícitamente como carril paralelo fuera del orden B1-B4); tabla de Contenido editorial reestructurada con estado real verificado contra filesystem (U0/U1/U3 trackeados y validan; **U2 solo working tree, no trackeado, no valida**: 2 errores de `autoevaluacion.emoticonos` ausente; U4-U9 carpetas vacías); cabecera "Última actualización" corregida; conteo de líneas obsoleto de `CLAUDE.md` eliminado; "A3 (verificar bug B3)" como próxima modificación de `diagrama.py` retirada (A3/B3 ya cerrados). Adicional: creado `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md` tras 4 rondas de revisión (propuesta aprobable, sin ejecutar todavía — ver CHANGELOG v10.35).
- **2026-05-06 11:00** — Build slim para Railway (v10.34): quitadas `crewai`, `langfuse`, `deepeval` de requirements.txt y `node`+`promptfoo` del Dockerfile. Solo queda lo que el dashboard necesita en runtime. **Documentado retroactivamente en B5 como cerrado**; el dashboard sirve v10.34 en `https://entornoeditorial.up.railway.app`.
- **2026-05-06 09:30** — Tildes/eñes corregidas en los 3 diagramas Mermaid del dashboard (v10.33). Niveles 1, 2 y 3. ERD y rutas de filesystem sin tocar. Entrada CHANGELOG retroactiva: el commit `5024914` se pusheó antes de bumpear versión, lo que viola la regla "cada commit bumpea versión" — esta entrada lo regulariza.
- **2026-05-06 00:30** — Correcciones tras 2.º dictamen del revisor (v10.32): validador endurecido — añadidas validaciones de presencia de `emoticonos`, tipos de sub-campos (int/str/bool/list-of-str), y valores fijos NC1 (instrucción literal, opciones canónicas, emoticonos=true) cuando `curso == "nc1"`. PROCESO-MAESTRO encabezado: "10 claves" → "10 claves obligatorias + 1 opcional". CHANGELOG v10.32 nota del validador actualizada.
- **2026-05-06 00:15** — Correcciones tras dictamen del revisor (v10.31/v10.32): U0 cuadro "Saludos" reclasificado de `lexical` a `cultural` (según definición del prompt: fórmulas sociales = cultural). CHANGELOG v10.31 desglose corregido (eran 10 cuadros = 4+1+1+2+2, antes sumaba 11). Limpiadas 2 referencias antiguas restantes: prompt.md paso 4 ("Reglas para cuadros gramaticales" → "Reglas para cuadros") y comentario en web/index.html ("Renderizar cuadros gramaticales" → con los 5 tipos).
- **2026-05-05 23:45** — Bloque de autoevaluación como campo top-level (v10.32): U1 migrado del `_nota` al top-level `autoevaluacion`, U3 capturado por primera vez (p43), U0 sin cambios (atípica). Validador, prompt, CLAUDE.md fase 1, ERD, dashboard y PROCESO-MAESTRO sincronizados.
- **2026-05-05 23:30** — Schema cuadros migrado (v10.31): `cuadros_gramaticales` → `cuadros` + `tipo_cuadro` en U0, U1, U3. Validador actualizado. Prompt, CLAUDE.md fase 1, diagrama.py, web/index.html y PROCESO-MAESTRO sincronizados. Validación: U0 1 aviso intencional, U1/U3 limpios.
- **2026-05-05 23:00** — Terminología ELE aplicada (v10.25): 3 tipos renombrados en los 3 JSONs + validador + prompt + CLAUDE.md de fase 1. CHANGELOG v10.25 añadido.
- **2026-05-05 22:00** — A1 validado por el autor (47 actividades de U3 correctas). A3 cerrado: B1 pospuesto (CrewAI bloqueado), B2 aceptado (en viejo sin trackear), B3 resuelto en v10.15, B4 no requiere acción (cosmético, se resuelve con nuevo schema). Bloque B parcializado: tarjetas necesita fase 2 primero, píldoras en su momento, reciclaje próximo a discutir. Próximo paso: diseñar `nc1-reciclaje.json` y su visualización en dashboard.
- **2026-05-05 21:30** — Rebajada afirmación "arquitectura limpia" en CHANGELOG v10.17 (revisor): se limpió solo el diagrama, no el código (referencias legacy a `viejo/repertorios/` siguen en `diagrama.py:550-557` para el flujo de agentes bloqueado).
- **2026-05-05 21:00** — Dashboard saneado: sidebar con INVENTARIOS/PROYECTO/AGENTES en mayúsculas (AGENTES bloqueado), arquitectura mermaid sin caja `viejo/`, zoom +/- en diagramas, eliminadas 3 referencias residuales a `padStart(2,'0')`. Cero referencias hardcoded a U01-U09 en la UI.
- **2026-05-05 20:00** — A2 cerrado (U0 extraído como prueba). Prompt de fase 1 ampliado con 3 secciones nuevas (unidades atípicas, sílaba tónica subrayada hasta U3, patrón "primer ítem resuelto como ejemplo"). Convención de naming extendida a U0 en docs.
- **2026-05-05 18:30** — CLAUDE.md raíz reducido a 85 líneas (Anthropic best practices). Movida historia/estado/planes a PROCESO-MAESTRO/README/REVIEW según corresponda.
- **2026-05-05 18:00** — Confirmada arquitectura datos centralizados + instrucciones modulares. Añadido al inicio del documento como principio arquitectónico no negociable. Sin cambios estructurales en los pasos.
- **2026-05-05 17:00** — Reescrito con gates explícitos. Cada paso ahora declara: archivos involucrados + actualizaciones meta requeridas + gate de cierre con condiciones numeradas + validación del revisor + dependencias hacia adelante. Añadidas reglas globales del proceso (qué meta-archivo se actualiza cuándo) y sección "cómo el revisor analiza este documento".
- **2026-05-05 16:30** — Creación inicial.
