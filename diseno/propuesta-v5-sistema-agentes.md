# PROPUESTA v5.0: Rediseño del Sistema de Agentes
## Nuevo Compañeros 1 — SGEL — Nivel A1.1

---

## 1. PROBLEMA DETECTADO EN v4.0

### 1.1 Los documentos son demasiado largos para ser operativos

| Documento | Líneas | Tokens aprox. | Problema |
|-----------|--------|---------------|----------|
| `marco-teorico-metodologico.md` | ~1140 | ~20.000 | Mezcla criterios operativos, fundamentación teórica, evidencia empírica y referencias. El agente recibe todo cuando solo necesita una fracción |
| `00-curso-general.md` | ~780 | ~15.000 | Mezcla datos factuales (perfil, temporalización) con orientaciones metodológicas completas (comprensión lectora, tarjetas, diferenciación, cognición encarnada) |

### 1.2 El Agente 2 (Redactor) concentra demasiado trabajo

En v4.0, el Agente 2 genera:
- Explotación didáctica sección a sección (Vocabulario, Gramática, Comunicación, Destrezas, Cultura)
- Atención a la diversidad y errores por L1
- Evaluación (criterios e instrumentos)

Para ello necesita leer ~35-45K tokens de contexto antes de escribir una línea. Cada tipo de sección del libro requiere criterios distintos:

| Tipo de sección | Criterios que necesita |
|-----------------|----------------------|
| Vocabulario | Ciclo 5 fases (vocabulario), CLT, Sentence Builders, categorización semántica |
| Gramática | Ciclo 5 fases (gramática), inductivo/deductivo, weaning off, CLT |
| Comunicación | Gagné/Merrill, comprensión auditiva Pre-Durante-Post |
| Destrezas (lectura) | Comprensión lectora Pre-Durante-Post, tarjetas estrategia, recycling |
| Destrezas (escucha) | Comprensión auditiva Pre-Durante-Post, información transitoria |
| Cultura | Conexión conocimiento previo, cognición encarnada |

Un solo agente no puede manejar todo esto con calidad consistente.

### 1.3 Duplicación y contenido disperso

- El ciclo de 5 fases y la CLT tienen resúmenes en `00-curso-general.md` Y desarrollo completo en `marco-teorico-metodologico.md`
- La comprensión lectora/auditiva, tarjetas de estrategia, diferenciación por niveles y cognición encarnada existen SOLO en `00-curso-general.md` — sin fundamentación en el marco teórico
- Los agentes no saben qué buscar en cada documento

### 1.4 Desconexión entre documentos y agentes

El marco teórico no distingue cómo cada sección se usa en la práctica:

| Sección del marco | Modo de uso real |
|-------------------|-----------------|
| §1 Merrill | **Generativa**: las 6 acciones de enriquecimiento son instrucciones directas |
| §2 Gagné | **Verificativa**: checklist post-redacción |
| §3 Inductivo/Deductivo | **Condicional**: solo para gramática, según enfoque del libro |
| §4 Atención | **Restrictiva**: límites temporales |
| §5 CLT | **Restrictiva**: límites de carga |
| §6 Recursividad | **Generativa**: proceso de 4 pasos activo |
| §7 Multimedia | **Condicional**: solo si hay audio/vídeo/PPT |
| §8 Ciclo 5 fases | **Protocolo**: secuencia completa para vocabulario/gramática |

Pero el documento presenta todo como un bloque homogéneo de ~1140 líneas.

---

## 2. PRINCIPIOS DEL REDISEÑO

### 2.1 Los documentos no se "leen" — se integran en los agentes

El contenido de `marco-teorico-metodologico.md` y `00-curso-general.md` no debería ser archivos que los agentes leen en runtime. Su contenido debe estar **destilado e integrado directamente en las instrucciones de cada agente**, incluyendo solo lo relevante para su tarea.

### 2.2 La guía impresa se organiza por secciones, no por lecciones

La guía del profesor se estructura por **unidad → secciones del libro** (Vocabulario, Gramática, Comunicación, Destrezas, Cultura, Reflexión, Evaluación). No se divide en "lección 1, lección 2...". El profesor lee la explotación sección por sección.

**Todas las actividades se explotan.** La guía contiene instrucciones para cada actividad del libro, sin excepción.

### 2.3 Dos productos, dos momentos

| Producto | Qué contiene | Cuándo se genera |
|----------|-------------|-----------------|
| **Guía impresa (Fase 1)** | Explotación completa de todas las actividades (con notas lingüísticas integradas) + diversidad + evaluación + solucionario + propuesta de priorización temporal | Ahora |
| **Herramienta adaptativa (Fase 2)** | El profesor personaliza: distribución en lecciones según sus horas, adaptación a L1 específica, énfasis en destrezas concretas | Después |

### 2.4 La priorización temporal va DESPUÉS de la explotación

La distribución en lecciones de 45 min no va en la guía impresa. Lo que sí va es una **propuesta de priorización temporal**: un agente que, una vez completada toda la explotación, analiza el conjunto y genera una recomendación:

- **Con 2h/semana (~60h anuales):** qué actividades son imprescindibles en clase y cuáles puede hacer el alumno autónomamente
- **Con 3+ horas/semana:** se usan todas las actividades en clase

Este agente necesita **criterios explícitos** para tomar esas decisiones (ver sección 4).

### 2.5 Repertorios de explotación, no plantillas fijas

La explotación de una actividad no es mecánica ni siempre igual. Cada tipo de actividad tiene **múltiples opciones de explotación** (un repertorio), y el agente selecciona la más adecuada según variables contextuales. Esto garantiza:

- **Variedad**: dos actividades de comprensión lectora en la misma unidad no se explotan igual
- **Adecuación**: la explotación responde al contenido concreto, no a una receta genérica
- **Calidad**: el agente toma decisiones informadas, no aplica una plantilla

### 2.6 Contexto mínimo por invocación

Ningún agente recibe todo el marco teórico ni todo el curso general. Cada agente recibe **solo** lo que necesita para su tarea concreta en ese momento. El orquestador se encarga de filtrar y distribuir el contexto.

---

## 3. ARQUITECTURA: AGENTES DE SECCIÓN CON REPERTORIOS

### 3.1 Problema del agente único vs. problema de muchos agentes

| Diseño | Problema |
|--------|----------|
| **1 agente para todo** (v4.0) | Sobrecarga cognitiva: ~35-45K tokens, decisiones inconsistentes |
| **1 agente por destreza** (~20 agentes) | Coordinación exponencial, sobre-ingeniería |
| **1 agente por sección del libro** (v5.0) | Equilibrio: cada uno especializado en su sección, repertorio acotado, coordinación manejable. 7 secciones = 7 agentes |

### 3.2 Agentes de sección

Cada sección del libro tiene un agente especializado. El libro tiene las mismas secciones en todas las unidades, por lo que cada agente desarrolla expertise en su tipo de contenido.

| Agente de sección | Sección que explota | Repertorios que maneja |
|--------------------|---------------------|------------------------|
| **Vocabulario** | Vocabulario | Ciclo 5 fases (variantes de vocabulario), Sentence Builders, categorización semántica, flashcards, traducción reflexiva |
| **Gramática** | Gramática | Ciclo 5 fases (variantes de gramática), inductivo/deductivo, weaning off, cuadros gramaticales, conjugación verbal |
| **Comunicación** | Comunicación | Diálogos, producción oral, comprensión auditiva (Pre-Durante-Post) |
| **Destrezas** | Destrezas | Comprensión lectora (Pre-Durante-Post), comprensión auditiva, producción escrita, tarjetas de estrategia |
| **Cultura** | Cultura | Conexión intercultural, cognición encarnada, debate, proyectos |
| **Reflexión** | Reflexión | Autoevaluación, repaso integrador, portfolio |
| **Evaluación** | Evaluación | Evaluación sumativa, criterios MCER, rúbricas, evaluación entre pares |

**7 agentes de sección** (1 agente = 1 sección del libro) en lugar de 1 (v4.0) o 20 (propuesta intermedia descartada).

### 3.3 Qué es un repertorio de explotación

Un repertorio es un **conjunto de opciones de explotación para un tipo de actividad**, junto con **criterios de selección** que determinan cuál es la más adecuada según el contexto.

**Ejemplo: Repertorio de comprensión lectora (Agente Destrezas)**

| Opción | Cuándo aplicarla | Descripción |
|--------|------------------|-------------|
| **Pre-Durante-Post estándar** | Texto informativo, primera lectura de la unidad | Activación → lectura global → lectura detallada → extracción lingüística |
| **Lectura guiada con tarjetas** | Texto largo o complejo para el nivel | Semáforo de lectura + Salto de la Rana; fragmentar en párrafos |
| **Text mining** | Texto rico en estructuras gramaticales que se están trabajando | Form Focus intensivo después de comprensión; extraer patrones |
| **Lectura + producción** | Texto modelo para escritura posterior | Comprensión → análisis de estructura → producción paralela |
| **Lectura cooperativa** | Texto con múltiples personajes/perspectivas | Jigsaw: cada grupo lee una parte y luego comparten |

**Criterios de selección:**

| Variable contextual | Cómo afecta la selección |
|---------------------|--------------------------|
| Longitud del texto | Textos largos → lectura guiada con tarjetas; textos cortos → estándar |
| Contenido lingüístico nuevo | Mucho contenido nuevo → text mining; poco → lectura + producción |
| Posición en la unidad | Primera aparición → estándar con más pre-lectura; final de unidad → cooperativa |
| Recursos disponibles | Con audio → integrar escucha; solo texto → más trabajo visual |
| Contenido reciclable | Conexión fuerte con unidades anteriores → incluir running dictation o communal memory |
| Actividades adyacentes | Si la siguiente actividad es producción escrita → lectura + producción como modelo |

### 3.4 Cómo se evita la sobrecarga del agente de sección

**El agente no recibe todo el repertorio a la vez.** El mecanismo es:

1. **El inventario ya viene estructurado por sección y con metadatos por actividad.** Cada actividad en el JSON ya tiene:
   - `seccion`: a qué sección del libro pertenece (Vocabulario, Gramática, Comunicación, etc.)
   - `tipo`: tipo de actividad (escucha y repite, completa huecos, práctica oral en parejas, etc.)
   - `destreza`: comprensión lectora, auditiva, producción oral, escrita, interacción, mediación
   - `tiene_audio`, `tiene_imagen`, `tiene_video`: recursos disponibles
   - `contenido_linguistico`: qué se trabaja
   - El orquestador no agrupa ni clasifica nada — lee directamente lo que el inventario ya organiza.

2. **El orquestador pre-filtra el repertorio** según los tipos de actividad presentes en cada sección. Ejemplo: si la sección de Gramática tiene actividades de tipo "señala la forma correcta", "ordena frases", "completa huecos" y "escribe preguntas", el orquestador selecciona del repertorio solo las opciones de explotación relevantes para esos tipos.

3. **El agente de sección recibe un contexto acotado:**

| Componente del prompt | Tokens aprox. |
|-----------------------|---------------|
| Instrucciones generales (principios destilados, restricciones) | ~2.000 |
| Repertorio filtrado para los tipos de actividad de esa sección | ~2.000-3.000 |
| Criterios de selección aplicables | ~500 |
| Actividades concretas a explotar (del inventario) | ~1.000-2.000 |
| Contexto lingüístico relevante (progresiones gramatical/léxica/fonética, conexiones con unidades previas) | ~1.000 |
| Contenidos anteriores para reciclaje (resumen) | ~500-1.000 |
| **Total por invocación** | **~7.000-9.500** |

**Comparación:** ~8K tokens (v5.0) vs. ~40K tokens (v4.0) = **reducción de ~5x**.

### 3.5 Principios integrados en cada agente de sección

Cada agente tiene destilados en su prompt SOLO los principios del marco teórico relevantes a su sección:

| Agente | Principios integrados (destilados de marco-teorico + curso-general) |
|--------|---------------------------------------------------------------------|
| **Vocabulario** | Ciclo 5 fases (fases de vocabulario: input visual saturado, categorización semántica, flashcards, traducción reflexiva) (§8), CLT aplicada (§5.3-5.6), Sentence Builders (§8.13), reciclaje dinámico (§6) |
| **Gramática** | Ciclo 5 fases (fases de gramática: awareness, pares mínimos, cuadros gramaticales) (§8), inductivo/deductivo (§3), CLT aplicada (§5.3-5.6), weaning off (§8.11), reciclaje dinámico (§6) |
| **Comunicación** | Merrill: acciones de enriquecimiento (§1), Gagné: checklist (§2), comprensión auditiva Pre-Durante-Post (curso-general), tarjetas de producción oral (curso-general), CLT: información transitoria (§5.5) |
| **Destrezas** | Comprensión lectora Pre-Durante-Post (curso-general), comprensión auditiva Pre-Durante-Post (curso-general), tarjetas de estrategia del alumno (curso-general), CLT: segmentación y modalidad (§5.5), recycling techniques (curso-general) |
| **Cultura** | Cognición encarnada (curso-general), conexión intercultural, Merrill: integración (§1), actividades de creación de objetos (curso-general) |
| **Reflexión** | Gagné: evaluación formativa y transferencia (§2), autoevaluación, portfolio, metacognición |
| **Evaluación** | Gagné: evaluación sumativa (§2), criterios MCER A1.1, rúbricas, evaluación entre pares |

**Todos los agentes** comparten (integrado en su prompt):
- Restricciones de atención: 10-15 min por actividad (§4)
- CLT: regla de oro (§5.3) — todo lo añadido debe reducir carga, no aumentarla
- Ritmicidad atencional: alternancia foco/difuso (curso-general)
- Agrupamientos por fase (curso-general)
- Gamificación: integrada como criterio transversal

### 3.6 Notas lingüísticas integradas en la explotación

Las notas lingüísticas **no** constituyen una sección separada al inicio de la unidad. En su lugar, cada agente de sección genera notas lingüísticas **dentro** de la explotación, exactamente donde son relevantes para el profesor.

**Principio:** El profesor no debería tener que ir a buscar información lingüística a otra parte de la guía. Cuando está leyendo la explotación de una actividad de gramática y necesita saber por qué *tener* es irregular, la nota está ahí mismo.

**Formato visual diferenciado:** Las notas lingüísticas se presentan con un formato distinto al de las instrucciones de explotación, para que el profesor las distinga de un vistazo:

```
┌─ NOTA LINGÜÍSTICA ──────────────────────────────────────┐
│ El verbo *tener* presenta irregularidad vocálica         │
│ (e→ie) en todas las personas excepto nosotros/vosotros. │
│ Es el primer verbo irregular que ven los alumnos.        │
│ Conexión U04: *querer* sigue el mismo patrón.           │
└──────────────────────────────────────────────────────────┘
```

**Tipos de notas que genera cada agente:**

| Agente | Notas lingüísticas que integra |
|--------|-------------------------------|
| **Vocabulario** | Vocabulario nuclear (frecuencia, cognados, falsos amigos), campos semánticos, género de sustantivos, plurales mixtos, conexiones léxicas con unidades anteriores y posteriores |
| **Gramática** | Ampliación gramatical para el profesor (paradigmas completos, irregularidades, contraste L1), conexiones gramaticales con unidades anteriores y posteriores |
| **Comunicación** | Funciones comunicativas y exponentes lingüísticos alternativos, registro formal/informal, pragmática |
| **Destrezas** | Vocabulario pasivo del texto (que el alumno no necesita producir), estructuras clave para la comprensión, estrategias de deducción por contexto |
| **Cultura** | Léxico cultural específico, referentes culturales que el profesor debe conocer |
| **Reflexión** | Metacognición, estrategias de aprendizaje, conexiones transversales de la unidad |
| **Evaluación** | Criterios lingüísticos de evaluación, descriptores MCER relevantes |

**Contexto que recibe cada agente para generar las notas:** El orquestador incluye en el contexto de cada agente de sección las progresiones gramatical, léxica y fonética, más los contenidos de las unidades adyacentes, para que el agente pueda establecer conexiones.

### 3.7 Estación de servicio: andamiaje con tarjetas por sección

Cada sección de la explotación didáctica comienza con una **Estación de servicio**: un conjunto de tarjetas imprimibles organizadas en cajas temáticas que el alumno puede consultar libremente durante las actividades.

**Principio:** La Estación de servicio es el andamiaje visible y tangible de la clase. En lugar de que el alumno pregunte al profesor cada duda, tiene a su disposición cajas de tarjetas organizadas por categoría donde puede buscar lo que necesita. Esto fomenta la autonomía y reduce la dependencia del profesor.

**Características:**

1. **Tarjetas imprimibles** — el profesor las imprime y las coloca en la mesa/rincón antes de empezar la sección
2. **Organizadas en cajas con nombre descriptivo** — el nombre de cada caja le dice al alumno qué va a encontrar (ej: "Producción" = estructuras para ayudarle a hablar/escribir)
3. **Las categorías dependen de la sección** — cada sección tiene cajas diferentes según lo que se trabaja
4. **Mezclan contenido ya trabajado + contenido nuevo** — las tarjetas incluyen tanto lo que el alumno ya sabe (reciclaje) como lo que va a necesitar en esta sección
5. **Acumulativas** — las cajas crecen unidad a unidad. La caja de Vocabulario de U05 contiene también tarjetas de U01-U04. El alumno va construyendo su banco de recursos
6. **El agente de sección genera el contenido completo de cada tarjeta** — no solo lista las cajas, sino que desarrolla el contenido de cada una

**Estructura de la Estación de servicio:**

```
┌─ ESTACIÓN DE SERVICIO ──────────────────────────────────────────────┐
│                                                                      │
│  Caja 1 [Nombre descriptivo]: descripción del contenido de las      │
│  tarjetas (ej: flashcards, listas, paradigmas...)                   │
│                                                                      │
│  Caja 2 [Nombre descriptivo]: descripción del contenido             │
│                                                                      │
│  Caja 3 [Nombre descriptivo]: descripción del contenido             │
│                                                                      │
│  Caja 4 Pistas de hoy: ayudas específicas para actividades          │
│  concretas de esta sección (ej: "Act. 3: ejemplo resuelto")         │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

**Cajas típicas por agente de sección:**

| Agente | Cajas posibles | Contenido de las tarjetas |
|--------|---------------|--------------------------|
| **Vocabulario** | Vocabulario (tarjetas con template estándar — ver abajo), Pistas de hoy | Tarjetas de vocabulario generadas con el template de 10 elementos (una tarjeta por palabra). Pistas de hoy: ayudas específicas de la sección |
| **Gramática** | Gramática (paradigmas, reglas, ejemplos), Producción gramatical (conectores, estructuras con foco en forma), Pistas de hoy | Gramática: conjugaciones, concordancia, reglas resumidas. Producción gramatical: conectores (*y, pero, porque, también*), estructuras clave ("Tiene... Es... Lleva...") |
| **Comunicación** | Funciones (exponentes lingüísticos por función comunicativa), Estrategias (tarjetas Comodín, Tiempo Extra, Repetición), Producción (modelos de diálogo, estructuras de turno), Pistas de hoy | Funciones: tarjetas con exponentes para presentarse, pedir, describir, etc. Estrategias: tarjetas con frases de supervivencia ("¿Puedes repetir?", "¿Cómo se dice...?") |
| **Destrezas** | Lectura (vocabulario clave del texto, estrategias de deducción), Escritura (plantilla de texto, conectores, modelo), Estrategias (tarjetas Semáforo, Salto de Rana), Pistas de hoy | Lectura: vocabulario pasivo necesario, preguntas guía. Escritura: estructura del texto modelo, frases útiles, checklist de revisión |
| **Cultura** | Vocabulario cultural (léxico específico del tema), Conexiones (preguntas para comparar con la cultura del alumno), Pistas de hoy | Vocabulario cultural: palabras clave del tema con explicación visual. Conexiones: tarjetas con preguntas comparativas |
| **Reflexión** | Repaso (tarjetas de contenidos clave de la unidad), Autoevaluación (descriptores "puedo..."), Pistas de hoy | Repaso: resumen visual de gramática + vocabulario + funciones de la unidad. Autoevaluación: descriptores MCER adaptados |
| **Evaluación** | Criterios (rúbricas simplificadas), Modelos (ejemplos de respuestas correctas), Pistas de hoy | Criterios: descriptores MCER A1.1 adaptados. Modelos: ejemplos resueltos para autoevaluación |

**IMPORTANTE: Cada agente de sección tiene su propio template de tarjeta.** El template define el formato estándar que todas las tarjetas de ese tipo deben seguir en todo el curso. Los templates de Gramática, Comunicación, Destrezas, Cultura, Reflexión y Evaluación se definirán cuando se desarrollen sus respectivos agentes. A continuación se define el template de Vocabulario, que es el primero en estar operativo.

#### Template de tarjeta de vocabulario (exclusivo del Agente Vocabulario)

Este template aplica a **todas las tarjetas de vocabulario del curso**, independientemente de la unidad o campo semántico. El agente de Vocabulario genera una tarjeta por palabra siguiendo este formato.

**CARA A — Consulta rápida (lo que el alumno ve al coger la tarjeta):**

| Zona | Elemento | Descripción |
|------|----------|-------------|
| Esquina superior izquierda | **Nº de unidad** | U01, U02, U03... Permite filtrar tarjetas por unidad cuando se acumulan |
| Esquina superior derecha | **Icono + color del campo semántico** | Un icono identificativo + color de fondo fijo por campo. Ej: familia = violeta, alimentación = verde, objetos de clase = azul. Un solo color por campo semántico. Identifica a qué campo pertenece la palabra al primer vistazo |
| Centro (texto grande) | **Palabra en español** con sílaba tónica en negrita | La palabra principal. La sílaba tónica se marca en negrita para ayudar con la pronunciación: a-**bue**-lo, her-**ma**-no, lá-**piz** |
| Color del texto central | **Color por género gramatical** | Azul = masculino, rojo = femenino. El alumno asocia género = color. Si la palabra no tiene género variable, se usa negro |
| Debajo de la palabra | **Regla morfológica** | La regla de formación que sigue la palabra. Para regulares: "M termina en **-o**, F termina en **-a**: abuel**o** / abuel**a**". Para irregulares: "Irregular: raíces distintas (padre/madre). Memorizar como par." El alumno siempre tiene la referencia de POR QUÉ la palabra tiene esa forma, no solo la excepción |
| Debajo del centro | **Ejemplo contextualizado** | Una frase corta de uso real con la palabra: *"Mi abuelo se llama Carlos."* No es un Sentence Builder — es un único ejemplo que muestra cómo se usa la palabra en contexto |
| Junto a la palabra | **Marca de frecuencia** | ★ (baja), ★★ (media), ★★★ (alta). Indica la prioridad de aprendizaje. El alumno sabe cuáles son las más importantes |
| Pie de tarjeta | **💬 Señal de irregularidad** (solo si aplica) | Un bocadillo de chat pequeño (💬) con descripción breve de la irregularidad. Ej: 💬 *"No sigue -o/-a: padre/madre son raíces distintas."* Solo aparece cuando la palabra tiene algo que no sigue el patrón esperado (género irregular, plural irregular, falso amigo, doble significado). Si la palabra es regular, no hay bocadillo |
| Zona inferior | **Espacio en blanco para nota personal** | Recuadro vacío donde el alumno escribe lo que quiera: dibujo, asociación, nota en su L1, mnemotécnico. La tarjeta no viene completa — tiene un espacio que el alumno personaliza |

**CARA B — Traducción multilingüe:**

| Zona | Elemento | Descripción |
|------|----------|-------------|
| Centro | **Traducciones en las 6 L1 del aula** | IT · FR · PT-BR · EN · CS · PL. Cada alumno busca su idioma. Resuelve el aula multilingüe sin intervención del profesor |

**Output obligatorio del Agente Vocabulario:** Además del template, el agente genera:
1. Una **tabla de tarjetas completa** (markdown) con una fila por palabra y todos los campos resueltos, dentro de la Estación de servicio de la explotación de cada unidad.
2. Un **CSV para InDesign** (delimitado por punto y coma, UTF-8) con los mismos datos, listo para importar en InDesign mediante combinación de datos (data merge). El CSV va al final de la Estación de servicio, después de la tabla markdown. Esto permite automatizar la producción de las tarjetas impresas sin reintroducir datos manualmente.

**Carácter acumulativo — responsabilidad del orquestador:**

El orquestador proporciona a cada agente de sección los contenidos de las unidades anteriores para que las cajas permanentes (Vocabulario, Gramática, Producción, Funciones, Estrategias) incluyan tanto el contenido nuevo como el ya trabajado. La caja "Pistas de hoy" es la única que es específica de cada sección y no se acumula.

**Lo que el agente genera para cada caja:**
- Nombre descriptivo de la caja
- Lista completa de tarjetas con su contenido desarrollado (para Vocabulario: tabla con todos los campos del template)
- Indicación de qué tarjetas son nuevas (esta unidad) y cuáles son de repaso (unidades anteriores)

### 3.8 Insignias: micro-credenciales por sección

Cada sección tiene **una insignia única** que el alumno obtiene al completarla. La insignia representa una competencia o habilidad concreta que el alumno demuestra.

**Principio:** La insignia funciona como meta visible de la sección. El alumno sabe desde el principio qué va a conseguir y qué tiene que hacer para conseguirlo. Esto da dirección y propósito a todas las actividades de la sección.

**Características:**

1. **Una por sección** — no por actividad, no por unidad
2. **Nombre temático vinculado al contenido** — el nombre conecta con lo que se trabaja en esa sección concreta (ej: "Descriptor de Surfistas" para una sección donde se aprende a describir personas)
3. **Vinculada a una competencia o habilidad demostrable** — "sé conjugar verbos regulares", "sé presentar a mi familia", "sé leer un horario de TV"
4. **Criterio doble para obtenerla**: completar las actividades de la sección + una tarea final que demuestra la competencia
5. **Únicas en todo el curso** — no se repiten entre secciones ni entre unidades
6. **Compartibles en redes sociales** — tienen un componente visual/digital que el alumno puede publicar
7. **Imprimibles** — hay una versión física que se entrega en clase
8. **Tono motivador, no competitivo** — "Motive, invite y no genere competición"

**Presentación al inicio de la sección:**

La insignia se presenta al alumno al comienzo de la sección, junto con el objetivo y lo que debe hacer para conseguirla:

```
┌─ GAMIFICACIÓN ───────────────────────────────────────────┐
│                                                           │
│  Objetivo — [Competencia/habilidad de la sección]        │
│                                                           │
│  Insignia: [Nombre temático]                             │
│  Para obtenerla: completar las X actividades y además    │
│  [tarea final que demuestra la competencia].             │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

**Lo que el agente de sección genera:**
- Nombre temático de la insignia (único, vinculado al contenido de esa sección en esa unidad)
- Competencia o habilidad que certifica (formulada como "sé + infinitivo")
- Criterio de obtención (actividades a completar + tarea final demostrativa)
- Descripción breve para compartir en redes sociales

**El orquestador verifica** que no haya insignias repetidas en toda la unidad ni en unidades anteriores.

### 3.9 Instrucciones de preparación del profesor

Cada bloque de actividades incluye **instrucciones de preparación** que le indican al profesor qué debe tener listo antes de la clase. Estas instrucciones van siempre debajo del objetivo del bloque.

**Contenido típico:**
- Materiales a imprimir (tarjetas de la Estación de servicio, insignia, píldoras, fichas)
- Recursos a preparar (audios, proyecciones, recortes)
- Recursos opcionales disponibles (juegos en plataformas digitales, materiales extra)
- Disposición del aula si es necesaria (mesas en grupos, espacio para moverse)

```
┌─ PREPARACIÓN ────────────────────────────────────────────┐
│  → Imprimir: Píldora gramatical 8.1, Insignia [nombre]  │
│  → Descargar: presentación píldora gramatical 8.1        │
│  → Opcional: juego de memory (Blinklearning/Unidad X)    │
└───────────────────────────────────────────────────────────┘
```

### 3.10 Estructura de la secuenciación didáctica

La secuenciación didáctica es el cuerpo de la explotación. **No se organiza actividad por actividad**, sino por **bloques de actividades agrupadas por lógica didáctica**.

**Principio:** Si varias actividades consecutivas persiguen el mismo objetivo o trabajan la misma función, se agrupan en un solo bloque con un único objetivo. No tiene sentido hacer un objetivo para cada actividad cuando comparten propósito. El agente de sección decide cómo agrupar según la lógica del contenido.

**Estructura de un bloque:**

```
┌─ ACTIVIDADES X-Y ────────────────────────────────────────┐
│                                                           │
│  Objetivo — [Qué se logra con este bloque]               │
│                                                           │
│  PREPARACIÓN                                              │
│  → Imprimir: ...                                         │
│  → Preparar: ...                                         │
│                                                           │
│  [Fase 1: título descriptivo en negrita]                 │
│  Instrucciones paso a paso...                            │
│                                                           │
│  [Fase 2: título descriptivo en negrita]                 │
│  Instrucciones paso a paso...                            │
│                                                           │
│  [Fase N: título descriptivo en negrita]                 │
│  Instrucciones paso a paso...                            │
│  → Puntos de insignia ganados en este bloque             │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

**Características clave:**

1. **Agrupación por lógica, no mecánica** — el agente agrupa actividades que comparten objetivo o función. Una actividad puede ser un bloque solo si tiene un objetivo propio diferenciado. El criterio es la lógica didáctica, no el número de actividad.

2. **Un objetivo por bloque** — formulado como competencia. No como descripción de la actividad ("Completar huecos") sino como logro ("Activar conocimiento conceptual y experiencial relacionado con actividades físicas y conocer las partes del cuerpo").

3. **Fases con título descriptivo** — dentro de cada bloque, la explotación se organiza en fases con título en negrita que describe la acción del profesor/alumno. No "Paso 1, Paso 2" sino títulos significativos:
   - "Parta desde la experiencia de los estudiantes"
   - "Presente el vocabulario desarrollando la escucha activa"
   - "Fortalezca la conciencia gramatical"

4. **Instrucciones detalladas por fase** — cada fase contiene instrucciones paso a paso para el profesor: qué decir, qué hacer, cómo gestionar la clase, qué esperar del alumno.

5. **Puntos de insignia al final del bloque** — al completar el bloque, el alumno gana puntos hacia la insignia de la sección. El profesor lo comunica explícitamente.

6. **Píldoras y fichas referenciadas donde corresponden** — cuando la explotación requiere que el alumno use una píldora gramatical, ficha o material complementario, se referencia en el momento exacto de la fase correspondiente (las píldoras se definirán en detalle posteriormente).

**Responsabilidad del agente de sección:**
- Analizar las actividades del inventario y decidir cómo agruparlas en bloques
- Formular el objetivo de cada bloque
- Diseñar las fases con títulos descriptivos
- Redactar las instrucciones detalladas de cada fase
- Distribuir los puntos de insignia entre los bloques
- Indicar las instrucciones de preparación de cada bloque

### 3.11 Píldoras: material complementario pautado para el alumno

Las píldoras son materiales para el alumno que guían la comprensión de un contenido nuevo. Hay **4-5 por unidad** (no por sección), y se deciden al inicio de la unidad antes de que los agentes de sección trabajen. Las genera un **agente dedicado** (Agente de Píldoras), no los agentes de sección.

**Doble objetivo:**
1. Que el alumno comprenda de forma **pautada** un contenido gramatical, de vocabulario o de mediación, combinando descubrimiento inferencial con regla explícita
2. Favorecer la **toma de notas** por parte del alumno — premisa "NOTAS y ANOTA": el alumno escribe, completa, decide

**Doble output — un agente, dos productos coherentes:**

Cada píldora tiene dos versiones generadas por el mismo agente, garantizando coherencia total entre ambas:

| Producto | Formato | Para qué | Contenido |
|----------|---------|----------|-----------|
| **Presentación interactiva** | Proyectable / digital | El profesor la usa en clase para guiar la explicación del contenido | Secuencia de descubrimiento guiado, presentación de la regla, verificación. Diseñada para proyectar paso a paso |
| **Hoja del estudiante** | Imprimible (PDF) | El alumno la recibe para trabajar durante y después de la presentación | Misma secuencia que la presentación, pero en formato de ficha con espacios para completar, escribir y anotar |

**Coherencia obligatoria:** La presentación interactiva y la hoja del estudiante siguen la misma secuencia, usan los mismos ejemplos, y cubren el mismo contenido. La hoja del estudiante es la versión "para escribir" de lo que el profesor presenta en pantalla. El alumno puede seguir la presentación con su hoja delante.

**Estructura interna de una píldora (siempre la misma en ambos formatos):**

```
┌─ PÍLDORA [tipo] [número] ────────────────────────────────┐
│                                                           │
│  1. DESCUBRIMIENTO GUIADO                                │
│     Preguntas inferenciales en la L1 del alumno que le   │
│     llevan a observar patrones y formular hipótesis       │
│     (completa, relaciona, V/F, elige la opción correcta) │
│                                                           │
│  2. REGLA EXPLÍCITA                                      │
│     Presentación clara de la regla/contenido              │
│     (paradigma, definición, esquema visual)               │
│                                                           │
│  3. COMPRENSIÓN DE LA REGLA                              │
│     Preguntas de verificación sobre la regla presentada:  │
│     afirmaciones para verificar, información a completar, │
│     V/F sobre la regla — para confirmar que el alumno     │
│     la ha entendido                                       │
│                                                           │
│  4. ESPACIO PARA NOTAS                                   │
│     El alumno anota en su lengua lo que ha aprendido      │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

**Multilingüe — cada píldora se genera en múltiples L1:**

Las instrucciones, preguntas inferenciales y explicaciones de cada píldora se formulan en la lengua materna del alumno. Los ejemplos y la regla explícita están en español. Cada píldora se genera en las siguientes lenguas:

| Lengua | Código |
|--------|--------|
| Italiano | IT |
| Francés | FR |
| Portugués (Brasil) | PT-BR |
| Inglés | EN |
| Checo | CS |
| Polaco | PL |

(Lista ampliable según necesidad editorial)

El agente genera **una versión por lengua** de cada píldora (tanto presentación como hoja). El contenido lingüístico en español es idéntico en todas las versiones; lo que cambia son las instrucciones, preguntas y explicaciones en L1.

**Características:**
1. **Estructura fija** — todas las píldoras siguen la misma secuencia: descubrimiento → regla → comprensión → notas
2. **Actividades cerradas y específicas** — completa, relaciona, V/F, elige la correcta. No abiertas ni de producción libre
3. **En la lengua materna del alumno** — las preguntas y explicaciones están en L1 para garantizar comprensión
4. **4-5 por unidad** — se asignan a los contenidos nuevos más relevantes de la unidad, distribuidas entre las secciones que lo necesiten
5. **Presentes en todas las secciones** — no solo en gramática. Pueden cubrir vocabulario, funciones comunicativas, mediación
6. **Doble formato** — presentación interactiva (para el profesor) + hoja imprimible (para el alumno), coherentes entre sí
7. **Multilingüe** — cada píldora existe en todas las L1 definidas
8. **Modificable y enriquecible** — el agente puede adaptar la cantidad y tipo de actividades según el contenido, siempre respetando la secuencia base

**Tipos de píldora:**
- **Píldora gramatical** — para contenidos gramaticales nuevos (ej: presente regular, verbo *tener*, posesivos)
- **Píldora de vocabulario** — para campos léxicos nuevos que requieren organización (ej: familia, alimentos)
- **Píldora de mediación/funciones** — para funciones comunicativas o estrategias nuevas

**Cuándo se genera una píldora:**
- Cuando se **presenta contenido nuevo** que requiere comprensión pautada
- Cuando el contenido implica un proceso de comprensión de reglas, patrones o categorías
- El criterio: ¿el alumno necesita entender algo antes de poder usarlo? → píldora

**Quién decide qué contenidos tienen píldora:**

Las píldoras se definen **antes** de que los agentes de sección trabajen. El editor (o el orquestador en su defecto) decide al inicio de cada unidad:
- Qué contenidos nuevos merecen píldora (4-5 máximo)
- De qué tipo es cada una
- A qué sección pertenece cada píldora

Los agentes de sección reciben la lista de píldoras asignadas a su sección y las **referencian** en el momento exacto de la explotación donde deben usarse. Pero **no generan el contenido** de la píldora — eso lo hace el Agente de Píldoras.

**Lo que genera el Agente de Píldoras para cada píldora:**
- Título y numeración (ej: "Píldora gramatical 3.1 — El presente regular")
- **Presentación interactiva**: contenido completo de las 4 secciones, diseñado para proyectar paso a paso
- **Hoja del estudiante**: misma secuencia en formato ficha imprimible con espacios para completar y anotar
- Ambos productos en cada una de las L1 definidas
- Indicación de en qué bloque de la explotación se usa

**Input que recibe el Agente de Píldoras:**
- Lista de píldoras decididas por el editor (contenido, tipo, sección)
- Contexto lingüístico relevante (progresiones, contenidos previos)
- Inventario de la sección correspondiente (para coherencia con las actividades del libro)

---

## 4. ORQUESTADOR

### 4.1 Función

El orquestador es el agente central que:
- **Pre-producción:** Prepara el contexto para cada agente de sección
- **Post-producción:** Verifica la calidad y coherencia del conjunto

No genera explotación directamente. Coordina.

### 4.2 Flujo de trabajo del orquestador

```
FASE PRE-PRODUCCIÓN (antes de invocar agentes de sección)
──────────────────────────────────────────────────────────
1. Recibe el inventario completo de la unidad (del Ag. Ingesta)
   → El inventario YA viene organizado por sección del libro
     (cada entrada de paginas_detalle tiene campo "seccion")
   → Cada actividad YA tiene metadatos: tipo, destreza, tiene_audio,
     tiene_imagen, contenido_linguistico
   → NO hay paso de "agrupar" ni "clasificar" — ya está hecho
1b. Recibe la lista de píldoras definidas por el editor (ver §3.11):
   → 4-5 píldoras por unidad, cada una asignada a una sección
   → Tipo de píldora (gramatical, vocabulario, mediación/funciones)
   → Contenido que cubre cada píldora
2. Para cada sección del inventario:
   a. Selecciona del repertorio las opciones de explotación relevantes
      según los tipos de actividad que ya están definidos en el inventario
   b. Prepara el resumen de contenidos anteriores para reciclaje
   c. Prepara el contexto lingüístico relevante (progresiones
      gramatical/léxica/fonética, conexiones con unidades adyacentes)
   d. Invoca al agente de sección correspondiente con:
      · Las actividades de esa sección (tal como están en el inventario)
      · El repertorio filtrado por los tipos de actividad presentes
      · El contexto lingüístico para generar notas integradas (ver §3.6)
      · Los contenidos anteriores para reciclaje
      · La lista de píldoras asignadas a esa sección (solo referencia,
        para que las incluya en la explotación donde corresponde)
3. Invoca al Agente de Píldoras (en paralelo con los agentes de sección):
   → Le pasa la lista completa de píldoras decididas por el editor
   → Contexto lingüístico relevante para cada píldora
   → Inventario de las secciones correspondientes
   → Lista de L1 en las que generar cada píldora

FASE POST-PRODUCCIÓN (después de recibir todas las explotaciones)
─────────────────────────────────────────────────────────────────
4. Verifica coherencia del conjunto:
   a. ¿Las horas totales son compatibles con la temporalización? (7h/unidad)
   b. ¿Hay variedad en las opciones de explotación elegidas?
      (no todas las lecturas se explotan igual, no todos los ejercicios igual)
   c. ¿El reciclaje cumple la regla 70/30?
   d. ¿La gamificación está distribuida de forma equilibrada?
   e. ¿Las insignias son únicas (no repetidas en la unidad ni en anteriores)?
   f. ¿Hay alternancia de agrupamientos (individual, parejas, grupos)?
   g. ¿Se respeta la ritmicidad atencional (foco/difuso)?
5. Si detecta problemas:
   a. Señala la sección y el criterio incumplido
   b. Re-invoca al agente de sección con instrucción de ajuste
6. Output: explotación completa de la unidad, lista para compilar
```

### 4.3 Criterios de verificación del orquestador

| Criterio | Umbral | Acción si no se cumple |
|----------|--------|------------------------|
| **Horas totales** | ≤7h de contenido por unidad (6-7 lecciones de contenido) | Pedir al agente que reduzca enriquecimiento en secciones menos críticas |
| **Variedad de explotación** | No repetir la misma opción de repertorio en >2 actividades consecutivas del mismo tipo | Sugerir opción alternativa al agente |
| **Reciclaje** | Al menos 30% de las activaciones/personalizaciones conectan con unidades anteriores | Indicar al agente puntos concretos de reciclaje |
| **Gamificación** | Al menos 1-2 elementos lúdicos por sección | Sugerir actividad del banco si falta |
| **Agrupamientos** | Al menos 3 tipos diferentes en cada sección | Indicar cambio |
| **Ritmicidad** | No más de 15 min de foco intenso sin transición | Indicar punto de pausa cognitiva |

### 4.4 Lo que el orquestador NO hace

- No genera explotación didáctica
- No lee el marco teórico completo (solo criterios de verificación destilados)
- No toma decisiones de contenido lingüístico (eso es de cada agente de sección, que genera sus propias notas lingüísticas integradas)
- No interviene en agentes transversales (diversidad, solucionario) — estos trabajan independientemente sobre el output compilado

---

## 5. ORGANIZACIÓN TEMPORAL Y AGENTES

### FASE ANTES: Preparación

| Agente | Qué hace | Input | Output |
|--------|----------|-------|--------|
| **Ingesta** | Extrae actividades del PDF del libro a datos estructurados organizados por página y sección, con metadatos por actividad (tipo, destreza, recursos, contenido lingüístico, textos completos, cuadros gramaticales) | PDF libro del alumno + imágenes de páginas | `datos/UXX-inventario.json` |

**Validación del editor** antes de continuar.

**Decisión de píldoras:** Tras validar el inventario, el editor (o el orquestador en su defecto) define qué **4-5 contenidos nuevos** de la unidad tendrán píldora (ver §3.11). Se decide:
- Qué contenidos merecen píldora (los que requieren comprensión pautada antes de poder usarse)
- De qué tipo es cada una (gramatical, de vocabulario, de mediación/funciones)
- A qué sección pertenece cada píldora

Esta lista se pasa al **Agente de Píldoras** (que genera el contenido completo en doble formato y multilingüe) y a cada **agente de sección** (que referencia las píldoras en la explotación donde corresponden).

> **Nota:** Las notas lingüísticas ya no son un agente separado. Cada agente de sección genera las notas lingüísticas relevantes integradas dentro de su explotación (ver §3.6).

### FASE DURANTE: Generación de la explotación

El **orquestador** coordina la invocación de los agentes de sección, filtrando el repertorio y el contexto para cada uno.

#### Agentes de sección (invocados por el orquestador)

| Agente | Sección del libro | Repertorios | Principios destilados | Output |
|--------|-------------------|-------------|----------------------|--------|
| **Vocabulario** | Vocabulario | Ciclo 5 fases (vocabulario), Sentence Builders, categorización semántica, flashcards | §5, §6, §8 del marco | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) — referencia píldoras donde corresponde |
| **Gramática** | Gramática | Ciclo 5 fases (gramática), inductivo/deductivo, weaning off, cuadros gramaticales | §3, §5, §6, §8 del marco | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) — referencia píldoras donde corresponde |
| **Comunicación** | Comunicación | Diálogos, producción oral, comprensión auditiva Pre-Durante-Post | §1, §2, §5.5, tarjetas producción oral | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) — referencia píldoras donde corresponde |
| **Destrezas** | Destrezas | Comprensión lectora Pre-Durante-Post (5 opciones), comprensión auditiva, producción escrita, tarjetas estrategia | §5.5, comprensión lectora/auditiva, recycling | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) — referencia píldoras donde corresponde |
| **Cultura** | Cultura | Conexión intercultural, cognición encarnada, creación de objetos, debate | §1 (integración), cognición encarnada | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) — referencia píldoras donde corresponde |
| **Reflexión** | Reflexión | Autoevaluación, repaso integrador, portfolio, metacognición | §2 (Gagné: evaluación formativa) | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) — referencia píldoras donde corresponde |
| **Evaluación** | Evaluación | Evaluación sumativa, rúbricas MCER, evaluación entre pares | §2 (Gagné: evaluación sumativa), MCER A1.1 | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) |

#### Agente de Píldoras (dedicado — genera material del alumno)

| Agente | Qué hace | Input | Output |
|--------|----------|-------|--------|
| **Píldoras** | Genera las 4-5 píldoras de la unidad, cada una en doble formato (presentación interactiva + hoja del estudiante) y en todas las L1 definidas (IT, FR, PT-BR, EN, CS, PL). Garantiza coherencia entre presentación y hoja. Ver §3.11 | Lista de píldoras decidida por el editor + contexto lingüístico + inventario de la sección correspondiente | Por cada píldora: presentación interactiva + hoja del estudiante × N lenguas |

El Agente de Píldoras puede trabajar **en paralelo** con los agentes de sección, ya que ambos parten de la misma decisión editorial (lista de píldoras). Los agentes de sección referencian las píldoras en la explotación; el Agente de Píldoras genera su contenido completo.

#### Agentes transversales (trabajan sobre el output compilado de toda la unidad)

| Agente | Qué hace | Input | Output |
|--------|----------|-------|--------|
| **Diversidad y errores por L1** | Adaptaciones por perfil + errores frecuentes por L1 | Explotación completa de la unidad + perfil alumnos + L1s | Adaptaciones + errores por L1 |
| **Solucionario** | Respuestas a todos los ejercicios + transcripciones | Inventario + PDF (verificación visual) | Respuestas + transcripciones |

**Validación del editor** de cada output antes de compilar.

### FASE DESPUÉS: Priorización y revisión

| Agente | Qué hace | Input | Output |
|--------|----------|-------|--------|
| **Priorizador temporal** | Analiza toda la explotación completada y genera propuesta de priorización por horas disponibles | Explotación completa + inventario + temporalización | Propuesta: actividades prioritarias (2h/semana) vs. todas (3+h/semana), con criterios |
| **Revisor** | Control de calidad del documento compilado | Documento compilado + marco teórico (como referencia de verificación) | Informe de calidad + correcciones |

**Validación del editor** final.

---

## 6. REPERTORIOS DE EXPLOTACIÓN: ESTRUCTURA

### 6.1 Estructura de un repertorio

Cada repertorio contiene:
1. **Opciones de explotación**: diferentes formas de explotar un mismo tipo de actividad
2. **Criterios de selección**: variables contextuales que determinan qué opción es más adecuada
3. **Principios restrictivos**: límites que aplican a TODAS las opciones (CLT, atención, etc.)

### 6.2 Repertorios por agente (a desarrollar)

#### Agente Vocabulario

| Tipo de actividad | Opciones de explotación |
|-------------------|------------------------|
| **Escucha y repite (vocabulario)** | Ciclo 5 fases con input visual saturado / Categorización semántica / Sentence Builder |
| **Escucha y relaciona** | Pre-Durante-Post auditivo con matching / Escucha segmentada |
| **Escucha y traduce** | Deducción por contexto antes de traducción / Traducción directa + reflexión contrastiva |
| **Práctica oral en parejas (vocabulario)** | Diálogo modelo → adaptación → producción libre / Gap de información / Encuesta + puesta en común |
| **Lee y escribe (vocabulario)** | Lectura modelo → producción paralela / Lectura + extracción + producción enriquecida |
| **Lee y escucha (vocabulario)** | Pre-Durante-Post con foco en vocabulario / Lectura contrastiva |
| **Comprensión lectora (vocabulario)** | Preguntas escalonadas / Búsqueda competitiva |
| **Completa huecos (vocabulario)** | Weaning off progresivo / Interleaving / Huecos → producción libre |

**Criterios de selección:**

| Variable | Afecta a |
|----------|----------|
| Cantidad de ítems nuevos (≤5 vs. >5) | Segmentar o no; nivel de apoyo inicial |
| Posición en la unidad (primera aparición vs. repaso) | Ciclo completo vs. solo fases 2-3-5 |
| Recursos disponibles (audio, imagen, texto) | Tipo de input y andamiaje |
| Contenido reciclable disponible | Nivel de interleaving con unidades anteriores |

#### Agente Gramática

| Tipo de actividad | Opciones de explotación |
|-------------------|------------------------|
| **Cuadro gramatical + ejercicios** | Ciclo 5 fases completo / Ciclo abreviado (1a+2b+3) / Solo fases 2-3-5 (reciclaje) |
| **Conjugación verbal** | Inductivo (si patrón saliente) / Deductivo (si irregular) / Mixto con pares mínimos |
| **Completa huecos (gramática)** | Weaning off progresivo / Interleaving / Huecos → producción libre |
| **Escribe preguntas (interrogativos)** | Preguntas escalonadas → producción libre / Encuesta con preguntas guiadas |
| **Producción oral (gramática)** | Diálogo guiado con foco gramatical / Role-play con estructura obligatoria |
| **Para aprender (sección del libro)** | Reflexión metacognitiva guiada / Sistematización con tarjetas |

**Criterios de selección:**

| Variable | Afecta a |
|----------|----------|
| Complejidad del contenido (regular vs. irregular) | Ciclo completo vs. abreviado; inductivo vs. deductivo |
| Cantidad de ítems nuevos (≤5 vs. >5) | Segmentar o no; nivel de apoyo inicial |
| Posición en la unidad (primera aparición vs. repaso) | Ciclo completo vs. solo fases 2-3-5 |
| Contenido reciclable disponible | Nivel de interleaving con unidades anteriores |

#### Agente Comunicación

| Tipo de actividad | Opciones de explotación |
|-------------------|------------------------|
| **Diálogo modelo** | Escucha + repetición + adaptación + actuación / Escucha + análisis funcional + producción libre / Escucha + role-play con variación |
| **Actividad de producción oral** | Con tarjetas de estrategia (Comodín, Tiempo Extra) / Con gap de información asimétrico / Con escalado (individual → parejas → grupo) |
| **Audio con preguntas** | Pre-Durante-Post estándar / Con predicción + verificación / Con transcripción visible (A1 complejo) |

**Criterios de selección:**

| Variable | Afecta a |
|----------|----------|
| Complejidad del audio (velocidad, vocabulario) | Nivel de andamiaje; uso de transcripción |
| Función comunicativa (presentarse, pedir, describir) | Tipo de role-play; nivel de personalización |
| Actividades adyacentes | Si hay gramática antes → conectar; si hay lectura después → preparar |

#### Agente Destrezas

| Tipo de actividad | Opciones de explotación |
|-------------------|------------------------|
| **Texto de lectura** | Pre-Durante-Post estándar / Lectura guiada con tarjetas / Text mining / Lectura + producción / Lectura cooperativa (jigsaw) |
| **Audio en destrezas** | Segmentada con tareas por fragmento / Con predicción y verificación / Con transcripción progresiva |
| **Producción escrita** | Modelo → adaptación → libre / Con Textlupe cooperativa / Con Sentence Builder como andamiaje |

**Criterios de selección:**

| Variable | Afecta a |
|----------|----------|
| Longitud del texto/audio | Fragmentación; uso de tarjetas |
| Contenido lingüístico nuevo | Intensidad del text mining |
| Posición en la unidad | Primera lectura → más pre-lectura; final → cooperativa |
| Recursos disponibles | Con audio → integrar escucha; con imágenes → escáner visual |

#### Agente Cultura

| Tipo de actividad | Opciones de explotación |
|-------------------|------------------------|
| **Texto cultural** | Lectura + comparación intercultural + debate / Lectura + creación de objeto / Lectura + presentación oral |
| **Actividad de conexión** | Conocimiento previo + mapa mental + producción / Investigación guiada + póster / Debate estructurado |

**Criterios de selección:**

| Variable | Afecta a |
|----------|----------|
| Tema (geografía, costumbres, personajes) | Tipo de producción final |
| Conexión con L1/cultura del alumno | Nivel de comparación intercultural |
| Posición respecto a proyecto (cada 3 unidades) | Integración con proyecto o actividad independiente |

#### Agente Reflexión

| Tipo de actividad | Opciones de explotación |
|-------------------|------------------------|
| **Actividad de repaso** | Quiz rápido + autoevaluación / Interleaving con unidades anteriores / Juego de repaso (gamificación) |
| **Autoevaluación** | Portfolio + reflexión guiada / Descriptores "puedo..." con autocalificación / Diario de aprendizaje |
| **Para aprender** | Reflexión metacognitiva guiada / Sistematización con tarjetas / Estrategias de estudio |

#### Agente Evaluación

| Tipo de actividad | Opciones de explotación |
|-------------------|------------------------|
| **Evaluación sumativa** | Rúbrica con descriptores MCER / Evaluación entre pares / Test de contenidos de la unidad |
| **Evaluación formativa** | Observación con checklist / Tareas de desempeño / Portfolio |

### 6.3 Gamificación como criterio transversal

La gamificación no es un repertorio separado sino un **criterio de enriquecimiento** que aplican todos los agentes de sección. Se integra como una variable más en la selección de opciones de explotación:

| Principio | Aplicación |
|-----------|------------|
| Elementos lúdicos distribuidos | Al menos 1-2 por sección (no concentrados en una sola) |
| Competición sana | Puntos, equipos, retos — siempre con objetivo lingüístico |
| Recompensa del proceso | Valorar el intento y la participación, no solo el resultado |
| Integración natural | El juego es un vehículo para la práctica, no un sustituto |

El orquestador verifica que la gamificación esté distribuida equilibradamente en la unidad.

---

## 7. AGENTE PRIORIZADOR TEMPORAL: CRITERIOS DE DECISIÓN

Este agente trabaja DESPUÉS de que toda la explotación esté completada. Necesita criterios explícitos para decidir qué actividades son prioritarias para clase y cuáles pueden hacerse fuera.

### Criterios de prioridad para clase (2h/semana)

| Criterio | Prioridad ALTA (en clase) | Prioridad BAJA (autónomo/casa) |
|----------|--------------------------|-------------------------------|
| **Tipo de interacción** | Requiere interacción oral, parejas, grupos | Individual, escrito, mecánico |
| **Primera exposición** | Contenido nuevo que el alumno ve por primera vez | Práctica adicional de contenido ya presentado |
| **Corrección necesaria** | Actividades donde los errores necesitan corrección inmediata | Ejercicios autocorregibles (con solucionario) |
| **Mediación del profesor** | Actividades que requieren modelado, guía, retroalimentación en tiempo real | Actividades con instrucciones claras y autosuficientes |
| **Fase del ciclo** | Fases 1 (modelling/awareness), 3 (retroalimentación), 4 (reflexión) | Fases 2a receptiva (parcial), 5 consolidación |
| **Componente sociocultural** | Cultura, debate, conexión personal | — |
| **Audio/vídeo** | Primera escucha/visualización con pre-actividad | Re-escuchas, fichas de trabajo del cuaderno |

### Output del priorizador

Para cada unidad, genera una tabla tipo:

| Sección | Actividad | En clase (2h) | Autónomo (2h) | En clase (3+h) |
|---------|-----------|---------------|---------------|----------------|
| Vocabulario | Flashcards p.34 | ✓ | | ✓ |
| Gramática | Cuadro + ej. 1-3 | ✓ | | ✓ |
| Gramática | Ej. 4-5 (completar) | | ✓ (cuaderno) | ✓ |
| Destrezas | Lectura p.40 | ✓ | | ✓ |
| ... | ... | ... | ... | ... |

---

## 8. ESTRUCTURA DE LA GUÍA IMPRESA (por unidad)

| Sección | Contenido | Genera |
|---------|-----------|--------|
| **1. Explotación didáctica** | Cada sección sigue esta secuencia: **Estación de servicio** (tarjetas de andamiaje, ver §3.7) → **Insignia** (meta gamificada de la sección, ver §3.8) → **Secuenciación didáctica** por bloques de actividades agrupadas por lógica, cada bloque con objetivo + preparación + fases con título descriptivo + puntos de insignia (ver §3.9-§3.10). Las notas lingüísticas van integradas dentro de las fases (ver §3.6). Las **píldoras** (ver §3.11) se referencian en las fases donde corresponden y su contenido completo se incluye como material anexo reproducible | Ag. Vocabulario + Ag. Gramática + Ag. Comunicación + Ag. Destrezas + Ag. Cultura + Ag. Reflexión + Ag. Evaluación (coordinados por Orquestador) |
| **2. Atención a la diversidad** | Adaptaciones por perfil + errores frecuentes por L1 | Ag. Diversidad |
| **3. Propuesta de priorización** | Tabla de actividades prioritarias según horas disponibles (2h vs. 3+h) | Ag. Priorizador temporal |
| **4. Píldoras (material reproducible)** | 4-5 píldoras por unidad en doble formato: presentación interactiva (para el profesor) + hoja del estudiante (imprimible). Cada píldora en todas las L1 (IT, FR, PT-BR, EN, CS, PL). Estructura fija: descubrimiento guiado → regla explícita → comprensión de la regla → espacio para notas. Ver §3.11 | **Ag. Píldoras** (agente dedicado) |
| **5. Solucionario** | Respuestas a todos los ejercicios | Ag. Solucionario |
| **6. Transcripciones** | Transcripciones de audios | Ag. Solucionario |

**Nota:** La evaluación ya no es una sección separada de la guía — el **Ag. Evaluación** genera su explotación como una sección más del libro (dentro de la sección 1), igual que Vocabulario, Gramática, etc.

---

## 9. CONSECUENCIA PARA LOS DOCUMENTOS

### `marco-teorico-metodologico.md`

Pasa de ser "lo que el agente lee" a ser **documento de referencia del proyecto**: fundamentación teórica que justifica las decisiones, consultable por el editor humano y usado como fuente para construir las instrucciones de cada agente. El Agente Revisor es el único que lo lee completo — para verificar que el output cumple los principios.

### `00-curso-general.md`

Mismo cambio: los datos factuales (perfil, temporalización, progresiones) y las orientaciones metodológicas se integran directamente en las instrucciones del agente que las necesita. El documento sigue existiendo como referencia del proyecto.

### Nuevo: Instrucciones operativas por agente

Cada agente recibe un prompt que incluye SOLO los criterios destilados que necesita, organizados como instrucciones directas. No lee documentos largos — sus instrucciones YA contienen la información relevante.

### Nuevo: Repertorios como documentos independientes

Cada repertorio de explotación se documenta como un archivo consultable:
- `repertorios/vocabulario.md`
- `repertorios/gramatica.md`
- `repertorios/comunicacion.md`
- `repertorios/destrezas.md`
- `repertorios/cultura.md`
- `repertorios/reflexion.md`
- `repertorios/evaluacion.md`

El orquestador extrae de estos archivos solo las opciones relevantes al tipo de actividad que se va a explotar en cada momento.

---

## 10. RESUMEN DE AGENTES v5.0

| # | Agente | Fase | Tipo | Output |
|---|--------|------|------|--------|
| 0 | Ingesta | ANTES | Preparación | `datos/UXX-inventario.json` (organizado por sección, con metadatos por actividad) |
| 1 | **Orquestador** | DURANTE | Coordinación | Contexto filtrado para cada agente + verificación post |
| 2 | Vocabulario | DURANTE | Sección | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) |
| 3 | Gramática | DURANTE | Sección | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) |
| 4 | Comunicación | DURANTE | Sección | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) |
| 5 | Destrezas | DURANTE | Sección | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) |
| 6 | Cultura | DURANTE | Sección | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) |
| 7 | Reflexión | DURANTE | Sección | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) |
| 8 | Evaluación | DURANTE | Sección | Estación de servicio + Insignia + Preparación + Explotación (con notas lingüísticas integradas) |
| 9 | **Píldoras** | DURANTE | Dedicado | Presentación interactiva + Hoja del estudiante × N lenguas (IT, FR, PT-BR, EN, CS, PL) |
| 10 | Diversidad y errores por L1 | DURANTE | Transversal | Adaptaciones + errores por L1 |
| 11 | Solucionario | DURANTE | Transversal | Respuestas + transcripciones |
| 12 | Priorizador temporal | DESPUÉS | Post-producción | Propuesta de priorización por horas |
| 13 | Revisor | DESPUÉS | Post-producción | Informe de calidad + correcciones |

**14 agentes**, organizados en 5 tipos:
- **1 de preparación** (ingesta)
- **1 de coordinación** (orquestador)
- **7 de sección** (vocabulario, gramática, comunicación, destrezas, cultura, reflexión, evaluación) — 1 agente por cada sección del libro. Cada uno genera notas lingüísticas integradas en su explotación (ver §3.6) y referencia píldoras donde corresponde
- **1 dedicado** (píldoras) — genera material del alumno en doble formato y multilingüe (ver §3.11)
- **2 transversales** (diversidad, solucionario)
- **2 de post-producción** (priorizador, revisor)

---

## 11. PRÓXIMOS PASOS

1. **Desarrollar los repertorios completos** de explotación por tipo de actividad para cada agente de sección, extrayendo las opciones de `marco-teorico-metodologico.md` y `00-curso-general.md`
2. **Definir los criterios de selección** detallados para cada repertorio (variables contextuales + tabla de decisión)
3. **Destilar las instrucciones operativas** de cada agente: prompt con principios integrados, restricciones, y formato de output
4. **Diseñar el prompt del orquestador** con criterios de verificación y lógica de routing
5. **Pilotar con U03** (La familia) — unidad con gramática nueva (presente regular, tener, posesivos), vocabulario temático (familia), y destrezas integradas

---

*Documento creado: 2025-02-01*
*Última actualización: 2025-02-01*
*Origen: Análisis del marco teórico en contexto del framework + diagnóstico de operatividad de agentes + decisiones de diseño sobre guía impresa + iteraciones sobre arquitectura de agentes de sección con repertorios*
