# Changelog — Guía Didáctica del Profesor (IA)
## Sistema de Agentes v5.0 — Nuevo Compañeros 1

> **Rol de este archivo:** registro cronológico de qué cambió. **NO es autoridad operativa** — la autoridad de cómo actuar es `CLAUDE.md`. Si una entrada antigua contradice a `CLAUDE.md`, manda `CLAUDE.md`.
>
> **Regla editorial:** entradas nuevas **cortas y operativas** (2-4 líneas: qué cambió + por qué + archivos). El detalle extenso de versiones antiguas ya está resuelto; no se replica ni se reescribe.
>
> **Histórico archivado** (consulta puntual, no relectura):
>
> | Rango | Archivo | Contenido |
> |---|---|---|
> | pre-v10.40 | `docs/historico/CHANGELOG-pre-refactor.md` | Sistema anterior al refactor |
> | v10.40–v10.164 | `docs/historico/CHANGELOG-fase1-cierre-y-fase2-paralela.md` | Cierre de fase 1 (U0-U9) + trabajo paralelo de fase 2 |
> | v11.0+ | este archivo | Post-fase 1: infraestructura, dashboard, deuda matcher |

---

## [v11.33 — 2026-05-20] — Fase 2: decisión de alcance — `comunicacion` y `estrategia` pospuestas

Cerrada la pieza "Cierre de alcance" que estaba pendiente en `REDISEÑO-EN-CURSO.md` §5 Nivel 1. Decisión del autor: el rediseño activo de fase 2 cubre solo los **bloques lingüísticos** (vocabulario, gramática, pronunciación/ortografía, verbal + `perifrasis` derivado); las **funciones comunicativas** y las **estrategias** quedan pospuestas a desarrollo posterior. Sincronización documental: (1) `REDISEÑO-EN-CURSO.md` — pieza retirada de la tabla de pendientes, decisión registrada como nota destacada; (2) `fases/2-reciclaje/CLAUDE.md` — el contrato corto dejó de afirmar que fase 2 modela funciones comunicativas y estrategias, ahora declara el alcance pospuesto; (3) `PROCESO-MAESTRO.md` — entrada nueva en bitácora con el roadmap de reincorporación. Cierra la tensión documental señalada por el revisor tras v11.31.

## [v11.32 — 2026-05-20] — REDISEÑO fase 2: corregida la incoherencia de P1

Micro-lote de consistencia tras v11.31. P1 (almacenamiento de datos enriquecidos) figuraba como "pendiente decisión" en `REDISEÑO-EN-CURSO.md` (§5 Nivel 1 + apéndice), pero el reservorio viejo lo cerró en **opción A** el 2026-05-10 (datos enriquecidos viven en `nc1-reciclaje.json`, regenerado al integrar cada unidad). Reetiquetado en ambos sitios como **decisión heredada a ratificar/formalizar**, no pendiente. La tensión documental de `CLAUDE.md` de fase 2 (cita `comunicacion`/`estrategia` como modelados) se deja intacta a propósito: depende del "cierre de alcance" todavía pendiente en §5 Nivel 1.

## [v11.31 — 2026-05-20] — REDISEÑO fase 2 §5: hoja de ruta del trabajo pendiente

Añadida §5 a `fases/2-reciclaje/REDISEÑO-EN-CURSO.md`: hoja de ruta viva del trabajo pendiente para cerrar el rediseño de fase 2 al estándar de contrato de fase 1. Estructurada en 4 niveles: (1) decisiones de modelo pendientes — incluye cuestiones nuevas (tratamiento detallado de formas verbales, carril propio para explicaciones gramaticales, triage declarado/reconciliable/contenido-nuevo para gramática y pron/orto, cierre de alcance de `comunicacion`/`estrategia`) + piezas heredadas del viejo (D1, D2, P1, §8, hallazgos del revisor); (2) contrato operativo a producir (prompt, schema de `nc1-reciclaje.json`, reglas reescritas, persistencia de decisiones IA, validación y gates); (3) implementación de Capa 1/Capa 2 (procedimiento, validador R1-R5, wiring); (4) reactivación operativa (adaptar scripts, validador cross-unidad, regeneración íntegra, sincronización dashboard/docs). Solo documento de rediseño; fase 2 sigue PAUSADA.

## [v11.30 — 2026-05-20] — Fix de consistencia en `fases/1-extraccion-inventario/CLAUDE.md`

La tabla "Para qué consultar qué archivo" citaba "(regla crítica 6)" al hablar de la política de naming canónico, pero esa es la **regla crítica 7** ("Canon canónico literal"); la 6 es "Documentación de fase 1 obligatoria". Corregida la referencia. Sin cambios funcionales.

---

## [v11.29 — 2026-05-20] — Residuos `ROADMAP.md` / `GITHUB-MANIFEST.md` en REVIEW y PROCESO-MAESTRO

Micro-lote de cierre tras v11.27. Quedaban dos rastros de los archivos retirados: `REVIEW.md` los listaba como filas "⚠ Heredado, sin tocar" en la tabla maestra de archivos del sistema; `PROCESO-MAESTRO.md` los mostraba en el árbol de estructura de raíz. `GITHUB-MANIFEST.md` ya no existe y `ROADMAP.md` nunca existió — ambas referencias retiradas. Cierra el carril de limpieza de raíz.

---

## [v11.28 — 2026-05-20] — Corrección del nombre de repo B en la autoridad documental

CLAUDE.md, README.md y PROCESO-MAESTRO.md nombraban repo B como `guia-sistema-trabajo` (el nombre planeado en v11.13), pero el repo B real es `temporal-antiguo-guia-ia` (renombrado por el otro chat en v11.14). 7 referencias activas corregidas (CLAUDE.md ×4, README.md ×2, PROCESO-MAESTRO.md ×1). Confirmado por el autor (Caso 1): repo B es el sistema de trabajo vivo donde sucede la redacción — el "Modelo de dos repos" y el "Flujo de publicación canónica" siguen válidos, solo el nombre estaba mal. Bitácora histórica de REVIEW intacta (en v11.13 el nombre planeado sí era `guia-sistema-trabajo`). Además: comentario de `integrar_unidad.py` en Comandos básicos actualizado (el flujo ya no usa worktree; el flag de reciclaje quedó en cuarentena en v11.19).

---

## [v11.27 — 2026-05-20] — Eliminado `GITHUB-MANIFEST.md` obsoleto

`GITHUB-MANIFEST.md` (118 líneas, gitignorado, nunca versionado) eliminado. Era el manifiesto de despliegue del sistema de agentes CrewAI en Railway (fechado 2026-03-16): listaba `scripts/crewai/`, `eval/`, `Dockerfile`, `railway.toml`, rutas `datos/inventarios/` — todo migrado a repo B, eliminado o en rutas viejas. Documento muerto que desinformaba. `.gitignore`: retiradas las líneas `ROADMAP.md` (inexistente) y `GITHUB-MANIFEST.md` de la sección de planificación local; `.github/` se conserva ignorado.

---

## [v11.26 — 2026-05-20] — Borrado de backups muertos `.bak.v10.150`

Efecto colateral de v11.25 detectado por el revisor: el patrón genérico `*.bak` no cubre los backups antiguos `*.bak.v10.150` (terminan en `.v10.150`, no en `.bak`), así que 6 archivos `unidades/U{1,2,3,7,8,9}/U*-nc1-inventario.json.bak.v10.150` quedaron como untracked. Son backups de la migración de saneamiento v10.150, cerrada hace tiempo; los inventarios están en v11.x validando 0/0/0. Eliminados — no se re-ignoran (cruft muerto). El patrón `*.bak` se mantiene para backups futuros.

---

## [v11.25 — 2026-05-20] — Limpieza `.gitignore` + coherencia de estructura

`.gitignore`: retirados los patrones de backup de migraciones cerradas (`*.bak.v10.145`, `*.bak.v10.150`) y sustituidos por un genérico `*.bak`. Coherencia documental: `ROADMAP.md` (no existe) y `GITHUB-MANIFEST.md` (existe pero gitignorado como planificación local, fuera de la autoridad documental) se retiran de la estructura del repo en `README.md` y `CLAUDE.md` — los docs los listaban como archivos del proyecto pese a no versionarse. Patrones binarios/diseño del `.gitignore` se dejan intactos (ignores defensivos).

---

## [v11.24 — 2026-05-20] — Adelgazado de `.env.example` para repo A

`.env.example` pasó de ~70 a ~24 líneas. Repo A es dashboard local + validador: no usa agentes en su flujo vigente, no necesita claves de API, y ninguna variable es obligatoria (el dashboard arranca sin `.env`). Retirado: API keys (ANTHROPIC/GROQ/DEEPSEEK — de agentes, repo B), bloque Crew Recurvo, bloque DeepEval, `PORT=8080` (puerto viejo). Conservado como opcional: `PORT`/`HOST`/`EXTRA_UNIDADES_PATHS`/`DEBUG` (servidor del dashboard) + bloque comentado `DATABASE_URL`/`LANGFUSE_*` (superficies de BD/trazas heredadas y dormidas — el código de `diagrama.py` aún las lee). Verificado contra el uso real de `os.environ` en `diagrama.py`. `.env` real (con claves) intacto y gitignorado.

---

## [v11.23 — 2026-05-20] — Residuo `.dockerignore` en el paso E3 de REVIEW

Hallazgo del revisor tras v11.22: el paso futuro E3 de `REVIEW.md` (Meta-lista de archivos a limpiar) aún nombraba `.dockerignore`, que no existe desde v11.21. Añadida nota inline aclarando que ya no aplica. Cierra el último rastro de `.dockerignore` en el plan vivo.

---

## [v11.22 — 2026-05-20] — Residuo `.dockerignore` en PROCESO-MAESTRO

Hallazgo del revisor tras v11.21: `PROCESO-MAESTRO.md:255` mencionaba `.dockerignore` en una lista de tarea sin marcar como superada. Añadida nota inline "tarea histórica ya superada; `.dockerignore` eliminado en v11.21". Sin más cambios.

---

## [v11.21 — 2026-05-20] — Retirada del stack de despliegue (Docker/Railway)

Repo A ya no se despliega en la nube — el dashboard es herramienta local (`python3 diagrama.py`). Eliminados `Dockerfile`, `.dockerignore` y `railway.toml`. Razón: el despliegue tenía sentido cuando se compartía el dashboard con el equipo y los módulos de agentes vivían aquí; tras la migración a dos repos (agentes en repo B) y la decisión de no desplegar repo A, el stack quedó sin uso (y `.dockerignore` arrastraba 7 líneas `viejo/` muertas). `requirements.txt` se mantiene (lo necesita el `.venv` local). Referencias actualizadas: `CLAUDE.md` y `PROCESO-MAESTRO.md` (estructura del repo), `README.md` (estructura + fila "Ejecución" del stack), `REVIEW.md` (estado global, B5 marcado ⊘ SUPERADO, tablas de archivos/código). Bitácora histórica de CHANGELOG/REVIEW no se reescribe.

---

## [v11.20 — 2026-05-20] — Renombrado de scripts: `sanear_inventario.py` y `matcher.py`

Lote 3 (naming) de la revisión de `scripts/`. Renombrado limpio con `git mv` + actualización de todas las referencias activas: `cleanup_v150.py` → `sanear_inventario.py` (el `v150` sugería one-shot, pero es la herramienta de saneamiento activa del flujo de fase 1); `migrate_at_r_v10145.py` → `matcher.py` (su nombre era de la CLI de migración v10.145 — one-shot cumplida — pero su valor vivo es la librería matcher que importa `sanear_inventario.py`). Referencias actualizadas: `CLAUDE.md`, `prompt.md`, `validar_inventario.py` (2 comentarios), `schema-inventario.md`, el import de `sanear_inventario.py` y los docstrings de ambos. Histórico de CHANGELOG/REVIEW no se reescribe (nombres de la época). Verificado: import OK, `sanear_inventario.py` corre, validador 0/0/0.

---

## [v11.19 — 2026-05-20] — Cuarentena de `regenerar_reciclaje_vocabulario.py`

Lote 2 de la revisión de `scripts/`. `regenerar_reciclaje_vocabulario.py` está roto (asume shape v10.114 pre-rediseño; los inventarios son post-v10.153). No se archiva — sigue colgado del flag opcional de `integrar_unidad.py`. Cambios: (1) guard fail-fast `_cuarentena()` al inicio de `main()` — el script se rechaza con mensaje explícito salvo `RECICLAJE_VOCAB_OVERRIDE=1`; (2) `integrar_unidad.py` ya no dispara el script roto desde `--regenerar-reciclaje` — imprime aviso de cuarentena y completa la integración del inventario sin abortar; el commit es solo el inventario. `regenerar_reciclaje_mapa.py` se deja intacto (sigue operativo, fase 2 pausada).

---

## [v11.18 — 2026-05-20] — Archivado del one-shot `inicializar_canon_semantico.py`

`scripts/inicializar_canon_semantico.py` (one-off que pobló el canon semántico; cumplido — el canon se mantiene a mano desde entonces) movido a `docs/historico/scripts-one-shot/` con README. Referencias activas actualizadas antes de mover: `validar_inventario.py` (mensaje de ayuda del error de canon ausente → ahora apunta a "restaurar desde git") y `PROCESO-MAESTRO.md` (nota de archivado). **`migrate_at_r_v10145.py` NO se archiva** pese al nombre one-shot: `cleanup_v150.py` lo importa como módulo matcher — sigue activo. Su renombrado queda para un lote posterior de naming.

---

## [v11.17 — 2026-05-20] — `eval/` movido a `temporal-antiguo-guia-ia`

`eval/` (3 archivos, 28K — `promptfoo.yaml`, `evaluar_tarjetas.py`, `provider_crewai.py`) era tooling de evaluación del sistema CrewAI/Recurvo, no infraestructura viva de este repo. Estaba **roto** desde v11.14: `provider_crewai.py` importa de `scripts/crewai/`, que se fue a `temporal-antiguo-guia-ia` con el borrado de `viejo/`. Copiado a `temporal-antiguo-guia-ia` (commit `cf5da5e`) y eliminado de aquí. `CLAUDE.md` y `README.md` — retirada la referencia a `eval/` de la estructura del repositorio. Fase 3 (tarjetas), cuando se construya, tendrá su evaluación propia si la necesita; no depende de este `eval/` atado a Recurvo.

---

## [v11.16 — 2026-05-20] — Higiene `.gitignore` + limpieza de carpetas sueltas

Pasada de limpieza de carpetas de raíz. `.gitignore`: añadidos `.venv/` (654M, virtualenv regenerable que estaba untracked sin ignorar — riesgo de commit accidental) y `.deepeval/` (carpeta que el framework recrea). Eliminadas carpetas sin valor: `.deepeval/` (vacía), `.github/copilot-instructions.md` (obsoleto — describía un workspace antiguo con rutas inexistentes, era para Copilot no Claude Code), `.claude/claude-code-chat-images/` (26 screenshots viejos, 6.1M).

---

## [v11.15 — 2026-05-20] — Limpieza de `.claude/` tras la migración

`.claude/` de repo A queda mínimo: solo `commands/check-fase1.md` + `settings.json` (config de infraestructura/inventarios). Retirados de repo A los archivos de trabajo editorial y del sistema CrewAI antiguo — ya copiados a repo B (`temporal-antiguo-guia-ia`, verificado idéntico, con rutas `viejo/`→`unidades/` adaptadas): `rules/{agent-prompt-design,tool-design,criterios-generacion-texto}.md`, `agents/auditor-seccion.md`, `skills/auditar-seccion/`, `commands/audit.md`. Borrado el `.bak` huérfano. `.gitignore`: `.claude/` deja de ignorarse en bloque — ahora se versiona `settings.json` + `commands/check-fase1.md`; siguen ignorados `settings.local.json` y `claude-code-chat-images/`. Carpeta `claude-code-chat-images/` (26 screenshots viejos, 6.1M) eliminada — no aportan nada; el ignore se mantiene por si la extensión la recrea.

---

## [v11.14 — 2026-05-20] — Migración a dos repos · Mitad 2 paso 2: borrado físico de `viejo/`

`viejo/` eliminado de repo A (disco + índice git): 8 archivos tracked + el resto ignorado. Su copia íntegra y verificada (`diff -rq` sin diferencias) vive en repo B `temporal-antiguo-guia-ia` (local `~/Desktop/temporal-antiguo-guia-ia`, GitHub privado `adminmc2/temporal-antiguo-guia-ia`, commits `8164c2f`+`6cdf342`). `.gitignore` — retirado el bloque "Contenido editorial" completo (~15 líneas que ignoraban `viejo/...`) + la línea de PDFs `viejo/unidades/**/fuente/`. Hook `.git/hooks/pre-commit` (bloqueaba commits con rutas `viejo/`) retirado: sin objeto. Repo A queda sin `viejo/`; el sistema de trabajo es ya exclusivamente repo B. Cierra la Mitad 2 de la migración.

---

## [v11.13 — 2026-05-20] — Migración a dos repos · Mitad 2 paso 1: coherencia documental

Repo A queda autocoherente sin `viejo/` como fuente de trabajo (aunque `viejo/` siga existiendo físicamente una iteración más; se borra en v11.14). Cambios: `CLAUDE.md` — nuevo bloque "Modelo de dos repos A/B", flujo de publicación reapuntado a repo B, reglas de oro y "Lo que NO se hace" sin "editar en viejo", `viejo/` fuera de la estructura. `README.md` — sección "Modelo de dos repositorios" sustituye a "Sobre el sistema anterior". `diagrama.py` — dict `AGENTS` (código muerto que apuntaba a `viejo/repertorios/`) retirado; comentario documenta la feature "repertorios por sección" como diferida (reintroducir desde repo B vía `GUIA_TRABAJO_REPO`). `PROCESO-MAESTRO.md` — nota de migración global: sus ~82 referencias `viejo/...` son punteros históricos a material que vive en repo B (reescritura completa pendiente de pasada posterior). Criterio de cierre: ningún documento activo presenta `viejo/` como zona de trabajo vigente.

---

## [v11.12 — 2026-05-20] — Versionar mirrors editoriales en repo A

Las propuestas editoriales publicadas (`unidades/U{0,1,2,4,5}/propuesta/*.md`) y los recursos (`recursos/tarjetas/*.csv`) estaban untracked — existían en disco pero fuera de git. Al ser el entregable de repo A, se commitean: 37 archivos, 6362 líneas. Preludio de la Mitad 2 (migración a dos repos).

---

## [v11.11 — 2026-05-20] — Compactación de CHANGELOG

`CHANGELOG.md` pasó de 4252 a ~250 líneas. El bloque v10.40–v10.164 (cierre de fase 1 + fase 2 paralela) se movió a `docs/historico/CHANGELOG-fase1-cierre-y-fase2-paralela.md` con cabecera fuerte que lo declara fuente documental de lo hecho en ambas fases. Header del activo gana índice de históricos por rango. Corte validado por contenido: todo v10.x es era fase 1; v11.0 es el milestone post-fase-1. README/CLAUDE sin tocar; REVIEW solo como meta-doc (banner + bitácora, por convención).

---

## [v11.10 — 2026-05-20] — Jerarquía de autoridad documental + regla editorial

Cierre del problema de crecimiento perpetuo de CHANGELOG/REVIEW sin rearchivar nada. Cambios: (1) cabeceras de CHANGELOG.md y REVIEW.md declaran su rol (registro/estado, NO autoridad) y la regla editorial de entradas cortas; (2) CLAUDE.md § "Documentos clave" añade columna ¿Autoridad? + bloque "Regla editorial" — CLAUDE.md manda, el resto apunta; (3) README.md añade línea "dónde mirar histórico" (`docs/historico/`). Sin mover archivos. Archivos: CLAUDE.md, README.md, CHANGELOG.md, REVIEW.md.

---

## [v11.9 — 2026-05-20] — Dashboard "Inventarios": tarjetas con A+B+C+D (stats, consolidados, propuesta, keywords)

Tarjetas de la vista Inventarios del dashboard ampliadas para mostrar contexto operativo y editorial de cada unidad de un vistazo. Las cards anteriores mostraban solo título, nivel, páginas y archivo; ahora también:

**Bloque A — Stats del inventario:** `📋 N actividades · N cuadros · N decisiones` (lectura directa del JSON: paginas_detalle, _decisiones_ia).

**Bloque B — Consolidados resumidos:** `📚 Léx N P/N R · ⚙ Gram N P/N R · 🔤 P/O N P/N R · 📖 Nv` (recuento de categorías principal/recurrente en las 4 dimensiones canónicas + lemas verbales).

**Bloque C — Propuesta editorial mini-grid:** 7 chips compactos `Voc ✓ · Gram ⏳ · Com · · ...` reutilizando el scanner ya existente de fase 1 (lectura de `unidades/UN/propuesta/<seccion>.md`). Cada chip tiene tooltip con el estado y usa la misma paleta de la grid "Estado de unidades" del proyecto.

**Bloque D — Keywords del inventario:** hasta 5 chips con los canónicos léxicos y gramaticales principales (ej. U6: `Establecimientos · Marcadores de lugar · Profesiones y lugares de trabajo · Imperativo (tú)`).

**Cambios:**

- `diagrama.py` `_scan_zona`: añadidos 4 campos al payload de cada unidad (`stats`, `consolidados`, `keywords`, `propuesta`). Reutiliza `scan_section` para no duplicar lógica.
- `web/index.html` `loadInventarios`: card más ancha (`minmax(340px, 1fr)` en lugar de 260px) y renderiza los 4 bloques compactamente. Tooltips en chips de propuesta. Archivo path se trunca con ellipsis.

**Higiene del commit:** `diagrama.py` + `web/index.html` + meta docs.

---

## [v11.8 — 2026-05-20] — Sync de puerto 8080→8081 fuera del subsistema dashboard

Hallazgo del revisor tras v11.7: aunque el subsistema dashboard quedó sincronizado, seguían 4 referencias activas a `8080` fuera de ese subsistema, mientras `diagrama.py` PORT = 8081 desde v10.127.

**Cambios — unificación a 8081 en todas las referencias activas:**

- `README.md:80`: comando de arranque (`# → http://localhost:8081`).
- `Dockerfile:16`: `EXPOSE 8081` (antes 8080, no coincidía con el puerto al que liga el server).
- `fases/1-extraccion-inventario/CLAUDE.md:38`: comando de validación visual.
- `fases/2-reciclaje/CLAUDE.md:54`: comando de revisión de timeline.

**Verificación:** `grep -rn "8080"` en `*.md` / `*.py` / `Dockerfile` (excluyendo `viejo/`, `docs/historico/`, y entradas históricas de CHANGELOG/REVIEW) → 0 coincidencias activas.

**Higiene del commit:** `README.md` + `Dockerfile` + 2 × CLAUDE.md de fase + meta docs.

---

## [v11.7 — 2026-05-19] — Cleanup-sync: drifts menores tras auditoría v11.6

Auditoría tras v11.6 detectó tres drifts del mismo subsistema. Lote único para cerrar todo en una sola pasada.

**Cambios:**

1. **`diagrama.py`**: eliminada la clave huérfana `"reflexion": "Reflexión"` de `SECTION_LABELS`. Era residuo inerte tras la retirada de la columna Reflexión en v11.1 (no participaba en `SECTIONS`, no afectaba runtime).
2. **`diagrama.py:5`**: docstring decía `http://127.0.0.1:8080`; corregido a `8081` (PORT real definido en `diagrama.py:29`).
3. **`CLAUDE.md:88`**: comentario en sección "Comandos básicos" decía `http://localhost:8080`; unificado a `8081` (coincide ya con § "Estado fase 1 — Comandos canónicos" en `CLAUDE.md:153`).
4. **`CLAUDE.md:24`**: estructura del repositorio mencionaba solo 6 secciones canónicas en `propuesta/` (vocabulario, gramatica, comunicacion, destrezas, cultura, evaluacion). El dashboard pinta una 7.ª columna `itinerarios` desde v11.1. Anotado en la estructura como opcional: planificación cross-unidad mostrada como 7.ª columna del dashboard.

**Higiene del commit:** `diagrama.py` + `CLAUDE.md` + meta docs.

**Próximo paso:** ya sin drifts pendientes, decidir entre reactivar fase 2 (reciclaje) o continuar con producto editorial.

---

## [v11.6 — 2026-05-19] — Sync CLAUDE.md raíz tras cierre de deuda matcher

Hallazgo del revisor tras v11.5: la sección "Estado fase 1 — Deudas residuales" de `CLAUDE.md` raíz seguía afirmando las 3 deudas matcher como abiertas, aunque ya quedaron resueltas en v11.3-v11.5. Bug puramente documental — no rompe runtime ni validación, pero deja una fuente normativa incorrecta para sesiones futuras (CLAUDE.md es la autoridad que cargan automáticamente todas las nuevas sesiones de Claude Code).

**Cambios:**

- `CLAUDE.md` § "Estado fase 1 — Deudas residuales catalogadas" reescrita:
  - Bloque nuevo "Deuda matcher: CERRADA en v11.3-v11.5" con check de cada bug y la versión que lo resolvió.
  - Bloque "Deudas todavía abiertas" conserva los canónicos huérfanos (`Abreviaturas de los diccionarios`, `vegetariano`) y la auditoría retroactiva U0-U5.

**Higiene del commit:** solo `CLAUDE.md` + meta docs.

---

## [v11.5 — 2026-05-19] — Deuda matcher bug 3: `_gather_text` recoge claves de dict

Tercer y último fix de la deuda técnica del matcher catalogada al cierre de fase 1. Con este commit, la deuda matcher queda cerrada por completo.

**Problema:**

`_gather_text(o, out)` iteraba sobre dicts recorriendo solo los valores (`o.values()`), nunca las claves. Caso real (U6 v10.158): la agenda semanal de Lorena en `p66-act4` se modelaba como dict `{"Lunes": "Piscina", "Martes": "Supermercado", ...}`. El matcher recogía solo los valores (las actividades), pero no los días — y `Días de la semana` solo aparecía con `Lunes` (capturado en otra actividad). Investigando se descubrió la causa: las claves del dict no se gathereaban.

**Fix:**

- `scripts/validar_inventario.py`: `_gather_text` ahora itera con `o.items()` y añade la clave al output si es string, además de recursar sobre el valor. Comportamiento idéntico para listas y strings.

**Resultado:**

- Para futuros inventarios, dicts con claves significativas (días, personajes, secciones, etc.) ya no obligan a reestructurar a lista de objetos solo para satisfacer al matcher.
- Las 10 unidades siguen validando 0/0/0 tras el fix (sin regresión).

**Decisión: U6 agenda NO se revierte a dict.**

El workaround de v10.158 (agenda lista de objetos `[{"dia": "Lunes", "actividad": "Piscina"}, ...]`) se mantiene. Razones: (a) revertir es un cambio estructural sin ganancia funcional (el matcher ya lee ambos shapes); (b) otros consumidores potenciales (dashboard, agentes) pueden depender del shape actual; (c) el fix elimina la necesidad del workaround **para nuevos inventarios**, que es lo importante.

**Trade-off aceptado:**

Recoger claves de dict aumenta levemente la superficie de match. Las claves del proyecto son normalmente etiquetas semánticas (`Lunes`, `Martes`, `personaje`, `texto_modelo`, etc.). Si una clave técnica coincidiera con un item canónico por casualidad, generaría falso positivo. Riesgo bajo; si emergiera se documentaría.

**Cierre de la deuda matcher:**

Las 3 deudas técnicas catalogadas al cierre de fase 1 quedan resueltas en v11.3-v11.5:
- ✅ Bug 1 (acentos): `_norm_text` aplica `_strip_accents` (v11.3).
- ✅ Bug 2 (imágenes): `imagen` en `INPUT_FIELDS_LIST` (v11.4).
- ✅ Bug 3 (claves de dict): `_gather_text` recoge claves (v11.5).

**Próximo paso:** reactivar fase 2 (reciclaje) o continuar con producto editorial.

**Higiene del commit:** solo `scripts/validar_inventario.py` + meta docs.

---

## [v11.4 — 2026-05-19] — Deuda matcher bug 2: matcher recoge `imagen.descripcion`

Segundo fix de la deuda técnica del matcher catalogada al cierre de fase 1.

**Problema:**

El validador `_activity_input_text` solo iteraba sobre `INPUT_FIELDS_LIST` = `(instruccion_original, datos, dialogo, dialogo_completo, texto, texto_completo, items_libro, muestra_de_lengua, opciones, audio)`. El campo `imagen.descripcion` no estaba incluido. Caso real (U9 v10.164): `morado/-a` aparecía en el libro como color de prendas en `p101-act04`, pero solo dentro de `imagen.descripcion` ("Siete fotos de prendas... 1 falda morada, ... 7 jersey morado"). El validador no lo veía → no se podía codificar como item de Colores y el contenido material se perdía.

**Razón editorial del fix** (autor en chat): la descripción de imagen es contexto editorial real que el alumno ve. Para entender una actividad es necesario saber qué muestra la imagen — no es metadato. El campo `respuestas`, en contraste, tiene función distinta (clave para profesor / contexto para agentes), pero esa decisión se mantiene fuera del alcance de este fix.

**Fix:**

- `scripts/validar_inventario.py`: añadido `"imagen"` a `INPUT_FIELDS_LIST`. `_gather_text` recurre sobre el dict `imagen` y recoge automáticamente todas las strings (incluido `descripcion`).

**Resultado:**

- `morado/-a` en U9 ahora codificado en bucket `Colores` recurrente con fuente `p101-act4` (recuperado tras workaround vacío de v10.164).
- Refs de actividad p101-act04 ampliadas con `Colores`.
- Las 10 unidades siguen validando 0/0/0 tras el fix.

**Trade-off aceptado:**

Algunas descripciones de imagen son verbosas (ej. p100-act01 con tres trajes tradicionales). Podrían generar falsos positivos puntuales para lemas cortos. Riesgo bajo y simétrico al que ya existe con `texto_completo`; si emergiera, se documentaría como deuda específica.

**Pendiente:**

- Bug 3 (matcher no recoge claves de dict) — caso `agenda` U6 v10.158.

**Higiene del commit:** `scripts/validar_inventario.py` + `unidades/U9/U9-nc1-inventario.json` + meta docs.

---

## [v11.3 — 2026-05-19] — Deuda matcher bug 1: normalización de acentos en `_norm_text`

Primer fix de la deuda técnica del matcher catalogada al cierre de fase 1 (v10.164).

**Problema:**

El validador `_norm_text` solo aplicaba lowercase + collapse de whitespace, sin normalizar tildes. Caso real (U8 v10.163): la palabra del libro era `marrones` (plural sin tilde). El item canónico debía ser `marrón` (singular con tilde, por §5.11). Pero `marrón` ≠ substring de `marrones` por la diferencia `ó`/`o` → matcher fallaba, obligando a escribir `marrones` como item (violando §5.11 unificación a singular).

**Fix:**

- Nueva función `_strip_accents(s)` en `scripts/validar_inventario.py` que descompone NFD y descarta los marks de tilde aguda/grave/circumflex, preservando `ñ` (re-componiendo `n + U+0303` → `ñ`).
- `_norm_text(s)` ahora aplica `_strip_accents` tras lowercase + whitespace collapse. Se aplica simétricamente a needle y haystack → comparación substring funciona con tildes ausentes en plural.

**Resultado:**

- `marrón` (item singular) atrapa `marrones` en texto ✓
- `años` atrapa `año` ✓
- `período` atrapa `periodo` ✓
- Las 10 unidades siguen validando 0/0/0 tras el fix (sin regresión).

**Rectificación de workaround:**

- `unidades/U8/U8-nc1-inventario.json`: `marrones` → `marrón` (forma singular canónica restaurada en bucket `Colores` recurrente). El workaround de v10.163 queda eliminado.

**Trade-off aceptado:**

La normalización acepta como match casos como `tu` ↔ `tú` (posesivo vs pronombre sujeto). En el inventario actual, ambos items declaran sus propias fuentes y la práctica editorial mantiene la disambiguación. Si emergiera una falsa coincidencia, se documentaría como deuda específica.

**Pendiente:**

- Bug 2 (matcher no recoge `image.descripcion`) — caso `morado/-a` U9.
- Bug 3 (matcher no recoge claves de dict) — caso `agenda` U6.

**Higiene del commit:** `scripts/validar_inventario.py` + `unidades/U8/U8-nc1-inventario.json` + meta docs.

---

## [v11.2 — 2026-05-19] — Dashboard auto-refresh por polling con hash

El dashboard "Estado de unidades" no detectaba cambios sin recargar manualmente la página. Implementado auto-refresh por polling con hash check, sin nuevas dependencias.

**Cómo funciona:**

- Cada **5 segundos**, el frontend hace `fetch('/api/diagrams')` en silencio.
- El endpoint ya devuelve un campo `hash` (md5 del `status` object) calculado en backend.
- Si el `hash` recibido coincide con el último renderizado → no se re-renderiza nada (sin DOM churn).
- Si el `hash` cambió → se re-renderiza la grid de estado, las tabs de diagrama y el diagrama activo.

**Resultado:** cualquier modificación en `unidades/UN/propuesta/<seccion>.md` (creación, edición, borrado, añadir/quitar `*pendiente*`) se refleja automáticamente en el dashboard en ≤5 segundos sin recargar la pestaña.

**Cambios:**

- `web/index.html`: `loadProjectData()` ahora acepta opciones (`{silent: true}` para polling), guarda `_projectHash`, y solo re-renderiza cuando el hash cambia. Añadido `setInterval(..., 5000)` para el polling silencioso.

**Higiene del commit:** solo `web/index.html` + meta docs.

**Próximo paso (v11.3+):** decidir entre deuda matcher (`_expand_needle` / `_gather_text`) o reactivación de fase 2.

---

## [v11.1 — 2026-05-19] — Dashboard "Estado de unidades": ajustes UX

Ajustes UX al panel "Estado de unidades" del dashboard tras revisión visual del autor.

**Cambios:**

1. **Retirada de columna "Reflexión"** — no se trabaja como sección editorial independiente; era ruido en la tabla. Grid pasa de 8 a 7 columnas.
2. **Criterio `complete` simplificado** — el conteo de líneas no es señal de calidad. Nuevo criterio: `complete` = archivo existe sin marcadores `*pendiente*`; `in-progress` = tiene pendientes; `missing` = no hay archivo.
3. **Celdas con marcas semánticas** en lugar de número de líneas: `✓` (complete), `N⏳` (in-progress con N pendientes), `·` (missing). El conteo de líneas dejó de mostrarse porque no aportaba info accionable.
4. **U0 atípica reconocida**: la unidad atípica tiene un único archivo `unidades/U0/propuesta/punto-de-partida.md` que cubre la unidad entera. El scanner ahora propaga ese archivo a las 7 celdas de U0.
5. **CSS grid alineado** a las nuevas 7 columnas (`grid-template-columns: 50px repeat(7, 1fr)`) — el ajuste sin esto provocaba desplazamiento de etiquetas U0/U1/... dentro de las celdas.

**Resultado:** dashboard pasa de `0/80` (estado v10.164 con scanner roto) a `31/70 completas` automáticamente. Cada celda comunica algo accionable.

**Próximo paso (v11.2):** auto-refresh por file-watcher cuando se añadan o modifiquen archivos en `propuesta/`.

**Higiene del commit:** `diagrama.py` + `web/index.html` + meta docs.

---

## [v11.0 — 2026-05-19] — Milestone post-fase 1: bump + fix scanner dashboard

Primera versión tras el cierre de fase 1 (v10.164). Bump de major para marcar el hito: la parte mecanizable de extracción de inventario queda consolidada y las nuevas iteraciones se centran en infraestructura y producto (no en saneamiento retrospectivo).

**Cambios:**

1. **Bump major v10.164 → v11.0** — milestone de cierre de extracción canónica + apertura del bloque de infraestructura/producto.
2. **Fix scanner del dashboard** (`diagrama.py` `scan_section`): el scanner buscaba el patrón legacy `unidades/UN/UN-<seccion>*.md` y devolvía `missing` para todo el material editorial nuevo, que vive en `unidades/UN/propuesta/<seccion>.md` (sin prefijo) según el flujo de publicación canónica documentado en CLAUDE.md raíz. Ahora busca primero en `propuesta/<seccion>.md` (nueva canónica) y luego en el patrón legacy (compatibilidad hacia atrás).

**Resultado verificable:** el dashboard "Estado de unidades" pasa de `0/80 completas` a `20/80 completas` automáticamente (U1, U2, U4, U5 con 5 secciones cada una en estado `complete` + 4 con `in-progress` en evaluación). U0 atípica + U3, U6-U9 sin propuesta = `missing` legítimo.

**Próximo paso (v11.1):** auto-refresh del dashboard cuando se añadan archivos en `propuesta/`.

**Higiene del commit:** solo `diagrama.py` + meta docs.

