# REVIEW — Bloque A cerrado (extracción literal)

Detalle íntegro del Bloque A "Estabilizar la fase 1" de `REVIEW.md`, archivado tras su cierre completo el 2026-05-07. Texto literal del bloque, sin reescribir.

Subpasos A1, A2, A3 cerrados el 2026-05-05; A4 (refactor documental de fase 1) cerrado el 2026-05-07 con merge `110e722` (v10.69) y cierres post-merge v10.70-v10.76b.

**Importante:** este archivo contiene **solo el detalle del Bloque A** (sub-pasos, gates, riesgos, plan ejecutable A4.0-A4.6). La bitácora cronológica general del proyecto **permanece viva en `REVIEW.md`** ("Bitácora de actualizaciones del REVIEW") y NO se traslada aquí.

Resumen vivo (1 párrafo) sigue en `REVIEW.md` en la posición original del Bloque A.

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

### A4. Refactor documental de fase 1 — ✅ CERRADO 2026-05-07 (merge `110e722`, v10.69; cierres post-merge v10.70-v10.73)

**Objetivo:** separar `fases/1-extraccion-inventario/prompt.md` (hoy 547 líneas mezclando schema + reglas + casos + mantenimiento) en **5 archivos por responsabilidad** (CLAUDE.md fase, prompt.md core, schema-inventario.md, reglas-operativas.md, convenciones-y-casos.md). NO reabre decisiones editoriales. NO modifica los inventarios U0/U1/U3.

**Pre-condición:** ninguna (la propuesta está cerrada en v10.39).

**Source of truth operativa:** `docs/historico/refactor-prompt-fase1/REFACTOR-PROPUESTA.md` (archivado tras el cierre del refactor; durante la ejecución vivió en `fases/1-extraccion-inventario/`). Este paso A4 NUNCA duplicó el plan; lo invocó y llevó el progreso por sub-paso.

**Sub-pasos** (según `REFACTOR-PROPUESTA.md` sección 5, ahora archivado):

| Sub-paso | Descripción breve | Estado |
|---|---|---|
| **A4.0** | Tag `pre-refactor-prompt-fase1` + rama `refactor/prompt-fase-1` (+ worktree dedicado, ver `docs/historico/refactor-prompt-fase1/REFACTOR-WORKTREE.md`) | ✅ 2026-05-06 16:30 (tag y rama → `cc1f18b`; worktree en `../guia-didactica-refactor/`) |
| **A4.1** | Crear los 3 archivos auxiliares vacíos con headers | ✅ 2026-05-06 18:45 (`schema-inventario.md` 8 líneas, `reglas-operativas.md` 8, `convenciones-y-casos.md` 10) |
| **A4.2** | Migrar contenido fila por fila aplicando split por capa + verificación de anclas | ✅ (a) schema · (b) reglas-operativas · (c) convenciones-y-casos. prompt.md: 547 → 108 líneas (–80%). 4 archivos en su sitio sin contenido editorial residual |
| **A4.3** | Reescribir `prompt.md` core desde cero (incluye sección "Cierre y validación") | ✅ 2026-05-07 02:00 (107 líneas, 9 secciones; cero placeholders intermedios; "Cierre y validación" absorbida; norte 80-120 cumplido) |
| **A4.4** | Reescribir `CLAUDE.md` de fase en modo contrato corto | ✅ cerrado limpio 2026-05-07 03:00 en v10.57 (59 líneas tras añadir convención root-relative explícita; 7 secciones; norte 40-60 cumplido; cero duplicaciones literales con prompt.md) |
| **A4.5** | Prueba empírica de reextracción y reclasificación contractual de los 3 oráculos (U0, U1, U3) | ✅ 2026-05-07 (v10.64–v10.67): U0 piloto (10 act); U1 (42 act, 3 fixes A1/A2/A3 del revisor); U3 (47 act, 11 cambios de tipo); +1 fix bloqueante v10.67. Validador U0/U1/U3 → 0/0 |
| **A4.5.5** | **Cross-check obligatorio** schema-inventario.md ↔ validar_inventario.py — gate ineludible antes del merge | ✅ 2026-05-07: 5/5 enumeraciones idénticas (tipo 20, destreza 6, enfoque 6, tipo_cuadro 5, seccion 7), 0 divergencias |
| **A4.6** | Sincronizar CHANGELOG/REVIEW/PROCESO-MAESTRO + merge a `main` | ✅ 2026-05-07 (commit `110e722`): merge `refactor/prompt-fase-1` → `main` con `--no-ff`; 14 archivos, +2555/–838; validador U0/U1/U3 → 0/0 post-merge |

**Marcador externo de progreso:** cada commit del refactor cita su sub-paso en el mensaje (ej. `A4.2: schema-inventario migrado`). El estado de cada fila de la tabla anterior se actualiza al cerrar el sub-paso correspondiente.

**Tipología de verificaciones por sub-paso** (regla operativa, ver detalle en `docs/historico/refactor-prompt-fase1/REFACTOR-PROPUESTA.md` §5):
- **A4.2 → A4.4:** solo checks locales de integridad documental (anclas semánticas, mapeo como checklist externo, no-duplicación entre archivos). NO pruebas funcionales.
- **A4.5:** primera prueba funcional oficial (reextracción empírica de los 3 casos).
- **A4.5.5:** cross-check schema ↔ validador antes del merge (gate obligatorio).
- **Smoke test opcional tras A4.4:** permitido en chat para detectar roturas obvias antes de A4.5. NO es gate formal ni sustituye la prueba funcional de A4.5.

**Gate de cierre de A4 entero:**
1. ✅ Sub-pasos A4.0 → A4.6 cerrados según los gates detallados en `docs/historico/refactor-prompt-fase1/REFACTOR-PROPUESTA.md`.
2. ✅ Acta del paso A4.5.5 con **0 divergencias** schema↔validador (puede implicar commit aparte de alineación del validador antes del merge — prerequisito ineludible, no opcional).
3. ✅ Prueba empírica del paso A4.5: los 3 casos validan con 0 errores y 0 avisos en estado pre-merge, sin pérdida de decisiones semánticas cerradas.
4. ✅ Merge `refactor/prompt-fase-1` → `main` ejecutado.
5. ✅ Bitácoras de REVIEW + CHANGELOG + PROCESO-MAESTRO actualizadas con el cierre.

**Bloquea a:** ninguna fase activa. El refactor mejora mantenibilidad de fase 1 sin alterar su funcionamiento.

**Riesgos y mitigaciones:** ver `docs/historico/refactor-prompt-fase1/REFACTOR-PROPUESTA.md` sección 6.

---

