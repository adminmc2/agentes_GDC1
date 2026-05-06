# Reglas operativas — Decisión, clasificación, población y unidades atípicas

> **Responsabilidad:** guía de decisión compacta y priorizada. Reúne lo que el modelo necesita decidir durante la extracción: qué tipo asignar, qué clasificar como cuadro/actividad/nota, cómo poblar campos cuyo shape ya está fijado en `schema-inventario.md`, cómo tratar unidades atípicas.
>
> **No contiene:** forma del JSON (vive en `schema-inventario.md`), convenciones de transcripción específicas (sílaba tónica, "primer ítem resuelto"), ni casos históricos resueltos. Esos viven en `convenciones-y-casos.md`.
>
> **Single source of truth de precedencias:** las reglas de precedencia (qué clasificar como actividad / cuadro / nota / autoevaluación, en qué orden, con qué excepciones) viven **exclusivamente aquí**. Cualquier otro archivo que necesite invocarlas lo hace por referencia, no por copia. Si una precedencia aparece reescrita en `prompt.md`, `CLAUDE.md` o cualquier otro artefacto, es un bug del refactor.
>
> **Estado:** archivo creado en A4.1 con header solo. Contenido se migra desde el `prompt.md` actual en A4.2 (ver mapeo en `REFACTOR-PROPUESTA.md` sección 4, filas con destino "→ reglas-operativas.md").