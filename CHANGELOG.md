# Changelog — Guía Didáctica del Profesor (IA)
## Sistema de Agentes v5.0 — Nuevo Compañeros 1

> Histórico anterior a v10.40 archivado en `docs/historico/CHANGELOG-pre-refactor.md`.

---

## [v10.114 — 2026-05-13] — Archivo de documentos absorbidos a `docs/historico/`

Dos documentos de fase 1 cuyo contenido ya está absorbido en los contratos vivos pasan a histórico:

- `fases/1-extraccion-inventario/schema-inventario-viejo.md` → `docs/historico/schema-inventario-viejo.md`. Su propio header lo declaraba histórico; sus decisiones viven ahora en `schema-inventario.md` cuerpo §1-§14.
- `fases/1-extraccion-inventario/PROPUESTA-PIEZA-2-IA-FIRST.md` → `docs/historico/PROPUESTA-PIEZA-2-IA-FIRST.md`. Propuesta arquitectónica del rediseño IA-first, absorbida en `prompt.md`, `schema-inventario.md`, `glosario.md` y `reglas-operativas.md`.

`fases/1-extraccion-inventario/REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md` se mantiene en su ubicación actual por decisión del autor (sigue siendo referencia de discusión activa). Referencias actualizadas en `CLAUDE.md` de fase 1.

## [v10.113 — 2026-05-13] — Retirada de fixtures exploratorias U2p y U3p tras prueba

Las fixtures `U2-propuesta` y `U3-propuesta` introducidas en v10.112 cumplieron su función (prueba mínima discriminativa + segunda prueba cerrable que reveló el error de proceso motivador de `reglas-operativas.md` §5.12-§5.14). Eliminadas del repositorio tras consolidar las lecciones en contrato vivo. `U1-propuesta` se mantiene intacta con su shape original (`_propuesta_rediseno` + `_migracion_rediseno`) y su banner especial en el dashboard, reservada como muestra de la arquitectura nueva para revisión futura. Sin cambios en el contrato documental ni en el dashboard.

## [v10.112 — 2026-05-13] — Rediseño fase 1: dashboard adaptado + fixtures exploratorias

Segundo commit del hito transitorio (continuación de v10.111).

- `diagrama.py`: mapping genérico `Np` → `UN-propuesta` (antes solo `U1p` hardcodeado).
- `web/index.html`: 3 bugs del renderer ante el shape nuevo corregidos. (1) `vocBlock` ahora lee `g.items || g.palabras` (compatibilidad shape nuevo + viejo). (2) `verbosBlock` lee `v.lo_que_se_trabaja || v.descripcion` (registry o schema). (3) `renderConsolidatedWithSubs` ahora pinta sub-bloques vacíos como "(vacío)" atenuado, en lugar de ocultarlos.
- Fixtures exploratorias en `unidades/`: `U1-propuesta` (preexistente, ahora trackeada), `U2-propuesta` (pp.24+30, cerrable tras decisiones D1-D3 en chat: Escuela canónico para léxico cultural, ser entra en cuadro Demostrativos, clases optativas/obligatorias renombrados; metadata coherente con contenido), `U3-propuesta` (pp.32+34, prueba discriminativa que reveló error sistémico de proceso al omitir vocabulario_consolidado.recurrente; motivó §5.12-§5.14 en reglas-operativas).
- Convención `_fixture_exploratoria` consolidada: visibles en dashboard como `Up`, declaradas extracontractuales en schema §A.5 y glosario.

## [v10.111 — 2026-05-13] — Rediseño fase 1: contrato documental consolidado (hito transitorio)

Primer commit del hito transitorio del rediseño de fase 1. **Schema NC1 cerrado en cuerpo; rediseño fase 1 completo NO cerrado** (deuda viva catalogada en Apéndice transitorio).

- `fases/1-extraccion-inventario/schema-inventario.md`: cuerpo §1-§14 cerrado para NC1 (top-level, página, actividad, cuadro, 4 enumeraciones cerradas, 4 bloques consolidados con fuentes y descripcion compartidas en §9.5/§9.6, respuestas y multimedia, marcas internas §14). Apéndice transitorio §A.1-§A.5 cataloga deuda externa: alineación validador (§A.1), clave transitoria `_migracion_rediseno` (§A.2), 11 ítems específicos para validador (§A.3 — renombrados de enums, ampliación tiempo, normalización formas_trabajadas, suite de verificación automatizada, etc.), condiciones de retirada del apéndice (§A.4), metadata extracontractual `_fixture_*` (§A.5).
- `fases/1-extraccion-inventario/glosario.md`: creado. Diccionario operativo de todos los términos del schema, alineado con `schema-inventario.md` punto por punto.
- `fases/1-extraccion-inventario/reglas-operativas.md`: 5 reglas del rediseño integradas en cuerpo con carácter OBLIGATORIO. §5.10 (verbo soporte: entra si sus formas aparecen, independientemente del foco), §5.11 (normalización formas_trabajadas), §5.12 con sub-A/B/C (procedimiento obligatorio de poblado de `recurrente` para las tres dimensiones), §5.13 (propuesta-en-chat ante toda decisión no clara), §5.14 (construcción iterativa de `recurrente`). Banner de follow-ups conserva la deuda residual: sufijo `@R`, regla 11 audio, input incidental, anticipación, heterogeneidad semántica, suite de verificación.
- `fases/1-extraccion-inventario/CLAUDE.md`: header reescrito con semáforo de estado real (🟢 schema, 🟡 reglas-operativas, 🟡 convenciones-y-casos). Regla de precedencia: en conflicto schema↔reglas-operativas, gana schema. Convención de fixtures `UNp` documentada.
- `fases/1-extraccion-inventario/prompt.md`: nota transitoria cubre validador + reglas-operativas con regla de precedencia; pasos 3a/3b explícitos (clasificar y derivar consolidados); lookup bajo demanda incluye los 4 archivos PCIC.
- `fases/1-extraccion-inventario/convenciones-y-casos.md`: renombrado `fonetica` → `pronunciacion_ortografia`.
- Registries esqueleto: `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`. `verbos-canonicos.json` ya poblado.
- 4 archivos PCIC A1 fuente: `pcic-a1-vocabulario.json` (417 entradas), `pcic-a1-gramatica.json`, `pcic-a1-pronunciacion-ortografia.json` (sub-bloques pronunciación + ortografía, pronunciación extraída de Cervantes web), `pcic-a1-comunicacion.json` (fuera de las 4 dimensiones, recurso disponible).
- Documentos archivados: `docs/historico/prompt-v1-antiguo.md`, `docs/historico/prompt-v2-monolitico-NO-USAR.md`. Documentos de transición arquitectónica: `REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md`, `PROPUESTA-PIEZA-2-IA-FIRST.md`, `schema-inventario-viejo.md`, `fases/2-reciclaje/REDISEÑO-EN-CURSO.md`.

## [v10.108f — 2026-05-11] — Cierre residual de coherencia: PROCESO-MAESTRO paso 7 del pipeline

Hallazgo medio del revisor sobre v10.108e: quedaba una línea viva en PROCESO-MAESTRO §3 (pipeline definido, paso 7) que decía *"actualizar `nc1-reciclaje.json` manualmente con ayuda de Claude Code en chat (no automático)"* y contradecía el comportamiento vigente desde v10.108d.

Reformulada como histórico, apuntando a la decisión 36 y al comportamiento actual (fase 2 pausada + flag `--regenerar-reciclaje` opcional). Grep cruzado confirma cero referencias residuales al modelo viejo automático en docs operativas / contrato vigente; las entradas cronológicas en bitácoras (REVIEW y PROCESO-MAESTRO) se conservan literales como historia.

REVIEW etiqueta de sincronización → v10.108f. Esta entrada se autodocumenta.

---

## [v10.108e — 2026-05-11] — Cierre de coherencia documental tras v10.108d

Tres correcciones tras hallazgos del revisor sobre v10.108d:

- **Medio:** `fases/2-reciclaje/CLAUDE.md` y `reglas-reciclaje.md` decían que el nivel auto "se ejecuta automáticamente al integrar cada unidad". Actualizados al comportamiento real: fase 2 pausada, integración no regenera por defecto, flag `--regenerar-reciclaje` opcional.
- **Bajo:** `CLAUDE.md` raíz tenía en el comentario del comando `integrar_unidad.py` el wording "valida + actualiza reciclaje + commit". Reformulado a "copia + valida + commit del inventario" con nota sobre el flag opcional.
- **Bajo:** `PROCESO-MAESTRO.md` líneas 118 (Parte 3, descripción D) y 546 (decisión 23) contaban dos modelos antiguos del reciclaje distintos del vigente. Anotadas como histórico/superado por la decisión 36; trazabilidad de evolución preservada (v10.97 introdujo scripts, v10.108 pausó fase 2, v10.108d desacopló).

REVIEW etiqueta de sincronización → v10.108e. Esta entrada se autodocumenta.

---

## [v10.108d — 2026-05-11] — Desacoplar regeneración de reciclaje del flujo de integración (fase 2 pausada)

Hallazgo medio del revisor: `integrar_unidad.py` ejecutaba `regenerar_reciclaje_vocabulario.py` automáticamente en cada integración, contradiciendo la pausa declarada de fase 2 en REVIEW/README/PROCESO-MAESTRO y las decisiones antiguas que describían el reciclaje como manual.

**Opción A disciplinada** aplicada:
- `scripts/integrar_unidad.py`: la llamada al regenerador queda detrás de un flag explícito `--regenerar-reciclaje`. Por defecto, el reciclaje no se toca. El docstring y el paso 4 reflejan el cambio. El commit final solo incluye el inventario por defecto, y el reciclaje solo si se regeneró.
- README.md, REVIEW.md y PROCESO-MAESTRO §36: nota corta que explica el comportamiento por defecto durante la pausa de fase 2 y la existencia del flag opcional.
- REVIEW etiqueta de sincronización → v10.108d.
- Eliminado el `.bak` local del canon (transitorio, gitignored).

Esta entrada se autodocumenta en el mismo commit para no reabrir la regresión de trazabilidad.

---

## [v10.108c — 2026-05-11] — Sincronización documental del batch canon (REVIEW + PROCESO-MAESTRO + CHANGELOG)

Cierre documental de la activación del canon semántico en fase 1
(v10.108 + v10.108b). Sin cambios funcionales: solo trazabilidad.

- CHANGELOG: entradas formales de v10.108, v10.108b y esta misma v10.108c (autodocumentada para no reabrir la regresión doc).
- REVIEW: estado de fase 1 actualizado con canon activado en rollout R1; etiqueta de sincronización → v10.108c; bitácora con el cierre del batch.
- PROCESO-MAESTRO: bitácora con la implementación cerrada de la decisión 36.

---

## [v10.108b — 2026-05-11] — Fix prompt: ítem 13 del checklist alineado al contrato del canon

Hallazgo bajo del revisor sobre v10.108: el ítem 13 del checklist de cierre del entrypoint decía "existen en el canon o son aliases conocidos", pero el resto del contrato exige canónicos literales para extracción nueva. Reformulado a "canónicos literales (no aliases)". Aliases solo se reconocen para diagnóstico de legacy. Sin cambios funcionales.

---

## [v10.108 — 2026-05-11] — Canon semántico activado en fase 1 (batch único)

Batch único que cierra la coherencia del canon en fase 1 sin romper main en ningún punto. Combina los pasos 3-7 del plan de implementación de la decisión 36 (E-final).

**6 archivos modificados, 0 archivos doc nuevos:**

- `schema-inventario.md`: §9, §10, §13 con restricciones canon + marca `_pendiente_canon`. Ejemplo top-level alineado a `<canonico>`.
- `reglas-operativas.md` §5.6: reescrita por completo. Sustituye la decisión "liberal" antigua. Define universo válido, frontera `aliases_indice` vs `aliases_auto` por procedencia, árbol de decisión, rollout R1/R2/R3 con matriz por tipo de match.
- `scripts/validar_inventario.py`: tercer canal `auditoria_legacy` con contador propio. Constantes `ROLLOUT_CANON_ITERACION = "R1"` y `LEGACY_UNIDADES_R1 = [0..9]`. Función `_validar_canon_inventario` recorre dos superficies (campo_semantico + claves de vocabulario_consolidado). Dos fixes: control de canon malformado (vía `canon.validar_canon`) y distinción real `aliases_indice` vs `aliases_auto` por iteración. `_pendiente_canon` → error duro siempre. Bug latente de shadowing `d`→`dx` en loop de destreza arreglado.
- `prompt.md`: pasos 5 y 6 del flujo instruyen agrupación canónica directa y `_pendiente_canon` como vía honesta. Checklist con 2 ítems nuevos (13 canon, 14 ausencia de marca).
- `CLAUDE.md` de fase 1: regla crítica 6 (canon como autoridad de naming) + entrada en tabla de navegación.
- `PROCESO-MAESTRO.md`: decisión 36 — `_pendiente_canon` aclarado como marca literal (no booleano).

**Comportamiento del validador (matriz documentada y aplicada):**

| Caso | R1 legacy | R1 no-legacy | R2 | R3 |
|---|---|---|---|---|
| canónico literal | OK | OK | OK | OK |
| `aliases_indice` | auditoría legacy | error duro | OK silencioso | error duro |
| `aliases_auto` | auditoría legacy | error duro | aviso | error duro |
| sin match | auditoría legacy | error duro | error duro | error duro |
| `_pendiente_canon` | error duro | error duro | error duro | error duro |

**Verificación:** U0-U9 siguen validando 0/0 con auditoría legacy informativa (11, 19, 9, 13, 9, 14, 16, 14, 16, 0 entradas respectivamente). Caso negativo controlado (U10 simulada) produce los errores duros esperados. Canon íntegro (98 entradas).

---

## [v10.105b — 2026-05-11] — Fix doc v10.105: ambigüedad de SoT + trazabilidad + tabla README

Tres correcciones tras hallazgos del revisor sobre v10.105:
- PROCESO-MAESTRO decisión 36: se quita la mención a `_politica` embebida en el JSON canónico (contradecía la versión aprobada "JSON solo de datos, política en `reglas-operativas.md`"). La política y `LEGACY_UNIDADES_R1` se ubican explícitamente en sus archivos correctos.
- REVIEW etiqueta de sincronización: v10.104b → v10.105b (estaba un commit por detrás).
- README tabla de estado: fase 2 marcada como "⏸ Pausada hasta cierre del canon de fase 1" para alinear con la sección Estado actual.

Esta entrada se autodocumenta en este commit para no reabrir la regresión de trazabilidad.

---

## [v10.105 — 2026-05-11] — Decisión de diseño cerrada: canon semántico en fase 1 (E-final)

Tras 5 iteraciones revisor↔ejecutor sobre cómo gobernar los nombres de `campo_semantico` y de las claves de `vocabulario_consolidado` en los inventarios:

**Propuesta E-final aprobada por el revisor:** el canon vive dentro de fase 1, integrado en sus documentos existentes sin crear archivos de doc nuevos. Artefactos nuevos solo son datos y código (`campos-semanticos-canonicos.json`, `scripts/canon.py`, `scripts/inicializar_canon_semantico.py`). Modificaciones quirúrgicas a `CLAUDE.md`/`prompt.md`/`reglas-operativas.md`/`schema-inventario.md` de fase 1. Validador endurecido con 3 canales (errores, avisos, auditoría legacy con contador propio). Rollout R1 (auditoría para U0-U9, error duro para nuevas) → R2 (legacy vaciada) → R3 (endurecimiento final). Dos carriles complementarios: extracción canónica desde origen (prompt) + saneamiento retrospectivo. Marca `_pendiente_canon` transitoria con triple defensa que bloquea cierre. Dashboard solo lectura. **Fase 2 pausada** hasta cierre de canon; modelo viejo del reciclaje (mapa+auto+detalle paralelo) anulado.

**Sincronización documental:**
- `REVIEW.md`: estado bloque B reformulado; B2a marcado como anulado; bitácora con entrada de la decisión.
- `PROCESO-MAESTRO.md`: decisión 36 nueva con detalle completo; anotación de anulación en la descripción del modelo viejo de `nc1-reciclaje.json` (línea 213); bitácora.
- `README.md`: estado actual de fase 1 y fase 2 actualizados.

No incluye `fases/2-reciclaje/REDISEÑO-EN-CURSO.md` (artefacto local untracked, sigue siendo el documento de trabajo de la reformulación de fase 2 cuando llegue su turno).

---

## [v10.104d — 2026-05-11] — Fix CHANGELOG: entrada formal de v10.104c

Hallazgo bajo del revisor sobre `05ddacb`: el fix de v10.104c reescribió la entrada de v10.104b pero no se autodocumentó como hito propio en el changelog. Añadida entrada formal de v10.104c. Esta entrada de v10.104d se autodocumenta en el mismo commit para no reabrir la brecha.

---

## [v10.104c — 2026-05-11] — Fix CHANGELOG: retira referencia a artefacto local untracked

Hallazgo bajo del revisor sobre v10.104b: la entrada de CHANGELOG mencionaba `fases/2-reciclaje/REDISEÑO-EN-CURSO.md` como ubicación de los refinamientos pendientes, pero ese archivo es local untracked. Reformulada la frase para no comprometer una referencia que no existe en clon limpio.

---

## [v10.104b — 2026-05-11] — Doc canónica de integración U9 + curso completo extraído

Sincroniza CHANGELOG/REVIEW/PROCESO-MAESTRO/README con la integración U9 (v10.104) y refleja que U0-U9 están integradas y validando 0/0. No incluye `REDISEÑO-EN-CURSO.md` (artefacto local untracked).

Esta entrada se autodocumenta en el mismo commit junto a la de v10.104, evitando reabrir la brecha de trazabilidad del patrón doc-comenta-pero-no-se-comenta.

**Estado tras este commit:** curso completo extraído (10 unidades). Fase 1 con todos los inventarios integrados; refinamientos del extractor identificados pendientes (canon semántico, doble superficie del validador, refuerzo del prompt) — su documentación operativa entrará en main cuando se cierre la decisión.

---

## [v10.104 — 2026-05-11] — Integración U9 a main (41 actividades, 6 cuadros, 0/0)

Integración limpia de U9 desde worktree `extract/U9` vía `integrar_unidad.py`. Última unidad del curso.

- **Stats:** 41 actividades, 6 cuadros, autoevaluación presente, validador 0/0.
- **Reciclaje:** se mantiene en 181 hilos (92 mapa + 89 auto) — U9 no introduce campos semánticos nuevos respecto a U0-U8; sus contenidos caen sobre hilos ya existentes.
- **Sin desviaciones** del flujo automatizado.

---

## [v10.103c — 2026-05-10] — Fix doc: autodocumenta v10.103b + retira referencia a artefacto local

Dos correcciones tras hallazgos del revisor sobre b887984:
- CHANGELOG/REVIEW/PROCESO-MAESTRO: añadida entrada formal de v10.103b (que sincronizaba la integración U8 pero no se autodocumentaba).
- REVIEW: retirada la referencia a `REDISEÑO-EN-CURSO.md` del estado comprometido del bloque B. Ese artefacto sigue local (untracked); no debe figurar como referencia activa en main.
- Esta entrada (v10.103c) se autodocumenta en el mismo commit, evitando reabrir la brecha de trazabilidad.

---

## [v10.103b — 2026-05-10] — Doc canónica de integración U8

Sincroniza CHANGELOG/REVIEW/PROCESO-MAESTRO con la integración U8 (v10.103). 46 actividades, 5 cuadros, 0/0, reciclaje a 181 hilos (92 mapa + 89 auto).

---

## [v10.103 — 2026-05-10] — Integración U8 a main (46 actividades, 5 cuadros, 0/0)

Integración limpia de U8 desde worktree `extract/U8` vía `integrar_unidad.py`. Reciclaje actualizado: 181 hilos (92 mapa + 89 auto). Sin desviaciones del flujo automatizado.

---

## [v10.102 — 2026-05-10] — Integración U7 a main (46 actividades, 4 cuadros, 0/0)

Integración limpia de U7 desde worktree `extract/U7` vía `integrar_unidad.py`. Reciclaje actualizado: 171 hilos (92 mapa + 79 auto). Sin desviaciones del flujo automatizado.

---

## [v10.101 — 2026-05-10] — Refuerzo del checklist de cierre del extractor (prompt.md)

Tras auditar los tres fixes del ejecutor 2 en U6 (ejemplo duplicado en respuestas + ítem inventado), análisis: las reglas canónicas existen y son suficientes (§1.6 y §5.7), pero son fallos invisibles al validador estructural. La fricción está en el cierre — el ejecutor no estaba comprobándolos antes de dar el JSON por bueno.

Añadidos 2 ítems al checklist de "Comprobaciones manuales" en `prompt.md` (no nueva sección, no bloat):
- Ítem 11: `datos.ejemplo_libro` no duplicado en `respuestas` (ref §1.6).
- Ítem 12: cardinalidad literal de `items_libro` igual a la del PDF, sin invención (ref §5.7).

No se modifican reglas. Solo se hace explícito en el prompt lo que ya era obligatorio.

---

## [v10.100 — 2026-05-10] — Integración U6 a main (44 actividades, 4 cuadros, 0/0)

Primera integración con el flujo automatizado `integrar_unidad.py`. Inventario U6 final auditado por el ejecutor 2 + actualización automática de `nc1-reciclaje.json` (161 hilos: 92 mapa + 69 auto).

Tres fixes de auditoría incluidos en el inventario final:
- Ejemplo duplicado eliminado en `respuestas` de U6-p64-act01.
- Ejemplo duplicado eliminado en `respuestas` de U6-p64-act02.
- Ítem inventado #9 eliminado en U6-p65-act04.

U6 usa el campo canónico `columnas_relaciona` en U6-p63-act05, U6-p63-act08, U6-p68-act02 y U6-p71-act05 (campo introducido en v10.98).

---

## [v10.99g — 2026-05-10] — Cierre de regresión doc: v10.99e/f autodocumentadas

Doble cierre para detener la regresión "cada commit doc abre una brecha nueva":
- Entrada de v10.99e corregida: decía "Tres correcciones" enumerando cuatro bullets, y uno (separación v10.99b/c) no fue cambio de v10.99e — esas entradas ya estaban separadas en v10.99d. Atribución falsa eliminada.
- Entrada formal de v10.99f añadida.
- Esta misma entrada (v10.99g) cierra el ciclo en el mismo commit que documenta a sus predecesoras, evitando otra brecha.

---

## [v10.99f — 2026-05-10] — Cierre trazabilidad: v10.99e documentado

Tras hallazgo del revisor: v10.99e era un commit doc pero no estaba reflejado en CHANGELOG/REVIEW/PROCESO-MAESTRO. Añadidas entradas formales en los tres documentos.

---

## [v10.99e — 2026-05-10] — Fix doc: cronología honesta v10.99 + estado sincronización

Tres correcciones tras hallazgos del revisor sobre v10.99d:
- CHANGELOG v10.99: la entrada original atribuía retroactivamente a v10.99 garantías que no entraron hasta v10.99b/c. Reescrita para reflejar solo lo que entró en ese commit.
- CHANGELOG: añadida entrada formal de v10.99d.
- REVIEW: estado de documentación marcado como ✅ sincronizada.

---

## [v10.99d — 2026-05-10] — Sincronización documental CHANGELOG/REVIEW/PROCESO-MAESTRO

Actualización obligatoria de los tres documentos canónicos tras los commits v10.97-v10.99c que habían quedado sin reflejarse. Sin cambios de código ni datos.

---

## [v10.99c — 2026-05-10] — Fix integrar_unidad: snapshot de nc1-reciclaje.json antes de regenerar

Si `regenerar_reciclaje_vocabulario.py` falla, ahora se restauran ambos archivos: el inventario de la unidad y `nc1-reciclaje.json`. Antes solo se restauraba el inventario, dejando el reciclaje potencialmente inconsistente.

---

## [v10.99b — 2026-05-10] — Fix integrar_unidad: git add antes del commit + corrección de sintaxis

Dos defectos del v10.99 cerrados tras hallazgos del revisor:
- Sintaxis de commit corregida: `git commit --only -- <paths> -m <msg>` era inválida (después de `--` todo es pathspec) → `git commit -m <msg> -- <paths>` con `-m` antes de `--`.
- `git add` explícito añadido antes del commit para que funcione con archivos nuevos (caso real: primera integración de U6).

---

## [v10.99 — 2026-05-10] — Script integrar_unidad.py + fase 2 CLAUDE.md actualizado

`scripts/integrar_unidad.py` — nuevo script que encadena los pasos de integración de una unidad: copia, valida, actualiza reciclaje, commit. Primera versión del flujo automatizado. **Defectos corregidos en commits posteriores:** sintaxis de commit inválida (v10.99b), restauración incompleta de main si fallaba el reciclaje (v10.99c).

`CLAUDE.md` raíz — añadido `integrar_unidad.py` a comandos básicos.

`fases/2-reciclaje/CLAUDE.md` y `reglas-reciclaje.md §4` — nivel auto documentado como parte del flujo de integración automática, no invocación manual.

---

## [v10.98 — 2026-05-10] — Campo canónico columnas_relaciona + migración U1/U5

Nuevo campo canónico `datos.columnas_relaciona` para actividades `relaciona` con dos columnas explícitas en el libro (`{izquierda: [str], derecha: [str]}`).

- `schema-inventario.md`: campo añadido al saco `datos`; §12 actualizado con excepción para `relaciona` columnar; ref a `TIPOS_QUE_REQUIEREN_CONTENIDO_VISIBLE`.
- `reglas-operativas.md §5.7`: excepción explícita para `relaciona` con dos columnas.
- `convenciones-y-casos.md §1.8`: convención nueva con ejemplo canónico y caso disparador.
- `validar_inventario.py`: `columnas_relaciona` en `CONTENIDOS_VISIBLES` + validación estructural; `TIPOS_QUE_REQUIEREN_ITEMS` renombrado a `TIPOS_QUE_REQUIEREN_CONTENIDO_VISIBLE`; mensaje de error actualizado.

Migración: `U1-p16-act4` (números↔palabras), `U5-p53-act01` (adjetivos↔contrarios), `U5-p55-act04` (preguntas↔respuestas). U6 pendiente para el ejecutor 2.

---

## [v10.97 — 2026-05-10] — Integración U5 + fase 2 reciclaje automatizada

Integración U5 a main (worktree `extract/U5`, 46 actividades, 4 cuadros, 0/0). Fix: `textos_personajes` de `U5-p58-act01` convertido de objeto a lista canónica `[{personaje, texto}]`.

Fase 2 reciclaje — base automatizada:
- `fases/2-reciclaje/CLAUDE.md`: contrato de fase con orden obligatorio de scripts.
- `fases/2-reciclaje/reglas-reciclaje.md`: criterios de agrupación, tabla de acciones, casebook.
- `scripts/regenerar_reciclaje_mapa.py`: genera hilos mapa desde `nc1-curso.json`; preserva auto/detalle. Procesa U0 (`contenido_general`) y campos estándar.
- `nc1-reciclaje.json` regenerado: 92 hilos mapa + 59 auto = 151 hilos. "Países hispanohablantes y nacionalidades" separado en dos hilos. "Léxico de aula" eliminado.

---

## [v10.96b — 2026-05-09] — Cierre v10.96: framing general del antipatrón `enfoque` ≠ `seccion` + corrección U5-p61-act04

Hallazgos del revisor sobre v10.96: la regla #3 hablaba solo de Cultura/Comunicación cuando el antipatrón aplica a cualquier sección, y el caso U5-p61-act04 estaba mal etiquetado (era sección Evaluación, no Comunicación).

**Cambios:**
- `reglas-operativas.md` §2.3 — bloque "Antipatrón frecuente" reformulado a proximidad editorial general: enumera las 6 secciones (`gramatica`, `vocabulario`, `comunicacion`, `cultura`, `destrezas`, `evaluacion`) y aclara que el antipatrón aplica sea cual sea la sección. U5-p61-act04 corregido a sección Evaluación.
- `convenciones-y-casos.md` §1.7 — título y ejemplo reformulados ("seccion: X → enfoque: X"). El bloque "cuándo SÍ aplica enfoque de dominio" ya cubre los 5 dominios (cultura, comunicacion, gramatica, vocabulario, fonetica), no solo dos. U5-p61-act04 corregido.

**Sin cambios funcionales en datos.** Validador U0-U4 → 0/0.

---

## [v10.96 — 2026-05-09] — Fixes de fase 1 a partir de hallazgos de extracción U5

Tres problemas detectados durante la revisión de U5 (ejecutor 2, sin integrar todavía a main) corregidos en el contrato de fase 1. El cuarto problema (palabras-respuesta de imágenes) se descartó tras revisión: era error del ejecutor, no gap del schema.

**Problema 1 — `textos_personajes` no reconocido por validador:**
- `schema-inventario.md` §3: campo nuevo `textos_personajes: [{personaje, texto}]` en saco `datos`, para N textos cortos atribuidos a N personajes (autorretratos, fichas, presentaciones múltiples). Distinto de `texto_completo` (texto seguido) y `dialogo_completo` (turnos).
- `validar_inventario.py`: añadido a `CONTENIDOS_VISIBLES` + validación estructural — debe ser lista de objetos con `personaje` y `texto` (strings no vacíos). Probado: detecta tipos mal formados.
- `convenciones-y-casos.md` §1.4-bis: regla con ejemplo, tabla de decisión entre los 3 campos canónicos, caso disparador U5-p58-act01 (4 descripciones en Destrezas).
- `reglas-operativas.md` §2.5: tabla de elección entre `texto_completo` / `dialogo_completo` / `textos_personajes` con principio "no fusionar para forzar `texto_completo` cuando hay atribución por personaje".

**Problema 2 — Etiquetas editoriales coladas en `respuestas`:**
- `convenciones-y-casos.md` §1.6: regla "marcadores editoriales no van en `respuestas`". `Posibles respuestas:`, `Ejemplo:`, `Modelo:`, `Solución:` se descartan; el contenido tras el marcador va a `datos.ejemplo_libro` / `datos.ejemplos_modelo` o a `respuestas` sin el marcador. Ejemplos correcto/incorrecto + casos disparadores U5-p54-act03, U5-p55-act02, U5-p61-act02.

**Problema 3 — `enfoque` heredado por proximidad editorial:**
- La regla ya existía en `reglas-operativas.md` §2.3 ("`enfoque` clasifica la actividad concreta, no la sección"). Lo que faltaba era refuerzo + caso visible.
- `reglas-operativas.md` §2.3: bloque "Antipatrón frecuente — copiar `enfoque` de `seccion`" con casos disparadores reales (U5-p60-act03, U5-p61-act04).
- `convenciones-y-casos.md` §1.7: ejemplo correcto/incorrecto + cuándo SÍ y cuándo NO usar `cultura`/`comunicacion` como enfoque (frente a `transversal`).

**Problema 4 — Palabras de imagen en respuestas:** descartado tras revisión con autor (error del ejecutor, no gap del schema).

**Verificado:** validador U0/U1/U2/U3/U4 → 0/0 tras los cambios.

---

## [v10.95 — 2026-05-09] — Modelo de hilos verbales: jerarquía uso → tipo de verbo → verbos + script auto vocabulario + categorías PCIC

**Bloque grande de cambios sobre `nc1-reciclaje.json` y la vista RECICLAJE del dashboard. Múltiples iteraciones con autor.**

**1. Taxonomía y rename:**
- `forma_verbal` → `tiempos_y_verbos` (cubre tiempos + tipos + verbos concretos).

**2. Schema de hilos verbales — 3 niveles de profundidad:**
- Cada hilo de `tiempos_y_verbos` (Presente, Imperativo, Pretérito indefinido) tiene `usos[]`.
- Cada `uso` tiene `id`, `titulo`, `ejemplo`, `tipos_verbo[]`.
- Cada `tipo_verbo` tiene `verbos[]` con `verbo`, `unidad`, `seccion`, `accion`, `formas_trabajadas`.
- Usos del presente derivados del estándar A1 (Universo Dele): acciones en el momento actual, hábitos y rutinas, información personal y verdades permanentes, verdades universales, futuro próximo.

**3. Categorías de verbos según PCIC del Cervantes / ELE canónico:**
- Verbos regulares (-ar / -er / -ir)
- Verbos con cambio vocálico (e→ie, o→ue, u→ue, e→i)
- Verbos con irregularidad en la 1.ª persona del singular
- Verbos totalmente irregulares
- Verbos pronominales
- Verbos del tipo *gustar*

(Antes había términos inventados: "defectivos pedagógicos", "súper irregulares", "irregulares yo (-go)" — corregidos.)

**4. Pase 1 ampliado a U0-U9 + reorden por aparición:**
- Pase 1 (mapa) cubre las 9 unidades (antes U0-U3).
- Hilos ordenados por unidad de primera aparición (U0 arriba, U9 abajo) — timeline más fluida.

**5. Script automático de vocabulario:**
- `scripts/regenerar_reciclaje_vocabulario.py` proyecta `vocabulario_consolidado` de cada inventario a hilos `vocabulario` con `nivel_analisis: "auto"`. 50 campos semánticos extraídos de U0-U4. Preserva hilos manuales (mapa).

**6. Vista RECICLAJE rediseñada — acordeón en la tabla:**
- Click en hilo verbal → expande inline con sub-filas por uso (cada uso con su mini-timeline).
- Click en uso → expande tipos de verbo y verbos concretos.
- Verbos del mismo nombre con múltiples eventos (ej. *ser* en U1+U2) se muestran en **una sola fila** con dots en cada unidad.
- Click en verbo (leaf) → drawer con secuencia de trabajo + ejemplo del uso.
- Texto agrandado, sin cursivas en verbos.

**7. Sección de incoherencias:**
- Componente al final de cada bloque de tipo (vocabulario, tiempos_y_verbos, contenido_gramatical, estrategia).
- Hoy vacío (verde "✓ Sin incoherencias detectadas") porque se anotarán manualmente cuando se detecten.

**Estado de datos:**
- 75 hilos: 23 manuales (mapa) + 52 auto (vocabulario por campo semántico).
- 3 hilos verbales con 9 usos totales, 25 verbos únicos, 50+ formas trabajadas anotadas.
- Inventarios sin tocar. Validador U0/U1/U2/U3/U4 → 0/0.

**Pendiente declarado por autor:** quedan más correcciones por iterar.

---

## [v10.94b — 2026-05-09] — Saneo post-v10.94: duplicado `estrategia` en frontend + 6 referencias vivas

Hallazgos del revisor sobre v10.94 (en dos rondas):

1. **`web/index.html`** — `REC_COLOR_TIPO` tenía la clave `estrategia` duplicada y el array `orden` repetía el mismo tipo, con lo que la vista RECICLAJE pintaba dos bloques ESTRATEGIA. Limpiado.
2. **`PROCESO-MAESTRO.md`** snapshot operativo (línea 227) y resumen vivo del bloque B (línea 697) actualizados al estado real (23 hilos / 70 eventos / U0-U9).
3. **`REVIEW.md`** estado vivo (líneas 45, 48, 157, 163) y tabla de artefactos (línea 428): U4 separada como trackeada (v10.93), B2a.1 cerrado v10.94, B2a.2 menciona inventarios disponibles + script automático pendiente.

**Sin cambios funcionales en datos.** Validador U0-U4 → 0/0.

---

## [v10.94 — 2026-05-09] — B2a pase 1 ampliado a U0-U9 + taxonomía unificada (4 tipos)

**Dos correcciones del autor sobre el alcance del pase 1:**

1. **Cobertura completa del índice.** El pase 1 anterior (v10.92) limitaba arbitrariamente a U0-U3 porque eran las únicas unidades integradas. Pero el pase 1 se basa en `nc1-curso.json` (índice oficial del libro), que ya contiene las 9 unidades. Las unidades aún no extraídas igualmente entran porque su contenido está declarado en el índice. Pase 1 regenerado cubriendo **U0-U9 completas**.
2. **Taxonomía unificada a 4 tipos.** El tipo `estrategia_comunicativa` se elimina; `estrategia` cubre cualquier tipo de estrategia (comunicativa, de aprendizaje, metacognitiva…) asociada a las destrezas de la lengua. El matiz va en la descripción del hilo, no en el tipo.

**Resultado del pase 1 ampliado:**
- 23 hilos, 70 eventos, todas las unidades del curso (U0-U9).
- Distribución por tipo: vocabulario 10, forma_verbal 1 (presente con 9 eventos), contenido_gramatical 5, estrategia 7.
- Hilos nuevos identificados al cubrir el resto del libro: comidas, vivienda, ubicación espacial, descripción, establecimientos, horarios, meses/animales, cuerpo, ropa, pronunciación (transversal), Para aprender (transversal), preposiciones, rutinas/hábitos.

**Cambios técnicos:**
- `unidades/nc1-reciclaje.json` — regenerado con 4 tipos válidos declarados en `_tipos_validos`.
- `PROCESO-MAESTRO.md` — bloque schema y decisión 20 actualizadas a 4 tipos.
- `web/index.html` — color map actualizado (estrategia_comunicativa eliminada).

**Próximo:** B2a.2 (pase 2 contra inventarios) + script automático de proyección de vocabulario por campo semántico.

---

## [v10.93 — 2026-05-09] — Integración de U4 a main (worktree extract/U4)

**Tercera integración del carril paralelo de extracciones** tras U2 (v10.87) y U3 (v10.91).

**Datos de U4:**
- 10 páginas (42-51), 49 actividades, 6 cuadros.
- Título: "Comidas y bebidas". Contrato post-refactor (taxonomía 20 + destreza/enfoque, schema cuadros).
- Validador: 0 errores / 0 avisos.

**Verificación del revisor (pre-merge):** todas las respuestas verificadas contra el solucionario del libro página por página. Ningún error de contenido (pronombres, conjugaciones, clasificaciones incluyendo queso como incontable, V/F, ordenaciones). El caso pescado/atún en p43-act01 es ambigüedad del propio libro, no del extractor.

**Estado de main post-integración:**
- Unidades trackeadas validando 0/0: U0, U1, U2, U3, U4.

**Próximo:** B2a.2 (pase 2 de reciclaje contra inventarios) y/o extracción de U5 en nuevo worktree por ejecutor 2.

---

## [v10.92b — 2026-05-09] — Saneo post-v10.92: contrato de hilos en docs vivas + multiplicidad de eventos

Hallazgos del revisor sobre v10.92: la migración funcional al modelo de hilos era correcta, pero el contrato vivo seguía describiendo el modelo punto-a-punto, y la timeline colapsaba silenciosamente múltiples eventos del mismo hilo en una unidad.

**Cambios:**
1. **`PROCESO-MAESTRO.md` bloque `nc1-reciclaje.json`** reescrito al modelo de hilos: top-level `hilos[]`, schema por hilo y por evento, acciones válidas (introduce/amplia/aplica/sistematiza/contrasta), multiplicidad permitida (varios eventos del mismo hilo en una unidad), endpoint `/api/reciclaje`.
2. **`REVIEW.md` B2a + tabla de artefactos** alineados con el estado real: B2a.1 (pase 1) ✅ cerrado v10.92; B2a.2 (pase 2 contra inventarios) abierto. Tabla de artefactos refleja "9 hilos / 23 eventos" en lugar de "esqueleto vacío".
3. **`REVIEW.md` referencias a endpoints** corregidas: `/api/global/<tipo>` (que no existe) → `/api/reciclaje` ya operativo; `/api/tarjetas` y `/api/pildoras` quedan pendientes.
4. **Decisión schema:** se permiten múltiples eventos del mismo hilo en la misma unidad (ej. una unidad puede `amplia` y `aplica` un mismo hilo simultáneamente). Documentado en PROCESO-MAESTRO.
5. **`web/index.html` timeline** corregida: indexa eventos por unidad como **lista**, no como dato único. Si una unidad tiene N eventos del mismo hilo, se renderizan los N puntos uno al lado del otro en su columna. Sin colapso silencioso.

**Sin cambios en datos.** 9 hilos / 23 eventos siguen igual; el JSON pase 1 ya cumple "máximo 1 evento por hilo+unidad" pero el schema y la viz ya soportan más para el pase 2.

---

## [v10.92 — 2026-05-09] — B2a (pase 1): primera población de `nc1-reciclaje.json` con modelo de hilos + vista en dashboard

**Refinamiento del schema cerrado en B1.5.** El modelo punto-a-punto (`reciclajes_por_unidad` con entradas `origen → destino`) era insuficiente para representar dos realidades editoriales:
1. **Fan-out:** un mismo contenido se ramifica en varias unidades (ej. números: U0→U1→U2→U3 como un único hilo, no 3 reciclajes sueltos).
2. **Cascada:** las ramificaciones se acumulan; lo que U3 recicla "de U1" en realidad ya pasó por U2.

**Schema nuevo:** `hilos[]` reemplaza `reciclajes_por_unidad`. Cada hilo es un contenido con identidad propia (`id`, `titulo`, `tipo`) y una secuencia de `eventos` por unidad con `accion` (introduce | amplia | aplica | sistematiza | contrasta), `seccion`, `descripcion`, `impacto`.

**Pase 1 generado** cruzando `nc1-curso.json` (sin abrir inventarios todavía):
- 9 hilos detectados: números, alfabeto, léxico de aula, países hispanohablantes, presente de indicativo, género/número, info personal, saludos, interrogativos.
- 23 eventos repartidos en U0/U1/U2/U3.
- Cada hilo lleva `nivel_analisis: "mapa"` para distinguirlo del pase 2 (que validará contra inventarios y añadirá vocabulario complementario de frecuencia).

**Dashboard:**
- Nueva ruta `/api/reciclaje` en `diagrama.py` (función `get_reciclaje`).
- Nuevo botón **RECICLAJE** en sidebar de `web/index.html`.
- Vista **línea de tiempo**: cada hilo es una barra horizontal con puntos en U0..U9 coloreados por acción (azul=introduce, verde=amplia, naranja=aplica, morado=sistematiza, rosa=contrasta). Click en punto o título abre drawer lateral con la trayectoria completa del hilo.
- Agrupación por tipo (vocabulario, forma_verbal, contenido_gramatical, estrategia_comunicativa) con border de color.

**Pendiente (pase 2):** validación de cada hilo contra los inventarios reales de U1/U2/U3 + adición del vocabulario complementario de frecuencia que el índice oficial no captura.

**Sin cambios funcionales en JSONs de inventario.** Validador U0/U1/U2/U3 → 0/0.

---

## [v10.91c — 2026-05-09] — Alineación operativa de B2a: U1/U2/U3 como scope unificado

Hallazgo del revisor sobre v10.91/v10.91b: el CHANGELOG anunciaba B2a con scope "U1/U2/U3" pero `REVIEW.md` (B2a + tabla de artefactos) y `PROCESO-MAESTRO.md` (resumen vivo) seguían diciendo "U1 y U2". Doble verdad operativa.

**Decisión cerrada con autor:** B2a (primera población de `nc1-reciclaje.json`) cubre U1, U2 y U3 — las 3 unidades trackeadas en main. U0 queda fuera por ser unidad atípica sin unidades anteriores que reciclar.

**Cambios:**
- `REVIEW.md` línea 48 (estado vivo bloque B), líneas 165-166 (B2a acción + gate), línea 431 (tabla artefactos).
- `PROCESO-MAESTRO.md` línea 699 (resumen vivo bloque B).

**Sin cambios funcionales.** Validador 0/0.

---

## [v10.91b — 2026-05-09] — Saneo documental post-v10.91: alineación de 3 referencias vivas

Hallazgos del revisor sobre v10.91: la integración funcional de U3 era correcta, pero 3 referencias vivas seguían en el escenario previo y contradecían el estado real:

1. **`nc1-curso.json:_nota`** — declaraba la divergencia 32-41 vs 34-43 como deuda técnica abierta. Actualizada: deuda saldada en v10.91.
2. **`REVIEW.md` estado vivo + tabla de artefactos** — U3 figuraba como borrada y U2 como solo working tree con errores. Ambas corregidas: U2 trackeada (v10.87), U3 reintegrada (v10.91), U4 como nueva extracción en worktree.
3. **`PROCESO-MAESTRO.md` protocolo ejecutor 2** — anclaba U3 como ejemplo de unidad fuera de main. Generalizado a U4/U5; U3 anotada como caso ya cerrado siguiendo el mismo protocolo.

**Sin cambios en JSONs de inventario.** Validador 0/0 sobre U0/U1/U2/U3.

---

## [v10.91 — 2026-05-09] — Integración de U3 a main (worktree extract/U3)

**Segunda integración del carril paralelo de extracciones** tras U2 (v10.87). El JSON fue re-extraído en el worktree `extract/U3` con el PDF correcto (páginas 32-41) tras el borrado del JSON erróneo en v10.88.

**Datos de U3:**
- 10 páginas (32-41), 47 actividades, 4 cuadros.
- Título: "La Familia". Contrato post-refactor (taxonomía 20 + destreza/enfoque, schema cuadros).
- Validador: 0 errores / 0 avisos.

**Estado de main post-integración:**
- Unidades trackeadas validando 0/0: U0, U1, U2, U3 (reintegrada).
- La deuda técnica de paginación anotada en `nc1-curso.json:_nota` queda saldada.

**Próximo:** B2a (primera población de `nc1-reciclaje.json` con U1/U2/U3).

---

## [v10.90 — 2026-05-08] — Saneo documental post-v10.89: REVIEW alineado, protocolo ejecutor 2, comando dashboard

**6 frentes corregidos:**

1. **REVIEW.md estado vivo (línea 48):** B1.5 ya no figura "en diseño" — marcado ✅ cerrado con referencia a v10.89. `nc1-reciclaje.json` ya no aparece como pendiente en la tabla de artefactos.
2. **REVIEW.md bloque B2 reescrito:** desacoplado de U3. Dividido en B2a (reciclaje, desbloqueado), B2b (tarjetas, bloqueado) y B2c (píldoras, bloqueado). U3 queda explícitamente fuera de main hasta nueva integración.
3. **REVIEW.md tabla artefactos:** U3 reflejada como borrada (v10.88, PDF erróneo, re-extracción en worktree `extract/U3`).
4. **PROCESO-MAESTRO.md resumen vivo (línea 676):** B1.5 marcado ✅; B2a desbloqueado.
5. **PROCESO-MAESTRO.md protocolo ejecutor 2 añadido** (zona operativa, antes de §27): worktree dedicado, validación con venv principal, revisión en dashboard con `EXTRA_UNIDADES_PATHS`, sin tocar main, integración posterior con receta `--no-ff --no-commit`.
6. **README.md §2 "Arrancar el dashboard":** comando oficial documentado para main solo y para worktrees paralelos con `EXTRA_UNIDADES_PATHS` (U3+U4 como ejemplo).
7. **web/index.html línea 575:** ruta obsoleta `viejo/unidades/UXX/` corregida a `unidades/UX/`.

**Sin cambios en JSONs de inventario. Validador U0/U1/U2 → 0/0. U3 en worktree paralelo.**

**Próximo:** B2a — primera población de `nc1-reciclaje.json` con reciclajes de U1 y U2.

---

## [v10.89 — 2026-05-08] — B1.5 cerrado: contrato de `nc1-reciclaje.json` + esqueleto vacío creado

**Decisión cerrada con autor:** schema completo de `nc1-reciclaje.json` cerrado en B1.5. Las 4 preguntas abiertas se resolvieron:

- **Disparadores:** criterio de conexión natural adoptado de `viejo/marco-teorico-metodologico.md` §6 — entra un contenido si refuerza o es requisito del contenido nuevo. Proceso de análisis de 4 pasos. No se recicla todo; máximo 5-6 elementos de mayor impacto por unidad.
- **Campo `origen`:** objeto `{ "unidad": N, "seccion": "..." }` — unidad + sección canónica del libro (vocabulario, gramatica, comunicacion, destrezas, cultura, pronunciacion_ortografia, para_aprender).
- **`indice_por_tipo`:** objeto con tipo como clave, valores = lista de IDs de entradas. Los 5 tipos cerrados arrancan con lista vacía.
- **Estado inicial:** archivo creado vacío en B1.5; primera población en B2 con U1 y U2.

**Archivos modificados:**
- `unidades/nc1-reciclaje.json` — creado (esqueleto vacío).
- `PROCESO-MAESTRO.md` — bloque `nc1-reciclaje.json` ampliado con decisiones de origen, indice_por_tipo y criterio de disparador.
- `REVIEW.md` — B1.5 marcado ✅ cerrado.
- `docs/actual/B1.5-contrato-reciclaje.md` — documento de trabajo (se mueve a historico).

**Sin cambios en JSONs de inventario.** Validador U0/U1/U2 → 0/0; U3 pendiente de re-extracción.

**Próximo:** B2 (primera población de `nc1-reciclaje.json` con U1 y U2).

---

## [v10.88 — 2026-05-08] — Borrado de `unidades/U3/U3-nc1-inventario.json` (PDF erróneo, pendiente de re-extracción)

**Decisión cerrada con autor:** el PDF de U3 que se había usado para la extracción inicial contenía errores (paginación divergente con el Scope and Sequence oficial: Scope dice U3=32-41; el inventario decía 34-43; ver decisión 35 en PROCESO-MAESTRO Parte 4 y deuda técnica anotada en `nc1-curso.json:_nota`).

**Acción:** el autor proporciona el PDF correcto y borra el JSON viejo. Main queda temporalmente sin inventario de U3 hasta la re-extracción.

**Estado:**
- `unidades/U3/U3-nc1-inventario.json` → borrado (esta versión).
- `unidades/U3/fuente/U3-nc1.pdf` → reemplazado por el correcto (gitignored, no entra al commit).

**Próximo:** worktree `extract/U3` + chat nuevo para que el ejecutor 2 re-extraiga la unidad con el contrato post-refactor (taxonomía 20, destreza/enfoque, schema cuadros con `texto_intro`/nullable, etc.).

**Sin cambios funcionales en código.** Validador sobre U0/U1/U2 → 0/0; U3 ahora "no existe" hasta la re-extracción.

---

## [v10.87 — 2026-05-08] — Integración de U2 a main (merge `extract/U2`)

**Primera integración del carril paralelo de extracciones** desde la apertura del modelo de worktrees (post v10.79). Sigue la receta acordada con el revisor (`git merge --no-ff --no-commit` + edición de archivos vivos compartidos + commit único).

**Contenido integrado:** `unidades/U2/U2-nc1-inventario.json` extraído por el ejecutor 2 en su worktree paralelo (`extract/U2`), validando 0/0 con el contrato post-refactor (taxonomía 20 + destreza/enfoque, schema §4 con `texto_intro`/`titulo` nullable/`lista_reglas`).

**Datos de U2:**
- 10 páginas (22-31), 52 actividades, 6 cuadros.
- Contenido: vocabulario de países hispanohablantes, ser/tener plurales, demostrativos, los números 21-100, las vocales fonéticas, ESO en España, etc.
- Inventario se ajusta al índice oficial del libro (`nc1-curso.json`).

**Hallazgos cerrados antes de la integración:**
- 7 correcciones del extractor original aplicadas (horario, cuadro ordinales eliminado, "tenemos" en p24-act02, Pierre Curso completo, cuadro mayúsculas con `texto_intro`, palabras_recuadro en p30-act03 eliminado, globo 3 con 11 letras corregido).
- 5 refinamientos de regla derivados (v10.83-v10.86): bifurcación "Para aprender", schema cuadros con `texto_intro`/`titulo` nullable/`lista_reglas`, `responder_preguntas_abiertas` con destreza condicional, distinción individual vs parejas.
- 1 verificación final aplicada en worktree (commit `155838f`): U2-p29-act04 destreza corregida a `[expresion_escrita]` tras confirmar contra PDF (escribe individual, no oral).

**Estado de main post-integración:**
- Unidades trackeadas validando 0/0: U0, U1, U2 (nuevo), U3.
- Worktree `extract/U2` y rama `extract/U2` se mantienen intactos hasta que el autor decida limpiarlos.
- Variable `EXTRA_UNIDADES_PATHS` del dashboard puede retirarse o dejarse (la lógica `main gana sobre extras` hace que U2 ahora se sirva desde main).

**Próximo:** B1.5 (diseño de `nc1-reciclaje.json`) en este chat (ejecutor 1); re-extracción de U3 cuando el autor proporcione PDF correcto (ejecutor 2 en nuevo worktree).

---

## [v10.86 — 2026-05-08] — Refinamiento §2.2 regla 3: distinción individual vs parejas en respuesta a preguntas

**Caso disparador** (riesgo residual del revisor sobre v10.85): si U2-p29-act04 resulta ser intercambio en parejas, no solo cambia la destreza, sino también el `tipo` (de `responder_preguntas_abiertas` a `interaccion_oral`). La regla §2.2 punto 3 actual no hacía explícita la distinción individual vs parejas.

**Decisión cerrada con autor:** refinar §2.2 regla 3 para que distinga 3 casos en lugar de 2:
- Respuesta concreta del input → `responder_preguntas_cerradas`.
- Respuesta personal/libre **individual** → `responder_preguntas_abiertas`.
- Respuesta personal/libre **en parejas** → `interaccion_oral` (la interacción con compañero prevalece).

**Cambio quirúrgico** (1 bullet añadido, 1 modificado, 0 párrafos nuevos):

```
- Respuesta personal/libre del alumno, individual (sin compañero) → responder_preguntas_abiertas.
- Respuesta personal/libre en parejas → interaccion_oral. Destreza: [interaccion_oral].
```

**Por qué refinar la regla en lugar de documentar un árbol de decisión aparte:** la regla precisa hace innecesaria la documentación adicional. Respeta el principio del autor de no engordar docs. Single source of truth de la decisión sigue en `reglas-operativas.md` §2.2.

**Sin cambios en JSONs.** La aplicación a U2-p29-act04 sigue pendiente de verificación contra PDF (worktree de U2). Las preguntas a verificar ahora son **dos**:
- ¿Solo o en parejas? (Si parejas → tipo `interaccion_oral`)
- ¿Escribe o habla? (Solo aplica si individual, decide la destreza)

**Validador U0/U1/U3 → 0/0.**

**Próximo:** verificar U2-p29-act04 contra PDF e integrar U2 a main.

---

## [v10.85 — 2026-05-08] — Refinamiento §2.3: `responder_preguntas_abiertas` con destreza condicional al enunciado del libro

**Caso disparador** (hallazgo C en U2-p29-act04 durante revisión del worktree de U2): la regla §2.3 decía que `responder_preguntas_abiertas` con respuesta personal/libre → `expresion_escrita` por defecto. Pero en algunos casos del libro la respuesta es oral (en parejas, en clase). Asumir `expresion_escrita` siempre es impreciso.

**Decisión cerrada con autor:** la destreza depende de lo que pida el enunciado real del libro:
- Si el libro pide escribir → `expresion_escrita`.
- Si el libro pide responder oralmente → `expresion_oral`.

**Cambio quirúrgico en `reglas-operativas.md` §2.3** (1 línea modificada, 0 párrafos añadidos):

Línea 68:
- **Antes:** *"Respuesta personal/libre del alumno, sin texto-fuente → `responder_preguntas_abiertas`. Destreza: `expresion_escrita` (es contenido propio)."*
- **Después:** *"Respuesta personal/libre del alumno, sin texto-fuente → `responder_preguntas_abiertas`. Destreza: `expresion_escrita` si el libro pide escribir; `expresion_oral` si el libro pide responder oralmente. Verificar contra el enunciado real."*

**Sin cambios en JSONs.** La aplicación a U2-p29-act04 concreta queda pendiente de verificación contra PDF (worktree de U2). U0/U1/U3 siguen validando 0/0; sus actividades de `responder_preguntas_abiertas` ya cumplen con el criterio (escritura).

**Próximo:** verificar PDF de U2-p29-act04 y aplicar el cambio si procede; integrar U2 a main.

---

## [v10.83b — 2026-05-08] — Cierre limpio de v10.83: alineación de 2 referencias vivas

Hallazgo del revisor sobre v10.83: la regla nueva quedó bien en `reglas-operativas.md` §1+§4, pero 2 referencias vivas seguían diciendo "Para aprender → siempre actividad" sin la bifurcación, contradiciendo v10.83 desde otros entry points.

**Sitios alineados:**

1. **`prompt.md:54`** (descripción de qué contiene `reglas-operativas.md`): decía *"...criterios de tipo y tipo_cuadro, 'Para aprender' → actividad / 'Observa' → nota, reglas de población..."*. Reescrito a *"...criterios de tipo y tipo_cuadro, criterios para 'Para aprender' y 'Observa', reglas de población..."*. La descripción **nombra** los criterios sin reducirlos a una formulación; la regla canónica vive en `reglas-operativas.md` §4.

2. **`convenciones-y-casos.md:141`** (sección 4.1, caso histórico): decía *"'Para aprender' es una actividad. Esta es la corrección que diferencia los dos elementos."* Reescrito para reflejar que el caso histórico citado tenía verbo imperativo (con tarea), y que la regla actual bifurca: *"con verbo imperativo → actividad; solo informativa → cuadro"*.

**Single source of truth restablecida**: la regla "Para aprender" tiene una sola definición canónica en `reglas-operativas.md` §4. Los demás archivos solo apuntan a ella, sin reformularla ni contradecirla.

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

**Próximo:** decidir hallazgos C-D del worktree de U2 e integrar U2 a main.

---

## [v10.84 — 2026-05-08] — Schema §4 (cuadros): `texto_intro` documentado + `titulo` nullable + `lista_reglas`

**Hallazgos del ejecutor 2 en U2 que motivan este cambio:**
1. Cuadros tipo lista de reglas (U2-p25 mayúsculas, U2-p29 mayúsculas) tienen un encabezado verbatim antes de la lista que el ejecutor 2 capturó como `texto_intro`. El schema lo permitía implícitamente (`contenido` es estructura libre), pero no lo documentaba como campo canónico — riesgo de divergencia entre extractores futuros.
2. El cuadro de U2-p29 no tiene título visible en el libro. El schema decía `"titulo": <str>` sin marcar nullable, dejando ambiguo el caso real.
3. El tipo `lista_reglas` aparecía implícitamente en U2 pero no estaba en la lista de ejemplos del schema.

**Cambios quirúrgicos en `schema-inventario.md` §4** (3 líneas modificadas, 1 nueva, 0 párrafos añadidos):
- `"titulo": <str>` → `"titulo": <str | null>` con comentario aclarando cuándo es null.
- En `"tipo"`: añadido `lista_reglas` a la lista de ejemplos.
- **Línea nueva**: `"texto_intro": <str opcional — encabezado introductorio antes de listas o tablas>`.

**Resuelve 3 cosas en un commit:**
- Documenta `texto_intro` como campo canónico.
- Cierra el hallazgo A previo (cuadro p29 sin título → `null` legítimo).
- Documenta `lista_reglas` como tipo válido (ya en uso de facto).

**Sin cambios funcionales en código** (`contenido` es estructura libre, el validador no chequea esos campos). Validador U0/U1/U3 → 0/0.

**Próximo:** decidir hallazgos C-D (oral vs escrita en U2-p29-act04, tipo busqueda_informacion en U2-p29-act07) e integrar U2 a main.

---

## [v10.83 — 2026-05-08] — Refinamiento de regla "Para aprender" tras dictamen del ejecutor 2 en U2

**Caso disparador** (extracción de U2 por ejecutor 2): el bloque "Para aprender — Uso de las mayúsculas" en U2-p25 es **puramente informativo** (lista de reglas con ejemplos, sin instrucción al alumno). La regla §1 regla 2 + §4 actuales decían "siempre actividad", lo que forzaba clasificación incorrecta.

**Decisión cerrada con autor:** bifurcar "Para aprender" según naturaleza:
- **Con tarea** (verbo imperativo al alumno): actividad (`tipo: produccion_escrita_guiada`, `datos.subtipo: "para_aprender"`).
- **Solo informativa** (sin verbo imperativo): cuadro con `tipo_cuadro` apropiado.

**Cambios en `reglas-operativas.md`** (reformulación, no añadido — respeta principio del autor de no engordar docs):

- **§1 regla 2 reescrita** como índice corto + puntero a §4 (mismo tamaño que antes; antes redirigía a "siempre actividad" sin matizar).
- **§4 reescrita** absorbiendo la bifurcación en una tabla con criterio decisional explícito + ejemplos canónicos de cada caso (con tarea: U3-p37 "Hacer un cuaderno de vocabulario"; solo informativa: U2-p25 "Uso de las mayúsculas"). Eliminada la duplicación previa entre §1 y §4. **§4 ahora es source of truth única**; §1 es índice.

**Auditoría aplicada a U0/U1/U3** antes de aplicar la regla:
- U0: sin "Para aprender" extraídos (atípica). Sin cambios.
- U1: sin "Para aprender" extraídos como actividad/cuadro, aunque el índice del libro tiene "Recursos para la clase" — gap del inventario, fix futuro de extracción de U1, no afecta a esta serie.
- U3: 1 caso (`U3-p37-act09 "Mira el cuaderno de Ronaldo... Escribe palabras nuevas y tradúcelas"`) con verbos imperativos al alumno → actividad legítima con tarea. **Sin cambios** necesarios.

**Sin reclasificaciones aplicadas**: la regla nueva confirma las clasificaciones existentes. La aplicación efectiva ocurre en U2 (en su worktree) que ya implementa la bifurcación.

**Sin cambios funcionales en código.** Validador U0/U1/U3 → 0/0.

**Próximo:** v10.84 (schema §4: documentar `texto_intro` + `titulo` nullable + `lista_reglas`).

---

## [v10.82b — 2026-05-08] — Refinamiento de B1.4 tras dictamen del revisor

**2 hallazgos del revisor sobre v10.82:**

**1. Schema documentado ≠ JSON real.** La decisión 35 y la sección B1.4 de REVIEW describían el apéndice como `título + página inicio` y un top-level cerrado, pero el archivo real usa `seccion` (no `titulo`) y añade un `_nota` top-level no documentado.

**Fix:**
- Decisión 35 (Parte 4) reescrita para reflejar el schema real: `seccion` en apéndice, `_nota` documentado como campo top-level opcional.
- B1.4 en REVIEW.md actualizado en consonancia.

**2. Cierre de B1.4 contradice su propia regla de source of truth.** La decisión 35 decía que cualquier divergencia entre `nc1-curso.json` y los inventarios per-unidad es bug "antes del cierre", pero el repo cerró con divergencias conocidas:
- U3 paginación: nc1-curso.json dice 32-41 (Scope and Sequence); inventario de U3 dice 34-43.
- U1 y U3 mezclan "PARA APRENDER" en `contenidos_indice.gramatica`.

**Causa identificada** (input del autor): el PDF actual de U3 tiene errores; la unidad se re-extraerá por el ejecutor 2 en un worktree paralelo cuando el autor proporcione un PDF correcto.

**Fix:** decisión 35 reformulada en su cláusula de source of truth:
> *`nc1-curso.json` es canónico para el índice editorial del curso. Los `paginas_libro` y `contenidos_indice` per-unidad pueden divergir legítimamente cuando el libro tiene portadas/separadores no extraídos o el PDF disponible no coincide con la edición oficial. Las divergencias se anotan como deuda técnica conocida en `_nota` y no bloquean el cierre de B1.4 ni de B1.5; se resuelven cuando se actualice el inventario afectado.*

**Cambios aplicados:**
- `PROCESO-MAESTRO.md` decisión 35: schema real documentado + regla source of truth refinada.
- `REVIEW.md` B1.4: schema real documentado + hallazgo U3 ampliado con causa y plan.
- `unidades/nc1-curso.json` `_nota` ampliado para listar las 2 deudas técnicas conocidas (U3 paginación, U1/U3 mezcla "PARA APRENDER").

**No se toca el JSON de U3 ni su PDF.** El autor los reemplazará después y el ejecutor 2 re-extraerá la unidad en un worktree paralelo.

**Sin cambios funcionales en código.** Validador U0/U1/U3 → 0/0.

**Próximo:** B1.5 (diseño de `nc1-reciclaje.json`) con base documental ahora coherente.

---

## [v10.82 — 2026-05-08] — B1.4 cerrado: creado `unidades/nc1-curso.json` (índice editorial global del curso)

**Objetivo del paso:** disponer del índice editorial canónico del curso "Nuevo Compañeros 1" como artefacto JSON consultable, antes de diseñar `nc1-reciclaje.json` (B1.5). Sin un mapa global de "qué enseña cada unidad", el reciclaje no se puede mapear con trazabilidad.

**Fuente:** índice oficial del libro impreso (Scope and Sequence, páginas 6-7), facilitado por el autor como imágenes en chat. **No se usa** `viejo/00-curso-general.md` como fuente — ese archivo tenía datos imprecisos en páginas (U1=10-23 y U2=14-33 se solapaban) y mezclaba dato editorial con metadocumentación pedagógica.

**Schema cerrado** (registrado como **decisión 35** en `PROCESO-MAESTRO.md` Parte 4):
- Path canónico: `unidades/nc1-curso.json`.
- Top-level: `curso` ("nc1"), `titulo`, `editorial`, `nivel` ("A1.1"), `fuente`, `estructura_libro`, `unidades` (array), `apendice` (array).
- **Por unidad regular** (U1-U9): campos top-level `vocabulario` (lista), `gramatica` (lista), `para_aprender` (string o `null`), `pronunciacion_ortografia` (string), `comunicacion` (lista), `destrezas` (lista), `cultura` (lista), más `pagina_inicio` y `paginas_libro`.
- **Por U0** (Punto de partida, atípica): solo `contenido_general` (lista).
- **Apéndice**: solo metadatos (título + `pagina_inicio`); contenido detallado fuera de alcance por ahora.
- **Contenido de las celdas**: **literal del índice del libro**, sin expansión MCER ni interpretación pedagógica añadida.

**Datos extraídos** del índice oficial:
- 10 unidades (U0 + U1-U9) con todos sus campos.
- Páginas correctas: U1=12-21, U2=22-31, U3=32-41, U4=42-51, U5=52-61, U6=62-71, U7=72-81, U8=82-91, U9=92-101 (10 páginas exactas por unidad regular).
- Apéndice: Glosario (102), Resumen Gramatical (107), Transcripciones (112).

**Hallazgos anotados (no bloqueantes):**
- Los `contenidos_indice` ya extraídos en `unidades/U1/...inventario.json` y `unidades/U3/...inventario.json` mezclan "PARA APRENDER" dentro del campo `gramatica` (ej. U3: "Hacer un cuaderno de vocabulario" aparece en gramática cuando es una estrategia metacognitiva separada). Anotado como **fix futuro de los inventarios**; no bloquea B1.4 ni B1.5.
- Single source of truth con `nc1-curso.json` y los `contenidos_indice` per-unidad: cualquier divergencia futura es bug que se resuelve antes del cierre.

**Sin validador estructural propio** todavía. Se decidirá si añadir checks a `scripts/validar_inventario.py` cuando aparezca el primer caso real de divergencia.

**Próximo:** B1.5 (diseño de `nc1-reciclaje.json`) ahora con `nc1-curso.json` ya disponible para mapear los flujos de reciclaje entre unidades.

---

## [v10.81 — 2026-05-08] — Dashboard: badge "extracción en curso" en lugar de path absoluto para unidades de worktrees paralelos

**Problema visual tras v10.79:** las tarjetas de inventarios mostraban el path del JSON. Para unidades en main, el path era relativo y corto (`unidades/U2/U2-nc1-inventario.json`). Para unidades de worktrees paralelos (vía `EXTRA_UNIDADES_PATHS`), el path absoluto largo aparecía sin contexto, dando una apariencia de error visual cuando en realidad indicaba un estado válido (extracción no integrada todavía).

**Fix:** en la lista de inventarios, si `zona === "extra"`, se muestra un badge informativo *"🔄 Extracción en curso (worktree paralelo)"* en lugar del path. Para unidades en main (`zona === ""`), se mantiene el path relativo como antes.

**Comportamiento al integrar una unidad a main:** automático. La API empieza a devolver `zona: ""` para esa unidad (main gana sobre extras), el badge desaparece y la tarjeta vuelve a mostrar el path relativo. Sin tocar código.

**Cambios en `web/index.html`:**
- `loadInventarios()`: render condicional según `u.zona`. Badge ámbar para extras, path monoespaciado para main.

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

---

## [v10.80b — 2026-05-08] — Dashboard: eliminado el badge de versión (uno solo, el de la derecha)

**Decisión del autor tras v10.80:** v10.80 había hecho el badge dinámico para resolver el desfase, pero seguían apareciendo **dos indicadores de versión** (badge verde a la izquierda + indicador `vX — hh:mm:ss` a la derecha). Decisión: dejar solo el indicador derecho, que ya muestra versión + hora viva. El badge era redundante.

**Cambios en `web/index.html`:**
- Eliminado el `<span id="version-badge">` del header.
- Eliminada la línea JS que actualizaba `version-badge.textContent` en `init()`.
- `serverVersion` se sigue cargando desde `/api/version` y se sigue mostrando en el indicador derecho via `updateStatus()`.

**Resultado:** una sola fuente visible de versión en el dashboard, sin posibilidad de desfase entre dos elementos.

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

---

## [v10.80 — 2026-05-08] — Dashboard: badge de versión dinámico (fix doble visualización)

**Problema detectado tras v10.79:** el header del dashboard mostraba dos versiones distintas. El badge verde (`v10.78`, hardcoded en `web/index.html` desde v10.78) y el indicador `v10.79 — hh:mm:ss` (dinámico desde `/api/version`). Origen: el badge se añadió como string literal, no como elemento dinámico.

**Fix:** badge convertido a `id="version-badge"` con texto inicial `v?.??` que se rellena en `init()` desde la respuesta de `/api/version`. Una sola fuente de verdad (`CHANGELOG.md` → `_read_version()` → `/api/version`).

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

---

## [v10.79 — 2026-05-08] — Dashboard: variable `EXTRA_UNIDADES_PATHS` para servir worktrees paralelos

**Problema resuelto:** durante extracciones paralelas, el JSON de la unidad en curso vive en un worktree separado (ej. `extract/U2`), no en `main`. El dashboard de main no veía esos JSONs porque solo escaneaba su propia carpeta `unidades/`.

**Solución:** variable de entorno `EXTRA_UNIDADES_PATHS` con paths adicionales a escanear (separador `:` estilo PATH). El dashboard fusiona inventarios de `unidades/` + paths extra. **Main tiene prioridad**: si una unidad existe en main, no se sobreescribe desde un path extra. Las unidades que solo están en paths extra se marcan con `zona='extra'`.

**Uso:**

```bash
EXTRA_UNIDADES_PATHS=/Users/.../guia-didactica-extract-U2/unidades python3 diagrama.py
```

**Cambios en `diagrama.py`:**
- Nueva función `_extra_unidades_paths()` (lee env var, valida existencia).
- `list_inventarios()` fusiona main + extras (main gana ante colisión).
- `get_inventario()` busca en main → extras como fallback.
- `_scan_zona()` tolera paths fuera de `PROJECT` usando absoluto cuando `relative_to(PROJECT)` falla.

**Ventajas:**
- Una sola URL (`localhost:8080`), una sola instancia.
- Refrescar el navegador muestra cambios del worktree paralelo en tiempo real.
- Cuando la unidad se integra a main, automáticamente pasa a verse desde main.
- Sirve para cualquier worktree de extracción futuro.

**Sin cambios en código de fase 1, schema, validador ni archivos de extracción.** Validador U0/U1/U3 → 0/0.

---

## [v10.78 — 2026-05-08] — Dashboard: enfoque visible en inventarios + badge de versión

- `web/index.html`: campo `enfoque` ahora se muestra en cada actividad de la vista Inventarios (debajo de Destreza).
- `web/index.html`: `destreza` renderiza correctamente cuando es array (valores separados por `·`).
- `web/index.html`: badge de versión `v10.78` visible en el header del dashboard.

---

## [v10.77c — 2026-05-07] — Cierre administrativo: corrección recursiva de meta-drift en v10.77b

Hallazgo del revisor sobre v10.77b: el propio micro-fix de v10.77b reprodujo el problema que estaba arreglando. El commit real de v10.77b fue `2026-05-07 19:55:26 +0200`, pero las nuevas referencias ancladas a `19:25 / commit 40c8a4c` quedaron desactualizadas el momento mismo del commit.

**Causa estructural:** cualquier acta que pretenda capturar "el momento real de su propio commit" entra en bucle: el commit aún no existe cuando se redacta el acta.

**Convención explicitada en este commit (v10.77c):**

> El campo *"Última actualización"* en cabeceras de archivos vivos apunta al **último commit consolidado de cierre de serie**, no al commit en curso. Las entradas de bitácora describen el commit que las introduce con timestamp aproximado al momento real del commit.

**Fixes aplicados:**

- `REVIEW.md:9`: cabecera ahora apunta a `becaa69` (v10.77b) como cierre real de la serie de limpieza, con timestamp `19:55`.
- `REVIEW.md:434`: entrada de v10.77b corregida a `19:55` con commit `becaa69` citado.
- `PROCESO-MAESTRO.md:661`: entrada de v10.77b corregida a `19:55`, citando ambos commits relevantes (commit principal `40c8a4c` y commit final `becaa69`).

**Decisión consciente:** este commit v10.77c **NO se auto-documenta como nueva "última actualización"** porque eso reabriría el bucle. La cabecera de REVIEW.md sigue apuntando a `becaa69`. Si en el futuro se introduce una nueva edición sustantiva, esa edición será la que actualice la cabecera.

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

**Cierre administrativo de la serie v10.72-v10.77c.** Base documental coherente; cierre de la serie y apertura del carril de extracciones paralelas sujetos a validación final del revisor.

---

## [v10.77b — 2026-05-07] — Micro-fix de 2 imprecisiones tras dictamen del revisor sobre v10.77

Hallazgos del revisor sobre v10.77 (`40c8a4c`):

**1. Timestamp ficticio en cabeceras y actas.** El acta v10.77 declaraba que los timestamps se pusieron "al momento real del commit", pero usé `14:00` cuando el commit real fue `2026-05-07 19:20 +0200` (verificado con `git log -1 --format='%ci'`). 14:00 era hora estimada de cierre de trabajo, no del commit. Imprecisión factual en 4 sitios:
- `REVIEW.md:9`
- `REVIEW.md:434` (entrada de bitácora del commit)
- `PROCESO-MAESTRO.md:660` (entrada de bitácora del documento)
- `CHANGELOG.md:24` (texto del acta)

**Fix:** sustituido `14:00` por `19:20` en los 4 sitios con referencia al commit `40c8a4c` para trazabilidad. La cabecera de REVIEW conserva ahora `19:20 (commit 40c8a4c, v10.77)`.

**2. Árbol vivo incompleto.** En `PROCESO-MAESTRO.md:472` (vista viva del árbol del repo) el bloque `docs/historico/` no listaba el archivo nuevo `REVIEW-bloque-A-cerrado.md` creado en el mismo commit v10.77.

**Fix:** añadida la entrada al árbol con su descripción.

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

**Cierre real de la serie v10.72-v10.77.** Tras este micro-fix, las cabeceras y bitácoras describen fielmente lo que dicen describir (momento real del commit anterior + estado físico real del repo).

---

## [v10.77 — 2026-05-07] — Compactación del Bloque A cerrado de REVIEW + 3 cabeceras desincronizadas

Última pieza de la limpieza documental tras v10.74-v10.76b. El Bloque A de REVIEW.md ("Estabilizar la fase 1") está totalmente cerrado desde 2026-05-07 (A1, A2, A3, A4 todos en ✅). Su detalle ejecutable (sub-pasos A4.0-A4.6, gates, riesgos, plan completo) ya solo aporta valor histórico; mantenerlo en REVIEW vivo cargaba ~8K chars sin contrapartida operativa.

**Decisión informada según receta del revisor** (4 ajustes sobre el plan inicial):

1. Corte por encabezado, no por número de línea (robustez ante reescrituras superiores).
2. Timestamps en cabeceras al momento real del commit, no al de la última bitácora previa.
3. Reformular `PROCESO-MAESTRO.md:648` para no afirmar que el detalle vive en REVIEW (ya no lo hace).
4. En el archivo histórico, no decir "bitácora completa archivada": la bitácora cronológica general del documento sigue viva en REVIEW.

**Cambios aplicados:**

- **Extracción literal del Bloque A** (líneas con `## Bloque A` hasta antes de `## Bloque B`, 99 líneas, 8.022 chars) a `docs/historico/REVIEW-bloque-A-cerrado.md` (111 líneas con cabecera explicativa). Sin reescribir.
- **Sustitución en REVIEW vivo** por resumen de 12 líneas con: estado de los 4 sub-pasos, resultado vivo (U0/U1/U3 0/0, 5 archivos operativos, validador alineado), referencia al archivo histórico, mención del merge `110e722` y aclaración de que la bitácora cronológica general permanece viva.
- **Cabeceras desincronizadas absorbidas en este commit** (condición pragmática del revisor):
  - `REVIEW.md:9`: "Última actualización: 2026-05-07 03:15" → momento del commit (corregido a `19:20` en v10.77b tras detectar imprecisión).
  - `PROCESO-MAESTRO.md:448`: "Última actualización: 2026-05-05" → "2026-05-07 (limpieza documental v10.72-v10.77...)".
  - `PROCESO-MAESTRO.md:630`: "actualizado 2026-05-05 19:00" → "actualizado 2026-05-07".
- **Reformulación de `PROCESO-MAESTRO.md:648`** ("Detalle vivo y bitácora en REVIEW.md" → "Resumen vivo en REVIEW sección Bloque A; detalle íntegro archivado en docs/historico/...; bitácora cronológica general permanece viva en REVIEW.md").

**Resultado medido:**
- REVIEW.md: 580 → 493 líneas (-15%, ~2K tokens menos en la parte viva).
- Detalle del Bloque A preservado íntegro en histórico (111 líneas).

**No se toca:**
- Bloques B-E vivos en REVIEW.
- Bitácora cronológica general de REVIEW (línea 521+).
- Bitácora del documento de PROCESO-MAESTRO.
- Referencias históricas a líneas o a "17 tipos" en bitácoras y actas anteriores (intocables, revisionismo prohibido).

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

**Cierre de la serie de limpieza documental.** Ahorro acumulado v10.72-v10.77: ~32K tokens (-37%) sobre el peso documental original. Base limpia para abrir extracciones paralelas (`extract/U2`, `extract/U4`, etc.) en chats nuevos con worktrees dedicados.

---

## [v10.76b — 2026-05-07] — Cierre de drift vivo en PROCESO-MAESTRO tras dictamen del revisor sobre v10.76

Hallazgos del revisor sobre v10.76: el archivado fue correcto, pero el documento vivo seguía arrastrando 3 zonas con drift activo que la limpieza no había tocado. Sin corregirlas, compactar más documentación habría consolidado incoherencias.

**1. Decisión 17 (Parte 4, línea 520):** decía "taxonomía cerrada de **17 valores**" en una decisión cerrada viva. Real: 20 valores desde v10.64. Tampoco mencionaba `destreza` (lista MCER de 6) ni `enfoque` (string del enum de 6) introducidos en v10.60.

**Fix:** decisión 17 reescrita con "taxonomía cerrada de **20 valores**" + referencia a schema §5 + mención de los 3 ejes ortogonales (`tipo`/`destreza`/`enfoque`) con sus enumeraciones cerradas y referencia a schema §5b/§5c.

**2. Árbol actual (Parte 3, líneas 450-486):** describía a U3 como "única poblada" cuando el repo ya tenía U0, U1 y U3 todas pobladas y validando 0/0; no mencionaba los 5 archivos vivos de `fases/1-extraccion-inventario/` post-refactor (solo CLAUDE.md y prompt.md); no incluía `docs/historico/` que existe desde v10.72 y se pobló más en v10.75 y v10.76.

**Fix:** árbol vivo reescrito al estado real: 3 unidades extraídas con conteo de actividades; los 5 archivos operativos de fase 1 listados (CLAUDE, prompt, schema-inventario, reglas-operativas, convenciones-y-casos); `docs/historico/` con sus 3 sub-rutas/archivos archivados; CLAUDE.md raíz mencionado como contrato global.

**3. Síntesis Parte 6 (líneas 637-642):** decía "📋 **Bloque A pendiente** (REVIEW): estabilizar fase 1 (validar U3, probar U4, resolver bugs B1-B4)". Real: A1, A2, A3, A4 todos ✅ cerrados; el bloque A entero está cerrado (REVIEW.md líneas 45 y 112).

**Fix:** Bloque A actualizado a ✅ cerrado con detalle de los 4 sub-pasos y referencia a REVIEW.md. Bloque B refinado al estado real (parcial: B5 cerrado, B1.5 en diseño, B1+B2 esperan dependencias).

**Lo que NO se toca** (legítimo, no es drift vivo):
- Bitácora del documento (Parte final): menciones a "17 tipos" en entradas del 2026-05-05 son históricas, describen el estado en su momento. Revisionismo prohibido.

**Sin cambios funcionales en código.** Validador U0/U1/U3 → 0/0.

**Próximo:** v10.77 (compactar bloque A REVIEW, decisión condicional) ahora con base documental viva limpia.

---

## [v10.76 — 2026-05-07] — Archivado de árboles históricos y Parte 5.bis de PROCESO-MAESTRO

Continuación de la limpieza documental tras v10.75. Tres bloques de PROCESO-MAESTRO.md auto-etiquetados como históricos en su propio contenido se trasladan a `docs/historico/`, dejando punteros cortos donde estaban.

**Bloques movidos:**

1. **Árbol intermedio del repositorio** (líneas 487-533, ~2.161 chars). Etiqueta original: *"estado anterior — pre-disolución de `nuevo/`"*. Útil para entender la fase de migración cuando `nuevo/` y `viejo/` coexistían.
2. **Árbol antes del split** (líneas 535-668, ~3.960 chars). Etiqueta original: *"referencia histórica — anterior a 2026-05-05 12:15, NO ES EL ESTADO ACTUAL"*. Estructura del repo cuando todo el contenido editorial vivía en raíz.
3. **Parte 5.bis: Histórico de la estrategia de migración (CERRADA)** (líneas 788-806, ~1.301 chars). Cronología y plan de la migración que produjo la estructura actual; declarada cerrada en su propio título.

**Destinos:**
- `docs/historico/PROCESO-MAESTRO-arboles-historicos.md` (196 líneas, 11.324 chars): los 2 árboles con cabecera explicando qué archiva y diferencia con el árbol vivo.
- `docs/historico/PROCESO-MAESTRO-parte5bis-migracion.md` (27 líneas, 1.807 chars): Parte 5.bis con cabecera.

**En PROCESO-MAESTRO vivo:** los 3 bloques quedan reemplazados por punteros cortos (3 líneas cada uno) que mantienen el encabezado original de la sección + 1 línea referenciando el histórico. La numeración y secuencia de Partes (1, 2, 3, 4, 5, 5.bis, 6, Bitácora) queda intacta.

**Lo que NO se toca:**
- Árbol actual (Parte 3, línea 450): es el estado vivo, queda íntegro.
- Bitácora del documento (Parte final): histórica pero parte de la trazabilidad viva del propio PROCESO-MAESTRO.
- Decisiones cerradas (Parte 4) y pendientes (Parte 5): vivos.

**Resultado medido:**
- PROCESO-MAESTRO.md: 868 → 677 líneas (-22%, ~190 líneas archivadas).
- Peso documental reducido en ~7K chars de partes vivas, preservados en archivos históricos referenciables.

**Sin cambios funcionales en código.** Validador U0/U1/U3 → 0/0.

**Próximo:** v10.77 (compactar bloque A cerrado de REVIEW.md, **decisión condicional** tras evaluar si tras v10.75-76 sigue compensando).

---

## [v10.75b — 2026-05-07] — Corrección de 2 inexactitudes menores en el acta de v10.75

Hallazgo del revisor sobre v10.75 (ambos en el acta del propio commit, no en el archivado):

1. La verificación post-archivado decía *"`diagrama._read_version()` devuelve `10.74`"*. La lógica real (lee primer `## [v...]`) devuelve `10.75` tras el commit, porque la primera entrada del CHANGELOG vivo pasa a ser v10.75.
2. La métrica final decía *"977 líneas (-61%)"*. Tras añadir la entrada v10.75 + puntero al histórico, el archivo resultó en **1.004 líneas (-60%)**.

Ninguna afecta a la funcionalidad ni al archivado en sí (que está bien hecho); solo precisión del acta.

**Fix:** ambas líneas del acta v10.75 actualizadas a los valores reales (CHANGELOG.md líneas 23 y 25; REVIEW.md bitácora del 2026-05-07 13:00).

**Sin cambios funcionales.** Validador U0/U1/U3 → 0/0.

**Próximo:** v10.76 (mover árboles históricos embebidos + Parte 5.bis de PROCESO-MAESTRO), ya con la serie documental cerrada limpia.

---

## [v10.75 — 2026-05-07] — Archivado del CHANGELOG pre-v10.40 a `docs/historico/`

Limpieza documental autorizada por el revisor tras el pase de coherencia (v10.74/v10.74b). El CHANGELOG vivo crecía sin límite y representaba el 56% del peso documental total del repo. Las entradas anteriores a v10.40 (refactor del prompt de fase 1) son histórico inmutable; trasladarlas reduce contaminación de contexto sin perder trazabilidad.

**Verificaciones previas al archivado:**
- `grep "\(#v" CHANGELOG.md` → 0 hits (sin links internos rotos).
- Frontera identificada: v10.40 termina en línea 977; v10.39 empieza en línea 978.
- `diagrama.py:_read_version()` solo busca el primer `## [v...]`, no acoplado al rango de versiones.

**Acción:**
- Trasladado el texto íntegro (líneas 978-2512, 1.535 líneas, ~112K chars) a `docs/historico/CHANGELOG-pre-refactor.md` con una cabecera mínima explicando qué archiva.
- CHANGELOG vivo conserva v10.40 íntegra hacia adelante.
- Puntero corto al histórico añadido bajo el título y antes del primer `---`.

**Verificaciones post-archivado:**
- `diagrama._read_version()` devuelve `10.75` tras el commit (primera entrada viva, comportamiento idéntico al previo).
- Validador U0/U1/U3 → 0/0 (control de sanidad lateral).
- Tamaño: CHANGELOG vivo pasa de 2.512 a 1.004 líneas tras añadir esta entrada y el puntero al histórico (-60%); peso documental del archivo reducido aproximadamente 28K tokens.

**No se reescriben** entradas históricas (revisionismo prohibido). El traslado es texto-a-texto sin edición.

**Próximo:** v10.76 (mover árboles históricos embebidos + Parte 5.bis de PROCESO-MAESTRO).

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

