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

## §2. (paso 2 — pendiente, lo indicará el autor)

*(Placeholder. Se rellenará cuando el autor indique el siguiente paso a discutir.)*

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
