# Agentes GDC1 — Sistema de generacion con IA

> Sistema de agentes para generar la guia del profesor del curso de espanol A1.1 "Nuevo Companeros 1" (SGEL).

## Que es

Agentes CrewAI que generan explotaciones didacticas a partir del inventario de actividades del libro del alumno. El sistema lee el inventario de cada unidad (JSON en BD), aplica criterios pedagogicos y genera contenido estructurado.

## Stack

| Componente | Tecnologia |
|---|---|
| Agentes | CrewAI 1.9.3 |
| LLMs | Anthropic (Claude) + Groq (GPT-OSS-120B, Kimi K2) |
| Base de datos | Neon PostgreSQL |
| Evaluacion | DeepEval (metricas rule-based) + promptfoo (comparar LLMs) |
| Trazabilidad | Langfuse (cloud, opcional) |
| Servidor | Python http.server (migracion a FastAPI pendiente) |
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
│   ├── evaluar_tarjetas.py     # 5 metricas rule-based + score global
│   ├── provider_crewai.py      # Wrapper para promptfoo
│   └── promptfoo.yaml          # Config comparacion de modelos
├── diagrama.py                 # Servidor web (APIs REST)
├── web/
│   └── index.html              # Dashboard (ejecucion, evaluacion, trazas)
├── datos/inventarios/          # Inventarios JSON extraidos del libro
├── Dockerfile                  # Python 3.12 + Node.js 20 + promptfoo
├── railway.toml                # Config Railway
├── requirements.txt            # Deps Python (crewai, deepeval, langfuse...)
└── .env.example                # Variables de entorno necesarias
```

## Instalacion local

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
2. Seleccionar agente (Recurvo) en sidebar
3. Elegir unidad y modelo
4. Pulsar "Ejecutar" — la consola muestra output en tiempo real
5. Evaluacion automatica al terminar

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

El repo esta conectado a Railway. Cada push a `main` redespliega automaticamente.

- URL: https://agentiaelegd.up.railway.app
- Variables de entorno: configurar en Railway Settings > Variables (ver `.env.example`)

## Estado

- **Funcional:** Agente Recurvo (vocabulario), 5 tools, evaluacion, dashboard, deploy
- **Pendiente:** 6 agentes mas (Vocabulario seccion, Gramatica, Comunicacion, Destrezas, Cultura, Evaluacion)
- **En rediseno:** Prompts pedagogicos, repertorios, arquitectura multi-agente
