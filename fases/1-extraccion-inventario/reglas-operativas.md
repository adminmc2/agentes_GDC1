# Reglas operativas — Decisión, clasificación, población y unidades atípicas

> **Responsabilidad:** guía de decisión compacta y priorizada. Reúne lo que el modelo necesita decidir durante la extracción: qué tipo asignar, qué clasificar como cuadro/actividad/nota, cómo poblar campos cuyo shape ya está fijado en `schema-inventario.md`, cómo tratar unidades atípicas.
>
> **No contiene:** forma del JSON (vive en `schema-inventario.md`), convenciones de transcripción específicas (sílaba tónica, "primer ítem resuelto", marcadores de diálogos, formato de sopas de letras), ni casos históricos resueltos. Esos viven en `convenciones-y-casos.md` (a poblar en A4.2c).
>
> **Single source of truth de precedencias:** las reglas de precedencia (qué clasificar como actividad / cuadro / nota / autoevaluación, en qué orden, con qué excepciones) viven **exclusivamente aquí**. Cualquier otro archivo que necesite invocarlas lo hace por referencia, no por copia. Si una precedencia aparece reescrita en `prompt.md`, `CLAUDE.md` o cualquier otro artefacto, es un bug del refactor.

---

## 1. Precedencia entre actividad / cuadro / nota / autoevaluación

Para cada elemento visible en una página del libro, determinar en este orden qué es:

1. **¿Tiene número de actividad** (1, 2, 3...) **y pide producción del alumno** (escuchar, repetir, escribir, relacionar...)? → **Actividad** con `tipo` de la taxonomía cerrada (§2).
2. **¿Es "Para aprender"?** → Siempre **actividad** (`tipo: produccion_escrita_guiada`, `datos.subtipo: "para_aprender"`), aunque no tenga número. Excepción explícita a la regla general.
3. **¿Es "Observa"?** → Siempre **nota**, aunque use el imperativo "Observa". Excepción explícita: "Observa" no pide producción del alumno; llama la atención sobre información de referencia. Nunca se convierte en actividad. **Dónde va según su contexto:**
   - Si acompaña a una **actividad**: en `datos._nota` de esa actividad.
   - Si acompaña a un **cuadro**: en `cuadro.observaciones` (campo opcional del schema del cuadro, ver `schema-inventario.md` §4).
4. **¿Es una tabla o recuadro de referencia sin número ni instrucción de producción?** → `cuadro` con `tipo_cuadro` apropiado (§3).
5. **¿Es el bloque "Mis resultados en esta unidad son: …"** que aparece al pie de la última página de cierre con tres opciones y emoticonos? → **bloque `autoevaluacion` top-level** (no actividad, no cuadro, no nota). Ver §6.

**Precedencia:** las excepciones explícitas (reglas 2, 3, 5) tienen prioridad sobre la regla general (regla 1). La regla general solo aplica cuando ninguna excepción encaja.

---

## 2. Cómo asignar `tipo` a una actividad (taxonomía cerrada de 19 valores)

Enumeración cerrada en `schema-inventario.md` §5.

### 2.1 Regla operativa: `tipo` = la acción específica del enunciado

> **El `tipo` describe la acción que el enunciado del libro pide al alumno.** Si el enunciado encadena varias acciones, el tipo lo determina **la última acción que pide producción concreta**. Si el enunciado solo pide absorber input (leer, escuchar, mirar) sin acción posterior, el tipo refleja literalmente esa absorción.
>
> El `tipo` es independiente de la `destreza`. La `destreza` describe **qué destrezas lingüísticas ejercita el alumno** (ver §2.3); puede combinar varias con `+`. Una misma mecánica puede ejercitar destrezas distintas; no se confunden.

### 2.2 Tabla canónica de los 19 tipos

| `tipo` | Acción del enunciado | Ejemplos del libro |
|---|---|---|
| `lee_y_escucha` | "Lee y escucha" / "Lee y escucha el diálogo" — solo input, sin acción posterior | "Lee y escucha." (fichas de presentación) |
| `ver_video` | "Mira el vídeo" — input con video, con o sin texto/audio acompañante | "Mira el vídeo o lee y escucha el diálogo." |
| `escucha_y_repite` | "Escucha y repite" | vocabulario, abecedario, interrogativos |
| `escucha_y_responde` | "Escucha y responde" oralmente, sin texto delante | (genérico) |
| `completa_huecos` | "Completa", "Completa con palabras del recuadro", "Lee y completa", "Escucha y completa la tabla/ficha" | rellenar huecos en frases, fichas, tablas |
| `relaciona` | "Relaciona X con Y" (típicamente con líneas conectoras) | números↔palabras, preguntas↔respuestas |
| `ordena` | "Ordena estos elementos" | (genérico) |
| `clasifica` | "Clasifica X en categorías" | (genérico) |
| `seleccion_multiple` | "Subraya el verbo correcto", "Marca", "Elige", "Escucha y marca" | subrayar entre alternativas, marcar bingo |
| `verdadero_falso` | "Marca verdadero o falso" | (genérico) |
| `responder_preguntas_cerradas` | "Contesta a las preguntas" cuando la respuesta es **concreta y sale del input** (texto leído, audio, video) | "Lee y contesta a las preguntas" sobre un texto |
| `responder_preguntas_abiertas` | "Contesta a las preguntas" cuando la respuesta es **personal/libre del alumno** | "Contesta: ¿Cómo te llamas? ¿De dónde eres?" |
| `interaccion_oral` | "En parejas", "Pregunta y contesta a tu compañero", "Saluda a tu compañero" | diálogo en parejas con estructura |
| `expresion_oral_libre` | "Preséntate", "Practica con palabras nuevas", "Presenta a tu compañero a la clase" | producción oral sin guion cerrado |
| `produccion_escrita_guiada` | "Escribe frases con…", "Forma frases", "Coloca el artículo", "Realiza las sumas y escribe", "Describe X con sus colores" | producción escrita siguiendo modelo/regla, sin huecos predefinidos |
| `expresion_escrita_libre` | "Escribe a tu amigo sobre…", "Escribe un correo", "Escribe un texto sobre…" | redacción libre sobre un tema |
| `busqueda_informacion` | "Busca información sobre…" | (genérico) |
| `tarea_final` | "Cread vuestro propio diálogo" + pasos en grupo (tarea colaborativa final) | crear y representar un diálogo |
| `juego` | "Juega a…" | "Juega al veo, veo" (cuando la actividad es jugar como tal, no como interacción genérica) |

**Reglas de desempate cuando el enunciado encadena varias acciones:**

1. **Si hay video** → `ver_video` (aunque también haya audio o texto).
2. **Si el enunciado pide una acción de manipulación posterior** (completa, marca, relaciona, subraya, ordena, clasifica) → el tipo es esa acción, no el input. Ej.: "Lee y completa" → `completa_huecos`; "Escucha y marca" → `seleccion_multiple`.
3. **Si el enunciado pide responder preguntas:**
   - Respuesta concreta del input → `responder_preguntas_cerradas`.
   - Respuesta personal/libre → `responder_preguntas_abiertas`.
4. **Si el enunciado solo pide input** (leer, escuchar, mirar) sin acción posterior → `lee_y_escucha` o `ver_video` según el medio.

### 2.3 Sobre la `destreza` (campo separado)

`destreza` es un string independiente de `tipo`. Combina con `+` las destrezas lingüísticas que el alumno ejercita en la actividad. Valores típicos:
- `comprension_lectora` (leer)
- `comprension_oral` (escuchar)
- `produccion_escrita` (escribir)
- `produccion_oral` (hablar)
- `interaccion` (interactuar oralmente)

Ejemplos de combinaciones del oráculo:
- "Escucha y completa las fichas" → `tipo: completa_huecos` + `destreza: comprension_oral+produccion_escrita`.
- "Lee y contesta preguntas" → `tipo: responder_preguntas_cerradas` + `destreza: comprension_lectora+produccion_escrita`.
- "Mira el vídeo o lee y escucha" → `tipo: ver_video` + `destreza: comprension_oral+comprension_lectora`.

### 2.4 Política de la enumeración

- La enumeración de 19 valores es **provisional y revisable a nivel global del proyecto**. No se amplía ni se cambia ad hoc por unidad. Cualquier modificación del set requiere decisión cerrada en PROCESO-MAESTRO antes de aplicarse en `schema-inventario.md` y en `validar_inventario.py` (regla de no-divergencia).
- Ante un caso ambiguo durante una extracción nueva: marcar como TODO en el JSON y consultar al autor antes de cerrar el inventario.

---

## 3. Cómo asignar `tipo_cuadro` (5 valores)

Enumeración cerrada en `schema-inventario.md` §7.

Cuando una página tiene un cuadro de referencia (clasificado según §1 regla 4), asignar `tipo_cuadro` según su naturaleza pedagógica:

- **`gramatical`** — tablas de conjugación, paradigmas morfológicos (artículos, género, posesivos, interrogativos, demostrativos), reglas ortográficas de uso gramatical.
- **`lexical`** — listas ilustradas de vocabulario, tablas de campos semánticos, colores, familias de palabras.
- **`fonetico`** — cuadros de pronunciación u ortografía fonética (c/qu, z/c, g/gu, entonación, acento...).
- **`cultural`** — cuadros con información sociocultural (saludos, costumbres, diálogos en contexto cultural, fórmulas sociales).
- **`comunicativo`** — cuadros de uso pragmático (registro, formalidad/informalidad, turnos de conversación, cortesía).

> **Ortogonalidad:** `seccion` de la página y `tipo_cuadro` son independientes. Un cuadro fonético puede aparecer en la sección `gramatica`; un cuadro léxico puede estar en `vocabulario`. No forzar que coincidan.

**Capturar todo el contenido visible del cuadro** (filas, columnas, celdas, ejemplos al pie) en `cuadro.contenido`.

---

## 4. Qué NO es un cuadro: "Para aprender" y "Observa"

Las siguientes cajas visuales del libro **NO son cuadros** aunque aparezcan visualmente como recuadros (ver §1 reglas 2 y 3):

**"Para aprender"** — Cajas con consejos o estrategias pedagógicas para el alumno (cómo llevar un cuaderno de vocabulario, cómo estudiar...). Son **actividades**, no cuadros. Usar:
```jsonc
{
  "id": "UX-pYY-actNN",
  "tipo": "produccion_escrita_guiada",
  "datos": { "subtipo": "para_aprender", ... }
}
```

**"Observa"** — Notas que llaman la atención sobre algún aspecto del idioma (variantes en Hispanoamérica, combinaciones de letras...). Son **notas**, no actividades ni cuadros:
- Si acompaña a una **actividad**: en `datos._nota` de esa actividad.
- Si acompaña a un **cuadro**: en `cuadro.observaciones`.

---

## 5. Reglas de población de campos (shape en schema, contenido aquí)

### 5.1 `vocabulario_consolidado`: distribución entre los 3 bloques

Tres bloques, cada uno agrupado por categoría/campo semántico:

- **`principal`** — Vocabulario **declarado en el índice de la unidad** (ej: si el índice dice "Vocabulario: Parientes", aquí va el léxico de parentesco trabajado en la sección Vocabulario). Agrupado por campo semántico (Familia, Profesiones, Lugares, etc.).
- **`recurrente`** — Vocabulario que aparece en **varias secciones** de la unidad (no solo Vocabulario). Por ejemplo, si "merendar" aparece en Vocabulario Y en Comunicación Y en Destrezas, va aquí. Agrupado por categoría temática.
- **`comprension`** — Léxico que **aparece y afecta la comprensión** del estudiante aunque no se trabaje explícitamente. Por ejemplo, palabras del cómic en la sección Cultura, asignaturas mencionadas, conectores básicos. Agrupado por categoría.

**`_descripcion`** dentro de cada bloque explica de qué va. Útil al revisar el JSON.

### 5.2 `secciones` (top-level): construcción del índice

- **Si una sección no existe en la unidad**, dejarla con `{ "paginas": [], "actividades_ids": [] }` (no omitir la clave).
- **`actividades_ids`** lista los IDs de actividad de cada sección, **en orden de aparición**. Permite acceso directo sin recorrer todas las páginas.

### 5.3 `seccion` por página: cómo determinarla

Mapeo canónico avalado por la práctica actual (oráculo: inventarios trackeados U0, U1, U3):

| Header del libro | Valor normalizado | Avalado en |
|---|---|---|
| Vocabulario | `vocabulario` | U1, U3 |
| Gramática | `gramatica` | U1, U3 |
| Comunicación | `comunicacion` | U1, U3 |
| Destrezas | `destrezas` | U1, U3 |
| Cultura | `cultura` | U1, U3 |
| Página de cierre de unidad con bloque `autoevaluacion` (U1-p21, U3-p43) | `evaluacion` | U1-p21, U3-p43 |

**Sobre `reflexion`:** está incluido en la enumeración cerrada de `seccion` (`schema-inventario.md` §8) pero **no tiene uso documentado en los inventarios actuales** (U0, U1, U3 no asignan `reflexion` a ninguna página). El criterio para distinguir `evaluacion` vs `reflexion` se documentará cuando aparezca el primer caso real. Hasta entonces, **usar `evaluacion` por consistencia con el oráculo**.

**Páginas que continúan una sección anterior** (típicamente con etiqueta visual tipo "(cont.)"): se les asigna **la misma clave normalizada** que la página origen. La etiqueta "(cont.)" del libro NO va al JSON; la sección sigue siendo la misma.

**Caso unidades atípicas:** ver §7.

### 5.4 `respuestas`: contenido y formato

Estructural en schema (`schema-inventario.md` §10): siempre presente como lista, vacía si no aplica.

**Cuando aplica:** recoge la respuesta esperada tal como aparece en el libro del profesor (suele estar marcada en color o en el margen). Cada respuesta como un string en la lista.

**Formatos:**
- **Selección múltiple:** indicar la opción correcta junto con su texto: `"3. → c) Una mezcla de dibujo y texto"`.
- **Verdadero/Falso:** `"1. La frase X — V"`.
- **Cloze / completar:** la respuesta completa o la palabra que va en el hueco, según convenga reproducir el ítem original (ver `convenciones-y-casos.md` para ejemplos).

### 5.5 `audio`, `imagen`, `video`: cuándo `presente=true`

Estructural en schema (`schema-inventario.md` §10): siempre presentes como sub-objetos.

**Marcar `presente=true`** cuando la actividad realmente requiere ese medio: hay un ícono de audio/video junto a la actividad, hay una imagen visible que el alumno consulta, hay un video referenciado. En caso contrario `presente=false`.

**`imagen.descripcion`:** obligatoria si `imagen.presente=true` (la restricción la aplica el validador). Suficientemente detallada para que un agente que no ve la imagen pueda entender qué muestra.

### 5.6 `campo_semantico`: cuándo aplica

Estructural en schema (`schema-inventario.md` §10): str opcional.

**Cuándo se usa:** cuando el contenido lingüístico de la actividad pertenece a un campo semántico identificable (Familia, Profesiones, Lugares, etc.).

**Decisión pendiente del autor:** ¿solo en sección vocabulario o en cualquier sección que toque vocabulario? Por ahora, **liberal**: cualquier actividad cuyo contenido pertenezca a un campo semántico lo lleva.

### 5.7 `datos.items_libro`: literalidad obligatoria

Estructural en schema (`schema-inventario.md` §12): lista de strings, obligatoria en actividades de cierto tipo (lista canónica en `validar_inventario.py:TIPOS_QUE_REQUIEREN_ITEMS`).

**Regla de literalidad (la más importante):** `items_libro` debe contener **el texto literal del libro**, con los huecos marcados como `_____` (5 guiones bajos). Nunca sustituir el enunciado por la respuesta. Nunca inventar el enunciado.

**Para qué tipos aplica:** completar huecos, opción múltiple, ordenar, clasificar, relacionar, verdadero/falso, y similares.

> Ejemplos correctos e incorrectos → `convenciones-y-casos.md` (a migrar en A4.2c).

---

## 6. Cuándo se incluye u omite el bloque `autoevaluacion`

`autoevaluacion` es opcional a nivel top-level (forma del campo en `schema-inventario.md` §6).

**Regla de decisión:**
- **Unidad regular (U1-U9):** el bloque está presente. Aparece al pie de la última página con tres opciones canónicas y emoticonos.
- **Unidad atípica sin bloque (ej. U0 "Punto de partida"):** el campo `autoevaluacion` se omite por completo (no se pone `null` ni vacío; simplemente no aparece la clave).

**Indicadores en el libro:**
- Si la última página de la unidad muestra el bloque "Mis resultados en esta unidad son: …" con tres opciones y emoticonos → presente.
- Si no aparece visualmente → omitido.

---

## 7. Reglas para unidades atípicas (introductorias)

Algunas unidades NO tienen las 5 secciones canónicas (vocabulario / gramática / comunicación / destrezas / cultura). Caso típico: la unidad introductoria **U0 "Punto de partida"** que es pre-A1.

**Cuando ocurra:**
1. Mapear todo el contenido a la sección que más se ajuste (en U0: `vocabulario`, porque todo el contenido es léxico-fonético).
2. Las demás secciones canónicas quedan vacías: `{ "paginas": [], "actividades_ids": [] }`.
3. Añadir clave top-level `_nota_unidad_atipica` con explicación de por qué es atípica y cómo se mapeó (forma de la clave en `schema-inventario.md` §11).
4. En `contenidos_indice`, las secciones que no aplican llevan el valor `"(no aplica en esta unidad introductoria)"`.

> Ejemplo JSON canónico de U0 → `convenciones-y-casos.md` (a migrar en A4.2c).

---

## 8. Estado del source of truth de las reglas decisionales

Tras A4.2b, el reparto entre archivos queda así:

| Tipo de regla | Archivo |
|---|---|
| Forma del JSON (estructura, tipos, enumeraciones, restricciones validables) | `schema-inventario.md` |
| Precedencias entre actividad/cuadro/nota/autoevaluación | **este archivo** (§1) |
| Distinción `completa_huecos` vs `produccion_escrita_guiada` | **este archivo** (§2.1) — antes en `prompt.md`, restaurado en v10.51, migrado aquí en A4.2b |
| Criterios para asignar cada uno de los 19 tipos | **canonizados en §2** (regla operativa: el `tipo` = la acción específica del enunciado del libro) |
| Cómo asignar `tipo_cuadro` | **este archivo** (§3) |
| "Para aprender" / "Observa" | **este archivo** (§4) |
| Reglas de población de cada campo | **este archivo** (§5) |
| Bloque `autoevaluacion`: cuándo presente/omitido | **este archivo** (§6) |
| Unidades atípicas: cuándo y cómo aplicar | **este archivo** (§7) |
| Convenciones de transcripción del libro al JSON (sílaba tónica, primer ítem resuelto, marcadores de diálogos, formato de sopas de letras) | `convenciones-y-casos.md` (a poblar en A4.2c) |
| Ejemplos correctos/incorrectos de `items_libro` | `convenciones-y-casos.md` (a poblar en A4.2c) |
| Casos históricos resueltos | `convenciones-y-casos.md` (a poblar en A4.2c) |
