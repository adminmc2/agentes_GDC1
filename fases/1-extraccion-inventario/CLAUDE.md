# Fase 1 — Extracción de inventario

> Auto-cargado por Claude Code al trabajar dentro de `fases/1-extraccion-inventario/`. **Contrato corto de la fase**: qué produce, dónde input/output, cómo validar, reglas críticas, navegación. El detalle operativo vive en los archivos hermanos.

> **Estado de los contratos de fase 1** (todos vivos bajo el modelo IA-first):
>
> - ✅ **`prompt.md`** — entry point operativo.
> - 🟢 **`schema-inventario.md`** — shape canónico del JSON (4 bloques top-level consolidados, 4 listas tipadas por actividad y cuadro, sufijo `@R`, marcas internas, `estructura_perifrastica`). Deuda específica de migración catalogada en el **Apéndice transitorio §A.3** del propio schema (alineación con el validador y con el registry verbal).
> - 🟢 **`reglas-operativas.md`** — autoridad operativa de decisión. Política transversal (propuesta-en-chat §0.1, construcción iterativa de `recurrente` §0.2, procedimiento A/B/C §0.3), precedencias (§1), asignación de tipo/destreza/enfoque/tipo_cuadro (§2-§3), "Para aprender"/"Observa" (§4), población de campos (§5: criterios paraguas, verbo soporte vs paradigma, anticipación por lema, canon léxico, ciclo de vida de marcas internas), derivación de los 4 bloques consolidados (§6: anticipación, normalización `formas_trabajadas`, sufijo `@R` con chequeo previo, Regla 11 audio), unidades atípicas (§7), política PCIC (§9), mejora continua (§10).
> - 🟢 **`convenciones-y-casos.md`** — convenciones de transcripción del libro al JSON y casebook. Lookup puntual durante la corrida.
> - 🚫 `docs/historico/prompt-v1-antiguo.md`, `docs/historico/prompt-v2-monolitico-NO-USAR.md` — versiones antiguas archivadas, no usar.
> - 🗄️ `docs/historico/PROPUESTA-PIEZA-2-IA-FIRST.md`, `docs/historico/schema-inventario-viejo.md` — archivados 2026-05-13.
> - 🗄️ `docs/historico/REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md` — archivado 2026-05-14.
> - 🗄️ `docs/historico/convenciones-y-casos-viejo.md` y `docs/historico/reglas-operativas-viejo.md` — archivados 2026-05-15 (v10.116) tras absorberse en los contratos vivos.
>
> **Precedencia explícita en caso de conflicto entre contratos vivos:** `schema-inventario.md` > `reglas-operativas.md` > `convenciones-y-casos.md`. Si una regla concreta entra en conflicto entre niveles, prevalece el superior.

---

## Qué produce esta fase

Convertir el PDF del libro de una unidad en un JSON estructurado (`UX-nc1-inventario.json`) que captura todo el contenido editorial visible al alumno (actividades, cuadros, vocabulario consolidado, bloque de autoevaluación) según el contrato de datos del proyecto.

## Input y output

- **Input:** `unidades/UX/fuente/UX-nc1.pdf` — PDF del libro del alumno con texto embebido (lo aporta el autor; gitignored).
- **Output:** `unidades/UX/UX-nc1-inventario.json` — un único archivo.

## Cómo se invoca

> Extrae el inventario de UX siguiendo `fases/1-extraccion-inventario/prompt.md`.

## Cómo validar

> **Convención de comandos:** todos los comandos en este archivo y en `prompt.md` son **root-relative** — se ejecutan desde la raíz del repo (`/guia-didactica-profesor-IA/` o el worktree equivalente), no desde esta carpeta de fase. Aunque este CLAUDE.md se auto-cargue al trabajar dentro de `fases/1-extraccion-inventario/`, los comandos asumen `cwd = raíz del repo`.

1. **Validador automático:** `python3 scripts/validar_inventario.py X` → debe dar **0 errores y 0 avisos** (1 aviso intencional aceptable si la unidad es atípica con `_nota_unidad_atipica`). **Estado transitorio:** mientras `scripts/validar_inventario.py` no esté alineado con `schema-inventario.md` (ver Apéndice transitorio §A.1 / §A.3 del schema y nota transitoria del `prompt.md`), este gate queda sustituido por validación manual contra el schema + revisión visual.
2. **Validación visual del autor:** `python3 diagrama.py` → `http://localhost:8080` → Inventarios → revisar 2-3 páginas al azar contrastando con el PDF.

---

## Reglas críticas (las que un humano nunca debe olvidar al trabajar en esta fase)

1. **Texto verbatim del libro** — el JSON debe contener el contenido visible al alumno **exactamente como aparece en el libro**, no como referencia ni interpretación. Para cloze, huecos como `_____`. Para textos, íntegros. Nunca sustituir el enunciado por la respuesta.
2. **No inventar contenido editorial** — si una palabra, fecha, dato o regla no está en la fuente original, no se añade. Caso ambiguo durante la extracción: surgir la duda **en chat** con opciones razonables (regla §0.1 de `reglas-operativas.md`), no marcar silenciosamente. Solo si el autor lo autoriza explícitamente se escribe `_pendiente_canon` o `_funcion_ambigua` (ciclo de vida en `reglas-operativas.md` §5.9).
3. **Single source of truth por capa** — las reglas estructurales viven en `schema-inventario.md`, las decisionales y de población en `reglas-operativas.md`, las convenciones de transcripción y casebook en `convenciones-y-casos.md`. **Precedencia en conflicto: schema > reglas > convenciones.** `CLAUDE.md` y `prompt.md` pueden repetir hechos y reglas mínimas de contrato de fase (objetivo, input/output, invocación, validación, literalidad) por ser entry points complementarios. Si lógica operativa o reglas de clasificación aparecen duplicadas fuera de su archivo canónico, es un bug.
4. **Validar antes de cerrar** — el JSON pasa el validador con 0 errores y la revisión visual antes de declararse cerrado. **Estado transitorio:** mientras `scripts/validar_inventario.py` no esté alineado con `schema-inventario.md` (ver Apéndice transitorio §A.1 / §A.3 del schema), el gate del validador se sustituye por validación manual contra el schema + revisión visual del autor; la revisión visual sigue siendo obligatoria.
5. **Schema documental ↔ validador no divergen como principio canónico** — `schema-inventario.md` y `scripts/validar_inventario.py` son contratos paralelos; cualquier divergencia es bug a resolver. **Estado transitorio:** hoy existe divergencia conocida y declarada en el Apéndice transitorio §A.1 / §A.3 del schema, con criterios de retirada (§A.4) y deuda concreta listada para Paso 3 del cierre. Hasta que el apéndice se retire, la divergencia es admitida pero gestionada; cero deuda silenciosa.
6. **Documentación de fase 1 es siempre obligatoria.** Antes de cualquier extracción, el ejecutor debe declarar en chat haber leído `schema-inventario.md` + `reglas-operativas.md` + `convenciones-y-casos.md`. Quien invoque al ejecutor (coordinador, autor, otro agente) debe **citar literalmente** `fases/1-extraccion-inventario/prompt.md` en la instrucción — no basta con describir la tarea. Razón: en U5 (v10.143) un bug recurrente derivado de §5.2 incompleta no fue atrapado porque el ejecutor no aplicó la doc; la causa raíz fue la regla incompleta, pero el gate de invocación falló como defensa. La generalización de §5.2 a las 4 dimensiones (v10.144) cierra el bug estructural; este gate cierra la cadena de invocación.

7. **Canon canónico literal es autoridad de naming** — toda referencia que entra al JSON como clave o valor canónico (referencias léxicas en `actividad.vocabulario` / `cuadro.vocabulario`, claves de `vocabulario_consolidado.{principal,recurrente}`, claves de `gramatica_consolidada.{principal,recurrente}`, claves de `pronunciacion_ortografia_consolidada.{principal,recurrente}`, `lema` en `tiempos_y_verbos`) debe ser literal del registry correspondiente (`campos-semanticos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`, `verbos-canonicos.json`). Si no hay canónico seguro, escalar en chat (regla §0.1 de `reglas-operativas.md`); solo si el autor lo autoriza se marca `_pendiente_canon`. Política y árbol de decisión: `reglas-operativas.md` §5.6.

   **Convención de auditoría — cita canónica vs mención temática.** Para auditar cualquier documento operativo de fase 1, aplicar la prueba de coincidencia literal con el registry **solo** cuando:
   - El doc dice "la clave es", "nombre canónico", "categoría canónica", "lema canónico", o equivalente.
   - El doc pone ejemplos entre comillas presentados como **valores de clave** del registry.

   **NO aplicar** la prueba de naming literal cuando el doc usa la palabra como **descripción del dominio en lenguaje natural** (ej. "acento, sílaba tónica, entonación, reglas ortográficas..."). La mención temática es libre; la cita canónica está sujeta a coincidencia exacta. Esta distinción se mantiene estable entre versiones para que auditorías sucesivas apliquen el mismo criterio.

---

## Para qué consultar qué archivo

| Pregunta | Archivo |
|---|---|
| ¿Cuál es el flujo operativo de la extracción? ¿Qué pasos sigo? | `prompt.md` |
| ¿Cuál es el shape del JSON? ¿Qué tipos, qué claves, qué enumeraciones? | `schema-inventario.md` |
| ¿Cómo decido X? (precedencias actividad/cuadro/nota/autoevaluación, asignación de `tipo`/`destreza`/`enfoque`/`tipo_cuadro`, "Para aprender" / "Observa", reglas de población de campos, unidades atípicas) | `reglas-operativas.md` |
| ¿Cómo transcribo X del libro al JSON? (primer ítem resuelto, textos de lectura, diálogos con huecos, textos atribuidos a personajes, sopas de letras, marcadores editoriales) | `convenciones-y-casos.md` §1 |
| ¿Cómo se ve un cloze, una selección múltiple, un cuestionario en el JSON? | `convenciones-y-casos.md` §2 |
| ¿Hubo un caso similar antes en una extracción real? | `convenciones-y-casos.md` §4 (casebook) |
| ¿Cómo se añade un caso nuevo al sistema? | `reglas-operativas.md` §10 (política de mejora continua) |
| ¿Qué nombres canónicos puedo usar como clave de los bloques consolidados o como referencia en las 4 listas tipadas de actividad/cuadro? | Cada dimensión tiene su registry: léxico → `campos-semanticos-canonicos.json`; gramatical → `gramatica-canonica.json`; pron/orto → `pronunciacion-ortografia-canonica.json`; verbal → `verbos-canonicos.json`. Política y árbol de decisión léxico → `reglas-operativas.md` §5.6. Política análoga aplica a los demás registries (regla crítica 6). |
| ¿Qué fuente PCIC apoya cada dimensión? Glosario "Fuentes PCIC y registries canónicos" (tabla resumen) + archivos `pcic-a1-vocabulario.json`, `pcic-a1-gramatica.json`, `pcic-a1-pronunciacion-ortografia.json`, `pcic-a1-comunicacion.json` |

---

## Fixtures exploratorias (`UNp`)

Carpetas tipo `unidades/UN-propuesta/` con inventarios `UN-propuesta-nc1-inventario.json` cuyo campo `unidad` es la cadena `"Np"` (no entero). **No son inventarios canónicos del curso.** Su propósito es servir como muestra para revisar el shape nuevo, estresar el contrato y exponer ambigüedades operativas durante el rediseño.

**Reglas:**
- Una fixture lleva siempre un bloque top-level `_fixture_exploratoria` con `tipo`, `fecha`, `proposito` y `no_es_inventario_canonico: true`.
- Puede contener marcas bloqueantes (`_pendiente_canon`, `_funcion_ambigua`) si la fixture documenta hallazgos no resueltos. Las marcas **deben haber sido surgidas en chat antes** (regla §0.1 de `reglas-operativas.md`); no se escriben silenciosamente.
- Un inventario candidato a cierre debe usar `unidad: N` (entero) y cabecera coincidente con `unidades/nc1-curso.json`.
- El dashboard tolera fixtures `Np` y las muestra junto a los inventarios oficiales para facilitar revisión humana.

---

## Documentos relacionados

- `prompt.md` (en esta carpeta) — prompt core ejecutable.
- `schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md` (en esta carpeta) — tres capas vivas de soporte. Precedencia: schema > reglas > convenciones.
- `../../scripts/validar_inventario.py` — validador estructural ejecutable, contrato paralelo del schema.
- `../../CLAUDE.md` (raíz) — contexto global del proyecto y reglas de oro globales.
- `../../PROCESO-MAESTRO.md` — decisiones cerradas a nivel de proyecto.
