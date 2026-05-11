# Reglas operativas — Fase 2 Reciclaje

> Criterios de decisión para la construcción automatizada de `nc1-reciclaje.json`. Este archivo es la fuente única de verdad para los scripts y para los LLMs que trabajen en esta fase.

---

## 1. Criterios de agrupación y naming de hilos

### 1.1 Un hilo por contenido atómico

Cada hilo representa **un único contenido identificable** del curso. El criterio de atomicidad es:

- **Vocabulario:** un hilo por `campo_semantico`. Si el inventario tiene "Países hispanohablantes" y "Nacionalidades" como campos distintos, son dos hilos distintos. Nunca se agrupan dos campos en un hilo.
- **Gramática:** un hilo por punto gramatical tal como aparece en `nc1-curso.json` (ej. "Artículos determinados", "Presente de indicativo regular"). Si un punto se subdivide en el libro, se mantiene la granularidad del índice editorial.
- **Comunicación:** un hilo por función comunicativa (ej. "Saludar", "Pedir y dar información personal").
- **Estrategia:** un hilo por estrategia de aprendizaje.

### 1.2 Naming obligatorio

El `titulo` del hilo es **siempre** el nombre canónico del contenido:

| Nivel | Fuente del nombre |
|---|---|
| `mapa` | Texto literal de `nc1-curso.json` (campo `vocabulario`, `gramatica`, `comunicacion`, etc.) |
| `auto` | Valor de `campo_semantico` en el inventario, literalmente |

**Prohibido:**
- Nombres inventados o paraguas genéricos ("Léxico de aula", "Contenido lingüístico").
- Combinar dos contenidos distintos en un título ("Países hispanohablantes y nacionalidades" si son campos distintos).

**Permitido:** fusionar en un hilo solo si en `nc1-curso.json` el contenido aparece como una única entrada. Si el inventario usa un nombre distinto para el mismo campo, el nombre canónico es el de `nc1-curso.json` (es el índice editorial del curso).

### 1.3 ID del hilo

Formato: `hilo-<slug-del-titulo>` donde slug = minúsculas, sin tildes, espacios → guiones.

Ejemplos:
- "Países hispanohablantes" → `hilo-paises-hispanohablantes`
- "Nacionalidades" → `hilo-nacionalidades`
- "Presente de indicativo regular" → `hilo-presente-indicativo-regular`

---

## 2. Criterios de acciones por evento

Cada aparición de un contenido en una unidad genera un evento con una `accion`. La acción describe **qué hace pedagógicamente esa unidad con ese contenido**:

| Accion | Cuándo aplicar |
|---|---|
| `introduce` | Primera vez que el contenido aparece en el curso. Solo puede haber un evento `introduce` por hilo. |
| `amplia` | El contenido ya fue introducido y la unidad añade nuevos elementos del mismo campo (más vocabulario, más formas verbales, más funciones). |
| `aplica` | La unidad usa el contenido en un contexto nuevo (nueva destreza, nueva tarea) sin añadir elementos nuevos. |
| `sistematiza` | La unidad organiza o formaliza explícitamente lo que ya se ha trabajado de forma dispersa (cuadros de resumen, reglas explícitas). |
| `contrasta` | La unidad trabaja el contenido en oposición con otro (ej. tú/usted, ser/estar, pretérito/imperfecto). |

**Regla de desempate:** si una unidad hace dos cosas (ej. amplía Y sistematiza), usar la acción dominante. Si ambas tienen el mismo peso, preferir `amplia` sobre `sistematiza`, `aplica` sobre `contrasta`.

### 2.1 Impacto

| Impacto | Criterio |
|---|---|
| `alto` | El contenido es un objetivo central de la unidad (aparece en título, en cuadro gramatical principal, o en bloque de vocabulario principal). |
| `medio` | El contenido es secundario o de apoyo en la unidad. |
| `bajo` | Mención puntual, ejercicio de repaso, nota al margen. |

---

## 3. Lógica del script `regenerar_reciclaje_mapa.py`

El script lee `nc1-curso.json` y genera hilos `nivel_analisis: "mapa"` siguiendo estas reglas:

### 3.1 Campos que se procesan

| Campo en nc1-curso.json | tipo de hilo generado |
|---|---|
| `vocabulario` (lista de strings) | `vocabulario` |
| `gramatica` (lista de strings) | `contenido_gramatical` |
| `comunicacion` (lista de strings) | `estrategia` |
| `pronunciacion_ortografia` | `contenido_gramatical` |
| `para_aprender` | `estrategia` |

### 3.2 Construcción de eventos

Para cada contenido en cada unidad:
1. Buscar si ya existe un hilo con ese título (normalizado). Si existe → nuevo evento con acción `amplia` (o la que corresponda). Si no existe → crear hilo con evento `introduce`.
2. La `descripcion` del evento es el texto literal del contenido en nc1-curso.json.
3. El `impacto` por defecto es `alto` para vocabulario y gramática principal, `medio` para el resto. Si el valor por defecto es incorrecto, se corrige la lógica del script en `CAMPO_IMPACTO`, no el JSON generado.

### 3.3 Qué NO hace el script

- No infiere si una acción es `aplica` vs `amplia` automáticamente para el nivel mapa: por defecto usa `amplia` para apariciones posteriores. Un LLM revisor puede corregir las acciones en una segunda pasada con los criterios de §2.
- No genera eventos para `cultura` ni `destrezas` (son contenido temático, no contenido lingüístico reciclable).
- El `impacto` por defecto (alto/medio según el campo) viene del script y no se retoca en el JSON. Si el impacto por defecto es incorrecto, se corrige la lógica del script, no el JSON generado.

---

## 4. Lógica del script `regenerar_reciclaje_vocabulario.py`

El script lee los inventarios aprobados en main y genera hilos `nivel_analisis: "auto"` por cada `campo_semantico` único.

**Estado actual:** fase 2 pausada (decisión 36, v10.108). `scripts/integrar_unidad.py` no regenera reciclaje por defecto desde v10.108d; la regeneración queda detrás del flag explícito `--regenerar-reciclaje`. Cuando fase 2 se reactive, la invocación volverá a ser parte del flujo por defecto o se replanteará según el modelo nuevo.

Lógica: primer aparición → `introduce`, siguientes → `amplia` (si principal/recurrente) o `aplica` (si solo comprensión). Ver código en `scripts/regenerar_reciclaje_vocabulario.py`.

---

## 5. Relación entre niveles mapa y auto

- El nivel `mapa` cubre **todos los tipos** de contenido (vocabulario, gramática, comunicación, estrategia).
- El nivel `auto` cubre **solo vocabulario** (lo que se puede extraer automáticamente de los inventarios).
- Para un mismo campo semántico pueden existir un hilo `mapa` y un hilo `auto` en paralelo. No se fusionan: cada uno tiene su propia granularidad y fuente.
- El dashboard muestra ambos niveles en la misma timeline para comparar.

---

## 6. Casos resueltos (casebook)

| Caso | Decisión |
|---|---|
| "Países hispanohablantes y nacionalidades" fusionados en un hilo mapa | Error. Son campos distintos en el inventario → dos hilos separados: "Países hispanohablantes" y "Nacionalidades". |
| "Léxico de aula" como nombre de hilo | Error. Nombre inventado. Usar el campo semántico real ("Para la clase", "Objetos de clase", o "Aula y objetos de la clase" si la fuente los agrupa bajo ese nombre). |
| Hilo mapa para `cultura` | No se genera. Cultura es contenido temático, no lingüístico reciclable en el sentido de esta fase. |