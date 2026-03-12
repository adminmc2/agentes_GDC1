# CLAUDE.md — Guía Didáctica del Profesor (SGEL)

> **ESTADO:** Proyecto en desarrollo activo. Arquitectura de agentes en redefinición. Todo puede cambiar.

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
- Si este archivo supera las 500 líneas, considerar dividirlo en archivos separados según las funciones del proyecto (ej. instrucciones de agentes, estado, restricciones) e importarlos desde un CLAUDE.md principal

---

## PREGUNTAS PENDIENTES (REVISAR EN CADA SESION)

Antes de continuar trabajando, el asistente DEBE revisar estas preguntas con el usuario:

### 1. Tareas en curso
**Pregunta:** ¿Hay tareas específicas en curso que documentar?
**Respuesta:** *pendiente*

### 2. Instrucciones de uso de agentes
**Pregunta:** ¿Hay instrucciones específicas que añadir sobre cómo generar nuevas unidades con los agentes?
**Respuesta:** *pendiente* (depende de la redefinición en curso)

### 3. Nivel de detalle
**Pregunta:** ¿El nivel de detalle del CLAUDE.md es correcto (más/menos información en alguna sección)?
**Respuesta:** *pendiente*

### 4. Restricciones
**Pregunta:** ¿Hay algo que añadir o quitar de la sección "Qué NO hacer"?
**Respuesta:** *pendiente*

---

## Descripción del Proyecto

### Qué es

Un sistema de 3 capas para el curso de español A1.1 "Nuevo Compañeros 1" (SGEL, adolescentes 12-15 años):

**Capa 1 — Guía impresa (en desarrollo)**
Guía del profesor editorial con explotaciones didácticas para las 9 unidades del libro. Producto impreso que publica SGEL. En desarrollo activo.

**Capa 2 — Sistema de agentes (en redefinición)**
Agentes IA que generan las explotaciones didácticas. Actualmente v5.0 con 7 agentes especializados + orquestador, pero la arquitectura está siendo revisada y puede cambiar completamente.

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

### Sistema de agentes (en redefinición)

| Componente | Estado |
|------------|--------|
| 7 agentes v5.0 + orquestador | Operativos, pero sujetos a cambio |
| 6 repertorios | Completos, pero sujetos a cambio |
| 4 resúmenes de configuración | Propósito no documentado |
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
├── agentes/                       # Agentes + orquestador (puede cambiar)
├── repertorios/                   # Opciones de explotación (puede cambiar)
├── unidades/                      # U01-U09, cada una en su carpeta (UXX/). Solo U03 con contenido
├── datos/                         # Inventarios JSON + imágenes del libro
├── referencias/                   # Bancos de técnicas pedagógicas
├── materiales/                    # Píldoras formativas (LaTeX/PDF) + tarjetas
├── material-complementario/       # PDFs editoriales + PowerPoint
├── tarjetas/                      # Diseño InDesign de tarjetas
└── diseno/                        # Propuestas del sistema de agentes

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

---

## Secciones Pendientes de Completar

Las siguientes secciones se añadirán según avance la redefinición:

- [ ] Arquitectura definitiva de agentes
- [ ] Estructura definitiva del proyecto
- [ ] Convenciones de nombrado finales
- [ ] Instrucciones de uso de agentes
- [ ] Flujo de trabajo completo
- [ ] Comandos útiles
- [ ] Archivos clave para contexto
