# REVIEW — Plan de trabajo paso a paso (con gates de validación)

> **Qué es este documento:** plan operativo de las tareas pendientes. Cada paso tiene: objetivo, archivos involucrados, **condiciones de cierre (gate)**, y validación del revisor. **No se pasa al siguiente paso hasta que TODAS las condiciones se cumplen.** El revisor lee este documento en cada iteración y certifica el cumplimiento de cada gate.
>
> **Audiencia:** revisor (validar gates) + ejecutor (Claude Code) + autor (decidir).
>
> **Relación con `PROCESO-MAESTRO.md`:** maestro = decisiones cerradas + bitácora; REVIEW = plan ejecutable con gates pendientes.
>
> **Última actualización:** 2026-05-07 03:15

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
| **A4.0** | Tag `pre-refactor-prompt-fase1` + rama `refactor/prompt-fase-1` (+ worktree dedicado, ver REFACTOR-WORKTREE.md) | ✅ 2026-05-06 16:30 (tag y rama → `cc1f18b`; worktree en `../guia-didactica-refactor/`) |
| **A4.1** | Crear los 3 archivos auxiliares vacíos con headers | ✅ 2026-05-06 18:45 (`schema-inventario.md` 8 líneas, `reglas-operativas.md` 8, `convenciones-y-casos.md` 10) |
| **A4.2** | Migrar contenido fila por fila aplicando split por capa + verificación de anclas | ✅ (a) schema · (b) reglas-operativas · (c) convenciones-y-casos. prompt.md: 547 → 108 líneas (–80%). 4 archivos en su sitio sin contenido editorial residual |
| **A4.3** | Reescribir `prompt.md` core desde cero (incluye sección "Cierre y validación") | ✅ 2026-05-07 02:00 (107 líneas, 9 secciones; cero placeholders intermedios; "Cierre y validación" absorbida; norte 80-120 cumplido) |
| **A4.4** | Reescribir `CLAUDE.md` de fase en modo contrato corto | ✅ cerrado limpio 2026-05-07 03:00 en v10.57 (59 líneas tras añadir convención root-relative explícita; 7 secciones; norte 40-60 cumplido; cero duplicaciones literales con prompt.md) |
| **A4.5** | Prueba empírica de reextracción y reclasificación contractual de los 3 oráculos (U0, U1, U3) | ✅ 2026-05-07 (v10.64–v10.67): U0 piloto (10 act); U1 (42 act, 3 fixes A1/A2/A3 del revisor); U3 (47 act, 11 cambios de tipo); +1 fix bloqueante v10.67. Validador U0/U1/U3 → 0/0 |
| **A4.5.5** | **Cross-check obligatorio** schema-inventario.md ↔ validar_inventario.py — gate ineludible antes del merge | ✅ 2026-05-07: 5/5 enumeraciones idénticas (tipo 20, destreza 6, enfoque 6, tipo_cuadro 5, seccion 7), 0 divergencias |
| **A4.6** | Sincronizar CHANGELOG/REVIEW/PROCESO-MAESTRO + merge a `main` | 📋 pendiente confirmación del autor |

**Marcador externo de progreso:** cada commit del refactor cita su sub-paso en el mensaje (ej. `A4.2: schema-inventario migrado`). El estado de cada fila de la tabla anterior se actualiza al cerrar el sub-paso correspondiente.

**Tipología de verificaciones por sub-paso** (regla operativa, ver detalle en `REFACTOR-PROPUESTA.md` §5):
- **A4.2 → A4.4:** solo checks locales de integridad documental (anclas semánticas, mapeo como checklist externo, no-duplicación entre archivos). NO pruebas funcionales.
- **A4.5:** primera prueba funcional oficial (reextracción empírica de los 3 casos).
- **A4.5.5:** cross-check schema ↔ validador antes del merge (gate obligatorio).
- **Smoke test opcional tras A4.4:** permitido en chat para detectar roturas obvias antes de A4.5. NO es gate formal ni sustituye la prueba funcional de A4.5.

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
