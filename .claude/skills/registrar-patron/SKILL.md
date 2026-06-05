---
name: registrar-patron
description: Asiste el registro de patrones observacionales en `docs/tecnicas-recurrentes.md`. Solo lectura. Propone bloques canónicos y filas de cambios; no modifica el archivo.
argument-hint: [nombre de la técnica]
arguments:
  - tecnica
allowed-tools: Read, Grep, Glob
disable-model-invocation: true
---

# Registro de patrón observacional en `docs/tecnicas-recurrentes.md`

Objetivo: asegurar formato canónico al añadir o actualizar entradas en `@docs/tecnicas-recurrentes.md`. **El skill no edita el archivo** — propone el bloque y la fila de cambios listos para pegar. La decisión editorial sigue siendo del usuario.

## Procedimiento (estricto)

1. **Lee `docs/tecnicas-recurrentes.md`** completo.
2. **Calcula el siguiente ordinal libre** para nuevas técnicas: localiza todos los headers `## N. <nombre>`, identifica el máximo N actual y propone **N+1** para entradas nuevas. Para actualizaciones, **reutiliza el ordinal existente** de la técnica encontrada.
3. **Resuelve el argumento `$tecnica`** con prioridad estricta:
   - **Coincidencia exacta** del título de sección (`## N. <nombre>`).
   - Si no hay exacta, **coincidencia normalizada** (sin acentos, sin mayúsculas, sin signos).
   - Si no hay normalizada, **coincidencia similar** por sustring o palabras clave.
   - **Coincidencia dudosa** (más de un candidato cercano): no decidir; listar candidatos en chat y pedir elección humana.
4. **Aplica el contrato según el caso:**
   - **Sin argumento**: listar las técnicas registradas con su estado + línea de arranque.
   - **Argumento inexistente**: reportar *"no existe"* + plantilla canónica de nueva entrada **con N+1 ya resuelto** + fila para tabla *Cambios*.
   - **Argumento existente**: citar entrada actual (con su ordinal real) + proponer parche mínimo (no regenerar la entrada completa) + fila para tabla *Cambios*.
   - **Coincidencia dudosa**: presentar candidatos y pedir elección.

## Plantillas canónicas

### Plantilla de nueva entrada (sección)

Para una técnica nueva, devolver el siguiente bloque con el ordinal **N** ya calculado como el siguiente libre del documento actual. Estado canónico de partida: **observada**. Si el usuario quiere proponer promoción de estado, el cambio va por la ruta de actualización (parche mínimo), no por esta plantilla base:

````markdown
## N. <Nombre canónico de la técnica>

**Descripción.** <Una frase o párrafo breve que nombra la mecánica concreta.>

**Ocurrencias.**
- UXY <bloque o rótulo> — <descripción local de cómo aparece>.
- UXY <bloque o rótulo> — <descripción local>.

**Cuándo encaja.** <Una o dos frases con el caso de aplicación natural.>

**Cuándo no.** <Una o dos frases con el caso donde forzarla resta valor.>

**Estado:** observada (corpus = <unidad o corpus actual>).
````

### Plantilla de fila para tabla *Cambios*

**Política de inserción:** la tabla `## Cambios` de `docs/tecnicas-recurrentes.md` es **cronológica ascendente**. La fila nueva se añade **al final de la tabla, con la fecha actual**, no al principio.

Formato canónico de fila:

```
| YYYY-MM-DD | <Acción concreta>. <Caso de partida o disparador del cambio.> |
```

### Plantilla de parche mínimo (actualización)

Para actualización, devolver **solo el diff necesario**, no la entrada completa. **No reasigna ordinal**: se reutiliza el N actual de la técnica. Ejemplos:

- Nueva ocurrencia → línea adicional en *Ocurrencias*:
  ```
  - U4 <bloque> — <descripción local>.
  ```
- Cambio de estado a **candidata firme** → línea reemplazada en *Estado*:
  ```
  **Estado:** candidata firme (replicada en U1 + U4 + U6).
  ```
- Cambio de estado a **promovida a regla** → línea reemplazada en *Estado*:
  ```
  **Estado:** promovida a regla (codificada en `manual-estilo-final.md §X.Y`).
  ```
- Refinamiento de *Cuándo encaja* o *Cuándo no* → frase reemplazada con cita del antes/después.

## Forma del informe

### Cabecera breve
- Argumento: `$tecnica` o *(sin argumento — listar registro)*.
- Resolución: exacta / normalizada / similar / dudosa / inexistente / lista completa.
- Si nueva técnica: ordinal propuesto **N+1** con cálculo declarado (*"último ordinal en el documento: N=4 → propuesto N=5"*).
- Si actualización: ordinal reutilizado.

### Cuerpo
- **Sin argumento**: tabla compacta con `# · Nombre · Estado · Ocurrencias (resumen)`.
- **Inexistente**: nota *"no existe"* + plantilla de nueva entrada rellenable (con ordinal resuelto, Estado de partida = observada) + fila de cambios sugerida para final de la tabla.
- **Existente**: entrada actual citada + parche mínimo propuesto + fila de cambios sugerida para final de la tabla.
- **Dudosa**: candidatos numerados con su estado y línea de arranque + pregunta directa al chat.

### Cierre
- Recordatorio breve: el skill solo propone. El usuario aplica la edición a mano sobre `docs/tecnicas-recurrentes.md` cuando dé OK. La fila nueva en `## Cambios` se inserta al final de la tabla.

## Límites duros (no negociables)

- **No** modifica `docs/tecnicas-recurrentes.md`. Solo propone bloques y filas listas para pegar.
- **No** decide promoción de estado por su cuenta. Lo propone el usuario.
- **No** propone Estado distinto de **observada** en la plantilla de nueva entrada. Promociones van por la ruta de actualización con parche mínimo.
- **No** promueve a regla. La promoción a regla activa exige tocar `manual-estilo-final.md` o equivalente — fuera del alcance de este skill.
- **No** resuelve coincidencias dudosas por inferencia; las eleva al chat para decisión humana.
- **No** regenera entradas completas en caso de actualización — solo el parche mínimo.
- **No** reasigna ordinales en actualización — el ordinal existente se reutiliza.

## Criterio de éxito del skill

Tras correr la skill, `git status` debe quedar limpio sobre `docs/tecnicas-recurrentes.md`. Si aparece modificado, el skill ha violado su contrato y debe revisarse.