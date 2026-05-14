# Fase 1 — Extracción de inventario

> Auto-cargado por Claude Code al trabajar dentro de `fases/1-extraccion-inventario/`. **Contrato corto de la fase**: qué produce, dónde input/output, cómo validar, reglas críticas, navegación. El detalle operativo vive en los archivos hermanos.

> ⚠️ **FASE 1 EN MIGRACIÓN.** Estado real de cada contrato a fecha actual:
>
> - ✅ **`prompt.md`** — entry point operativo nuevo, alineado con el modelo IA-first.
> - 🟢 **`schema-inventario.md`** — cuerpo alineado con el modelo nuevo (4 bloques top-level consolidados, 4 listas tipadas por actividad y cuadro, sufijo `@R`, marcas internas declaradas, normalización de formas_trabajadas). Deuda específica de migración aún pendiente, catalogada en el **Apéndice transitorio §A.3** del propio schema (renombrados de enums, alineación con el validador y con el registry verbal).
> - 🟢 **`reglas-operativas.md`** — autoridad operativa de decisión reescrita desde cero bajo modelo IA-first. Contiene política transversal (propuesta-en-chat, construcción iterativa de recurrente, procedimiento sistemático con A/B/C), precedencia actividad/cuadro/nota/autoevaluación, asignación de tipo/destreza/enfoque/tipo_cuadro, casos "Para aprender" y "Observa", criterios pedagógicos paraguas de población de listas tipadas, canon semántico léxico, ciclo de vida de marcas internas, derivación de los 4 bloques consolidados, unidades atípicas, política PCIC, política de mejora continua. `reglas-operativas-viejo.md` queda como reservorio histórico no consultable operativamente.
> - 🟡 **`convenciones-y-casos.md`** — **deuda pendiente.** Renombrado a `convenciones-y-casos-viejo.md` durante el rediseño; el nuevo archivo se construirá en lote siguiente. Mientras tanto, las referencias a `convenciones-y-casos.md` desde otros docs pueden estar rotas. Contenido vigente vive en `-viejo`.
> - 🚫 `docs/historico/prompt-v1-antiguo.md`, `docs/historico/prompt-v2-monolitico-NO-USAR.md` — versiones antiguas archivadas, no usar.
> - 🗄️ `docs/historico/PROPUESTA-PIEZA-2-IA-FIRST.md`, `docs/historico/schema-inventario-viejo.md` — archivados en histórico el 2026-05-13; ya absorbidos en los contratos vivos.
> - 🗄️ `docs/historico/REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md` — discusión arquitectónica del rediseño de fase 1. Archivado el 2026-05-14 tras absorberse todas sus piezas en los contratos vivos (schema, reglas, glosario, registries).
>
> **Regla de precedencia durante la transición:** cuando una regla concreta de `reglas-operativas.md` entra en conflicto con `schema-inventario.md`, **prevalece el schema**. Detalle de la transición operativa en la nota transitoria del `prompt.md`.

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

1. **Validador automático:** `python3 scripts/validar_inventario.py X` → debe dar **0 errores y 0 avisos** (1 aviso intencional aceptable si la unidad es atípica con `_nota_unidad_atipica`).
2. **Validación visual del autor:** `python3 diagrama.py` → `http://localhost:8080` → Inventarios → revisar 2-3 páginas al azar contrastando con el PDF.

---

## Reglas críticas (las que un humano nunca debe olvidar al trabajar en esta fase)

1. **Texto verbatim del libro** — el JSON debe contener el contenido visible al alumno **exactamente como aparece en el libro**, no como referencia ni interpretación. Para cloze, huecos como `_____`. Para textos, íntegros. Nunca sustituir el enunciado por la respuesta.
2. **No inventar contenido editorial** — si una palabra, fecha, dato o regla no está en la fuente original, no se añade. Caso ambiguo durante la extracción: surgir la duda **en chat** con opciones razonables (regla §0.1 de `reglas-operativas.md`), no marcar silenciosamente. Solo si el autor lo autoriza explícitamente se escribe `_pendiente_canon` o `_funcion_ambigua` (ciclo de vida en `reglas-operativas.md` §5.9).
3. **Single source of truth por capa** — las reglas estructurales y decisionales viven una sola vez en los archivos de soporte vivos (`schema-inventario.md`, `reglas-operativas.md`). La capa de **convenciones de transcripción y casebook** queda en deuda transitoria: el archivo vivo `convenciones-y-casos.md` aún no ha sido reescrito; mientras tanto se consulta `convenciones-y-casos-viejo.md` solo para esa capa concreta, y nunca prevalece sobre schema o reglas. `CLAUDE.md` y `prompt.md` pueden repetir hechos y reglas mínimas de contrato de fase (objetivo, input/output, invocación, validación, literalidad) por ser entry points complementarios. Si lógica operativa o reglas de clasificación aparecen duplicadas fuera de su archivo canónico, es un bug.
4. **Validar antes de cerrar** — el JSON pasa el validador con 0 errores y la revisión visual antes de declararse cerrado.
5. **Schema documental ↔ validador no divergen** — `schema-inventario.md` y `scripts/validar_inventario.py` son contratos paralelos. Cualquier divergencia entre ambos es un bug que se resuelve antes del cierre.
6. **Canon semántico léxico es autoridad de naming** — las claves de `vocabulario_consolidado.{principal,recurrente}` (2 sub-bloques, no 3) y las referencias léxicas en `actividad.vocabulario` / `cuadro.vocabulario` deben ser canónicas del registry (`campos-semanticos-canonicos.json`). Si no hay canónico seguro, escalar en chat (regla §0.1 de `reglas-operativas.md`); solo si el autor lo autoriza se marca `_pendiente_canon`. Política y árbol de decisión: `reglas-operativas.md` §5.6.

---

## Para qué consultar qué archivo

| Pregunta | Archivo |
|---|---|
| ¿Cuál es el flujo operativo de la extracción? ¿Qué pasos sigo? | `prompt.md` |
| ¿Cuál es el shape del JSON? ¿Qué tipos, qué claves, qué enumeraciones? | `schema-inventario.md` |
| ¿Cómo decido X? (precedencias actividad/cuadro/nota/autoevaluación, asignación de `tipo`/`destreza`/`enfoque`/`tipo_cuadro`, "Para aprender" / "Observa", reglas de población de campos, unidades atípicas) | `reglas-operativas.md` |
| ¿Cómo transcribo X del libro al JSON? (sílaba tónica subrayada, primer ítem resuelto, textos de lectura, diálogos, sopas de letras) | `convenciones-y-casos-viejo.md` §1 (deuda transitoria; nunca prevalece sobre schema/reglas) |
| ¿Cómo se ve un cloze, una selección múltiple, un cuestionario en el JSON? | `convenciones-y-casos-viejo.md` §2-3 (deuda transitoria) |
| ¿Hubo un caso similar antes en una extracción real? | `convenciones-y-casos-viejo.md` §4 (casebook histórico) |
| ¿Cómo se añade un caso nuevo al sistema? | `convenciones-y-casos-viejo.md` §5 (diferido hasta reescribir el archivo vivo) |
| ¿Qué nombres canónicos léxicos puedo usar como clave de `vocabulario_consolidado.{principal,recurrente}` o en `actividad.vocabulario`? | `campos-semanticos-canonicos.json` (fuente de datos) + `reglas-operativas.md` §5.6 (política y árbol de decisión) |
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
- `schema-inventario.md`, `reglas-operativas.md` (en esta carpeta) — artefactos de soporte vivos.
- `convenciones-y-casos-viejo.md` (en esta carpeta) — reservorio histórico consultable solo para convenciones de transcripción y casebook durante la deuda transitoria; nunca prevalece sobre schema/reglas. El archivo vivo `convenciones-y-casos.md` se reescribirá en el lote siguiente.
- `../../scripts/validar_inventario.py` — validador estructural ejecutable, contrato paralelo del schema.
- `../../CLAUDE.md` (raíz) — contexto global del proyecto y reglas de oro globales.
- `../../PROCESO-MAESTRO.md` — decisiones cerradas a nivel de proyecto.
