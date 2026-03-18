# Changelog — Guía Didáctica del Profesor (IA)
## Sistema de Agentes v5.0 — Nuevo Compañeros 1

---

## [v8.5 — 2026-03-18] — Rediseño task_description generador + eliminación irregularidad

### Modificado — BD crew_agents (generador)
- **task_description** reescrito completo: definiciones de campos con ejemplos, formato combo (estructura → ejemplo), política plurales colectivos, cada forma = 1 tarjeta, preservar tildes en sílaba tónica
- **task_expected_output** actualizado: 23 campos (sin irregularidad), ejemplo con nuevos combos y regla
- Eliminada referencia a "Nuevo Compañeros 1" (agente no atado a libro específico)
- Eliminada sección CRITICAL RULES (duplicaba reglas_aprendidas, P7)

### Modificado — BD reglas_aprendidas
- Regla id=1 (silaba_tonica): añadido "preserve accent marks" → maMÁ, paPÁ
- Regla id=2 (combo): redefinido como construcciones gramaticales (estructura → ejemplo)
- Regla id=3 (genero): cada forma = 1 tarjeta (profesor ≠ profesora), regla solo describe la palabra

### Modificado — Código (eliminación de irregularidad)
- `diagrama.py`: eliminado de SELECT y allowed fields
- `scripts/crewai/tools.py`: eliminado de tool description, INSERT, CSV SELECT, headers y row builder
- `scripts/crear_crew_agents.py`: simplificado a referencia a BD (seed script)
- `eval/provider_crewai.py`: actualizado a 23 campos y nueva terminología

### Modificado — Documentación
- `materiales/especificaciones-diseno-tarjetas.md`: combos redefinidos como construcciones gramaticales con formato estructura → ejemplo
- `.claude/rules/agent-prompt-design.md`: terminología combos actualizada, referencia a especificaciones actualizada

---

## [v8.4b — 2026-03-17] — CLAUDE.md condensado (334 → 171 líneas)

### Modificado — CLAUDE.md
- Reducido de 334 a 171 líneas (−49%)
- **Eliminado:** Preguntas resueltas (1, 3, 4, 9), esquema SQL crew_agents (ya en BD), árbol local completo (derivable del filesystem), sección "GitHub y Railway" duplicada, nota redundante "Paso 6"
- **Condensado:** Preguntas pendientes (59→15 líneas), tabla CrewAI (20→10 filas), ciclo de trabajo, flujo de producción
- **Actualizado:** crew_agents de "pendiente" a "implementado" (4 sitios), dashboard v8.3→v8.4, tabla BD 9→10 tablas, checkbox crew_agents marcado como completado
- **Eliminado:** "No hay build/test" de restricciones (hay agentes ejecutables)

---

## [v8.4 — 2026-03-17] — crew_agents en BD: config de agentes editable y persistente

### Nuevo — tabla `crew_agents` (Neon PostgreSQL)
- Tabla creada con esquema: id, crew, agent_key, agent_order, role, goal, backstory, task_description, task_expected_output, max_iter, updated_at
- Poblada con los 3 agentes de Recurvo (generador, verificador, escritor)
- Script de creación: `scripts/crear_crew_agents.py` (idempotente, ON CONFLICT DO UPDATE)

### Modificado — `scripts/crewai/recurvo.py`
- **Lee config de agentes desde BD** en lugar de tenerla hardcodeada
- Nueva función `cargar_config_bd("recurvo")`: consulta crew_agents y devuelve lista de configs
- Nueva función `crear_crew(unidad)`: construye agentes, tareas y Crew dinámicamente desde BD
- `_render()`: reemplaza placeholders `{unidad}` y `{unidad:02d}` en templates de BD
- Tools y LLM params siguen en código/env vars (TOOLS_MAP, LLM_KEY_MAP, LLM_CFG)

### Modificado — `diagrama.py`
- `SERVER_VERSION = "8.4"`
- Nuevas funciones: `get_crew_agents(crew)`, `update_crew_agent(id, data)`
- Nuevos endpoints: `GET /api/crew_agents?crew=X`, `POST /api/crew_agents/update`

### Modificado — `web/index.html`
- **Nueva sección Pipeline**: reemplaza las secciones separadas de Prompt y Tareas
- Pipeline carga datos desde `/api/crew_agents` (BD) — muestra role, goal, backstory, task_description, task_expected_output, max_iter por agente
- Editar/Guardar persiste cambios en BD via `/api/crew_agents/update`
- Eliminado role/goal/backstory hardcodeado del objeto AGENTES JS
- Nueva variable global `crewAgents` para cache de datos de BD

---

## [v8.2 — 2026-03-17j] — Pulido: tildes restantes + logo header + botones legibles

### Corregido — `web/index.html`
- **Tildes**: Sílaba tónica, Traducción, Género (select de correcciones), Sílaba (tabla tarjetas), Métricas (título gráfico)
- **Logo inline**: favicon Agentia ELE visible en header junto al título
- **Botones tabla tarjetas**: "Corr"/"Elim" → "Corregir"/"Eliminar" con tooltips

---

## [v8.0 — 2026-03-17h] — Rediseño completo: navegación multi-nivel + tema Material Design

### Rediseño completo — `web/index.html`
- **Navegación multi-nivel**: Unidad → Sección → Agente → Ejecución
  - Inspirado en LangSmith, Langfuse, Braintrust
- **Sidebar por secciones** (no por agentes): Toda la unidad, Vocabulario, Gramática, Comunicación, Cultura, Destrezas, Reflexión, Evaluación
  - Cada sección muestra cuántos agentes tiene asignados
  - Secciones sin agentes muestran "Sin agentes asignados"
- **6 vistas**: Proyecto, Sección, Agente (config), Nueva ejecución, Detalle ejecución, Comparar
- **Vista Agente (config)**: secciones colapsables con prompt (role/goal/backstory), tareas, herramientas, métricas de evaluación, parámetros
- **Separación agente vs ejecución**: config del agente (prompt, tools, tasks) es estable; parámetros de ejecución (modelo, temperatura, max_tokens, top-p) son variables por run
- **Vista Ejecución**: consola, evaluación (score + métricas + radar), tarjetas, trazas LLM — todo colapsable
- **Comparación**: checkbox en lista de ejecuciones → comparar métricas lado a lado
- **Material Design 3**: fuente Inter (Google Fonts), elevación por sombras, botones pill (border-radius: 20px), focus ring en inputs
  - Paleta dorado-oliva/crema: primary #7D7432, surface #FFFDF6, surface-variant #F5F0DC
  - Cards interactivas = elevated (sombra), cards de texto = outlined (borde, sin sombra)
  - Reemplaza completamente el tema oscuro anterior
- **Favicon**: logo Agentia ELE (`web/favicon.svg`) servido desde `diagrama.py`
- **Header y sidebar sin separación**: mismo color, sin sombra en header → bloque sólido
- **Tildes corregidas**: 19+ instancias en textos visibles (Gramática, Comunicación, Evaluación, Reflexión, ejecución, métricas, parámetros, sílabas, etc.)

### Modificado — `diagrama.py`
- `SERVER_VERSION = "8.0"`
- Nuevo endpoint: `/favicon.svg`, `/favicon.ico` → sirve `web/favicon.svg`

### Modelo de datos JS
- `SECCIONES[]`: 8 secciones con agentes asignados
- `AGENTES{}`: definición completa de cada agente (Recurvo) con role, goal, backstory, tasks, tools, eval_metrics, params
- Datos sincronizados con `recurvo.py` real

### Patrón de diseño
- Todo gira alrededor de la ejecución (run-centric)
- Agentes se aplican a secciones, no se navegan directamente
- Modelo LLM pertenece a la ejecución, no al agente (permite comparar modelos)

---

## [v7.0 — 2026-03-17g] — Fix Langfuse definitivo + versión visible en dashboard

### Corregido — `requirements.txt`
- `langfuse==3.14.5` → `langfuse==2.60.10` — única versión compatible con litellm 1.82.2 (bundled en crewai 1.9.3)
- langfuse 3.x/4.x eliminaron `.trace()` y `sdk_integration` que litellm necesita
- Probado localmente: 0 errores Langfuse, trazas enviadas correctamente

### Añadido — Versión del servidor en dashboard
- `SERVER_VERSION = "7.0"` en `diagrama.py` — formato `major.minor`
- Endpoint `/api/version` para consultar versión
- Dashboard muestra "En vivo v7.0 — HH:MM:SS" junto al indicador de estado
- major se incrementa en cambios sustanciales, minor en deploys pequeños

---

## [2026-03-17f] — Fix: langfuse 4.0 incompatible con litellm, bajar a 3.14.5

### Corregido — `requirements.txt`
- `langfuse==4.0.0` → `langfuse==3.14.5` — litellm pasa `sdk_integration` a `Langfuse()`, que v4.0 eliminó
- Con v3.14.5, `litellm.success_callback = ["langfuse"]` funciona correctamente

---

## [2026-03-17e] — Langfuse: reemplazar integración rota por litellm callback

### Corregido — `scripts/crewai/recurvo.py`
- Eliminada integración anterior con `@observe` + TracerProvider (25 líneas, 0 datos útiles)
- Nueva integración: `litellm.success_callback = ["langfuse"]` (4 líneas)
- Captura automática de cada llamada LLM: tokens, coste, modelo, latencia, prompt, respuesta
- Sin conflicto OTel (no usa TracerProvider ni @observe)

---

## [2026-03-17c] — Actualizar catálogo de modelos Groq

### Modificado — `diagrama.py` (AVAILABLE_MODELS)
- 6 modelos Groq (antes 2): GPT-OSS 120B, GPT-OSS 20B, Llama 3.3 70B, Llama 4 Scout 17B, Kimi K2 (nueva versión -0905), Qwen 3 32B
- Eliminado `kimi-k2-instruct` viejo (131K ctx) — reemplazado por `-0905` (262K ctx)
- Añadidos campos `ctx` y `nota` a cada modelo para el dashboard
- Claude Sonnet 4 mantenido como opción de pago

### Modificado — `.env.example`
- Documentados los 6 modelos Groq con contexto y output máximo

---

## [2026-03-17b] — Fix: añadir litellm para soporte multi-modelo en CrewAI

### Corregido — `requirements.txt`
- `crewai==1.9.3` → `crewai[litellm]==1.9.3` — instala litellm como extra para routing de modelos no nativos (Groq, etc.)
- CrewAI 1.9.3 eliminó litellm de sus dependencias core (ahora es extra opcional). Sin él, el string `groq/openai/gpt-oss-120b` no se resuelve y el agente no arranca
- Verificado: crewai 1.10.1+ no es instalable (requiere `lancedb>=0.29.2` inexistente en PyPI). 1.9.3 es la última estable funcional

---

## [2026-03-17] — Dashboard reescrito: navegación por pestañas + tabla tarjetas + comparación

### Reescrito — `web/index.html` con patrones de mercado (Langfuse/LangSmith)
- Navegación por pestañas: Evaluación, Tarjetas, Trazas, Consola, Historial (sustituye scroll vertical)
- Tarjetas: tabla ordenable con búsqueda (`sortTarjetas(col)` + `filterTarjetas()`) — columnas: Palabra, Nivel, Gen, Sílaba, Campo, Regla, traducciones (IT/FR/PT/EN/CS/PL/TR), Combos, Acciones
- Comparación de evaluaciones: selección con checkbox de 2 runs, vista side-by-side de métricas
- Badges con contadores en pestañas (tarjetas, trazas, historial)
- Auto-switch: consola al ejecutar agente, evaluación al completar
- Preservada toda la funcionalidad existente: vista proyecto (grid + Mermaid), sidebar, ejecución con Popen streaming, modal de correcciones, todas las APIs

---

## [2026-03-16d] — Repo organizado + GitHub + Railway desplegado

### Reorganización del repositorio para GitHub
- Repo publicado en https://github.com/adminmc2/agentes_GDC1.git (rama `main`)
- Solo código funcional del sistema de agentes (18 archivos). Todo el contenido editorial excluido vía `.gitignore`
- Creado `GITHUB-MANIFEST.md` con lista detallada de archivos incluidos/excluidos y justificación
- Excluidos por ahora (pendientes de rediseño): `agentes/`, `repertorios/`, `datos/tarjetas/`, `scripts/resultados_prueba/`, `diseno/`

### Deploy en Railway
- URL pública: https://agentiaelegd.up.railway.app
- Dashboard y API funcionando en producción
- Creados: `Dockerfile` (Python 3.12 + Node.js 20), `railway.toml`, `.dockerignore`

### Dependencias añadidas
- `deepeval==3.8.9` añadido a `requirements.txt`
- `promptfoo` instalado vía npm global en Dockerfile (Node.js 20)
- `.env.example` creado con todas las variables documentadas (sin secrets)

### Correcciones
- Fix GitGuardian: placeholders en `.env.example` cambiados de patrones reales (`sk-ant-...`) a texto genérico
- Fix: `LANGFUSE_BASE_URL` renombrado a `LANGFUSE_HOST` (nombre correcto para SDK v4)

---

## [2026-03-16c] — Dashboard con dos vistas (Proyecto + Agentes) + tema claro

### Reescrito — `web/index.html` con navegación sidebar entre dos vistas
- **Vista Proyecto**: grid de estado 9 unidades × 8 secciones + 5 diagramas Mermaid (arquitectura, flujo, dependencias, estado agentes, BD)
- **Vista Agentes**: evaluación (score+radar+historial), tarjetas, errores, trazas Langfuse, consola, historial evaluaciones
- Sidebar: botón "Proyecto" + lista de 6 agentes + controles de ejecución + historial de runs
- Tema claro (#f5f6fa fondo, #fff tarjetas) — sustituye el tema oscuro

### Añadido — Ejecución de agentes desde la web (`diagrama.py`)
- `start_agent()`: subprocess.Popen en thread daemon con timeout 600s
- `get_agent_status()`: polling del estado de ejecución
- Endpoints: `/api/agente/run` (POST), `/api/agente/status` (GET), `/api/agente/output` (GET), `/api/modelos` (GET)
- Variable `RECURVO_LLM` para seleccionar modelo desde la web

### Añadido — Trazas Langfuse en la web
- `get_trazas()` y `get_traza_detalle()`: consultan Langfuse API directamente
- Endpoints: `/api/trazas` (GET), `/api/trazas/{id}` (GET)
- Trazas expandibles en el dashboard con observaciones detalladas

### Limpieza
- Eliminadas sustituciones SECTIONS_JSON/LABELS_JSON en `diagrama.py` (ya no necesarias)
- El frontend carga toda la configuración de agentes y modelos internamente

---

## [2026-03-16b] — Sistema de evaluación y trazabilidad integrado

### Implementado — Stack de evaluación completo
- **Langfuse** (v4.0.0): trazabilidad integrada en `recurvo.py` via OTel. Se activa automáticamente al configurar `LANGFUSE_PUBLIC_KEY` en `.env`. Stub transparente cuando no está configurado.
- **DeepEval** (v3.8.9): métricas automáticas de calidad para tarjetas de vocabulario.
- **promptfoo** (ya instalado): config YAML para comparar modelos (GPT-OSS-120B vs Kimi K2 vs Claude Sonnet).

### Creado — Script de evaluación (`eval/evaluar_tarjetas.py`)
- 5 métricas rule-based: plurales, sílaba tónica, combos, traducciones, reglas
- Score global ponderado (0-100)
- Detección de errores con detalle por tarjeta
- Tabla `evaluaciones` en BD para historial
- Modo terminal con informe visual + modo JSON
- Integrado con la web via API `/api/evaluaciones`

### Creado — Pestaña "Evaluación" en la web
- Score global con indicador visual (verde/amarillo/rojo)
- Gráfico radar con las 5 métricas (Chart.js)
- Gráfico de línea con historial de scores
- Lista de errores detectados con badges por tipo
- Historial de evaluaciones con barras de progreso
- Botón "Evaluar ahora" (ejecuta evaluación y guarda en BD)
- Enlace directo a Langfuse cloud

### Creado — Config promptfoo (`eval/promptfoo.yaml`)
- 2 providers configurados: GPT-OSS-120B y Kimi K2 (Groq, gratis)
- Claude Sonnet comentado (coste ~$0.13/ejecución)
- 5 assertions: tarjetas_suficientes, sin_plurales, nivel_1_minimo, traducciones_completas, combos_variados
- Usa `eval/provider_crewai.py` como wrapper del agente

### Mejorado — Ciclo de feedback
- Backstory del generador reforzado: prioriza correcciones previas sobre cualquier otra instrucción
- Ciclo completo: corrección en web → BD → tool consultar_correcciones → agente lee → no repite error

### Infraestructura
- `.env`: añadidas variables Langfuse (LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_BASE_URL)
- `diagrama.py`: añadidos endpoints `/api/evaluaciones` (GET), `/api/evaluaciones/run` (POST)
- `web/index.html`: Chart.js CDN añadido, pestaña Evaluación con ~200 líneas de JS
- Tabla `evaluaciones` creada en BD Neon PostgreSQL

---

## [2026-03-16] — Primera ejecución exitosa del agente Recurvo + Web de gestión

### Implementado — Agente Recurvo funcional (CrewAI)
- `scripts/crewai/tools.py`: 5 herramientas custom contra Neon PostgreSQL (consultar_inventario, consultar_tarjetas_previas, consultar_correcciones, escribir_tarjetas, exportar_csv)
- `scripts/crewai/recurvo.py`: arquitectura de 2 tareas secuenciales (generador + escritor) para resolver que el LLM no llamaba a las tools de escritura
- Bug corregido: `**kwargs` en las firmas de `_run()` rompía el `args_schema` de CrewAI (las herramientas no exponían parámetros)
- Primera ejecución completa: 5/5 tools ejecutados, 19 tarjetas escritas en BD, CSV exportado
- Modelo: GPT-OSS-120B en Groq (gratis). Coste: $0.00

### Creado — Web de gestión del proyecto
- `diagrama.py`: servidor web con APIs REST para tarjetas y correcciones (GET/POST)
- `web/index.html`: frontend separado con hot reload (no requiere reiniciar servidor para ver cambios)
- Título: "Sistema de gestión proyecto Guía didáctica"
- 7 pestañas: Estado, Arquitectura, Flujo generación, Dependencias, Agentes U03, Base de datos, Correcciones
- Pestaña Correcciones: visualiza tarjetas de la BD, permite corregir campos individuales, eliminar tarjetas, y registra todo en tabla `correcciones`

### Auditoría — Calidad de las 19 tarjetas U03
- 5 plurales incorrectos (abuelos, padres, hijos, nietos, nietas) → deben eliminarse
- 6 errores de sílaba tónica (mujer, padres, nietos, nietas, primo, prima)
- 19 reglas en formato incorrecto
- 19 combos repetitivos
- Faltan: nieto, nieta, sobrino, sobrina, niveles 2 y 3
- Pendiente de corrección

### Investigación — Feedback y evaluación de agentes
- Documentado: `crewai train`, Knowledge System, `@human_feedback` en Flows
- Evaluación: Langfuse (tracing), DeepEval (métricas), promptfoo (comparar modelos)
- Pendiente de instalar e integrar

### Limpieza
- `diagrama.py`: eliminado HTML embebido (418 líneas), extraído a `web/index.html`
- `.gitignore`: añadidos `*.pkl`, `datos/fuente/**/*.pdf`
- Eliminadas JPGs de `datos/imagenes/U03/` (reemplazadas por PDF embebido)
- Renombrado `datos/U03-inventario.json` → `datos/inventarios/U03-inventario.json`

---

## [2026-03-15] — Documento de diseño: memoria, aprendizaje y agente Recurvo

### Creado — `diseno/crewai-memoria-aprendizaje.md`
- Análisis de los 4 tipos de memoria de CrewAI y su aplicabilidad real a este proyecto
- Definición completa del agente Recurvo (primer agente de Fase 1): identidad, inputs, output JSON, 16+2 campos, tools, modelo, lógica de extracción
- Plan de construcción corregido (10 fases) con dependencias
- Preguntas pendientes antes de implementar (7 preguntas en 3 categorías)
- Conclusiones clave: entity memory de CrewAI no es fiable para vocabulario (usar tool custom con búsqueda exacta), feedback del editor es el mecanismo de aprendizaje más valioso (prioridad alta)

---

## [2026-03-15] — Arquitectura de dos fases: Agentes de Recursos → Agentes de Sección

### Decisión arquitectónica — Agentes de Recursos como preprocesadores
- Los agentes de material (Tarjetas, Gramatips, Estrategias) trabajan ANTES e independientemente de los agentes de sección
- Extraen contenido desde la fuente (inventario), no desde la interpretación de otro agente
- Justificación: Context Engineering (Anthropic), Multi-Agent Framework (Google), reducción de propagación de errores
- Añadida meta-regla en CLAUDE.md: decisiones justificadas por especialistas, no por criterio personal
- Actualizada propuesta de diseño en `diseno/sistema-agentes-propuesta.md`

---

## [2026-03-15] — Rediseño sistema de agentes + Prueba comparativa de modelos

### Decisión — Sistema v5.0 descartado como sistema funcional
- Los 7 prompts .md + orquestador NO eran agentes autónomos: eran instrucciones cargadas manualmente en Claude
- Sin automatización, memoria, orquestación ni aprendizaje
- Decisión: rediseño completo con framework de agentes reales

### Seleccionado — CrewAI como framework
- Alternativas evaluadas y descartadas: n8n (automatización, no agentes), Python custom (riesgo), LangGraph (excesivo)
- CrewAI ofrece: agentes con herramientas, memoria persistente, orquestación secuencial, soporte multi-modelo
- Pendiente: diseño detallado de la arquitectura antes de implementar

### Añadido — Prueba comparativa de 3 modelos LLM
- Script `scripts/probar_modelos.py`: genera misma sección (Vocabulario U03) con 3 modelos
- Resultados en `scripts/resultados_prueba/` (claude-sonnet.md, kimi-k2.md, qwen3-32b.md)
- Claude Sonnet 4.6: mejor calidad, español editorial impecable ($0.13/sección)
- Kimi K2 (Groq): aceptable con revisión, errores menores ortográficos ($0.03/sección)
- Qwen 3 32B (Groq): descartado — errores factuales en traducciones y sílabas tónicas ($0.008/sección)

### Añadido — APIs y configuración
- `.env` con API keys de Anthropic y Groq (gitignored)
- `.gitignore` actualizado: `.env`, `__pycache__/`, `*.pyc`
- CLAUDE.md actualizado: estado, sistema de agentes, preguntas pendientes 7-8, estructura, restricciones

---

## [2026-03-15] — Contenidos índice en BD + Script importación + Validación inventario U03

### Añadido — `contenidos_indice` JSONB en tabla `unidades`
- Campo JSONB añadido a la tabla `unidades` con ALTER TABLE
- Poblado para las 10 unidades (U00-U09) desde el índice general del libro
- Contiene: vocabulario, gramática, comunicación, cultura por unidad
- Solución parcial al reciclaje inter-unidad: permite consultar contenidos de cualquier unidad previa
- **Pendiente:** verificar y completar con detalle real cuando se generen inventarios completos
- Diagrama ER actualizado en `diagrama.py`

### Añadido — Script de importación JSON → PostgreSQL
- `scripts/importar_inventario.py`: importa inventario JSON a Neon PostgreSQL
- Idempotente: borra la unidad existente (CASCADE) y reimporta
- Diseñado para cualquier unidad (U01-U09), recibe el JSON como argumento
- U03 importada: 10 páginas, 47 actividades, 184 respuestas, 3 cuadros gramaticales
- CLAUDE.md actualizado: script marcado como completado, `scripts/` añadido a estructura

### Eliminado — Tabla `dependencias_seccion`
- Eliminada de Neon PostgreSQL (estaba vacía, nunca se pobló)
- Motivo: redundante — el orden de secciones y la lógica de reciclaje ya están definidos en los prompts de cada agente
- Esquema pasa de 10 a 9 tablas
- Añadida pregunta pendiente 6 en CLAUDE.md: cómo instrumentar el proceso de reciclaje de contenidos

---

## [2026-03-15] — Validación inventario U03 contra PDF + Material fuente

### Corregido — Inventario U03 (validación contra PDF embebido)
- 6 errores corregidos tras comparación visual página a página (10 páginas, 34-43):
  1. `contenidos_indice.gramatica`: "Verbo tener" → "Interrogativos"
  2. p35 act5 texto_modelo: "seis años" → "ocho años"
  3. p35 act7 respuesta 4: "hermano" → "hermanos" (plural)
  4. p36 cuadro Interrogativos, ejemplo Qué: "¿Qué hora comes?" → "¿Qué comes?"
  5. p36 act3 ítem 4: "¿Dónde / Cuál" → "¿Cómo / Dónde"
  6. p43 act5 sopa de letras: cuadrícula completa reescrita, respuestas "padre, sobrina" → "hijo, tío"

---

## [2026-03-15] — Material fuente PDF y limpieza de JPGs

### Modificado — Material fuente U03
- PDF embebido generado desde InDesign: `datos/fuente/U03/U03-libro.pdf` (4 MB, texto seleccionable)
- 10 JPGs eliminadas de `datos/fuente/U03/` (git rm, ya no necesarias)
- Carpeta residual `datos/imagenes/` eliminada
- Fichero residual `datos/U03-inventario.json` eliminado (duplicado del que está en `datos/inventarios/`)
- Referencias en inventario JSON actualizadas: apuntan al PDF en vez de a JPGs individuales
- CLAUDE.md actualizado: tarea de PDF marcada como completada

---

## [2026-03-14] — Reorganización de datos/, base de datos Neon y diagrama de procesos

### Añadido — Base de datos (Neon PostgreSQL)
- Esquema creado en Neon (neon.tech) con 10 tablas
- Tablas de contenido: unidades (con campo curso), paginas, actividades, respuestas, cuadros_gramaticales
- Tablas de relaciones: reciclaje, dependencias_seccion
- Tablas Layer 3: profesores (nombre, centro, país, nivel escolar), grupos (cantidad estudiantes, NEE, horas/semana, duración clase, horas/año), personalizaciones (vinculada a grupo, no a profesor)
- Decisión de diseño: profesores y grupos separados porque un profesor puede tener varios grupos con contextos distintos
- Índices para consultas frecuentes
- Diagrama ER añadido como nueva pestaña en diagrama de procesos

### Modificado — Estructura del proyecto
- `datos/` reorganizado: separación de material fuente (`datos/fuente/`) e inventarios extraídos (`datos/inventarios/`)
- `datos/imagenes/U03/*.jpg` → `datos/fuente/U03/*.jpg` (git mv, historial preservado)
- `datos/U03-inventario.json` → `datos/inventarios/U03-inventario.json` (git mv, historial preservado)
- Todas las referencias actualizadas en: inventario JSON, diagrama.py, unidades U03, audit.md, diseño

### Modificado — CLAUDE.md
- Estructura del repositorio actualizada con nueva organización de `datos/`
- Añadida sección "Proceso de generación del inventario": PDF embebido → Claude → JSON → PostgreSQL
- Añadida sección "Base de datos (Neon PostgreSQL)"
- Tareas pendientes documentadas: generar PDF embebido U03, script importación JSON → PostgreSQL

### Añadido — Diagrama de procesos (`diagrama.py`)
- Servidor local (python3, zero deps) en http://127.0.0.1:8080
- 4 diagramas Mermaid: arquitectura general, flujo de generación, dependencias entre secciones, agentes U03
- Tabla de estado con escaneo en tiempo real del proyecto (polling cada 3 seg)
- Arquitectura corregida: Libro → Material fuente → Inventario JSON → Agentes (flujo secuencial)

### Modificado — Diagrama de procesos
- Tildes corregidas en todos los textos (Gramática, Comunicación, Evaluación, etc.)
- Labels de tabla con nombres correctos en español
- Actualización en tiempo real de todos los diagramas (no solo la tabla)

---

## [2026-02-20] — Píldoras Formativas, mejoras estructurales de agentes y reescritura U03

### Modificado — Agentes (mejoras estructurales derivadas de la revisión de U03)
- `agentes/ag-vocabulario.md` — §9 ampliada con transiciones anticipatorias entre fases (CLT: carga extrínseca). Regla de posición de píldora formativa añadida al template: ANTES de la fase que la necesita (VanPatten). Añadidas §10 (Nivel de detalle y confianza en el profesor), §11 (Integración de estación de servicio en fases, MCER aprender a aprender), §12 (Dinámicas de gestión de aula: banco de 7 dinámicas para práctica oral, solo en F2b y práctica libre).
- `agentes/ag-gramatica.md` — Template de output actualizado: eliminadas cajas ASCII, píldora reposicionada ANTES de la fase, doble título (técnico + funcional). Añadidas §7-§11 (versiones comprimidas de §9-§12 de ag-vocabulario.md con referencia cruzada).

### Modificado — Píldoras Formativas
- `agentes/ag-vocabulario.md` — Sección "Notas Lingüísticas" reescrita completamente como "Píldoras Formativas". Añadido banco de acciones con 6 categorías y ~40 acciones concretas. Lógica de selección con 4 variables contextuales.
- `agentes/ag-gramatica.md` — Sección "Notas Lingüísticas" renombrada a "Píldoras Formativas". Referencia al banco de acciones compartido en ag-vocabulario.md.
- `unidades/U03-familia.md` — 4 "NOTA LINGÜÍSTICA" renombradas a "PÍLDORA FORMATIVA". Encabezado §2 actualizado.
- `unidades/U01-U09` — Encabezado §2 "Notas lingüísticas para el profesor" → "Píldoras formativas para el profesor" en todos los templates.

### Modificado — U03 Familia (Bloque 1 Vocabulario)
- `datos/inventarios/U03-inventario.json` — Reescritura completa contra imágenes del libro del profesor: añadido campo `respuestas` a todas las actividades, pistas de audio 31-42, corrección p.38 (4 personajes + vídeo), corrección p.36 act.1 tipo y act.2 nueva, p.37 act.5 ampliada a 9 ítems, recuadros naranjas como campos separados.
- `unidades/U03-familia.md` — Fases 4, 5 y 6 reescritas según propuesta del autor: Fase 4 simplificada (escucha activa + transición tarjetas), Fase 5 con píldora proyectada ANTES + alumnos preguntan con libros cerrados + tarjetas como comprobación autónoma, Fase 6 con instrucción marco + 4 dinámicas opcionales (palmada, doble palmada, sí/no, L1→L2).

---

## [2026-02-16] — Revisión completa, JSON actualizado y "escucha y repite"

### Modificado
- `datos/inventarios/U03-inventario.json` — Actualizado Vocabulario (p.34-35) para nueva edición del libro: act. 2 cambia de "relaciona" a "forma frases"; act. 5 texto modelo corregido (Ana tiene 6 años, no 8); act. 6 texto de Javier actualizado (Getafe = ciudad, no pueblo; añadida edad Alejandra y fútbol); acts. 7-10 reorganizadas (7 = completa frases sobre Javier, 8 = texto de Lucía Alonso de Cantabria en lugar de Leonora arahuaca de Colombia, 9 = preguntas sobre Lucía, 10 = síntesis comparativa Javier/Lucía con 6 frases); reducido de 11 a 10 actividades.
- `unidades/U03-familia.md` — Fase 2 reescrita: "escucha y repite" es ahora el eje central de la fase, como pide la actividad 1 del libro. Secuencia: (1) el profesor señala brevemente las 3 generaciones del árbol, (2) primera escucha global del audio, (3) segunda escucha con repetición oral de cada término, (4) refuerzo con el árbol de la pizarra. Antes: la presentación oral del profesor era el eje y el audio era accesorio al final.
- `unidades/U03-familia.md` — Título funcional de Fase 2 actualizado: de "PRESENTE EL VOCABULARIO CON EL ÁRBOL GENEALÓGICO" a "ESCUCHE Y REPITA LOS TÉRMINOS DE PARENTESCO".
- `unidades/U03-familia.md` — Texto corrupto de act. 6 corregido (duplicación "Madrid. La madre, Catalina, estudia..." eliminada).
- `unidades/U03-familia.md` — Etiquetas internas restantes eliminadas: "Weaning off —" en Fase 6, "(F4)" en Reflexión final, "(F5)" en Consolidación distribuida, "F1a del Ciclo de 5 fases: modelling" y "Agente Gramática" en notas lingüísticas. Sustituidas por lenguaje neutro para el profesor.
- `unidades/U03-familia.md` — Frase 2 de act. 10 corregida (punto espurio eliminado).
- `unidades/U03-familia.md` — Fase 3 reescrita completamente: de "Descubra el patrón de género -o/-a" a "Active la conciencia gramatical". Cambios principales: (1) el descubrimiento del patrón -o/-a pasa a la píldora formativa gramatical (inductiva, enfoque VanPatten/Conti) que se proyecta; (2) se introduce el posesivo "su" con la estructura "Su + parentesco se llama ___"; (3) los alumnos clasifican los 11 nombres del árbol en masculinos/femeninos en sus cuadernos ANTES de la escucha, como estrategia de comprensión; (4) el género funciona como herramienta para la Actividad 2, no como conocimiento abstracto. Fase 4 ajustada: eliminada pre-escucha redundante (los alumnos ya tienen los nombres clasificados desde Fase 3), la escucha 1 conecta con las hipótesis previas. Eliminado refuerzo post-corrección (ya innecesario). Nota lingüística simplificada.

---

## [2026-02-16] — Formato de output, formulación de objetivos y fundamentación teórica

### Añadido
- `referencias/formulacion-objetivos.md` — Documento de referencia v2 para formulación de objetivos. Incorpora: 3 tipos de objetivos (comunicativo/lingüístico/gramatical), objetivos de procesamiento del input (VanPatten), regla del "no 2 por 1", correspondencia ACTFL-MCER (A1 ≈ Novice High), modelo SMART completo (5 componentes con temporalización), regla del 40% para número de objetivos, 5 errores frecuentes, matiz de Conti sobre Bloom en lenguas. Fuentes: MCER, PCIC, ACTFL, VanPatten, Canale y Swain, Long, Ellis, Dörnyei, Deci y Ryan, Vygotsky, Marzano, Wiggins y McTighe.
- `unidades/U03-vocabulario-tarjetas.csv` — Archivo CSV independiente (18 palabras, delimitador punto y coma, UTF-8) listo para importar en InDesign mediante data merge.

### Modificado
- `agentes/ag-vocabulario.md` — Eliminadas todas las cajas ASCII (┌─┐│└─┘) del formato de output. Sustituidas por encabezados markdown en negrita. Concepto de "Caja" preservado como instrucción funcional para el profesor (qué material preparar/imprimir). Añadida referencia a `formulacion-objetivos.md` para verbos observables.
- `unidades/U03-familia.md` — Reescritura completa de §3.1 Vocabulario ajustada al contenido real de la nueva versión del libro (p.34-35). 10 actividades en 3 bloques (B1: acts. 1-4, B2: acts. 5-7, B3: acts. 8-10), 13 fases. Nombres del árbol genealógico corregidos (Carmen, Roberto, Carlos, Alicia, María, Nacho, Juana, Luis, Álvaro, Paloma, Pilar). Segundo personaje: Lucía Alonso (Cantabria) en lugar de Leonora (arahuaca, Colombia). Nota intercultural actualizada (contraste urbano/rural en España). Textos del libro transcritos. Objetivos verificados contra `formulacion-objetivos.md` v2. CSV y tabla de tarjetas actualizados.
- `unidades/U03-vocabulario-tarjetas.csv` — Ejemplos actualizados con personajes reales del libro (David, Javier, Lucía, Alicia, Luis, Carmen, etc.).
- `unidades/U03-familia.md` — Objetivo Bloque 1 reformulado a nivel macro: "Reconocer y nombrar los términos de parentesco básicos en español" (eliminada referencia al árbol genealógico como medio de aprendizaje).
- `referencias/formulacion-objetivos.md` — Añadida §7.6: confundir medio de aprendizaje con objetivo + formular a nivel de actividad individual. Regla para agentes: el objetivo describe el resultado macro del bloque.
- `agentes/ag-vocabulario.md` — Añadida instrucción de §7.6 en formato de objetivo de bloque.
- `unidades/U03-familia.md` — Gamificación simplificada: insignia renombrada de "GENEALOGISTA" a "Esa es la familia mía". Eliminado sistema de puntos por bloque. Obtención descrita en términos generales. Eliminados bloques de "Gamificación — Bloque X". Cierre de sección sin recuento de puntos.
- `agentes/ag-vocabulario.md` — Template de gamificación actualizado: nuevo formato (Objetivo + Imprimir + Insignia y obtención general). Eliminado desglose de puntos por bloque. El profesor decide el mecanismo de evaluación.
- `unidades/U03-familia.md` — Gamificación confirmada como UNA por sección: eliminadas 2 referencias a "Reto GENEALOGISTA" en actividades 4 y 9 (sustituidas por "¡Reto!" genérico). Justificación de act. 9 clarificada ("elemento lúdico competitivo", no "gamificación").
- `agentes/ag-vocabulario.md` — Gamificación clarificada como UNA por sección en §6 Decisiones y en template de output. 3 reglas explícitas: (1) una gamificación por sección, (2) obtención general, (3) retos en actividades ≠ gamificación (no llevan nombre de insignia).
- `unidades/U03-familia.md` — Fase 1 reescrita: explotación de foto introductoria (p.34 izquierda) como punto de partida obligatorio. Versión limpia instruccional sin justificaciones teóricas. Preguntas con reciclaje de vocabulario conocido. Modelado inicial de 3 pares señalando la foto.
- `agentes/ag-vocabulario.md` — Añadida §7: Foto introductoria como punto de partida obligatorio (regla general para todas las secciones de vocabulario). Función pedagógica: pre-input simplificado (CLT), activación de conocimientos previos (reciclaje 70/30), modelado F1a de 2-3 pares, conexión personal sin preguntas intrusivas. Restricciones explícitas.
- `agentes/ag-vocabulario.md` — Añadida §8: Separación documento / agente. Regla general: el output para el profesor contiene solo instrucciones operativas; las justificaciones teóricas y anotaciones internas no aparecen en el producto final.
- `unidades/U03-familia.md` — Fase 1: corregido modelado (padre/madre + hijo/hija en lugar de abuelo/a, ajustado a lo visible en la foto). Doble título añadido a TODAS las fases (1-13) + cierre de sección: título técnico (trazabilidad) + TÍTULO FUNCIONAL EN MAYÚSCULAS para el profesor.
- `agentes/ag-vocabulario.md` — Template de fases actualizado con sistema de doble título: (1) Fase N técnica para trazabilidad, (2) TÍTULO FUNCIONAL EN MAYÚSCULAS para el profesor. Nota explicativa con ejemplos.
- `unidades/U03-familia.md` — Secuencialidad entre fases: eliminadas instrucciones redundantes (abrir libro cuando ya está abierto, preparar lo que ya está preparado). Eliminadas etiquetas internas del agente: *F1a — Modelling:*, *F1b — Awareness:*, Segmentación léxica (CLT), Reciclaje 70/30, (worked example obligatorio en A1), (CLT §5.7), "fomenta la metacognición".
- `agentes/ag-vocabulario.md` — §8 ampliada con lista explícita de etiquetas internas prohibidas en el output. Añadida §9: Secuencialidad entre fases (no repetir instrucciones ya ejecutadas).

---

## [2026-02-01] — Generación de U03 Vocabulario

### Añadido
- `unidades/U03-familia.md` §3.1 — Explotación completa de Vocabulario (Parientes, p.34-35) generada por Agente Vocabulario v5.0. 11 actividades en 3 bloques, 14 fases, 4 notas lingüísticas, insignia GENEALOGISTA, reciclaje 70/30 integrado.
- `pruebas/U03-vocabulario-razonamiento.md` — Documento de trazabilidad con las 10 secciones de decisiones del agente.

---

## [2025-02-01] — Sistema de agentes v5.0

### Añadido
- `propuesta-v5-sistema-agentes.md` — Propuesta completa del sistema de 14 agentes (7 de sección + 7 de soporte).
- `agentes/ag-vocabulario.md` — Prompt operativo del Agente Vocabulario.
- Repertorios de explotación por tipo de actividad.

### Modificado
- `unidades/U03-familia.md` — Actualizado de v4.0 a v5.0: eliminada explotación manual, preparado para generación por agentes.

---

## [2025-01-31] — Estructura inicial del proyecto

### Añadido
- `unidades/U03-familia.md` — Creación inicial con contenidos extraídos del índice y contexto secuencial.
- `00-curso-general.md` — Descripción general del curso.
- `marco-teorico-metodologico.md` — Fundamentación teórica (CLT, VanPatten, Bloom, MCER).
