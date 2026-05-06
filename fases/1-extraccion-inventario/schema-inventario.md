# Schema del inventario — Contrato de datos puro

> **Responsabilidad:** definir la **forma** del JSON `UX-nc1-inventario.json`. Solo estructura, tipos, obligatoriedad y restricciones validables sin contexto editorial.
>
> **No contiene:** cuándo aplica cada campo, cómo elegir el valor, reglas de población semántica, workflow de extracción, ejemplos pedagógicos ni casos históricos. Esos viven en `reglas-operativas.md` o `convenciones-y-casos.md`.
>
> **Source of truth con el validador:** este archivo y `scripts/validar_inventario.py` son contratos paralelos del mismo shape. **No pueden divergir en el momento del merge a `main`.** Cualquier divergencia se resuelve antes del merge en commit aparte (ver `REFACTOR-PROPUESTA.md` paso 5.5).
>
> **Estado:** archivo creado en A4.1 con header solo. Contenido se migra desde el `prompt.md` actual en A4.2 (ver mapeo en `REFACTOR-PROPUESTA.md` sección 4).