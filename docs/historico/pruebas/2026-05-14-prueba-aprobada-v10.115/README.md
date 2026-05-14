# Prueba aprobada del contrato v10.115 — fixture U4-propuesta (2026-05-14)

> Evidencia forense. **No es inventario canónico.** Esta fixture certificó el protocolo de extracción de v10.115 sobre las páginas 42-46 de U4. Se conserva tal cual fue generada por el agente — no se ha retocado post-fix.

## Alcance

- Worktree de prueba: `../guia-prueba-v10.115/` (rama `v10.115-wip`, eliminada tras cierre).
- Páginas extraídas: 42-46 (vocabulario, gramática, comunicación parcial).
- Chat limpio, IA-first puro, sin red de seguridad humana intermedia.

## Los 9 ejes — todos aprobados

| # | Eje | Resultado |
|---|---|---|
| 1 | Pureza de entrada | ✅ 10 archivos en cadena, exclusiones declaradas |
| 2 | Navegabilidad del contrato | ✅ Cero consultas al `-viejo` |
| 3 | Coherencia de refs `§X.Y` | ✅ Toda cita verificable; cero §5.10-§5.14 viejas |
| 4 | Política propuesta-en-chat (§0.1) | ✅ 15 propuestas abiertas, cero autoresoluciones |
| 5 | Procedimiento §0.3 A/B/C | ✅ Las 3 dimensiones barridas (C legítimamente vacío en alcance parcial) |
| 6 | Familia `@R` (§6.5) | ✅ Chequeo previo documentado, 0 sufijos aplicados, 0 cuadros con `@R` |
| 7 | No dependencia normativa del `-viejo` | ✅ Cero invocaciones |
| 8 | Conformidad de fixture (shape JSON) | ✅ `unidad: "4p"`, `_fixture_exploratoria` completo |
| 9 | Conformidad de fixture (convención de fase) | ✅ Carpeta, nombre, informe junto al JSON |

## Bug crítico de la corrida fallida anterior — eliminado

La corrida fallida del 2026-05-14 sobre el contrato viejo v10.114 (archivada en `../pruebas-fallidas/2026-05-14-corrida-invalida-v10.115/`) había aplicado `@R` mecánicamente a tipos no productivos (`completa_huecos@R`, `seleccion_multiple@R`, `escucha_y_repite@R`) y a cuadros (`cuadro@p44#1@R`), violando schema §9.5.

Tras el endurecimiento de §6.5 con chequeo previo obligatorio del `tipo`, esta corrida produjo **0 sufijos `@R` aplicados** con tabla de verificación caso por caso documentada en el informe §5. **Bug resuelto.**

## Defecto de salida promovido a mejora de contrato

La fixture codificó `comer` con forma infinitiva (`"comer"`) bajo `tiempo: "Presente"` en `U4-propuesta-nc1-inventario.json:466`. Esto reveló una incoherencia heredada en el contrato: `Perífrasis` figuraba en el enum `tiempo`, mezclando categoría flexiva (tiempo verbal) con categoría sintáctica (estructura perifrástica). Adoptada **opción B** post-prueba:

- `Perífrasis` retirado del enum `tiempo` (queda con 4 valores).
- Añadido campo opcional `estructura_perifrastica: <str>` en `actividad.tiempos_y_verbos[]`.
- §5.2 de `reglas-operativas.md` reformulada con **regla de anticipación por lema** (resuelve la asimetría `ir`/`hacer`).
- Propagado a `schema-inventario.md`, `reglas-operativas.md`, `glosario.md`.

## Defectos menores preservados como evidencia pre-fix

No se reescriben — sirven para documentar el momento del descubrimiento:

1. **`primer plato` y `segundo plato` con `fuentes: []`** (`U4-propuesta-nc1-inventario.json:114-115`). Invención del agente: esos términos viven en pp.48-49 ("Comer en España"), fuera del alcance pp.42-46 de la fixture.
2. **Asimetría `ir` vs `hacer`**: `ir` entró como perífrasis aunque su lema sea canónico de U6+; `hacer` se excluyó por la misma razón. Decisión intuitiva del agente, no regla. **Resuelto por la nueva §5.2.**
3. **Doble entrada `comer` infinitivo + conjugada** (`U4-propuesta-nc1-inventario.json:466` + entradas conjugadas en otras actividades). El infinitivo subordinado a `quieres comer` se codificó como entrada separada. **Resuelto por la opción B**: el infinitivo complemento queda implícito en `estructura_perifrastica` del auxiliar, no se registra como entrada separada.

Estas anomalías ya no se reproducirían si se ejecutara una corrida nueva sobre el contrato v10.115 post-fix. Re-ejecutar para confirmarlo se descartó por no añadir evidencia estructural nueva.

## Decisiones documentadas en `_decisiones_ia` (15 entradas)

Propuestas abiertas escaladas al autor, no autoresueltas. Resumen en el informe §3. Su resolución no bloquea el cierre de v10.115 — son input para el dashboard y para iteraciones futuras.
