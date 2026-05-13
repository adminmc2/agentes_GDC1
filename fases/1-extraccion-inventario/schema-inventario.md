# Schema del inventario — Contrato de datos puro

> **Responsabilidad:** definir la **forma** del JSON `UX-nc1-inventario.json`. Solo estructura, tipos, obligatoriedad y restricciones validables sin contexto editorial.
>
> **No contiene:** cuándo aplica cada campo, cómo elegir el valor, reglas de población semántica, workflow de extracción, ejemplos pedagógicos ni casos históricos. Esos viven en `reglas-operativas.md` o `convenciones-y-casos.md`.

> ⚠️ **Aviso transitorio:** `validar_inventario.py` y `reglas-operativas.md` aún no están alineados con este schema; la validación contra este shape es manual. Detalle, implicaciones y criterios de retirada → **Apéndice transitorio** al final del documento.

> **Naturaleza del contrato.** El **shape base** (top-level, schema por página/actividad/cuadro, las 4 listas tipadas, los 4 bloques consolidados y las marcas internas declaradas en §14) es el contrato canónico estable del sistema. Se mantiene entre cursos salvo decisión formal de rediseño del contrato. Las **enumeraciones cerradas** (`tipo`, `destreza`, `enfoque`, `tiempo`, `tipo_cuadro`, `seccion`, `autoevaluacion.opciones`) son igualmente canónicas, pero **versionables por expansión controlada**: pueden ampliarse cuando el alcance real del curso lo exija. La ampliación no es libre: requiere documentación explícita del cambio y actualización paralela del schema, del validador y, cuando corresponda, de `reglas-operativas.md`. Mientras no se amplíe, cada enumeración es estricta y rechaza valores fuera del set.

---

## 1. Estructura top-level (13 claves obligatorias + 3 opcionales canónicas + 1 transitoria)

```jsonc
{
  "unidad": <int, sin cero>,
  "curso": "nc1",
  "titulo": <str>,
  "paginas_libro": <str, ej: "34-43">,
  "nivel": <str, ej: "A1.1">,
  "fuente": {
    "archivo": "unidades/UX/fuente/UX-nc1.pdf",
    "version_extraccion": "<YYYY-MM-DD>"
  },
  "contenidos_indice": {
    "vocabulario": <str>,
    "gramatica": <str>,
    "comunicacion": <str>,
    "destrezas": <str>,
    "cultura": <str>
  },

  "vocabulario_consolidado":              <objeto principal+recurrente — ver §9.1>,
  "tiempos_y_verbos_consolidado":         <lista de lemas — ver §9.2>,
  "gramatica_consolidada":                <objeto principal+recurrente — ver §9.3>,
  "pronunciacion_ortografia_consolidada": <objeto principal+recurrente — ver §9.4>,

  "secciones": {
    "vocabulario":  { "paginas": [int], "actividades_ids": [str] },
    "gramatica":    { "paginas": [int], "actividades_ids": [str] },
    "comunicacion": { "paginas": [int], "actividades_ids": [str] },
    "destrezas":    { "paginas": [int], "actividades_ids": [str] },
    "cultura":      { "paginas": [int], "actividades_ids": [str] },
    "evaluacion":   { "paginas": [int], "actividades_ids": [str] },
    "reflexion":    { "paginas": [int], "actividades_ids": [str] }
  },
  // Opcionales canónicas
  "autoevaluacion":         <bloque, opcional — ver §6>,
  "_nota_unidad_atipica":   <str, opcional — ver §11>,
  "_decisiones_ia":         [str, opcional — ver §14],

  // Opcional transitoria (ver Apéndice)
  "_migracion_rediseno":    <objeto, opcional — clave transitoria, ver Apéndice>,

  "paginas_detalle":        [<página>, ...]
}
```

**Recuento del shape:** 13 claves obligatorias (`unidad`, `curso`, `titulo`, `paginas_libro`, `nivel`, `fuente`, `contenidos_indice`, los 4 bloques consolidados, `secciones`, `paginas_detalle`) + 3 claves opcionales canónicas (`autoevaluacion`, `_nota_unidad_atipica`, `_decisiones_ia`) + 1 clave opcional transitoria (`_migracion_rediseno`, ver Apéndice).

---

## 2. Schema por página (elemento de `paginas_detalle`)

```jsonc
{
  "pagina": <int>,
  "seccion": <clave normalizada de las 7 — ver §8>,
  "actividades": [<actividad>, ...],
  "cuadros": [<cuadro>, ...]   // opcional
}
```

---

## 3. Schema por actividad

```jsonc
{
  "id": "UX-pYY-actNN",
  "numero": <int opcional — ver nota §3.1>,
  "tipo": <de la taxonomía cerrada — ver §5>,
  "destreza": [<de la enumeración cerrada — ver §5b>],
  "enfoque": <de la enumeración cerrada — ver §5c>,
  "instruccion_original": <str literal del libro>,

  // === 4 listas tipadas — siempre presentes; lista vacía si la actividad no trabaja la dimensión ===
  "vocabulario":               [str],                 // referencias canónicas léxico
  "tiempos_y_verbos":          [<objeto verbal>],     // ver §3.2
  "gramatica":                 [str],                 // referencias canónicas gramaticales
  "pronunciacion_ortografia":  [str],                 // referencias canónicas pron/orto

  "audio":  { "presente": <bool>, "pista": <int opcional>, "transcripcion": <str opcional> },   // detalle normativo en §10
  "imagen": { "presente": <bool>, "descripcion": <str obligatorio si presente=true> },           // detalle normativo en §10
  "video":  { "presente": <bool> },                                                              // detalle normativo en §10
  "respuestas": [str],   // SIEMPRE presente. Lista vacía si no aplica.
  "datos": {             // saco abierto para CONTENIDO LITERAL DEL LIBRO
    "subtipo": <str opcional>,
    "items_libro": [str],
    "texto_completo": <str>,
    "dialogo_completo": [str],
    "textos_personajes": [{"personaje": <str>, "texto": <str>}],
    "preguntas": [str],
    "preguntas_opciones": [{...}],
    "cuadricula": [[str]],
    "frases": [str],
    "ejemplo_libro": <str>,
    "texto_modelo": <str>,
    "columnas_relaciona": { "izquierda": [str], "derecha": [str] },
    "nombres_dados": [str],
    "palabras_recuadro": [str],
    "horarios_digitales": {<id>: <hora>},
    "programas_tv": [str],
    "peliculas_cartelera": [str],
    "personajes": [str],
    "titulo_dialogo": <str>,
    "pasos": [str],
    "expresiones_dadas": [str],
    "afirmaciones_a_corregir": [str],
    "texto_correo": <str>,
    "ejemplos_modelo": [str],
    "objetivo_palabras": <int>
    // ... cualquier dato específico que NO encaje en los campos canónicos
  },

  // Marcas internas opcionales (ver §14)
  "_funcion_ambigua":  <bool opcional>,
  "_decisiones_ia":    [str, opcional]
}
```

> **Convención de presencia y vaciedad de las 4 listas tipadas:** las cuatro listas (`vocabulario`, `tiempos_y_verbos`, `gramatica`, `pronunciacion_ortografia`) están **siempre presentes** en cada actividad. Pueden ser **lista vacía** si la actividad no trabaja esa dimensión. Misma convención que `respuestas`: separa existencia del carril (siempre) de contenido efectivo del carril (puede no haberlo). La ausencia del campo en el JSON es error de shape, no "no aplica".

> **Política de extensibilidad de `datos`:** saco abierto. Cualquier campo nuevo se documenta y se añade al schema con la regla de población correspondiente en `reglas-operativas.md`.

### 3.1 Nota sobre `numero`

El campo `numero` es **opcional**. La mayoría de actividades del libro están numeradas (1, 2, 3...) y en ese caso `numero` se rellena con el entero del libro. Algunas actividades NO llevan número visible (ej. "Para aprender", cuadros que se clasifican como actividad por reglas-operativas §1, autoevaluación a pie de página): en esos casos `numero` se omite del JSON. El validador acepta su ausencia. Si está presente, debe ser entero.

> Cuándo numerar y cuándo omitir → `reglas-operativas.md` §1.

### 3.2 Shape exacto de `actividad.tiempos_y_verbos`

Cada elemento de la lista es un objeto con **exactamente 3 campos obligatorios**:

```jsonc
{
  "lema":              <str>,         // canónico de verbos-canonicos.json (validable)
  "tiempo":            <str>,         // del enum cerrado — ver §5d
  "formas_trabajadas": [str]          // formas conjugadas concretas presentes en
                                      // ESTA actividad. Literales del libro, no canónicas.
                                      // Lista no vacía. El validador chequea que pertenezcan
                                      // al paradigma del lema declarado (validación
                                      // estructural; el detalle vive en reglas-operativas.md).
}
```

**Ejemplo:**

```jsonc
"tiempos_y_verbos": [
  { "lema": "ser",      "tiempo": "Presente", "formas_trabajadas": ["soy", "eres", "es"] },
  { "lema": "llamarse", "tiempo": "Presente", "formas_trabajadas": ["me llamo", "te llamas", "se llama"] }
]
```

**Casos especiales:**

- **Perífrasis** (ej. `ir a + infinitivo`): se declara con `"tiempo": "Perífrasis"` y `formas_trabajadas` reflejando las apariciones concretas (`["voy a", "vas a", ...]`).
- **Forma no personal del verbo trabajada pedagógicamente fuera de perífrasis** (infinitivo aislado, listas de verbos en infinitivo, ejercicios de identificación...): se declara con `"tiempo": "Infinitivo"` y `formas_trabajadas` reflejando la forma del libro (`["cantar"]`).
- **Si el verbo aparece sin paradigma trabajado** (mención léxica suelta): no se añade a esta lista; va a `vocabulario` si procede.

**Coherencia con top-level y registry:**

- El **registry** `verbos-canonicos.json` lista todos los lemas válidos con su metadata completa (rasgo por tiempo, doble dimensión, etc.).
- La **actividad** referencia un subconjunto: solo los lemas que esa actividad trabaja, con el tiempo concreto y las formas exactas.
- El **top-level** `tiempos_y_verbos_consolidado` agrega todas las referencias de todas las actividades + cuadros de la unidad con shape más rico (ver §9.2).

---

## 4. Schema por cuadro

Los cuadros admiten las mismas 4 listas tipadas que una actividad y aportan a los bloques top-level en igualdad de condiciones.

```jsonc
{
  "tipo_cuadro": <enum de 5 valores — ver §7>,
  "titulo": <str | null>,
  "contenido": {
    "tipo": <str — tabla_conjugacion | tabla_interrogativos | tabla_posesivos | ...>,
    "texto_intro": <str opcional>,
    "ejemplos": [str]
    // ... estructura libre según el cuadro
  },
  "observaciones": <str, opcional>,

  // === 4 listas tipadas — siempre presentes; lista vacía si el cuadro no trabaja la dimensión ===
  "vocabulario":              [str],
  "tiempos_y_verbos":         [<objeto verbal>],    // shape igual a §3.2
  "gramatica":                [str],
  "pronunciacion_ortografia": [str]
}
```

> **Convención de presencia y vaciedad de las 4 listas tipadas:** misma que en actividad (§3). Las cuatro listas están **siempre presentes** en cada cuadro; pueden ser **lista vacía** si el cuadro no trabaja esa dimensión. La opcionalidad del cuadro como unidad vive en `página.cuadros` (§2), no en sus listas internas.

> `tipo_cuadro` describe la categoría pedagógica. `contenido.tipo` describe su estructura interna. Son complementarios.

---

## 5. Taxonomía cerrada de tipos de actividad (20 valores)

```
escucha
escucha_y_repite
escucha_y_responde
lee_y_escucha
ver_video
completa_huecos
relaciona
ordena
clasifica
seleccion_multiple
verdadero_falso
responder_preguntas_cerradas
responder_preguntas_abiertas
interaccion_oral
expresion_oral_libre
produccion_escrita_guiada
expresion_escrita_libre
busqueda_informacion
tarea_final
juego
```

> Criterios → `reglas-operativas.md` §2.

---

## 5b. Enumeración cerrada de `destreza` (6 valores — eje habilidad MCER)

```
comprension_auditiva
comprension_lectora
expresion_escrita
expresion_oral
interaccion_oral
mediacion
```

**Restricciones:**
- Lista de strings (no string suelto).
- Mínimo 1 elemento.
- Orden alfabético obligatorio.
- Cero duplicados.

---

## 5c. Enumeración cerrada de `enfoque` (6 valores — eje dominio de contenido)

```
gramatica
vocabulario
comunicacion
pronunciacion_ortografia
cultura
transversal
```

---

## 5d. Enumeración cerrada de `tiempo` verbal (5 valores)

Usado en `actividad.tiempos_y_verbos[].tiempo` y en el agregado top-level. Cubre tanto **tiempos finitos** (formas conjugadas en persona y número) como la categoría **forma no personal del verbo**, cuando esta se trabaja pedagógicamente fuera de perífrasis. En NC1 la única forma no personal con presencia real es el **infinitivo**; `Participio` y `Gerundio` no aparecen en el corpus y por tanto no entran en el enum. Si NC2 los introduce, se amplían por expansión controlada (regla "Naturaleza del contrato").

```
Presente
Pretérito indefinido
Imperativo
Perífrasis
Infinitivo
```

> Criterios y qué usos pedagógicos viven dentro de cada tiempo → `reglas-operativas.md` §5.1.

---

## 6. Schema del bloque de autoevaluación (top-level opcional)

```jsonc
"autoevaluacion": {
  "pagina": <int>,
  "instruccion_original": <str literal>,
  "opciones": [str, str, str],
  "emoticonos": <bool>
}
```

**Valores fijos en NC1:**
- `instruccion_original`: `"Mis resultados en esta unidad son:"`.
- `opciones`: `["MUY BUENOS", "BUENOS", "NO MUY BUENOS"]`.
- `emoticonos`: `true`.

---

## 7. Enumeración cerrada de `tipo_cuadro` (5 valores)

```
gramatical
lexical
pronunciacion_ortografia
cultural
comunicativo
```

---

## 8. Enumeración cerrada de `seccion` (7 valores normalizados)

```
vocabulario
gramatica
comunicacion
destrezas
cultura
evaluacion
reflexion
```

---

## 9. Estructura de los 4 bloques consolidados

Los 4 bloques top-level (`vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`) recogen, agregadas por unidad, las referencias canónicas que las actividades y los cuadros han declarado en sus 4 listas tipadas. Cada bloque tiene su shape concreto (§9.1–§9.4). Los apartados §9.5 y §9.6 describen dos contratos transversales compartidos por los 4 bloques: el formato canónico de `fuentes` y la forma del campo `descripcion`.

---

### 9.1. Estructura de `vocabulario_consolidado`

Objeto con 2 sub-bloques: `principal` y `recurrente`. **Categorías canónicas:** de `campos-semanticos-canonicos.json` (registry). **Fuente PCIC paralela:** `pcic-a1-vocabulario.json`.

```jsonc
"vocabulario_consolidado": {
  "principal":  { "<categoria_canonica>": <entrada>, ... },
  "recurrente": { "<categoria_canonica>": <entrada>, ... }
}
```

**Shape de cada entrada (categoría):**

```jsonc
"<categoria_canonica>": {
  "items": [
    { "palabra": <str>, "fuentes": [<formato_fuente>, ...] },
    ...
  ],
  "fuentes":     [<formato_fuente>, ...],    // unión agregada de fuentes de todos los items
  "descripcion": { "U<n>": <str>, ... }      // texto libre por unidad — ver §9.6
}
```

### 9.2. Estructura de `tiempos_y_verbos_consolidado`

Lista plana de objetos, una entrada por lema verbal:

```jsonc
"tiempos_y_verbos_consolidado": [
  {
    "lema":            <str>,                  // canónico de verbos-canonicos.json
    "tipo_de_verbo":   [str],                  // categoría sintáctico-semántica, lista
                                               //   (copulativo, transitivo, pronominal,
                                               //   reflexivo, ...). Ortogonal a la morfología.
    "rasgo_por_tiempo": {                      // clasificación morfológica por tiempo / forma
      "Presente":             <str>,           // valor del enum por tiempo (ver registry)
      "Pretérito indefinido": <str>,           // opcional, solo si aplica
      "Imperativo":           <str>,           // opcional, solo si aplica
      "Infinitivo":           <str>            // opcional, solo si la unidad trabaja la forma no personal
    },
    "tiempos":         [str],                  // tiempos en los que el lema se conjuga en el curso
    "formas_trabajadas": [str],                // unión agregada de formas trabajadas
                                               //   de todas las actividades + cuadros
    "fuentes":         [<formato_fuente>, ...], // ver §9.5
    "descripcion":     { "U<n>": <str>, ... }   // texto libre por unidad
  },
  ...
]
```

**Notas:**

- Una entrada por lema único. Si un lema aparece en varias actividades, se agrega aquí una sola vez con sus fuentes acumuladas.
- La lista es plana (no anidada por tiempo). La jerarquía pedagógica (tiempo → uso → rasgo → verbo) vive en fase 2 como lógica de proyección, no aquí.

> Detalle del registry verbal (`verbos-canonicos.json`), criterios de inclusión, ejemplos canónicos → `reglas-operativas.md`.

---

### 9.3. Estructura de `gramatica_consolidada`

Mismo shape que `vocabulario_consolidado` (§9.1): 2 sub-bloques con entradas por categoría canónica.

```jsonc
"gramatica_consolidada": {
  "principal":  { "<categoria_canonica>": <entrada>, ... },
  "recurrente": { "<categoria_canonica>": <entrada>, ... }
}
```

**Shape de cada entrada:** idéntico a §9.1 (con `items`, `fuentes`, `descripcion`).

**Categorías canónicas:** de `gramatica-canonica.json` (registry). **Fuente PCIC paralela:** `pcic-a1-gramatica.json`.

---

### 9.4. Estructura de `pronunciacion_ortografia_consolidada`

Mismo shape que `vocabulario_consolidado` (§9.1).

```jsonc
"pronunciacion_ortografia_consolidada": {
  "principal":  { "<categoria_canonica>": <entrada>, ... },
  "recurrente": { "<categoria_canonica>": <entrada>, ... }
}
```

**Categorías canónicas:** de `pronunciacion-ortografia-canonica.json` (registry). **Fuente PCIC paralela:** `pcic-a1-pronunciacion-ortografia.json` (sub-bloques `pronunciacion` y `ortografia`).

---

### 9.5. Formato canónico de `fuentes`

Cada elemento de `fuentes` es un string que cumple la expresión regular:

```
^(p\d+-act\d+(@R)?|cuadro@p\d+(#\d+)?)$
```

- `pNN-actMM` — fuente de actividad. Puede llevar sufijo `@R`.
- `cuadro@pNN[#K]` — fuente de cuadro (con `#K` opcional si hay varios cuadros en la misma página). **No admite sufijo `@R`** (los cuadros no tienen campo `respuestas`).
- Sufijo opcional `@R` — solo válido en fuentes de actividad. Indica que la palabra aparece únicamente en el campo `respuestas` de una actividad de **producción** (`produccion_escrita_guiada`, `produccion_escrita_libre`, `expresion_oral_libre`, `expresion_escrita_libre`, `tarea_final`, `interaccion_oral`). Indica output producido por el alumno, no input leído del libro.

**Ejemplos válidos:** `"p13-act5"`, `"cuadro@p14"`, `"cuadro@p20#3"`, `"p15-act6@R"`.

### 9.6. Campo `descripcion` 

Diccionario con clave = unidad donde aparece la categoría, valor = texto libre que explica qué se enseña.

**Obligatoriedad:** obligatoria en cada entrada del sub-bloque `principal`. Opcional en `recurrente`.

**Ejemplo:**

```jsonc
"Pronombre sujeto": {
  "items": [...],
  "fuentes": [...],
  "descripcion": {
    "U1": "PCIC A1 §7.1.1 — Pronombres personales en función de sujeto..."
  }
}
```

> Criterios de qué entra en `principal` vs `recurrente`, cómo se redacta `descripcion` (referencia PCIC), y la lógica de 3 pasos para `recurrente` → `reglas-operativas.md` §5.1.

---

## 10. Estructura de `respuestas` y sub-objetos `audio`/`imagen`/`video`

### `respuestas`

- **Siempre presente** en cada actividad.
- Tipo: lista de strings.
- Puede ser lista vacía si la actividad no tiene respuesta esperada.

### `audio`, `imagen`, `video`

- **Siempre presentes como sub-objetos** en cada actividad.

```jsonc
"audio":  { "presente": <bool>, "pista": <int opcional>,
            "transcripcion": <str opcional> }
"imagen": { "presente": <bool>, "descripcion": <str — obligatorio si presente=true> }
"video":  { "presente": <bool> }
```

**Restricción condicional:** si `imagen.presente == true`, entonces `imagen.descripcion` debe estar presente y no vacío.

**Sobre `audio.transcripcion`:** opcional. Si está presente, contiene la transcripción literal del audio. Solo entonces el contenido del audio cuenta como fuente válida (ver `reglas-operativas.md` regla 11).

---

## 11. `_nota_unidad_atipica` (clave opcional top-level)

```jsonc
"_nota_unidad_atipica": <str>
```

- Solo presente en unidades atípicas (ej. U0 "Punto de partida" pre-A1.1).

---

## 12. `datos.items_libro` (estructura)

Literalidad obligatoria.

- Tipo: lista de strings.
- Presente dentro de `actividad.datos`.
- Obligatoria en actividades de tipo `completa_huecos`, `ordena`, `clasifica`, `seleccion_multiple`, `verdadero_falso`.

---

## 13. Sincronía con el validador

Este schema y `scripts/validar_inventario.py` son contratos paralelos. El validador debe chequear, sin excepción:

- Cada clave declarada **obligatoria** aquí (en particular los 3 ejes por actividad `tipo`/`destreza`/`enfoque` y los 4 bloques top-level consolidados).
- Cada **enumeración cerrada**: `tipo` (§5), `destreza` (§5b), `enfoque` (§5c), `tiempo` (§5d), `tipo_cuadro` (§7), `seccion` (§8), `autoevaluacion.opciones` NC1 (§6) — rechazar todo valor fuera del set.
- Cada **restricción condicional**: `imagen.descripcion` obligatoria si `imagen.presente=true` (§10); `autoevaluacion` con valores fijos NC1 cuando `curso=="nc1"` (§6); `destreza` en orden alfabético y sin duplicados (§5b); referencias canónicas existentes en los registries (`campos-semanticos-canonicos.json`, `verbos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`); formato de `fuentes` (§9.5 regex); `descripcion` obligatoria en cada entrada de `principal` de cada bloque consolidado.
- Cada **clave opcional del top-level** (`autoevaluacion`, `_nota_unidad_atipica`, `_decisiones_ia`, `_migracion_rediseno`) debe figurar en `CLAVES_TOP_OPCIONALES` del validador para no emitir aviso. Las marcas internas que viven dentro de actividad o de entrada de categoría (`_funcion_ambigua`, `_decisiones_ia` en actividad, `_pendiente_canon`) **no entran** en esa lista; el validador las trata según §14 (las bloqueantes como error duro).
- Cada **marca interna que bloquea cierre** (`_pendiente_canon`, `_funcion_ambigua`) debe detectarse como error duro (§14).

Cualquier divergencia entre este schema y el validador es un bug que se resuelve antes del cierre.

> Estado actual de la alineación validador↔schema → **Apéndice transitorio**.

---

## 14. Marcas internas declaradas en el contrato

Marcas opcionales permitidas en el JSON con su shape exacto, ubicación y ciclo de vida (resumen). El **detalle operativo del ciclo de vida** (cuándo se permiten, cuándo se resuelven, cómo escalar) vive en `reglas-operativas.md` §5.9.

| Marca | Tipo | Ubicación | Forma exacta | ¿Bloquea cierre? |
|---|---|---|---|---|
| `_pendiente_canon` | string literal | (a) Como **valor** de un campo de categoría canónica. (b) Como **clave** transitoria dentro de un sub-bloque `principal`/`recurrente` de cualquier bloque top-level consolidado. | El string literal `"_pendiente_canon"`. | **Sí** (error duro). |
| `_funcion_ambigua` | boolean | Como campo opcional dentro de una **entrada de categoría** en cualquier bloque consolidado, o dentro de una **actividad**. | `"_funcion_ambigua": true` | **Sí** (error duro). |
| `_decisiones_ia` | array de string | Como campo opcional **top-level del inventario** o **dentro de una actividad concreta**. | `"_decisiones_ia": ["U1-p13-act7: 'ella' descartado como sujeto tras preposición 'sin'", ...]` | **No.** Persistente, para auditoría. |

> La marca transitoria `_migracion_rediseno` (admitida como clave opcional top-level mientras dure la migración) se documenta en el **Apéndice transitorio**.

**Reglas comunes:**

- Toda marca empieza con prefijo `_` (subrayado).
- Las marcas que bloquean cierre (`_pendiente_canon`, `_funcion_ambigua`) deben resolverse antes de declarar un inventario cerrado.
- El validador detecta las marcas bloqueantes como error duro.

> Ciclo de vida completo (cuándo se permiten, cuándo se resuelven, cómo escalar al autor) → `reglas-operativas.md` §5.9.

---

## Apéndice transitorio — migración modelo viejo → nuevo (retirar al cierre)

> Este apéndice **no forma parte del contrato canónico del schema**. Documenta deuda de transición vigente mientras se migra la cohorte de inventarios heredados del modelo viejo al modelo nuevo. Cuando se cumplan las condiciones de retirada (más abajo), este apéndice se elimina íntegramente y el cuerpo principal queda como contrato puro.

### A.1 Estado de alineación validador ↔ schema (hoy)

Este schema describe el modelo nuevo (4 bloques top-level consolidados, 4 listas tipadas por actividad, sufijo `@R`, marcas internas declaradas). `scripts/validar_inventario.py` todavía valida el modelo viejo. La desalineación es **consciente y temporal**.

Implicaciones operativas mientras dure:

- Este schema es la autoridad sobre el shape nuevo.
- El validador produce errores falsos sobre inventarios que cumplen el shape nuevo.
- La validación contra el shape nuevo es **manual** (lectura del schema + revisión visual).
- Los inventarios viejos (U0–U9 ya extraídos, no migrados) no cumplen este schema; es esperado.

### A.2 Clave transitoria `_migracion_rediseno`

Clave opcional top-level admitida **solo mientras dure la migración**. Marca un inventario que ha sido reescrito del modelo viejo al nuevo y deja constancia de hallazgos relevantes para fase 2.

**Shape:**

```jsonc
"_migracion_rediseno": {
  "aplicada": <bool>,
  "fecha":    "<YYYY-MM-DD>",
  "anticipaciones_detectadas_para_fase_2": [<objeto>, ...]
}
```

**Ciclo de vida:** se añade al migrar un inventario viejo; persiste en el archivo durante la fase de transición; **desaparece** cuando se cumplen las condiciones de retirada del apéndice. NC2 y unidades nuevas no la usan: nacen ya en el modelo nuevo.

**¿Bloquea cierre?** No. Es metadata de migración.

### A.3 Deuda específica que `validar_inventario.py` debe absorber en Paso 3

Listado vivo de cambios canonizados en este schema que el validador aún no contempla. Se completa cuando Paso 3 cierre.

- **Enum `enfoque` (§5c)** — renombrado `fonetica` → `pronunciacion_ortografia`.
- **Enum `tipo_cuadro` (§7)** — renombrado `fonetico` → `pronunciacion_ortografia`.
- **Enum `tiempo` (§5d)** — ampliado de 4 a 5 valores: añadido `Infinitivo` para cubrir la categoría "forma no personal del verbo" trabajada fuera de perífrasis. `Participio` y `Gerundio` se descartan en NC1 por inexistencia en el corpus.
- **Top-level** — claves obligatorias nuevas (`vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`) y claves opcionales declaradas (`_decisiones_ia`, `_migracion_rediseno`).
- **Schema por actividad** — eliminados `contenido_linguistico` y `campo_semantico`; añadidas las 4 listas tipadas y las marcas internas `_funcion_ambigua`, `_decisiones_ia`.
- **`vocabulario_consolidado`** — sub-bloque `comprension` eliminado del modelo.
- **Formato de fuentes (§9.5)** — regex con sufijo `@R` para fuentes de respuesta de actividades de producción.
- **Coincidencia con `nc1-curso.json`** — los campos top-level (`unidad`, `titulo`, `paginas_libro`, `nivel`, `contenidos_indice`) deben coincidir exactamente con la entrada de la unidad en `nc1-curso.json`.
- **Desalineación `tiempos_y_verbos_consolidado` (§9.2) ↔ `verbos-canonicos.json`** — `lema`, `tipo_de_verbo`, `rasgo_por_tiempo` y `tiempos` ya alineados. Pendientes: el schema declara `formas_trabajadas` (lista de formas concretas literales del libro), `fuentes` (lista pNN-actMM/cuadro@pNN) y `descripcion` (U<n> → texto); el registry usa `apariciones` (U<n> → lista de tiempos abreviados) y `lo_que_se_trabaja` (U<n> → texto), y no guarda formas concretas. Decidir en Paso 3 qué shape gana en cada campo pendiente y alinear el otro.
- **Lista de tipos productivos que admiten sufijo `@R` (§9.5)** — los 6 tipos canónicos son `produccion_escrita_guiada`, `produccion_escrita_libre`, `expresion_oral_libre`, `expresion_escrita_libre`, `tarea_final`, `interaccion_oral`. La regla operativa que decide cuándo aplicar `@R` debe usar exactamente esta lista al migrar a `reglas-operativas.md` (Paso 2). Cualquier divergencia es bug.
- **Regla 11 sobre `audio.transcripcion` como fuente válida (§10)** — la regla operativa que declara que el audio aporta a los bloques consolidados solo cuando `audio.transcripcion` está presente debe migrarse a `reglas-operativas.md` con ese enunciado exacto.
- **Normalización de `formas_trabajadas` en consolidado.** Literalidad estricta en actividad/cuadro (incluida mayúscula inicial de frase); **minúscula** en `tiempos_y_verbos_consolidado.formas_trabajadas` al agregar. Evita duplicados artificiales (`["Tengo", "tengo"]`). El validador, al alinearse, debe comprobar que las formas del consolidado están en minúscula.
- **Suite automatizada de verificación global de integridad.** Construir un script (ampliando `scripts/validar_inventario.py` o creando `scripts/verificar_integridad.py`) que ejecute, contra TODOS los JSONs del proyecto:
  1. Cumplimiento del shape declarado en este schema (top-level, página, actividad, cuadro, 4 bloques consolidados, enumeraciones cerradas, restricciones condicionales).
  2. Toda referencia canónica usada en un inventario existe en su registry (`campos-semanticos-canonicos.json`, `verbos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`).
  3. Toda fuente cumple la regex de §9.5.
  4. Coincidencia exacta entre cabecera de cada inventario y `unidades/nc1-curso.json` (campos `unidad`, `titulo`, `paginas_libro`, `nivel`, `contenidos_indice`).
  5. Coherencia interna: `secciones` reconstruible desde `paginas_detalle`; los 4 bloques consolidados son derivables de las listas tipadas de actividades y cuadros; `formas_trabajadas` en consolidado están en minúscula.
  6. Integridad de los archivos PCIC (`pcic-a1-*.json`) contra su `_meta` declarado.
  7. Integridad de los registries (`*-canonicos.json`, `*-canonica.json`) contra su shape interno.
  8. Detección de marcas internas bloqueantes (`_pendiente_canon`, `_funcion_ambigua`) en cualquier inventario canónico (sin `_fixture_exploratoria`).
  9. Rechazo de claves `_fixture_*` o `unidad` no entero en inventarios canónicos.
  La suite debe ejecutarse en cada cierre de unidad, en cada commit relevante y antes de declarar cualquier inventario como canónico/cerrado. Resultado esperado: 0 errores y 0 avisos para inventarios canónicos; los fixtures `Np` quedan tolerados pero reportados aparte.

### A.5 Metadata extracontractual: claves `_fixture_*`

Las claves cuyo nombre empieza por `_fixture_` (típicamente `_fixture_exploratoria`) son **metadata extracontractual** del JSON: el dashboard las tolera y las pinta para revisión humana, pero **no forman parte del contrato canónico** y el validador debe **ignorarlas** (ni rechazarlas ni emitir aviso).

Convención completa:
- Solo se usan en artefactos exploratorios (fixtures) cuyo `unidad` es la cadena `"Np"` (no entero).
- Un inventario canónico (`unidad: N` entero) **no debe** llevar ninguna clave `_fixture_*`.
- El validador, al alinearse en Paso 3, debe implementar la doble regla: (a) ignorar `_fixture_*` en cualquier nivel del JSON; (b) rechazar la presencia de `_fixture_*` cuando `unidad` es entero.

> Esta lista es operativa: cualquier nueva decisión que afecte al validador se añade aquí en el momento de cerrarla.

### A.4 Condiciones de retirada del apéndice

Este apéndice se elimina, y con él la clave `_migracion_rediseno` y el aviso transitorio del header, cuando se cumplen **todas** estas condiciones:

1. U0–U9 migradas al shape nuevo y validando sin errores.
2. `scripts/validar_inventario.py` alineado con este schema.
3. `reglas-operativas.md` alineada con este schema.
4. Ningún inventario conserva `_migracion_rediseno`.
5. La validación manual deja de ser mecanismo sustitutivo del validador.
6. Se registra el cierre en `CHANGELOG.md`.
