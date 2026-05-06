# Schema del inventario — Contrato de datos puro

> **Responsabilidad:** definir la **forma** del JSON `UX-nc1-inventario.json`. Solo estructura, tipos, obligatoriedad y restricciones validables sin contexto editorial.
>
> **No contiene:** cuándo aplica cada campo, cómo elegir el valor, reglas de población semántica, workflow de extracción, ejemplos pedagógicos ni casos históricos. Esos viven en `reglas-operativas.md` o `convenciones-y-casos.md`.
>
> **Source of truth con el validador:** este archivo y `scripts/validar_inventario.py` son contratos paralelos del mismo shape. **No pueden divergir en el momento del merge a `main`.** Cualquier divergencia se resuelve antes del merge en commit aparte (ver `REFACTOR-PROPUESTA.md` paso 5.5).

---

## 1. Estructura top-level (10 claves obligatorias + 1 opcional)

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
  "vocabulario_consolidado": {
    "principal": { "_descripcion": "...", "<Campo>": [palabras] },
    "recurrente": { "_descripcion": "...", "<Categoria>": [palabras] },
    "comprension": { "_descripcion": "...", "<Categoria>": [palabras] }
  },
  "secciones": {
    "vocabulario":  { "paginas": [int], "actividades_ids": [str] },
    "gramatica":    { "paginas": [int], "actividades_ids": [str] },
    "comunicacion": { "paginas": [int], "actividades_ids": [str] },
    "destrezas":    { "paginas": [int], "actividades_ids": [str] },
    "cultura":      { "paginas": [int], "actividades_ids": [str] },
    "evaluacion":   { "paginas": [int], "actividades_ids": [str] },
    "reflexion":    { "paginas": [int], "actividades_ids": [str] }
  },
  "autoevaluacion": <bloque, opcional — ver §6>,
  "_nota_unidad_atipica": <str, opcional — ver §11>,
  "paginas_detalle": [<página>, ...]
}
```

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
  "numero": <int>,
  "tipo": <de la taxonomía cerrada — ver §5>,
  "destreza": <str: comprension_oral | produccion_oral | ... combinables con +>,
  "instruccion_original": <str literal del libro>,
  "contenido_linguistico": [str],
  "campo_semantico": <str opcional — ver §10>,
  "audio":  { "presente": <bool>, "pista": <int opcional> },
  "imagen": { "presente": <bool>, "descripcion": <str obligatorio si presente=true> },
  "video":  { "presente": <bool> },
  "respuestas": [str],   // SIEMPRE presente. Lista vacía si no aplica.
  "datos": {             // saco abierto para CONTENIDO LITERAL DEL LIBRO
    "subtipo": <str opcional — sopa_de_letras, dialogo_video, programacion_tv, ...>,
    "items_libro": [str],          // contenido tal cual con _____ donde haya huecos
    "texto_completo": <str>,       // texto de lectura completo
    "dialogo_completo": [str],     // líneas del diálogo con [1], [2] en huecos
    "preguntas": [str],            // lista literal de preguntas
    "preguntas_opciones": [{...}], // selección múltiple
    "cuadricula": [[str]],         // sopa de letras
    "frases": [str],               // listado de frases
    "ejemplo_libro": <str>,        // ejemplo entre comillas/cursiva
    "texto_modelo": <str>,         // texto que el alumno toma como modelo
    "nombres_dados": [str],        // listado de nombres/palabras del recuadro
    "palabras_recuadro": [str],
    "horarios_digitales": {<id>: <hora>},
    "programas_tv": [str],
    "peliculas_cartelera": [str],
    "personajes": [str],
    "titulo_dialogo": <str>,
    "pasos": [str],
    "reglas_foneticas": [str],
    "palabras_modelo": [str],
    "expresiones_dadas": [str],
    "afirmaciones_a_corregir": [str],
    "texto_correo": <str>,
    "ejemplos_modelo": [str],
    "objetivo_palabras": <int>
    // ... cualquier dato específico que NO encaje en los campos canónicos
  }
}
```

> **Política de extensibilidad de `datos`:** saco abierto. Cualquier campo nuevo que no esté en la lista anterior se documenta y se añade al schema con la regla de población correspondiente en `reglas-operativas.md`.

---

## 4. Schema por cuadro

```jsonc
{
  "tipo_cuadro": <enum de 5 valores — ver §7>,
  "titulo": <str>,
  "contenido": {
    "tipo": <str — tabla_conjugacion | tabla_interrogativos | tabla_posesivos | lista_ilustrada | tabla_colores | ...>,
    // estructura libre según el cuadro, capturando TODO el contenido visible
    "ejemplos": [str]
  },
  "observaciones": <str, opcional> // texto literal de la caja "Observa" si acompaña al cuadro
}
```

> **Nota:** `tipo_cuadro` describe la categoría pedagógica del cuadro (gramatical, lexical, etc.). `contenido.tipo` describe su estructura interna (cómo está maquetado: tabla, lista, etc.). Son complementarios, no redundantes.

---

## 5. Taxonomía cerrada de tipos de actividad (17 valores)

Enumeración. Usar EXACTAMENTE uno de estos valores en `actividad.tipo`. Cualquier otro valor falla la validación.

```
escucha_y_repite
escucha_y_responde
completa_huecos
relaciona
ordena
clasifica
seleccion_multiple
verdadero_falso
interaccion_oral
expresion_oral_libre
produccion_escrita_guiada
expresion_escrita_libre
comprension_lectora
comprension_auditiva
busqueda_informacion
tarea_final
juego
```

> Enumeración provisional y revisable a nivel global del proyecto. Cualquier ampliación o cambio del set entra como decisión cerrada en PROCESO-MAESTRO antes de aplicarse aquí y en el validador.

> Criterios de cuándo asignar cada tipo (incluida la distinción `completa_huecos` vs `produccion_escrita_guiada`) y workflow ante casos ambiguos → `reglas-operativas.md`.

---

## 6. Schema del bloque de autoevaluación (top-level opcional)

```jsonc
"autoevaluacion": {
  "pagina": <int>,                        // página donde aparece el bloque
  "instruccion_original": <str literal>,  // ej: "Mis resultados en esta unidad son:"
  "opciones": [str, str, str],            // exactamente 3 elementos
  "emoticonos": <bool>                    // true si van acompañadas de emoticonos
}
```

**Restricciones estructurales:**
- Los 4 sub-campos (`pagina`, `instruccion_original`, `opciones`, `emoticonos`) son obligatorios cuando el bloque está presente.
- `opciones` debe ser exactamente una lista de 3 strings.
- El bloque entero es **opcional a nivel top-level**.

> Cuándo se omite el bloque y cuándo está presente → `reglas-operativas.md`.

**Valores fijos en NC1** (validables mecánicamente cuando `curso == "nc1"`):
- `instruccion_original`: `"Mis resultados en esta unidad son:"`.
- `opciones`: `["MUY BUENOS", "BUENOS", "NO MUY BUENOS"]` (las tres siempre, en este orden).
- `emoticonos`: `true`.

---

## 7. Enumeración cerrada de `tipo_cuadro` (5 valores)

```
gramatical
lexical
fonetico
cultural
comunicativo
```

> Los criterios de cuándo asignar cada uno (qué cuenta como gramatical / lexical / fonetico / cultural / comunicativo) viven en `reglas-operativas.md`. Aquí solo está la enumeración de valores válidos.

---

## 8. Enumeración cerrada de `seccion` (7 valores normalizados)

Valor de la clave `seccion` dentro de cada página, y de las claves del top-level `secciones`:

```
vocabulario
gramatica
comunicacion
destrezas
cultura
evaluacion
reflexion
```

> Valor normalizado. **NO** se admite texto libre. Solo uno de los 7 valores listados arriba.

> Cómo determinar la sección de una página dada (incluido el caso de páginas que continúan una sección) → `reglas-operativas.md`.

---

## 9. Estructura de `vocabulario_consolidado`

Objeto con exactamente 3 sub-bloques nombrados, cada uno con la misma estructura interna:

```jsonc
"vocabulario_consolidado": {
  "principal":   { "_descripcion": <str>, "<categoria>": [str], ... },
  "recurrente":  { "_descripcion": <str>, "<categoria>": [str], ... },
  "comprension": { "_descripcion": <str>, "<categoria>": [str], ... }
}
```

- Cada sub-bloque es un objeto cuyas claves son nombres de categoría (campo semántico, categoría temática, etc.) y los valores son listas de strings (palabras).
- La clave `_descripcion` (con guion bajo, no es categoría) explica de qué va cada bloque.

> Los criterios de **qué palabras cuentan como `principal` / `recurrente` / `comprension`** viven en `reglas-operativas.md`. Aquí solo está la forma del objeto.

---

## 10. Estructura de `respuestas`, `campo_semantico`, `audio`/`imagen`/`video`

### `respuestas`
- **Siempre presente** en cada actividad.
- Tipo: lista de strings.
- Puede ser lista vacía si la actividad no tiene respuesta esperada.

> Qué contenido va en la lista (formato según contexto: numeración, huecos, diálogos) → `reglas-operativas.md`.

### `campo_semantico`
- Opcional a nivel de actividad.
- Tipo: string.

> Cuándo aplica y cómo elegir el valor → `reglas-operativas.md`.

### `audio`, `imagen`, `video`
- **Siempre presentes como sub-objetos** en cada actividad.
- Patrón estructural:

```jsonc
"audio":  { "presente": <bool>, "pista": <int opcional> }
"imagen": { "presente": <bool>, "descripcion": <str — obligatorio si presente=true> }
"video":  { "presente": <bool> }
```

- **Restricción condicional validable mecánicamente:** si `imagen.presente == true`, entonces `imagen.descripcion` debe estar presente y no vacío.

> Cuándo marcar `presente=true` → `reglas-operativas.md`.

---

## 11. `_nota_unidad_atipica` (clave opcional contractual top-level)

```jsonc
"_nota_unidad_atipica": <str>
```

- Tipo: string.
- Aparece a nivel top-level del JSON.
- **Solo presente en unidades atípicas** (ej. U0 "Punto de partida" pre-A1.1).
- **Tratamiento estricto:** es contractual, no "tolerada-no-canónica". El validador la reconoce como opcional sin emitir aviso. Si el validador no la incluye en `CLAVES_TOP_OPCIONALES`, hay divergencia con este schema y se resuelve antes del merge (ver §13).

> Cuándo añadirla, qué contenido escribir y cómo mapear las secciones vacías de unidades atípicas → `reglas-operativas.md`. Ejemplo JSON canónico de U0 → `convenciones-y-casos.md`.

---

## 12. `datos.items_libro` (estructura)

- Tipo: lista de strings.
- Presente dentro de `actividad.datos`.
- Obligatoria en actividades de tipo `completa_huecos`, `relaciona`, `ordena`, `clasifica`, `seleccion_multiple`, `verdadero_falso` (la lista canónica vive en `validar_inventario.py:TIPOS_QUE_REQUIEREN_ITEMS`, contrato paralelo).

> La regla de **literalidad obligatoria** del contenido (texto exacto del libro, huecos como `_____`, no inventar enunciados) → `reglas-operativas.md`. Ejemplos correctos e incorrectos → `convenciones-y-casos.md`.

---

## 13. Source of truth con `scripts/validar_inventario.py`

Este archivo y `scripts/validar_inventario.py` son **contratos paralelos del mismo shape**. La regla de no-divergencia es estricta:

- Cada clave declarada **obligatoria** aquí debe ser chequeada como obligatoria por el validador.
- Cada **enumeración cerrada** (17 tipos de actividad, 5 valores de `tipo_cuadro`, 7 secciones canónicas, 3 opciones canónicas de autoevaluación NC1) debe ser rechazada por el validador si aparece un valor fuera del set.
- Cada **restricción condicional** (ej. `imagen.descripcion` obligatoria si `imagen.presente=true`, `autoevaluacion` con valores fijos NC1 cuando `curso=="nc1"`) debe ser aplicada por el validador.
- Cada **clave opcional declarada** (`autoevaluacion`, `_nota_unidad_atipica`) debe estar en `CLAVES_TOP_OPCIONALES` del validador para que no emita aviso.

**Si se detecta divergencia,** se resuelve **antes del merge** alineando uno de los dos artefactos en commit aparte. La divergencia no es un estado válido de cierre del refactor (ver `REFACTOR-PROPUESTA.md` paso 5.5).
