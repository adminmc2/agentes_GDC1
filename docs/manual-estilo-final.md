# Manual de estilo — capa `final/`

> Manual de estilo aplicable a la capa `unidades/**/final/*.md` (versión editorial limpia y human-readable, apta para maquetación InDesign y para ajustes editoriales finales en repo A).
>
> Esta es la **fuente única de las reglas**. La activación automática se hace mediante `.claude/rules/final-style.md` (path-scoped).
>
> Para reglas que aplican a la capa `propuesta/` (fuente editorial rica con metanotas), este manual NO aplica.

---

## 1. Propósito y alcance

### Qué cubre

- Reglas ortográficas (RAE).
- Reglas tipográficas (comillas, raya, cursivas, mayúsculas).
- Convenciones canónicas del proyecto (categorías de tarjetas, nomenclatura).
- Lenguaje no marcado por género.
- Terminología homogeneizada.
- Estructura de la versión final.

### A qué archivos aplica

Cualquier archivo `.md` que matchee el patrón `unidades/**/final/*.md`:
- Las 6 secciones canónicas (vocabulario, gramática, comunicación, destrezas, cultura, evaluación).
- El itinerario imprimible (`itinerario.md`) cuando exista.
- Cualquier otro archivo futuro en esa carpeta.

### Lo que NO redefine este manual

La **formulación de objetivos** (cómo se redacta un objetivo general de sección o un objetivo de bloque: verbos validados/prohibidos, naturaleza por sección, anti-aditivo, etc.) se rige por `docs/formulacion-objetivos.md`. Este manual no redefine ese criterio.

### A qué NO aplica

- `unidades/**/propuesta/*.md` → fuente editorial rica con metanotas, trazabilidad de proceso, briefs, etc. Tiene sus propias reglas (las del repo B).
- `unidades/**/recursos/**` → CSVs de tarjetas, materiales complementarios.
- `unidades/**/fuente/**` → PDF del libro.
- Archivos auxiliares del sistema (`docs/`, `scripts/`, `web/`, etc.).

### Fuentes oficiales

| Sigla | Obra | Año |
|---|---|---|
| **OLE** | *Ortografía de la lengua española* (RAE / ASALE) | 2010 |
| **DPD** | *Diccionario panhispánico de dudas* (RAE / ASALE) | 2005, actualizada |
| **LEE** | *Libro de estilo de la lengua española* (RAE) | 2018 |
| **DLE** | *Diccionario de la lengua española* (RAE / ASALE) | edición vigente |

Las reglas de este manual citan la fuente cuando proceden de la normativa oficial. Las que no llevan cita son **convenciones del proyecto** (decisiones acordadas con el autor durante la redacción del sistema).

### Herramientas auxiliares de consulta (NO oficiales)

Para validar la existencia o forma de una palabra concreta durante el trabajo editorial, se puede consultar:

- `https://rae-api.com` — API no oficial que expone consultas al DLE. Útil como vía rápida de verificación léxica, pero **NO es fuente normativa**: la autoridad sigue siendo el DLE de la RAE/ASALE (tabla anterior).

Cualquier discrepancia entre una herramienta auxiliar y una fuente oficial se resuelve a favor de la fuente oficial.

---

## 2. Estructura mínima de un archivo `final/<seccion>.md`

Lo que **se queda**:
- Apertura: `Insignia gamificada` + `Objetivo` + `Imprimir ficha X.Y—...` + `Insignia y obtención` con su párrafo.
- Headers de bloque: `### Ejercicios X-Y` o `### Ejercicio X` (solo el rango de ejercicios; sin "BLOQUE", sin páginas, sin dos puntos, sin título descriptivo).
- Cada bloque: `Objetivo` + rótulos imperativos en mayúsculas + cuerpo con instrucciones al docente.
- `ENTREGA DE INSIGNIA` con su párrafo canónico.

Lo que **NO va** en `final/`:
- Trazabilidad del objetivo (referencia + cita + desglose).
- Metanota del bloque (pautas aplicadas, análisis JSON, decisiones).
- Apéndice "Técnicas y dinámicas usadas".
- Sección "Fichas" con descripción de insignia / tarjeta.
- Brief detallado de píldora.
- Spec textual de tarjeta cara A/B.
- Brief de canción + registro de estilos musicales.
- Cabecera del archivo (`# UXX — ...`) y nota inicial.
- Cabecera de doble página (`## DOBLE PÁGINA N (pp. X-Y)`).
- Separadores horizontales (`---`) entre bloques (los headers `###` ya separan).
- Conteo automático de palabras.
- **Instrucciones de preparación / impresión de tarjetas** (líneas tipo *"Preparar Tarjetas de Vocabulario - X (10 tarjetas, cara frontal solo imagen…)"*). La impresión y disponibilidad de las tarjetas vive en la **estación de servicio del itinerario imprimible**, no en el cuerpo del docente de cada bloque. En `final/` nunca se le pide al docente preparar/imprimir tarjetas — se asume que están disponibles desde el inicio de la unidad.

### 2.1 Convenciones específicas por sección

Algunas secciones llevan líneas obligatorias adicionales a la estructura mínima. Estas convenciones aplican siempre (no son opcionales).

#### Comunicación — referencia al vídeo de la unidad

Cada `unidades/U[X]/final/comunicacion.md` incluye, en el bloque 1 (después del objetivo de bloque y antes de las líneas *Imprimir*), la línea:

> *Buscar Vídeo de comunicación **unidad X***

Donde X es el número de la unidad. Cada unidad tiene su vídeo de comunicación correspondiente (U1→vídeo 1, U2→vídeo 2…). La línea avisa al docente del material audiovisual que debe localizar antes de la sesión.

**Formato canónico:**
- *Buscar* con mayúscula inicial.
- *Vídeo* con mayúscula y tilde.
- *unidad X* en minúscula y negrita (§9.2).
- Sin dos puntos, sin guion al final.

#### Comunicación — tarjetas de estrategia

Las tarjetas de estrategia de Comunicación se referencian con el formato canónico:

> *Imprimir tarjeta de estrategia—[destreza]—*[título]**

Ejemplo: *Imprimir tarjeta de estrategia—interacción oral—*Saludar y despedirse**.

La destreza va en minúscula y precede al título; el título va en cursiva. Tres componentes separados por guion largo (em-dash). La línea va al inicio del bloque donde se usa la tarjeta, junto al resto de líneas *Imprimir*.

#### Comunicación — referencias a las caras de la tarjeta en el cuerpo

Las etiquetas *CARA A* / *CARA B* son convención editorial interna. **NO aparecen en el cuerpo del docente.** En el cuerpo, las caras se nombran **por su contenido**:

- *"la cara del saludo en cuatro pasos"* (no *"CARA A (saluda en cuatro pasos)"*)
- *"la cara de las micro-funciones"* (no *"CARA A"*)
- *"la cara del diálogo modelo"* (no *"CARA B"*)
- *"la cara de los trucos comunicativos"* (no *"CARA B"*)

Las etiquetas internas se reservan a la spec textual de la tarjeta (que no va en `final/` por ser material de autoría interna). Regla equivalente a la convención canónica de repo B en `tarjetas-estrategia-comunicacion-pautas.md` §1.

#### Evaluación — conexión a unidad siguiente

Cada `unidades/U[X]/final/evaluacion.md` cierra dentro del rótulo *AUTOEVALUACIÓN Y CIERRE* con una **sola frase escueta** de conexión a la unidad siguiente. Formato canónico:

> *Cierre con la conexión a la **unidad X+1**: en la próxima unidad [síntesis breve del contenido nuclear].*

**Formato canónico:**
- *Cierre* como verbo del docente.
- *unidad X+1* en minúscula y negrita (§9.2).
- **Una sola frase**, sin enumeración exhaustiva — síntesis del contenido nuclear en tres a cinco elementos.
- Es la **única referencia anticipatoria permitida** en cualquier `final/`. En el resto de secciones aplica el bullet de §10.1 sobre referencias anticipatorias.

**Casos observados.**
- U1E: *"Cierre con la conexión a la **unidad 2**: en la próxima unidad hablarán de los países hispanohablantes, ampliarán las nacionalidades al plural y los números hasta el 100."*
- U3E: *"Cierre con la conexión a la **unidad 4**: en la próxima unidad hablarán de alimentos y comidas, aprenderán a expresar lo que les gusta con gustar y a usar hay para hablar de cantidades."*

---

## 3. Acentuación diacrítica

### 3.1 Regla general (OLE 2010, §3.4.3.2)

Llevan tilde cuando son **interrogativos o exclamativos**, en estilo directo o indirecto. No llevan tilde cuando son **relativos, conjunciones o adverbios** sin valor interrogativo / exclamativo.

| Palabra | Con tilde (interrogativo / exclamativo) | Sin tilde (relativo / conjunción) |
|---|---|---|
| qué / que | *¿**Qué** ves?* · *Pregunte **qué** edad tienen* | *Pida **que** abran el libro* · *la palabra **que** se repite* |
| cómo / como | *Explique **cómo** se hace* | *Así es **como** se hace* · *plantearlo **como** producción* |
| dónde / donde | *Pregunte **dónde** está* · *Señalando **dónde** se ve la información* | *Voy **donde** estás* |
| quién / quien | *¿**Quién** tiene doce años?* | *A **quien** tiene a un lado* |
| cuándo / cuando | *Pregunte **cuándo** llega* | *Cuando llegue, avise* |
| cuánto / cuanto | *¿**Cuántos** años tiene?* | *Lleve **cuanto** quiera* |
| cuál / cual | *¿**Cuál** es la nacionalidad?* | (raro como relativo) |

### 3.2 Caso límite — verbos de comunicación + adverbio

Construcciones como *"señalando dónde está"*, *"pídales que señalen dónde"* admiten ambas interpretaciones:
- Como **interrogativa indirecta** (con tilde): *"señalando (la respuesta a la pregunta) dónde está"*.
- Como **relativa** (sin tilde): *"señalando el lugar donde está"*.

**Convención del proyecto**: en estos casos límite, **con tilde** (interpretación interrogativa indirecta).

### 3.3 Tildes diacríticas monosilábicas (OLE 2010, §3.4.3.1)

| Palabra | Con tilde | Sin tilde |
|---|---|---|
| sé / se | *Lo **sé*** (verbo *saber* o *ser*) | *Se va* (pronombre) |
| dé / de | *Que **dé** una pasada* (verbo *dar*) | *Una pasada **de** repaso* (preposición) |
| sí / si | *Diga ***sí*** (afirmación, pronombre reflexivo) | *Si quiere, hágalo* (condicional) |
| más / mas | *No hace falta **más*** (cuantitativo) | *Quería, **mas** no pudo* (conjunción adversativa, hoy en desuso) |
| él / el | ***Él** lo dice* (pronombre) | ***El** libro* (artículo) |
| mí / mi | *A **mí*** (pronombre) | ***Mi** nombre* (posesivo) |
| tú / tu | ***Tú** decides* (pronombre) | ***Tu** nombre* (posesivo) |
| té / te | ***Té** (bebida)* | *Yo **te** veo* (pronombre) |

### 3.4 *Solo* — adverbio sin tilde (OLE 2010, §3.4.3.3)

Desde la *Ortografía* de 2010, **se eliminó la tilde diacrítica de *solo*** cuando funciona como adverbio (equivalente a *únicamente*). La RAE permite mantenerla solo en casos de ambigüedad real.

- ✅ *solo imagen* (adverbio, sin tilde).
- ✅ *solo escuchan* (adverbio, sin tilde).
- ✅ *un libro solo* (adjetivo = *en soledad*, sin tilde).

---

## 4. Mayúsculas y minúsculas

### 4.1 Regla general española (OLE 2010, §4.2)

Llevan mayúscula:
- La primera letra de la oración (tras punto, tras signo de cierre `?!` que cierra oración).
- Los nombres propios.

NO llevan mayúscula:
- Los nombres comunes (incluidos los que en inglés sí llevan: meses, días, idiomas, gentilicios, conceptos abstractos).
- Las palabras dentro de un título salvo la primera y los nombres propios.

### 4.2 Convenciones del proyecto (canónicas en `final/`)

Hay **excepciones convenidas** que sobrescriben la regla general por motivos editoriales/pedagógicos:

| Elemento | Forma canónica | Ejemplo |
|---|---|---|
| Rótulos imperativos del docente | TODO EN MAYÚSCULAS | `PRESENTE A KATRINA Y RAFA` |
| Etiquetas estructurales del cuerpo | Mayúscula inicial | `Insignia gamificada` · `Objetivo` · `Insignia y obtención` · `ENTREGA DE INSIGNIA` |
| Lemas de insignia entre exclamaciones | TODO EN MAYÚSCULAS — uniforme en todas las menciones (etiqueta de ficha, párrafos, headers) | `¡MUCHO GUSTO!` · `¡HOLA!` (nunca `¡Mucho gusto!`) |
| Headers de bloque | **Solo el rango de ejercicios**, sin título descriptivo | `### Ejercicios 1-2` · `### Ejercicio 5` · `### Ejercicios 5-9` |
| Referencias a unidades **dentro de párrafo** | minúscula | `los países hispanohablantes que conocieron en la unidad 0` |
| Referencias a unidades **dentro de rótulo en mayúsculas** | MAYÚSCULA (excepción por el rótulo) | `RECUPERE EL ABECEDARIO DE LA UNIDAD 0` |
| Categorías canónicas de tarjetas | Mayúscula inicial en `Tarjetas` y `Vocabulario` o `Destreza` | `Tarjetas de Vocabulario - <campo>` · `Tarjetas de Destreza - <qué destreza> - <nombre>` |

### 4.3 Calcos del inglés a evitar

| Forma incorrecta (calco inglés) | Forma correcta (español) |
|---|---|
| `Imprimir ficha 1.1—Insignia: ¡Mucho gusto!` | `Imprimir ficha 1.1—insignia: ¡Mucho gusto!` (insignia = nombre común) |
| `Tarjetas de Vocabulario - Objetos de la Clase` | `Tarjetas de Vocabulario - objetos de la clase` (campo semántico = nombre común) |
| `Nombre del Bloque` (cada palabra capitalizada) | `Nombre del bloque` (solo la primera) |

### 4.4 Gentilicios e idiomas

Siempre en minúscula (OLE 2010, §4.2.4.10):
- ✅ *español, española, francés, francesa, inglés, inglesa, brasileño, brasileña, colombiano, colombiana, argentino, argentina*.

---

## 5. Prefijos (OLE 2010, §5.4.2)

Los prefijos se escriben **unidos** a la base sin guion cuando la base es **una sola palabra** que empieza por consonante o vocal:

| Forma correcta | Forma incorrecta |
|---|---|
| `minidinámica` | ~~mini-dinámica~~ |
| `minidiálogos` | ~~mini-diálogos~~ |
| `prerredacción` | ~~pre-redacción~~ |
| `posdebate` | ~~pos-debate~~ |
| `multinivel` | ~~multi-nivel~~ |

**Excepciones que sí llevan guion** (OLE 2010, §5.4.2.3):
- Cuando la base es **mayúscula inicial** o **sigla**: `mini-USB`, `pro-OTAN`.
- Cuando la base empieza por **número**: `sub-21`.
- Cuando la base es una **palabra compleja** (varias palabras): `ex primer ministro` (separado, no `expri­mer ministro`).

---

## 6. Categorías canónicas del proyecto

### 6.1 Tarjetas

Formato canónico de mención en el cuerpo del docente:

| Tipo | Formato |
|---|---|
| Tarjetas de vocabulario | `Tarjetas de Vocabulario - <campo semántico en minúscula>` |
| Tarjetas de destreza | `Tarjetas de Destreza - <qué destreza> - <nombre>` |

Ejemplos:
- `Tarjetas de Vocabulario - objetos de la clase`
- `Tarjetas de Vocabulario - familia`
- `Tarjetas de Destreza - comprensión auditiva - escucha en tres modos`

**Tipografía del título individual de tarjeta.** Cuando el nombre concreto de una tarjeta (de destreza, de estrategia, de vocabulario nombrada) se **cita en el cuerpo del docente como referencia individual** — distinta de la mención canónica del tipo de la tabla anterior —, va siempre en cursiva con mayúscula inicial (título-case): *Caza el dato*, *Escucha en tres modos*, *Saludar y despedirse*, *Presentarse y datos personales*. Nunca en ALL CAPS — esa forma queda reservada a rótulos imperativos del docente y a lemas de insignia (§4.2).

### 6.2 Nomenclatura interna que NO debe aparecer en `final/`

| Nomenclatura interna | Razón | Sustituir por |
|---|---|---|
| `Caja 1`, `caja 1`, `Caja 2`, `caja 2` | Sistema de almacenamiento del equipo editorial, no lengua de aula | Reformular con el formato canónico de tarjetas (§6.1) |
| `BLOQUE 1`, `bloque 1`, `BLOQUE N` | Etiqueta estructural del proceso editorial | Referirse al contenido directamente (*"las tres estructuras iniciales"*, *"el primer ejercicio"*) |
| `cara A`, `cara B` | Convención editorial de tarjetas Caja 2 | Nombrar por contenido (*"la cara del diálogo modelo"*, *"la cara de las micro-funciones"*) |
| `R1`, `R2`, `R3`, `B1`, `B2`, `B3` | Códigos internos de planificación | No aparecen — son metainformación de proceso |

---

## 7. Lenguaje no marcado por género

### 7.1 Banco canónico de sustitución

Cuando el referente es genérico, usar formas no marcadas:

| Forma marcada (a evitar) | Forma no marcada (a usar) |
|---|---|
| compañero / compañera | la pareja · la otra persona · alguien · quien tiene al lado · quien participa |
| alumno / alumna | el estudiante · cada estudiante · el grupo · la clase |
| voluntario / voluntaria | persona voluntaria · quien se ofrezca · alguien del grupo |
| profesor / profesora | el docente · quien enseña |
| niño / niña | la persona joven · cada estudiante · el grupo (según contexto A1.1) |
| amigo / amiga | la persona · alguien (según contexto) |
| portador / portadora | quien lleva la tarjeta · quien tiene la tarjeta |

**Nota — cuantificación plural.** En plural cuantificado (*tres voluntarios*, *cuatro alumnos*), cuantificar la acción en lugar de las personas: *tres intervenciones* · *tres turnos* · *tres aportaciones*. Evita tanto el masculino genérico marcado como las metonimias forzadas.

### 7.2 Epicenos aceptados (no se sustituyen)

Términos cuyo género gramatical no marca el sexo del referente:
- ✅ *el docente* / *la docente*
- ✅ *el estudiante* / *la estudiante*

Estos se mantienen tal cual.

### 7.3 Excepciones

- **Personajes del libro con nombre propio**: se respeta el género del personaje tal como aparece (*Katrina es española*, *Rafa es argentino*).
- **Contenido lingüístico explícito de M/F**: en ejercicios que enseñan concordancia (ej. nacionalidades en columnas *chico* / *chica*), se respeta como contenido factual del libro.

---

## 8. Terminología homogeneizada

### 8.1 Banco canónico (recoge criterio #18 del repo B)

| Concepto | Forma canónica | Formas a evitar |
|---|---|---|
| Tarea del libro o bloque editorial | `ejercicio` (palabra completa) | ~~ej.~~ · ~~act.~~ · ~~actividad~~ · ~~actividades~~ — vetada también para bloques editoriales y referencias internas, no solo para tareas numeradas. Excepción: nombres propios de productos SGEL (`Actividades Extra`, `Actividad global 1/2` del Cuaderno de juegos) y nombres de archivos físicos (`actividades_extra.pdf`). |
| Material sonoro del libro | `pista` (palabra completa) | ~~audio~~ · ~~audición~~ (`escucha` solo como destreza CO) |
| Páginas del libro | `página` / `páginas` (palabra completa) | ~~p.~~ · ~~pp.~~ · ~~pág.~~ |
| Docente | `docente` | ~~profesor~~ · ~~profesora~~ · ~~prof.~~ |
| Estudiante | `estudiante` | (forma única; epiceno aceptado) |
| Elementos visuales del libro | `foto` (fotografía real) · `dibujo` (no fotográfico) · `ilustración` (mixto) · `imagen` (paraguas) | ~~fotografía~~ |
| Elementos enmarcados | `cuadro` = elemento del libro · `tabla` = filas/columnas · `recuadro` = bordeado · `caja` reservado a tarjetas | (distinción semántica) |
| Agrupaciones de aula | `clase` = todo el grupo · `grupos` / `pequeños grupos` = ad hoc · `parejas` = de 2 · `aula` = contenedor físico · `plenaria` = formato | ~~equipo~~ (salvo dinámica concreta tipo concurso) |
| Píldora | `píldora` (con tilde) | ~~pildora~~ |
| Diapositiva | `diapositiva` | ~~slide~~ (solo en specs técnicos internos) |
| Tarjeta | `tarjeta` | (forma única) |
| Hipótesis o conjetura del grupo recogida por el docente | `respuestas` · `propuestas` | ~~apuestas~~ |
| Personas que intervienen oralmente en plenaria o puesta en común | `intervenciones` · `turnos` · `aportaciones` | ~~voces~~ |

### 8.2 Tiempos en el cuerpo

Los tiempos prescriptivos **no aparecen en el cuerpo de los rótulos** (cuántos minutos dura cada paso). Los tiempos orientativos viven en metanotas del proceso editorial (`propuesta/`), no en `final/`.

### 8.3 Sin siglas — palabras completas

En el cuerpo del docente, las categorías lingüísticas y didácticas se escriben **siempre con la palabra completa**, no con siglas abreviadas. Las siglas convencionales del lenguaje editorial interno (M, F, CO, CL, EE, EO, L1, etc.) son metainformación del proyecto, no léxico de aula.

- ❌ *"el contraste **M/F** en estos nombres"*
- ✅ *"el contraste entre **masculino** y **femenino** en estos nombres"*

Ejemplos análogos:
- `M / F` → `masculino / femenino` (o `masculino y femenino`).
- `CO` → `comprensión oral`.
- `CL` → `comprensión lectora`.
- `EE` → `expresión escrita`.
- `EO` → `expresión oral`.
- `L1` → `lengua materna del estudiante` (o `su lengua`).

**Excepción**: pares mínimos ortográficos (`g/j`, `b/v`, `h/sin h`) NO son siglas que sustituyan palabras — son la representación literal de la oposición ortográfica. Se mantienen tal cual.

---

## 9. Convenciones tipográficas

### 9.1 Cursivas (citas, preguntas y habla)

Se usan cursivas (`*texto*`) **sin comillas adicionales** para:

- **Preguntas o instrucciones que el docente dice en voz alta** a la clase: `dígales: *En la primera página hay un bocadillo grande con una palabra para saludar. ¿Qué creéis que dice?*`.
- **Citas específicas del libro** (textos, diálogos, enunciados): `el ejemplo del libro (*Me llamo Pedro y soy de España, soy español*)`.
- **Ejemplos de habla del estudiante**: `*¡Hola!, me llamo… Soy de…*`.
- **Estructuras lingüísticas formalizadas**: `*me llamo, soy de, tengo X años*`.
- **Palabras o expresiones del libro citadas explícitamente**: `*el portátil, la mochila*`.
- **Diálogos modelo**: `*Veo, veo / ¿Qué ves? / Una cosita...*`.

⚠ **NO usar comillas dobles ni latinas dentro de la cursiva.** La cursiva es suficiente; las comillas son redundantes y rompen la convención del proyecto.

- ✅ `dígales: *¿Qué creéis que dice?*`
- ❌ `dígales: *"¿Qué creéis que dice?"*`
- ❌ `dígales: «¿Qué creéis que dice?»`

### 9.2 Negrita (referencias numeradas del libro + nombres de insignia y unidad)

Se usa **negrita** (`**texto**`) **siempre** para:

#### Referencias numeradas concretas del libro

| Tipo de referencia | Ejemplo |
|---|---|
| Pistas de audio | `Ponga la **pista 7**` |
| Ejercicios individuales | `Para el **ejercicio 6**` |
| Rangos de ejercicios | `Pase a los **ejercicios 1-2**` |
| Páginas individuales | `Pida que abran la **página 12**` |
| Rangos de páginas | `**Páginas 12-13**` |

**Excepción — referencias anafóricas sin número**: no van en negrita.

- ❌ ~~uno de los diez del **ejercicio anterior**~~
- ✅ `uno de los diez del ejercicio anterior` (sin negrita; no es referencia numerada específica)

#### Nombres de insignia (el lema entre exclamaciones)

| Tipo | Ejemplo |
|---|---|
| Lema de la insignia en cuerpo de párrafo o etiqueta | `recibirán la insignia **¡MUCHO GUSTO!**` · `Imprimir ficha 1.1—insignia: **¡MUCHO GUSTO!**` |

⚠ **Solo el lema** va en negrita. La palabra `insignia` suelta o cualquier referencia anafórica (`esta insignia`, `la insignia`) **NO** va en negrita.

- ❌ ~~recibirán la **insignia** ¡MUCHO GUSTO!~~
- ✅ `recibirán la insignia **¡MUCHO GUSTO!**`

#### Nombres de unidad

| Tipo | Ejemplo |
|---|---|
| Referencia a unidad específica en párrafo | `los países que conocieron en la **unidad 0**` |
| Referencia a unidad específica en párrafo | `palabras de la **unidad 0**` |

⚠ Va en negrita **y** en minúscula cuando aparece dentro de párrafo (regla §4.2). Dentro de rótulo en mayúsculas se queda en mayúsculas y sin negrita (es excepción del rótulo).

#### Avisos y enumeraciones

- **Avisos críticos al docente**: `**Antes de poner la pista**`.
- **Distinciones léxicas dentro de una enumeración**: `**Primera tanda:** ...`. `**Segunda tanda:** ...`.

Sin abusar — la negrita pierde fuerza si se usa demasiado.

### 9.3 Raya (—) como inciso

La raya se usa **sin espacios interiores** y **con espacios exteriores** (OLE 2010, §6.4.2):

- ✅ `No formalice la distinción de género —se trabaja en gramática—, pero pídales que se fijen...`
- ❌ `No formalice — se trabaja en gramática —, pero...` (espacios interiores incorrectos)

### 9.4 Raya en etiquetas compactas

En etiquetas tipo `Imprimir ficha 1.1—insignia: ¡Mucho gusto!`, la raya puede usarse **sin espacios** por compactación visual. Es convención del proyecto.

### 9.5 Paréntesis vs dos puntos vs rayas en enumeraciones y citas

#### Enumeraciones

- **Dos puntos (:)** cuando la enumeración está **anunciada** por un cardinal o sintagma anticipador (*"cuatro palabras"*, *"los cinco objetos"*, *"las tres letras"*). Reordenar la frase si hace falta para que la enumeración vaya al final con dos puntos. Ejemplo: *"pida que las escriban en el cuaderno: jamón, agua, Honduras, hospital"*.
- **Paréntesis ( )** cuando la enumeración es **inciso accesorio o aclaratorio** que se puede omitir sin alterar la oración principal. Ejemplo: *"las tres preguntas tipo (¿Con g o con j? ¿Con b o con v? ¿Con h o sin ella?) son importantes para esclarecer entre dos opciones"*.
- **Rayas (— —)** cuando la enumeración es **inciso importante** pero no anunciado, con más peso que un paréntesis.

Criterio práctico: si la enumeración es el contenido principal anunciado, dos puntos. Si es aclaración accesoria al hilo del párrafo, paréntesis. Si es contenido relevante intercalado, rayas.

#### Citas textuales del libro

Las citas textuales del libro (modelo, diálogo, ejemplo, frase del enunciado) introducidas por un anuncio descriptivo (*"el modelo del libro"*, *"el ejemplo del libro"*, *"el diálogo modelo del ejercicio X"*) se introducen con **dos puntos**, NO con paréntesis. La cita va siempre en **cursiva** (regla §9.1) y con **mayúscula inicial** porque es oración completa (OLE §4.2.6).

- ❌ *"Siguiendo el modelo del libro (*¡Hola!, me llamo… Soy de… Tengo… años*), en lugar de plantearlo..."*
- ✅ *"Siguiendo el modelo del libro: *¡Hola!, me llamo… Soy de… Tengo… años*. En lugar de plantearlo..."*

Si la frase principal continúa tras la cita, se reformula en dos oraciones separadas por punto, no se prolonga el inciso parentético.

---

## 10. Voz del cuerpo del docente y criterios editoriales de redacción

El cuerpo del docente vive en **lengua de aula con acción concreta**. No contiene metadiscurso sobre el sistema editorial.

### 10.1 Lo que NO debe aparecer

- Anuncios sobre el corpus: *"el set acaba de ampliarse"*, *"esta unidad inaugura...".*
- **Resúmenes-balance de cierre de sección**: frases que recapitulan lo aprendido en clave grandilocuente o de balance editorial. Ejemplos a evitar: *"el círculo está cerrado"*, *"en una sola doble página han aprendido a…"*, *"el set queda activado"*, *"con esto cerramos el bloque de…"*. No describen acción del docente ni aportan andamiaje al aula: solo cierran retóricamente lo que la propia secuencia de ejercicios ya cierra. Fuera del cuerpo.
- Decisiones del equipo editorial: *"hemos decidido..."*, *"el equipo propone..."*.
- Referencias a otras secciones del propio sistema MD: *"como ya vimos en la metanota..."*.
- **Referencias anticipatorias a otra sección de la guía o del libro**: *"—el plural se trabaja en gramática—"*, *"—lo verán en comunicación—"*, *"—esto se cierra en evaluación—"*. El docente ya sabe que el libro tiene secciones; anunciar curricularmente lo que viene después es metadiscurso editorial. La intención didáctica de no abrir la regla en este punto se mantiene con la forma propositiva de §10.4 (*sin desarrollar la explicación detallada*, *sin formalizar la regla*).
- **Afirmaciones normativas redundantes sobre el libro**: *"La estructura obligatoria es siempre la del libro"*, *"Hay que seguir el orden del libro"*, *"Esto es lo que dice el libro"*. El docente ya sabe que el libro es la fuente; el cuerpo de los rótulos debe limitarse a la acción concreta sin recordatorios meta-editoriales.
- **Afirmaciones hiperbólicas, grandilocuentes o no verificables**: *"son las preguntas reales de cualquier hablante de español al escribir un nombre nuevo: las van a oír y a hacer toda la vida"*, *"este vocabulario les acompañará siempre"*, *"es la clave para…"*. No aportan valor lingüístico ni didáctico; son retórica de relleno. Si una afirmación no aporta valor lingüístico verificable, fuera del cuerpo. Sustituir por explicación funcional concreta (ej.: *"son importantes para esclarecer entre dos opciones"*).
- **Predicciones narrativas sobre la respuesta de la clase**: *"saldrá X"*, *"dirán Y"*, *"la clase responderá Z"*. Narran el resultado esperado en vez de indicar qué hace el docente para conducirlo. Sustituir por andamiaje activo (*guíelos para que…*, *conduzca a…*, *apoye las respuestas que aparezcan…*). Se exceptúan las bifurcaciones operativas con instrucción para cada rama (*si sale X, confírmelo; si no, redirija con Y*).
- **Prescripción de decisiones libres del docente**: paletas de colores específicas (*a · rojo · e · amarillo · i · verde…*), mapeos concretos de items intercambiables (combos de tarjetas, asignación de roles, orden de turnos), mecánicas detalladas cuya secuencia exacta no es obligatoria pedagógicamente. La guía orienta el qué y el para qué; el docente decide el cómo concreto cuando la elección no carga peso didáctico. Sustituir por instrucción abierta: *"asigne un color distinto a cada vocal"*, *"reparta las tarjetas en parejas"*, *"haga dos o tres rondas"*.
- **Respuestas de los ejercicios cuando ya están visibles en la imagen del libro del alumno**: ejemplo: *"completan los huecos con la letra correcta (J / j, V / v, H / con h)"* — el paréntesis es redundante porque el docente ya ve las respuestas en su material y el alumno trabaja sobre el libro. Solo se incluyen respuestas en el cuerpo del docente si hay algo específico que destacar (ej.: ítem con error frecuente, opción ambigua, ítem que el docente debe corregir explícitamente). Por defecto, fuera.

### 10.2 Filtro de detección

Pregunta antes de escribir cualquier frase del cuerpo del docente:

> *¿Esta frase describe una acción concreta del docente en el aula, o solo describe el estado del sistema editorial / del aprendizaje?*

Si describe **estado** y no acción, **fuera del cuerpo**.

### 10.3 Voz del cuerpo — el docente no realiza acciones del estudiante

El cuerpo describe acciones que el docente realiza desde su posición frente al aula (explicar, dirigir la atención, escribir en pizarra, leer en voz alta con el grupo, modelar). **No se usan verbos en imperativo dirigidos al docente para acciones que físicamente realiza el estudiante con su material** — abrir el libro, hojearlo, escribir en el cuaderno, subrayar en su libro. Esas acciones se introducen con verbos que enmarquen la propuesta del docente al grupo: *Proponga abrir, Pida que abran, Pídales que hojeen, Dígales que escriban*.

**Razón.** La guía describe lo que el docente hace o propone; no usurpa la acción del estudiante. La voz coherente refuerza la separación entre el rol del docente (conduce, modela, propone) y el del estudiante (ejecuta sobre su material).

**Casos a evitar y su corrección:**

| ❌ Incorrecto | ✅ Correcto |
|---|---|
| *Abra la página 14.* | *Proponga abrir la página 14.* / *Pida a la clase que abra la página 14.* |
| *Hojee la unidad.* | *Pídales que hojeen la unidad.* |
| *Subraye los verbos.* | *Pídales que subrayen los verbos.* |
| *Escriba la respuesta en el cuaderno.* | *Pídales que escriban la respuesta en el cuaderno.* |

**Excepción — sí va imperativo al docente** cuando la acción ocurre en la zona del docente (pizarra, voz, gesto, modelado): *Escriba en la pizarra · Lea con la clase · Dibuje un triángulo · Mime las acciones · Diríjase a una persona del grupo*.

**Filtro de detección.** Antes de cualquier imperativo en el cuerpo, preguntarse: *¿esta acción la ejecuta el docente desde su posición, o la ejecuta el estudiante sobre su propio material?* Si es del estudiante, reformular con *Proponga / Pida que / Pídales que / Dígales que*.

### 10.4 Estilo propositivo en restricciones temporales de fase inductiva

Cuando en una secuencia didáctica hay algo que **aún no debe enunciarse o formalizarse** (la regla no se da hasta que la formulan los estudiantes, la respuesta no se revela hasta el cierre, el patrón no se nombra antes de que se descubra), se redacta en **forma propositiva** que describe lo que sí ocurre, no en imperativo prohibitivo dirigido al docente.

**Razón.** El imperativo prohibitivo (*no formalice, no enuncie, no dé la respuesta*) carga al docente con una vigilancia negativa. La forma propositiva (*sin formalizar, sin enunciar, deje que…*) describe la misma intención didáctica en clave de propuesta abierta — coherente con la voz de andamiaje que conduce, no controla.

**Ámbito acotado.** Esta regla aplica a **restricciones temporales del marco inductivo** (MARS EARS): el contenido se mantiene oculto hasta el momento didáctico apropiado. **No** prohíbe el imperativo negativo cuando la acción negada es una norma de aula que el docente sí debe sostener activamente (ej.: *Mantenga la inmersión en español*, *No traduzca a su lengua* sigue siendo válido si la regla del aula es inmersión).

**Casos a evitar y su corrección:**

| ❌ Imperativo prohibitivo | ✅ Propositivo |
|---|---|
| *No formalice la regla todavía.* | *Sin formalizar la regla.* / *Aún sin enunciar la regla.* |
| *No dé la respuesta.* | *Sin dar la respuesta.* / *Deje que la encuentren ellos.* |
| *No enuncie el patrón antes de tiempo.* | *Aún sin nombrar el patrón.* |
| *No interrumpa al estudiante.* | *Espere a que termine.* / *Acompañe en silencio.* |

### 10.5 Doble marcaje de restricción temporal en fase inductiva

Una restricción temporal de fase inductiva (no formalizar la regla todavía, no anticipar la respuesta, no nombrar el patrón antes de que se descubra) se enuncia **una sola vez por actividad**. Si la misma restricción aparece marcada al abrir y al cerrar la misma actividad, hay **doblete funcional**: dos marcadores de la misma intención didáctica flanqueando una secuencia única.

**Cómo resolver el doblete.** Conservar la marca que mejor encaje pedagógicamente — **normalmente la de cierre**, porque es donde el docente decide si lanzar la formalización tras la fase inductiva — y eliminar la otra. Si la marca de apertura aporta algo que el cierre no recoge (un matiz distinto, una acción concreta a evitar), conservar la apertura y eliminar el cierre.

**Tercer caso — eliminar ambas.** Si la propia secuencia de la actividad hace explícita la fase inductiva por diseño (preguntas abiertas, descubrimiento guiado, ninguna enunciación de regla en el cuerpo), eliminar las dos marcas: el diseño ya hace el trabajo del marcador, y los avisos verbales se vuelven redundantes con el dispositivo didáctico mismo.

**Razón.** La fase inductiva ya está marcada por el diseño mismo de la actividad (preguntas abiertas, descubrimiento, no enunciación). Marcarlo además al abrir y al cerrar carga al docente con dos avisos del mismo principio sin sumar pedagogía.

**Filtro de detección.** Ante una actividad con marca propositiva de restricción temporal (§10.4), preguntarse: *¿esta restricción ya está marcada en otro punto de la misma actividad?* Si sí, evaluar dónde se queda y dónde se elimina.

**Ejemplo resuelto** (U1G B2, *Contraste el masculino y el femenino*, 2026-05-26):

| Posición | Texto | Decisión |
|---|---|---|
| Apertura | *Sin dar la regla todavía, lance al grupo cuatro preguntas breves…* | Eliminada (duplicaba el cierre). |
| Cierre | *Mantenga la tensión: deje que la regla la cierren los propios estudiantes al final del bloque.* | Eliminada en revisión posterior — las 4 preguntas abiertas marcan por sí solas la fase inductiva; ningún marcador verbal necesario (caso del "tercer caso" del párrafo anterior). |

⚠ **A diferencia de §10.6**, esta regla no exige consulta previa: si el doblete funcional es evidente (misma restricción, misma actividad, dos marcadores), el chat lo resuelve aplicando el criterio "normalmente conservar el cierre". Si hay ambigüedad sobre qué marca conservar, sí consultar.

**Prioridad cruzada con §10.6.** Si un mismo fragmento dispara también §10.6 (recuenta contenido visible del libro además de ser doblete temporal), **manda §10.6**: aplica el gate de consulta previa de §10.6 antes de cualquier eliminación. La regla más cautelosa prevalece.

### 10.6 Recuento redundante de contenido visible del libro: consulta previa antes de eliminar

Las **aclaraciones-recuento** que enumeran o desglosan contenido que el docente tiene a la vista en el libro del alumno (ítems de un ejercicio, contenido de un cuadro, frases de un audio, opciones de una tabla) tienen valor **solo si añaden foco didáctico, contraste, criterio de atención o aviso de riesgo**. Si solo recuentan lo que el docente ya ve a simple vista, normalmente pueden salir del cuerpo.

**Formas en que aparecen:**

- Generalizaciones numéricas: *"cinco son de tipo X, uno es de tipo Y"*.
- Enumeración del contenido de un cuadro: *"Artículos determinados (el/la/los/las), Masculino y femenino (nombres de cosas y de personas)…"*.
- Lista parentética de ejemplos cuando el docente ya los tiene delante.
- Reproducción de citas textuales del libro tras *"lea con la clase el ejemplo del ejercicio X: …"* o *"…el ejemplo del libro: …"*. La cita ya está en el libro a la vista del docente; sale el contenido tras los dos puntos, se mantiene la instrucción (*"Lea con la clase el ejemplo del ejercicio X"*).
- Descripciones del enunciado o del formato del ejercicio que recuentan lo que el docente ya ve en el libro: *"El ejercicio 3 pide cuatro datos sobre Jorge"*, *"El ejercicio 4 cierra la comprensión con cuatro frases de verdadero o falso"*, *"Pase al ejercicio 7: dictado de ocho números"*. La identificación del ejercicio se hace con referencia numerada (*"Para el ejercicio 3"*, *"En el ejercicio 4"*); la orientación describe lo que el docente hace, no lo que el ejercicio pide.

**El valor está en lo que la aclaración añade, no en lo que enumera.** Una aclaración aporta si:

- distingue **categorías que requieren explicación distinta**;
- focaliza la **atención del docente** en ítems con dificultad recurrente;
- anuncia un **contraste o un riesgo didáctico** que el ejercicio no señala por sí solo.

Si la aclaración solo nombra lo que está visible y no cumple ninguna de esas tres funciones, es candidata a eliminación.

⚠ **Pero la decisión final es del editor.** Determinar si una aclaración aporta foco, contraste, atención o aviso requiere juicio editorial sobre el contexto pedagógico. **Ningún chat puede eliminar aclaraciones-recuento por su cuenta basándose solo en este criterio.**

**Procedimiento obligatorio cuando se detecta una candidata:**

1. **No eliminar directamente.**
2. **Citar en chat** la aclaración detectada con su contexto (rótulo, ejercicio, cuadro).
3. **Aplicar el filtro** y exponer el análisis: *"¿esta aclaración añade foco, contraste, atención o aviso, o solo recuenta lo visible?"*
4. **Proponer al editor** dos opciones: mantener o eliminar, con una recomendación razonada.
5. **Esperar OK explícito en chat.** **Silencio o ausencia de respuesta no equivalen a aprobación.** Solo el OK literal autoriza la eliminación.

**Razón de la consulta obligatoria.** El docente tiene el material delante, sí, pero a veces una aclaración aparentemente redundante recoge un matiz que el editor introdujo deliberadamente (un punto de atención, una conexión con otro bloque, una ayuda para el docente que enseña esto por primera vez, un aviso de error frecuente). Eliminar sin consultar puede borrar valor editorial sutil que el chat no aprecia.

**Filtro orientativo (no decisorio):**

> *Esta aclaración, ¿añade foco, contraste, criterio de atención o aviso de riesgo didáctico, o solo recuenta contenido visible del libro?*

Si la respuesta es "solo recuenta", **proponer** la eliminación al editor en chat. No aplicarla por defecto.

**Ejemplos de aclaraciones-recuento cuyo análisis en chat fue concluyente:**

| Aclaración | Análisis | Decisión del editor |
|---|---|---|
| *Cinco son tercera persona (Iván, María, él, Charlie, Julia → tiene), uno es primera (yo → tengo).* (U1G B1, ej. 2) | Solo recuenta los sujetos del ejercicio. No añade foco distinto. | Fuera (2026-05-26). |
| *Artículos determinados (el/la/los/las), Masculino y femenino (nombres de cosas y de personas), Nacionalidad (mexicano/mexicana, español/española, japonés/japonesa).* (U1G B2) | Solo recuenta el contenido del cuadro; el docente lo ve al dirigir la atención. | Fuera (2026-05-26). |
| *La mitad son -o/-a clásicos…; cuatro son profesiones -or/-ero…; dos son invariables.* (U1G B2, ej. 5) | Distingue tres tipos morfológicos que requieren explicación distinta. | Mantener. |
| *Tres ítems piden cuidado especial: el 6 (...), el 9 (...), el 10 (...).* (U7G B1, ej. 1) | Focaliza la corrección donde la clase suele dudar. | Mantener. |
| *regulares (profesor/profesora, niño/niña), formas dadas en femenino con masculino a inferir (amigo/amiga), nacionalidades con cambio de acento (campeón/campeona, alemán/alemana), y una con cambio gráfico (griego/griega, brasileño/brasileña).* (U1G B2, ej. 4) | Las categorías distinguen cuatro tipos morfológicos; los paréntesis actúan como tagger que etiqueta cada ítem con su categoría — ayuda a focalizar la corrección. | Mantener (2026-05-26). |
| *los ocho colores del libro (rojo, blanco, negro, amarillo, azul, marrón, verde, rosa).* (U1G B2, ej. 7) | Los paréntesis son insumo de acción inmediata para una tarea de pizarra; sin ellos el docente tiene que ir a la página 15 a leer la lista. | Mantener (2026-05-26). |
| *Formular preguntas con los interrogativos básicos (cómo, cuántos, de dónde, qué, cuál).* (U1G B3, objetivo de bloque) | La enumeración entre paréntesis recuenta el contenido del ejercicio 9; los interrogativos están visibles en el libro. El objetivo de bloque debe ser síntesis, no inventario del contenido enumerado. | Fuera (2026-05-26). |
| *Lea con la clase el ejemplo del ejercicio 2: ¡Hola! · ¿Cómo te llamas? · Me llamo… ¿Y tú? · Me llamo…* (U1 Comunicación B1, ej. 2) y casos análogos en ej. 3, 5, 6 + vocabulario U1V *Me llamo Pedro y soy de España, soy español* | La cita reproduce contenido visible del libro del alumno; el docente la tiene a la vista. Sale tras los dos puntos; se mantiene la instrucción *"Lea con la clase el ejemplo del ejercicio X"* o *"el ejemplo del libro"*. | Fuera (2026-05-26). |

⚠ **Los ejemplos de esta tabla NO son plantillas reutilizables.** Cada nuevo caso requiere consulta independiente, aunque parezca análogo a uno ya resuelto. La tabla es histórico de decisiones, no jurisprudencia.

### 10.7 Sin referencias a "bloque" en el cuerpo del docente

Los **bloques** son convención editorial interna (división del archivo `final/` por *Ejercicios X-Y*). **No aparecen en el cuerpo del docente.** En su lugar, las referencias intra-archivo se hacen:

- por **número de ejercicio**: *"el ejercicio 4"*, *"los ejercicios anteriores"*, *"el ejercicio 7"*.
- por **temporalidad**: *"anteriormente"*, *"ya visto"*, *"trabajado antes"*, *"como aprendieron"*.
- por **contenido**: *"los patrones de masculino y femenino"*, *"la fórmula del saludo"*.

**Casos a evitar:**

| ❌ Con "bloque" | ✅ Por ejercicio / anteriormente / contenido |
|---|---|
| *"al cerrar el bloque…"* | *"al cerrar la sección…"* / *"al cerrar el ejercicio X…"* |
| *"los patrones del bloque…"* | *"los patrones del ejercicio 4"* / *"los patrones vistos"* |
| *"integra todo lo del bloque"* | *"integra todo lo trabajado en los ejercicios anteriores"* |
| *"la tarjeta del bloque 1"* | *"la tarjeta usada anteriormente"* / *"la tarjeta del ejercicio 3"* |

**Razón.** El docente no ve la sección como dividida en "bloques" — ve ejercicios numerados. La división en bloques es organización interna del archivo (para legibilidad editorial); referenciarla al docente añade jerga sin función.

### 10.8 ENTREGA DE INSIGNIA: rótulo + frase única

El rótulo *ENTREGA DE INSIGNIA* nombra la acción. **No se repite debajo** con *"Entrega de insignia ¡LEMA!"* como segunda línea — sería redundancia visual con el rótulo.

El bloque queda en una o dos frases:

1. Frase obligatoria: *"Mencione que por [logros del estudiante], reciben la insignia **¡LEMA!**"*
2. Frase opcional (solo si el comentario cultural sobre el lema es **verificable y aporta**): *"Comente que en español [lema] es [explicación breve real]."*

Si el lema no tiene comentario cultural verdadero o significativo, **no se inventa**: el bloque queda solo con la frase obligatoria.

---

## 11. Cómo aplicar este manual

### 11.1 Activación automática

Este manual se activa automáticamente cuando Claude trabaja con cualquier archivo `unidades/**/final/*.md`, mediante la regla path-scoped `.claude/rules/final-style.md`.

### 11.2 Si hay conflicto entre el manual y un archivo existente

- **No improvisar**.
- **Señalar el conflicto en chat** explícitamente.
- **Pedir decisión al autor** antes de modificar.

### 11.3 Cómo proponer una regla nueva o cambiar una existente

1. Documentar el caso concreto que motiva la propuesta.
2. Proponer redacción específica de la regla.
3. Esperar OK del autor.
4. Actualizar este manual en commit propio.
5. La regla activa automáticamente desde el siguiente uso.

### 11.4 Criterio de aplicación: compactación y consulta

Tras verificar estructura, objetivo y dinámica del archivo, se realiza una **pasada de compactación editorial** sobre el cuerpo del docente. Esta pasada se aplica **sin microconsulta paso a paso**: se ejecuta directamente cuando el caso es evidente. La consulta en chat se reserva a los supuestos listados al final de este apartado.

**Criterios de la pasada de compactación** (decir lo mismo con menos palabras, sin alterar dinámica, secuencia ni intención didáctica):

- Reducir redundancias evidentes (frases que reformulan la anterior sin añadir información nueva).
- Eliminar conectores temporales de relleno (*A continuación*, *Entonces*, *Después*) cuando el orden del texto ya marca la sucesión.
- Suprimir sujetos explícitos redundantes (*los estudiantes*, *cada alumno*) cuando el contexto los hace implícitos.
- Suprimir adjetivos y adverbios sin carga informativa (*real*, *propio*, *rápidamente*, *formalmente*).
- Eliminar afirmaciones hiperbólicas según §10.1, sin sustituirlas por nada.
- Aplicar §10.4 (estilo propositivo) y §10.5 (sin doblete de marca temporal) cuando el caso sea claro y autoejecutable.
- Variar los cierres de corrección según naturaleza del ejercicio (ej. *Corrigen en parejas* vs. *Corrija en plenaria*).

**Cuándo SÍ se abre consulta en chat (no automatismo, no compactación silenciosa):**

- Eliminación de generalizaciones o aclaraciones-recuento del libro — siempre §10.6, con gate de consulta previa.
- Cambios que afecten la estructura o la dinámica del archivo (eliminar una actividad, cambiar tipo de corrección de forma sustancial, mover bloques).
- Falta de claridad en el material original que impida decidir con confianza.
- Dudas sustantivas sobre qué categoría aplicar, qué dinámica preservar, qué objetivo reformular.

**Filtro de detección antes de cada recorte:**

> *¿Este recorte pierde algo (información operativa, dinámica, claridad) o solo redundancia?* Si solo redundancia → aplicar. Si pierde algo → consultar.

---

## 12. Cambios y versiones

| Fecha | Cambio |
|---|---|
| 2026-05-25 | Manual inicial — capa `final/`. Codifica decisiones de la sesión coordinador del 2026-05-25 sobre derivación retroactiva de propuestas a versión limpia. |
| 2026-05-26 | §10.1 — reformulado el bullet de resúmenes-balance de cierre de sección: *"el círculo está cerrado"* y *"en una sola doble página han aprendido…"* pasan a estar definitivamente fuera (caso confirmado en piloto U1V). |
| 2026-05-26 | §10.3 nueva — voz del cuerpo: el docente no realiza acciones del estudiante (*Abra* → *Proponga abrir*, etc.). Codifica un patrón implícito ya practicado en vocabulario U1V. |
| 2026-05-26 | §10.4 nueva — estilo propositivo en restricciones temporales de fase inductiva (*no formalice* → *sin formalizar*). Ámbito acotado a restricciones del marco inductivo MARS EARS; no afecta a normas de aula sostenidas activamente. Aplicación retroactiva al piloto: *vocabulario.md* L39, *gramatica.md* L39 y L65. |
| 2026-05-26 | §10.6 nueva — generalizaciones del ejercicio: consulta previa en chat obligatoria antes de cualquier eliminación. Silencio ≠ OK; ejemplos no son jurisprudencia. §10.5 reservada para futuras reglas de voz. |
| 2026-05-26 | §10 retitulada — *"Estructura sin metadiscurso editorial"* → *"Voz del cuerpo del docente y criterios editoriales de redacción"*. Tras incorporar §10.3-10.6, el título anterior solo describía §10.1-10.2. |
| 2026-05-26 | §10.5 nueva — doble marcaje de restricción temporal en fase inductiva: una sola marca por actividad, normalmente la de cierre. Codifica el caso U1G B2 (apertura *"sin dar la regla todavía"* eliminada por duplicar el cierre). Sin gate de consulta: regla autoejecutable cuando el doblete es evidente. |
| 2026-05-26 | §10.6 ampliada — de *"generalizaciones del ejercicio"* a *"recuento redundante de contenido visible del libro"*. Mantiene el gate de consulta previa (silencio ≠ OK, sin jurisprudencia). Acotación añadida: el valor está en lo que la aclaración añade (foco, contraste, atención, aviso), no en lo que enumera. |
| 2026-05-26 | §10.5 — nota de prioridad cruzada con §10.6 añadida: cuando un fragmento dispara ambas, manda §10.6 (la regla más cautelosa). |
| 2026-05-26 | §10.5 — añadido "tercer caso": si la propia secuencia hace explícita la fase inductiva por diseño (preguntas abiertas, descubrimiento guiado), eliminar ambas marcas. Ejemplo U1G B2 revisado: cierre también eliminado al constatar que las 4 preguntas abiertas marcan por sí solas la inducción. |
| 2026-05-26 | §11.4 nueva — criterio de aplicación: compactación y consulta. Codifica la pasada de compactación editorial sobre el cuerpo del docente como **paso de uso del manual** (no como bloque doctrinal nuevo). La compactación ordinaria se aplica sin microconsulta; la consulta en chat queda reservada a §10.6, cambios de estructura/dinámica y dudas reales. |
| 2026-05-26 | §10.6 — fila nueva en la tabla de ejemplos: enumeración entre paréntesis dentro del objetivo de bloque que recuenta contenido visible del libro (caso *"Formular preguntas con los interrogativos básicos (cómo, cuántos, de dónde, qué, cuál)"* — eliminados los paréntesis). El objetivo de bloque es síntesis, no inventario. |
| 2026-05-26 | §2.1 nueva — convenciones específicas por sección. Codifica para Comunicación: (a) línea obligatoria *"Buscar Vídeo de comunicación **unidad X**"* en B1; (b) formato canónico de tarjeta de estrategia: *"Imprimir tarjeta de estrategia—[destreza]—*[título]*"*. |
| 2026-05-26 | §13 nueva — patrones observados pendientes de codificación. Registra dos patrones detectados en el piloto U1 que el autor decide no codificar todavía: narración meta-pedagógica del proceso (Patrón 1) y autoafirmaciones sobre el éxito esperado de una dinámica (Patrón 3). Revisar al cerrar más unidades. |
| 2026-05-26 | §13 — patrón 4 añadido: fusión de rótulos secuenciales con acciones encadenadas (caso piloto U1 Comunicación B1, dos rótulos *CONTEXTUALICE…* + *PRESENTE EL VÍDEO* fusionados). Sin codificar — exige juicio editorial sobre granularidad. |
| 2026-05-26 | §2.1 — añadida subsección Comunicación: las etiquetas *CARA A* / *CARA B* son convención editorial interna y no aparecen en el cuerpo del docente; en el cuerpo se nombran por contenido (*la cara del saludo en cuatro pasos*, *la cara de las micro-funciones*…). Aplicado retroactivamente en U1 Comunicación B1. |
| 2026-05-26 | §10.6 — añadido cuarto bullet en "Formas en que aparecen": reproducción de citas textuales del libro tras *"lea con la clase el ejemplo: …"*. El docente tiene el libro a la vista; la cita reproducida en el cuerpo no añade. Aplicado retroactivamente: 4 ocurrencias en U1 Comunicación + 1 en U1V. |
| 2026-05-26 | §10.7 nueva — sin referencias a *"bloque"* en el cuerpo del docente. Los bloques son convención editorial interna; en el cuerpo se referencia por número de ejercicio (*"el ejercicio 4"*), temporalidad (*"anteriormente"*) o contenido (*"los patrones de M/F"*). Aplicado retroactivamente: 2 ocurrencias en U1 (comunicacion.md L75, gramatica.md L67) + el caso original en U1 Comunicación B3 (*"del bloque 1"* → *"usada anteriormente"*). |
| 2026-05-26 | §10.8 nueva — ENTREGA DE INSIGNIA: rótulo + frase única. Eliminada la línea *"Entrega de insignia ¡LEMA!"* duplicada bajo el rótulo en los tres `final/` (vocabulario, gramatica, comunicacion); el lema se integra en la frase *"…reciben la insignia ¡LEMA!"*. Comentario cultural opcional solo si verificable. Eliminada afirmación falsa sobre *a conocernos* en U1 Comunicación. |
| 2026-05-28 | §10.1 — bullet nuevo: referencias anticipatorias a otra sección de la guía o del libro (*"—el plural se trabaja en gramática—"*). Caso detectado en U2V. La intención didáctica de no abrir la regla se conserva con la forma propositiva de §10.4. |
| 2026-05-28 | §8.1 — entrada nueva: *apuestas* queda vetado para verbalizar la recogida de hipótesis del grupo; se usa *respuestas* o *propuestas*. Caso detectado en U2V. El matiz lúdico-conjetural de *apuesta* no encaja con la voz docente. |
| 2026-05-28 | §8.1 — entrada nueva: *voces* queda vetado como metonimia cuantificable de personas que intervienen en plenaria; se usa *intervenciones*, *turnos* o *aportaciones*. Caso detectado en U2V (cuantificación plural de intervinientes). |
| 2026-05-28 | §7.1 — nota nueva tras la tabla: en plural cuantificado, cuantificar la acción (*tres intervenciones*), no las personas. Cierra el cuello de botella que llevaba a metonimias forzadas o a masculino genérico. |
| 2026-05-28 | §10.1 — bullet nuevo: predicciones narrativas sobre la respuesta de la clase (*"saldrá X"*, *"dirán Y"*) prohibidas. Sustituir por andamiaje activo. Excepción: bifurcaciones operativas con instrucción para cada rama (*si sale X, confírmelo; si no, redirija con Y*). Caso detectado en U2G. Integrado como bullet en §10.1 (no sección autónoma) porque encaja en la frontera §10.1/§10.2. |
| 2026-05-28 | §13 — Patrón 5 añadido: worked examples redundantes con el saber del docente (paradigmas verbales triviales). Sin codificar por inestabilidad de la frontera con modelados que sí orientan. Caso piloto en U2G. |
| 2026-05-29 | §10.6 — ampliada con un quinto bullet en "Formas en que aparecen": descripciones del enunciado o del formato del ejercicio que recuentan lo visible (*"El ejercicio X pide…"*, *"El ejercicio Y cierra con…"*, *"Pase al ejercicio Z: dictado de…"*). La identificación se hace con referencia numerada; la orientación describe lo que el docente hace, no lo que el ejercicio pide. Mantiene el gate de consulta previa de §10.6 (silencio ≠ OK). Caso detectado en U2 Comunicación. |
| 2026-06-01 | §10.1 — bullet nuevo: prescripción de decisiones libres del docente (paletas de colores específicas, mapeos concretos, mecánicas detalladas no obligadas). La guía orienta el qué y el para qué; el docente decide el cómo concreto cuando la elección no carga peso didáctico. Caso detectado en U2 Gramática y Cultura. |
| 2026-06-01 | §6.1 — nota tipográfica añadida: el título individual de una tarjeta citado como referencia individual va en cursiva título-case (*Caza el dato*, *Escucha en tres modos*, *Saludar y despedirse*, *Presentarse y datos personales*), nunca en ALL CAPS (reservado a rótulos imperativos y lemas de insignia §4.2). Distinción explícita respecto a la mención canónica del tipo de la tabla §6.1. Caso detectado en U2 Destrezas. |
| 2026-06-01 | §2.1 — subsección nueva *Evaluación — conexión a unidad siguiente*: una sola frase escueta al cierre de *AUTOEVALUACIÓN Y CIERRE* con formato canónico (*Cierre con la conexión a la **unidad X+1**: en la próxima unidad…*). Única referencia anticipatoria permitida en cualquier `final/`. Codificación desde patrón cumplido en U1E + U3E. |

Este manual es **vivo**. Las reglas se ajustan a medida que la capa `final/` crezca y aparezcan casos límite no contemplados. Cualquier modificación se documenta arriba.

---

## 13. Patrones observados pendientes de codificación

Lista interna de patrones detectados durante el piloto que **no se han codificado todavía**. Cada uno necesita más casos de observación antes de decidir si merece regla propia, encajar como subcaso de regla existente, o descartar como decisión editorial caso a caso. Revisar al cerrar más unidades.

### Patrón 1 — Narración meta-pedagógica del proceso de aprendizaje

**Caso piloto** (U1G B2, rótulo *SISTEMATICE LA REGLA DE CONCORDANCIA*):

> *"…ahora la verbalizan ellos y usted la oficializa señalando dónde queda en el libro."*

**Qué describe.** Comentario sobre **quién verbaliza qué** y **quién oficializa qué** en la dinámica de aula (estudiantes verbalizan, profesor oficializa), en lugar de instruir una acción concreta del docente.

**Estado.** Eliminado en piloto. Sin codificar — el autor necesita más casos para decidir si es subcaso de §10.1 (metadiscurso editorial) o si merece regla propia.

### Patrón 3 — Autoafirmaciones sobre el éxito esperado de una dinámica

**Caso piloto** (U1G B3, ensayo en parejas tras el modelado del docente):

> *"Dos o tres intercambios bastan para automatizar la melodía y la fórmula."*

**Qué describe.** Afirmación que **declara cuántas repeticiones, rondas o intercambios bastarán para producir tal aprendizaje** (prescripción pedagógica generalista). La instrucción concreta de cantidad (*tres rondas, dos vueltas*) se mantiene; lo que sale es la afirmación de **suficiencia para conseguir X**.

**Estado.** Eliminado en piloto. Sin codificar — decisión caso a caso por ahora. Revisar al cerrar más unidades: si el patrón se repite consistentemente, se codifica como subcaso de §10.1.

### Patrón 4 — Fusión de rótulos secuenciales con acciones encadenadas

**Caso piloto** (U1 Comunicación B1):

> Dos rótulos consecutivos:
> *"CONTEXTUALICE LA SITUACIÓN COMUNICATIVA"* (conectar con lo trabajado en Vocabulario y Gramática + bridge al vídeo)
> *"PRESENTE EL DIÁLOGO MEDIANTE EL VÍDEO"* (lanzar el vídeo + dos proyecciones)
>
> → fusionados en uno: *"CONTEXTUALICE LA SITUACIÓN Y PRESENTE EL VÍDEO"*

**Qué describe.** Dos rótulos consecutivos cuyas acciones forman una **secuencia natural única** (contextualizar → presentar, modelar → practicar, leer → responder) pueden fusionarse cuando la separación entre ambos no añade granularidad didáctica real. El comentario del autor: *"dos títulos en uno no tiene sentido tantos"* — la atomización excesiva de rótulos satura visualmente al docente sin añadir orientación operativa.

**Estado.** Aplicado en piloto. Sin codificar como regla — exige juicio editorial sobre si la separación entre rótulos aporta granularidad o solo fragmenta visualmente. Un chat no debería fusionar rótulos por su cuenta. Revisar al cerrar más unidades: si el patrón se repite consistentemente, codificar como regla con gate de consulta previa (similar a §10.6).

### Patrón 5 — Worked examples redundantes con el saber del docente

**Casos piloto** (U2G, 2026-05-28):
- *"pídales las tres formas del singular de tener (tengo, tienes, tiene)"* — eliminado el paréntesis.
- *"escríbalas en la fila Una persona: tengo / tienes / tiene"* — eliminado.
- *"escríbalas: tenemos, tenéis"* — eliminado.

**Qué describe.** Ejemplos que **no están en el libro** pero son trivialmente recuperables para un docente de ELE A1.1 (paradigmas verbales básicos, opuestos M/F evidentes). Distinto de §10.6 (recuento del libro).

**Estado.** Sin codificar — la línea con worked examples que sí orientan (apocopación *primer curso, tercer piso*, modelados orales que disparan dinámica) sigue siendo inestable. Revisar al cerrar U2 y U3.
