# Guía Didáctica del Profesor — Nuevo Compañeros 1

Sistema editorial asistido por IA para producir la **guía didáctica del profesor** del libro de texto *Nuevo Compañeros 1* (NC1, ELE A1.1, SGEL).

El contenido editorial se genera siguiendo un **proceso de 8 fases**, partiendo del PDF del libro original.

---

## Estado del proyecto

| Fase | Descripción | Estado |
|------|-------------|--------|
| 1 | Input PDF → inventario JSON | ✅ U0-U9 integradas y validando 0/0 |
| 2 | Reciclaje de contenidos | 🔄 Reactivada (v11.69) — pipeline Capa 1 + validadores implementado; Capa 2 corrida como shakedown en U0-U3 (v11.80→v12.18), pendiente de procedimentalizar (Nivel 5, v12.19) |
| 3 | Tarjetas de vocabulario | 📋 Pendiente |
| 4 | Tarjetas de estrategia | 📋 Pendiente |
| 5 | Píldoras formativas | 📋 Pendiente |
| 6 | Generación sección por sección | 📋 Pendiente |
| 7 | Doble versión (completa / 2 páginas) | 📋 Pendiente |
| 8 | Principios teórico-metodológicos + repertorios | 📋 Pendiente |

---

## Estructura del repositorio

```
guia-didactica-profesor-IA/
├── unidades/                        ← contenido editorial por unidad (sistema activo)
│   └── UX/
│       ├── UX-nc1-inventario.json   ← inventario extraído del PDF
│       ├── fuente/UX-nc1.pdf        ← PDF del libro (gitignored)
│       └── tarjetas/, pildoras/, *.md
├── fases/                           ← una carpeta por fase con su CLAUDE.md + prompt
│   └── 1-extraccion-inventario/
│       ├── CLAUDE.md                ← contexto operativo de la fase
│       └── prompt.md                ← instrucciones detalladas para extracción
├── scripts/
│   └── validar_inventario.py        ← validación estructural sin LLM
├── web/                             ← frontend del dashboard
├── diagrama.py                      ← servidor del dashboard (HTTP + APIs)
│
├── CLAUDE.md                        ← contexto auto-cargado por Claude Code
├── PROCESO-MAESTRO.md               ← decisiones acumuladas + bitácora
├── REVIEW.md                        ← plan de trabajo con gates de validación
├── CHANGELOG.md                     ← historial técnico de cambios
│
├── docs/historico/                  ← histórico archivado (changelog/review/docs viejos)
├── requirements.txt, .env.example
└── .gitignore
```

> **Autoridad documental:** `CLAUDE.md` (raíz + de fase) manda sobre cómo actuar hoy. `CHANGELOG.md` y `REVIEW.md` son registro/estado, no autoridad. **Dónde mirar el histórico:** todo lo cerrado o superado vive en `docs/historico/` — no hace falta releer logs gigantes; consultar ahí solo si se necesita contexto antiguo puntual.

---

## Cómo se trabaja con el sistema

### 1. Extraer el inventario de una unidad nueva

Cuando el autor entrega el PDF de una unidad (ej. U4):

```
1. Colocar el PDF en unidades/U4/fuente/U4-nc1.pdf
2. En chat con Claude Code:
   "Extrae el inventario de U4 siguiendo fases/1-extraccion-inventario/CLAUDE.md y fases/1-extraccion-inventario/prompt.md."
3. Claude Code lee el prompt → lee el PDF → escribe unidades/U4/U4-nc1-inventario.json
4. Validar:
   python3 scripts/validar_inventario.py 4
5. Revisar visualmente en el dashboard.
```

### 2. Arrancar el dashboard

```bash
# Solo main:
source .venv/bin/activate
python3 diagrama.py
# → http://localhost:8081

# Con worktrees paralelos (extract/U3, extract/U4…):
source .venv/bin/activate
EXTRA_UNIDADES_PATHS=/Users/armandocruz/Desktop/guia-didactica-extract-U3/unidades:/Users/armandocruz/Desktop/guia-didactica-extract-U4/unidades \
  python3 diagrama.py
# Las unidades en worktree aparecen con badge ámbar "🔄 Extracción en curso".
# Main tiene prioridad: si la unidad se integra, el badge desaparece automáticamente.
```

### 3. Validar un inventario

```bash
python3 scripts/validar_inventario.py 3
# o por path:
python3 scripts/validar_inventario.py unidades/U3/U3-nc1-inventario.json
```

---

## Convenciones de naming

- Carpetas de unidad: `U0/`, `U1/`, `U2/`...`U9/` (sin cero a la izquierda; U0 es la unidad introductoria atípica "Punto de partida").
- Archivos por unidad: prefijo `UX-nc1-`. Ejemplo: `U3-nc1-inventario.json`.
- Archivos globales del curso: prefijo `nc1-`. Ejemplo: `nc1-tarjetas.json`.
- Curso: `nc1` = "Nuevo Compañeros 1".

> La convención sin cero solo es válida para cursos de ≤9 unidades. Para 10+ habría que reintroducir el cero.

---

## Reglas de oro (no negociables)

1. **Texto verbatim del libro** en el JSON.
2. **No transformar sin razón.**
3. **Validar antes de cerrar.**
4. **No inventar contenido.**
5. **Una fuente única** por criterio editorial.
6. **Redacción editorial en repo B** (`temporal-antiguo-guia-ia`); repo A solo recibe el entregable publicado.

Detalle completo: [`CLAUDE.md`](CLAUDE.md).

---

## Documentos clave

| Documento | Para qué |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Contexto y reglas que Claude Code carga en cada sesión |
| [`PROCESO-MAESTRO.md`](PROCESO-MAESTRO.md) | Decisiones cerradas, esquemas, bitácora |
| [`REVIEW.md`](REVIEW.md) | Plan ejecutable: pasos pendientes, gates, validaciones |
| [`CHANGELOG.md`](CHANGELOG.md) | Historial técnico de cambios |
| [`fases/1-extraccion-inventario/prompt.md`](fases/1-extraccion-inventario/prompt.md) | Prompt versionado de la fase 1 |

---

## Stack técnico

| Componente | Tecnología |
|---|---|
| Extracción de inventario | Claude Code en chat con prompt versionado |
| Validación estructural | Python (cero LLM) |
| Dashboard | Python `http.server` + HTML/CSS/JS (Material Design 3, Phosphor icons, Mermaid) |
| Persistencia de datos | JSON en filesystem (BD Neon PostgreSQL solo en el sistema CrewAI v5 anterior, no usada en activo) |
| Ejecución | Local — `python3 diagrama.py`. Sin despliegue en la nube (stack Docker/Railway retirado en v11.21; el dashboard es herramienta local) |

---

## Modelo de dos repositorios (A / B)

El proyecto vive en **dos repositorios separados**:

- **Repo A — este** (`guia-didactica-profesor-IA`): el **entregable publicado + infraestructura**. Inventarios canónicos, fases, scripts, dashboard, docs. Es lo que se versiona en GitHub.
- **Repo B — externo** (`temporal-antiguo-guia-ia`, en `~/Desktop/`): el **sistema de trabajo**. Sistema metodológico vivo (hub, pautas, plantillas, registro), zona de redacción en curso y archivo del sistema CrewAI v5 anterior.

La redacción editorial sucede en repo B. Cuando una unidad cierra, su material se **publica** (copia) a la ruta canónica de repo A (`unidades/UX/propuesta/`). Repo A nunca es zona de redacción — solo recibe el entregable.

**Histórico:** hasta la migración (v11.x), el sistema de trabajo vivía en una carpeta `viejo/` dentro de repo A. Las propuestas ya publicadas pueden contener referencias `viejo/...` — son snapshot histórico, no se reescriben. Más detalle del modelo y de la migración en `PROCESO-MAESTRO.md`.

---

## Estado actual

- **Fase 1 — curso completo extraído.** U0-U9 integradas y validando 0/0. Refinamiento abierto: canon semántico en construcción para gobernar nombres de `campo_semantico` y `vocabulario_consolidado` desde fase 1 (propuesta E-final aprobada por revisor 2026-05-11, implementación pendiente).
- **Fase 2 (reciclaje) reactivada** (v11.69). El rediseño IA-first cerró sus cuatro niveles de herramienta: pipeline de Capa 1 (`scripts/generar_reciclaje_capa1.py`), validadores del gate (`validar_reciclaje.py`, `validar_cross_unidad.py`) y `nc1-reciclaje.json` regenerado al shape del rediseño (118 hilos). Capa 2 ha corrido como shakedown en U0-U3 (v11.80, v11.84, v12.4, v12.10, v12.18); el contrato sigue sub-procedimentado — Nivel 5 abierto en [`fases/2-reciclaje/REDISEÑO-EN-CURSO.md`](fases/2-reciclaje/REDISEÑO-EN-CURSO.md) §5 para cerrar Capa 2 al estándar de Capa 1 (pipeline de sub-trabajos discretos: mecánico + IA aislada).
- **Fases 3-8 pendientes** de definir prompt y construir.
- **Plan detallado y gates pendientes:** ver [`REVIEW.md`](REVIEW.md).
