# Procesamiento de unidad — prompt dry-run con worktree, revisión iterativa e integración diferida

> **Propósito:** prompt envoltorio para procesar una unidad en chat limpio dentro de un **worktree aislado**, sin tocar el árbol principal del repo, hasta que pase **todas** las pruebas (validador, suite global, dashboard, revisión visual del autor) e integre **el ejecutor coordinador** (no el agente del chat de procesamiento).
>
> **Por qué este protocolo:** evita contaminación del árbol principal con extracciones a medias, evita perder el inventario anterior si la nueva extracción es defectuosa, y obliga a revisión visual en dashboard antes de cualquier integración.
>
> **Cómo se usa:**
> 1. El ejecutor coordinador (la persona o chat principal) prepara el worktree `../guia-proc-U[X]/` con rama `proc-u[x]-wip` (igual que se hizo en v10.115 con `guia-prueba-v10.115`).
> 2. El ejecutor abre Claude Code dentro de ese worktree y pega el cuerpo del prompt (debajo de la línea horizontal).
> 3. El agente del chat de procesamiento trabaja **solo dentro del worktree**, presenta inventario en chat, itera con el autor.
> 4. Tras OK del autor, el agente escribe el JSON candidato **en el worktree**, valida con `validar_inventario.py`, lo deja preparado.
> 5. El ejecutor coordinador revisa en dashboard, integra al árbol principal solo si todo cuadra, elimina el worktree después.

---

# Procesamiento de unidad — modo dry-run con revisión iterativa

Vas a procesar la unidad **U[X]** (cámbialo por el número que toca) siguiendo el flujo de fase 1 del proyecto.

## ⚠ Aislamiento en worktree (NO TE LO SALTES)

Estás trabajando dentro de un **worktree aislado** del repo principal (`../guia-proc-U[X]/` o similar). Verifica antes de empezar:

```bash
git rev-parse --show-toplevel    # debe terminar en /guia-proc-U[X] o similar, NO en /guia-didactica-profesor-IA
git branch --show-current        # debe ser proc-u[x]-wip o similar, NO main
```

Si `git rev-parse --show-toplevel` devuelve `/guia-didactica-profesor-IA` o `git branch` devuelve `main`, **abandona la corrida y avisa al ejecutor coordinador**: el worktree no está montado y trabajar aquí contaminaría el árbol principal.

**Reglas del worktree:**

- **TODO** lo que escribas (JSON de inventario, informes, archivos auxiliares) vive en este worktree.
- **NUNCA** modificas archivos del árbol principal directamente (los contratos vivos, registries, scripts: solo lectura para ti).
- **NUNCA** ejecutas `git push`, `git merge` ni nada que afecte a `main`.
- **NUNCA** eliminas, renombras ni sobrescribes el inventario canónico anterior `unidades/U[X]/U[X]-nc1-inventario.json` del árbol principal. El inventario anterior se conserva intacto fuera de tu alcance; en este worktree puedes escribir el candidato nuevo con el mismo path (porque el worktree tiene su propio working tree independiente).

## Contratos vivos a leer (en orden)

- `fases/1-extraccion-inventario/prompt.md` — entry point operativo.
- `fases/1-extraccion-inventario/schema-inventario.md` — shape canónico.
- `fases/1-extraccion-inventario/reglas-operativas.md` — autoridad operativa.
- `fases/1-extraccion-inventario/convenciones-y-casos.md` — transcripción y casebook (lookup puntual, no obligatorio leer entero).
- `fases/1-extraccion-inventario/glosario.md` — terminología (lookup).

**Precedencia jerárquica en caso de conflicto:** schema > reglas > convenciones.

## Registries canónicos disponibles (poblados — usa solo nombres literales)

- `campos-semanticos-canonicos.json` — 99 categorías léxicas.
- `verbos-canonicos.json` — 48 lemas verbales.
- `gramatica-canonica.json` — 23 categorías gramaticales.
- `pronunciacion-ortografia-canonica.json` — 7 categorías pron-ortográficas.

PCIC A1 como respaldo en `pcic-a1-*.json` (4 archivos).

## Modo de trabajo (importante — NO TE LO SALTES)

**Esto es una corrida en worktree aislado, dry-run primero, persistencia diferida.**

Fases del trabajo:

1. **Extracción**: extraes el inventario completo de la unidad siguiendo el contrato.
2. **Presentación en chat (dry-run)**: presentas el resultado en chat, **sin tocar el filesystem para escribir el JSON definitivo** todavía. El autor revisa lo que le presentas, da feedback, pide cambios.
3. **Iteración**: iteramos las veces que haga falta sobre el JSON presentado en chat.
4. **OK del autor**: solo cuando el autor diga "OK, escribe", escribes el JSON candidato en `unidades/U[X]/U[X]-nc1-inventario.json` **dentro del worktree** (no del árbol principal).
5. **Validación local en worktree**: ejecutas `python3 scripts/validar_inventario.py X` y reportas el resultado.
6. **Entrega**: confirmas al autor que el candidato está listo en el worktree para que el ejecutor coordinador haga revisión visual en dashboard e integración. **TÚ NO INTEGRAS.**

Sí puedes (necesitas) leer el PDF y los contratos. Lo que NO puedes hacer:

- Persistir el output sin OK del autor.
- Escribir fuera del worktree.
- Eliminar o sobrescribir el inventario canónico anterior del árbol principal.
- Integrar / hacer merge / hacer push.

## Política operativa durante la extracción

- **§0.1 propuesta-en-chat**: si encuentras una decisión no clara durante la extracción (canónico ambiguo, frontera de clasificación, contenido raro), plantéala en chat con 2-4 opciones razonables ANTES de seguir. No dejes nada silencioso para presentarlo al final.
- Naming canónico literal del registry. PROHIBIDO inventar nombres.
- `_pendiente_canon` y `_funcion_ambigua` solo tras propuesta-en-chat.
- Sufijo `@R` en fuentes solo cuando el `tipo` está en los 5 productivos (regla §6.5).
- 4 listas tipadas siempre presentes en cada actividad (vacías si no aplica).

## Qué presentas al terminar la extracción (todo en chat, no escribir)

1. **Inventario JSON completo** en bloque de código markdown.
2. **Resumen de estructura**: páginas extraídas, conteo de actividades por sección, conteo de cuadros, conteo de entradas en cada bloque consolidado.
3. **Trazado §0.3 A/B/C** en las 3 dimensiones con `recurrente` (vocabulario, gramática, pron-orto) — declarar barrido aunque alguna pasada termine en vacío.
4. **`_decisiones_ia`** registradas y por qué.
5. **Propuestas abiertas** (§0.1) que surgieron durante la corrida y su resolución para cada una.
6. **Anomalías o gaps detectados** respecto al contrato (casos frontera, canon insuficiente, etc.).

## Cuando el autor apruebe el dry-run

El autor te dirá explícitamente "OK, escribe". Entonces:

1. **Escribe** `unidades/U[X]/U[X]-nc1-inventario.json` **dentro del worktree** (el cwd ya es el worktree, así que el path relativo escribe al lugar correcto del worktree, no al árbol principal). Verifica con `git rev-parse --show-toplevel` antes si tienes duda.
2. **Ejecuta `python3 scripts/validar_inventario.py X`** y reporta el resultado.
   - **Expectativa esperada:** 0 errores y 0 avisos sobre este inventario nuevo. Puede haber **auditoría legacy** si quedan canónicos en `vocabulario_consolidado` no presentes en `campos-semanticos-canonicos.json`; se evalúa caso por caso.
   - Si hay errores, paramos, los analizamos, decide el autor si arreglas o si los dejas como deuda explícita para discutir con el ejecutor coordinador.
3. **Commit en el worktree** con mensaje descriptivo:
   ```bash
   git add -A
   git commit -m "proc-u[x]: candidato dry-run aprobado por autor + validador 0/0"
   ```
4. **Avisa al ejecutor coordinador** que el candidato está listo en el worktree para revisión visual + integración. Incluye en el aviso:
   - Path del worktree (`git rev-parse --show-toplevel`).
   - Rama (`git branch --show-current`).
   - SHA del commit del candidato.
   - Salida del validador.
   - Pendientes conocidos (auditoría legacy, propuestas no resueltas, etc.).

**A partir de aquí tu trabajo termina.** El ejecutor coordinador hará:

- Revisión visual del candidato en el dashboard (`python3 diagrama.py` apuntando al worktree, o con flag específico).
- Comparación contra el inventario canónico anterior si existe (no para reemplazar a ciegas, sino para entender qué cambia respecto al shape viejo).
- Ejecución de `python3 scripts/verificar_integridad.py` (con la salvedad transitoria de que durante la migración la suite reportará ruido de las unidades aún en shape viejo; el ejecutor filtra los errores que apuntan a esta unidad nueva).
- Decisión de integrar al árbol principal (típicamente fast-forward o copia controlada del JSON al `unidades/U[X]/` de main).
- Eliminación del worktree y su rama solo después de integración limpia y commit en main.

NO ejecutes ninguno de estos pasos tú. NO toques el árbol principal. NO elimines el worktree.

## Prohibiciones explícitas (resumen)

- ❌ Escribir fuera del worktree.
- ❌ Eliminar / renombrar / sobrescribir el inventario canónico anterior del árbol principal.
- ❌ Hacer `git push`, `git merge`, `git rebase` contra main.
- ❌ Eliminar el worktree o su rama.
- ❌ Persistir el JSON sin OK explícito del autor.
- ❌ Aplicar marcas bloqueantes silenciosas.
- ❌ Inventar canónicos no presentes en los registries.

## Empieza ahora

1. Verifica el worktree (`git rev-parse --show-toplevel` + `git branch --show-current`). Si no está montado correctamente, ABORTA y reporta al ejecutor.
2. Lee `prompt.md` y los contratos vivos.
3. Empieza la extracción de **U[X]** (sustituye [X] por el número).
4. Cuando tengas el JSON listo, **preséntalo en chat sin escribirlo**.
5. Espera feedback del autor antes de cualquier cambio en el filesystem.
6. Tras el OK, escribes en el worktree + validas + commiteas en el worktree + avisas al ejecutor coordinador para integración.