# CLAUDE.md — Guía Didáctica del Profesor (SGEL)

> **ESTADO:** Proyecto en desarrollo activo. Sistema de agentes v5.0 descartado como sistema funcional. Rediseño completo en curso: migración a CrewAI + estrategia multi-modelo (Groq/Anthropic). Todo puede cambiar.

---

## REGLA PRINCIPAL

**Al inicio de cada sesión y tras cada acción o cambio relevante, preguntar al usuario si es necesario actualizar este CLAUDE.md.**

---

## CICLO DE TRABAJO

Cada vez que se inicie sesión o se haga un cambio en el proyecto:

1. Revisar las preguntas pendientes (abajo)
2. Realizar el cambio
3. Preguntar al usuario:
   - ¿Esto afecta al CLAUDE.md?
   - ¿Hay instrucciones específicas que añadir?
   - ¿Hay algo que añadir/quitar de "Qué NO hacer"?
   - ¿Hay tareas nuevas pendientes?
4. Actualizar CLAUDE.md si es necesario
5. Pasar al siguiente cambio

---

## Reglas obligatorias tras cada cambio

- Actualizar CHANGELOG.md con lo que se modificó
- Actualizar README.md si el cambio afecta a instalación o uso
- Actualizar ROADMAP.md cuando el usuario indique que algo es un roadmap o hito
- Ante cualquier cambio en un componente de la arquitectura del proyecto, analizar el impacto global: verificar coherencia (consistencia con el resto), correspondencia (referencias cruzadas correctas), adecuación (cumple su función) y lógica (la composición general sigue teniendo sentido)
- Cada decisión nueva de diseño (estructura, esquema, proceso, arquitectura) debe explicarse con detalle: qué es, por qué se elige, qué alternativas se descartaron y por qué. El usuario debe poder evaluar si la decisión es adecuada antes de implementarla
- Las decisiones de diseño deben justificarse por políticas, patrones y prácticas establecidas por especialistas del ámbito (ingeniería de agentes, context engineering, diseño multi-agente, didáctica ELE), no por criterio personal. Citar fuentes o principios reconocidos cuando sea posible
- Si este archivo supera las 500 líneas, considerar dividirlo en archivos separados según las funciones del proyecto (ej. instrucciones de agentes, estado, restricciones) e importarlos desde un CLAUDE.md principal

---

## PREGUNTAS PENDIENTES (REVISAR EN CADA SESION)

Antes de continuar trabajando, el asistente DEBE revisar estas preguntas con el usuario:

### 1. Tareas en curso
**Pregunta:** ¿Hay tareas específicas en curso que documentar?
**Respuesta:** *pendiente*

### 2. Instrucciones de uso de agentes
**Pregunta:** ¿Hay instrucciones específicas que añadir sobre cómo generar nuevas unidades con los agentes?
**Respuesta:** En curso. Framework seleccionado: CrewAI. Pendiente definir arquitectura detallada antes de implementar.

### 3. Nivel de detalle
**Pregunta:** ¿El nivel de detalle del CLAUDE.md es correcto (más/menos información en alguna sección)?
**Respuesta:** *pendiente*

### 4. Restricciones
**Pregunta:** ¿Hay algo que añadir o quitar de la sección "Qué NO hacer"?
**Respuesta:** *pendiente*

### 5. Esquema de personalización (BD Neon)
**Pregunta:** ¿El esquema actual de la tabla `personalizaciones` en Neon PostgreSQL (tiempo_custom, variante, notas, completada) sigue siendo adecuado para Layer 3? Los campos son provisionales y deberán redefinirse cuando se desarrolle la capa de guías personalizadas para profesores.
**Respuesta:** *pendiente* (se revisará cuando Layer 3 se concrete)

### 6. Proceso de reciclaje de contenidos
**Pregunta:** ¿Cómo se garantiza que el contenido de secciones/unidades anteriores se recicla correctamente?
**Contexto:** La regla 70/30 y la lógica de reciclaje están definidas dentro de los prompts de cada agente (vocabulario, comunicación, cultura, etc.), pero no existe un mecanismo técnico que lo instrumente. Actualmente: (a) la tabla `reciclaje` en la BD está vacía y no se sabe quién la pobla; (b) los agentes necesitan recibir como INPUT el contenido de secciones anteriores, pero no está definido cómo se genera ese input; (c) el reciclaje inter-unidad requiere tener los inventarios de todas las unidades previas importados. Se debe analizar: quién genera los datos de reciclaje (humano, agente, script), cuándo en el flujo de producción, y cómo se alimenta a cada agente. Esto es prerequisito del paso 6 (protocolo de invocación).
**Respuesta:** *pendiente* (se abordará dentro del diseño del sistema CrewAI — la orquestación automática debe resolver el paso de contexto entre agentes)

### 7. Modelo de generación de contenido
**Pregunta:** ¿Qué modelo LLM usar para la generación de contenido editorial?
**Contexto:** Prueba completada (2026-03-15). Claude Sonnet = mejor calidad, $0.13/sección. Kimi K2 = aceptable con revisión, $0.03/sección. Qwen 3 32B = descartado por errores factuales. Se necesitan más pruebas con secciones diferentes (gramática, comunicación, cultura) antes de decidir.
**Respuesta:** *pendiente* (más pruebas necesarias)

### 8. Arquitectura detallada CrewAI
**Pregunta:** ¿Cómo se estructura el sistema CrewAI? (agentes, tareas, herramientas, memoria, modelo por tarea, flujo de verificación)
**Contexto:** Framework seleccionado pero no implementado. Debe diseñarse antes de construir. Incluye: qué herramientas necesita cada agente, cómo se gestiona la memoria/aprendizaje, qué modelo asignar a cada tarea, y cómo funciona la verificación automática de outputs.
**Respuesta:** *pendiente* (diseñar antes de implementar)

---

## Descripción del Proyecto

### Qué es

Un sistema de 3 capas para el curso de español A1.1 "Nuevo Compañeros 1" (SGEL, adolescentes 12-15 años):

**Capa 1 — Guía impresa (en desarrollo)**
Guía del profesor editorial con explotaciones didácticas para las 9 unidades del libro. Producto impreso que publica SGEL. En desarrollo activo.

**Capa 2 — Sistema de agentes (en rediseño completo)**
Agentes IA que generan las explotaciones didácticas. El sistema v5.0 (7 prompts .md + orquestador) no era un sistema funcional de agentes: eran instrucciones pedagógicas cargadas manualmente en Claude sin automatización, memoria ni orquestación real. Se está rediseñando con CrewAI como framework de agentes autónomos con herramientas, memoria persistente y soporte multi-modelo (Groq + Anthropic).

**Capa 3 — Guías personalizadas (futuro)**
Los agentes sirven a profesores individuales que usen el curso para adaptar y personalizar la guía a su grupo, ritmo y necesidades concretas.

### Premisa fundamental

**Todo está en construcción y todo puede cambiar.** No asumir que ningún componente es definitivo.

---

## Estado Actual

### Contenido producido

| Componente | Estado |
|------------|--------|
| U03 — Vocabulario | Completo |
| U03 — Gramática | Completo |
| U03 — Itinerarios | Completo (8 sesiones, 62 tarjetas) |
| U03 — Píldoras formativas | Completas (10, LaTeX + PDF) |
| U03 — Tarjetas vocabulario | Completas (InDesign + CSV) |
| U03 — Material complementario | Indexado (4 recursos) |
| U03 — Comunicación | Estructura creada, sin explotación |
| U03 — Destrezas | Estructura creada, sin explotación |
| U03 — Cultura | Estructura creada, sin explotación |
| U03 — Reflexión | Estructura creada, sin contenido |
| U03 — Evaluación | Estructura creada, sin contenido |
| U01-U02, U04-U09 | Plantillas con `*pendiente*` |

### Infraestructura pedagógica (estable)

| Componente | Estado |
|------------|--------|
| Marco teórico (72 KB) | Completo |
| Curso general (50 KB) | Completo |
| Bancos de técnicas (10 archivos, ~800+ técnicas) | Completos |

### Sistema de agentes CrewAI (primera ejecución exitosa)

| Componente | Estado |
|------------|--------|
| 7 prompts de agente (.md) + orquestador | Referencia pedagógica. NO son agentes autónomos |
| 6 repertorios | Válidos como input para los futuros agentes reales |
| Framework CrewAI | **Implementado para agente Recurvo.** Primera ejecución exitosa: 5/5 tools, 19 tarjetas en BD, CSV exportado |
| Agente Recurvo (vocabulario) | Funcional. Arquitectura 2 tareas: generador (3 tools lectura) + escritor (2 tools escritura) |
| 5 tools custom (BD) | Funcionando: consultar_inventario, consultar_tarjetas_previas, consultar_correcciones, escribir_tarjetas, exportar_csv |
| APIs configuradas | `.env` con Anthropic (Claude) + Groq (GPT-OSS-120B, Kimi K2, etc.) |
| Prueba comparativa de modelos | Completada. Resultados en `scripts/resultados_prueba/` |
| Web de gestión | `diagrama.py` + `web/index.html`. 7 pestañas incl. Correcciones con CRUD contra BD |
| Feedback/aprendizaje | Tabla `correcciones` en BD + tool + pestaña web. Pendiente: Knowledge System, crewai train |
| Evaluación de agentes | Investigado: Langfuse, DeepEval, promptfoo. Pendiente de instalar |
| Propuestas de diseño | En `diseno/` |

---

## Estructura del Repositorio

```
guia-didactica-profesor-IA/
├── CLAUDE.md                      # Este archivo
├── 00-curso-general.md            # Orientaciones del curso
├── marco-teorico-metodologico.md  # Fundamentos teóricos
├── CHANGELOG.md                   # Historial
│
├── agentes/                       # Prompts pedagógicos de referencia (NO son agentes autónomos)
├── repertorios/                   # Opciones de explotación (input para agentes)
├── unidades/                      # U01-U09, cada una en su carpeta (UXX/). Solo U03 con contenido
├── datos/
│   ├── fuente/                    # Material fuente del libro del alumno (PDF embebido por unidad)
│   └── inventarios/               # Inventarios JSON extraídos de las páginas
├── referencias/                   # Bancos de técnicas pedagógicas
├── materiales/                    # Píldoras formativas (LaTeX/PDF) + tarjetas
├── material-complementario/       # PDFs editoriales + PowerPoint
├── tarjetas/                      # Diseño InDesign de tarjetas
├── scripts/                       # Scripts y agentes
│   ├── importar_inventario.py    # Importación JSON → Neon PostgreSQL
│   ├── probar_modelos.py         # Prueba comparativa de LLMs
│   ├── resultados_prueba/        # Outputs de la prueba de modelos
│   └── crewai/                   # Agentes CrewAI
│       ├── recurvo.py            # Agente Recurvo (vocabulario) — 2 tareas secuenciales
│       └── tools.py              # 5 herramientas custom contra BD
├── diagrama.py                    # Servidor web de gestión (APIs + Mermaid)
├── web/
│   └── index.html                 # Frontend (hot reload, no requiere reiniciar servidor)
├── .env                          # API keys Anthropic + Groq (gitignored)
└── diseno/                        # Propuestas del sistema de agentes
    ├── sistema-agentes-propuesta.md   # Arquitectura general + dos fases (Recursos → Secciones)
    └── crewai-memoria-aprendizaje.md  # Memoria, aprendizaje y definición del agente Recurvo

# SEPARADO (en Desktop, sin git):
# SGEL-proyecto-impreso-Guia-1/    # 8.4 GB de diseño + materiales exportados
```

---

## Qué NO Hacer (Provisional)

- No modificar archivos binarios (.pdf, .indd, .ai, .psd)
- No crear archivos nuevos sin necesidad
- No renombrar ni mover carpetas sin consultar
- No hay build/test (esto es documentación)
- No eliminar `*pendiente*` sin completar el contenido
- No asumir que la arquitectura de agentes es definitiva
- No tomar decisiones de diseño del sistema sin consultar al usuario
- No usar los prompts .md de `agentes/` como si fueran un sistema autónomo — son instrucciones pedagógicas de referencia, no agentes funcionales
- No construir sistemas de agentes sin prueba previa de calidad con los modelos reales

---

## Proceso de generación del inventario

1. Exportar desde InDesign un **PDF con texto embebido** por unidad (ej. `datos/fuente/U03-libro.pdf`)
2. Claude lee el PDF directamente y extrae todas las actividades al JSON (ej. `datos/inventarios/U03-inventario.json`)
3. El JSON se valida e importa a la base de datos (Neon PostgreSQL)
4. Las JPGs actuales en `datos/fuente/U03/` se eliminarán cuando exista el PDF correspondiente

> **Completado:** PDF embebido de U03 generado desde InDesign (`datos/fuente/U03/U03-libro.pdf`). JPGs eliminadas.

---

## Base de datos (Neon PostgreSQL)

Almacén estructurado del proyecto. El JSON sigue siendo el formato de intercambio con Claude; la BD es la fuente de verdad.

- **Servicio:** Neon (neon.tech) — PostgreSQL serverless
- **Esquema creado:** 9 tablas (unidades, paginas, actividades, respuestas, cuadros_gramaticales, reciclaje, profesores, grupos, personalizaciones). Tabla `dependencias_seccion` eliminada por redundante — el orden de secciones está definido en los prompts de cada agente.
- **Campo `contenidos_indice` (JSONB):** Añadido a `unidades`. Contiene el índice de contenidos del libro (vocabulario, gramática, comunicación, cultura, etc.) para cada unidad. Actualmente poblado con datos del índice general del libro para U00-U09. **Pendiente:** cuando se generen los inventarios completos de cada unidad, verificar y completar estos datos con el detalle real de cada página.
- **Flujo:** JSON → script importación → PostgreSQL

> **Completado:** Script de importación `scripts/importar_inventario.py` creado y ejecutado. U03 importada: 10 páginas, 47 actividades, 184 respuestas, 3 cuadros gramaticales. Idempotente (DELETE CASCADE + reimportación).
> **Completado:** `contenidos_indice` poblado para las 10 unidades (U00-U09) desde el índice del libro. Solución parcial al reciclaje inter-unidad: permite a los agentes consultar qué contenidos lingüísticos se trabajan en cada unidad.

---

## Flujo completo de producción (acordado)

El orden de pasos para producir contenido de una unidad:

1. **Exportar material fuente** — InDesign → PDF embebido por unidad → `datos/fuente/`
2. **Extraer inventario** — Claude lee el PDF → genera JSON → `datos/inventarios/`
3. **Validar inventario** — Comparación visual fuente vs JSON, corregir errores
4. **Importar a BD** — JSON validado → script → Neon PostgreSQL
5. **Poblar reciclaje** — Analizar contenido lingüístico y mapear qué se recicla entre secciones/unidades
6. **Construir sistema de agentes (CrewAI)** — Framework seleccionado: CrewAI con multi-modelo (Groq + Anthropic). Los prompts .md actuales se reutilizarán como instrucciones pedagógicas dentro de agentes reales con herramientas, memoria y orquestación automática. Prueba de modelos completada (ver resultados en `scripts/resultados_prueba/`). **Pendiente:** definir arquitectura detallada antes de implementar.
7. **Generar explotación** — Agente CrewAI + inventario + reciclaje + repertorio + infraestructura → explotación didáctica por sección

> **Análisis completado (paso 6):** El sistema v5.0 se descartó como sistema funcional. Se seleccionó CrewAI como framework. Se realizó prueba comparativa de 3 modelos (Claude Sonnet, Kimi K2, Qwen 3 32B). Alternativas descartadas: n8n (herramienta de automatización, no de agentes), Python custom desde cero (riesgo de repetir el mismo error), LangGraph (excesivo para flujo secuencial). Pendiente: diseño detallado de la arquitectura CrewAI antes de construir.

---

## Secciones Pendientes de Completar

Las siguientes secciones se añadirán según avance la redefinición:

- [ ] Arquitectura definitiva de agentes
- [ ] Estructura definitiva del proyecto
- [ ] Convenciones de nombrado finales
- [ ] Instrucciones de uso de agentes
- [ ] Flujo de trabajo completo
- [x] Script de importación JSON → PostgreSQL
- [ ] Comandos útiles
- [ ] Archivos clave para contexto
