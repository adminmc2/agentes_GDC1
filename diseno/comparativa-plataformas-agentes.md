# COMPARATIVA DE PLATAFORMAS Y FRAMEWORKS PARA SISTEMA MULTI-AGENTE
## Guía Didáctica del Profesor — Análisis para selección de herramienta

---

## 1. RESUMEN EJECUTIVO

No existe una plataforma "mejor" universal. La elección depende de: nivel técnico del equipo, presupuesto, ecosistema cloud existente, y tipo de proyecto. A continuación se analizan **15 plataformas** organizadas en 3 categorías.

---

## 2. TABLA COMPARATIVA GENERAL

### Categoría A: Frameworks de código (requieren Python)

| Plataforma | Creador | Tipo | Multi-Agente | Facilidad de uso | Modelo IA | Coste framework | GitHub Stars | Ideal para |
|---|---|---|---|---|---|---|---|---|
| **CrewAI** | AI Fund (Andrew Ng) | Open source (Python) | ✅ Roles en lenguaje natural, "crews" | ⭐⭐⭐⭐ Fácil | Cualquiera (Claude, GPT, Gemini, Llama) | Gratis | ~36k | Equipos colaborativos con roles definidos |
| **LangGraph** | LangChain | Open source (Python) | ✅ Grafos de estado, nodos y aristas | ⭐⭐ Difícil | Cualquiera | Gratis | ~15k | Flujos complejos con ramificaciones y checkpoints |
| **AutoGen** | Microsoft | Open source (Python/.NET) | ✅ Conversaciones multi-agente | ⭐⭐⭐ Medio | Cualquiera (optimizado Azure) | Gratis | ~45k | Investigación, pipelines iterativos |
| **MetaGPT** | Comunidad | Open source (Python) | ✅ Simulación de equipos (PM, Dev, QA) | ⭐⭐⭐ Medio | Cualquiera | Gratis | ~48k | Simulación de roles profesionales |
| **OpenAI Agents SDK** | OpenAI | Open source (Python) | ✅ Handoffs entre agentes | ⭐⭐⭐⭐⭐ Muy fácil | Solo OpenAI (GPT) | Gratis | ~18k | Prototipos rápidos en ecosistema OpenAI |
| **Google ADK** | Google | Open source (Python) | ✅ Sequential, Parallel, Loop | ⭐⭐⭐ Medio | Gemini (extensible) | Gratis | ~25k | Desarrolladores en ecosistema Google Cloud |
| **AWS Strands Agents** | Amazon | Open source (Python) | ✅ Event-driven | ⭐⭐⭐ Medio | Cualquiera (vía Bedrock) | Gratis | ~5k | Empresas en ecosistema AWS |

### Categoría B: Plataformas visuales / Low-code / No-code

| Plataforma | Creador | Tipo | Multi-Agente | Facilidad de uso | Modelo IA | Coste plataforma | GitHub Stars | Ideal para |
|---|---|---|---|---|---|---|---|---|
| **n8n** | n8n GmbH | Open source (self-host) / Cloud | ✅ Nodos de agente IA en workflows | ⭐⭐⭐⭐⭐ Visual drag-drop | Cualquiera | Gratis (self-host) / desde $24/mes (cloud) | ~133k | Automatización de flujos + IA sin código |
| **Dify** | Dify.AI | Open source | ✅ Workflows con agentes | ⭐⭐⭐⭐⭐ Muy intuitivo | Cualquiera | Gratis (self-host) / desde $59/mes (cloud) | ~58k | No-técnicos, prototipado ultra-rápido |
| **Flowise** | Comunidad | Open source (Node.js) | ✅ Chatflows con agentes | ⭐⭐⭐⭐ Visual | Cualquiera | Gratis | ~30k | Chatbots, despliegue self-hosted estable |
| **Langflow** | DataStax | Open source (Python) | ✅ Canvas visual con agentes | ⭐⭐⭐ Medio-alto | Cualquiera | Gratis (open source) / Cloud disponible | ~42k | RAG + agentes con flexibilidad Python |

### Categoría C: Servicios gestionados en la nube (Managed)

| Plataforma | Creador | Tipo | Multi-Agente | Facilidad de uso | Modelo IA | Coste | Ideal para |
|---|---|---|---|---|---|---|---|
| **AWS Bedrock AgentCore** | Amazon | Servicio gestionado | ✅ A2A protocol, multi-framework | ⭐⭐⭐⭐ Consola | Cualquiera (Claude, Nova, Llama, Gemini) | Pago por uso AWS | Enterprise, cumplimiento normativo |
| **Claude Code + Agent SDK** | Anthropic | SDK + CLI | ✅ Subagentes especializados | ⭐⭐⭐⭐ CLI intuitivo | Claude | Pago por uso API | Agentes de código, desarrollo, contenido |
| **Azure AI Agent Service** | Microsoft | Servicio gestionado | ✅ Multi-agente | ⭐⭐⭐⭐ Consola | OpenAI, Llama, etc. | Pago por uso Azure | Enterprise Microsoft |

---

## 3. COMPARATIVA POR CRITERIOS CLAVE PARA NUESTRO PROYECTO

### Lo que necesitamos:
- 8 agentes especializados con roles definidos
- Flujo secuencial con pasos en paralelo
- Validación humana entre pasos
- Soporte multilingüe (contenido en español)
- Escalable a 9 unidades
- Sin necesidad de infraestructura compleja

| Criterio | CrewAI | LangGraph | AutoGen | n8n | Dify | Claude Code |
|---|---|---|---|---|---|---|
| **Roles definidos por agente** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Flujo secuencial + paralelo** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Validación humana (HITL)** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Calidad output texto largo** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Sin config. técnica** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Coste para empezar** | Gratis + API | Gratis + API | Gratis + API | Gratis (self) | Gratis (self) | Solo API |
| **Reproducible (9 unidades)** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Caso real en educación** | ✅ General Assembly | ⚠️ No documentado | ✅ EduPlanner (research) | ⚠️ No específico | ⚠️ No específico | ⚠️ No específico |
| **TOTAL** | ⭐⭐⭐⭐ | ⭐⭐⭐½ | ⭐⭐⭐½ | ⭐⭐⭐⭐ | ⭐⭐⭐½ | ⭐⭐⭐⭐½ |

---

## 4. ANÁLISIS DETALLADO: TOP 5 PARA NUESTRO PROYECTO

### 🥇 Opción 1: Claude Code (lo que usamos ahora)

| Aspecto | Detalle |
|---------|---------|
| **Ventajas** | Ya estamos aquí; calidad de texto superior (Opus 4.5); validación humana natural; sin configuración; agentes como subtareas |
| **Desventajas** | No tiene pipeline automatizado; cada unidad requiere ejecución manual; coste API por uso |
| **Coste estimado** | ~$5-15 por unidad generada (depende de extensión) |
| **Caso de uso real** | Prueba de concepto inmediata, iterar la U03 ahora |
| **Veredicto** | Mejor para Fase 1 — desarrollo y validación del concepto |

### 🥈 Opción 2: CrewAI

| Aspecto | Detalle |
|---------|---------|
| **Ventajas** | Roles naturales ("investigador", "redactor", "revisor"); General Assembly lo usa para guías; respaldado por Andrew Ng; UI no-code disponible (CrewAI Studio) |
| **Desventajas** | Requiere Python; configuración inicial; menos control fino que LangGraph |
| **Coste estimado** | Gratis (framework) + coste API del LLM elegido |
| **Caso de uso real** | General Assembly genera contenido de cursos y guías de instructor con CrewAI |
| **Veredicto** | Mejor para Fase 2 — producción automatizada de las 9 unidades |

### 🥉 Opción 3: n8n

| Aspecto | Detalle |
|---------|---------|
| **Ventajas** | 100% visual, drag-and-drop; +400 integraciones (Google Drive, Notion, etc.); nodos de agente IA; human-in-the-loop nativo; 133k GitHub stars |
| **Desventajas** | Los nodos de IA son más limitados para texto largo; orientado a automatización general, no específico para multi-agente complejo |
| **Coste estimado** | Gratis (self-hosted) o desde $24/mes (cloud) + API LLM |
| **Caso de uso real** | Automatización educativa (matrículas, notificaciones, generación de contenido) |
| **Veredicto** | Excelente si quieres interfaz visual y conectar con Google Drive, Notion, LMS |

### 4️⃣ Opción 4: Dify

| Aspecto | Detalle |
|---------|---------|
| **Ventajas** | La más intuitiva para no-programadores; mejor debugging (trazas de cada paso); workflows con loops y condicionales; UI moderna |
| **Desventajas** | Menos maduro para multi-agente complejo; más orientado a chatbots y apps |
| **Coste estimado** | Gratis (self-hosted) o desde $59/mes (cloud) + API LLM |
| **Caso de uso real** | Prototipado rápido de flujos con IA |
| **Veredicto** | Buena opción si prefieres interfaz visual sin código y prototipado rápido |

### 5️⃣ Opción 5: LangGraph

| Aspecto | Detalle |
|---------|---------|
| **Ventajas** | Control total del flujo; checkpoints y replay; menor latencia de todos los frameworks; grafos deterministas |
| **Desventajas** | Curva de aprendizaje alta; requiere pensar en grafos y estados; docs técnicos |
| **Coste estimado** | Gratis + API LLM |
| **Caso de uso real** | Usado por MAS-CMD (research paper 2025) para materiales educativos |
| **Veredicto** | Solo si tienes equipo técnico experimentado |

---

## 5. ESTRATEGIA RECOMENDADA (3 FASES)

```
FASE 1: AHORA ──────────────────────────────────────────────
│ Herramienta: Claude Code (donde estamos)
│ Objetivo: Completar la Guía U03 como prueba de concepto
│ Ventaja: Sin configuración, empezamos ya
│ Resultado: Guía U03 validada + prompts refinados para cada agente
│
FASE 2: AUTOMATIZACIÓN ─────────────────────────────────────
│ Herramienta: CrewAI o n8n (según perfil del equipo)
│   → CrewAI si hay alguien con Python en el equipo
│   → n8n si se prefiere interfaz visual sin código
│ Objetivo: Migrar los prompts validados a un pipeline reproducible
│ Resultado: Pipeline que genera las 9 unidades con supervisión humana
│
FASE 3: PRODUCCIÓN ─────────────────────────────────────────
│ Herramienta: La elegida en Fase 2 + integraciones
│ Objetivo: Conectar con Google Drive, editorial, revisores
│ Resultado: Sistema completo de producción de guías didácticas
```

---

## 6. COSTE REAL: ¿CUÁNTO CUESTA GENERAR UNA GUÍA?

El framework es gratis en todos los casos. El coste real viene de las llamadas API al modelo de IA:

| Modelo | Coste por 1M tokens input | Coste por 1M tokens output | Estimación por unidad* |
|--------|---------------------------|----------------------------|----------------------|
| Claude Opus 4.5 | $15 | $75 | ~$10-20 |
| Claude Sonnet 4 | $3 | $15 | ~$2-5 |
| GPT-4o | $2.50 | $10 | ~$2-4 |
| GPT-4o mini | $0.15 | $0.60 | ~$0.20-0.50 |
| Gemini 2.5 Pro | $1.25-2.50 | $10-15 | ~$2-5 |
| Llama 3.3 70B (local) | Gratis | Gratis | Solo coste hardware |

*Estimación para una guía completa de ~15.000 palabras con múltiples iteraciones de los 8 agentes.

---

## 7. DECISIÓN: ¿QUÉ NECESITAS ELEGIR AHORA?

No necesitas elegir ahora la plataforma final. Lo que necesitas es:

1. **Validar el concepto** → Lo hacemos aquí con Claude Code (Fase 1)
2. **Refinar los prompts de cada agente** → Se guardan como `.md` reutilizables
3. **Cuando tengas las 9 unidades claras** → Elegir entre CrewAI o n8n según tu equipo

Los prompts que creemos ahora son **portables**: funcionan en cualquier plataforma.

---

## FUENTES

- [LangGraph vs CrewAI vs AutoGen: Top 10 AI Agent Frameworks](https://o-mega.ai/articles/langgraph-vs-crewai-vs-autogen-top-10-agent-frameworks-2026)
- [AutoGen vs CrewAI vs LangGraph vs OpenAI — Galileo](https://galileo.ai/blog/autogen-vs-crewai-vs-langgraph-vs-openai-agents-framework)
- [8 Best Multi-Agent AI Frameworks for 2026](https://www.multimodal.dev/post/best-multi-agent-ai-frameworks)
- [Top 9 AI Agent Frameworks — Shakudo (Jan 2026)](https://www.shakudo.io/blog/top-9-ai-agent-frameworks)
- [12 Best AI Agent Frameworks in 2026 — Data Science Collective](https://medium.com/data-science-collective/the-best-ai-agent-frameworks-for-2026-tier-list-b3a4362fac0d)
- [CrewAI vs n8n — ZenML](https://www.zenml.io/blog/crewai-vs-n8n)
- [9 AI Agent Frameworks Battle — n8n Blog](https://blog.n8n.io/ai-agent-frameworks/)
- [Comparing Dify and Low-Code LLMOps Platforms — AiX Society](https://aixsociety.com/comparing-dify-ai-and-leading-low%E2%80%91code-llmops-platforms/)
- [Google ADK vs AWS Strands — TechAhead](https://www.techaheadcorp.com/blog/google-adk-vs-aws-strands-which-ai-agent-platform-wins/)
- [Claude Agent SDK — Anthropic Docs](https://docs.claude.com/en/api/agent-sdk/overview)
- [Top 5 Open-Source Agentic AI Frameworks 2026 — AIMultiple](https://research.aimultiple.com/agentic-frameworks/)
- [CrewAI — General Assembly Case Study](https://www.crewai.com/)
- [DataCamp: CrewAI vs LangGraph vs AutoGen](https://www.datacamp.com/tutorial/crewai-vs-langgraph-vs-autogen)

---

*Documento creado: 2025-01-31*
*Versión: 1.0*
