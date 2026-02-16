# PRESENTACIÓN DEL PROYECTO
## Sistema de Agentes v5.0 — Guía Didáctica Nuevo Compañeros 1
### Contenido para diapositivas (para Kimi)

---

## DIAPOSITIVA 1 — PORTADA

**Título:** Guía Didáctica del Profesor — Nuevo Compañeros 1
**Subtítulo:** Sistema de Agentes v5.0 con IA
**Producto:** SGEL — Nivel A1.1 — Adolescentes 12-15 años
**Versión:** v5.0

---

## DIAPOSITIVA 2 — EL PRODUCTO

**Título:** ¿Qué estamos creando?

**Contenido:**
- Una **guía didáctica impresa** para el profesor de *Nuevo Compañeros 1*
- Cubre las **9 unidades** del libro, sección por sección
- Incluye instrucciones detalladas para **cada actividad** del libro, sin excepción
- Generada con un sistema de **14 agentes de IA** especializados y coordinados

**Frase clave:** *No es una guía genérica: es una explotación didáctica completa, fundamentada teóricamente y adaptada a cada actividad concreta del libro.*

---      

## DIAPOSITIVA 3 — ESTRUCTURA DE LA GUÍA (por unidad)

**Título:** ¿Qué contiene la guía?

| Sección | Contenido | Quién lo genera |
|---------|-----------|-----------------|
| **1. Explotación didáctica** | Instrucciones sección por sección (Vocabulario, Gramática, Comunicación, Destrezas, Cultura, Reflexión, Evaluación) | 7 agentes de sección |
| **2. Atención a la diversidad** | Adaptaciones por perfil + errores frecuentes por L1 | Agente Diversidad |
| **3. Priorización temporal** | Qué actividades son prioritarias según horas disponibles | Agente Priorizador |
| **4. Píldoras** | Material reproducible para el alumno (multilingüe) | Agente Píldoras |
| **5. Solucionario** | Respuestas + transcripciones | Agente Solucionario |

---

## DIAPOSITIVA 4 — EL PROBLEMA (v4.0)

**Título:** ¿Por qué un rediseño?

**Punto 1 — Documentos demasiado largos:**
- Marco teórico: ~20.000 tokens (1.140 líneas)
- Curso general: ~15.000 tokens (780 líneas)
- El agente recibía todo cuando solo necesitaba una fracción

**Punto 2 — Un solo agente para todo:**
- El Agente Redactor de v4.0 generaba Vocabulario, Gramática, Comunicación, Destrezas, Cultura...
- Necesitaba leer ~35-45K tokens de contexto antes de escribir una línea
- Criterios diferentes por sección → decisiones inconsistentes

**Punto 3 — Desconexión:**
- El marco teórico no distinguía cómo usar cada sección en la práctica
- Los agentes no sabían qué buscar en cada documento

**Visual sugerido:** Diagrama con un agente grande (v4.0) rodeado de documentos enormes → sobrecarga

---

## DIAPOSITIVA 5 — PRINCIPIOS DEL REDISEÑO

**Título:** 6 principios de la v5.0

| # | Principio | Qué significa |
|---|-----------|---------------|
| 1 | **Integrar, no leer** | El contenido teórico se destila e integra en las instrucciones de cada agente. No leen documentos largos |
| 2 | **Organizar por secciones** | La guía se estructura por secciones del libro (Vocabulario, Gramática...), no por lecciones |
| 3 | **Repertorios, no plantillas** | Cada tipo de actividad tiene múltiples opciones de explotación. El agente elige la más adecuada |
| 4 | **Contexto mínimo** | Cada agente recibe solo lo que necesita (~8K tokens vs. ~40K en v4.0) |
| 5 | **1 agente = 1 sección** | Cada sección del libro tiene su propio agente especializado |
| 6 | **Priorización después** | Primero se explota todo; después se prioriza según horas disponibles |

---

## DIAPOSITIVA 6 — ARQUITECTURA: VISIÓN GENERAL

**Título:** 14 agentes, 5 tipos

**Visual sugerido:** Diagrama con los 5 tipos de agentes organizados por fases

| Tipo | Agentes | Cuántos |
|------|---------|---------|
| **Preparación** | Ingesta | 1 |
| **Coordinación** | Orquestador | 1 |
| **Sección** | Vocabulario, Gramática, Comunicación, Destrezas, Cultura, Reflexión, Evaluación | 7 |
| **Dedicado** | Píldoras | 1 |
| **Transversal** | Diversidad, Solucionario | 2 |
| **Post-producción** | Priorizador, Revisor | 2 |
| **TOTAL** | | **14** |

**Frase clave:** *7 secciones del libro = 7 agentes especializados. 1 agente = 1 sección.*

---

## DIAPOSITIVA 7 — FLUJO DE TRABAJO

**Título:** ¿Cómo funciona el proceso?

**FASE ANTES:**
```
PDF del libro → Agente Ingesta → inventario.json (actividades estructuradas por sección)
                                → Editor define píldoras (4-5 por unidad)
```

**FASE DURANTE:**
```
Inventario → Orquestador → filtra repertorio + contexto para cada sección
                         → invoca 7 agentes de sección (en secuencia)
                         → invoca Agente Píldoras (en paralelo)
                         → invoca agentes transversales (sobre resultado compilado)
                         → verifica coherencia del conjunto
```

**FASE DESPUÉS:**
```
Explotación completa → Priorizador temporal → propuesta 2h vs. 3+h
                     → Revisor → control de calidad
                     → Editor → validación final
```

---

## DIAPOSITIVA 8 — EL ORQUESTADOR

**Título:** El orquestador: coordinar sin generar

**Lo que HACE:**
- Pre-filtra el repertorio según los tipos de actividad de cada sección
- Prepara el contexto lingüístico (progresiones, reciclaje)
- Invoca a cada agente de sección con solo lo que necesita
- Verifica coherencia del conjunto después

**Lo que NO hace:**
- No genera explotación didáctica
- No lee el marco teórico completo
- No toma decisiones de contenido lingüístico

**Criterios de verificación post-producción:**

| Criterio | Umbral |
|----------|--------|
| Horas totales | ≤7h por unidad |
| Variedad | No repetir misma opción en >2 actividades consecutivas |
| Reciclaje | ≥30% conexiones con unidades anteriores |
| Gamificación | 1-2 elementos lúdicos por sección |
| Agrupamientos | ≥3 tipos por sección |
| Ritmicidad | Máximo 15 min de foco intenso |

---

## DIAPOSITIVA 9 — AGENTES DE SECCIÓN

**Título:** 7 agentes especializados

| Agente | Sección | Repertorios clave |
|--------|---------|-------------------|
| **Vocabulario** | Vocabulario | Ciclo 5 fases, Constructores de frases, categorización, tarjetas |
| **Gramática** | Gramática | Ciclo 5 fases, inductivo/deductivo, apoyo decreciente, cuadros |
| **Comunicación** | Comunicación | Diálogos, producción oral, Pre-Durante-Post auditivo |
| **Destrezas** | Destrezas | Comprensión lectora/auditiva, tarjetas de estrategia |
| **Cultura** | Cultura | Conexión intercultural, cognición encarnada, debate |
| **Reflexión** | Reflexión | Autoevaluación, repaso integrador, portafolio |
| **Evaluación** | Evaluación | Rúbricas MCER, evaluación entre pares |

**Cada agente genera:**
- Estación de servicio (tarjetas de andamiaje)
- Insignia (micro-credencial gamificada)
- Explotación por bloques (con notas lingüísticas integradas)

---

## DIAPOSITIVA 10 — REPERTORIOS DE EXPLOTACIÓN

**Título:** Repertorios: variedad con criterio

**¿Qué es un repertorio?**
Un conjunto de **opciones de explotación** para un tipo de actividad, con **criterios de selección** que determinan cuál usar según el contexto.

**Ejemplo — Comprensión lectora (Ag. Destrezas):**

| Opción | Cuándo |
|--------|--------|
| Pre-Durante-Post estándar | Texto informativo, primera lectura |
| Lectura guiada con tarjetas | Texto largo o complejo |
| Extracción textual | Texto rico en gramática |
| Lectura + producción | Texto modelo para escritura |
| Lectura cooperativa (rompecabezas) | Múltiples perspectivas |

**Variables que determinan la selección:**
- Longitud y complejidad del texto
- Posición en la unidad
- Recursos disponibles (audio, imagen)
- Contenido reciclable
- Actividad adyacente

**Frase clave:** *Dos actividades de comprensión lectora en la misma unidad nunca se explotan igual.*

---

## DIAPOSITIVA 11 — REDUCCIÓN DE CONTEXTO

**Título:** De 40K tokens a 8K por invocación

**v4.0 — Un agente recibía TODO:**
- Marco teórico completo (~20K)
- Curso general completo (~15K)
- Inventario completo de la unidad
- **Total: ~35-45K tokens**

**v5.0 — Cada agente recibe SOLO lo suyo:**

| Componente | Tokens |
|------------|--------|
| Instrucciones (principios destilados) | ~2.000 |
| Repertorio filtrado | ~2.000-3.000 |
| Criterios de selección | ~500 |
| Actividades de la sección | ~1.000-2.000 |
| Contexto lingüístico | ~1.000 |
| Contenidos para reciclaje | ~500-1.000 |
| **Total** | **~7.000-9.500** |

**Visual sugerido:** Comparación visual: barra grande (40K) vs. barra pequeña (8K) = reducción 5x

---

## DIAPOSITIVA 12 — ESTACIÓN DE SERVICIO

**Título:** Andamiaje visible: la Estación de Servicio

**¿Qué es?**
Tarjetas imprimibles organizadas en cajas temáticas que el alumno consulta libremente durante las actividades.

**Principio:** El alumno busca lo que necesita en lugar de preguntar al profesor → fomenta autonomía.

**Características:**
- Tarjetas imprimibles por sección
- Organizadas en cajas con nombre descriptivo
- Mezclan contenido nuevo + repaso
- **Acumulativas**: crecen unidad a unidad
- **Cada agente de sección tiene su propio plantilla de tarjeta** (formato estándar para todo el curso)

**Ejemplo real — Estación de servicio de U03 Vocabulario (Parientes):**

| Caja | Contenido |
|------|-----------|
| **Tarjetas de vocabulario** | 20 tarjetas con plantilla de 10 elementos (una por palabra). Campo semántico: Familia (violeta) |
| **Árbol genealógico ampliado** | Recurso de aula en tamaño grande con los 11 nombres del libro |
| **Pistas de hoy** | Patrón -o/-a, excepciones (padre/madre), plurales mixtos, exposición incidental |

**Las cajas dependen de la sección.** Gramática tendrá paradigmas y conectores. Comunicación tendrá exponentes y estrategias.

---

## DIAPOSITIVA 12b — TEMPLATE DE TARJETA DE VOCABULARIO

**Título:** Template de tarjeta de vocabulario: 10 elementos

**Cada tarjeta de vocabulario del curso sigue este formato estándar** (una tarjeta por palabra):

**CARA A — Consulta rápida:**

| Zona | Elemento |
|------|----------|
| Esquina sup. izquierda | **Nº de unidad** (U01, U02, U03...) |
| Esquina sup. derecha | **Icono + color del campo semántico** (un color por campo: familia = violeta) |
| Centro (texto grande) | **Palabra en español** con sílaba tónica en negrita (a-**bue**-lo) |
| Color del texto | **Color por género gramatical** (azul = M, rojo = F, negro = sin género) |
| Debajo de la palabra | **Regla morfológica** (por qué tiene esa forma: "M en -o, F en -a" o "Irregular: raíces distintas") |
| Debajo del centro | **Ejemplo contextualizado** (frase corta de uso real) |
| Junto a la palabra | **Marca de frecuencia** (★ / ★★ / ★★★) |
| Pie de tarjeta | **💬 Señal de irregularidad** (solo si aplica: bocadillo con descripción breve) |
| Zona inferior | **Espacio en blanco para nota personal** (el alumno personaliza) |

**CARA B — Traducción multilingüe:**
Traducciones en las 6 L1 del aula: IT · FR · PT-BR · EN · CS · PL

**Frase clave:** *La tarjeta es autosuficiente: contiene el dato (palabra + género), la explicación (regla), el uso (ejemplo), la prioridad (frecuencia) y la traducción. El alumno no necesita al profesor para consultarla.*

---

## DIAPOSITIVA 13 — INSIGNIAS

**Título:** Gamificación: una insignia por sección

**¿Qué es?**
Una micro-credencial que el alumno obtiene al completar cada sección.

**Características:**
- **Una por sección**, no por actividad ni por unidad
- **Nombre temático** vinculado al contenido (ej: "Genealogista" para vocabulario de familia)
- **Competencia demostrable**: "Sé nombrar a los miembros de mi familia en español"
- **Criterio de obtención**: completar actividades + acumular puntos
- **Compartible** en redes sociales
- **Imprimible** para entregar en clase
- **Tono motivador**, no competitivo
- **Única** en todo el curso (no se repite)

**Se presenta al inicio de cada sección** → da dirección y propósito a todas las actividades.

---

## DIAPOSITIVA 14 — PÍLDORAS

**Título:** Píldoras: material pautado para el alumno

**¿Qué es?**
Material complementario que guía al alumno en la comprensión de contenido nuevo. 4-5 por unidad.

**Doble formato:**

| Producto | Para qué | Formato |
|----------|----------|---------|
| Presentación interactiva | El profesor la proyecta en clase | Digital |
| Hoja del estudiante | El alumno la recibe para trabajar | Imprimible |

**Estructura fija (ambos formatos):**
1. **Descubrimiento guiado** — preguntas inferenciales en L1
2. **Regla explícita** — presentación clara
3. **Comprensión de la regla** — verificación (V/F, completar)
4. **Espacio para notas** — el alumno anota

**Multilingüe:** Cada píldora se genera en 6 lenguas maternas:
IT, FR, PT-BR, EN, CS, PL

**Tipos:** Gramatical, de vocabulario, de mediación/funciones

---

## DIAPOSITIVA 15 — SECUENCIACIÓN DIDÁCTICA

**Título:** Cómo se estructura la explotación

**Principio:** No se organiza actividad por actividad, sino por **bloques agrupados por lógica didáctica**.

**Estructura de cada sección:**
```
SECCIÓN: [Nombre] — Páginas [XX-YY]

  ┌─ ESTACIÓN DE SERVICIO ──────────────┐
  │  Cajas de tarjetas de andamiaje     │
  └─────────────────────────────────────┘

  ┌─ GAMIFICACIÓN ──────────────────────┐
  │  Insignia + objetivo + criterio     │
  └─────────────────────────────────────┘

  ┌─ ACTIVIDADES 1-4 ──────────────────┐
  │  Objetivo del bloque               │
  │  Preparación (imprimir, preparar)  │
  │  Fase 1: Título descriptivo        │
  │  Fase 2: Título descriptivo        │
  │  Notas lingüísticas (integradas)   │
  │  Puntos de insignia                │
  └─────────────────────────────────────┘

  ┌─ ACTIVIDADES 5-8 ──────────────────┐
  │  [mismo patrón]                    │
  └─────────────────────────────────────┘

  ┌─ CIERRE DE SECCIÓN ────────────────┐
  │  Recuento + reflexión + tarea      │
  └─────────────────────────────────────┘
```

---

## DIAPOSITIVA 16 — NOTAS LINGÜÍSTICAS INTEGRADAS

**Título:** Notas lingüísticas: donde el profesor las necesita

**Principio:** El profesor no va a buscar información a otra parte de la guía. La nota está exactamente donde la necesita.

**Formato visual diferenciado:**
```
┌─ NOTA LINGÜÍSTICA ─────────────────────────────────┐
│ El verbo "tener" presenta irregularidad vocálica    │
│ (e→ie) en todas las personas excepto nos/vos.      │
│ Primer verbo irregular que ven los alumnos.         │
│ Conexión U04: "querer" sigue el mismo patrón.      │
└─────────────────────────────────────────────────────┘
```

**Cada agente genera sus propias notas:**

| Agente | Tipo de notas |
|--------|---------------|
| Vocabulario | Cognados, falsos amigos, campos semánticos, género, plurales mixtos |
| Gramática | Paradigmas, irregularidades, contraste L1, conexiones entre unidades |
| Comunicación | Exponentes alternativos, registro formal/informal, pragmática |
| Destrezas | Vocabulario pasivo, estrategias de deducción |
| Cultura | Léxico cultural, referentes culturales |

---

## DIAPOSITIVA 17 — PRINCIPIOS TEÓRICOS DESTILADOS

**Título:** Marco teórico → Instrucciones operativas

**No se lee el marco teórico completo.** Se destila en principios directos para cada agente:

| Fuente teórica | Cómo se usa | En qué agente |
|----------------|-------------|----------------|
| **Merrill** (§1) | 6 acciones de enriquecimiento | Comunicación, Cultura |
| **Gagné** (§2) | Lista de verificación | Todos (post-redacción) |
| **Inductivo/Deductivo** (§3) | Decisión por contenido | Gramática |
| **Atención** (§4) | Límites temporales (10-15 min) | Todos |
| **CLT** (§5) | Límites de carga cognitiva | Todos |
| **Recursividad** (§6) | Proceso reciclaje 4 pasos | Vocabulario, Gramática |
| **Ciclo 5 fases** (§8) | Protocolo completo | Vocabulario, Gramática |
| **Apoyo decreciente** (§8.11) | Apoyo decreciente | Gramática, Vocabulario |
| **Constructores de frases** (§8.13) | Matrices combinatorias | Vocabulario |

**Todos los agentes comparten:**
- Restricción de atención: 10-15 min por actividad
- CLT regla de oro: todo lo añadido reduce carga, no la aumenta
- Ritmicidad atencional: alternancia foco/difuso
- Gamificación integrada

---

## DIAPOSITIVA 18 — RECICLAJE Y COHERENCIA

**Título:** Regla 70/30 y coherencia entre secciones

**Regla 70/30:**
- 70% contenido nuevo de la sección
- 30% reciclaje de unidades anteriores

**El orquestador gestiona la coherencia:**
- Prepara para cada agente un resumen de contenidos anteriores
- Señala conexiones naturales entre unidades
- Indica qué de la sección de Vocabulario se puede aprovechar en Gramática

**Ejemplo de coherencia Vocabulario → Gramática:**
```
Los textos de Vocabulario (p.34-35) ya usan formas del presente regular:
"vive en Madrid", "trabaja en un hospital", "tiene 42 años"

→ El alumno ya ha tenido exposición incidental (Fase 1a: modelado)
→ El Agente Gramática puede usar un Ciclo abreviado
→ Conexión explícita: "¿Recordáis las formas de los textos?"
```

---

## DIAPOSITIVA 19 — PRIORIZACIÓN TEMPORAL

**Título:** Después de explotar todo: priorizar

**El Agente Priorizador trabaja DESPUÉS** de que toda la explotación esté completa.

**Criterios de prioridad para clase (2h/semana):**

| Prioridad ALTA (en clase) | Prioridad BAJA (casa/autónomo) |
|---------------------------|-------------------------------|
| Interacción oral, parejas, grupos | Individual, escrito, mecánico |
| Contenido nuevo (primera exposición) | Práctica adicional |
| Necesita corrección inmediata | Autocorregible con solucionario |
| Requiere mediación del profesor | Instrucciones autosuficientes |
| Fases 1, 3, 4 del Ciclo | Fases 2a receptiva, 5 consolidación |

**Resultado:** Tabla por unidad con actividades prioritarias (2h) vs. todas (3+h)

---

## DIAPOSITIVA 20 — DOS PRODUCTOS, DOS MOMENTOS

**Título:** Fase 1 (ahora) + Fase 2 (después)

| | Fase 1: Guía impresa | Fase 2: Herramienta adaptativa |
|---|---------------------|-------------------------------|
| **Qué** | Explotación completa de todas las actividades | El profesor personaliza según su contexto |
| **Cómo** | 14 agentes coordinados | Interfaz interactiva |
| **Para qué** | Guía universal para cualquier profesor | Adaptación a horas, L1, énfasis |
| **Cuándo** | Ahora | Después |

---

## DIAPOSITIVA 21 — RESUMEN DE AGENTES

**Título:** Los 14 agentes del sistema v5.0

| # | Agente | Fase | Tipo |
|---|--------|------|------|
| 0 | Ingesta | ANTES | Preparación |
| 1 | **Orquestador** | DURANTE | Coordinación |
| 2 | Vocabulario | DURANTE | Sección |
| 3 | Gramática | DURANTE | Sección |
| 4 | Comunicación | DURANTE | Sección |
| 5 | Destrezas | DURANTE | Sección |
| 6 | Cultura | DURANTE | Sección |
| 7 | Reflexión | DURANTE | Sección |
| 8 | Evaluación | DURANTE | Sección |
| 9 | **Píldoras** | DURANTE | Dedicado |
| 10 | Diversidad y errores L1 | DURANTE | Transversal |
| 11 | Solucionario | DURANTE | Transversal |
| 12 | Priorizador temporal | DESPUÉS | Post-producción |
| 13 | Revisor | DESPUÉS | Post-producción |

---

## DIAPOSITIVA 22 — DOCUMENTOS DEL PROYECTO

**Título:** Estructura de archivos

**Documentos de referencia (no se leen en tiempo de ejecución):**
- `marco-teorico-metodologico.md` — fundamentación teórica
- `00-curso-general.md` — datos del curso y orientaciones

**Instrucciones operativas (un archivo por agente):**
- `agentes/orquestador.md`
- `agentes/ag-vocabulario.md`
- `agentes/ag-gramatica.md`
- `agentes/ag-comunicacion.md` *(pendiente)*
- `agentes/ag-destrezas.md` *(pendiente)*
- `agentes/ag-cultura.md` *(pendiente)*
- `agentes/ag-reflexion.md` *(pendiente)*
- `agentes/ag-evaluacion.md` *(pendiente)*

**Repertorios de explotación (7 archivos):**
- `repertorios/vocabulario.md`
- `repertorios/gramatica.md`
- `repertorios/comunicacion.md` *(pendiente)*
- `repertorios/destrezas.md` *(pendiente)*
- `repertorios/cultura.md` *(pendiente)*
- `repertorios/reflexion.md` *(pendiente)*
- `repertorios/evaluacion.md` *(pendiente)*

**Datos por unidad:**
- `datos/UXX-inventario.json`

**Resultado por unidad:**
- `unidades/UXX-[nombre].md`

---

## DIAPOSITIVA 23 — ESTADO ACTUAL

**Título:** ¿Dónde estamos?

| Componente | Estado |
|------------|--------|
| Propuesta v5.0 completa | ✅ Terminado |
| Marco teórico | ✅ Existente (referencia) |
| Curso general | ✅ Existente (referencia) |
| Agente Orquestador | ✅ Instrucciones operativas |
| Agente Vocabulario | ✅ Instrucciones + repertorio + plantilla tarjeta (10 elementos) |
| Agente Gramática | ✅ Instrucciones + repertorio |
| Agentes Comunicación, Destrezas, Cultura, Reflexión, Evaluación | ⏳ Pendiente |
| Repertorios restantes (5) | ⏳ Pendiente |
| Agente Píldoras | ⏳ Pendiente |
| Inventario U03 | ✅ Completado |
| Piloto U03 Vocabulario | ✅ Completado (11 acts, 3 bloques, 14 fases, 20 tarjetas generadas, razonamiento) |
| Piloto U03 secciones restantes (Gramática → Evaluación) | ⏳ Pendiente |
| Unidades U01-U09 | ⏳ Pendiente |

---

## DIAPOSITIVA 24 — PRÓXIMOS PASOS

**Título:** Hoja de ruta

1. ~~Completar piloto U03 Vocabulario~~ ✅ — 11 actividades, 3 bloques, 14 fases, 20 tarjetas con plantilla de 10 elementos, documento de razonamiento completo
2. **Pilotar U03 Gramática** — validar el Agente Gramática con la sección de Gramática de U03 (p.36-37)
3. **Desarrollar agentes restantes** — Comunicación, Destrezas, Cultura, Reflexión, Evaluación (5 instrucciones operativas + 5 repertorios + 5 plantillas de tarjeta)
4. **Desarrollar Agente Píldoras** — instrucciones + formato + prueba multilingüe
5. **Pilotar U03 completa** — las 7 secciones con todos los agentes
6. **Producción U01-U09** — generar las 9 unidades completas
7. **Post-producción** — priorización temporal + revisión de calidad
8. **Compilación** — guía impresa final

---

## DIAPOSITIVA 25 — CIERRE

**Título:** En resumen

**El sistema v5.0:**
- **14 agentes** especializados y coordinados
- **7 agentes de sección** (1 por cada sección del libro)
- **Repertorios de explotación** con criterios de selección (no plantillas fijas)
- **Reducción 5x** de contexto por invocación (8K vs. 40K tokens)
- **Trazabilidad completa** de cada decisión
- **Fundamentación teórica** destilada en instrucciones operativas

**El producto final:**
- Guía impresa completa para 9 unidades
- Instrucciones paso a paso para cada actividad
- Notas lingüísticas integradas donde se necesitan
- Material reproducible multilingüe (píldoras)
- Gamificación con insignias por sección
- Andamiaje visible (Estaciones de servicio con tarjetas de 10 elementos)
- Tarjetas de vocabulario con regla morfológica, ejemplo, frecuencia, género, traducción 6 L1
- Propuesta de priorización temporal

---

*Documento preparado para presentación por Kimi.*
*Fuente: propuesta-v5-sistema-agentes.md — Sistema de Agentes v5.0*
