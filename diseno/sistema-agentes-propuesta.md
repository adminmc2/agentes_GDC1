# PROPUESTA: Sistema Multi-Agente para la Guía Didáctica del Profesor
## Nuevo Compañeros 1 — SGEL — Nivel A1.1
## Versión 4.0

---

## 1. CONTEXTO Y OBJETIVO

### Qué creamos

La **guía didáctica del profesor** para *Nuevo Compañeros 1* (SGEL). El libro del alumno ya está hecho. Los agentes generan el documento que indica al profesor **cómo explotar** ese libro en el aula.

### Dos fases

| Fase | Producto |
|------|----------|
| **Fase 1** | Guía impresa: explotación didáctica, orientaciones, solucionario, transcripciones |
| **Fase 2** | Herramienta adaptativa: los profesores personalizan la guía a su contexto (país, L1, horas) |

### Principio fundamental

> **El libro del alumno es el input. La guía del profesor es el output.**
> Los agentes NO crean actividades. Analizan las existentes y generan instrucciones para el profesor.

### Qué es un agente (definición técnica)

Un agente es un sistema que usa un LLM + herramientas + bucle de control autónomo (Anthropic, 2024; OpenAI, 2025; Google, 2024). Se diferencia de un asistente bien configurado en que:
- **Usa herramientas** (leer archivos, consultar base de datos, escribir outputs)
- **Toma decisiones** sobre qué hacer a continuación
- **Opera en un bucle** hasta lograr su objetivo o pedir validación humana
- **Se autocorrige** basándose en el resultado de sus acciones

### Humano en el centro

El editor valida cada output antes de que el siguiente agente trabaje. Los flujos híbridos humano-IA superan a los sistemas autónomos (EduPlanner, 2025; General Assembly GAIA).

---

## 2. ARQUITECTURA DE DATOS

### 2.1 Premisa: extraer una vez, usar siempre

El contenido del libro del alumno se extrae una sola vez del PDF y se almacena de forma estructurada. Los agentes **nunca procesan el PDF directamente** — consultan los datos ya extraídos.

### 2.2 Proceso de ingesta (se ejecuta una vez por unidad)

```
PDF libro del alumno (págs. 34-43)
         │
         ▼
  EXTRACCIÓN (visión + texto)
         │
         ▼
  BASE DE DATOS ESTRUCTURADA
  ┌────────────────────────────────────────────┐
  │ Por cada actividad:                        │
  │   - id: U03-COM-01                         │
  │   - unidad: 3                              │
  │   - seccion: Comunicación                  │
  │   - pagina: 34                             │
  │   - tipo: diálogo / ejercicio / lectura    │
  │   - contenido_linguistico: [posesivos]     │
  │   - destreza: comprensión oral             │
  │   - tiene_audio: sí/no                     │
  │   - tiene_imagen: sí/no                    │
  │   - instruccion_original: "Escucha y lee"  │
  │   - descripcion: texto libre               │
  └────────────────────────────────────────────┘
```

### 2.3 Formato de almacenamiento

| Fase | Formato | Justificación |
|------|---------|---------------|
| **Fase 1 (prototipo)** | JSON + archivos markdown | Simple, versionable, funciona en Claude Code |
| **Fase 2 (producción)** | Base de datos (PostgreSQL o SQLite) + vector store para RAG | Consultable, escalable, permite búsqueda semántica |

### 2.4 Estructura de archivos del proyecto

```
guia-didactica-profesor-IA/
├── 00-curso-general.md                ← Info general, temporalización, progresiones
├── marco-teorico-metodologico.md      ← Backstage: configura CÓMO trabajan los agentes
├── unidades/
│   ├── U01-hola.md ... U09-ropa.md   ← Contenidos + guía detallada (output final)
├── datos/                             ← NUEVO: datos estructurados del libro
│   ├── U03-inventario.json            ← Inventario de actividades extraído del PDF
│   └── ...
├── recursos/                          ← PDFs originales (se procesan una vez)
├── output/                            ← Outputs intermedios de cada agente
├── agentes/                           ← Prompts de cada agente
│   ├── planificador.md
│   ├── redactor-explotacion.md
│   ├── solucionario.md
│   └── revisor.md
├── sistema-agentes-propuesta.md       ← ESTE ARCHIVO
└── comparativa-plataformas-agentes.md
```

### 2.5 Documentos compartidos (Main Context Documents)

Estos documentos los leen TODOS los agentes como contexto base:

| Documento | Función | Cómo lo usan los agentes |
|-----------|---------|--------------------------|
| `00-curso-general.md` | Perfil del estudiante, temporalización, progresiones | Datos factuales: quién es el alumno, cuánto tiempo hay, qué sabe |
| `marco-teorico-metodologico.md` | Principios pedagógicos (Merrill, Gagné, carga cognitiva...) | **Backstage**: configura las decisiones del agente, NO aparece en el output para el profesor |
| `unidades/UXX.md` | Contenidos de la unidad + contexto secuencial | Qué se enseña, qué vino antes, qué viene después |
| `datos/UXX-inventario.json` | Inventario estructurado de actividades del libro | Base de trabajo: qué actividades hay, de qué tipo, en qué página |

---

## 3. LOS 4 AGENTES

### Justificación: por qué 4

La investigación (CrewAI content pipelines, General Assembly GAIA, EduPlanner) muestra que los sistemas de producción para generación de contenido editorial usan entre 3 y 5 agentes con roles acotados. Cada agente tiene:
- Un rol claro y una responsabilidad única
- Herramientas específicas (no todas)
- Un output verificable por el editor
- Un prompt corto y enfocado (200-500 tokens de instrucción)

### AGENTE 1: Planificador

| Campo | Descripción |
|-------|-------------|
| **Rol** | Planifica la secuencia didáctica y prepara las notas lingüísticas |
| **Lee** | `00-curso-general.md` + `datos/inventarios/U03-inventario.json` + `unidades/U03-familia.md` + unidades adyacentes (U02, U04) + `marco-teorico-metodologico.md` (sección 4: atención adolescente, sección 6: recursividad) |
| **Herramientas** | Read (archivos), consulta datos estructurados |
| **Produce** | `output/U03-01-planificacion.md` que contiene: (1) Secuencia de lecciones (distribución en sesiones de 45-55 min) + (2) Notas lingüísticas para el profesor (gramática ampliada, vocabulario nuclear, pronunciación, conexiones con unidades previas/posteriores) |
| **Rellena en U03** | Secciones 1 + 2 |
| **Restricciones** | Respetar el orden de secciones del libro. Cubrir todas las actividades del inventario. No omitir ni reordenar secciones |
| **NO hace** | No escribe la explotación didáctica. No reordena el libro |
| **Validación** | El editor aprueba la secuencia y las notas antes de continuar |

### AGENTE 2: Redactor de Explotación Didáctica

| Campo | Descripción |
|-------|-------------|
| **Rol** | Escribe las instrucciones para el profesor, actividad a actividad |
| **Lee** | `datos/inventarios/U03-inventario.json` + `output/U03-01-planificacion.md` (aprobada) + `marco-teorico-metodologico.md` (completo — este es el agente que más lo necesita) + `00-curso-general.md` (perfil estudiante, L1s) |
| **Herramientas** | Read, Write |
| **Produce** | `output/U03-02-explotacion.md` que contiene: (3) Explotación didáctica sección a sección + (4) Atención a la diversidad y errores por L1 + (5) Evaluación (criterios e instrumentos) |
| **Rellena en U03** | Secciones 3 + 4 + 5 |
| **Cómo usa el marco teórico** | El marco teórico configura sus decisiones internamente. El output es práctico: instrucciones claras para el profesor sin jerga teórica. Ejemplo: el agente aplica Gagné (activar conocimiento previo) pero escribe "Antes de abrir el libro, pregunte: ¿Cómo decís 'my mother'?" — no "Aplique el evento 3 de Gagné" |
| **Acciones de enriquecimiento** | Además de la explotación completa de cada actividad, puede enriquecer la secuencia con: (1) Activación antes de una sección, (2) Contextualización del propósito, (3) Ejemplos adicionales antes de gramática, (4) Personalización tras ejercicios, (5) Preguntas conectadas a la vida del alumno, (6) Calentamientos/cierres breves. Estas son adiciones al libro, no sustituciones. Ver `marco-teorico-metodologico.md` §1 |
| **NO hace** | No inventa actividades nuevas. No sustituye las explicaciones del libro por otras. No omite ejercicios. Explica cómo explotar las existentes. Puede sugerir calentamientos y cierres breves |
| **Validación** | El editor aprueba la explotación, diversidad y evaluación |

### AGENTE 3: Solucionario

| Campo | Descripción |
|-------|-------------|
| **Rol** | Genera respuestas y transcripciones |
| **Lee** | `datos/inventarios/U03-inventario.json` (actividades con sus instrucciones exactas) + recurso PDF si necesita verificar visualmente un ejercicio |
| **Herramientas** | Read, PDF vision (puntual), Write |
| **Produce** | `output/U03-03-solucionario.md` que contiene: (6) Solucionario completo + (7) Transcripciones de audios |
| **Rellena en U03** | Secciones 6 + 7 |
| **REQUIERE** | Acceso a los ejercicios exactos del libro (desde datos estructurados o PDF) |
| **Validación** | El editor verifica las respuestas |

### AGENTE 4: Revisor de Calidad

| Campo | Descripción |
|-------|-------------|
| **Rol** | Control de calidad del documento completo |
| **Lee** | `unidades/U03-familia.md` (compilado) + `00-curso-general.md` + `marco-teorico-metodologico.md` |
| **Herramientas** | Read |
| **Produce** | `output/U03-04-revision.md` con: informe de calidad (claridad, integridad, practicidad, pertinencia) + lista de correcciones sugeridas |
| **Evalúa** | Claridad (¿instrucciones claras para profesor no nativo?), Integridad (¿todas las actividades cubiertas?), Practicidad (¿realista en 45-55 min?), Pertinencia (¿adecuado para adolescentes 10-15?) |
| **NO hace** | No genera contenido nuevo. Identifica problemas y propone correcciones |

---

## 4. FLUJO DE EJECUCIÓN

```
FASE 0: INGESTA (una vez por unidad)
    │   PDF libro del alumno → Extracción → datos/inventarios/U03-inventario.json
    │   ✓ Editor verifica que el inventario es correcto
    ▼
FASE 1: PLANIFICACIÓN
    │   Agente 1 (Planificador)
    │   Lee: inventario + curso general + marco teórico + unidades adyacentes
    │   Escribe: output/U03-01-planificacion.md
    │   ✓ Editor valida secuencia + notas lingüísticas
    ▼
FASE 2: REDACCIÓN
    │   Agente 2 (Redactor de Explotación)
    │   Lee: planificación aprobada + inventario + marco teórico + curso general
    │   Escribe: output/U03-02-explotacion.md
    │   ✓ Editor valida explotación + diversidad + evaluación
    │
    │   Agente 3 (Solucionario) [puede ejecutarse en paralelo con Agente 2]
    │   Lee: inventario + PDF (verificación puntual)
    │   Escribe: output/U03-03-solucionario.md
    │   ✓ Editor valida respuestas
    ▼
FASE 3: COMPILACIÓN E INTEGRACIÓN
    │   Se integran los outputs aprobados en unidades/U03-familia.md
    │   (esto puede ser automático o manual)
    ▼
FASE 4: REVISIÓN
    │   Agente 4 (Revisor)
    │   Lee: U03-familia.md compilado
    │   Escribe: output/U03-04-revision.md
    │   ✓ Editor aplica correcciones finales
    ▼
    📄 unidades/U03-familia.md — VERSIÓN FINAL
```

---

## 5. EL MARCO TEÓRICO COMO BACKSTAGE

### Principio

El `marco-teorico-metodologico.md` configura CÓMO los agentes toman decisiones. NO aparece en el documento final que lee el profesor.

### Cómo lo usa cada agente

| Agente | Qué secciones del marco usa | Cómo lo aplica |
|--------|------------------------------|----------------|
| **Planificador** | Sección 4 (atención adolescente: tiempos), Sección 6 (recursividad: qué reciclar) | Distribuye secciones respetando 10-15 min por actividad. Incluye reciclaje de unidades previas en las notas |
| **Redactor** | TODO el marco (Merrill, Gagné, inductivo/deductivo, carga cognitiva, multimedia) | Aplica los principios como criterio editorial interno. Output = instrucciones prácticas sin teoría visible |
| **Solucionario** | No lo usa directamente | — |
| **Revisor** | Sección 5 (carga cognitiva: verificar que no se sobrecarga), Sección 1 (Merrill: verificar que hay activación/aplicación/integración) | Evalúa si la guía cumple los principios sin nombrarlos |

### Ejemplo concreto

Lo que el marco teórico dice al agente (instrucción interna):
> "Aplica el principio de activación (Merrill): antes de cada sección nueva, incluye una pregunta o actividad breve que conecte con conocimiento previo del alumno"

Lo que el agente escribe para el profesor (output visible):
> "Antes de abrir el libro en la página 36, pregunte a los alumnos: *¿Tenéis hermanos? ¿Cuántos?* Apunte en la pizarra las respuestas."

El profesor recibe instrucciones claras y prácticas. No necesita saber que eso viene de Merrill.

---

## 6. RUTA A PRODUCCIÓN

### Fase 1: Prototipo (ahora)

| Componente | Herramienta | Descripción |
|------------|-------------|-------------|
| **Ingesta de datos** | Claude Code (visión PDF) | Extraer inventario del libro a JSON |
| **Agentes** | Claude Code (subagentes) | Cada agente = un subagente con prompt acotado y herramientas específicas |
| **Validación** | Manual (editor revisa outputs) | Bucle de feedback editor ↔ agente |
| **Almacenamiento** | Archivos JSON + markdown | Simple, versionable |

### Fase 2: Producto (después)

| Componente | Herramienta | Descripción |
|------------|-------------|-------------|
| **Ingesta de datos** | Pipeline automatizado | PDF → extracción → base de datos |
| **Agentes** | Claude Agent SDK (Python) | Mismos prompts, empaquetados como servicio |
| **Validación** | Interfaz web | El profesor/editor valida desde navegador |
| **Almacenamiento** | PostgreSQL + vector store | Consultable, escalable, RAG |
| **API** | FastAPI | Endpoints para cada agente |
| **Alternativa** | LangGraph | Si se necesitan workflows complejos con persistencia multi-día |

### Por qué esta ruta

1. **Claude Agent SDK es Claude Code como librería.** Lo que prototipamos aquí se empaqueta directamente en Python sin migración
2. **Los prompts de los agentes son los mismos** en ambas fases. Solo cambia la infraestructura
3. **La base de datos estructurada** (inventario) es reutilizable en ambas fases
4. **El coste es bajo:** ~$0.50-$2.50 por unidad en llamadas API

---

## 7. MAPEO COMPLETO

| Agente | Lee | Escribe | Rellena en UXX |
|--------|-----|---------|----------------|
| **1. Planificador** | `00-curso-general.md` + `datos/UXX-inventario.json` + `unidades/UXX.md` + unidades adyacentes + marco teórico (parcial) | `output/UXX-01-planificacion.md` | Secciones 1 + 2 |
| **2. Redactor** | `datos/UXX-inventario.json` + output Agente 1 + marco teórico (completo) + `00-curso-general.md` | `output/UXX-02-explotacion.md` | Secciones 3 + 4 + 5 |
| **3. Solucionario** | `datos/UXX-inventario.json` + PDF (verificación) | `output/UXX-03-solucionario.md` | Secciones 6 + 7 |
| **4. Revisor** | `unidades/UXX.md` compilado + `00-curso-general.md` + marco teórico | `output/UXX-04-revision.md` | Correcciones |

---

## 8. FASE 2: HERRAMIENTA ADAPTATIVA

Una vez validada la Fase 1, los agentes se reconvierten en herramienta para el profesor:

| El profesor dice... | Agente que responde | Qué modifica |
|---------------------|---------------------|--------------|
| "Mis alumnos son todos anglófonos" | Redactor (rehace diversidad para inglés) | Sección 4 |
| "Solo tengo 1 hora semanal" | Planificador (recompacta secuencia) | Sección 1 |
| "Mis alumnos ya saben presente regular" | Planificador (ajusta notas y secuencia) | Secciones 1 + 2 |
| "Necesito más actividades orales" | Redactor (enfatiza producción oral) | Sección 3 |
| "Evalúo con portfolio" | Redactor (adapta evaluación) | Sección 5 |

---

## 9. PRÓXIMOS PASOS

1. ✅ Marco teórico guardado como `marco-teorico-metodologico.md`
2. ✅ Propuesta de agentes v4.0 — 4 agentes reales con base de datos estructurada
3. **Crear carpeta `datos/` e inventario de U03** — Extraer actividades del PDF a JSON
4. **Definir prompts de cada agente** — En `agentes/planificador.md`, etc.
5. **Ejecutar Agente 1** (Planificador) con U03 como piloto
6. **Iterar** con validación del editor
7. **Repetir** para unidades restantes
8. **Empaquetar en Agent SDK** para Fase 2

---

## FUENTES Y REFERENCIAS

### Sistemas multi-agente educativos
- [EduPlanner: LLM-Based Multi-Agent Systems for Instructional Design](https://arxiv.org/abs/2504.05370) — arXiv 2025
- [Enabling Multi-Agent Systems as Learning Designers (MAS-CMD)](https://arxiv.org/abs/2508.16659) — arXiv 2025
- [Instructional Agents — Stanford SCALE Initiative](https://scale.stanford.edu/ai/repository/instructional-agents-llm-agents-automated-course-material-generation-teaching)
- [General Assembly GAIA — CrewAI Case Study](https://www.techtarget.com/searchcio/feature/Agentic-AI-speeds-curriculum-drafting-at-General-Assembly)

### Definiciones y arquitectura de agentes
- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — Dic 2024
- [OpenAI — A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) — Abr 2025
- [Google — Agents Whitepaper](https://www.kaggle.com/whitepaper-agents) — Sep 2024
- [LangChain — What is an Agent?](https://www.blog.langchain.com/what-is-an-agent/)
- [Microsoft — Single vs Multi-Agent Architecture](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/single-agent-multiple-agents)

### Diseño de agentes
- [Anthropic — Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) — 2025
- [AWS — Agentic AI: Choosing the Right Pattern](https://aws.amazon.com/blogs/industries/agentic-ai-in-financial-services-choosing-the-right-pattern-for-multi-agent-systems/)
- [CrewAI — Crafting Effective Agents](https://docs.crewai.com/en/guides/agents/crafting-effective-agents)
- [IBM — Agentic Drift](https://www.ibm.com/think/insights/agentic-drift-hidden-risk-degrades-ai-agent-performance) — 2025

### Plataformas y producción
- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview)
- [LangGraph Platform GA](https://www.blog.langchain.com/langgraph-platform-ga/)
- [LangGraph vs CrewAI](https://xcelore.com/blog/langgraph-vs-crewai/)
- [LangChain — State of AI Agents Survey](https://www.langchain.com/state-of-agent-engineering) — 2025

### Pedagogía ELE
- [Generación de contenidos educativos con IA — UPM](https://oa.upm.es/91516/)

---

---

## ACTUALIZACIÓN 2026-03-15 — Arquitectura de dos fases: Recursos → Secciones

### Decisión arquitectónica

Los agentes de material (Tarjetas, Gramatips, Estrategias) trabajan **antes e independientemente** de los agentes de sección. No son post-procesadores — son **preprocesadores** que extraen, estructuran y condensan información desde la fuente (inventario), y alimentan a los agentes de sección con materiales listos.

### Justificación (por principios establecidos)

1. **Context Engineering (Anthropic, 2025):** "Sub-agent architectures where specialized agents handle focused tasks and return condensed, distilled summaries." Los agentes de recursos condensan vocabulario/gramática en materiales estructurados que reducen el ruido para los agentes downstream.

2. **Multi-Agent Framework (Google, 2025):** "Document processing subgraph includes agents for text extraction, formatting analysis, and content classification, operating independently." Los agentes de recursos operan independientemente sobre el inventario.

3. **Signal-to-noise (Context Engineering):** "Maximize signal-to-noise ratio by treating every token as precious." Los agentes de sección reciben materiales estructurados, no inventario crudo.

4. **Reducción de propagación de errores:** Los agentes de recursos trabajan desde la fuente validada (inventario JSON), no desde la interpretación de otro agente.

### Flujo de dos fases

```
FASE 1 — AGENTES DE RECURSOS (paralelo, desde inventario)
  Agente Tarjetas   → extrae TODO el vocabulario → genera tarjetas (nuevo ⭐ / reutilizado ♻️)
  Agente Gramatips   → extrae TODA la gramática → genera tips (nueva ★ / repaso ↻)
  Agente Estrategias → identifica TODAS las destrezas → genera/reutiliza estrategias

FASE 2 — AGENTES DE SECCIÓN (secuencial)
  Vocabulario → Gramática → Comunicación → Destrezas → Cultura → Reflexión
  Cada uno recibe: inventario + materiales de Fase 1 + output de secciones anteriores
  Cada uno produce: explotación didáctica (su único foco)
```

### Ventajas sobre el diseño anterior (cada sección genera sus materiales)

- **Consistencia:** 1 agente genera TODAS las tarjetas con el mismo criterio
- **Reutilización inter-unidad:** el agente de Tarjetas conoce todas las tarjetas de U01-U09
- **Foco:** cada agente tiene UNA responsabilidad
- **Aprendizaje:** correcciones a tarjetas afectan a 1 agente, no a 6

---

*Documento creado: 2025-01-31*
*Versión: 4.0 — Rediseño completo: 4 agentes reales, base de datos estructurada, marco teórico como backstage, ruta a producción con Claude Agent SDK*
*Actualización 2026-03-15: Arquitectura de dos fases (Recursos → Secciones), framework CrewAI, estrategia multi-modelo (Groq + Anthropic)*
*Cambios desde v3.0: De 8 agentes simulados a 4 agentes reales con herramientas; ingesta de datos separada de generación; marco teórico integrado como instrucción interna (no visible al profesor); ruta clara prototipo→producción*
