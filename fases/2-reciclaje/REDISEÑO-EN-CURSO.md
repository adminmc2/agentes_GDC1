# Rediseño de fase 2 — modelo IA-first (versión activa)

> **Estado:** EN CONSTRUCCIÓN. Documento vivo y **único** del rediseño de fase 2 bajo modelo IA-first. El antiguo `REDISEÑO-EN-CURSO-viejo.md` se archivó en `docs/historico/` (v11.34); su material vivo sin procesar quedó absorbido en el "Reservorio" al final de este documento.
>
> **Audiencia:** autor + revisor. El ejecutor (Claude) lo va actualizando paso a paso conforme el autor y el revisor cierran decisiones.
>
> **Estrategia de construcción:** este documento se construye **en pasos** indicados por el autor. Cada paso cierra una pieza concreta del rediseño. No se anticipan piezas no discutidas — el esqueleto contiene placeholders que se rellenan cuando llegue su turno.

---

## §1. Modelo de trabajo (paso 1 — definido 2026-05-15)

### §1.1. Granularidad

Procesamiento **por unidad**. Cada unidad pasa por un ciclo completo (fase 1 + fase 2) antes de pasar a la siguiente.

### §1.2. Estructura del ciclo por unidad

Para cada unidad U[X]:

1. **Fase 1 — extracción del inventario** en **Chat A**:
   - Worktree aislado (`../guia-proc-U[x]/`, rama `proc-u[x]-wip`).
   - Prompt envoltorio: `fases/1-extraccion-inventario/prompt-dry-run.md`.
   - Dry-run, iteración con el autor, OK del autor, escritura del JSON candidato, validación.
   - Cierra cuando el inventario está listo.
2. **Fase 2 — procesamiento del reciclaje** en **Chat B** (mismo worktree, distinto chat):
   - Prompt envoltorio propio de fase 2 *(pendiente de diseño en pasos siguientes)*.
   - Cubre Capa 1 + Capa 2 sobre la unidad recién integrada.
   - Cierra cuando el reciclaje incremental está listo.
3. **Integración a main** del paquete completo (inventario nuevo + reciclaje actualizado) por el ejecutor coordinador.
4. Salto a la siguiente unidad.

### §1.3. Arquitectura interna de fase 2 (decisión heredada del viejo, vigente)

Híbrida en dos partes, **no a la vez**:

- **Capa 1 — script determinista** (Python, automático): genera el esqueleto mecánico de `nc1-reciclaje.json` (hilos nivel `mapa` desde `nc1-curso.json`; hilos nivel `auto` desde los 4 bloques top-level consolidados del inventario; acciones por defecto).
- **Capa 2 — sesión IA enriquecedora**: refina decisiones editoriales (acciones), aplica validación cross-unidad (R1-R5), detecta candidatos §8, propone-en-chat al autor lo no obvio.

### §1.4. Hitos cross-unidad

- **Por unidad**: ciclo completo (Capa 1 + Capa 2 sobre la unidad recién integrada).
- **Tras 3 unidades acumuladas**: revisión cross-unidad ampliada (Capa 2 sobre el bloque de unidades).
- **Tras todas las unidades del curso (cierre de bloque)**: revisión global final (Capa 2 íntegra + cierre de decisiones pendientes + regeneración íntegra de `nc1-reciclaje.json`).

*(Granularidad exacta de los hitos intermedios — si solo cada 3 o también cada 6, etc. — pendiente de definir en pasos siguientes.)*

### §1.5. Régimen temporal del modelo (dual)

El diseño sirve para **dos regímenes operativos**:

- **Régimen actual (construcción del sistema):** mientras se procesan U1-U9 y se calibran los sistemas. Ejecución manual supervisada por el ejecutor coordinador (chat principal). Cada paso (Capa 1, Capa 2, integración) lo dispara el humano.
- **Régimen futuro (operación con agentes):** una vez el sistema está calibrado y la arquitectura estabilizada. El flujo lo orquesta un sistema de agentes (Claude Code primero, agentes autónomos después). El humano supervisa **decisiones editoriales** en gates, no la mecánica del flujo.

**Principio de diseño:** mismo flujo, mismos prompts envoltorios, mismos contratos. Solo cambia el **disparador** (humano vs agente). Por eso el diseño debe quedar bien estructurado **ahora** para no reescribir después.

### §1.6. Alcance

El rediseño cubre el curso **NC1** (Nuevo Compañeros 1). Multi-curso (NC2 u otros) está **explícitamente fuera de alcance**: cuando aparezca un curso nuevo, se reconsidera la arquitectura entonces. Hoy no se diseña para soportarlo.

---

## §2. Modelo de análisis por unidad (paso 2 — definido 2026-05-15)

### §2.1. Tres momentos de análisis

Cada unidad U[n] se analiza en **tres momentos** complementarios. Los tres son obligatorios; ninguno reemplaza a otro.

1. **Intra-unidad** — análisis dentro de la propia U[n]: qué contenidos aparecen, en qué bloques, con qué función didáctica interna.
2. **Cross-atrás** — comparación de U[n] contra U[0..n-1]: detecta retomas, ampliaciones, sistematizaciones y contrastes sobre lo ya introducido.
3. **Cross-adelante** — comparación de U[n] contra U[n+1..N]: detecta **anticipaciones** (contenido que aparece en U[n] como input incidental antes de ser canónico en una unidad posterior).

El momento 3 exige que el mapa canónico del curso (`nc1-curso.json` + registries canónicos con `_apariciones`) esté disponible al procesar U[n]. Por eso fase 2 se ejecuta **después** de que fase 1 haya cerrado el inventario de U[n] y los registries reflejen el rol canónico de cada contenido por unidad.

### §2.2. Granularidad por bloque

La unidad de análisis (el "hilo" de reciclaje) depende del bloque:

| Bloque | Granularidad del hilo | Fuente canónica |
|---|---|---|
| Vocabulario | **Campo semántico** | `campos-semanticos-canonicos.json` + `vocabulario_consolidado` del inventario |
| Gramática | **Categoría gramatical** (sub-organizada por `_grupo`, ver §6.3) | `gramatica-canonica.json` + `gramatica_consolidada` del inventario |
| Pronunciación/ortografía | **Categoría pron/orto** | `pronunciacion-ortografia-canonica.json` + `pronunciacion_ortografia_consolidada` del inventario |
| Verbal | **Lema** | `verbos-canonicos.json` + `tiempos_y_verbos_consolidado[].lema` del inventario |
| Perífrasis | **Perífrasis** (hilo aparte, ver §3.3) | `perifrasis-canonicas.json` (5.º registry, ver §6.2) + `estructura_perifrastica` del inventario |

Vocabulario es el único bloque con granularidad de campo semántico (agrupa ítems léxicos). Los demás bajan a la unidad atómica de su dimensión (categoría, lema o perífrasis). El bloque gramática se sub-organiza internamente por `_grupo` (§6.3) sin cambiar su granularidad de hilo.

### §2.3. Etiquetas del hilo (coexistentes)

Cada evento de un hilo en una unidad lleva **una lista de etiquetas** (`etiquetas[]`), no una `accion` única. Las seis etiquetas posibles son:

| Etiqueta | Significado |
|---|---|
| `introduce` | Primera aparición canónica del contenido en el curso. |
| `amplia` | Añade ítems, formas o usos a un contenido ya introducido. |
| `aplica` | Reutiliza el contenido en una tarea sin presentarlo como objeto de estudio. |
| `sistematiza` | Recoge y organiza explícitamente lo que ya estaba activo (cuadro, regla, paradigma). |
| `contrasta` | Pone en oposición con otro contenido (ser/estar, indefinido/definido, etc.). |
| `anticipacion` | Aparece como input incidental antes de ser canónico en una unidad posterior. |

**Coexistencia:** un mismo evento puede llevar varias etiquetas a la vez (ej. `["amplia", "sistematiza"]` cuando un cuadro añade ítems y los organiza; `["aplica", "anticipacion"]` cuando una actividad reutiliza algo ya canónico pero además introduce de pasada una forma que se canonizará después).

**Detección por momento:** `introduce` y `anticipacion` solo se detectan correctamente con cross-adelante (momento 3). `amplia`, `aplica`, `sistematiza`, `contrasta` requieren cross-atrás (momento 2). La etiqueta sola intra-unidad no basta para asignar correctamente ninguna.

### §2.4. Shape del hilo (esbozo)

```json
{
  "bloque": "vocabulario | gramatica | pronunciacion_ortografia | verbal",
  "titulo": "<nombre canónico del registry>",
  "eventos": [
    {
      "unidad": 3,
      "etiquetas": ["amplia", "sistematiza"],
      "evidencias": [ ... ],
      "_nota_ia": "opcional, propuesta razonada de la Capa 2"
    }
  ]
}
```

El detalle del shape (campos exactos, evidencias, persistencia de notas IA) se cierra en pasos siguientes.

---

## §3. Cobertura por bloque y tratamiento de marcas (paso 3 — definido 2026-05-15)

Resuelve cuatro gaps de fase 1 que el modelo §2 dejaba implícitos: pron/orto, verbal, perífrasis y marcas internas.

### §3.1. Pronunciación / ortografía

- **Granularidad del hilo:** una categoría canónica de `pronunciacion-ortografia-canonica.json` = un hilo (ej. "Acento gráfico", "Letra h muda", "Diptongos").
- **Etiquetas aplicables:** las 6 genéricas de §2.3 + **`discrimina`** (específica del bloque): actividades de discriminación auditiva/ortográfica donde el alumno opone formas sin que el contenido se introduzca, amplíe ni sistematice.
- **Fuente de evidencias:** referencias en `actividad.pronunciacion_ortografia[]` + `cuadro.pronunciacion_ortografia[]` + el bloque `pronunciacion_ortografia_consolidada.{principal,recurrente}` del inventario.
- **Recurrencia:** una categoría que aparece como `recurrente` en el consolidado **no** recibe etiqueta automática. La Capa 2 IA analiza el contexto y propone la(s) etiqueta(s) razonadas; el humano cierra.

### §3.2. Tiempos y verbos

- **Granularidad del hilo:** un lema canónico de `verbos-canonicos.json` = un hilo.
- **Granularidad del evento:** un evento por **lema-tiempo**. Si en una unidad el lema `comer` aparece en presente y en indefinido, se generan dos eventos distintos en ese hilo, no uno fusionado.
- **Etiquetas aplicables:** las 6 genéricas de §2.3 sin añadidos.
- **Fuente de evidencias:** `actividad.tiempos_y_verbos[]` + `cuadro.tiempos_y_verbos[]` + `tiempos_y_verbos_consolidado[]` del inventario + atributo `apariciones` del registry `verbos-canonicos.json` (rol canónico por unidad).
- **Detalle del bloque verbal** (formas concretas en el evento, progresión del paradigma, anticipación de formas): ver §7.

### §3.3. Perífrasis verbales

- **Modelado:** **hilo aparte** del lema. La perífrasis `ir a + infinitivo` genera un hilo propio (`bloque: "perifrasis"`, `titulo: "ir a + infinitivo"`), independiente del hilo del lema `ir`.
- **Fuente de evidencias:** campo `estructura_perifrastica` en `actividad.tiempos_y_verbos[]` (schema §3.2; reglas §5.1.2, §5.2).
- **Etiquetas aplicables:** las 6 genéricas de §2.3.
- **Relación con el hilo del auxiliar:** ortogonal. El auxiliar (ej. `ir`) puede tener eventos propios como lema-objeto en otras unidades; la perífrasis tiene su propio recorrido.

### §3.4. Marcas internas (entrada de fase 1)

Política de tratamiento por marca:

| Marca | Bloquea fase 1 | Tratamiento en fase 2 |
|---|---|---|
| `_pendiente_canon` | Sí | **No bloquea fase 2.** Fase 2 puede empezar y procesa el inventario con la marca presente. Se trata como hallazgo pendiente que el autor cerrará en su momento. |
| `_funcion_ambigua` | Sí | Fase 2 lo **analiza** y lo lleva a chat con el autor como caso a cerrar. No se asume resolución automática. |
| `_decisiones_ia` | No | Fase 2 las **lee** como contexto editorial previo, las **cuestiona** si entran en conflicto con el análisis cross-unidad, y **propone** ajustes razonados. No se aceptan a ciegas ni se reescriben silenciosamente. |

**Marcas propias de fase 2:** la Capa 2 IA puede generar marcas análogas (`_decisiones_ia_fase2`, etc.) para registrar sus propias decisiones editoriales. En la práctica, sin embargo, **lo deseable es cerrar cada decisión con el humano** antes de persistirla, no acumular marcas sin resolver. Las marcas de fase 2 son excepción, no flujo normal.

### §3.5. Sufijo `@R` en evidencias

El sufijo `@R` (referencias que solo aparecen en respuestas de actividades productivas; schema F1 §9.5, reglas §6.5) **no genera tratamiento diferencial** en fase 2: el hilo registra el evento igual, ya que el alumno trabaja ese contenido al producir la respuesta. Regla operativa única: **al copiar la referencia al evento del hilo, se preserva el sufijo `@R` tal cual aparece en el inventario**, como metadato de trazabilidad para el revisor. Sin etiqueta especial, sin filtrado.

### §3.6. `principal` vs `recurrente` (clasificación de F1) en fase 2

`principal` / `recurrente` es una clasificación interna de fase 1 (organiza los bloques consolidados del inventario), **no dicta la etiqueta del evento en fase 2**.

- La etiqueta del evento la decide la **Capa 2 IA** leyendo el contexto real (descripciones detalladas del inventario, referencias en actividades/cuadros, comparativa cross-unidad).
- **Prior fuerte**: aproximadamente el 90% de los contenidos clasificados como `recurrente` en el inventario reciben en el hilo etiquetas de repetición (`aplica`, `amplia`, `sistematiza`, `contrasta`). `introduce` sobre un `recurrente` es la excepción legítima — corresponde a contenido nuevo que no está declarado en el índice del curso pero que sí se introduce realmente en la unidad.
- La IA se apoya en las **descripciones detalladas** del bloque consolidado (no solo en la clasificación `principal`/`recurrente`) para asignar etiqueta.
- **Dashboard**: `principal`/`recurrente` se conserva como metadato auxiliar del evento, no como eje único de clasificación ni filtro destacado.

### §3.7. Sub-bloque `comprension` (modelo viejo) — eliminado

El sub-bloque `vocabulario_consolidado.comprension` existía en el schema F1 v10.114 (pre-rediseño). Fue **eliminado en v10.115** del schema de fase 1: el `vocabulario_consolidado` solo tiene `principal` y `recurrente`.

**Decisión para fase 2:** **eliminar toda referencia a `comprension`**. No se conserva el concepto bajo otro nombre, no se introduce una etiqueta `comprende` ni equivalente. Cuando se reescriban los scripts y `reglas-reciclaje.md` al shape nuevo, se retira sin sustituto.

---

## §4. Modelo recursivo del hilo y nivel `detalle` (paso 4 — definido 2026-05-15)

Doctrina recuperada del viejo (§2) + `viejo/marco-teorico-metodologico.md §6` + `docs/historico/B1.5-contrato-reciclaje.md`. Distingue dos ejes que el rediseño activo no había separado.

### §4.1. Dos ejes distintos: capa de procesamiento vs capa de población

- **Capa 1 / Capa 2** (§1.3) = quién procesa: script determinista vs sesión IA enriquecedora.
- **`mapa` / `auto` / `detalle`** = grado de **población del mismo hilo**.

No son lo mismo. Un único hilo por contenido editorial atraviesa los tres grados de población.

### §4.2. Modelo recursivo de capas del hilo

Un único hilo por contenido editorial, con tres capas progresivas y acumulativas:

| Capa | Origen | Información que añade |
|---|---|---|
| `mapa` | `nc1-curso.json` (índice editorial) | Esqueleto: identidad del hilo (id, título, tipo) + eventos básicos `(unidad, sección)`. Nombres inmutables. |
| `auto` | Inventarios fase 1 (4 bloques top-level consolidados + 4 listas tipadas por actividad/cuadro) | Enriquece los eventos: contenidos concretos por unidad, etiquetas (§2.3 + `discrimina` en pron/orto), referencias canónicas. |
| `detalle` | Análisis lingüístico-pedagógico cross-unidad sobre el inventario | Justifica el procedimiento didáctico (§4.4). |

El campo `nivel_analisis` **no clasifica el hilo** en tres tipos paralelos — indica el **grado de población** que ese hilo ya tiene. El hilo nace en `mapa`, se enriquece a `auto`, se completa a `detalle`. Recursivo y acumulativo, no paralelo.

### §4.3. Función del reciclaje: catálogo acumulativo

`nc1-reciclaje.json` es un **catálogo acumulativo** de contenidos reciclados a lo largo del curso. Criterios documentados (no inventados):

- **Conexión natural con el contenido nuevo** (`B1.5-contrato-reciclaje.md`).
- **Refuerzo o requisito** para aprender lo nuevo (idem).
- **No se recicla todo**: solo los **5-6 elementos de mayor impacto** por unidad (idem).
- **Dosificación 70/30**: ~70% contenido nuevo de la unidad + ~30% reciclaje (`marco-teorico-metodologico.md §6`).
- **Análisis contextual, no tabla fija**: "lo que se recicla depende de lo que se va a enseñar" (idem).

### §4.4. Nivel `detalle`: justificación lingüístico-pedagógica

`detalle` **no añade más contenido** al hilo. Añade **explicación del procedimiento didáctico** fundamentada en la **lógica lingüística** del proceso de enseñanza.

**Qué expone para cada evento:**

- **Cadena de prerrequisitos lingüísticos**: para enseñar X aquí, antes hizo falta enseñar A, B, C. Justificado en la lógica lingüística, no en intuición editorial.
- **Justificación**: por qué esos prerrequisitos son condición (qué estructura, regla o léxico los hace necesarios).
- **Relaciones**: cómo el contenido se conecta con otros del curso — no solo "antes/después", sino qué dependencia lingüística los vincula.

**Representación interna**: nodos enlazados. Cada evento del hilo = un nodo con su análisis lingüístico-pedagógico asociado. Los enlaces entre nodos materializan el procedimiento: "en U[n] introduce X · en U[m] recupera X · en U[k] amplía X · en U[p] contrasta X con Y" — siempre con la justificación lingüística detrás de cada paso.

**Representación en el dashboard**: la tabla actual del reciclaje **se mantiene** (es adecuada para mapa/auto). El nivel `detalle` **no se intenta hacer navegable dentro de la tabla** (sería inviable). Se abre como **modal a página completa** desde el hilo: una apertura sobre toda la página, no una columna lateral. El editor entra en el modal, navega el grafo de nodos-enlaces lingüísticos, y vuelve a la tabla.

### §4.5. Quién pobla cada capa

- `mapa` → Capa 1 (script determinista, desde `nc1-curso.json`).
- `auto` → Capa 1 (script determinista, desde los 4 bloques consolidados del inventario) + Capa 2 IA para asignar etiquetas según §2.3 y §3.
- `detalle` → Capa 2 IA. Procedimiento concreto (qué prompt, qué inputs, cómo se persiste) pendiente de definir en pasos siguientes.

---

## §5. Hoja de ruta — trabajo pendiente (definida 2026-05-20)

Inventario vivo de lo que falta para cerrar el rediseño de fase 2 al estándar de fase 1 (contrato operativo completo, no solo modelo conceptual). Ordenado en **cuatro niveles**; cada nivel se aborda cuando el anterior está suficientemente cerrado. Las piezas se mueven a secciones propias (§6+) conforme se discuten y cierran.

### Nivel 1 — Decisiones de modelo — ✅ COMPLETO (2026-05-21)

Las decisiones de modelo están cerradas. Trayecto: alcance (v11.33) · D2/§6 · formas verbales/§7 · explicaciones/§8 · triage/§9 · D1 absorbida en §9.6 · siempre-presentes/§10.

> **Decisión de alcance — cerrada 2026-05-20.** `comunicacion` (funciones comunicativas) y `estrategia` quedan **fuera del rediseño actual de fase 2**: son desarrollo **posterior**. El rediseño vigente cubre solo los bloques lingüísticos del inventario — vocabulario, gramática, pronunciación/ortografía, verbal y `perifrasis`. Registrado en la bitácora de `PROCESO-MAESTRO.md`.

**Único residuo del Nivel 1 — P1.** Decisión heredada del viejo, cerrada en **opción A** (2026-05-10): los datos enriquecidos viven en `nc1-reciclaje.json`, regenerado al integrar cada unidad. Falta **ratificarla/formalizarla** en el Nivel 2 (contrato de regeneración) — no es una decisión abierta, es un trámite de formalización.

### Nivel 2 — Contrato operativo a producir

Lo que falta **escribir** para que fase 2 tenga el mismo estándar de contrato que fase 1.

- ✅ **Schema / contrato de `nc1-reciclaje.json`** — `fases/2-reciclaje/schema-reciclaje.md`, creado en v11.45. Shape del top-level (`_meta` + `hilos[]` + `propuestas[]`), del hilo (`id` slug estable, `bloque`, `titulo`, `_grupo`, `nivel_analisis`, `eventos`, `detalle`), del evento, de `explicacion` y de la propuesta. Funcional para JSON y para BD. `detalle` con contrato mínimo (nodos/enlaces); shape fino diferido al diseño del modal. *(Nota (§8.4) absorbida: pendiente precisar la serialización de `que_dice_el_libro` con cuadros de contenido estructurado, al cerrar el sub-contrato del `detalle`.)*
- **Persistencia de las decisiones de la Capa 2 IA** — ✅ resuelta de paso por el schema: bloque `propuestas[]` top-level (cola con `estado` pendiente/aceptada/rechazada).
- **Prompt envoltorio de fase 2** por unidad (entry point operativo).
- ✅ **Reglas operativas reescritas** — `reglas-reciclaje.md` reescrito al modelo §1-§10 en v11.46. Es la autoridad decisional estable de fase 2 (granularidad, naming, etiquetas, triage, anticipación, formas verbales, explicación, siempre-presentes, marcas, `@R`, cuándo escalar). Sin lógica de scripts (es Nivel 3) ni narrativa de transición.
- **Comandos de validación + criterio de cierre** — qué se ejecuta y qué gate certifica que el reciclaje de una unidad está cerrado.
- **Ratificación formal de P1** — confirmar opción A y formalizar el contrato de regeneración.

### Nivel 3 — Implementación de Capa 1 y Capa 2

- **Procedimiento concreto de Capa 1** (script determinista): qué genera, en qué orden. **Nota (§7.4):** el desglose de `formas` por unidad exige leer `actividad.tiempos_y_verbos`, no solo el consolidado agregado — tenerlo presente al diseñar Capa 1.
- **Validador cross-unidad R1-R5** — reglas de validación cruzada. Material heredado en el **Reservorio §R.1**, pendiente de procesar.
- **Sesión IA de Capa 2** — cómo se ejecuta el enriquecimiento, qué inputs recibe.
- **Wiring** — encadenado de Capa 1 → Capa 2 → integración.

### Nivel 4 — Reactivación operativa

Fase 2 está PAUSADA. Reactivar exige, en este orden:

1. **Adaptar los 2 scripts** `regenerar_reciclaje_*.py` del shape viejo (v10.114) al shape de fase 1 actual.
2. **Implementar el validador cross-unidad** (R1-R5).
3. **Regenerar `nc1-reciclaje.json` íntegro** (181 hilos hoy congelados).
4. **Sincronizar dashboard + docs raíz** — vista de reciclaje del dashboard (incluido el modal `detalle` de §4.4) y actualización de `CLAUDE.md` de fase 2, `CLAUDE.md` raíz, `REVIEW.md`, `PROCESO-MAESTRO.md`.

---

## §6. D2 — Universo de hilos válidos y sub-organización de gramática (paso 6 — definido 2026-05-20)

Cierra la pieza D2. La formulación vieja (lista PCIC curada de ~55 subcategorías) queda **obsoleta**.

### §6.1. Universo de hilos válidos

El universo de títulos de hilo válidos de fase 2 = **los 4 registries canónicos de fase 1** (`campos-semanticos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`, `verbos-canonicos.json`) **+ el registry derivado `perifrasis-canonicas.json`** (5.º, propio de fase 2 — ver §6.2). Fase 2 **no cura un universo libre**: hereda los 4 de fase 1 y solo añade el derivado de perífrasis.

- **Cerrado para escritura**: fase 2 no inventa un título canónico. Si no está en uno de los 5 registries, fase 2 no lo crea.
- **Abierto para detección**: si fase 2, al analizar en profundidad, surfacea una **estructura no declarada** en ningún registry, eso es un **hallazgo legítimo** que se escala al autor (misma política que §10 "siempre presentes"). No se inventa, no se rechaza: se propone.

### §6.2. Perífrasis — 5.º registry

Las perífrasis verbales (§3.3) pasan a tener registry propio: **`perifrasis-canonicas.json`** (5.º registry). Universo cerrado también para perífrasis. Se poblará desde el campo `estructura_perifrastica` de los inventarios + PCIC A1.

Esto **cierra la incoherencia §2.2↔§3.3**: la tabla de bloques de §2.2 pasa de 4 a 5 bloques (ver §2.2 actualizada).

### §6.3. Bloque gramática — sub-organización por `_grupo`

El bloque gramática gana un campo interno **`_grupo`** en cada categoría de `gramatica-canonica.json`. Eje de agrupación: **subsistema gramatical**, alineado con la estructura del PCIC A1 (estable y legible). Grupos:

- **Determinantes** — artículos determinados/indeterminados, demostrativos, posesivos.
- **Pronombres** — pronombre sujeto, átonos de OI, interrogativos.
- **Sintagma nominal y concordancia** — concordancia de género, de número, contables/incontables.
- **Construcciones** — hay, construcción gustar/doler, oposición ser/estar.
- **Tiempos y modos verbales** — ver §6.4.
- **Adverbios y marcadores** — posición, adverbios de cantidad, marcadores temporales del pasado.
- **Preposiciones**.

El dashboard lee la gramática **agrupada por `_grupo`** — favorece la lectura. `_grupo` es organización interna, no cambia la granularidad del hilo (sigue siendo la categoría gramatical).

### §6.4. Grupo "Tiempos y modos verbales"

Dentro de gramática. Contiene **dos tipos de categorías**:

1. **Flexión / paradigmas verbales** — el sistema de conjugación como contenido gramatical enseñado: paradigma de verbos regulares, paradigmas de irregularidad vocálica (e>ie, o>ue…), imperativo regular e irregular, etc.
2. **Usos de tiempos y modos** — para qué sirve cada tiempo/modo a nivel A1: presente → acciones habituales / descripción / estados; imperativo → instrucciones / peticiones; etc.

Ambos tipos se **canonizan desde el PCIC A1** (hoy no capturados) como categorías nuevas de `gramatica-canonica.json` bajo este grupo, con `_pcic_ref`.

**Distinción clave — tres planos separados:**

| Plano | Qué responde | Dónde vive |
|---|---|---|
| **Bloque `verbal`** | ¿Qué verbos concretos aparecen y cómo se conjugan? Lista grande, cada verbo del libro. | Apartado propio (bloque `verbal`, granularidad lema) |
| **Grupo "Tiempos y modos verbales"** | ¿Qué reglas de conjugación y qué usos de tiempo/modo enseña el libro? Sistema verbal abstracto. | Dentro del bloque `gramatica` |
| **Grupo "Construcciones"** | hay, gustar/doler, ser/estar. | Dentro del bloque `gramatica` |

El bloque `verbal` responde "¿qué verbos y cómo se conjugan?"; el grupo "Tiempos y modos verbales" responde "¿qué reglas y usos?". Planos distintos, no se fusionan.

### §6.5. Sincronizaciones pendientes que arrastra D2

D2 queda cerrado como decisión de modelo, pero deja dos costuras con el contrato operativo de alrededor — anotadas aquí para no perderlas:

1. **Fuente real de perífrasis anticipatorias.** §6.2 dice que `perifrasis-canonicas.json` se poblará desde `estructura_perifrastica` del inventario. Pero el contrato vigente de fase 1 **excluye de `tiempos_y_verbos` los auxiliares de aparición anticipatoria** (`reglas-operativas.md §5.2`, `glosario.md`), y con el auxiliar se excluye la perífrasis. Es decir: una perífrasis que aparece antes de que su auxiliar sea canónico **no viaja** por `estructura_perifrastica`. **Resuelto en §7.3** (modelo híbrido): fase 2 lee el registro transitorio de anticipaciones (`_migracion_rediseno` / `_fixture_exploratoria`) y completa el análisis por su cuenta. La perífrasis anticipatoria se recupera por esa vía, sin depender de que `estructura_perifrastica` la transporte.
2. **Contrato corto de fase 2 desactualizado.** El `CLAUDE.md` de fase 2 aún describe el nivel `auto` desde `vocabulario_consolidado` y la regla "un hilo por campo semántico" — anterior al modelo de 5 bloques. Sincronizado parcialmente en v11.38; revisión completa cuando fase 2 se reactive.

### §6.6. Tareas de población diferidas

§6 **decide y documenta** el modelo; no ejecuta cambios de registry ahora. Quedan como tareas posteriores (tocan registries de fase 1, listadas en §5):

- Crear y poblar `perifrasis-canonicas.json`.
- Añadir el campo `_grupo` a las 17 categorías de `gramatica-canonica.json`.
- Canonizar desde PCIC A1 las categorías nuevas del grupo "Tiempos y modos verbales" (flexión + usos).

---

## §7. Tratamiento detallado de formas verbales (paso 7 — definido 2026-05-21)

Detalla el bloque `verbal` del modelo. Resuelve cómo se representa la **progresión del paradigma** y cierra la costura de perífrasis anticipatoria de §6.5.

### §7.1. El evento verbal lleva las formas concretas

El hilo verbal es por **lema** (§3.2); el evento es por **lema-tiempo-unidad**. El evento lleva un campo **`formas`**: la lista de formas conjugadas concretas que esa unidad trabaja de ese lema en ese tiempo.

```json
{
  "bloque": "verbal", "titulo": "ser",
  "eventos": [
    { "unidad": 1, "tiempo": "Presente", "etiquetas": ["introduce"],
      "formas": ["soy", "eres", "es"] },
    { "unidad": 2, "tiempo": "Presente", "etiquetas": ["amplia"],
      "formas": ["somos", "sois", "son"] }
  ]
}
```

- La **forma concreta es dato del evento**, no una sub-entidad con recorrido propio (opción A del diseño). No se rastrea cada forma individual a lo largo del curso.
- La **progresión del paradigma** se lee comparando los `formas` de eventos sucesivos del mismo hilo: en el ejemplo, U1 introduce el singular y U2 amplía al plural.
- Fuente: `formas_trabajadas` del inventario (hoy lista plana agregada por lema) + las formas declaradas en `actividad.tiempos_y_verbos` por unidad, que permiten desglosar por unidad.
- *Nota:* este shape es el punto de partida; podrá enriquecerse más adelante (p. ej. anotar persona) si el análisis lo pide.

### §7.2. `rasgo_por_tiempo` se queda en el hilo verbal

El atributo `rasgo_por_tiempo` del inventario (comportamiento morfológico del lema: `regular -ar`, `irregularidad vocálica o→ue`, `totalmente irregular`…) **se mantiene en el hilo verbal**, como atributo del lema. No migra al grupo gramatical "Tiempos y modos verbales" (§6.4).

Frontera con §6.4: `rasgo_por_tiempo` describe **este lema concreto** (cómo se conjuga `poder`); el grupo gramatical "Tiempos y modos verbales" modela la **flexión abstracta como contenido enseñado** (la regla "irregularidad vocálica o→ue" como paradigma que el libro presenta). Son dos planos: atributo del verbo concreto vs contenido gramatical. No se fusionan; pueden referenciarse.

### §7.3. Anticipación de formas — modelo híbrido

Fase 1 **no registra** en el consolidado las formas cuyo lema es canónico de una unidad posterior; las anota, con poco detalle, en `_migracion_rediseno.anticipaciones_detectadas_para_fase_2` o en `_fixture_exploratoria`.

**Fase 2 opera en modelo híbrido:** **lee** ese registro transitorio de anticipaciones **y decide** — como la anotación de fase 1 es escueta, fase 2 completa el análisis re-mirando las actividades de la unidad y genera el evento correspondiente con etiqueta `anticipacion`.

Esto **cierra la costura §6.5 punto 1**: la perífrasis anticipatoria (auxiliar cuyo lema es posterior, hoy excluida de `tiempos_y_verbos` y de `estructura_perifrastica`) se recupera por la misma vía — fase 2 la detecta vía el registro de anticipaciones + análisis propio, no depende de que `estructura_perifrastica` la transporte.

### §7.4. Tareas diferidas

- El desglose de `formas` por unidad depende de leer `actividad.tiempos_y_verbos` (no solo el consolidado agregado): se concreta al implementar la Capa 1 (§5 Nivel 3).
- La lectura del registro de anticipaciones (`_migracion_rediseno`) es una marca **transitoria** de fase 1; cuando fase 1 cierre esa deuda, fase 2 ajusta la fuente.

---

## §8. Carril de explicaciones — el evento lleva la explicación analizada (paso 8 — definido 2026-05-21)

Resuelve dónde vive la **explicación** que el libro da de un contenido (el cuadro "cómo se forma X", "cuándo se usa Y").

### §8.1. La explicación es un atributo del evento, no un hilo propio

Un solo hilo por contenido. Donde el libro explica el contenido, el **evento de esa unidad lleva un campo `explicacion`**. No se crea un hilo aparte "Explicación de X" — duplicaría el recorrido del hilo de la categoría.

```json
{
  "bloque": "gramatica", "titulo": "Oposición ser / estar",
  "eventos": [
    { "unidad": 5, "etiquetas": ["introduce", "sistematiza"],
      "explicacion": {
        "que_dice_el_libro": "ser para identidad/características; estar para ubicación/estado",
        "fuente": "cuadro@p47",
        "analisis_ia": "Requiere adjetivos descriptivos (U1) y locuciones de lugar (U5). El libro no contrasta casos límite."
      } },
    { "unidad": 7, "etiquetas": ["aplica"] }
  ]
}
```

### §8.2. El campo `explicacion` tiene dos partes

- **`que_dice_el_libro`** — lo que el cuadro expone literalmente. Es válido tenerlo, pero **no es el trabajo de fase 2**.
- **`analisis_ia`** — **el trabajo de fase 2**: relaciones lógicas, prerrequisitos, coherencia, incoherencias detectadas. Aquí está el valor. La fuente (el cuadro) puede ser pobre o escueta; fase 2 no se limita a copiarla — la analiza en profundidad.

### §8.3. Alcance — los 5 bloques

El campo `explicacion` aplica a **cualquier bloque** (vocabulario, gramática, pron/orto, verbal, perífrasis) cuyo contenido el libro explique con un cuadro. No es exclusivo de gramática.

### §8.4. Evidencia

Cuadros del inventario con el `tipo_cuadro` correspondiente — `cuadro.titulo` + `cuadro.contenido`. La evidencia alimenta `que_dice_el_libro`; el `analisis_ia` lo produce la Capa 2 IA mirando además las relaciones cross-unidad.

### §8.5. Relación con el nivel `detalle` (§4.4)

No se solapan:

- El **`analisis_ia` del `explicacion`** es **local a un evento** — analiza la explicación de ese contenido en esa unidad.
- El **nivel `detalle`** (§4.4) es la justificación lingüístico-pedagógica de **todo el hilo / la cadena cross-unidad** — el recorrido completo.

El `que_dice_el_libro` y los `analisis_ia` de los eventos son **insumos** que el nivel `detalle` usa para razonar la cadena completa. El cuadro es material; el `detalle` razona sobre él.

---

## §9. Triage índice — estatus de cada contenido por evento (paso 9 — definido 2026-05-21, generalizado a los 5 bloques en v11.43)

Aplica a **los 5 bloques** (vocabulario, gramática, pron/orto, verbal, perífrasis). Cada vez que un contenido aparece en una unidad, el triage determina su estatus respecto al índice editorial del curso (`nc1-curso.json`). La lógica "¿declarado / reconciliable / nuevo?" no es específica de gramática — vale para cualquier contenido.

### §9.1. Las tres salidas

1. **Declarado literal** — el contenido coincide con una entrada del índice del curso para esa unidad.
2. **Reconciliable** — no está literal en el índice, pero es el **mismo contenido** que una entrada del índice declarada con otro nombre.
3. **Contenido nuevo real** — aparece en el libro pero **no está en el índice** y **no es reconciliable** con ninguna entrada. Contenido que el libro trae sin que el índice lo declare.

Lo no declarado **no se vuelca a "nuevo" por defecto**: se analiza en detalle para distinguir reconciliable de nuevo real.

### §9.2. Quién aplica cada salida

Principio de eficiencia: aprovechar lo que fase 1 ya resuelve; desarrollar en fase 2 solo lo que falte.

- **Declarado literal** → **precomputable por la Capa 1** (coincidencia mecánica con el índice del curso). No requiere IA.
- **Reconciliable** → **Capa 2 IA propone** la reconciliación; el **humano cierra**.
- **Contenido nuevo real** → **Capa 2 IA genera una propuesta al autor** ("detectada esta categoría no declarada — ¿canonizar en el registry de fase 1 o dejarla como hallazgo?"). Decide el autor. Mismo tipo de hallazgo que §10 "siempre presentes".

Reconciliaciones y categorías nuevas son siempre **propuestas** (IA propone / humano cierra), nunca decisiones automáticas de fase 2.

### §9.3. Granularidad — por evento

El estatus del triage se marca **por evento** (categoría-unidad), **no** una sola vez por categoría. Una misma categoría puede tener estatus distinto según la unidad: p. ej. "Marcadores temporales del pasado" está declarada en el índice de U9 (→ `declarado`) pero puede aparecer de pasada en U3 (→ `nuevo` / anticipación).

### §9.4. Registro en el evento

El evento del hilo lleva un campo **`procedencia_indice`** con valor `declarado` | `reconciliado` | `nuevo`. Si es `reconciliado`, se anota además a qué entrada del índice equivale. El campo es resultado de propuesta — la parte no mecánica (reconciliado/nuevo) queda pendiente de cierre humano.

### §9.5. `procedencia_indice` y `etiquetas` son dos ejes ortogonales

El triage **añade un eje nuevo** al evento; no sustituye ni se mezcla con las etiquetas de §2.3. Un evento lleva **los dos**:

| Eje | Valores | Qué responde |
|---|---|---|
| `etiquetas` (§2.3) | introduce, amplia, aplica, sistematiza, contrasta, anticipacion (+ discrimina en pron/orto) | ¿Qué **hace** la unidad con el contenido? |
| `procedencia_indice` (§9) | declarado, reconciliado, nuevo | ¿Qué **estatus** tiene respecto al índice del curso? |

Ejemplos de combinación: `etiquetas: ["amplia"]` + `procedencia_indice: "declarado"`; `etiquetas: ["anticipacion"]` + `procedencia_indice: "nuevo"`.

### §9.6. D1 — tabla de equivalencias: absorbida en §9

La pieza **D1** del rediseño viejo (`nc1-equivalencias-hilos.json`, una tabla curada a mano que vinculaba títulos del índice con campos de los inventarios por equivalencia semántica) **queda absorbida por el triage**. Ya no hace falta un archivo de equivalencias curado: la reconciliación índice↔canónico es la salida `reconciliado` del triage §9, y el triage aplica a los 5 bloques. La equivalencia se resuelve evento a evento como propuesta IA con cierre humano, no como tabla estática previa.

---

## §10. Componentes "siempre presentes no indexados" (paso 10 — definido 2026-05-21)

Procesa el material heredado del viejo §8 (antes en el Reservorio §R.2) y lo reconcilia con el modelo §1-§9. Cierra la última pieza conceptual del Nivel 1.

### §10.1. Definición

Componentes lingüísticos que aparecen **sistemáticamente** en el corpus de NC1 pero que el libro **NO enseña como contenido** del índice editorial (`nc1-curso.json`). Su omnipresencia es un fenómeno cross-unidad; su tratamiento canónico no es trivial.

### §10.2. Es un patrón cross-unidad del triage §9

Un "siempre presente" **no es un mecanismo aparte**: es un componente que el triage §9 marcaría `nuevo` (no declarado en el índice) **de forma sistemática, en muchas o todas las unidades**. §10 es la **lectura agregada** del triage — el mecanismo que reconoce ese patrón cross-unidad. Un `nuevo` aislado es un hallazgo puntual; un `nuevo` recurrente curso a curso es un "siempre presente".

### §10.3. Detección — Capa 2 IA en los hitos cross-unidad

La detección la hace la **Capa 2 IA** en los **hitos cross-unidad** (§1.4 — cada 3 unidades / cierre global), cuando ya hay varias unidades acumuladas para que el patrón sea visible. No se detecta procesando una unidad aislada.

### §10.4. Qué se hace — propuesta al autor con tres salidas

La Capa 2 IA genera una **propuesta al autor**, con evidencia (frecuencia, distribución por unidades, función pragmática vs gramatical). Tres salidas posibles, decide el autor caso por caso:

- **(a)** Canonizar como **categoría cross-unidad** en el registry de fase 1 que corresponda.
- **(b)** Modelarlo como **bloque analítico transversal** propio de `nc1-reciclaje.json`.
- **(c)** **Ignorarlo** si no aporta valor de análisis.

### §10.5. Criterio de ampliación de la lista

Un candidato nuevo entra en la lista de "siempre presentes" cuando se cumplen las tres condiciones: (1) **presencia sistemática cross-unidad**, (2) **no declarado** en el índice editorial, (3) **función pragmática / de input**, no contenido enseñado. La Capa 2 IA lo propone en un hito cross-unidad; el autor confirma la incorporación.

### §10.6. Lista inicial de candidatos (detectados durante v10.117)

| Candidato | Evidencia | Pregunta para fase 2 |
|---|---|---|
| Conjunciones copulativas (`y`, `e`) | Omnipresentes como coordinador de constituyentes | ¿Categoría gramatical cross-unidad o input pragmático? |
| Conjunciones disyuntivas (`o`, `u`) | Frecuentes en cuestionarios y opciones | Idem |
| Adverbios de afirmación y negación (`sí`, `no`, `también`, `tampoco`) | "sí"/"no" omnipresentes desde U1; "también"/"tampoco" tardíos | ¿Se separan por momento de aparición? |

### §10.7. Política operativa

1. **Fase 1 no los canoniza automáticamente.** Si una extracción surfacea uno con anclaje material claro, se escala al autor por §0.1.
2. **Fase 2 los detecta como patrón** al agregar inventarios cross-unidad — produce un `hallazgo`/propuesta, no una modificación silenciosa de ningún registry.
3. **El autor decide** caso por caso entre las tres salidas de §10.4.
4. **Si el autor canoniza** (salida a), se añade al registry de fase 1 con `_pcic_ref` y `_apariciones`, y se actualiza `_meta.siempre_presentes_no_indexados` del registry para retirar el candidato.

---

## §N. Apéndice — Disposición de las piezas del REDISEÑO-EN-CURSO-viejo.md

El viejo se archivó en `docs/historico/REDISEÑO-EN-CURSO-viejo.md` (v11.34). Esta tabla cierra la disposición final de cada una de sus piezas. Tres estados: **ya migrado** (absorbido en una sección del activo), **superado en su formulación vieja** (la pieza sigue viva pero su versión vieja no sirve; se redefine en el activo), **en reservorio** (material vivo sin procesar, copiado al Reservorio de este documento).

| Pieza del viejo | Estado | Disposición |
|---|---|---|
| §1 Punto de partida (el problema) | Obsoleto | Diagnóstico histórico que motivó el rediseño. No se migra. |
| §2 Modelo objetivo (mapa/auto/detalle) | Ya migrado | Absorbido en §4 (modelo recursivo del hilo). |
| §3 · D1 — Tabla de equivalencias canónica | Cerrado en §9.6 | La tabla curada (`nc1-equivalencias-hilos.json`) queda obsoleta. La reconciliación índice↔canónico la hace el triage §9 (salida `reconciliado`), aplicado a los 5 bloques. No se crea archivo de equivalencias. |
| §3 · D2 — Universo cerrado de hilos válidos | Cerrado en §6 | La formulación vieja (lista PCIC curada) queda obsoleta. Redefinido en §6: universo = los 5 registries de fase 1 (4 + `perifrasis-canonicas.json`), cerrado para escritura y abierto para detección. |
| §3 · D3 — Disparador de regeneración: Claude Code | Ya migrado | Reformulado y absorbido en §1.5 (régimen temporal dual). |
| §4 · P1 — Almacenamiento de datos enriquecidos | Ya migrado | Decidido en opción A (2026-05-10); reflejado en §5 Nivel 1 como decisión heredada a ratificar. |
| §5 Hallazgos del revisor | Obsoleto | Un solo hallazgo, ya cerrado por D1+D2. No se migra. |
| §6 Pasos de migración | Obsoleto | Reemplazado por la hoja de ruta de §5. No se migra. |
| §7 · R1-R5 validación cruzada cross-unidad | En reservorio | Material vivo sin procesar. Copiado al Reservorio. Se procesará en §5 Nivel 3. |
| §8 · Componentes "siempre presentes no indexados" | Cerrado en §10 | Procesado: §10 lo reconcilia con el triage (patrón cross-unidad de `nuevo`), define detección, salidas y criterio de ampliación. |

---

## §R. Reservorio — material heredado sin procesar

> **Procedencia:** copiado **verbatim** de `REDISEÑO-EN-CURSO-viejo.md` §7 y §8 al archivar ese documento (v11.34, 2026-05-20).
> **Estado:** material vivo **sin procesar**. Al procesarse, cada bloque se mueve a una sección propia y se retira de aquí. El antiguo §R.2 (siempre-presentes) se procesó como §10 (v11.44); queda solo §R.1.

### §R.1 — Capa 1: Validación cruzada cross-unidad (heredado del viejo §7, cerrado en diseño 2026-05-12)

> **Origen:** decisiones derivadas del rediseño de fase 1 que requieren chequeos cross-unidad. Estas reglas viven en el validador `scripts/validar_inventarios_cross.py` (capa 1 del pipeline de fase 2 redefinida).
>
> **Nota:** este bloque sustituye conceptualmente al viejo modelo "mapa + auto" en lo relativo a coherencia cross-unidad. La materialización (código del validador) se hace en E4a del plan del rediseño de fase 1, no aquí.

**R1 — Detección de anticipación de léxico.** *Premisa:* fase 1 codifica `recurrente` solo si el léxico aparece con frecuencia, no está en el índice de la propia unidad, **y** no es canónico en una unidad posterior. Lo que cumple las dos primeras condiciones pero falla la tercera lo deja silenciosamente fuera. Fase 2 lo detecta y reporta. *Algoritmo:* (1) leer el índice editorial completo (`nc1-curso.json`); (2) leer el `principal` de cada inventario; (3) leer el `recurrente` de cada inventario; (4) re-ejecutar análisis de frecuencias — para cada término frecuente que no está en `principal` ni `recurrente` de U(n): si es canónico en U(n+k) posterior → alerta de anticipación; si es canónico solo en U(n−k) anterior o en ninguna → no es alerta. *Output:* alertas `{unidad, termino, unidad_canónica, frecuencia, ejemplos}`.

**R2 — Detección de inventos** (validación intra-unidad asumida como pre-condición). "No inventar palabras" es regla de fase 1. Fase 2 ejecuta un chequeo redundante: cada palabra de `vocabulario_consolidado` debe aparecer literalmente en alguna actividad/cuadro de la unidad. Si falla, indica bug del extractor.

**R3 — Detección de errores de clasificación semántica.** Fase 2 usa el canon (`campos-semanticos-canonicos.json`) para detectar palabras mal categorizadas (ej. `campeón` en `Nacionalidades`). Regla intra-unidad de fase 1; fase 2 la usa como sanity check post-extracción.

**R4 — Inconsistencias de progresión** (regla preexistente): léxico `recurrente` en U(n) que no fue `principal` en ninguna U(n−k); dos unidades con nombres distintos para el mismo contenido semántico; verbos en `vocabulario_consolidado` que deberían vivir en `tiempos_y_verbos_consolidado`.

**R5 — Coherencia bidireccional de trazabilidad** (asumida como pre-condición). La coherencia entre `actividad.X` y `top-level.X.fuentes` la chequea el validador intra-unidad de fase 1. Fase 2 la asume y aborta si no se cumple.

*Estado heredado:* diseño de reglas cerrado el 2026-05-12; implementación en `validar_inventarios_cross.py` pendiente.

> El antiguo §R.2 (componentes "siempre presentes no indexados") **se procesó en v11.44** y vive ahora como sección propia **§10**.

---

## Histórico de versiones del documento activo

- **2026-05-15 (v10.126)** — Documento creado tras renombrar el viejo `REDISEÑO-EN-CURSO.md` → `REDISEÑO-EN-CURSO-viejo.md`. Contiene paso 1 cerrado (modelo de trabajo) + placeholders + apéndice de aprovechamiento.
- **2026-05-15 (v10.119)** — §2 cerrado: modelo de análisis por unidad (3 momentos: intra / cross-atrás / cross-adelante), granularidad por bloque, 6 etiquetas coexistentes, esbozo del shape del hilo.
- **2026-05-15 (v10.133)** — §3 cerrado: cobertura por bloque y tratamiento de marcas. Pron/orto (categoría + `discrimina`), verbal (lema, evento por lema-tiempo), perífrasis (hilo aparte), política de marcas internas (`_pendiente_canon` no bloquea, `_funcion_ambigua` a chat, `_decisiones_ia` lectura crítica). §3.5 (sufijo `@R` se preserva sin tratamiento diferencial) y §3.6 (`principal`/`recurrente` no dicta etiqueta del evento) cerrados en mismo paso. §3.7: sub-bloque `comprension` eliminado sin sustituto.
- **2026-05-21 (v11.46)** — Nivel 2: `reglas-reciclaje.md` reescrito íntegro del modelo viejo (campo_semantico, acción única, scripts) al modelo §1-§10 — autoridad decisional estable de fase 2 (§1-§11). Sincronizado el `CLAUDE.md` de fase 2 (cruces a las nuevas secciones, terminología acción→etiquetas).
- **2026-05-21 (v11.45)** — Nivel 2 arranca: creado `schema-reciclaje.md` (documento de contrato aparte, espeja `schema-inventario.md` de fase 1). Shape canónico de `nc1-reciclaje.json` — `_meta` + `hilos[]` (con `id` slug estable) + `propuestas[]`. Funcional para JSON y BD. Resuelve de paso la pieza "persistencia de decisiones IA" (bloque `propuestas[]`). `detalle` con contrato mínimo, shape fino diferido.
- **2026-05-21 (v11.44)** — §10 cerrado: componentes "siempre presentes no indexados" procesados del Reservorio §R.2. Reconciliados como patrón cross-unidad del triage §9 (un `nuevo` sistemático). Detección por la Capa 2 IA en hitos cross-unidad; tres salidas de propuesta al autor (canonizar / bloque analítico / ignorar); criterio de ampliación definido. **Nivel 1 del roadmap COMPLETO** (residuo: ratificación formal de P1 en Nivel 2). Reservorio: queda solo §R.1.
- **2026-05-21 (v11.43)** — §9 generalizado a los 5 bloques (el triage no era específico de gramática). Nueva §9.5 (`procedencia_indice` y `etiquetas` son dos ejes ortogonales del evento) y §9.6 (D1 absorbida: la tabla de equivalencias curada queda obsoleta, la reconciliación la hace el triage). D1 cerrado — Nivel 1 del roadmap completo salvo §R.2.
- **2026-05-21 (v11.42)** — §9 cerrado: triage índice. Tres salidas por evento (`declarado` / `reconciliado` / `nuevo`) para gramática y pron/orto. Declarado literal lo precomputa la Capa 1; reconciliable y nuevo son propuestas de la Capa 2 IA con cierre humano. Estatus por evento (categoría-unidad), registrado en `procedencia_indice`. Anclada en §5 Nivel 2 la nota de serialización de `que_dice_el_libro` (§8.4).
- **2026-05-21 (v11.41)** — §8 cerrado: carril de explicaciones. La explicación que el libro da de un contenido es un **atributo del evento** (campo `explicacion`), no un hilo propio. Dos partes: `que_dice_el_libro` (literal del cuadro) + `analisis_ia` (el trabajo de fase 2: relaciones, lógica, incoherencias). Alcance a los 5 bloques. Insumo del nivel `detalle`, no se solapa con él. Anclada en §5 Nivel 3 la nota del desglose de `formas` para Capa 1.
- **2026-05-21 (v11.40)** — §7 cerrado: tratamiento detallado de formas verbales. El evento verbal lleva un campo `formas` (lista de formas concretas por unidad, opción A); la progresión del paradigma se lee comparando eventos. `rasgo_por_tiempo` se queda en el hilo verbal, frontera trazada con el grupo gramatical §6.4. Anticipación de formas en modelo híbrido (fase 2 lee el registro transitorio y completa el análisis) — cierra la costura §6.5 punto 1, incluida la perífrasis anticipatoria.
- **2026-05-20 (v11.38)** — Sincronización post-D2: §6.1 precisa la fórmula del universo (4 registries de fase 1 + `perifrasis-canonicas.json` derivado); nueva §6.5 anota las dos costuras que arrastra D2 (fuente de perífrasis anticipatorias, contrato corto de fase 2); `CLAUDE.md` de fase 2 sincronizado (nivel `auto` desde los 5 bloques; regla de granularidad por bloque).
- **2026-05-20 (v11.37)** — §6 cerrado (D2): universo de hilos válidos = los 5 registries de fase 1 (4 + nuevo `perifrasis-canonicas.json`), cerrado para escritura / abierto para detección. Perífrasis pasa a 5.º bloque (cierra incoherencia §2.2↔§3.3). Bloque gramática sub-organizado por `_grupo` (subsistema gramatical, 7 grupos). Grupo "Tiempos y modos verbales" — flexión/paradigmas + usos, desde PCIC A1 — distinto del bloque `verbal` (lista de verbos). §2.2 actualizada (5 bloques). Población de registries: tarea diferida.
- **2026-05-20 (v11.34)** — Integración a documento único: `REDISEÑO-EN-CURSO-viejo.md` archivado en `docs/historico/`. Su material vivo sin procesar (§7 R1-R5, §8 siempre-presentes) copiado verbatim al nuevo apéndice §R (Reservorio). Apéndice §N reescrito con la disposición final de cada pieza del viejo (ya migrado / superado en formulación vieja / en reservorio / obsoleto). D2 reetiquetado: la lista PCIC vieja queda superada, la pieza sigue viva. Referencias activas al viejo actualizadas en `PROCESO-MAESTRO.md`, `gramatica-canonica.json` y `CLAUDE.md` de fase 2.
- **2026-05-20 (v11.33)** — Decisión de alcance cerrada: `comunicacion` y `estrategia` pospuestas a desarrollo posterior. Pieza "Cierre de alcance" retirada de §5 Nivel 1 (pasa a decisión cerrada con nota destacada). Sincronizado `CLAUDE.md` de fase 2 y bitácora de `PROCESO-MAESTRO.md`.
- **2026-05-20 (v11.32)** — Corregida la incoherencia de P1: el viejo lo cerró en opción A (2026-05-10); el documento activo lo marcaba como "pendiente decisión" en §5 y en el apéndice. Reetiquetado como decisión heredada a ratificar/formalizar en ambos sitios.
- **2026-05-20 (v11.31)** — §5 añadido: hoja de ruta del trabajo pendiente en 4 niveles (decisiones de modelo · contrato operativo · implementación Capa 1/2 · reactivación). Integra cuestiones nuevas: formas verbales, carril de explicaciones gramaticales, triage declarado/reconciliable/nuevo para gramática y pron/orto, cierre de alcance de comunicación/estrategia.
- **2026-05-15 (v10.136)** — §4 cerrado: modelo recursivo del hilo (`mapa → auto → detalle` como capas acumulativas, no paralelas; distinción con Capa 1/Capa 2 de procesamiento) + función del reciclaje como catálogo acumulativo con criterios documentados (5-6 por unidad, 70/30, análisis contextual) + nivel `detalle` como justificación lingüístico-pedagógica representada como grafo de nodos-enlaces y visualizada como modal a página completa en el dashboard.
