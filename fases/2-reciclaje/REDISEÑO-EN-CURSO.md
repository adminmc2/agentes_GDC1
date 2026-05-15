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

## §3. (paso 3 — pendiente)

*(Placeholder.)*

---

## §N. Apéndice — Qué se aprovecha del REDISEÑO-EN-CURSO-viejo.md

Tabla de seguimiento de qué piezas de la versión vieja se importan al documento nuevo, cuáles se descartan y cuáles se reformulan. Se completa progresivamente con cada paso del rediseño.

| Pieza del viejo | Estado | Destino en el documento activo |
|---|---|---|
| Modelo objetivo (§2 del viejo) | Pendiente revisión | — |
| D1 — Tabla de equivalencias canónica externa | Pendiente revisión | — |
| D2 — Universo cerrado de hilos canónicos válidos | Pendiente revisión | — |
| D3 — Disparador de regeneración: Claude Code | Vigente (heredado) | Reformulado y absorbido en §1.5 (régimen temporal dual) |
| P1 — Almacenamiento de datos enriquecidos (opción A vs B) | Pendiente decisión | — |
| Capa 1 — R1-R5 validación cruzada cross-unidad | Pendiente revisión | — |
| §8 — Componentes "siempre presentes no indexados" | Vigente (registrado v10.117) | Pendiente reubicación en documento activo |
| Hallazgos del revisor (§5 del viejo) | Pendiente revisión | — |

---

## Histórico de versiones del documento activo

- **2026-05-15 (v10.126)** — Documento creado tras renombrar el viejo `REDISEÑO-EN-CURSO.md` → `REDISEÑO-EN-CURSO-viejo.md`. Contiene paso 1 cerrado (modelo de trabajo) + placeholders + apéndice de aprovechamiento.
- **2026-05-15 (v10.119)** — §2 cerrado: modelo de análisis por unidad (3 momentos: intra / cross-atrás / cross-adelante), granularidad por bloque, 6 etiquetas coexistentes, esbozo del shape del hilo.
