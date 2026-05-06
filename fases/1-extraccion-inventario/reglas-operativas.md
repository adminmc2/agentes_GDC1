# Reglas operativas — Decisión, clasificación, población y unidades atípicas

> **Responsabilidad:** guía de decisión compacta y priorizada. Reúne lo que el modelo necesita decidir durante la extracción: qué tipo asignar, qué clasificar como cuadro/actividad/nota, cómo poblar campos cuyo shape ya está fijado en `schema-inventario.md`, cómo tratar unidades atípicas.
>
> **No contiene:** forma del JSON (vive en `schema-inventario.md`), convenciones de transcripción específicas (sílaba tónica, "primer ítem resuelto"), ni casos históricos resueltos. Esos viven en `convenciones-y-casos.md`.
>
> **Single source of truth de precedencias:** las reglas de precedencia (qué clasificar como actividad / cuadro / nota / autoevaluación, en qué orden, con qué excepciones) viven **exclusivamente aquí**. Cualquier otro archivo que necesite invocarlas lo hace por referencia, no por copia. Si una precedencia aparece reescrita en `prompt.md`, `CLAUDE.md` o cualquier otro artefacto, es un bug del refactor.
>
> **Estado:** archivo en construcción. El grueso del contenido se migra desde el `prompt.md` actual en A4.2b (ver mapeo en `REFACTOR-PROPUESTA.md` sección 4, filas con destino "→ reglas-operativas.md"). Lo que aparece debajo son fragmentos absorbidos en v10.49 al limpiar fugas decisionales que se habían colado en `schema-inventario.md` durante A4.2a.

---

## Cuándo se incluye u omite el bloque `autoevaluacion`

`autoevaluacion` es opcional a nivel top-level (forma del campo en `schema-inventario.md` §6).

**Regla de decisión:**
- **Unidad regular (U1-U9):** el bloque está presente. Aparece al pie de la última página con tres opciones canónicas y emoticonos.
- **Unidad atípica sin bloque (ej. U0 "Punto de partida"):** el campo `autoevaluacion` se omite por completo (no se pone `null` ni vacío; simplemente no aparece la clave).

**Indicadores en el libro:**
- Si la última página de la unidad muestra el bloque "Mis resultados en esta unidad son: …" con tres opciones y emoticonos → presente.
- Si no aparece visualmente → omitido.

---

## Cómo determinar la sección de una página

`seccion` toma uno de 7 valores normalizados (forma en `schema-inventario.md` §8).

**Procedimiento:**
1. Identificar el header visible en la página (encabezado o pestaña del libro).
2. Mapear el header al valor normalizado correspondiente:

| Header del libro | Valor normalizado |
|---|---|
| Vocabulario | `vocabulario` |
| Gramática | `gramatica` |
| Comunicación | `comunicacion` |
| Destrezas | `destrezas` |
| Cultura | `cultura` |
| Evaluación / Practica lo aprendido | `evaluacion` |
| Reflexión / Autoevaluación / cierre | `reflexion` |

**Páginas que continúan una sección anterior** (típicamente con etiqueta visual tipo "(cont.)"): se les asigna **la misma clave normalizada** que la página origen. La etiqueta "(cont.)" del libro NO va al JSON; la sección sigue siendo la misma.

**Caso unidades atípicas:** si una página no encaja en ninguna de las 7 categorías → ver "Reglas para unidades atípicas" más abajo (a migrar en A4.2b completo).

---

## Criterios para asignar `tipo` (taxonomía cerrada de 17 valores)

Enumeración cerrada en `schema-inventario.md` §5.

**Pendiente de migración completa en A4.2b.** El criterio canónico para cada uno de los 17 tipos vive aún en `prompt.md` y se moverá aquí en el siguiente sub-paso.

**Ya documentado** (absorbido en v10.49 desde la fuga workflow de schema):
- La enumeración de 17 valores es **provisional y revisable a nivel global del proyecto**. No se amplía ni se cambia ad hoc por unidad. Cualquier modificación del set requiere decisión cerrada en PROCESO-MAESTRO antes de aplicarse en `schema-inventario.md` y en `validar_inventario.py`.
- Ante casos ambiguos durante la extracción (un contenido del libro que no encaja claro en ningún tipo): marcar como TODO y consultar al autor antes de cerrar el inventario.

---

## (Pendiente de A4.2b)

El resto del contenido decisional vive todavía en `prompt.md` y se migra en A4.2b según el mapeo de `REFACTOR-PROPUESTA.md` sección 4:

- Precedencia entre actividad / cuadro / nota / autoevaluación.
- "Para aprender" → actividad.
- "Observa" → nota; cuándo va en `datos._nota`, cuándo en `cuadro.observaciones`.
- Cómo asignar `tipo_cuadro` (gramatical / lexical / fonetico / cultural / comunicativo).
- Distinción `completa_huecos` vs `produccion_escrita_guiada`.
- Reglas de población de `respuestas`, `campo_semantico`, `vocabulario_consolidado` (qué cuenta como `principal`/`recurrente`/`comprension`), `audio`/`imagen`/`video` (cuándo `presente=true`).
- Construcción del índice top-level `secciones`.
- Reglas para unidades atípicas (cuándo añadir `_nota_unidad_atipica`, mapeo de secciones inaplicables).
- Literalidad obligatoria de `datos.items_libro` (texto exacto del libro, huecos como `_____`).
