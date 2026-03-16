# CrewAI — Memoria, Aprendizaje y Agente Recurvo
## Guía Didáctica del Profesor — Nuevo Compañeros 1

> **Fecha:** 2026-03-15
> **Estado:** Diseño. Nada implementado todavía.
> **Dependencia:** Requiere la arquitectura de dos fases definida en `sistema-agentes-propuesta.md` (actualización 2026-03-15)

---

## 1. SISTEMA DE MEMORIA EN CREWAI — ANÁLISIS PARA ESTE PROYECTO

CrewAI ofrece 4 tipos de memoria. No todos aplican igual a todos los agentes. Este análisis evalúa cada tipo según su utilidad **real** para este proyecto, no su descripción teórica.

### 1.1 Memoria a corto plazo (ChromaDB + RAG)

**Qué hace:** Dentro de una ejecución, cada agente puede acceder a lo que produjeron los anteriores. Usa ChromaDB (base de datos vectorial) con RAG (Retrieval-Augmented Generation) para buscar por similaridad semántica.

**Aplica a este proyecto:** Sí, parcialmente.

- **Fase 1 → Fase 2:** Los agentes de sección (Fase 2) necesitan recibir lo que produjeron los agentes de recursos (Fase 1). Este es el mecanismo de paso.
- **Matiz importante:** Para datos estructurados como tarjetas JSON, **pasar el output directamente entre tareas es más fiable que depender del RAG**, que está diseñado para texto no estructurado. CrewAI permite ambos mecanismos. Para los agentes de recursos, el paso directo (output de una tarea como input de otra) es lo correcto.
- **Entre agentes de Fase 1:** No aplica. Los 3 agentes de recursos (Tarjetas, Gramatips, Estrategias) corren en paralelo y no necesitan leerse entre sí.

**Veredicto:** Usar el paso directo de outputs entre tareas. El RAG de ChromaDB es útil como complemento, no como mecanismo principal.

### 1.2 Memoria a largo plazo (SQLite)

**Qué hace:** Después de cada ejecución, almacena qué enfoque usó el agente, qué resultado produjo, y si fue aprobado o corregido. En la siguiente ejecución, el agente consulta: "¿qué funcionó la última vez?"

**Aplica a este proyecto:** Sí, pero con matices según el tipo de agente.

- **Agentes creativos (Redactor de explotación, Cultura):** Muy útil. Estos agentes toman decisiones sobre enfoque, tono, nivel de detalle. "¿La última vez fui demasiado prescriptivo?" → ajustar.
- **Agentes de recursos (Recurvo, Gramatips):** Útil pero diferente. El trabajo es más determinista (extraer → clasificar → generar). El "aprendizaje" aquí no es de enfoque sino de **correcciones factuales**: traducciones corregidas, sílabas tónicas corregidas, reglas morfológicas corregidas.

**Veredicto:** Activar para todos los agentes. Pero para el agente Recurvo, lo que se almacena son correcciones factuales, no variaciones de enfoque.

### 1.3 Memoria de entidades (RAG)

**Qué hace:** Recuerda conceptos del dominio como entidades con atributos. Cuantas más unidades procese, más sabe del dominio. Usa RAG (búsqueda por similaridad semántica).

**Aplica a este proyecto:** La función es esencial, pero la implementación por defecto NO es la más fiable para vocabulario.

- **El problema:** El entity memory de CrewAI busca por similaridad semántica. "Abuelo" y "abuela" son semánticamente similares — el RAG podría confundirlos o devolver ambos cuando solo necesitas uno. Para un catálogo de vocabulario donde necesitas búsqueda exacta ("¿existe ya la palabra *abuelo*?"), una consulta directa a base de datos o JSON es más fiable.
- **La solución:** Crear una **tool custom** dentro de CrewAI que consulte la BD (Neon PostgreSQL) con búsqueda exacta. No es salir de CrewAI — es extenderlo de la forma en que está diseñado para ser extendido.
- **Para otros agentes:** El entity memory sí puede ser útil para agentes de sección que necesitan recordar conceptos pedagógicos ("inductivo vs deductivo", "weaning off", "scaffolding") donde la similaridad semántica es una ventaja.

**Veredicto:** Para vocabulario → tool custom con búsqueda exacta. Para conceptos pedagógicos → entity memory de CrewAI.

### 1.4 Aprendizaje por feedback (se construye dentro de CrewAI)

**Qué hace:** CrewAI NO incluye un sistema de feedback editorial. Lo construimos nosotros como extensión. El ciclo es:

1. El agente genera output (ej: tarjetas de vocabulario para U03)
2. El editor revisa y califica: **aprobado** o **corregido**
3. Si corrige, el sistema almacena: "en vocabulario U03, el error fue X, la corrección fue Y"
4. En U04, el agente recibe en su contexto: "ERRORES ANTERIORES A EVITAR: [lista]"
5. Los outputs aprobados se convierten en ejemplos de referencia (few-shot)

**Aplica a este proyecto:** Es el mecanismo más valioso. Es lo que realmente hace que el sistema mejore entre unidades.

**Requisitos de implementación:**

| Requisito | Descripción |
|-----------|-------------|
| Formato de almacenamiento | Tabla `correcciones` en Neon PostgreSQL con: agente, unidad, sección, campo, valor_original, valor_corregido, tipo_error, fecha |
| Inyección en prompt | Antes de cada ejecución, recuperar correcciones relevantes e inyectarlas en el contexto |
| Gestión de tamaño | Limitar a las N correcciones más relevantes para no explotar la ventana de contexto. Criterio: priorizar errores recurrentes y errores recientes |
| Few-shot examples | Los outputs aprobados sin correcciones se guardan como ejemplos de referencia |

**Veredicto:** Prioridad alta. Construir como tools + contexto inyectado dentro de CrewAI.

### 1.5 Optimización automática de prompts (DSPy) — FUTURO

**Qué hace:** Framework que optimiza automáticamente los prompts basándose en qué instrucciones producen mejores resultados.

**Aplica a este proyecto:** No todavía. Necesita ~30 outputs aprobados como dataset de entrenamiento. Con 1 unidad completa (U03), estamos lejos.

**Cuándo activar:** Después de completar U06-U07 (si hay suficientes outputs aprobados).

**Veredicto:** En el roadmap, no en el diseño actual.

---

## 2. RESUMEN: QUÉ USAR DE CREWAI Y QUÉ PERSONALIZAR

| Componente | ¿Estándar CrewAI o custom? | Justificación |
|---|---|---|
| Agent (rol, meta, backstory) | Estándar | Funciona tal cual |
| Task (descripción, output) | Estándar | Funciona tal cual |
| Crew + Process | Estándar | Fase 1 parallel, Fase 2 sequential |
| Tools | **Custom** (la mayoría) | Consultar BD (inventario, tarjetas, correcciones), escribir en BD, exportar CSV. Normal en CrewAI — la mayoría de proyectos crean tools propias |
| Short-term memory | Estándar + paso directo | Paso directo de outputs para datos estructurados |
| Long-term memory | Estándar | Activar para todos los agentes |
| Entity memory | **Custom** para vocabulario | Tool con búsqueda exacta en BD, no RAG semántico |
| Feedback/aprendizaje | **Custom** | No existe en CrewAI. Lo construimos como tool + contexto |
| LLM por agente | Estándar (multi-model) | CrewAI soporta asignar modelo diferente por agente |

---

## 2B. DECISIÓN ARQUITECTÓNICA: BD COMO FUENTE DE VERDAD

### Principio

**La base de datos (Neon PostgreSQL) es la fuente de verdad para todos los datos estructurados.** Los archivos JSON son formato de extracción/entrada, no de almacenamiento. Los archivos CSV son formato de exportación para InDesign.

### Flujo

```
ANTES (descartado):
  Agente → JSON local → script importa → BD
  (duplicación, sincronización manual, fragilidad)

AHORA (adoptado):
  Agente → BD directamente (via tool custom de CrewAI)
  BD → CSV (exportación para InDesign, bajo demanda)
```

### Qué va en la BD y qué en archivos

| Dato | Almacenamiento | Razón |
|---|---|---|
| Inventarios de actividades | **BD** (ya están: tablas `paginas`, `actividades`, `respuestas`) | Datos estructurados, esquema fijo, relaciones |
| Tarjetas de vocabulario | **BD** (nueva tabla `tarjetas_vocabulario`) | Datos estructurados, búsqueda exacta por palabra, relaciones con unidades |
| Correcciones del editor | **BD** (nueva tabla `correcciones`) | Datos relacionales (corrección → tarjeta → agente) |
| Contenidos índice | **BD** (ya existe: `unidades.contenidos_indice`) | Ya implementado |
| CSV para InDesign | **Exportación desde BD** | Formato de salida, no almacenamiento. Se genera bajo demanda |
| JSON de extracción | **Archivo temporal** (`datos/inventarios/`) | Formato de entrada: Claude lee PDF → genera JSON → se importa a BD. Una vez importado, la BD es la verdad |
| Prompts de agentes (.md) | **Archivos** | Documentos no estructurados, versionables en git |
| Marco teórico, repertorios | **Archivos** | Infraestructura pedagógica, no datos operacionales |

### Justificación por fuentes profesionales

1. **Google Cloud (2025):** "Build stateless agent applications and manage state in external storage services." Los agentes no deben depender de archivos locales como estado.
2. **AWS (2025):** "The database technology should be selected based on the nature of the data stored and access patterns." Datos estructurados con esquema fijo → BD relacional.
3. **Microsoft (2025):** "Hierarchical multi-agent architecture with clear functional layers including storage." La capa de almacenamiento es propia, no archivos sueltos.
4. **Anthropic (2025):** "Subagents call tools to store their work in external systems, then pass lightweight references." El agente escribe en BD, pasa referencia al siguiente agente.

### Fuentes

- [Google Cloud — Choose your agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components)
- [AWS — Key components of a data-driven agentic AI application](https://aws.amazon.com/blogs/database/key-components-of-a-data-driven-agentic-ai-application/)
- [Microsoft — Data architecture for AI agents](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/data-architecture-plan)
- [Anthropic — Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

---

## 3. AGENTE RECURVO — VOCABULARIO

> **Nombre:** Recurvo (Recurso + Vocabulario). Agente de recursos especializado en vocabulario.

### 3.1 Identidad

| Campo CrewAI | Valor |
|---|---|
| **name** | `recurso_vocabulario` |
| **role** | Extractor y generador de tarjetas de vocabulario |
| **goal** | Identificar y estructurar el vocabulario de una unidad en tres niveles (campo semántico principal del índice, campos secundarios por frecuencia, palabras difíciles sueltas) y expresiones multipalabra. Generar tarjetas estandarizadas y proponer la lista completa al editor para validación |
| **backstory** | Especialista en lexicología aplicada a ELE A1.1. Conoce los campos semánticos del nivel, las 7 L1 del aula (IT, FR, PT-BR, EN, CS, PL, TR), las reglas morfológicas del español (género, número, acentuación) y el inventario léxico de todas las unidades previas. Su trabajo alimenta a los agentes de sección, que reciben tarjetas listas en lugar de extraer vocabulario ellos mismos. |
| **phase** | 1 (Recursos — paralelo) |
| **llm** | `claude-sonnet-4-6` (generación) |

### 3.2 Jerarquía de vocabulario

El agente identifica vocabulario en tres niveles, no indiscriminadamente:

| Nivel | Origen | Ejemplo U03 | Obligatoriedad |
|---|---|---|---|
| **1. Campo semántico principal** | Definido en el índice de contenidos de la unidad (`contenidos_indice`) | Parentesco (familia) | Obligatorio. Todas las palabras de este campo generan tarjeta |
| **2. Campos semánticos secundarios** | NO vienen en el índice. Se determinan por su **frecuencia de aparición** en las actividades de la unidad | Profesiones | El agente los identifica y propone. El editor valida |
| **3. Palabras difíciles sueltas** | Palabras que el estudiante probablemente no conoce, aunque no pertenezcan a ningún campo semántico recurrente | — | El agente las propone. El editor valida |

Además, el agente identifica **expresiones multipalabra** (chunks léxicos) que funcionan como unidad y no deben separarse en palabras individuales. Ejemplo U03: "hermano menor", "hermano mayor" → una tarjeta por expresión, no por palabra.

### 3.3 Qué hace

1. Consulta la BD: inventario completo de la unidad (todas las páginas, todas las secciones)
2. Consulta la BD: índice de contenidos (`contenidos_indice`) para obtener el campo semántico principal
3. Identifica vocabulario en los 3 niveles + expresiones multipalabra
4. Consulta la BD: tarjetas de unidades anteriores (memoria inter-unidad)
5. Clasifica cada entrada: **nueva ⭐** (primera aparición) o **reutilizada ♻️** (ya tiene tarjeta)
6. Genera tarjetas nuevas con todos los campos del formato obligatorio
7. Para tarjetas reutilizadas: copia la tarjeta existente, actualiza frecuencia acumulada
8. **Propone la lista completa al editor para validación** antes de escribir en BD
9. **Escribe las tarjetas validadas en la BD** (tabla `tarjetas_vocabulario`)
10. Exporta CSV para InDesign bajo demanda

### 3.4 Qué NO hace

- No genera explotación didáctica (eso es de los agentes de sección)
- No decide cómo usar las tarjetas en clase (eso es de los agentes de sección)
- No genera gramatips ni estrategias (otros agentes de Fase 1)
- No interpreta actividades pedagógicamente — solo extrae y estructura vocabulario
- No decide unilateralmente qué vocabulario entra — propone y el editor valida (niveles 2 y 3)

### 3.5 Inputs

Todos los inputs vienen de la BD (Neon PostgreSQL), no de archivos locales.

| Input | Tabla BD | Descripción |
|---|---|---|
| Inventario | `paginas`, `actividades`, `respuestas` | Todas las actividades de la unidad: tipo, destreza, recursos, contenido lingüístico, textos |
| Contenidos índice | `unidades.contenidos_indice` | Campo semántico principal y contenidos lingüísticos de la unidad |
| Tarjetas previas | `tarjetas_vocabulario` (nueva) | Tarjetas generadas en unidades anteriores. Permite detectar reutilización (♻️) |
| Correcciones previas | `correcciones` (nueva) | Errores corregidos por el editor en ejecuciones anteriores |
| PDF fuente (opcional) | Archivo: `datos/fuente/UXX/UXX-libro.pdf` | Solo para verificación visual si hay ambigüedad en el inventario |

### 3.5 Output

JSON estructurado (no markdown). El markdown lo genera el agente de sección cuando integra las tarjetas en la Caja 1 de la Estación de Servicio.

```json
{
  "unidad": 3,
  "fecha_generacion": "2026-03-15",
  "total_tarjetas": 18,
  "nuevas": 16,
  "reutilizadas": 2,
  "por_seccion": {
    "vocabulario": {
      "paginas": [34, 35],
      "tarjetas": [
        {
          "palabra": "abuelo",
          "genero": "M",
          "color_genero": "azul",
          "silaba_tonica": "aBUElo",
          "regla": "M termina en -o, F termina en -a: abuel-o / abuel-a",
          "campo_semantico": "Parentesco",
          "color_campo": "violeta",
          "ejemplo": "Mi abuelo tiene setenta años.",
          "frecuencia": 3,
          "irregularidad": "",
          "combos": [
            "mi/tu/su + abuelo",
            "el abuelo de + nombre",
            "abuelo + abuela = abuelos",
            "es el abuelo de"
          ],
          "traducciones": {
            "IT": "nonno",
            "FR": "grand-père",
            "PT_BR": "avô",
            "EN": "grandfather",
            "CS": "dědeček",
            "PL": "dziadek",
            "TR": "büyükbaba"
          },
          "_gestion": {
            "unidad": 3,
            "estado": "nueva",
            "unidad_origen": 3
          }
        }
      ]
    },
    "gramatica": {
      "paginas": [36, 37],
      "tarjetas": []
    },
    "comunicacion": {
      "paginas": [38, 39],
      "tarjetas": []
    }
  }
}
```

> **Output:**
> - **Primario:** Escribe las tarjetas directamente en la tabla `tarjetas_vocabulario` de Neon PostgreSQL. Los agentes de sección (Fase 2) las consultan desde la BD.
> - **Exportación:** `datos/tarjetas/UXX-vocabulario.csv` — CSV para InDesign (Data Merge). Se genera bajo demanda desde la BD. Solo campos impresos, sin campos de gestión. Delimitado por `;`.
>
> El JSON de ejemplo de arriba muestra la estructura de datos, no el formato de almacenamiento. Los datos viven en la BD.

### 3.6 Formato de tarjeta — Campos

#### Campos de la tarjeta (aparecen en la tarjeta impresa)

| # | Campo | Descripción | Ejemplo |
|---|---|---|---|
| 1 | Palabra | Término en español (o expresión multipalabra) | abuelo / hermano menor |
| 2 | Género | M / F | M |
| 3 | Color género | azul (M) / rojo (F). Solo dos colores, según `materiales/especificaciones-diseno-tarjetas.md` | azul |
| 4 | Sílaba tónica | Palabra completa sin guiones, sílaba tónica en MAYÚSCULAS | aBUElo |
| 5 | Regla | Regla morfológica que explica la forma | M en -o, F en -a: abuel-o / abuel-a |
| 6 | Campo semántico | Nombre del grupo léxico | Parentesco |
| 7 | Color campo | Color asignado al campo semántico (badge/icono oscuro). Ver `materiales/especificaciones-diseno-tarjetas.md` | violeta |
| 8 | Ejemplo | Frase corta de uso real | Mi abuelo tiene setenta años. |
| 9 | Frecuencia | ★ (baja) / ★★ (media) / ★★★ (alta) → 1/2/3 en JSON. Ver criterios de cálculo abajo | 3 |
| 10 | Irregularidad | Solo si no sigue el patrón. Vacío si es regular | — |
| 11 | Combos | 4 combinaciones frecuentes de la palabra (chunks / patrones de construcción gramatical). Definidos en `materiales/especificaciones-diseno-tarjetas.md` | mi/tu/su + padre, el padre de + nombre, es el padre de, padre + madre = padres |
| 12 | IT | Traducción italiano | nonno |
| 13 | FR | Traducción francés | grand-père |
| 14 | PT-BR | Traducción portugués brasileño | avô |
| 15 | EN | Traducción inglés | grandfather |
| 16 | CS | Traducción checo | dědeček |
| 17 | PL | Traducción polaco | dziadek |
| 18 | TR | Traducción turco | büyükbaba |
| — | Espacio de nota personal | No es un campo de datos. Es un espacio en blanco físico en la tarjeta impresa donde el alumno escribe sus propias notas | — |

#### Campos de gestión interna (NO aparecen en la tarjeta impresa)

| # | Campo | Descripción | Ejemplo |
|---|---|---|---|
| 19 | Unidad | Unidad donde aparece. Solo para clasificación interna y agrupación | 3 |
| 20 | Estado | nueva ⭐ / reutilizada ♻️ | nueva |
| 21 | Unidad origen | Unidad donde se generó la tarjeta por primera vez | 3 |

#### Criterios de cálculo de frecuencia

**Pendiente de definir.** La frecuencia (★/★★/★★★) indica la importancia de la palabra para el nivel A1.1, pero no hay criterios objetivos establecidos todavía. Opciones a evaluar:

| Criterio | Descripción | Ventaja | Riesgo |
|---|---|---|---|
| Frecuencia en el libro | Cuántas veces aparece la palabra en las actividades del libro | Objetivo, medible | No refleja la frecuencia real del español |
| Frecuencia léxica general | Basada en corpus de frecuencia del español (ej: CREA, Corpus del Español) | Refleja el uso real | Puede no coincidir con la progresión del libro |
| Frecuencia funcional A1.1 | Qué tan útil es la palabra para las funciones comunicativas del nivel A1.1 (presentarse, describir familia, etc.) | Alineado con MCER | Subjetivo sin criterio explícito |
| Combinación | Promedio ponderado de las anteriores | Más completo | Más complejo |

> **Decisión pendiente:** ¿qué criterio usa el editor actualmente? ¿O se define uno nuevo?

### 3.7 Tools (herramientas CrewAI)

Todas las tools de datos operan contra Neon PostgreSQL.

| Tool | Tipo | Función |
|---|---|---|
| `consultar_inventario` | Custom (BD) | Consulta actividades de la unidad en BD (`paginas`, `actividades`). Filtra por sección si se le pide |
| `consultar_tarjetas_previas` | Custom (BD) | Busca en `tarjetas_vocabulario` si una palabra ya tiene tarjeta en unidades anteriores. Búsqueda exacta |
| `consultar_correcciones` | Custom (BD) | Recupera correcciones del editor desde `correcciones` para este tipo de agente |
| `escribir_tarjetas` | Custom (BD) | Escribe tarjetas validadas en `tarjetas_vocabulario` |
| `exportar_csv` | Custom | Genera CSV desde la BD para InDesign. Formato Data Merge, delimitado por `;` |
| `PDFReadTool` | CrewAI estándar | Lee el PDF del libro si necesita verificar visualmente algo ambiguo |

### 3.8 Modelo LLM

**Generación: Claude Sonnet** (`claude-sonnet-4-6`)

Justificación basada en la prueba comparativa (2026-03-15):
- Es el único modelo que acertó sílabas tónicas (a-BUE-lo, no a-BU-elo)
- Traducciones correctas a 6 idiomas (primo = cousin, no nephew)
- Reglas morfológicas sin errores factuales
- Las tarjetas son material impreso que llega al alumno — tolerancia a errores = cero

**Verificación (futuro): Modelo económico** (Haiku o Kimi K2) para cross-check de traducciones y sílabas tónicas como segunda capa de control.

### 3.9 Memoria

| Tipo | Configuración | Función para este agente |
|---|---|---|
| Short-term | Activada (estándar CrewAI) | Su output pasa a los agentes de sección en Fase 2 |
| Long-term | Activada (estándar CrewAI) | Almacena correcciones factuales entre ejecuciones |
| Entity | **Tool custom** (BD) | `tarjetas_vocabulario` con búsqueda exacta por palabra. Permite detectar ♻️ reutilizadas |
| Feedback | **Tool custom** (BD) | `correcciones` — inyecta correcciones del editor en el prompt antes de cada ejecución |

### 3.10 Lógica de extracción

```
PASO 1 — Identificar el campo semántico principal
  Consultar BD: unidades.contenidos_indice → campo semántico del índice
  Ejemplo U03: "Parentesco (familia)"

PASO 2 — Recorrer el inventario completo de la unidad
  Consultar BD: paginas + actividades de la unidad
  Para cada página y actividad:
    a. Extraer vocabulario explícito (negrita, listas, etiquetas en imágenes)
    b. Extraer vocabulario de textos (diálogos, modelos, lecturas)
    c. Identificar expresiones multipalabra que funcionan como unidad
       (ej: "hermano menor", "hermano mayor" → 1 tarjeta, no 2 palabras)

PASO 3 — Clasificar en 3 niveles
  Nivel 1: Palabras del campo semántico principal (del índice) → obligatorias
  Nivel 2: Palabras de campos semánticos secundarios, determinados por
           frecuencia de aparición en la unidad (NO vienen en el índice)
           → propuestas al editor
  Nivel 3: Palabras difíciles sueltas que el estudiante probablemente
           no conoce, sin pertenecer a un campo recurrente → propuestas al editor

PASO 4 — Consultar tarjetas previas en BD
  Consultar BD: tarjetas_vocabulario WHERE unidad < unidad_actual
  Para cada entrada (palabra o expresión):
    ¿Existe tarjeta en unidades anteriores?
      → SÍ: estado = ♻️ reutilizada. Copiar tarjeta, actualizar frecuencia
      → NO: estado = ⭐ nueva. Generar todos los campos

PASO 5 — Proponer al editor
  Presentar lista completa organizada por niveles.
  El editor valida: confirma, elimina o añade entradas.
  (Actualmente en VSCode; futuro: interfaz dedicada)

PASO 6 — Escribir en BD
  a. INSERT tarjetas validadas en tarjetas_vocabulario
     (cada tarjeta asignada a la sección donde aparece por primera vez)
  b. Exportar CSV bajo demanda: SELECT → datos/tarjetas/UXX-vocabulario.csv
```

### 3.11 Criterios de calidad (verificables)

| Criterio | Verificación |
|---|---|
| Todas las palabras del inventario están cubiertas | Comparar tarjetas en BD vs. actividades del inventario en BD |
| Sílabas tónicas correctas | RAE como referencia |
| Traducciones a 7 idiomas correctas | Diccionarios de referencia (WordReference, Reverso) |
| Reglas morfológicas sin errores | Gramática de referencia A1.1 |
| Estado nueva/reutilizada correcto | `SELECT` cruzado en BD: tarjeta actual vs. tarjetas con unidad_origen < unidad_actual |
| CSV válido para InDesign | Importar en InDesign y verificar que los campos se mapean |

---

## 4. PLAN DE CONSTRUCCIÓN (CORREGIDO)

Plan original revisado con correcciones basadas en el análisis de la prueba de modelos y la arquitectura de dos fases.

> **Nota:** "Paso" = orden de construcción. "Fase" = arquitectura de agentes (Fase 1 Recursos, Fase 2 Secciones). Son cosas distintas.

| Paso | Qué | Corrección vs. plan original | Resultado |
|---|---|---|---|
| 1. Infraestructura | Instalar CrewAI + Groq SDK + Anthropic SDK, .env, estructura de carpetas. **Crear tablas `tarjetas_vocabulario` y `correcciones` en Neon PostgreSQL** | Añadido: creación de tablas BD para tarjetas y feedback | Sistema base + BD lista |
| 2. Herramientas | Tools custom contra BD: consultar inventario, consultar tarjetas previas, consultar correcciones, escribir tarjetas, exportar CSV | Todas las tools operan contra la BD, no contra archivos JSON | Los agentes leen/escriben directamente en BD |
| 3. Primer agente | **Agente Recurvo** con Claude Sonnet | **Cambio:** el plan original decía "Agente vocabulario con Kimi K2". La prueba demostró que Kimi K2 falla en traducciones y sílabas. Para tarjetas (material impreso) se usa Claude Sonnet | Genera tarjetas U03 como prueba |
| 4. Validación | Comparar tarjetas generadas vs. tarjetas U03 existentes (hechas manualmente) | **Nuevo paso.** Antes de avanzar, verificar que el agente produce tarjetas al nivel del trabajo manual | Calidad validada |
| 5. Segundo agente Fase 1 | Agente Gramatips (mismo patrón que Recurvo) | Sin cambios | Fase 1 con 2 de 3 agentes |
| 6. Tercer agente Fase 1 | Agente Estrategias | Sin cambios | Fase 1 completa |
| 7. Primer agente Fase 2 | Agente de sección Vocabulario (consume tarjetas del Recurvo) | **Cambio:** antes no existía la separación Fase 1/Fase 2 | Genera explotación didáctica con tarjetas ya listas |
| 8. Cadena completa | Todos los agentes de Fase 2 + orquestador + verificador | Sin cambios | Genera unidad completa |
| 9. Feedback | Interfaz de corrección, almacenamiento, inyección | **Subido de prioridad:** el plan original lo ponía en paso 6, pero es más valioso implementarlo antes de producción | El sistema aprende |
| 10. Producción | Generar U04-U09 | Sin cambios | Contenido real |

### Dependencias críticas

```
Paso 1 (infra) → Paso 2 (tools) → Paso 3 (Recurvo) → Paso 4 (validación)
                                                            ↓
                                           Paso 5+6 (otros agentes Fase 1)
                                                            ↓
                                           Paso 7 (primer agente Fase 2)
                                                            ↓
                                           Paso 8 (cadena) → Paso 9 (feedback) → Paso 10 (producción)
```

---

## 5. PREGUNTAS PENDIENTES (por resolver antes de implementar)

### 5.1 Sobre el agente Recurvo

1. ~~**¿Dónde se guardan las tarjetas generadas?**~~ **RESUELTO.** En la BD (tabla `tarjetas_vocabulario`). El CSV para InDesign (`datos/tarjetas/UXX-vocabulario.csv`) se exporta desde la BD bajo demanda. No hay JSON intermedio como almacenamiento.

2. ~~**¿Los campos 19-21 (unidad, estado, unidad_origen) son correctos?**~~ **RESUELTO.** Confirmados como correctos. Campos de gestión interna, no aparecen en la tarjeta impresa.

3. ~~**¿Quién decide qué vocabulario es "enseñable"?**~~ **RESUELTO.** El criterio principal es el nivel: si una palabra está por encima de lo que el estudiante A1.1 puede conocer, es candidata a tarjeta. El agente propone basándose en este criterio de nivel, el editor decide.

4. ~~**¿CSV dentro del JSON o separado?**~~ **RESUELTO.** CSV exportado desde BD: `datos/tarjetas/UXX-vocabulario.csv`. No hay JSON de almacenamiento.

### 5.2 Sobre el sistema de feedback

5. ~~**¿Dónde se almacenan las correcciones?**~~ **RESUELTO.** En la BD (nueva tabla `correcciones` en Neon PostgreSQL). Consistente con la decisión BD-first (sección 2B). El editor califica actualmente en VSCode consultando la BD; en el futuro, mediante interfaz dedicada.

6. ~~**¿Cómo califica el editor?**~~ **RESUELTO.** Actualmente: el editor revisa en VSCode y registra correcciones directamente en la BD (tipo de error + valor original + valor corregido). Futuro: interfaz dedicada para calificación. Categorías: aprobado / corregido + tipo de error (traducción, sílaba, regla, omisión, otro).

### 5.3 Sobre la arquitectura

7. ~~**¿Los agentes de Fase 1 comparten el mismo Crew o son Crews separados?**~~ **RESUELTO.** Un solo Crew con `Process.parallel`. Los 3 agentes son independientes entre sí, CrewAI gestiona la ejecución paralela, y si uno falla queremos investigar antes de continuar (Fase 2 necesita los 3 outputs).

---

## FUENTES

### CrewAI
- **Memory:** [docs.crewai.com/concepts/memory](https://docs.crewai.com/concepts/memory)
- **Tools:** [docs.crewai.com/concepts/tools](https://docs.crewai.com/concepts/tools)
- **Multi-LLM:** [docs.crewai.com/concepts/llms](https://docs.crewai.com/concepts/llms)

### Arquitectura BD-first (sección 2B)
- **Google Cloud — Choose your agentic AI architecture components:** [cloud.google.com](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components)
- **AWS — Key components of a data-driven agentic AI application:** [aws.amazon.com](https://aws.amazon.com/blogs/database/key-components-of-a-data-driven-agentic-ai-application/)
- **Microsoft — Data architecture for AI agents:** [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/data-architecture-plan)
- **Anthropic — Context Engineering:** [anthropic.com](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

### Proyecto
- **Prueba comparativa 3 modelos:** Resultados en `scripts/resultados_prueba/`
- **Arquitectura dos fases:** `diseno/sistema-agentes-propuesta.md` (actualización 2026-03-15)

---

*Documento creado: 2026-03-15*
*Versión: 1.1 — BD como fuente de verdad (sección 2B), agente Recurvo con inputs/outputs BD-first, 7 idiomas (TR añadido), combos, preguntas 1-6 resueltas*
