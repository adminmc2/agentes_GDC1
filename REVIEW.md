# REVIEW — Plan de trabajo paso a paso (con gates de validación)

> **Qué es este documento:** plan operativo de las tareas pendientes. Cada paso tiene: objetivo, archivos involucrados, **condiciones de cierre (gate)**, y validación del revisor. **No se pasa al siguiente paso hasta que TODAS las condiciones se cumplen.** El revisor lee este documento en cada iteración y certifica el cumplimiento de cada gate.
>
> **Audiencia:** revisor (validar gates) + ejecutor (Claude Code) + autor (decidir).
>
> **Relación con `PROCESO-MAESTRO.md`:** maestro = decisiones cerradas + bitácora; REVIEW = plan ejecutable con gates pendientes.
>
> **Última actualización:** 2026-05-05 18:30

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
| Fase 1 — Extracción de inventario | ✅ Operativa con U3 y U0 (gates A1, A3 pendientes; A2 ✅ cerrado con U0) |
| Infraestructura (dashboard, validador) | ✅ Activa |
| Documentación raíz (CLAUDE.md, README, PROCESO-MAESTRO, REVIEW) | ✅ Actualizada |
| Bloque B (cerrar infraestructura fase 1) | 📋 Pendiente |
| Bloque C (fases 2-8) | 📋 Pendiente |
| Bloque D (lecciones Claude Code) | 📋 Pendiente |
| Bloque E (limpieza final) | 📋 Pendiente |

---

## Bloque A — Estabilizar la fase 1

### A1. Validar U3 con el autor revisando actividad por actividad

**Objetivo:** que el JSON U3 quede sin errores y que el prompt incorpore TODAS las reglas/casos detectados.

**Archivos a modificar (trabajo principal):**
- `unidades/U3/U3-nc1-inventario.json` — corregir errores detectados.
- `fases/1-extraccion-inventario/prompt.md` — añadir cada caso/regla aprendido.

**Actualizaciones meta requeridas:**
- `REVIEW.md` — bitácora con cada error corregido.
- `PROCESO-MAESTRO.md` — bitácora de la sesión de revisión.
- `CHANGELOG.md` — al hacer commit, entrada que liste los cambios.
- `CLAUDE.md` — solo si el caso revela una NUEVA regla de oro global.

**Gate de cierre (TODAS deben cumplirse):**
1. ✅ Autor ha revisado las 47 actividades de U3 y declara: "no encuentro más errores".
2. ✅ Cada error encontrado tiene su corrección en el JSON.
3. ✅ Cada error encontrado tiene su regla añadida al prompt.
4. ✅ `python3 scripts/validar_inventario.py 3` → ✅ JSON válido, 0 avisos.
5. ✅ Bitácora del REVIEW actualizada con el resumen de la sesión.
6. ✅ Commit hecho con CHANGELOG actualizado.

**Validación del revisor:**
- Verificar que el prompt contiene una sección "Casos resueltos en U3" actualizada.
- Verificar que el JSON pasa el validador.
- Verificar que CHANGELOG tiene la entrada correspondiente.

**Bloquea a:** ~~A2~~ — A2 ya cerrado en paralelo con U0 cuando llegó el PDF antes que A1 estuviera completo (decisión explícita de paralelismo del autor el 2026-05-05). A1 sigue pendiente como tarea independiente.

---

### A2. Probar el sistema con una unidad nueva — ✅ CERRADO 2026-05-05 con U0

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

### A3. Resolver bugs conocidos B1, B2, B3, B4

**Objetivo:** dejar la infraestructura limpia antes de seguir construyendo.

**Pre-condición:** ninguna (puede hacerse en paralelo con A1).

**Archivos a verificar/modificar:**
- `diagrama.py` línea ~715 (B3) — verificar que ya apunta a `unidades/U3/U3-nc1-inventario.json` tras la disolución de `nuevo/`.
- `viejo/scripts/crewai/tools.py` línea ~346 (B1) — decisión: arreglar / postergar / eliminar al borrar viejo.
- `viejo/repertorios/` (B2) — decisión: trackear / desactivar lectura en producción / mover.
- `web/index.html` — `_normSeccion` (B4) — solo aplica a JSON viejo; en JSON nuevo las claves ya están normalizadas. **Posiblemente ya resuelto.**

**Actualizaciones meta requeridas:**
- `PROCESO-MAESTRO.md` — actualizar Parte 5 marcando bugs resueltos o cerrados con decisión.
- `REVIEW.md` — marcar como ✅.
- `CHANGELOG.md` — solo si hay cambio de código.

**Gate de cierre:**
1. ✅ B1: decisión documentada en PROCESO-MAESTRO (arreglar / postergar / eliminar).
2. ✅ B2: decisión documentada.
3. ✅ B3: verificado en código (línea actualizada o constada como ya correcta).
4. ✅ B4: verificado (resuelto al cambiar al schema normalizado).
5. ✅ Si se hizo cambio de código: commit + CHANGELOG.

---

## Bloque B — Cerrar la infraestructura de fase 1

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

**Bloquea a:** B2.

---

### B2. Generar los 3 JSONs globales con datos de U3

**Objetivo:** tener archivos `nc1-tarjetas.json`, `nc1-pildoras.json`, `nc1-reciclaje.json` en `unidades/`.

**Pre-condición:** B1 cerrado. B3 (migración de contenido) decidido.

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
| `CLAUDE.md` | ✅ Creado (196 líneas) | Cada cierre de fase, cada cambio en estructura/comandos/reglas |
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
| `diagrama.py` | ✅ Activo (zona simplificada) | B4 (vista globales), A3 (verificar bug B3) |
| `web/index.html` | ✅ Vista Inventarios funcional | B4, mejoras estéticas |
| `eval/` | ⚠ Heredado | Bloque C cuando aplique |
| `fases/1-extraccion-inventario/prompt.md` | ✅ Operativo | A1 (con cada error nuevo en U3), A2 (con casos nuevos en otras unidades) |
| `scripts/validar_inventario.py` | ✅ Operativo | Cuando se añada un caso de validación |
| `scripts/regenerar_tarjetas_globales.py` | 📋 No existe | B1 |
| `scripts/regenerar_pildoras_globales.py` | 📋 No existe | B1 |

### Contenido editorial (raíz)
| Carpeta/Archivo | Estado | Próxima modificación |
|---|---|---|
| `unidades/U3/U3-nc1-inventario.json` | ✅ Validado | A1 (correcciones), B3 (decidir si migrar más contenido) |
| `unidades/U3/fuente/U3-nc1.pdf` | ✅ En su sitio (gitignored) | — |
| `unidades/U3/tarjetas/`, `pildoras/`, MDs | 📋 No migrados | B3 |
| `unidades/U1/`...`U9/` | 📋 No existen | A2 cuando lleguen PDFs |
| `unidades/nc1-tarjetas.json` | 📋 No existe | B2 |
| `unidades/nc1-pildoras.json` | 📋 No existe | B2 |
| `unidades/nc1-reciclaje.json` | 📋 No existe | B2 |

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

- **2026-05-05 20:00** — A2 cerrado (U0 extraído como prueba). Prompt de fase 1 ampliado con 3 secciones nuevas (unidades atípicas, sílaba tónica subrayada hasta U3, patrón "primer ítem resuelto como ejemplo"). Convención de naming extendida a U0 en docs.
- **2026-05-05 18:30** — CLAUDE.md raíz reducido a 85 líneas (Anthropic best practices). Movida historia/estado/planes a PROCESO-MAESTRO/README/REVIEW según corresponda.
- **2026-05-05 18:00** — Confirmada arquitectura datos centralizados + instrucciones modulares. Añadido al inicio del documento como principio arquitectónico no negociable. Sin cambios estructurales en los pasos.
- **2026-05-05 17:00** — Reescrito con gates explícitos. Cada paso ahora declara: archivos involucrados + actualizaciones meta requeridas + gate de cierre con condiciones numeradas + validación del revisor + dependencias hacia adelante. Añadidas reglas globales del proceso (qué meta-archivo se actualiza cuándo) y sección "cómo el revisor analiza este documento".
- **2026-05-05 16:30** — Creación inicial.
