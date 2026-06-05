---
name: check-final
description: Audita un archivo `final/` contra el checklist v1 de reglas codificadas de repo A. Solo lectura. Devuelve informe en chat con ✅/❌/⚠ por ítem y citas concretas. No modifica el archivo.
argument-hint: <ruta al archivo final.md>
arguments:
  - archivo
disable-model-invocation: true
---

# Auditoría de `final/` — checklist v1 canónico

Objetivo: verificar que `$archivo` cumple las reglas activas y canónicas codificadas en `@docs/manual-estilo-final.md` y `@docs/formulacion-objetivos.md`. No audita patrones pendientes (`§13` del manual) ni técnicas observacionales de `@docs/tecnicas-recurrentes.md`.

## Procedimiento (estricto)

1. **Lee el archivo auditado** completo: `$archivo`.
2. **Identifica el tipo de sección** por el nombre del archivo: `vocabulario`, `gramatica`, `comunicacion`, `destrezas`, `cultura`, `evaluacion`.
3. **Relee las autoridades canónicas** de repo A:
   - `docs/manual-estilo-final.md` — toda la doctrina activa.
   - `docs/formulacion-objetivos.md` — criterio de objetivos.
4. **Aplica el checklist v1 de 12 ítems** sobre el archivo auditado, ítem por ítem.
5. **Devuelve un informe** con cabecera + tabla + cierre.

## Checklist v1 — 12 ítems

### 1. Estructura mínima de `final/` (§2)

Apertura canónica (Insignia gamificada + Objetivo + Imprimir ficha + Insignia y obtención), headers `### Ejercicios X-Y` o `### Ejercicio X`, bloques con Objetivo + rótulos + cuerpo, ENTREGA DE INSIGNIA al cierre. Ausencia de residuos de `propuesta/` (metanotas, trazabilidad, brief de píldora, spec de tarjeta, cabeceras `# UXX —` o `## DOBLE PÁGINA`).

**Excepción Evaluación**: ver §2.1 *Evaluación — estructura específica* — apertura solo con *Objetivo* (sin *Insignia gamificada* ni *Imprimir ficha* ni *Insignia y obtención*), headers `### Versión A — ...` y `### Versión B — ...` (no `### Ejercicios X-Y`), sin *ENTREGA DE INSIGNIA*.

### 2. Convenciones específicas de la sección (§2.1)

**Comunicación — vídeo** (§2.1 *Comunicación — referencia al vídeo de la unidad*): existe la línea con formato canónico `*Buscar Vídeo de comunicación **unidad X***` (*Buscar* con mayúscula inicial; *Vídeo* con tilde y mayúscula; *unidad X* en minúscula y negrita; sin dos puntos ni guion al final). **Placement**: en el bloque 1, después del objetivo de bloque y antes de las líneas Imprimir. **Auditar formato + placement.**

**Comunicación — tarjeta de estrategia** (§2.1 *Comunicación — tarjetas de estrategia*): formato canónico `*Imprimir tarjeta de estrategia—[destreza]—*[título]**` (destreza en minúscula precede al título; título en cursiva; tres componentes separados por em-dash). **Placement**: al inicio del bloque donde se usa, junto al resto de líneas Imprimir. Caras nombradas por contenido, nunca por etiqueta *CARA A* / *CARA B*. **Auditar formato + placement + caras.**

**Evaluación — conexión a unidad siguiente** (§2.1 *Evaluación — conexión a unidad siguiente*): formato canónico `*Cierre con la conexión a la **unidad X+1**: en la próxima unidad [síntesis breve]…*` (*Cierre* como verbo; *unidad X+1* en minúscula y negrita; **una sola frase escueta**; síntesis de tres a cinco elementos). **Placement**: dentro del rótulo *AUTOEVALUACIÓN Y CIERRE*. **Auditar formato + placement + frase única → varias frases = ❌, no ⚠.**

### 3. Objetivos (`formulacion-objetivos.md`)

Un verbo, no aditivo, naturaleza correcta por sección (§2.1). Si la sección es Evaluación: test de descarte (¿podría copiarse a Comunicación sin chirriar? Si sí → ❌).

### 4. Rótulos, headers, casing (§4.2)

Rótulos imperativos en MAYÚSCULAS. Labels (*Insignia gamificada*, *Objetivo*, *Insignia y obtención*, *ENTREGA DE INSIGNIA*) con casing canónico. Headers `### Ejercicios X-Y` o `### Ejercicio X` sin "BLOQUE", sin páginas, sin título descriptivo.

**Excepción Evaluación**: ver §2.1 *Evaluación — rótulos como etiquetas de contenido* — los rótulos son etiquetas de contenido o destreza **sin verbo** (*VERBO SER*, *DATOS PERSONALES*, *AUTOEVALUACIÓN Y CIERRE*, *REALIZACIÓN ESCALONADA*, *CORRECCIÓN COLECTIVA*), también en MAYÚSCULAS. En este modelo no aplica el criterio del verbo imperativo del docente.

⚠ **El verbo del rótulo NO se audita contra banco** (repo A no tiene fuente única todavía); si un verbo chirría, marcar ⚠ con cita, nunca ❌.

### 5. Imprimir + numeración ficha/píldora + nomenclatura canónica

`Imprimir ficha X.Y—...` con formato canónico de etiqueta. *insignia* en minúscula como nombre común. *píldora* con tilde. Mención canónica del tipo de tarjeta según §6.1 *Tarjetas*: `Tarjetas de Vocabulario - <campo>` o `Tarjetas de Destreza - <destreza> - <nombre>`. Título individual de tarjeta en cursiva título-case (§6.1 nota de tipografía del título individual de tarjeta).

**No se audita correlatividad numérica de X.Y a la unidad** — sin fuente única codificada en repo A.

**El formato de la línea `Imprimir tarjeta de estrategia—...` se audita en el ítem 2** (§2.1 *Comunicación — tarjetas de estrategia*), no aquí. Evita doble cobertura.

### 6. Nomenclatura interna vetada (§6.2)

Sin `Caja 1` / `Caja 2`, sin `BLOQUE N` / `bloque 1`, sin `CARA A` / `CARA B`, sin códigos `R1` / `R2` / `B1`.

### 7. Voz del cuerpo (§10.3)

Se audita **solo el caso de §10.3**: imperativos dirigidos al docente para acciones que **físicamente realiza el estudiante** (*Abra el libro* → mal si el alumno es quien abre). Las acciones del estudiante formuladas con *"Pida que… / Dígales que… / Proponga…"* **son válidas** y NO se marcan.

### 8. Metadiscurso, sobreprescripción y referencias prohibidas (§10.1)

Sin anuncios sobre el corpus, resúmenes-balance grandilocuentes, decisiones del equipo editorial, referencias anafóricas al MD, referencias anticipatorias (excepto Evaluación, ítem 2), afirmaciones normativas redundantes sobre el libro, hipérboles, predicciones narrativas (*"saldrá X"*), respuestas ya visibles en imagen del libro, prescripción de decisiones libres del docente (paletas, mapeos, mecánicas detalladas no obligadas).

### 9. Restricciones inductivas (§10.4 y §10.5)

Solo si aparecen marcas explícitas. Estilo propositivo (*"sin formalizar la regla"*, no *"no formalice"*). Una sola marca por rótulo (normalmente la de cierre); doble marcaje → ❌.

### 10. Posible §10.6 — recuento redundante

⚠ por defecto, **NUNCA ❌ automático**. La regla §10.6 nace con gate de consulta previa al autor. Solo marcar ❌ si es caso grosero y evidente. El resto de candidatos → ⚠ con cita y nota *"posible §10.6 — confirmar"*.

### 11. Sin "bloque" en el cuerpo (§10.7)

Búsqueda de la palabra *bloque* en el cuerpo del docente. Referencias permitidas: número de ejercicio (*"el ejercicio 4"*), temporalidad (*"anteriormente"*), contenido (*"los patrones de M/F"*).

### 12. ENTREGA DE INSIGNIA (§10.8)

Aplica a todas las secciones **salvo Evaluación**. En Evaluación no se audita porque, según §2.1 *Evaluación — estructura específica*, el archivo no lleva rótulo *ENTREGA DE INSIGNIA*. En el resto de secciones:

Estructura siempre auditable: rótulo + frase obligatoria *"Mencione que por [logros], reciben la insignia ¡LEMA!"* presente. Sin línea repetida *"Entrega de insignia ¡LEMA!"* bajo el rótulo → si está, ❌.

Segunda frase cultural opcional: presente → ✅ si no plantea problema visible. ⚠ si parece **afirmación cultural no sustentada por el propio texto** (caso límite que requiere revisión humana). **No se audita verificabilidad factual con cruces externos — fuera del alcance v1.**

## Fuera del alcance v1 (no auditar)

- Patrones pendientes de codificación (§13 del manual).
- Técnicas observacionales (`docs/tecnicas-recurrentes.md`).
- Verificación cruzada con repo B.
- Existencia real de assets externos (ficha imprimible, audio, vídeo) — la regla canónica no la exige todavía.
- Enforcement fuerte de verbos de rótulo contra banco — sin fuente única en repo A.

## Forma del informe

### Cabecera breve

- **Archivo auditado**: `$archivo`
- **Sección**: <tipo identificado>
- **Conteo**: X ✅ / Y ⚠ / Z ❌

### Tabla única

| # | Regla | Veredicto | Cita y referencia |
|---|---|---|---|
| 1 | Estructura mínima `final/` (§2) | ✅ / ❌ / ⚠ | si ❌/⚠: `archivo.md:LÍNEA` + cita breve + ancla a la regla |
| 2 | Convenciones específicas de la sección (§2.1) | … | … |
| … | … | … | … |

**Convenciones de severidad:**
- **✅** cumple.
- **❌** incumplimiento claro de regla codificada. Cita obligatoria.
- **⚠** caso límite, regla parcialmente satisfecha, o revisión humana necesaria. Cita obligatoria.

**Regla de citas:**
- En ❌ y ⚠, cita obligatoria con línea del archivo auditado y referencia a la regla del manual por **título de subsección** (no por número de línea, que es frágil).
- En ✅, cita mínima solo cuando aporte valor; si no, basta confirmación breve.

### Cierre

- **Bloqueadores** (todos los ❌): lista compacta de incumplimientos que impiden cerrar la sección.
- **No bloqueantes** (⚠ menores resolubles sin consulta): lista compacta.
- **Zonas de consulta** (⚠ que requieren OK del autor, especialmente §10.6): lista con la formulación *"posible §10.6 — confirmar"* o equivalente.

## Límites duros (no negociables)

- **No** modifica el archivo auditado.
- **No** propone reescrituras automáticas. Solo informa.
- **No** introduce reglas nuevas. Aplica las codificadas en `manual-estilo-final.md` y `formulacion-objetivos.md` tal cual.
- **No** audita el verbo del rótulo contra "banco de verbos" — esa fuente no existe canónicamente en repo A. Si un verbo chirría, ⚠ con cita.
- **No** audita patrones pendientes (§13) ni técnicas observacionales.
- **No** audita existencia real de assets externos.
- **No** cruza con repo B.

## Criterio de éxito del skill

Tras correr la skill, `git status` debe quedar limpio sobre el archivo auditado. Si aparece modificado, el skill ha violado su contrato y debe revisarse.