# REVIEW — Plan de trabajo paso a paso (con gates de validación)

> **Qué es este documento:** plan operativo de las tareas pendientes. Cada paso tiene: objetivo, archivos involucrados, **condiciones de cierre (gate)**, y validación del revisor. **No se pasa al siguiente paso hasta que TODAS las condiciones se cumplen.** El revisor lee este documento en cada iteración y certifica el cumplimiento de cada gate.
>
> **Audiencia:** revisor (validar gates) + ejecutor (Claude Code) + autor (decidir).
>
> **Relación con `PROCESO-MAESTRO.md`:** maestro = decisiones cerradas + bitácora; REVIEW = plan ejecutable con gates pendientes.
>
> **Última actualización:** 2026-05-06 15:00

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
| Fase 1 — Extracción de inventario | ✅ Operativa con U0, U1 y U3 trackeados y validando (A1 ✅, A2 ✅ con reserva, A3 ✅ cerrado) · 🔄 **A4 refactor documental en curso** (5 archivos objetivo). U2 en working tree, no validado |
| Infraestructura (dashboard, validador) | ✅ Activa local + ✅ desplegada en producción (Railway, B5 cerrado) |
| Documentación raíz (CLAUDE.md, README, PROCESO-MAESTRO, REVIEW) | ✅ Actualizada |
| Bloque B (cerrar infraestructura fase 1) | 🔄 Parcial — B1.5 (reciclaje) en diseño · B1+B2 esperan dependencias · B5 (despliegue público) ✅ cerrado fuera de orden · tarjetas dependen de fase 2 · píldoras dependen de fase 5 |
| Bloque C (fases 2-8) | 📋 Pendiente |
| Bloque D (lecciones Claude Code) | 📋 Pendiente |
| Bloque E (limpieza final) | 📋 Pendiente |

---

## Bloque A — Estabilizar la fase 1

### A1. Validar U3 con el autor revisando actividad por actividad — ✅ CERRADO 2026-05-05

**Gate de cierre (cumplido el 2026-05-05 22:00):**
1. ✅ Autor revisó las 47 actividades de U3 y declaró: "son correctas".
2. ✅ Sin errores detectados — no hubo correcciones al JSON.
3. ✅ Prompt contiene sección "Casos resueltos en U3" (v10.13).
4. ✅ `python3 scripts/validar_inventario.py 3` → JSON válido, 0 avisos.
5. ✅ Bitácora actualizada.
6. ✅ Commits v10.21 + v10.22 documentan el estado.

---

### A2. Probar el sistema con una unidad nueva — ✅ CERRADO CON RESERVA 2026-05-05 con U0

**Reserva pendiente:** ítem 4 del gate (reproducibilidad por segunda extracción) está diferida, no verificada. El cierre se considera operativo bajo la asunción de que la varianza del LLM con prompt detallado es aceptable. Si en el futuro se observa varianza problemática, A2 se reabre.

**Objetivo:** validar que el prompt funciona en escala (no solo con U3).

**Pre-condición original:** A1 cerrado + autor entrega un PDF nuevo.
**Pre-condición real ejecutada:** autor entregó PDF de U0 antes de cerrar A1; **decisión explícita de paralelismo** — A2 se ejecutó sin esperar a A1.

**Archivos a crear:**
- `unidades/UX/fuente/UX-nc1.pdf` — lo aporta el autor (gitignored).
- `unidades/UX/UX-nc1-inventario.json` — Claude Code lo genera siguiendo el prompt.

**Archivos a modificar:**
- `fases/1-extraccion-inventario/prompt.md` — si aparecen casos nuevos no contemplados en U3.

**Actualizaciones meta requeridas:**
- `REVIEW.md` — bitácora.
- `PROCESO-MAESTRO.md` — bitácora.
- `CHANGELOG.md` — entrada con commit.
- `CLAUDE.md` — solo si una nueva regla de oro emerge.

**Gate de cierre (cumplido con U0 el 2026-05-05):**
1. ✅ Inventario U0 generado y validado con `python3 scripts/validar_inventario.py 0` (1 aviso intencional sobre `_nota_unidad_atipica`).
2. ✅ Autor revisó visualmente U0 en el dashboard y declaró conformidad.
3. ✅ Surgieron 4 casos nuevos: prompt actualizado en `fases/1-extraccion-inventario/prompt.md` (commit `3a169ca`) con secciones "unidades atípicas", "sílaba tónica subrayada hasta U3", "primer ítem resuelto como ejemplo".
4. ⚠ Reproducibilidad: pendiente verificar con segunda extracción de la misma unidad. Diferida (no bloqueante; la varianza del LLM se considera aceptable a priori).
5. ✅ Commits `4de266f` (v10.12) y `3a169ca` (v10.13). CHANGELOG actualizado en `5a5d6e7` para v10.11 y posteriores en commits sucesivos.

**Bloquea a:** ya nada operativo. B1 y siguientes desbloqueados.

---

### A3. Resolver bugs conocidos B1, B2, B3, B4 — ✅ CERRADO 2026-05-05

**Gate cumplido:**
1. ✅ **B1** (`viejo/scripts/crewai/tools.py:346` path muerto a `datos/tarjetas/`): **Pospuesto indefinidamente.** El flujo CrewAI está bloqueado (AGENTES = BLOQUEADO en sidebar). Bug inerte hasta que se reactive.
2. ✅ **B2** (`viejo/repertorios/` no rastreable en Railway): **Aceptado.** Está en `viejo/` donde toca. Se queda sin trackear. El flujo de agentes está bloqueado y no lo usa activamente.
3. ✅ **B3** (`diagrama.py` ref hardcoded a `U03`): **Resuelto en v10.15.** Verificado: apunta a `unidades/U3/U3-nc1-inventario.json`.
4. ✅ **B4** (`_normSeccion` no fusiona pestañas "(cont.)"): **No requiere acción.** El bug era cosmético y aplica solo al JSON viejo. El nuevo schema usa claves normalizadas (vocabulario, gramatica...) — el problema desaparece automáticamente al migrar.

---

### A4. Refactor documental de fase 1 — 🔄 EN CURSO (decidido 2026-05-06)

**Objetivo:** separar `fases/1-extraccion-inventario/prompt.md` (hoy 547 líneas mezclando schema + reglas + casos + mantenimiento) en **5 archivos por responsabilidad** (CLAUDE.md fase, prompt.md core, schema-inventario.md, reglas-operativas.md, convenciones-y-casos.md). NO reabre decisiones editoriales. NO modifica los inventarios U0/U1/U3.

**Pre-condición:** ninguna (la propuesta está cerrada en v10.39).

**Source of truth operativa:** `fases/1-extraccion-inventario/REFACTOR-PROPUESTA.md`. Este paso A4 NO duplica el plan; lo invoca y lleva el progreso por sub-paso.

**Sub-pasos** (según REFACTOR-PROPUESTA.md sección 5):

| Sub-paso | Descripción breve | Estado |
|---|---|---|
| **A4.0** | Tag `pre-refactor-prompt-fase1` + rama `refactor/prompt-fase-1` | 📋 |
| **A4.1** | Crear los 3 archivos auxiliares vacíos con headers | 📋 |
| **A4.2** | Migrar contenido fila por fila aplicando split por capa + verificación de anclas | 📋 |
| **A4.3** | Reescribir `prompt.md` core desde cero (incluye sección "Cierre y validación") | 📋 |
| **A4.4** | Reescribir `CLAUDE.md` de fase en modo contrato corto | 📋 |
| **A4.5** | Prueba empírica de reextracción (3 casos: página rica + U0 completa + U1-p21) | 📋 |
| **A4.5.5** | **Cross-check obligatorio** schema-inventario.md ↔ validar_inventario.py — gate ineludible antes del merge | 📋 |
| **A4.6** | Sincronizar CHANGELOG/REVIEW/PROCESO-MAESTRO + merge a `main` | 📋 |

**Marcador externo de progreso:** cada commit del refactor cita su sub-paso en el mensaje (ej. `A4.2: schema-inventario migrado`). El estado de cada fila de la tabla anterior se actualiza al cerrar el sub-paso correspondiente.

**Gate de cierre de A4 entero:**
1. ✅ Sub-pasos A4.0 → A4.6 cerrados según los gates detallados en REFACTOR-PROPUESTA.md.
2. ✅ Acta del paso A4.5.5 con **0 divergencias** schema↔validador (puede implicar commit aparte de alineación del validador antes del merge — prerequisito ineludible, no opcional).
3. ✅ Prueba empírica del paso A4.5: los 3 casos validan con 0 errores y 0 avisos en estado pre-merge, sin pérdida de decisiones semánticas cerradas.
4. ✅ Merge `refactor/prompt-fase-1` → `main` ejecutado.
5. ✅ Bitácoras de REVIEW + CHANGELOG + PROCESO-MAESTRO actualizadas con el cierre.

**Bloquea a:** ninguna fase activa. El refactor mejora mantenibilidad de fase 1 sin alterar su funcionamiento.

**Riesgos y mitigaciones:** ver REFACTOR-PROPUESTA.md sección 6.

---

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

### B1.5. Diseño de `nc1-reciclaje.json` — definir contrato antes de generar

**Objetivo:** cerrar formalmente cómo se construye `nc1-reciclaje.json`. La nota del bloque B (líneas iniciales) declara que el autor quiere "definir antes de implementar"; este paso lo materializa con gate propio.

**Pre-condición:** ninguna (decisión del autor). En paralelo con B1; no depende de B1.

**Preguntas que cierra el paso:**
- ¿Qué dispara una entrada de reciclaje (qué actividad de qué unidad recicla qué de qué unidad anterior)?
- ¿Formato de cada entrada individual? (campos mínimos, IDs de actividad origen/destino, tipo de reciclaje, contenido).
- ¿Política de mantenimiento: manual por Claude Code en chat, automático por script, o mixto?
- ¿Confirmar o ajustar el esqueleto top-level que B2 hoy presupone (`curso`, `actualizado`, `reciclajes_por_unidad: {}`, `indice_por_tipo: {...}`)?

**Archivos a modificar:**
- `PROCESO-MAESTRO.md` — Parte 4: registrar la decisión (esquema cerrado de nc1-reciclaje).

**Actualizaciones meta requeridas:**
- `PROCESO-MAESTRO.md` — entrada en Parte 4.
- `REVIEW.md` — gate marcado, B2 actualizado para depender de B1.5.
- `CHANGELOG.md` — entrada del cierre de decisión.

**Gate de cierre:**
1. ✅ Decisión sobre disparadores, formato per-entrada, política de mantenimiento y esqueleto top-level cerrada con el autor.
2. ✅ Decisión registrada en PROCESO-MAESTRO.md Parte 4.
3. ✅ Si el esqueleto resulta distinto del que asume hoy B2, B2 se ajusta antes de ejecutarse.
4. ✅ Commit + CHANGELOG.

**Bloquea a:** B2 (parte reciclaje).

---

### B2. Generar los 3 JSONs globales con datos de U3

**Objetivo:** tener archivos `nc1-tarjetas.json`, `nc1-pildoras.json`, `nc1-reciclaje.json` en `unidades/`.

**Pre-condición:** B1 cerrado (para tarjetas+píldoras) + **B1.5 cerrado** (para reciclaje). B3 (migración de contenido) decidido.

**Archivos a crear:**
- `unidades/nc1-tarjetas.json` — generado por script.
- `unidades/nc1-pildoras.json` — generado por script.
- `unidades/nc1-reciclaje.json` — escrito a mano por Claude Code en chat con autor (vacío hasta que haya 2+ unidades).

**Actualizaciones meta requeridas:**
- `PROCESO-MAESTRO.md` — bitácora.
- `REVIEW.md` — gate.
- `CHANGELOG.md` — commit.

**Gate de cierre:**
1. ✅ Los 3 archivos existen en `unidades/`.
2. ✅ Cada uno tiene estructura conforme al esquema (validable visualmente).
3. ✅ `nc1-reciclaje.json` tiene al menos el esqueleto top-level (`curso`, `actualizado`, `reciclajes_por_unidad: {}`, `indice_por_tipo: {...}`).
4. ✅ Commit + CHANGELOG.

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
- `diagrama.py` — endpoints `/api/global/<tipo>` (tarjetas/pildoras/reciclaje).
- `web/index.html` — sección o pestañas en "Inventarios" para los globales.

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
| `unidades/U2/U2-nc1-inventario.json` | ⚠ **Solo working tree, no trackeado** · falla validación con 2 errores (`autoevaluacion.emoticonos` ausente). No usable hoy | Decisión pendiente: completar autoevaluación + trackear, o descartar |
| `unidades/U3/U3-nc1-inventario.json` | ✅ Validado · trackeado | B3 (decidir si migrar más contenido) |
| `unidades/U3/fuente/U3-nc1.pdf` | ✅ En su sitio (gitignored) | — |
| `unidades/U3/tarjetas/`, `pildoras/`, MDs | 📋 No migrados | B3 |
| `unidades/U4/`...`U9/` | 📋 Carpetas vacías, sin inventario | Nuevas extracciones cuando lleguen PDFs |
| `unidades/nc1-tarjetas.json` | 📋 No existe | B2 |
| `unidades/nc1-pildoras.json` | 📋 No existe | B2 |
| `unidades/nc1-reciclaje.json` | 📋 No existe | Diseño en B1.5, generación en B2 |

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

- **2026-05-06 15:00** — Fix de coherencia documental tras dictamen del revisor (v10.41): (a) PROCESO-MAESTRO Parte 4 — eliminada numeración duplicada de "Decisión 27"; el bloque "Arquitectura datos+instrucciones" se ha movido de Parte 5 a Parte 4 (donde corresponde por estar cerrada) preservando su número 27 por antigüedad; las decisiones del refactor de fase 1 (v10.40) se renumeran de 27-33 a 28-34. Eliminado el subheader "Decisiones cerradas adicionales (post-creación inicial)" de Parte 5 (contradecía el título "Decisiones pendientes" de la propia parte). (b) Cabecera "Última actualización" de REVIEW sincronizada con la bitácora.
- **2026-05-06 14:30** — Refactor de fase 1 documentado como plan ejecutable (v10.40). Antes de empezar la ejecución, plan trazado en los dos artefactos canónicos: PROCESO-MAESTRO Parte 4 ampliada con 7 decisiones cerradas (27-33: arquitectura, frontera de capas, source of truth, skill fuera, contrato schema↔validador, delegación operativa a REFACTOR-PROPUESTA.md); REVIEW bloque A con paso A4 nuevo y 8 sub-pasos enumerados (A4.0-A4.6 + A4.5.5 cross-check obligatorio). Estado global bloque A actualizado a "🔄 A4 en curso". Cero código tocado: solo documentación del plan ejecutable. Próximo: A4.0 (tag + rama).
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
