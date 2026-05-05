# CLAUDE.md — Guía Didáctica del Profesor (SGEL)

> **ESTADO:** Proyecto en desarrollo activo. Crew Recurvo v2.0 funcional (3 agentes, pipeline secuencial, LLM por agente). Dashboard v8.5 Material Design 3. Tabla `crew_agents` implementada en BD. Pendiente: más crews para otras secciones.

---

## REGLA PRINCIPAL

**Al inicio de cada sesión y tras cada acción o cambio relevante, preguntar al usuario si es necesario actualizar este CLAUDE.md.**

---

## CICLO DE TRABAJO

1. Revisar las preguntas pendientes (abajo)
2. Realizar el cambio
3. Preguntar: ¿afecta al CLAUDE.md, hay instrucciones nuevas, algo para "Qué NO hacer", tareas pendientes?
4. Actualizar CLAUDE.md si es necesario

---

## Reglas obligatorias tras cada cambio

- Actualizar CHANGELOG.md con lo que se modificó
- Actualizar README.md si el cambio afecta a instalación o uso
- Actualizar ROADMAP.md cuando el usuario indique que algo es un roadmap o hito
- Ante cualquier cambio arquitectónico, analizar impacto global: coherencia, correspondencia, adecuación y lógica
- Cada decisión de diseño debe explicarse con detalle (qué, por qué, alternativas descartadas) para que el usuario la evalúe antes de implementarla
- Las decisiones deben justificarse por políticas y prácticas de especialistas (ingeniería de agentes, context engineering, didáctica ELE). Citar fuentes cuando sea posible
- Si este archivo supera las 500 líneas, dividirlo en archivos separados e importarlos desde un CLAUDE.md principal

---

## PREGUNTAS PENDIENTES

Revisar con el usuario al inicio de cada sesión:

1. **Instrucciones de uso de agentes** — Recurvo v2.0 implementado. Pendiente: instrucciones para crear nuevos crews. Metodología en `.claude/rules/agent-prompt-design.md`
2. **Esquema personalización (Layer 3)** — Tabla `personalizaciones` provisional. Se revisará cuando Layer 3 se concrete
3. **Reciclaje de contenidos** — La tabla `reciclaje` está vacía. Falta definir: quién genera los datos, cuándo, y cómo se alimentan a cada agente. Se abordará en el diseño de orquestación CrewAI
4. **Modelo LLM para contenido** — Prueba (2026-03-15): Sonnet = mejor calidad ($0.13/sección), Kimi K2 = aceptable ($0.03/sección), Qwen 3 32B = descartado. Faltan pruebas con gramática, comunicación, cultura
5. **Crews pendientes** — Patrón Recurvo establecido (1 Crew = N agentes secuenciales, LLM por agente). Pendiente: aplicarlo a gramática, comunicación, cultura, destrezas, etc.

---

## Descripción del Proyecto

Un sistema de 3 capas para el curso de español A1.1 "Nuevo Compañeros 1" (SGEL, adolescentes 12-15 años):

**Capa 1 — Guía impresa (en desarrollo)**
Guía del profesor editorial con explotaciones didácticas para las 9 unidades del libro. Producto impreso de SGEL.

**Capa 2 — Sistema de agentes (en desarrollo)**
CrewAI: agentes autónomos con herramientas, memoria, orquestación y soporte multi-modelo (Groq/Anthropic/DeepSeek). Primer crew funcional: Recurvo v2.0 (vocabulario, 3 agentes). Pendiente: crews para las demás secciones.

**Capa 3 — Guías personalizadas (futuro)**
Profesores individuales adaptan la guía a su grupo, ritmo y necesidades.

### Premisa fundamental

**Todo está en construcción y todo puede cambiar.** No asumir que ningún componente es definitivo.

---

## Estado Actual

### Contenido producido (U03 es la unidad piloto)

| Componente | Estado |
|------------|--------|
| Vocabulario, Gramática, Itinerarios | Completos |
| Píldoras formativas (10), Tarjetas vocab, Material comp. | Completos |
| Comunicación, Destrezas, Cultura | Estructura creada, sin explotación |
| Reflexión, Evaluación | Estructura creada, sin contenido |
| U01-U02, U04-U09 | Plantillas con `*pendiente*` |

### Infraestructura pedagógica (estable)

Marco teórico (72 KB) + Curso general (50 KB) + 10 bancos de técnicas (~800+ técnicas) — todo completo.

### Sistema de agentes CrewAI

| Componente | Estado |
|------------|--------|
| Crew Recurvo (vocabulario) | **v2.0**. Pipeline: Generador → Verificador → Escritor. LLM + parámetros por agente. Reglas de formato editorial en `.claude/rules/criterios-generacion-tarjetas.md` (gramapop sin etiquetas Sing./Pl., `Femenino:`/`Masculino:` solo en Familia, combos con nomenclatura `[ ] ( ) / +`, colores por nivel) |
| 6 tools custom | consultar_inventario, consultar_tarjetas_previas, consultar_correcciones, consultar_reglas, escribir_tarjetas, exportar_csv |
| 12 modelos | Groq (7, gratis) + Anthropic (3) + DeepSeek (2). Config en dashboard |
| Tabla `crew_agents` (BD) | **Implementada.** Config mutable de agentes editable desde dashboard |
| Dashboard v8.5 | Material Design 3, navegación multi-nivel, paleta dorado-oliva/crema, LLM por agente, Editar/Guardar, ciclo de revisión, gestión de reglas |
| Feedback/aprendizaje | Ciclo completo: corrección web → BD → tool → agente. UX de revisión: progreso, patrones, crear regla desde corrección |
| Evaluación | DeepEval (5 métricas rule-based) + promptfoo (comparar LLMs) + tabla evaluaciones en BD |
| Langfuse (trazas) | Integrado. Se activa con `LANGFUSE_PUBLIC_KEY` en `.env` |
| 7 prompts .md + 6 repertorios | Referencia pedagógica, NO agentes autónomos. Pendientes de rediseño |
| **GitHub** | https://github.com/adminmc2/agentes_GDC1.git |
| **Railway** | https://agentiaelegd.up.railway.app |

---

## Repositorio y Despliegue

**GitHub/Railway** solo reciben el sistema de agentes (~20 archivos). El contenido editorial se queda local. Ver `GITHUB-MANIFEST.md` para la lista detallada.

**Estructura del repositorio (zona viejo / zona nuevo):**

El repo está en proceso de reorganización. Hoy convive lo "viejo" (estado actual sin tocar) y lo "nuevo" (estructura definitiva en construcción). Ver `PROCESO-MAESTRO.md` para el detalle.

- `viejo/` — todo el contenido editorial actual (unidades, materiales, agentes, repertorios, referencias, diseno, etc.). Sin cambios bruscos. De aquí se extrae lo que se va migrando.
- `nuevo/` — estructura definitiva en construcción. Caso piloto: U3.
- Raíz — código activo (`scripts/`, `web/`, `eval/`), dashboard (`diagrama.py`), docs (`CLAUDE.md`, `README.md`, `CHANGELOG.md`, `PROCESO-MAESTRO.md`, `ROADMAP.md`, `GITHUB-MANIFEST.md`), config (`Dockerfile`, `railway.toml`, `requirements.txt`, `.env.example`).

**Estructura por unidad (estado actual, en `viejo/unidades/UXX/`):**

```
viejo/unidades/UXX/
├── inventario.json              ← fuente canónica
├── fuente/                      ← PDF del libro
├── tarjetas/
│   ├── csv/                     ← salida del agente Recurvo
│   ├── diseno/                  ← PSDs, PNGs, INDD
│   └── validacion/              ← PDF/TEX de validación editorial
├── pildoras/                    ← PDFs/TEX de píldoras
└── *.md                         ← markdowns de producción por sección
```

**En GitHub:** `scripts/crewai/` (agentes + tools), `scripts/` (importación, pruebas), `eval/` (métricas + promptfoo), `diagrama.py` + `web/` (servidor + dashboard), Dockerfile, railway.toml, requirements.txt, .env.example

**Solo local:** todo `viejo/` (contenido editorial completo), CLAUDE.md, ROADMAP.md, PROCESO-MAESTRO.md, .env

**Separado (Desktop, sin git):** `SGEL-proyecto-impreso-Guia-1/` (8.4 GB)

---

## Qué NO Hacer

- No modificar archivos binarios (.pdf, .indd, .ai, .psd)
- No crear archivos nuevos sin necesidad
- No renombrar ni mover carpetas sin consultar
- No eliminar `*pendiente*` sin completar el contenido
- No asumir que la arquitectura de agentes es definitiva
- No tomar decisiones de diseño del sistema sin consultar al usuario
- No usar los prompts .md de `viejo/agentes/` como sistema autónomo — son referencia pedagógica
- No construir agentes sin prueba previa de calidad con los modelos reales
- No escribir role/goal/backstory en español — config en inglés, output en español (ver `.claude/rules/agent-prompt-design.md`)
- No hardcodear config mutable de agentes en Python — debe vivir en la tabla `crew_agents` de BD
- **No modificar `.claude/rules/agent-prompt-design.md` sin autorización explícita del usuario.** Este archivo contiene la metodología de diseño de agentes y la referencia del pipeline Recurvo. Cualquier cambio (añadir, editar o eliminar contenido) requiere aprobación previa
- **No modificar `.claude/rules/tool-design.md` sin autorización explícita del usuario.** Metodología de diseño de herramientas (9 principios). Misma protección que el archivo de agentes
- **No modificar `scripts/crewai/tools.py` sin consultar la metodología en `.claude/rules/tool-design.md`.** Toda creación o modificación de herramientas debe cumplir los 9 principios

---

## Proceso de generación del inventario

1. Exportar desde InDesign un **PDF con texto embebido** por unidad → `viejo/unidades/UXX/fuente/`
2. Claude lee el PDF → extrae actividades al JSON → `viejo/unidades/UXX/inventario.json`
3. Validar JSON vs fuente, corregir errores
4. Importar a BD con `scripts/importar_inventario.py viejo/unidades/UXX/inventario.json` (idempotente)

> **Completado para U03:** 10 páginas, 47 actividades, 184 respuestas, 3 cuadros gramaticales.

---

## Base de datos (Neon PostgreSQL)

Fuente de verdad del proyecto. JSON es formato de intercambio; la BD almacena todo.

- **Esquema:** 11 tablas — unidades, paginas, actividades, respuestas, cuadros_gramaticales, reciclaje, profesores, grupos, personalizaciones, **crew_agents**, **reglas_aprendidas**
- **`crew_agents`:** Config mutable de agentes (role, goal, backstory, task_description, task_expected_output, max_iter). Editable desde dashboard. Implementada con datos de Recurvo (3 agentes)
- **`reglas_aprendidas`:** Dos tipos de reglas: (1) **especificaciones de producto** — definidas por diseño, raramente cambian (ej: formato sílaba tónica, qué es un combo); (2) **patrones aprendidos** — destilados de correcciones acumuladas, crecen con el uso (ej: "día es masculino pese a terminar en -a"). Actualmente solo hay tipo 1 (4 reglas seed). Tipo 2 pendiente de desarrollar cuando haya correcciones reales. Campos: tipo_error, regla, ejemplos, n_correcciones, activa. El agente las consulta con `consultar_reglas`
- **`contenidos_indice` (JSONB):** En tabla `unidades`. Índice de contenidos del libro para U00-U09. Pendiente: completar con detalle real cuando se generen inventarios
- **Importación:** `scripts/importar_inventario.py` — DELETE CASCADE + reimportación

---

## Flujo completo de producción

1. **Exportar material fuente** — InDesign → PDF embebido → `viejo/unidades/UXX/fuente/`
2. **Extraer inventario** — Claude lee PDF → JSON → `viejo/unidades/UXX/inventario.json`
3. **Validar inventario** — Comparación visual fuente vs JSON
4. **Importar a BD** — JSON → script → Neon PostgreSQL
5. **Poblar reciclaje** — Mapear contenido lingüístico entre secciones/unidades
6. **Ejecutar crew** — CrewAI genera explotación didáctica por sección (inventario + reciclaje + repertorio + infraestructura)

> Patrón establecido con Recurvo. Pendiente: crear crews para gramática, comunicación, cultura, destrezas, etc.

---

## Pendientes

- [x] Arquitectura de referencia (Crew Recurvo v2.0)
- [x] Script de importación JSON → PostgreSQL
- [x] Metodología de diseño de prompts (`.claude/rules/agent-prompt-design.md`)
- [x] Política de idioma (inglés config, español output)
- [x] Tabla `crew_agents` + API + dashboard editable
- [ ] Crews para demás secciones (gramática, comunicación, cultura, destrezas, etc.)
- [ ] Instrucciones de uso de agentes (para usuarios finales)
- [x] UX del ciclo de aprendizaje — **prerequisito para reglas tipo 2**. Sin UX que facilite corregir, no se acumulan correcciones, y sin correcciones no hay patrones que destilar. Incluye: (1) opción "crear regla" desde el modal de corrección, (2) interfaz de gestión de reglas, (3) estado de revisión por tarjeta (sin_revisar/revisada), (4) panel de patrones (correcciones agrupadas por tipo), (5) indicadores de progreso de revisión
- [ ] Proceso de destilación de reglas tipo 2 (patrones aprendidos de correcciones acumuladas). **Depende de UX del ciclo de aprendizaje.** Hoy es manual (opción A). Cuando haya suficientes correcciones, evaluar semi-automatización (opción B)
- [ ] Estructura definitiva del proyecto y convenciones de nombrado
- [ ] Comandos útiles y archivos clave para contexto
