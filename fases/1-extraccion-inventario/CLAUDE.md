# Fase 1 — Extracción de inventario

> Auto-cargado por Claude Code al trabajar dentro de `fases/1-extraccion-inventario/`. **Contrato corto de la fase**: qué produce, dónde input/output, cómo validar, reglas críticas, navegación. El detalle operativo vive en los archivos hermanos.

> ⚠️ **FASE 1 EN MIGRACIÓN.** Estado real de cada contrato a fecha actual:
>
> - ✅ **`prompt.md`** — entry point operativo nuevo, alineado con el modelo IA-first.
> - 🟢 **`schema-inventario.md`** — cuerpo alineado con el modelo nuevo (4 bloques top-level consolidados, 4 listas tipadas por actividad y cuadro, sufijo `@R`, marcas internas declaradas, normalización de formas_trabajadas). Deuda específica de migración aún pendiente, catalogada en el **Apéndice transitorio §A.3** del propio schema (renombrados de enums, alineación con el validador y con el registry verbal).
> - 🟡 **`reglas-operativas.md`** — cuerpo mixto. La mayoría de §1-§9 conserva contenido v1 pre-rediseño (pendiente migración Paso 2). Pero **ya hay reglas del rediseño integradas en cuerpo con carácter obligatorio**: §5.10 (verbo soporte vs paradigma trabajado), §5.11 (normalización de `formas_trabajadas` en consolidado), §5.12 (procedimiento OBLIGATORIO de poblado de `recurrente`, con detección por dimensión §5.12.A/B/C), §5.13 (propuesta-en-chat ante toda decisión no clara), §5.14 (construcción iterativa de `recurrente`). El **banner de follow-ups** al inicio del archivo conserva las reglas aún no integradas: sufijo `@R`, regla 11 sobre `audio.transcripcion`, input incidental vs contenido enseñado, anticipación vs recurrente, heterogeneidad semántica.
> - 🟡 **`convenciones-y-casos.md`** — ajustes parciales aplicados durante el rediseño (renombrado `fonetica → pronunciacion_ortografia`). Migración completa pendiente.
> - 🚫 `docs/historico/prompt-v1-antiguo.md`, `docs/historico/prompt-v2-monolitico-NO-USAR.md` — versiones antiguas archivadas, no usar.
> - 📑 `REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md`, `PROPUESTA-PIEZA-2-IA-FIRST.md` — documentos de discusión arquitectónica, no input de corridas.
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
2. **No inventar contenido editorial** — si una palabra, fecha, dato o regla no está en la fuente original, no se añade. Caso ambiguo durante la extracción: marcar como TODO en el JSON y consultar al autor antes de cerrar el inventario.
3. **Single source of truth por capa** — las reglas estructurales, decisionales y convenciones viven una sola vez en los archivos de soporte (`schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md`). `CLAUDE.md` y `prompt.md` pueden repetir hechos y reglas mínimas de contrato de fase (objetivo, input/output, invocación, validación, literalidad) por ser entry points complementarios. Si lógica operativa o reglas de clasificación aparecen duplicadas fuera de su archivo canónico, es un bug.
4. **Validar antes de cerrar** — el JSON pasa el validador con 0 errores y la revisión visual antes de declararse cerrado.
5. **Schema documental ↔ validador no divergen** — `schema-inventario.md` y `scripts/validar_inventario.py` son contratos paralelos. Cualquier divergencia entre ambos es un bug que se resuelve antes del cierre.
6. **Canon semántico es autoridad de naming** — los valores de `actividad.campo_semantico` y las claves de `vocabulario_consolidado.{principal,recurrente,comprension}` deben ser canónicos del canon (`campos-semanticos-canonicos.json`). Si no hay canónico seguro, usar la marca literal `"_pendiente_canon"` y resolver antes del cierre. Política, árbol de decisión y rollout en `reglas-operativas.md` §5.6.

---

## Para qué consultar qué archivo

| Pregunta | Archivo |
|---|---|
| ¿Cuál es el flujo operativo de la extracción? ¿Qué pasos sigo? | `prompt.md` |
| ¿Cuál es el shape del JSON? ¿Qué tipos, qué claves, qué enumeraciones? | `schema-inventario.md` |
| ¿Cómo decido X? (precedencias actividad/cuadro/nota/autoevaluación, asignación de `tipo`/`destreza`/`enfoque`/`tipo_cuadro`, "Para aprender" / "Observa", reglas de población de campos, unidades atípicas) | `reglas-operativas.md` |
| ¿Cómo transcribo X del libro al JSON? (sílaba tónica subrayada, primer ítem resuelto, textos de lectura, diálogos, sopas de letras) | `convenciones-y-casos.md` §1 |
| ¿Cómo se ve un cloze, una selección múltiple, un cuestionario en el JSON? | `convenciones-y-casos.md` §2-3 |
| ¿Hubo un caso similar antes en una extracción real? | `convenciones-y-casos.md` §4 (casebook) |
| ¿Cómo se añade un caso nuevo al sistema? | `convenciones-y-casos.md` §5 |
| ¿Qué nombres de `campo_semantico` y de claves de `vocabulario_consolidado` son válidos? | `campos-semanticos-canonicos.json` (fuente de datos) + `reglas-operativas.md` §5.6 (política, árbol de decisión, rollout) |
| ¿Qué fuente PCIC apoya cada dimensión? Glosario "Fuentes PCIC y registries canónicos" (tabla resumen) + archivos `pcic-a1-vocabulario.json`, `pcic-a1-gramatica.json`, `pcic-a1-pronunciacion-ortografia.json`, `pcic-a1-comunicacion.json` |

---

## Fixtures exploratorias (`UNp`)

Carpetas tipo `unidades/UN-propuesta/` con inventarios `UN-propuesta-nc1-inventario.json` cuyo campo `unidad` es la cadena `"Np"` (no entero). **No son inventarios canónicos del curso.** Su propósito es servir como muestra para revisar el shape nuevo, estresar el contrato y exponer ambigüedades operativas durante el rediseño.

**Reglas:**
- Una fixture lleva siempre un bloque top-level `_fixture_exploratoria` con `tipo`, `fecha`, `proposito` y `no_es_inventario_canonico: true`.
- Puede contener marcas bloqueantes (`_pendiente_canon`, `_funcion_ambigua`) — la fixture **no es cerrable**.
- Un inventario candidato a cierre debe usar `unidad: N` (entero) y cabecera coincidente con `unidades/nc1-curso.json`.
- El dashboard tolera fixtures `Np` y las muestra junto a los inventarios oficiales para facilitar revisión humana.

---

## Documentos relacionados

- `prompt.md` (en esta carpeta) — prompt core ejecutable.
- `schema-inventario.md`, `reglas-operativas.md`, `convenciones-y-casos.md` (en esta carpeta) — artefactos de soporte.
- `../../scripts/validar_inventario.py` — validador estructural ejecutable, contrato paralelo del schema.
- `../../CLAUDE.md` (raíz) — contexto global del proyecto y reglas de oro globales.
- `../../PROCESO-MAESTRO.md` — decisiones cerradas a nivel de proyecto.
