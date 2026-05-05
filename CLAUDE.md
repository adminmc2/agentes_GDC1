# CLAUDE.md — Guía Didáctica del Profesor IA

> Auto-cargado por Claude Code en cada sesión. Define el contexto global del proyecto y las reglas no negociables que toda interacción debe respetar.
>
> **Reglas operativas detalladas por fase** viven en `fases/<N>-<nombre>/CLAUDE.md` y se cargan automáticamente cuando se trabaja en esa fase.
>
> **Estado del proyecto, decisiones y plan:** ver `PROCESO-MAESTRO.md` y `REVIEW.md`.

---

## Qué es este proyecto

Sistema editorial asistido por IA para producir la **guía didáctica del profesor** del libro "Nuevo Compañeros 1" (NC1, ELE A1.1, SGEL).

El contenido editorial se genera siguiendo un **proceso de 8 fases**, partiendo del PDF del libro original.

---

## Estructura del repositorio

```
guia-didactica-profesor-IA/
├── unidades/UX/                   ← contenido editorial por unidad (sistema activo)
│   ├── UX-nc1-inventario.json
│   ├── fuente/UX-nc1.pdf          (gitignored)
│   ├── tarjetas/, pildoras/, *.md
├── fases/                         ← una carpeta por fase con su CLAUDE.md + prompt + artefactos
│   └── 1-extraccion-inventario/
│       ├── CLAUDE.md              (cargado solo al trabajar en esta fase)
│       └── prompt.md              (instrucciones operativas detalladas)
├── scripts/
│   └── validar_inventario.py      (validación estructural sin LLM)
├── web/, diagrama.py, eval/       (infraestructura activa)
├── viejo/                         (archivo del sistema CrewAI v5 anterior — INTOCABLE)
├── CLAUDE.md                      (este archivo)
├── PROCESO-MAESTRO.md             (decisiones + bitácora)
├── REVIEW.md                      (plan ejecutable con gates)
├── README.md, CHANGELOG.md, ROADMAP.md
└── Dockerfile, requirements.txt, railway.toml, .env.example
```

`viejo/` no se toca. Contiene el sistema CrewAI v5 anterior, conservado como referencia hasta su eliminación final.

---

## Modelo conceptual

Tres tipos de contenido (no mezclar):

1. **Producto editorial** — la guía, las tarjetas, los textos.
2. **Sistema técnico** — código Python, dashboard, evaluación.
3. **Especificaciones** — los criterios y reglas (CLAUDE.md, prompts versionados, esquemas).

Dos audiencias para las especificaciones:

- **Claude Code** (presente operativo) — lee los archivos `.md` directamente en chat.
- **Agentes CrewAI** (futuro automatizado) — leerán desde el CLAUDE.md + prompt de cada fase como su system prompt.

---

## Las 8 fases del proceso

| # | Fase | Estado | Carpeta |
|---|---|---|---|
| 1 | Input PDF → inventario JSON | ✅ Operativa | `fases/1-extraccion-inventario/` |
| 2 | Análisis de vocabulario | 📋 Pendiente | — |
| 3 | Tarjetas de vocabulario | 📋 Pendiente | — |
| 4 | Tarjetas de estrategia | 📋 Pendiente | — |
| 5 | Píldoras formativas | 📋 Pendiente | — |
| 6 | Generación sección por sección | 📋 Pendiente | — |
| 7 | Doble versión (completa / 2 páginas) | 📋 Pendiente | — |
| 8 | Principios teórico-metodológicos + repertorios | 📋 Pendiente | — |

Cada fase nueva crea su carpeta `fases/<N>-<nombre>/` con su `CLAUDE.md` + `prompt.md`.

---

## Reglas de oro (no negociables, globales)

1. **Texto verbatim del libro.** El contenido editorial extraído del libro debe reproducir el texto del libro exactamente como aparece, no como referencia ni interpretación.
2. **No transformar sin razón.** Si una decisión editorial no requiere cambio, no se cambia. Cualquier transformación se documenta.
3. **Validar antes de cerrar.** Cada artefacto producido pasa por validación (script, revisión visual o ambas) antes de declararse cerrado.
4. **No inventar.** Si una palabra, fecha o dato no está en la fuente original, no se añade. Marcar como "verificación pendiente" y consultar al autor.
5. **Una fuente única.** Cada criterio editorial vive en un único archivo. La duplicación lleva a desincronización.
6. **No tocar `viejo/`.** Contiene el sistema anterior, intocable hasta su eliminación final autorizada por el autor.

---

## Convenciones de naming

- Carpetas de unidad: `U1/`, `U2/`...`U9/` (sin cero a la izquierda).
- Archivos por unidad: prefijo `UX-nc1-`. Ejemplo: `U3-nc1-inventario.json`.
- Archivos globales del curso: prefijo `nc1-`. Ejemplo: `nc1-tarjetas.json`.
- Curso: `nc1` = "Nuevo Compañeros 1".

> La convención sin cero solo es válida para cursos de ≤9 unidades. Para 10+ habría que reintroducir el cero.

---

## Comandos básicos

```bash
# Arrancar dashboard
python3 diagrama.py
# → http://localhost:8080

# Validar inventario de una unidad
python3 scripts/validar_inventario.py 3
```

---

## Lo que NO se hace (global)

- No modificar nada en `viejo/`.
- No ejecutar el sistema CrewAI antiguo (no está conectado al sistema actual).
- No transformar JSON antiguo a nuevo schema sobre la marcha; cada unidad se extrae directamente del PDF con el prompt de la fase correspondiente.
- No saltarse la validación antes de cerrar un artefacto.
- No inventar contenido editorial. Toda palabra debe tener respaldo en la fuente.
- No duplicar instrucciones operativas en este CLAUDE.md raíz si ya viven en el CLAUDE.md de una fase.

---

## Documentos clave

| Archivo | Para qué |
|---|---|
| `PROCESO-MAESTRO.md` | Decisiones cerradas, esquemas, bitácora |
| `REVIEW.md` | Plan ejecutable con gates de validación |
| `README.md` | Descripción del proyecto |
| `CHANGELOG.md` | Historial técnico |
| `fases/<N>-<nombre>/CLAUDE.md` | Contexto operativo de cada fase |
| `fases/<N>-<nombre>/prompt.md` | Instrucciones detalladas de cada fase |

---

## Estado actual del proyecto

- **Fase 1 operativa** — U3 extraída con éxito (47 actividades, JSON válido).
- **U1, U2, U4-U9 pendientes** de extracción cuando lleguen sus PDFs.
- **Fases 2-8 pendientes** de definir.
- **`viejo/` preservado** como archivo del sistema CrewAI v5 anterior.
