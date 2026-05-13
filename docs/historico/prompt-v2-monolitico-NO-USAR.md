# Prompt: extracción del inventario JSON de una unidad (v2 — IA-first)

> **Versión:** v2 (2026-05-12) — modelo IA-first con validación determinista.
> **Versión anterior:** `prompt-v1-antiguo.md` (preservada como referencia histórica; no usar).
> **Quién lo usa:** Claude Code (u otro agente IA) cada vez que se procesa una unidad nueva.
> **Quién lo mantiene:** el autor + Claude Code, conforme aparecen casos nuevos.
> **Cómo se invoca:** `Procesa la unidad UX siguiendo fases/1-extraccion-inventario/prompt.md.`

---

## Principio rector

**La IA decide. El código comprueba. El humano cierra.**

- La **IA** (este agente) hace el trabajo interpretativo: extraer del PDF, clasificar contenido, asignar categorías, decidir función real de palabras ambiguas, redactar descripciones.
- El **código** (`validar_inventario.py`) verifica estructura, formato, coherencia bidireccional.
- El **humano** revisa visualmente y cierra. Sin su OK explícito, ninguna unidad se considera terminada.

---

## Las tres etapas del procesamiento

Cada unidad pasa por estas tres etapas, **en este orden estricto**:

```
PDF de la unidad
    │
    ▼  ETAPA 1 — EXTRACCIÓN (IA)
JSON crudo con paginas_detalle[] (verbatim)
    │
    ▼  ETAPA 2 — CLASIFICACIÓN (IA)
JSON enriquecido con los 4 bloques top-level + listas tipadas por actividad
    │
    ▼  ETAPA 3 — COMPROBACIÓN (código)
JSON validado (0 errores) — listo para revisión humana
    │
    ▼  REVISIÓN VISUAL (humano)
JSON congelado en disco → cierre del inventario de la unidad
```

---

## Inputs del prompt (lectura obligatoria antes de empezar)

Antes de procesar cualquier unidad, la IA debe leer:

1. **`fases/1-extraccion-inventario/REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md`** — documento de diseño. Fuente de verdad para las 14 reglas, protocolo §7bis, definiciones de `principal`/`recurrente`, doble dimensión, etc.
2. **`fases/1-extraccion-inventario/schema-inventario.md`** — shape exacto del JSON.
3. **`unidades/nc1-curso.json`** — índice maestro del libro (TODAS las unidades, no solo la actual).
4. **Los cuatro registries canónicos**:
   - `fases/1-extraccion-inventario/campos-semanticos-canonicos.json` (léxico)
   - `fases/1-extraccion-inventario/verbos-canonicos.json` (verbal)
   - `fases/1-extraccion-inventario/gramatica-canonica.json` (gramática)
   - `fases/1-extraccion-inventario/pronunciacion-ortografia-canonica.json` (pron/orto)
5. **`fases/1-extraccion-inventario/pcic-a1-gramatica.json`** — PCIC A1 (referencia para descripciones).
6. **`fases/1-extraccion-inventario/reglas-operativas.md`** y **`convenciones-y-casos.md`** — material complementario.
7. **El PDF de la unidad**: `unidades/UX/fuente/UX-nc1.pdf`.

---

# ETAPA 1 — EXTRACCIÓN

## Objetivo

Producir un JSON crudo con la **estructura física de la unidad** y **todo el texto verbatim** que el alumno ve impreso (o que escucha si hay transcripción literal del audio).

## Regla de oro (no negociable)

**El JSON debe contener el contenido visible al alumno EXACTAMENTE COMO APARECE EN EL LIBRO, no como referencia ni como interpretación.**

- Las frases con huecos se escriben con `_____` marcando el hueco (no la respuesta).
- Los textos de lectura se transcriben íntegros.
- Los diálogos se transcriben completos.
- Las opciones de selección múltiple van tal cual están redactadas.
- Las palabras del recuadro/banco van tal cual.
- Las cuadrículas (sopa de letras, etc.) van con todas sus celdas.
- Las imágenes se describen brevemente para reconstruir lo que ve el alumno (no es contenido del libro pero permite trazabilidad).

**Si en el libro hay un texto, el JSON debe poder regenerar el texto. Si hay una tabla, el JSON debe contener la tabla.**

## Procedimiento

1. **Leer todas las páginas del PDF** (`unidades/UX/fuente/UX-nc1.pdf`). Unidades regulares ~10 páginas; **U0 atípica tiene 4 páginas**.
2. **Identificar metadatos**: rango de páginas, título, nivel, fuente.
3. **Identificar secciones del índice de contenidos**:
   - Caso normal (U1-U9): 7 secciones canónicas (`vocabulario`, `gramatica`, `comunicacion`, `destrezas`, `cultura`, `evaluacion`, `reflexion`).
   - Caso atípico (U0 u otra unidad introductoria): el índice no sigue las 7 secciones. Aplicar `reglas-operativas.md` §7.
4. **Para cada página**: identificar la sección, las actividades (numeradas o no), los cuadros (con `tipo_cuadro` del enum: `gramatical`, `lexical`, `fonetico`, `cultural`, `comunicativo`) y las notas "Observa".
5. **Para cada actividad** extraer:
   - `id` (formato `UX-pYY-actN`).
   - `tipo` (enum cerrado de 20 valores, ver `schema-inventario.md` §5).
   - `destreza` (lista de valores MCER del enum cerrado de 6: `comprension_auditiva`, `comprension_lectora`, `expresion_escrita`, `expresion_oral`, `interaccion_oral`, `mediacion`; orden alfabético; sin duplicados; mínimo 1).
   - `enfoque` (string del enum cerrado de 6: `vocabulario`, `gramatica`, `comunicacion`, `cultura`, `fonetica`, `transversal`).
   - `instruccion_original` (literal, lo que el libro le dice al alumno qué hacer).
   - `datos` (estructura variable según el `tipo`: `items_libro`, `texto_completo`, `dialogo_completo`, `ejemplo_libro`, `palabras_recuadro`, `preguntas`, `opciones_respuesta`, etc.).
   - `respuestas` (lista, aunque vacía).
   - `audio`, `imagen`, `video` (sub-objetos con `presente: true/false` + detalles).
6. **Para cada cuadro**: extraer `tipo_cuadro` + `contenido` (texto verbatim, tabla, etc.).
7. **Detectar bloque de autoevaluación al pie de la última página** si existe (campo top-level `autoevaluacion`).

## Output de etapa 1

JSON con esta estructura mínima:

```jsonc
{
  "unidad": <int>,
  "curso": "nc1",
  "titulo": "...",
  "paginas_libro": "X-Y",
  "nivel": "A1.1",
  "fuente": "...",
  "contenidos_indice": { /* del índice editorial */ },
  "secciones": { /* índice top-level */ },
  "autoevaluacion": { /* si aplica */ },
  "paginas_detalle": [
    {
      "pagina": <int>,
      "seccion": "...",
      "actividades": [ { /* shape de actividad */ } ],
      "cuadros": [ { /* shape de cuadro */ } ]
    }
  ]
}
```

**Aún NO se rellenan**: `vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`. Eso es etapa 2.

---

# ETAPA 2 — CLASIFICACIÓN

## Objetivo

Enriquecer el JSON de etapa 1 asignando:

1. **Por cada actividad**: las 4 listas tipadas (`vocabulario`, `tiempos_y_verbos`, `gramatica`, `pronunciacion_ortografia`) con referencias canónicas.
2. **Top-level**: los 4 bloques consolidados (`vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`), cada uno con `principal` y `recurrente` (no `comprension` — eliminado del modelo).

## Las 14 reglas operativas — consulta obligatoria

Antes de clasificar, **debes haber leído y entender las 14 reglas** del documento de rediseño §7. Resumen operativo:

| # | Regla | Aplicación operativa |
|---|---|---|
| 1 | Cada referencia en `actividad.{vocabulario, gramatica, pronunciacion_ortografia}` es un canónico válido del registry correspondiente. | Verifica contra los 4 registries antes de declarar. |
| 1b | Para `actividad.tiempos_y_verbos`: `lema` y `tiempo` son canónicos; `formas_trabajadas` es literal del libro (no canon). | Cita el libro para `formas_trabajadas`. |
| 2 | Top-level es derivado; actividad es fuente. | Construye top-level agregando referencias de actividades + cuadros. |
| 3 | Datos literales del libro no son referencias canónicas. | `datos.items_libro` es verbatim, no canon. |
| 4 | `enfoque` es informativo, no clasificatorio. | No condiciona qué se asigna en las 4 listas tipadas. |
| 5 | Marca `_pendiente_canon` si no encuentras canónico seguro. | No inventes nombres. |
| 6 | Coherencia bidireccional actividad ↔ top-level. | Si la actividad referencia `X`, el top-level `X` lista esa actividad en `fuentes`. |
| 7 | Validación de `recurrente` en 3 pasos (antes → después → valor). | Ver protocolo abajo. |
| 8 | 🚫 Prohibido inventar palabras. | Solo entra lo que aparece literal. |
| 9 | Clasificación semántica coherente. | `campeón` no es nacionalidad, etc. |
| 10 | Trazabilidad obligatoria con formato `pXX-actYY` o `cuadro@pXX[#N]`, opcional sufijo `@R` para fuentes de respuesta. | Toda entrada con sus fuentes. |
| 11 | Solo el contenido que el alumno LEE cuenta como fuente. | Ver tabla canónica de campos abajo. |
| 12 | Lectura cruzada del índice maestro (TODAS las unidades). | Necesario para detectar anticipaciones (regla 7). |
| 13 | Descripción PCIC obligatoria en `principal` con formato `{Un: "..."}`. | Una descripción por unidad donde aparece. |
| 14 | Desambiguación funcional (principio general). | Ver protocolo §7bis abajo. |

## Tabla canónica de campos del JSON (regla 11)

Esta tabla decide qué campos son fuente válida y cuáles se excluyen:

| Campo | ¿Alumno lo lee/procesa? | Validez |
|---|---|---|
| `instruccion_original` | No (oral del profesor) | ❌ excluir |
| `datos.pasos`, `datos.pasos_a_seguir` | No (instrucciones de tarea) | ❌ excluir |
| `datos.instrucciones_adicionales`, `datos.guion_didactico` | No | ❌ excluir |
| `datos._nota`, `datos._comentario`, cualquier campo con prefijo `_` | No (nota interna) | ❌ excluir |
| `datos.subtipo`, `datos.objetivo`, `datos.objetivos` | No (metadata) | ❌ excluir |
| `imagen.descripcion` | No (descripción narrativa del extractor) | ❌ excluir |
| `audio.descripcion` (si existe, narrativa) | No | ❌ excluir |
| **`datos.items_libro`** (sin contar numerador `1`, `2`...) | Sí | ✅ contar |
| **`datos.texto_completo`** | Sí | ✅ contar |
| **`datos.dialogo_completo`** | Sí | ✅ contar |
| **`datos.ejemplo_libro`**, **`datos.ejemplos_modelo`** | Sí | ✅ contar |
| **`datos.palabras_recuadro`** | Sí | ✅ contar |
| **`datos.preguntas`**, **`datos.opciones_respuesta`** | Sí | ✅ contar |
| **`datos.dialogos_modelo`**, **`datos.expresiones_dadas`** | Sí | ✅ contar |
| **`respuestas`** (de actividades de selección/comprensión) | Sí | ✅ contar |
| **`respuestas`** (de actividades de **producción**) | Producido por el alumno | ✅ contar **marcado con sufijo `@R`** |
| **`audio.transcripcion`** (si existe transcripción literal) | Sí (escucha) | ✅ contar |
| **Contenido de `cuadros`** (`cuadro.contenido` y subcampos) | Sí | ✅ contar |

### Marcado `@R` para respuestas de producción

Si la actividad tiene `tipo` ∈ `{produccion_escrita_guiada, produccion_escrita_libre, expresion_oral_libre, expresion_escrita_libre, tarea_final, interaccion_oral}`, sus `respuestas` se contabilizan **con sufijo `@R`** en la fuente:

- Ejemplo: `"p15-act6@R"` indica que la palabra aparece en la respuesta producida por el alumno, no en el contenido leído. El dashboard renderiza estas fuentes con color distinto.

### Paréntesis-anotación

Dentro de cualquier campo de contenido, **excluye** paréntesis con anotaciones del extractor que describen cómo aparece visualmente algo:

- `(con círculo morado en el libro)`, `(subrayado)`, `(en negrita)`, `(en cursiva)`, `(tachado)`, `(resaltado)`, `(ilustrado)`.

Limpia esos paréntesis antes de buscar palabras. El contenido legítimo del paréntesis se mantiene si no es anotación visual.

## Protocolo §7bis — verificación por categoría (regla 14)

Para cada palabra que decidas asignar como referencia de una categoría, verifica que **la función real coincide con la definición de la categoría**. Casos típicos:

**Pronombres personales sujeto** (PCIC §7.1.1):
- ✅ Sujeto explícito antepuesto al verbo: "**Yo** me llamo Pedro."
- ✅ En tabla de paradigmas (etiqueta del paradigma trabajado).
- ❌ Tras preposición → es pronombre tónico, no sujeto: "sin **ella**", "con **él**", "para **mí**".
- ❌ Referencia deíctica a una letra/sonido: "¿Con h o sin **ella**?" donde *ella* refiere a la letra h.

**Conjunciones** (PCIC §14):
- ✅ Une dos elementos del mismo rango: "rojo **y** azul".
- ❌ Como letra (en actividades de abecedario, en `-X/-Y`, en `letra X`, en `/X/`).
- ❌ En descripción morfológica.

**Adverbios de afirmación/negación** (PCIC §8):
- ✅ `no` antepuesto a verbo, `sí/no` como respuesta breve.

**Adverbios de grado/intensificadores** (PCIC §8):
- ✅ `muy` antepuesto a adjetivo/adverbio.

**Cuantificadores comparativos** (PCIC §8):
- ✅ `más` como comparativo de superioridad.
- ❌ En operación aritmética: "tres más cinco = ocho".

**Artículos definidos/indefinidos** (PCIC §3):
- ✅ Antepuesto a sustantivo.

**Vocabulario**:
- ✅ Uso real en frase: "Tengo un **libro** y una **mochila**".
- ❌ Mención metalingüística: "la palabra **libro**".

**Si una palabra aparece con función ambigua**, marca la entrada con `_funcion_ambigua: true` y escala al autor.

## Lógica de los 3 pasos para `recurrente` (regla 7)

Para que un término entre como `recurrente` en U(n) en cualquier bloque:

1. **Paso 1 (antes)**: ¿está declarado en el índice maestro de alguna unidad anterior U(n-k)?
   - **Sí** → recurrente legítimo (repaso). Fin.
   - **No** → paso 2.
2. **Paso 2 (después)**: ¿es canónico en una unidad posterior U(n+k)?
   - **Sí** → **anticipación**: NO se codifica como `recurrente`. Se registra en `_migracion_rediseno.anticipaciones_detectadas_para_fase_2`. Fin.
   - **No** → paso 3.
3. **Paso 3 (valor pedagógico)**: ¿es contenido necesario para lo que U(n) construye?
   - **Sí** → entra en `recurrente` con descripción explícita de por qué.
   - **No** → no entra; queda fuera del consolidado.

**Pre-condiciones del filtro**:
- Frecuencia mínima ≥ 2 apariciones en contenido (excluyendo instrucción, regla 11).
- No está en `principal` (índice de la propia unidad).
- Función verificada (regla 14).

## Asignación de categorías PCIC

Para cada item / palabra que clasifiques, usa el nombre de la categoría **directamente del registry correspondiente** (que viene de PCIC A1 o del índice editorial). No inventes nombres. Si dudas, marca `_pendiente_canon`.

## Descripción por categoría (regla 13)

Cada entrada en `principal` lleva un campo `descripcion` con texto libre **por unidad**:

```jsonc
"Pronombre sujeto": {
  "items": [...],
  "fuentes": [...],
  "descripcion": {
    "U1": "PCIC A1 §7.1.1 — Pronombres personales en función de sujeto. ... En U1 son necesarios para construir paradigmas verbales (ser, tener, llamarse) y contrastar tú/usted."
  },
  "_pcic_referencia": "7.1.1 Pronombre sujeto"
}
```

La descripción debe:
- Empezar citando el código PCIC (ej. "PCIC A1 §7.1.1").
- Continuar con definición funcional breve.
- Acabar con cómo se trabaja en esa unidad concreta.

## Doble dimensión (verbal + gramatical)

Un verbo entra en ambos registries (`verbos-canonicos.json` + `gramatica-canonica.json`) si el libro trabaja simultáneamente:
1. El lema/paradigma verbal (morfología).
2. Una construcción/oposición/función verbal como contenido gramatical.

Casos típicos NC1: `ser`, `estar`, `gustar`, `doler`, `haber` (solo `hay`), `querer`, `ir`.

## Output de etapa 2

JSON enriquecido con todos los bloques top-level y las 4 listas por actividad rellenas. Cero marcas `_pendiente_canon` o `_funcion_ambigua` sin resolver.

---

# ETAPA 3 — COMPROBACIÓN

## Objetivo

Validar estructura, formato, coherencia. Sin trabajo interpretativo.

## Cómo

```bash
python3 scripts/validar_inventario.py X
```

**Esperado**: 0 errores y 0 avisos. (1 aviso intencional aceptable si la unidad es atípica con `_nota_unidad_atipica`.)

## Qué valida (resumen)

- Shape JSON correcto (claves obligatorias, tipos).
- Enums cerrados respetados (`tipo`, `destreza`, `enfoque`, `tipo_cuadro`).
- Formato canónico de fuentes (`pXX-actYY`, `cuadro@pXX[#N]`, opcional `@R`).
- Coherencia bidireccional actividad ↔ top-level.
- Cada `principal` lleva `descripcion`.
- Cada item con ≥ 1 fuente.
- Referencias al canon existen (lookup contra los 4 registries).
- Cero marcas `_pendiente_canon` / `_funcion_ambigua` en el JSON final.

## Qué NO valida (es trabajo de etapa 2)

- Si la función de una palabra coincide con su categoría.
- Si una palabra está en uso metalingüístico o real.
- Si una descripción es correcta pedagógicamente.

---

# Cierre — revisión visual humana

Antes de declarar el inventario terminado:

1. **El autor abre el dashboard** (`python3 diagrama.py` → http://localhost:8080).
2. **Selecciona la unidad UX** y recorre 2-3 páginas al azar contrastando con el PDF.
3. **Si todo OK** → commit dedicado con el JSON. La unidad se considera cerrada y se congela.
4. **Si hay error** → feedback documentado. La IA refina el `prompt.md` (este archivo) o el JSON, y se re-ejecuta etapa 2.

## Política de re-ejecución

- El `prompt.md` (este archivo) se mejora cuando aparecen casos nuevos. Cada cambio es un commit.
- Las unidades anteriores **no se re-extraen automáticamente** al cambiar el prompt. Solo se re-extraen por decisión explícita del autor.
- Cada unidad cerrada queda congelada en disco. Solo se re-toca por bug o cambio de canon.

---

# Marcas de estado y trazabilidad

Marcas que el agente puede usar durante el procesamiento:

- `_pendiente_canon`: literal en una clave o valor de categoría cuando no hay canónico seguro. Bloquea el cierre.
- `_funcion_ambigua: true`: en una entrada cuando la función no se puede determinar con confianza. Bloquea el cierre.
- `_decisiones_ia: [...]`: lista opcional de notas del agente sobre decisiones no triviales (para auditoría).
- `_migracion_rediseno.anticipaciones_detectadas_para_fase_2`: lista de términos que pasarían la frecuencia pero son canónicos de unidades posteriores (regla 7 paso 2).

Todas las marcas que empiecen con `_` son metadata interna; el código las preserva pero no las cuenta como contenido.

---

# Definición de éxito final

Una unidad UX se considera cerrada cuando:

1. ✅ Etapa 3 (`validar_inventario.py X`) devuelve 0 errores y 0 avisos.
2. ✅ Cero marcas `_pendiente_canon` o `_funcion_ambigua` en el JSON.
3. ✅ El autor ha revisado visualmente 2-3 páginas al azar y aprobado.
4. ✅ Cualquier caso no contemplado en este prompt o en el documento de rediseño ha sido escalado al autor antes del cierre.

Si una de estas condiciones falla, la unidad NO está cerrada y debe revisarse.
