# Rediseño de fase 2 — modelo IA-first (versión activa)

> **Estado:** EN CONSTRUCCIÓN. Documento vivo del rediseño de fase 2 bajo modelo IA-first. Reemplaza progresivamente a `REDISEÑO-EN-CURSO-viejo.md` (versión vieja, conservada como reservorio histórico hasta que este documento cubra todo lo vigente y el viejo se archive en `docs/historico/`).
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
| Gramática | **Categoría gramatical** | `gramatica-canonica.json` + `gramatica_consolidada` del inventario |
| Pronunciación/ortografía | **Categoría pron/orto** | `pronunciacion-ortografia-canonica.json` + `pronunciacion_ortografia_consolidada` del inventario |
| Verbal | **Lema** | `verbos-canonicos.json` + `tiempos_y_verbos_consolidado[].lema` del inventario |

Vocabulario es el único bloque con granularidad de campo semántico (agrupa ítems léxicos). Los otros tres bloques bajan a la unidad atómica de su dimensión (categoría o lema).

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

### Nivel 1 — Decisiones de modelo pendientes

Lo que falta **decidir** antes de poder escribir contrato.

| Pieza | Qué resuelve |
|---|---|
| **Tratamiento detallado de formas verbales** | Separar tres planos hoy mezclados: (a) **lema**, (b) **forma verbal concreta** (yo hablo, tú hablas…), (c) **explicación gramatical** asociada al verbo. El hilo verbal debe mostrar la **progresión del paradigma** (qué personas/tiempos se trabajan por unidad). Incluye resolver la anticipación de formas (formas como input incidental antes de que el lema sea canónico). |
| **Carril propio para las explicaciones gramaticales** | La explicación/cuadro que el libro expone ("cómo se forma el presente") no es el paradigma ni la categoría suelta. Decidir si es hilo propio o atributo del hilo. Necesita espacio de análisis separado. |
| **Triage declarado / no declarado en índice** (gramática y pron/orto) | NO es un eje binario. Es un **flujo de decisión** de tres salidas para cada categoría que aparece: (1) **declarado literal** — está en el índice del curso tal cual; (2) **reconciliable** — no está literal, pero es un elemento del índice categorizado de otra forma → se reconcilia; (3) **contenido nuevo real** — no encaja en el índice de ningún modo → se escala al autor. La gramática y la pron/orto no declaradas se analizan **en detalle** antes de clasificarlas, no se vuelcan a "no declarado" por defecto. |
| **Cierre de alcance: `comunicacion` y `estrategia`** | El contrato activo (`CLAUDE.md` de fase 2) todavía nombra funciones comunicativas y estrategias como contenido que el reciclaje modela, pero el rediseño nuevo (§2-§4) no las trata de forma visible. Decidir explícitamente: ¿fase 2 las cubre, las pospone o las excluye? Sin esta decisión el alcance queda ambiguo. |
| **D1 — Tabla de equivalencias** (`nc1-equivalencias-hilos.json`) | Vincular hilos `mapa` ↔ `auto` por equivalencia semántica, no por coincidencia de texto. Decidida en el viejo, no poblada. |
| **D2 — Universo cerrado de hilos canónicos válidos** | Qué hilos pueden existir y cuáles no. |
| **P1 — Almacenamiento de datos enriquecidos** (opción A) | **Decisión heredada a ratificar/formalizar**, no pendiente: el viejo cerró P1 en **opción A** (2026-05-10) — los datos enriquecidos viven en `nc1-reciclaje.json`, regenerado al integrar cada unidad. Falta ratificarla en el modelo nuevo y formalizar el contrato de regeneración. |
| **§8 — Componentes "siempre presentes no indexados"** | Conjunciones, adverbios sí/no… Política de tratamiento. Reubicar del viejo al activo. |
| **Hallazgos del revisor** (§5 del viejo) | Revisar uno a uno e integrar o descartar. |

### Nivel 2 — Contrato operativo a producir

Lo que falta **escribir** para que fase 2 tenga el mismo estándar de contrato que fase 1.

- **Prompt envoltorio de fase 2** por unidad (entry point operativo).
- **Schema / contrato de `nc1-reciclaje.json`** — shape canónico del hilo y del evento (hoy disperso, sin documento de contrato).
- **Reglas operativas reescritas** — `reglas-reciclaje.md` está en shape viejo; reescribir al modelo IA-first.
- **Persistencia de las decisiones de la Capa 2 IA** — dónde y cómo se guardan las propuestas decisionales.
- **Comandos de validación + criterio de cierre** — qué se ejecuta y qué gate certifica que el reciclaje de una unidad está cerrado.

### Nivel 3 — Implementación de Capa 1 y Capa 2

- **Procedimiento concreto de Capa 1** (script determinista): qué genera, en qué orden.
- **Validador cross-unidad R1-R5** — reglas de validación cruzada heredadas del viejo.
- **Sesión IA de Capa 2** — cómo se ejecuta el enriquecimiento, qué inputs recibe.
- **Wiring** — encadenado de Capa 1 → Capa 2 → integración.

### Nivel 4 — Reactivación operativa

Fase 2 está PAUSADA. Reactivar exige, en este orden:

1. **Adaptar los 2 scripts** `regenerar_reciclaje_*.py` del shape viejo (v10.114) al shape de fase 1 actual.
2. **Implementar el validador cross-unidad** (R1-R5).
3. **Regenerar `nc1-reciclaje.json` íntegro** (181 hilos hoy congelados).
4. **Sincronizar dashboard + docs raíz** — vista de reciclaje del dashboard (incluido el modal `detalle` de §4.4) y actualización de `CLAUDE.md` de fase 2, `CLAUDE.md` raíz, `REVIEW.md`, `PROCESO-MAESTRO.md`.

---

## §N. Apéndice — Qué se aprovecha del REDISEÑO-EN-CURSO-viejo.md

Tabla de seguimiento de qué piezas de la versión vieja se importan al documento nuevo, cuáles se descartan y cuáles se reformulan. Se completa progresivamente con cada paso del rediseño.

| Pieza del viejo | Estado | Destino en el documento activo |
|---|---|---|
| Modelo objetivo (§2 del viejo) | Pendiente revisión | — |
| D1 — Tabla de equivalencias canónica externa | Pendiente revisión | — |
| D2 — Universo cerrado de hilos canónicos válidos | Pendiente revisión | — |
| D3 — Disparador de regeneración: Claude Code | Vigente (heredado) | Reformulado y absorbido en §1.5 (régimen temporal dual) |
| P1 — Almacenamiento de datos enriquecidos | Decidido en el viejo (opción A, 2026-05-10) | Heredado a ratificar/formalizar — listado en §5 Nivel 1 |
| Capa 1 — R1-R5 validación cruzada cross-unidad | Pendiente revisión | — |
| §8 — Componentes "siempre presentes no indexados" | Vigente (registrado v10.117) | Pendiente reubicación en documento activo |
| Hallazgos del revisor (§5 del viejo) | Pendiente revisión | — |

---

## Histórico de versiones del documento activo

- **2026-05-15 (v10.126)** — Documento creado tras renombrar el viejo `REDISEÑO-EN-CURSO.md` → `REDISEÑO-EN-CURSO-viejo.md`. Contiene paso 1 cerrado (modelo de trabajo) + placeholders + apéndice de aprovechamiento.
- **2026-05-15 (v10.119)** — §2 cerrado: modelo de análisis por unidad (3 momentos: intra / cross-atrás / cross-adelante), granularidad por bloque, 6 etiquetas coexistentes, esbozo del shape del hilo.
- **2026-05-15 (v10.133)** — §3 cerrado: cobertura por bloque y tratamiento de marcas. Pron/orto (categoría + `discrimina`), verbal (lema, evento por lema-tiempo), perífrasis (hilo aparte), política de marcas internas (`_pendiente_canon` no bloquea, `_funcion_ambigua` a chat, `_decisiones_ia` lectura crítica). §3.5 (sufijo `@R` se preserva sin tratamiento diferencial) y §3.6 (`principal`/`recurrente` no dicta etiqueta del evento) cerrados en mismo paso. §3.7: sub-bloque `comprension` eliminado sin sustituto.
- **2026-05-20 (v11.32)** — Corregida la incoherencia de P1: el viejo lo cerró en opción A (2026-05-10); el documento activo lo marcaba como "pendiente decisión" en §5 y en el apéndice. Reetiquetado como decisión heredada a ratificar/formalizar en ambos sitios.
- **2026-05-20 (v11.31)** — §5 añadido: hoja de ruta del trabajo pendiente en 4 niveles (decisiones de modelo · contrato operativo · implementación Capa 1/2 · reactivación). Integra cuestiones nuevas: formas verbales, carril de explicaciones gramaticales, triage declarado/reconciliable/nuevo para gramática y pron/orto, cierre de alcance de comunicación/estrategia.
- **2026-05-15 (v10.136)** — §4 cerrado: modelo recursivo del hilo (`mapa → auto → detalle` como capas acumulativas, no paralelas; distinción con Capa 1/Capa 2 de procesamiento) + función del reciclaje como catálogo acumulativo con criterios documentados (5-6 por unidad, 70/30, análisis contextual) + nivel `detalle` como justificación lingüístico-pedagógica representada como grafo de nodos-enlaces y visualizada como modal a página completa en el dashboard.
