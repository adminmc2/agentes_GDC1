# PROCESO-MAESTRO — Árboles del repositorio (histórico)

Archivo de los dos árboles históricos del repositorio que vivían embebidos en `PROCESO-MAESTRO.md` Parte 3. Texto íntegro, sin reescribir.

El árbol vivo (estado físico real, hoy) sigue en `PROCESO-MAESTRO.md` Parte 3.

Los dos archivos aquí archivados:
- **Árbol intermedio:** estado anterior, pre-disolución de `nuevo/`. Útil para entender la estructura de la fase de migración cuando `nuevo/` y `viejo/` coexistían como zonas separadas.
- **Árbol antes del split:** referencia histórica, anterior a 2026-05-05 12:15. Estado del repo cuando todo el contenido editorial vivía en raíz, antes del split a `viejo/`.

---

### Árbol intermedio (estado anterior — pre-disolución de `nuevo/`)

```
guia-didactica-profesor-IA/
│
├── viejo/                                       ← contenido editorial actual sin tocar
│   ├── unidades/U03/                            (única poblada en aquel momento)
│   ├── materiales/                              (1 archivo: especificaciones-diseno-tarjetas.md)
│   ├── agentes/                                 (7 ag-*.md + 4 resumen-configuracion-*.md)
│   ├── repertorios/                             (6 bancos por sección)
│   ├── referencias/                             (12 documentos de técnicas)
│   ├── diseno/                                  (propuestas con versiones)
│   ├── material-complementario/                 (gitignored, ~21 MB)
│   ├── _template/                               (origen desconocido)
│   ├── marco-teorico-metodologico.md
│   └── 00-curso-general.md
│
├── nuevo/                                       ← estructura definitiva en construcción
│   ├── README.md
│   ├── unidades/U3/                             (vacía, esperando migración)
│   └── scripts/prompts/                         (vacía, pendiente extraccion-inventario.md)
│
├── scripts/                                     ← código activo (raíz)
│   ├── importar_inventario.py
│   ├── crear_crew_agents.py
│   ├── probar_modelos.py
│   └── crewai/{recurvo.py, tools.py, tool_versions.json}
│
├── web/                                         ← dashboard activo (raíz)
│   ├── index.html (90 KB)
│   └── favicon.svg
├── diagrama.py                                  ← servidor del dashboard (raíz, mal nombrado)
│
├── eval/                                        ← evaluación (raíz)
│   ├── evaluar_tarjetas.py
│   ├── provider_crewai.py
│   └── promptfoo.yaml
│
├── .claude/
│   ├── rules/{agent-prompt-design.md, tool-design.md, criterios-generacion-tarjetas.md, criterios-generacion-texto.md}
│   └── settings.json
│
├── README.md, CLAUDE.md, CHANGELOG.md, ROADMAP.md, GITHUB-MANIFEST.md
├── PROCESO-MAESTRO.md                           ← este documento (temporal)
├── Dockerfile, railway.toml, requirements.txt, .env.example
└── .gitignore, .dockerignore
```

---

### Árbol antes del split (referencia histórica — anterior a 2026-05-05 12:15, NO ES EL ESTADO ACTUAL)

```
guia-didactica-profesor-IA/
├── unidades/
│   ├── U03/                                    ← única unidad poblada
│   │   ├── inventario.json                     (pendiente renombrar a U3-nc1-inventario.json)
│   │   ├── fuente/
│   │   │   └── U03-libro.pdf                   (pendiente renombrar a U3-nc1.pdf)
│   │   ├── tarjetas/{csv,diseno,validacion}/
│   │   ├── pildoras/                           (10 PDFs + 10 TEX)
│   │   └── U03-{vocabulario,gramatica,...}.md  (16 MDs por sección + variantes)
│   ├── U01/, U02/                              (solo placeholder MD; carpetas internas creadas)
│   └── U04/, U05/, ... U09/                    (solo placeholder MD; carpetas internas creadas)
│
├── .claude/
│   ├── rules/
│   │   ├── agent-prompt-design.md              (meta-regla técnica, protegida)
│   │   ├── tool-design.md                      (meta-regla técnica, protegida)
│   │   ├── criterios-generacion-tarjetas.md    (criterio editorial — mezcla mal con meta-reglas)
│   │   └── criterios-generacion-texto.md       (criterio editorial — mezcla mal con meta-reglas)
│   └── settings.json
│
├── agentes/                                     ← 7 archivos: especificaciones operativas vivas
│   ├── ag-vocabulario.md                       (35 KB — incluye banco de píldoras)
│   ├── ag-gramatica.md                         (18 KB — incluye banco de píldoras)
│   ├── ag-comunicacion.md                      (29 KB)
│   ├── ag-destrezas.md                         (30 KB)
│   ├── ag-cultura.md                           (22 KB)
│   ├── ag-evaluacion.md                        (16 KB)
│   ├── orquestador.md                          (7.5 KB)
│   └── resumen-configuracion-*.md              (4 archivos, 24-31 KB cada uno)
│
├── repertorios/                                 ← 6 bancos de técnicas por sección
│   ├── vocabulario.md, gramatica.md, comunicacion.md
│   ├── destrezas.md, cultura.md, evaluacion.md
│
├── referencias/                                 ← 12 documentos de técnicas detalladas
│   ├── repertorio-120-tecnicas-EIO.md
│   ├── repertorio-124-tecnicas-CA.md
│   ├── analisis-100-tecnicas-CL.md
│   ├── analisis-84-estrategias-EE.md
│   └── ... (8 más)
│
├── materiales/                                  ← solo 1 archivo (queda casi vacía)
│   └── especificaciones-diseno-tarjetas.md     (162 líneas, desactualizado desde abril)
│
├── scripts/
│   ├── importar_inventario.py                  (JSON → BD)
│   ├── crear_crew_agents.py
│   ├── probar_modelos.py
│   ├── crewai/
│   │   ├── recurvo.py                          (orquestador CrewAI)
│   │   ├── tools.py                            (6 tools, protegida)
│   │   └── tool_versions.json
│   └── resultados_prueba/                      (basura: salidas viejas)
│
├── web/
│   ├── index.html                              (dashboard Material Design 3)
│   └── favicon.svg
├── diagrama.py                                  ← servidor web mal nombrado, suelto en raíz
│
├── eval/
│   ├── evaluar_tarjetas.py                     (5 métricas DeepEval)
│   ├── provider_crewai.py                      (wrapper promptfoo)
│   └── promptfoo.yaml
│
├── diseno/                                      ← propuestas con versiones (poco claro qué es vigente)
│
├── material-complementario/                     (gitignored, solo local, ~21 MB)
├── _template/                                   (sin trackear, propósito desconocido)
│
├── marco-teorico-metodologico.md                ← suelto en raíz
├── 00-curso-general.md                          ← suelto en raíz
├── README.md, CLAUDE.md, CHANGELOG.md, ROADMAP.md, GITHUB-MANIFEST.md
├── PROCESO-MAESTRO.md                           ← este documento (temporal)
├── Dockerfile, railway.toml, requirements.txt, .env.example
├── .gitignore, .dockerignore
└── BASURA TÉCNICA: texput.log, __pycache__/, .DS_Store, eval/__pycache__/
```

### Notas históricas adicionales (anteriores al split)

> Lo siguiente describe cambios previos al split de zonas `viejo/` + `nuevo/`. Ya está reflejado en el árbol actual de arriba. Se conserva como contexto.

```
guia-didactica-profesor-IA/
├── unidades/                       ← contenido editorial (U03 migrado, resto placeholders)
├── .claude/rules/                  ← 4 archivos: 2 meta-reglas + 2 criterios editoriales (mezcla)
├── materiales/                     ← solo 1 archivo (especificaciones-diseno-tarjetas.md)
├── scripts/                        ← código Python
├── web/                            ← dashboard
├── eval/                           ← evaluación
├── repertorios/                    ← 6 repertorios por sección
├── referencias/                    ← 12 documentos de técnicas
├── agentes/                        ← 11 prompts MD de agentes (referencia, no ejecutable)
├── diseno/                         ← documentos de diseño con versiones
├── pedagogia/                      ← (no existe todavía)
├── _template/                      ← carpeta sin trackear, propósito desconocido
├── material-complementario/        ← solo local (gitignored)
├── marco-teorico-metodologico.md   ← suelto en raíz
├── 00-curso-general.md             ← suelto en raíz
├── diagrama.py                     ← servidor web suelto en raíz (mal nombrado)
├── README.md, CLAUDE.md, CHANGELOG.md, ROADMAP.md, GITHUB-MANIFEST.md
└── Dockerfile, railway.toml, requirements.txt, .env.example
```

### Problemas conocidos

- `.claude/rules/` mezcla meta-reglas técnicas con criterios editoriales.
- `materiales/` quedó casi vacía (1 archivo).
- `repertorios/` y `referencias/` solapan parcialmente sin jerarquía.
- **`agentes/*.md` son especificaciones operativas vivas, no "prompts viejos".** Contienen protocolos por sección (banco de píldoras, criterios de selección, ciclo de fases). Son referencia activa para Claude Code, no material a archivar. Esto invalida la idea anterior de moverlos a `pedagogia/agentes-prompts-referencia/`.
- Marco teórico y curso general están sueltos en raíz.
- `diagrama.py` es realmente el servidor web (mal nombrado).
- Hay basura técnica: `texput.log`, `__pycache__/`, `.DS_Store`, `scripts/resultados_prueba/`.
- `_template/` sin trackear, propósito por confirmar.

### Hallazgo importante sobre los archivos `agentes/*.md`

Tras revisar contenido, los 7 archivos `ag-*.md` (vocabulario, gramática, comunicación, destrezas, cultura, evaluación, orquestador) **son los documentos más densos del proyecto en cuanto a protocolo operativo**. Cada uno mezcla:

- Configuración de un agente CrewAI (rol, objetivo, tarea).
- Criterios pedagógicos de su sección (qué hacer, en qué orden, con qué técnicas).
- Bancos de acciones reutilizables (la Fase 5 vive aquí, dispersa).
- Referencias a marcos teóricos (Conti, MARS EARS, Gagné, VanPatten).

Esto significa que la **especificación por sección** que estábamos buscando ya existe parcialmente: está dentro de `ag-*.md`. La reorganización debe **separar dos cosas mezcladas en cada archivo**:
- La parte que es **especificación operativa de la sección** (criterios, protocolos, bancos) → debe ir a `especificaciones/SECCION/`.
- La parte que es **configuración del agente CrewAI** (rol, prompt, tools) → debe ir a `scripts/crewai/` o a la BD `crew_agents`.

Esto es una decisión de diseño todavía no tomada. Va a la Parte 5 como pendiente nueva.

---
