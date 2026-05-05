# Agentes GDC1 — Sistema de generación con IA

> Sistema de agentes para generar la guía del profesor del curso de español A1.1 "Nuevo Compañeros 1" (SGEL).

## Qué es

Agentes CrewAI que generan explotaciones didácticas a partir del inventario de actividades del libro del alumno. El sistema lee el inventario de cada unidad (JSON en BD), aplica criterios pedagógicos y genera contenido estructurado.

## Stack

| Componente | Tecnología |
|---|---|
| Agentes | CrewAI 1.9.3 |
| LLMs | Anthropic (Claude) + Groq (GPT-OSS-120B, Kimi K2) |
| Base de datos | Neon PostgreSQL |
| Evaluación | DeepEval (métricas rule-based) + promptfoo (comparar LLMs) |
| Trazabilidad | Langfuse (cloud, opcional) |
| Servidor | Python http.server (migración a FastAPI pendiente) |
| Deploy | Railway (Docker) |

## Estructura

```
agentes_GDC1/
├── scripts/crewai/
│   ├── recurvo.py              # Agente Recurvo (vocabulario) — 2 tareas secuenciales
│   └── tools.py                # 5 tools custom contra BD Neon
├── scripts/
│   ├── importar_inventario.py  # JSON → PostgreSQL
│   └── probar_modelos.py       # Prueba comparativa de LLMs
├── eval/
│   ├── evaluar_tarjetas.py     # 5 métricas rule-based + score global
│   ├── provider_crewai.py      # Wrapper para promptfoo
│   └── promptfoo.yaml          # Config comparación de modelos
├── diagrama.py                 # Servidor web (APIs REST)
├── web/
│   ├── index.html              # Dashboard Material Design 3 (navegación multi-nivel)
│   └── favicon.svg             # Logo Agentia ELE
├── viejo/unidades/UXX/         # Contenido por unidad (estado actual): inventario.json, fuente/, tarjetas/, pildoras/, *.md
├── nuevo/                      # Estructura definitiva en construcción (ver PROCESO-MAESTRO.md)
├── Dockerfile                  # Python 3.12 + Node.js 20 + promptfoo
├── railway.toml                # Config Railway
├── requirements.txt            # Deps Python (crewai, deepeval, langfuse...)
└── .env.example                # Variables de entorno necesarias
```

## Instalación local

```bash
# Clonar
git clone https://github.com/adminmc2/agentes_GDC1.git
cd agentes_GDC1

# Entorno virtual
python -m venv venv && source venv/bin/activate

# Dependencias Python
pip install -r requirements.txt

# promptfoo (requiere Node.js)
npm install -g promptfoo

# Configurar variables
cp .env.example .env
# Editar .env con tus API keys y DATABASE_URL

# Arrancar servidor
python diagrama.py
# Dashboard en http://localhost:8080
```

## Uso

### Ejecutar agente desde el dashboard
1. Abrir http://localhost:8080
2. Seleccionar unidad en sidebar y navegar a la sección (ej. "Toda la unidad")
3. Elegir agente (Recurvo) → "+ Nueva ejecución"
4. Configurar modelo, temperatura, max tokens → "Ejecutar"
5. Consola en tiempo real + evaluación automática al terminar

### Ejecutar agente por terminal
```bash
python scripts/crewai/recurvo.py 3  # Unidad 3
```

### Evaluar tarjetas
```bash
python eval/evaluar_tarjetas.py --unidad 3
```

### Comparar modelos con promptfoo
```bash
cd eval && promptfoo eval && promptfoo view
```

## Deploy (Railway)

El repo está conectado a Railway. Cada push a `main` redespliega automáticamente.

- URL: https://agentiaelegd.up.railway.app
- Variables de entorno: configurar en Railway Settings > Variables (ver `.env.example`)

## Estado

- **Funcional:** Agente Recurvo (vocabulario), 5 tools, evaluación, dashboard, deploy
- **Pendiente:** 6 agentes más (Vocabulario sección, Gramática, Comunicación, Destrezas, Cultura, Evaluación)
- **En rediseño:** Prompts pedagógicos, repertorios, arquitectura multi-agente
