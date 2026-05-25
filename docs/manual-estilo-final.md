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
| Tarea numerada del libro | `ejercicio` (palabra completa) | ~~ej.~~ · ~~act.~~ · ~~actividad~~ (cuando se refiere a tarea numerada) |
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

## 10. Estructura sin metadiscurso editorial

El cuerpo del docente vive en **lengua de aula con acción concreta**. No contiene metadiscurso sobre el sistema editorial.

### 10.1 Lo que NO debe aparecer

- Anuncios sobre el corpus: *"el set acaba de ampliarse"*, *"esta unidad inaugura...".*
- **Resúmenes-balance de cierre de sección**: frases que recapitulan lo aprendido en clave grandilocuente o de balance editorial. Ejemplos a evitar: *"el círculo está cerrado"*, *"en una sola doble página han aprendido a…"*, *"el set queda activado"*, *"con esto cerramos el bloque de…"*. No describen acción del docente ni aportan andamiaje al aula: solo cierran retóricamente lo que la propia secuencia de ejercicios ya cierra. Fuera del cuerpo.
- Decisiones del equipo editorial: *"hemos decidido..."*, *"el equipo propone..."*.
- Referencias a otras secciones del propio sistema MD: *"como ya vimos en la metanota..."*.
- **Afirmaciones normativas redundantes sobre el libro**: *"La estructura obligatoria es siempre la del libro"*, *"Hay que seguir el orden del libro"*, *"Esto es lo que dice el libro"*. El docente ya sabe que el libro es la fuente; el cuerpo de los rótulos debe limitarse a la acción concreta sin recordatorios meta-editoriales.
- **Afirmaciones hiperbólicas, grandilocuentes o no verificables**: *"son las preguntas reales de cualquier hablante de español al escribir un nombre nuevo: las van a oír y a hacer toda la vida"*, *"este vocabulario les acompañará siempre"*, *"es la clave para…"*. No aportan valor lingüístico ni didáctico; son retórica de relleno. Si una afirmación no aporta valor lingüístico verificable, fuera del cuerpo. Sustituir por explicación funcional concreta (ej.: *"son importantes para esclarecer entre dos opciones"*).
- **Respuestas de los ejercicios cuando ya están visibles en la imagen del libro del alumno**: ejemplo: *"completan los huecos con la letra correcta (J / j, V / v, H / con h)"* — el paréntesis es redundante porque el docente ya ve las respuestas en su material y el alumno trabaja sobre el libro. Solo se incluyen respuestas en el cuerpo del docente si hay algo específico que destacar (ej.: ítem con error frecuente, opción ambigua, ítem que el docente debe corregir explícitamente). Por defecto, fuera.

### 10.2 Filtro de detección

Pregunta antes de escribir cualquier frase del cuerpo del docente:

> *¿Esta frase describe una acción concreta del docente en el aula, o solo describe el estado del sistema editorial / del aprendizaje?*

Si describe **estado** y no acción, **fuera del cuerpo**.

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

---

## 12. Cambios y versiones

| Fecha | Cambio |
|---|---|
| 2026-05-25 | Manual inicial — capa `final/`. Codifica decisiones de la sesión coordinador del 2026-05-25 sobre derivación retroactiva de propuestas a versión limpia. |
| 2026-05-26 | §10.1 — reformulado el bullet de resúmenes-balance de cierre de sección: *"el círculo está cerrado"* y *"en una sola doble página han aprendido…"* pasan a estar definitivamente fuera (caso confirmado en piloto U1V). |

Este manual es **vivo**. Las reglas se ajustan a medida que la capa `final/` crezca y aparezcan casos límite no contemplados. Cualquier modificación se documenta arriba.
