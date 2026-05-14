# Corrida inválida sobre contrato viejo (2026-05-14)

> Baseline diagnóstica. **No es certificación de v10.115.**

## Qué pasó

El 2026-05-14 se lanzó un chat limpio para certificar el contrato v10.115 (reset IA-first de `reglas-operativas.md` + alineación de docs de fase 1). El chat se ejecutó por error contra el **worktree principal** (`main`, en v10.114), no contra el worktree paralelo `../guia-prueba-v10.115/` (rama `v10.115-wip`) donde vivía el contrato a probar.

Resultado: el agente trabajó contra el contrato viejo (numeración §5.10-§5.14, 6 tipos productivos, etc.). Los artefactos generados quedaron sobre el árbol activo en `unidades/U4-propuesta/` y fueron movidos aquí para preservar trazabilidad.

## Valor diagnóstico (lo que SÍ sirve a pesar del setup roto)

1. **Aplicación mecánica de `@R`.** El agente puso `@R` sobre cuadros (`cuadro@p44#1@R`) y sobre tipos no productivos (`completa_huecos@R`, `seleccion_multiple@R`, `escucha_y_repite@R`). Bug trasladable a v10.115 si la prosa de §6.5 no fuerza chequeo previo del `tipo`. Materializado en el JSON (línea 55 y posteriores) y reportado en el informe §5 (línea 140).
2. **Errores semánticos en verbos.** El JSON propone `lema: "haber"` para la forma *hacemos* (debería ser `hacer`); mezcla `tomamos` bajo `comer`. Indica que el barrido verbal sin verificación contra el registry produce errores sustantivos, independientes del contrato.
3. **§0.1 no se cumplió.** El informe declara "corrida sin autor presente" y registra 10 decisiones como `_decisiones_ia` sin escalado real. La regla §0.1 (propuesta-en-chat) exige interacción, no auto-resolución. Hallazgo de proceso.

## Qué NO sirve

- Cualquier diagnóstico positivo sobre v10.115 (no se probó).
- Cualquier comparación numérica de citas §X.Y (vienen del viejo).

## Decisión

Re-ejecutar la prueba **exclusivamente** en `../guia-prueba-v10.115/` (rama `v10.115-wip`), con guardrails de aborto y endurecimiento previo de §6.5 (ver bitácora v10.115 en CHANGELOG + REVIEW).
