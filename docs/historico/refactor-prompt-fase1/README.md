# Histórico — Refactor del prompt de fase 1

Carpeta de archivo de documentos operativamente cerrados pero que se conservan como rastro del proceso de refactor.

## Contenido

- **`REFACTOR-PROPUESTA.md`** — Plan ejecutable del refactor de fase 1 (extracción de inventario). Trazó la arquitectura objetivo (split del prompt monolítico de 547 líneas en 5 archivos por capa), los 8 sub-pasos (A4.0 → A4.6 + A4.5.5 cross-check obligatorio), criterios de gate, frontera de capas no negociable, riesgos y mitigaciones. Cerrado al 100% con el merge de `refactor/prompt-fase-1` → `main` en commit `110e722` (v10.69).

- **`REFACTOR-WORKTREE.md`** — Documentación del worktree dedicado (`/Users/armandocruz/Desktop/guia-didactica-refactor/` sobre la rama `refactor/prompt-fase-1`) usado durante toda la ejecución del refactor. Explica setup, reglas de uso, comandos de verificación y procedimiento de cierre. Útil como plantilla si se planteara otro refactor con worktree dedicado en el futuro.

## Por qué están aquí y no en `fases/1-extraccion-inventario/`

Ambos eran artefactos **del proceso** de refactor, no del producto. Una vez ejecutado y mergeado el plan, dejan de ser operativos: `fases/1-extraccion-inventario/` debe contener solo lo que un agente o un humano usa al extraer un inventario nuevo (CLAUDE.md, prompt.md, schema-inventario.md, reglas-operativas.md, convenciones-y-casos.md). Mezclar plan ejecutable y artefacto vivo confunde el contrato de la fase.

Los archivos se movieron con `git mv` para preservar historial. Las referencias históricas en `CHANGELOG.md` y en la bitácora de `REVIEW.md` mantienen el path original (`fases/1-extraccion-inventario/REFACTOR-*.md`) porque describen el estado del repositorio en el momento del commit; reescribirlas sería revisionismo.

## Cuándo consultar

- Si se planea **otro refactor de fase** (fase 2 onwards): plantilla del proceso, sub-pasos canónicos, criterios de gate, formulación del cross-check schema↔validador.
- Si se necesita **reabrir alguna decisión** tomada durante el refactor: el plan ejecutable contiene el razonamiento y los criterios.
- Si alguien necesita **entender cómo funcionó el worktree dedicado**: setup paso a paso en `REFACTOR-WORKTREE.md`.

## Lo que NO entra en esta carpeta

- `viejo/` (sistema CrewAI v5 anterior, intocable hasta su eliminación final autorizada por el autor) — esa zona tiene sus propias reglas y permanece sin cambios.
- Artefactos vivos de fase 1 — siguen en `fases/1-extraccion-inventario/`.
- Bitácoras y CHANGELOG — siguen en raíz, son source of truth viva del progreso.
