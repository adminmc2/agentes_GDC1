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

## [v11.98 — 2026-05-23] — Portada U9 (Ropa, p.92) — cobertura completa U0-U9

Añadido `portada` a U9: número «9», título, foto de chica en tienda de ropa y los 5 epígrafes del índice. **Cobertura completa**: U0-U9 ya tienen `portada` rellena. Validador 10/10 unidades 0/0/0.

---

## [v11.97 — 2026-05-23] — Portada U8 (Descripciones, p.82)

Añadido `portada` a U8: número «8», título, foto de grupo de 4 jóvenes con ropa de invierno y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.96 — 2026-05-23] — Portada U7 (Hábitos, p.72)

Añadido `portada` a U7: número «7», título, foto de manos enjabonadas bajo el grifo y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.95 — 2026-05-23] — Portada U6 (¿A dónde vas?, p.62)

Añadido `portada` a U6: número «6», título, foto de chica en sección de productos frescos y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.94 — 2026-05-23] — Portada U5 (¿Dónde están las llaves?, p.52)

Añadido `portada` a U5: número «5», título, foto de llavero con casita de madera y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.93 — 2026-05-23] — Portada U4 (Comidas y bebidas, p.42)

Añadido `portada` a U4: número «4», título, foto de platos servidos en mesa y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.92 — 2026-05-23] — Portada U3 (La Familia, p.32)

Añadido `portada` a U3: número «3», título, foto de pícnic familiar y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.91 — 2026-05-23] — Portada U2 (Países de habla hispana, p.22)

Añadido `portada` a U2: número «2», título, foto de 3 jóvenes en piragua y los 5 epígrafes del índice. Errata del libro «datos pesonales» (sic) mantenida verbatim. Validador 0/0/0.

---

## [v11.90 — 2026-05-23] — Portada U1 (¡Hola!, p.12)

Añadido `portada` a U1: número «1», título «¡Hola!», foto de dos chicos y los 5 epígrafes del índice (VOCABULARIO/GRAMÁTICA/COMUNICACIÓN/DESTREZAS/CULTURA con sus contenidos). Validador 0/0/0.

---

## [v11.89 — 2026-05-23] — Portada U0 (Punto de partida, p.8)

Añadido `portada` al inventario de U0 (`unidades/U0/U0-nc1-inventario.json`). Unidad atípica sin numeración: capturados verbatim el título («Punto de partida»), la foto de cubos con letras del abecedario y el índice de cuatro epígrafes. Validador 0/0/0.

---

## [v11.88 — 2026-05-23] — Schema fase 1: campo `portada` opcional (apertura de unidad)

Nuevo campo top-level opcional `portada` en el inventario, para capturar la columna de apertura de cada unidad (número + título + fotos temáticas, siempre 1.ª página de Vocabulario, columna izquierda). Es metadato de unidad — ni actividad ni cuadro — por eso va al nivel de `titulo`/`nivel`. Shape: `{pagina: int, descripcion: str (verbatim)}`. **Campo opcional**: no rompe U0-U9 (validador 0/0/0 tras el cambio). `schema-inventario.md` §1 (recuento + jsonc) + nueva §1.1 con shape y semántica. `validar_inventario.py`: `portada` en `CLAVES_TOP_OPCIONALES` + chequeo de shape (si presente: ambas subclaves obligatorias, `pagina` int, `descripcion` str no vacío). Corregida también la inconsistencia preexistente en §1: recuento decía "13 obligatorias" pero L54 ya decía 12 (tras la eliminación de `contenidos_indice` en v11.67). Próximo: rellenar `portada` unidad por unidad leyendo el PDF, empezando por U0.

---

## [v11.86 — 2026-05-23] — Relaciones cross-hilo: contrato + helper de candidatos por cuadro compartido

Capa contractual de las **relaciones cross-hilo** (qué se apoya en qué, qué contrasta con qué). `schema-reciclaje.md` §6 amplía el enum de `propuestas.tipo` con `relacion_cross_hilo` y añade el payload **no dirigido** `relacion_candidata: {hilos: [a, b] ordenados, cuadros_compartidos}` — la propuesta candidata identifica un par sin asignar origen ni destino; la dirección (cuando el `tipo` la requiere) se decide solo al aceptar, evitando sesgar editorialmente por orden alfabético. Nueva §7 introduce `hilo.relaciones[]` (lectura editorial cerrada — `hilo_ref`, `tipo` enum cerrado de 5 valores, `detalle`, `unidad_relevante?`) con frontera explícita frente a `detalle.enlaces`; §7-Notas renumerada a §8. `reglas-reciclaje.md` §15 define los 5 tipos (`usa`, `prerrequisito`, `activa` direccionales; `contrasta`, `comparte` simétricos) con criterio + ejemplo, política de extensión del enum y política de cierre (en aceptación el humano elige `tipo` y, si direccional, qué hilo del par actúa como origen). `glosario.md` añade entrada para `hilo.relaciones[]`. `scripts/proponer_relaciones_cuadro.py` detecta pares de hilos que comparten cuadro en una misma unidad y crea/actualiza propuestas pendientes idempotentemente (id canónico del par ordenado vía `id_relacion_par(a, b)` — único constructor compartido por helper y futuro flujo de cierre). `scripts/validar_reciclaje.py` endurece el gate: valida `hilo.relaciones[]` (referencia existente, sin autorreferencia, tipo enum, `unidad_relevante` en `_meta.unidades_cubiertas`) y `relacion_candidata` cuando tipo=relacion_cross_hilo (`hilos` lista de 2 strings distintos, ordenados, ambos existentes; cuadros con prefijo `cuadro@`; `hilo_ref` y `hilo_destino` rechazados explícitamente para este tipo). Helper en dry-run sobre el canónico v11.85 detecta 173 candidatos — no se escribe ni se ejecuta sin orden explícita. Rediseño visual del modal queda para v11.87 (cuando haya `relaciones` cerradas que visualizar).

## [v11.85 — 2026-05-23] — Dashboard: drawer lateral → modal centrado (REDISEÑO §4.4)

Refactor del drawer del reciclaje en `web/index.html`. La columna lateral de 480px no daba espacio para explicaciones largas ni para el modal a página completa que el rediseño pide para `nivel: detalle` (§4.4). Sustituido por un **modal centrado** sobre overlay semi-transparente (rgba 0.55), con ancho `min(760px, 94vw)`, altura `max 88vh`, scroll interno, bordes redondeados y sombra elevada. Click fuera (overlay) cierra como antes. El id `rec-drawer` se conserva por compatibilidad con el JS — solo cambia el posicionamiento CSS. Sin tocar lógica de render ni datos. Sintaxis JS validada con `node --check`. Prepara la infraestructura para la siguiente iteración de explicaciones detalladas de Capa 2.

## [v11.84 — 2026-05-23] — Capa 2 sobre U1: etiquetas + propuestas (explicaciones pendientes)

Segunda sesión real de Capa 2 IA, sobre U1. Aplicado a `unidades/nc1-reciclaje.json`:

- **21 eventos U1 con etiquetas editoriales**: 9 `introduce`; 1 `amplia` (Números cardinales — U0 introdujo 0-10, U1 amplía 1-20); 1 `aplica` (Para la clase); 4 `anticipacion` (Adjetivos de nacionalidad → U2; Interrogativos → U3; Signos de puntuación → U7; Sonidos y correspondencias); 2 `[introduce, sistematiza]` (Artículos determinados con cuadro@p14#2 paradigma completo; verbal · ser con cuadros sistematizadores); 2 `[introduce]` verbal (llamarse, tener); 1 `[sistematiza]` (`voc · Saludos y despedidas` U1 — corregido durante la sesión: si U0 marcó `[anticipacion]`, U1 no puede ser `[introduce]`; lo correcto es `sistematiza` — U1 recoge lo activado en U0 y añade despedidas + registro formal/informal); 1 evento sin etiqueta (`voc · Gentilicios` U1 — en limbo hasta resolver la propuesta de alias).
- **Procedencia verbal decidida por Capa 2**: los 3 lemas (ser, llamarse, tener) → `reconciliado · "indice:Verbos ser, llamarse y tener (formas singulares)"`.
- **2 propuestas de la sesión U0 resueltas (rechazadas)**: `prop-abecedario-cobertura-cross-unidad` (fase 1 separó correctamente Abecedario vs Nombres de las letras); `prop-saludos-y-despedidas-vocab-vs-cultura` (cultura fuera del scope; se queda como vocabulario).
- **1 propuesta nueva abierta**: `prop-gentilicios-alias-adjetivos-nacionalidad` — diferida a U2.

**Pendiente declarado**: las **explicaciones** de los cuadros de U1 quedan sin escribir. El autor señaló que el criterio editorial necesita más rigor — las explicaciones deben ser flujos didácticos detallados, no descripciones de actividades, y deben aplicarse a cada etiqueta (incluyendo verbos con contexto de tiempos y formas) no solo a eventos con cuadro. Se redactan en próxima iteración tras tener el modal centrado del dashboard activo. Observación: typo `"Me lllamo"` en `verb · llamarse` U1 heredado del inventario fase 1.

Validador estructural sin errores. `_meta.version` sincronizado por el hook v11.82.

## [v11.83 — 2026-05-23] — Rectificación cobertura U7 · campo "Animales domésticos y salvajes"

Detectado por el autor: el CSV `unidades/U07-propuesta/tarjetas/csv/animales.csv` solo cubría 14 animales, alineado con `items[]` del inventario. Pero la nota `D-Animales-amplios` (v10.161) declaraba 18 lemas como ampliación del campo desde los textos de Destrezas (p78, p79) y solo se habían materializado 3 (orangután, yegua, potro); los 15 restantes faltaban en `items[]`.

- **Inventario** `unidades/U7/U7-nc1-inventario.json`: `items[]` 14 → 29 (+mamífero, anfibio, reptil, ave, ciervo, cebra, rana, tortuga, cocodrilo, víbora, pitón, boa, paloma, loro, cacatúa, en singular canónico). `fuentes` del campo ampliadas con `p78-act1`, `p78-act2`. Nota `D-Animales-amplios` reformulada como registro de la rectificación. Validación: 0/0/0.
- **CSV** `unidades/U07-propuesta/tarjetas/csv/animales.csv` (repo B): 14 → 29 filas, mismo formato (9 traducciones, 3 combos, sílaba tónica, gramapop).
- **Reapertura puntual de fase 1** en alcance U7 (cerrada en v10.164). Rectificación de cobertura por nota mal materializada, no cambio de contrato.

## [v11.82 — 2026-05-23] — Sincronización automática de `_meta` del canónico (pre-commit hook)

Tras v11.81 (sync manual), el autor pidió que la actualización fuera automática para no depender de la memoria humana. Implementado:

- **`scripts/sync_meta_reciclaje.py`** — idempotente: lee `CHANGELOG.md` (máximo `vX.Y`) y la fecha de hoy, escribe `_meta.version` y `_meta.fecha` en `nc1-reciclaje.json` solo si cambian.
- **`scripts/hooks/pre-commit`** — hook git que detecta si `unidades/nc1-reciclaje.json` está staged en un commit y, si lo está, ejecuta el sync y re-stage del JSON. Si no toca el canónico, no hace nada.
- **Instalación:** `git config core.hooksPath scripts/hooks` (una sola vez por checkout).
- **Documentación:** sección nueva en `fases/2-reciclaje/CLAUDE.md`.

Desde ahora cualquier commit que incluya cambios al canónico (regeneración de Capa 1, escritura directa de Capa 2, ediciones manuales) llevará `_meta.version` actualizado automáticamente. El dashboard refleja siempre la versión real sin intervención.

## [v11.81 — 2026-05-23] — Sync `_meta.version` del canónico (dashboard muestra versión actual)

Higiene. `_meta.version` de `nc1-reciclaje.json` lo escribe el generador de Capa 1; la última corrida fue en v11.76 y se quedó en `v11.77` (lectura del CHANGELOG en ese momento). Tras v11.77→v11.80 el JSON cambió varias veces sin regenerar (Capa 2 sobre U0 en v11.80 escribió etiquetas, explicación y propuestas directamente). El dashboard mostraba `v11.77` en la cabecera, desfasado del estado real. Sincronizado a `v11.81` para reflejar el contenido actual. Solo `unidades/nc1-reciclaje.json` (campo `_meta.version`).

## [v11.80 — 2026-05-23] — Capa 2 sobre U0 cerrada (primera unidad enriquecida)

Primera sesión real de Capa 2 IA completada — shakedown del procedimiento §12 sobre U0 (atípica, "Punto de partida"). Cambios sobre `unidades/nc1-reciclaje.json`:

- **6 eventos U0 con etiquetas editoriales**: `voc · Abecedario español` [introduce]; `voc · Países que hablan español` [introduce]; `voc · Números cardinales` [introduce]; `voc · Para la clase` [introduce]; `voc · Saludos y despedidas` [anticipacion]; `pron · Sonidos y correspondencias ortográficas` [anticipacion]. Corrección de la sesión previa: se retira `sistematiza` de Abecedario y Países — `sistematiza` exige contenido "ya activo" (`reglas §3`), y U0 es primera aparición canónica. Las dos pasan a solo `[introduce]`.
- **Explicación en `voc · Saludos y despedidas` U0** según el cuadro@p11 ("Buenos días / Buenas tardes / Buenas noches") — `analisis_ia` sitúa el evento en el arco U0→U1.
- **2 propuestas editoriales abiertas** en `propuestas[]`:
  - `prop-abecedario-cobertura-cross-unidad` (tipo: `siempre_presente`) — ¿debería el hilo `voc · Abecedario español` recoger eventos en U1+ cuando el inventario alfabético reaparece transversalmente, o ya están cubiertas por otros hilos (sonidos, letras homófonas)?
  - `prop-saludos-y-despedidas-vocab-vs-cultura` (tipo: `reconciliacion`) — tensión entre fase 1 (lo categorizó como `vocabulario`) y el curso (lo declara como `cultura` en U1). El contenido es funcionalmente pragmático; decidir si reclasificar el hilo o aceptar la simplificación léxica.
- Ambas propuestas se difieren a la sesión de U1 — su naturaleza cross-unidad pide ver primero cómo reaparecen los contenidos antes de cerrar la decisión.

Validador estructural sin errores. U0 cumple los criterios §13 (a) chequeo estructural + (c) revisión editorial; las propuestas que afectan a U0 quedan explícitamente diferidas. Primera evidencia del flujo `Capa 1 mecánica → sesión Capa 2 → merge no destructivo` funcionando end-to-end sobre una unidad real.

## [v11.79 — 2026-05-23] — Glosario: documenta las iniciales I/E/P/F del dashboard en `procedencia_indice`

Deuda documental retroactiva. La tabla del glosario raíz para `procedencia_indice` describía los 4 casos editoriales del dashboard pero no enseñaba las iniciales (I/E/P/F) que el dashboard usa. Añadida columna "Inicial dashboard" + nota de que el JSON conserva 3 valores técnicos y las 4 iniciales viven solo en la vista (`REC_PROCEDENCIA_CATS`, `web/index.html`). Solo `glosario.md`.

## [v11.78 — 2026-05-23] — Dashboard drawer: `reconciliado_con` visible como texto persistente

Micro-UX. En v11.77 el chip de procedencia se afinó a 4 categorías (I/E/P/F), pero el `reconciliado_con` completo (`indice:Números 0-10`, `pcic:A1`, etc.) solo era visible al pasar el cursor por el chip (`title`) — invisible en móvil/touch y poco escaneable. v11.78 lo muestra **como texto persistente** en la fila del evento del drawer, en gris claro itálico, precedido por flecha (`→ indice:Números 0-10`). Sin perder el tooltip — el `title` con `procedencia · reconciliado_con` se mantiene como hover-detail. Solo `web/index.html`; sintaxis JS validada.

## [v11.77 — 2026-05-23] — Dashboard: leyenda de procedencia con 4 chips (separa `reconciliado` por prefijo)

Follow-up no bloqueante de v11.76. Ahora que `reconciliado_con` lleva prefijo (`indice:` o `pcic:`), la leyenda del dashboard que decía `[E] reconciliado según el PCIC` para todo era imprecisa. v11.77 divide visualmente la categoría:

| JSON | Rótulo en dashboard | Inicial |
|---|---|---|
| `procedencia: declarado` | contenido del índice | **I** |
| `procedencia: reconciliado` + `reconciliado_con: "indice:..."` | equivalente del índice | **E** |
| `procedencia: reconciliado` + `reconciliado_con: "pcic:..."` | reconciliado según el PCIC | **P** |
| `procedencia: nuevo` | fuera del índice | **F** |

El JSON sigue con 3 valores técnicos (`declarado`/`reconciliado`/`nuevo`) — la sub-división vive **solo en la vista**. Reparto visible hoy: I=78 · E=4 · P=44 · F=3 · sin asignar=154 (verbal). Solo `web/index.html`; sintaxis JS validada con `node --check`.

## [v11.76 — 2026-05-23] — Modelo: triage identitario mecánico (alias + PCIC) + merge no destructivo

Tras revisión del autor de v11.75: la cautela "Capa 1 sin aliases" era una sobrecorrección — `campos-semanticos-canonicos.json` (`origen` + `aliases_indice`) y `gramatica-canonica.json` / `pronunciacion-ortografia-canonica.json` / `perifrasis-canonicas.json` (`_pcic_ref`) ya traen el respaldo estructurado para resolver `reconciliado` mecánicamente. Tres cambios:

**Modelo (REDISEÑO §9, reglas §4, glosario, prompt fase 2, schema §3):**

- `procedencia_indice` se resuelve **íntegramente en Capa 1** para vocabulario, gramática, pron/orto y perífrasis (lee registries). El bloque **verbal queda como excepción** mientras `verbos-canonicos.json` no exponga respaldo estructurado equivalente — la procedencia sale sin asignar y la Capa 2 la decide. Documentado explícitamente.
- `reconciliado_con` amplía semántica con **prefijos obligatorios**: `"indice:<entrada>"` (alias del índice del curso) o `"pcic:<ref>"` (`"pcic:A1"` como fallback). Schema §3 + validador estructural actualizados.
- Capa 2 deja de tener procedencia en su núcleo de tareas: solo verbal o corrección excepcional.

**Generador (`scripts/generar_reciclaje_capa1.py`):**

- `IndiceCurso` preserva la entrada literal del índice para resolver `indice:<X>`; `Registries` expone `campos_raw`, `gramatica_raw`, `pronorto_raw`, `perifrasis_raw` con metadata cruda; nuevo `Constructor.resolver_procedencia()` aplica las reglas mecánicamente.
- **Merge no destructivo**: la regeneración fusiona con el archivo previo — sobreescribe campos mecánicos (`procedencia_indice`, `reconciliado_con`, `evidencias`, `formas`), preserva interpretativos (`etiquetas`, `explicacion`, `detalle`). En `verbal`, donde `procedencia_indice` y `reconciliado_con` son trabajo de Capa 2 (no mecánico), también se preservan — y el detector de pérdidas los considera enriquecimiento editorial. **Abort por defecto ante pérdida**. Flag `--permitir-perdidas` (opt-in) vuelca el detalle en `docs/historico/`.
- `validar_capa1()` relajada: acepta `declarado` / `reconciliado` / `nuevo` y exige prefijo en `reconciliado_con`.

**Reparto nuevo:** 78 declarado · 48 reconciliado (44 con `pcic:`, 4 con `indice:`) · 3 nuevo · 154 sin asignar (verbal). Validadores estructural + cross-unidad sin regresión (14 alertas idénticas, son de datos). Las etiquetas de Capa 2 ya escritas en U0 sobreviven al merge — 0 pérdidas detectadas en esta regeneración.

**Nota UX pendiente**: la leyenda del dashboard `[E] reconciliado según el PCIC` es ligeramente imprecisa ahora que algunos reconciliados llevan prefijo `indice:` (4 de 48). El drawer muestra el `reconciliado_con` completo y eso aclara el caso. Si se valora, una iteración v11.77 puede afinar la rotulación.

## [v11.75 — 2026-05-23] — Modelo: `procedencia_indice` pasa a eje identitario puro (curso-wide, sin aliases)

Corrección de modelo Nivel 1/2 tras feedback del autor en la sesión de Capa 2 sobre U0: el `procedencia_indice` antiguo (§9.1) **mezclaba dos ejes** — pertenencia al índice del curso y temporalidad respecto de la unidad canónica —, produciendo casos donde "Saludos y despedidas U0" salía como `nuevo` aunque el curso lo declara para U1. **Cambio:** `procedencia_indice` se redefine como **eje identitario puro**, evaluado **curso-wide**, sin uso de aliases del registry:

- `declarado` → el título canónico coincide literalmente con una entrada del índice del curso **en cualquier unidad** (no solo la del evento). Lo precomputa la Capa 1.
- `reconciliado` → alias / equivalencia PCIC. Decisión de Capa 2, propuesta + cierre humano. **La Capa 1 no usa aliases para `declarado`** (cautela importante: si se metiera el alias por la puerta de atrás, se re-mezclarían los ejes).
- `nuevo` → no aparece en el índice del curso en ninguna unidad ni es reconciliable.

La temporalidad (esta unidad vs la canónica) la lleva **enteramente la etiqueta**: `anticipacion` (antes), sin etiqueta temporal (en su unidad canónica), `aplica` (después).

Archivos: `REDISEÑO-EN-CURSO.md` §9 reformulado · `reglas-reciclaje.md` §4 + §14 R1 sincronizados · `glosario.md` raíz · `scripts/generar_reciclaje_capa1.py` (`IndiceCurso` simplificado a un solo set curso-wide; `declarado()` sin aliases; `add_evento_mapa` decide procedencia con la misma regla) · `nc1-reciclaje.json` regenerado. Reparto nuevo: **100 eventos `declarado`** (antes 41) y 183 sin asignar (para Capa 2 triar `reconciliado`/`nuevo`). Validador estructural y cross-unidad sin regresión (14 alertas R1/R4 idénticas, son de datos).

## [v11.74 — 2026-05-23] — Revisión R1/R4: diagnóstico y dos propuestas anotadas para Capa 2

Lectura una a una de las 14 alertas del validador cross-unidad sobre el canónico v11.68. Ninguna es bug de fase 1. **12 son insumo normal del pipeline**: las 6 R1 (anticipación material) alimentarán la etiqueta `anticipacion` cuando Capa 2 procese U1-U6; 6 de las 8 R4 son léxico PCIC incidental coherente con la unidad (`recurrente` de fondo, §3.6). **2 sospechosas anotadas en bitácora REVIEW** como propuestas a abrir en la sesión de Capa 2 — para no depender de memoria de sesión: `Gentilicios` U1 (posible alias de `Adjetivos de nacionalidad`) y `Bebida` U4 (tensión índice↔contenido — el título "Comidas y bebidas" no cuadra con el principal declarado). Sin tocar datos ni registries; solo registro de la revisión y las dos propuestas pendientes.

## [v11.73 — 2026-05-23] — Higiene: eliminar `diff_index.txt`

Artefacto suelto (140 líneas, un `git diff > …` antiguo, no funcional) colado en v11.72 al usar `git add -A`. Commit aislado solo con el borrado. Compromiso: usar pathspec explícito en `git add` también en repo A para que no se repita.

## [v11.72 — 2026-05-23] — Dashboard RECICLAJE: dos ejes visuales ortogonales (etiqueta + procedencia del índice) con rótulos editoriales

Itera sobre v11.71 a partir de feedback del autor mirando la vista: el evento tiene dos ejes ortogonales (`etiquetas` y `procedencia_indice`, `REDISEÑO §9.5`) y el dashboard solo mostraba uno. Cambios en `web/index.html`:

- **Quitadas las dos notas verbosas de arriba** (nivel + estado de etiquetas).
- **Dos leyendas compactas en su lugar**, una por eje. Cada chip lleva su marca + rótulo + `(n)` con el reparto real; los valores sin presencia se ven atenuados (no fingen estar).
- **Diferenciación no cromática** entre ejes para que ningún chip se pueda confundir con otro: etiqueta sigue como **círculo de color**; procedencia pasa a **cuadrito gris oscuro con inicial mnemotécnica** (`I` contenido del índice · `E` reconciliado según el PCIC · `F` fuera del índice). Los dos ejes hablan visualmente lenguajes distintos (color vs letra) — imposible solapamiento.
- **Rótulos editoriales** para `procedencia_indice` — los técnicos eran opacos al editor:

  | JSON | Dashboard |
  |---|---|
  | `declarado` | **contenido del índice** |
  | `reconciliado` | **reconciliado según el PCIC** |
  | `nuevo` | **fuera del índice** |

  El JSON conserva los valores técnicos; el mapeo a rótulos vive solo en la vista. El drawer también muestra el rótulo editorial.

Glosario raíz (`glosario.md` Bloque 2) actualizado: nueva entrada `procedencia_indice` con tabla técnico↔editorial y significado de cada valor.

Reparto actual visible: 41 eventos `[I]` contenido del índice, 0 `[E]` reconciliado según el PCIC (atenuado), 0 `[F]` fuera del índice (atenuado), 242 sin asignar. Etiquetas: 0/283 (las 7 atenuadas) + 283 sin etiquetar (Capa 2 aún sin estrenar).

## [v11.71 — 2026-05-23] — Dashboard RECICLAJE: corrección UX (badge `auto` y leyenda Capa 2)

Tres correcciones puntuales sobre v11.70, a partir de feedback del autor mirando la vista real:

1. El badge `AUTO` aparecía con fondo lila intenso en las 118 filas con el mismo valor — ruido visual sin información. Ahora solo se muestra como **marcador pequeño sin fondo** y **únicamente cuando el hilo se desvía del nivel dominante** (hoy: ningún hilo se desvía → 0 marcadores por fila).
2. Nueva **nota global discreta** arriba de la vista con el reparto de niveles ("118/118 hilos en `auto`. Esqueleto poblado desde inventarios; la Capa 2 IA aún no ha generado hilos en `detalle`.").
3. La leyenda de "Etiqueta del evento (Capa 2)" prometía 7 colores que **no aparecen** en el render (todos los puntos son grises hoy). Se sustituye por una **nota honesta** que describe el estado-esqueleto y enumera las etiquetas por nombre, no por chip de color. Cuando la Capa 2 corra y existan eventos etiquetados, la nota cambia automáticamente al modo "colores reales".

Solo `web/index.html`; sintaxis verificada con `node --check`. Sin tocar datos ni lógica.

## [v11.70 — 2026-05-22] — Dashboard: vista RECICLAJE adaptada al shape del rediseño

La vista RECICLAJE de `web/index.html` estaba construida para el shape pre-rediseño (`h.tipo`, `ev.accion`, `ev.impacto`, `ev.descripcion`, `h.usos`, `recData.actualizado`) y quedó rota tras la regeneración de `nc1-reciclaje.json` en v11.68 — un consumidor del archivo que la validación de v11.68 no cubrió. Rewire al modelo nuevo: agrupación por `bloque`, badge de `nivel_analisis`, eventos con `etiquetas[]` (chips múltiples), `procedencia_indice` y `evidencias[]`; drawer con `evidencias`/`formas`/`tiempo`; cabecera de la vista con `_meta.fecha`/`estado` y conteo de hilos/propuestas; bloque `propuestas[]` separado al final con estado vacío sobrio. El estado-esqueleto de Capa 1 (eventos con `etiquetas: []`) se representa como **válido** — dot gris, "sin etiquetar (Capa 1)" — sin fingir semántica de Capa 2 inexistente. Solo `web/index.html` (−119 líneas netas: el modelo nuevo es más plano, sin `usos`/`tipos_verbo` anidados); `diagrama.py` sin cambios (`/api/reciclaje` ya sirve el archivo tal cual). Sintaxis JS verificada con `node --check`.

## [v11.69 — 2026-05-22] — Fase 2 REACTIVADA (lote documental)

Levantada la pausa de la decisión 36. El Nivel 4 del rediseño cerró su parte de herramienta (v11.62-v11.68: Capa 1, los dos validadores del gate, `nc1-reciclaje.json` regenerado al shape del rediseño), así que la pausa deja de tener objeto. Lote **documental**, sin lógica nueva: `CLAUDE.md`/`prompt.md`/`reglas-reciclaje.md` de fase 2 actualizados (banners de estado → REACTIVADA; comandos reales del pipeline `generar_reciclaje_capa1.py` y del gate `validar_reciclaje.py`/`validar_cross_unidad.py`); `scripts/integrar_unidad.py` retira el flag `--regenerar-reciclaje` y la lógica de cuarentena — el reciclaje lo gestiona el pipeline de fase 2, no la integración (`REDISEÑO-EN-CURSO.md` §13.4); `CLAUDE.md` raíz, `README.md`, `REVIEW.md`, `PROCESO-MAESTRO.md` sincronizados. **Cautela explícita en los contratos:** la Capa 2 (sesión IA enriquecedora) nunca se ha ejecutado — su primera corrida real será también su shakedown. La reactivación habilita el pipeline; correr la Capa 2 unidad a unidad es la pieza siguiente, no parte de este lote.

## [v11.68 — 2026-05-22] — Fase 2 Nivel 4: regeneración del canónico `nc1-reciclaje.json`

`nc1-reciclaje.json` se regenera con el generador de Capa 1 (v11.62-v11.63): el archivo pasa del shape pre-rediseño v10.114 (181 hilos, claves `curso/_acciones_validas/...`) al shape del rediseño (`_meta/hilos/propuestas`, 118 hilos / 283 eventos). Validado: validador estructural 0 errores contra `schema-reciclaje.md`; validador cross-unidad R1-R5 — pre-condiciones R2/R5 OK, 14 alertas R1/R4 idénticas a v11.65 (son de datos, no regresión de generación). `propuestas[]` queda vacío (el archivo viejo no tenía). Con esto la Capa 1 del pipeline de fase 2 queda materializada de extremo a extremo. **Fase 2 sigue PAUSADA**: la regeneración produce el esqueleto mecánico, no reactiva la fase — pendientes la Capa 2 (sesión IA enriquecedora) y la reactivación operativa. Archivo: `unidades/nc1-reciclaje.json`.

## [v11.67 — 2026-05-22] — Eliminado `contenidos_indice` del inventario canónico

`contenidos_indice` era una copia del índice editorial dentro de cada inventario — duplicación de lo que ya vive en `nc1-curso.json`, desincronizada desde 2026-05-08 (deuda técnica conocida ya registrada en B1.4). Se **elimina**: el índice del curso tiene fuente única en `nc1-curso.json` (regla de oro 4). Campo retirado de los 10 inventarios U0-U9. `validar_inventario.py` deja de exigirlo; `verificar_integridad.py` chequeo 4 limpio (la comparación retirada en v11.66 pasa a definitiva). Contratos de fase 1 actualizados: `schema-inventario.md` (12 claves obligatorias, antes 13), `glosario.md`, `reglas-operativas.md`, `PROCESO-MAESTRO.md`. El dashboard conserva el bloque "Índice de contenidos" leyéndolo ahora de `nc1-curso.json` — `get_inventario` adjunta `_indice_curso` (`diagrama.py` + `web/index.html`). Validación: U0-U9 a 0/0/0, `verificar_integridad.py` 9/9 (0 errores), `validar_cross_unidad.py` sin regresión. Cierra de paso la contradicción glosario↔PROCESO-MAESTRO sobre si `contenidos_indice` debía coincidir o podía divergir.

## [v11.66 — 2026-05-22] — Fase 1: fix del chequeo 4 de `verificar_integridad.py`

Micro-fix de un comparador desactualizado, detectado al implementar v11.65. El chequeo 4 (cabecera↔`nc1-curso.json`) daba 55 falsos positivos: (a) comparaba `nivel` por unidad cuando es un campo **global** de `nc1-curso.json` — corregido a comparar contra el global; (b) comparaba `contenidos_indice` (texto concatenado del inventario, copia abreviada de ~2026-05-05) contra los campos de `nc1-curso.json` (listas, índice fiel al libro, creado 2026-05-08) — divergen en shape y contenido. Esa segunda comparación se **retira temporalmente**: el glosario de fase 1 exige coincidencia exacta de `contenidos_indice` con `nc1-curso.json`, y la vía limpia no es relajar el contrato sino **regenerar `contenidos_indice` desde la fuente canónica** — pieza aparte pendiente (incluye decidir si `contenidos_indice` pasa a listas o se compara texto↔`join(lista)`). Tras el fix, `verificar_integridad.py` pasa entero (0 errores, exit 0). No toca datos de inventario. Archivo: `scripts/verificar_integridad.py`.

## [v11.65 — 2026-05-22] — Fase 2 Nivel 4: validador cross-unidad R1-R5

Componente (b) del gate de cierre (`reglas-reciclaje.md` §13-§14). Nuevo `scripts/validar_cross_unidad.py`. R2 y R5 (pre-condiciones que abortan) se **delegan** a `verificar_integridad.py` (chequeos 1/2/3/5 — regla de oro 4, no se re-implementa lo que fase 1 ya valida); R1, R3, R4 (alertas) se calculan sobre los inventarios. R1 en **versión proxy determinista** (decisión 2026-05-22): detecta categorías `recurrente` en U(n) cuyo `principal` es posterior — anticipación material trazable, descartado el análisis de frecuencia sobre texto crudo por ruidoso. R3: categorías en la dimensión equivocada vs los registries. R4: `recurrente` que nunca es `principal` + lemas verbales en `vocabulario_consolidado`. Ejecución actual: pre-condiciones R2/R5 OK; 14 alertas (R1×6, R4×8, R3×0) — observaciones cross-unidad que el validador per-unidad de fase 1 no puede ver. Hallazgo informativo (no aborta): `verificar_integridad.py` chequeo 4 (cabecera↔`nc1-curso.json`) falla con 55 errores — **no es drift de datos**: el chequeo 4 quedó desactualizado respecto al shape actual de `nc1-curso.json` (compara `nivel` por unidad, que hoy es global, y `contenidos_indice` texto contra listas). Ajeno a R2/R5; arreglo trivial pendiente como pieza aparte de fase 1. Archivo: `scripts/validar_cross_unidad.py` (nuevo).

## [v11.64 — 2026-05-22] — Fase 2 Nivel 4: validador estructural como script

Componente (a) del gate de cierre (`reglas-reciclaje.md` §13). Nuevo `scripts/validar_reciclaje.py` — chequeo estructural de `nc1-reciclaje.json` contra `schema-reciclaje.md` (claves, tipos, enumeraciones); valida el archivo en cualquier estadio del pipeline (salida de Capa 1 o enriquecida por Capa 2 con etiquetas, `reconciliado`/`nuevo`, `explicacion`, `detalle`). `generar_reciclaje_capa1.py` se refactoriza para **importar** ese validador (fuente única, regla de oro 4): su `validar()` se parte en `validar_schema` (compartido) + `validar_capa1` (invariantes §11.4 propias de la salida de Capa 1, que no aplican a un archivo ya enriquecido). Dry-run del generador sin regresión (118 hilos / 283 eventos / OK); validador en seco sobre salida fresca de Capa 1: 0 errores. El canónico `nc1-reciclaje.json` sigue intacto (en shape pre-rediseño, no conforme — esperado hasta el Nivel 4). Archivos: `scripts/validar_reciclaje.py` (nuevo), `scripts/generar_reciclaje_capa1.py`.

## [v11.63 — 2026-05-22] — Fase 2 Nivel 4: proyección `mapa` de la Capa 1

Cierra la laguna declarada en v11.62. `scripts/generar_reciclaje_capa1.py` añade la proyección de nivel `mapa` (§4.2/§4.5): siembra desde el índice de `nc1-curso.json` con resolución **conservadora** — resuelve una entrada del índice a su título canónico solo si la coincidencia es inequívoca (§11.4 invariantes 2-3); las entradas que no resuelven (lemas verbales embebidos en `gramatica`, divergencias de naming con los registries, pron a nivel de subcategoría) se reportan como **avisos**, no se fuerzan. `nivel_analisis` pasa a calcularse según el grado de población (`auto` si el hilo tiene evento respaldado por inventario, `mapa` si solo está declarado en el índice). Dry-run: 118 hilos (auto 118 / mapa 0 — curso íntegramente cubierto) / 283 eventos / 41 con `procedencia_indice: declarado` / 25 avisos / validación OK. El canónico `nc1-reciclaje.json` sigue sin reescribirse. Archivo: `scripts/generar_reciclaje_capa1.py`.

## [v11.62 — 2026-05-22] — Fase 2 Nivel 4: generador de Capa 1 validado en dry-run

Primer paso del Nivel 4 (implementación en código), **checkpoint de herramienta, sin reactivar fase 2**. Nuevo `scripts/generar_reciclaje_capa1.py` — Capa 1 modo íntegro: materializa la **proyección `auto`** del contrato §11 (hilos de los 5 bloques desde inventarios, eventos, `evidencias`, `formas`, `procedencia_indice: declarado`), preserva `propuestas[]` y valida la salida contra `schema-reciclaje.md` + las 10 invariantes §11.4 antes de escribir. Dry-run: 118 hilos / 283 eventos / OK. Laguna conocida: la proyección de nivel `mapa` desde `nc1-curso.json` (§11, `REDISEÑO` §4.2) **aún no se materializa** — todos los hilos salen `auto`; pendiente del Nivel 4. El canónico `nc1-reciclaje.json` **no se reescribe**. Nota empírica diferida añadida en `REDISEÑO-EN-CURSO.md` §7.4. Archivos: `scripts/generar_reciclaje_capa1.py` (nuevo), `REDISEÑO-EN-CURSO.md`.

## [v11.61 — 2026-05-21] — Fase 2: cierre de la deriva terminológica Nivel 3/Nivel 4 en el `CLAUDE.md`

Micro-lote de coherencia tras v11.60. El `CLAUDE.md` de fase 2 aún tenía 6 referencias que situaban la implementación en código en "Nivel 3", contradiciendo el cierre del Nivel 3 (diseño) ya registrado en `REDISEÑO-EN-CURSO.md`: el banner (scripts viejos "se sustituirán en el Nivel 3"), la tabla `nivel_analisis`, "Cómo se invoca", "Cómo se invoca / nivel auto", "Cómo validar" y la tabla "Para qué consultar". Las 6 corregidas: la implementación en código y la sustitución de los scripts viejos son **Nivel 4**; el Nivel 3 (diseño del pipeline) está cerrado. Banner de estado actualizado a v11.61. Sin cambios de modelo — solo coherencia documental; cierra el riesgo documental señalado por el revisor.

## [v11.60 — 2026-05-21] — REDISEÑO fase 2 §13: wiring del pipeline — Nivel 3 (diseño) completo

Última pieza de diseño del Nivel 3. Nueva §13 en `REDISEÑO-EN-CURSO.md` — wiring del pipeline: consolida el encadenado end-to-end (no abre decisiones nuevas). Cinco bloques: propósito; flujo incremental por unidad (Capa 1 → Capa 2 → gate → integración); flujo en hitos cross-unidad (revisión ampliada, que no es regeneración íntegra) y cierre global; puntos de corte y abortos (el gate va después de Capa 2 y antes de integración — si falla, no hay integración a main; la integración la hace el ejecutor coordinador, no la sesión de Capa 2); y **frontera explícita Nivel 3 / Nivel 4** — Nivel 3 define el contrato del encadenado, Nivel 4 lo implementa en código, regenera `nc1-reciclaje.json` y reactiva la fase. **Con esto el Nivel 3 (diseño del pipeline) queda completo.** Corregida en el mismo lote la deriva terminológica que situaba el código en "Nivel 3": `CLAUDE.md` de fase 2 y `prompt.md` (×3) pasan a decir que la implementación en código es Nivel 4. Queda solo el Nivel 4.

## [v11.59 — 2026-05-21] — REDISEÑO fase 2 §12: procedimiento de la sesión de Capa 2

Segunda pieza del Nivel 3. Nueva §12 en `REDISEÑO-EN-CURSO.md` — procedimiento de la sesión IA enriquecedora (Capa 2), que opera sobre el esqueleto de Capa 1 sin reconstruirlo. (1) **Inputs**: el `nc1-reciclaje.json` salido de Capa 1, el inventario de la unidad, `nc1-curso.json`, los 5 registries, el reciclaje actual (para preservar `propuestas[]`), las marcas internas de fase 1 como contexto revisable (no autoridad) y el recorrido previo consolidado de unidades anteriores (necesario para `amplia`/`aplica`/`sistematiza`/`contrasta` y el triage). (2) **Secuencia** de 7 pasos en 3 fases que no se mezclan: precondiciones de arranque (pre-chequeo R2/R5 + shape) · trabajo editorial (3 momentos de análisis, etiquetas, triage, `explicacion`, `propuestas[]`) · gate de cierre. (3) El nivel **`detalle` no es salida obligatoria por unidad**: la pasada por unidad produce etiquetas/triage/`explicacion`/propuestas; el `detalle` se promueve en los hitos cross-unidad cuando el hilo tiene masa crítica. (4) **Régimen**: sesión IA supervisada por unidad en Chat B; la IA propone, el autor cierra o difiere; las `propuestas[]` basta con que queden resueltas o explícitamente diferidas. Queda en el Nivel 3 solo el wiring.

## [v11.58 — 2026-05-21] — Fase 2 Nivel 3: §R.1 procesado — validador cross-unidad R1-R5

Procesada la pieza §R.1 del Reservorio (R1-R5, validación cruzada cross-unidad heredada del rediseño viejo §7). Convertida en contrato operativo: nueva §14 en `reglas-reciclaje.md` — "Validador cross-unidad — R1-R5". Reformulaciones aplicadas sobre el material heredado: **R2** redefinido de "literalidad universal" a **materialidad y trazabilidad** (en vocabulario los ítems aparecen literalmente, en verbal las formas/lema atestiguados, en gramática/pron-orto la categoría trazada a actividades/cuadros — la etiqueta canónica no aparece literal en el libro); **R3** acotado a "errores de clasificación por dimensión". R2 y R5 son pre-condiciones (fallo = bug de fase 1, aborta); R1, R3, R4 producen alertas para el criterio de cierre §13. El nombre del script y el nivel de implementación no se cristalizan — "se difiere al bloque de implementación del pipeline". Con esto el **Reservorio §R queda vacío y se retira** de `REDISEÑO-EN-CURSO.md`: el rediseño ya no tiene material heredado sin procesar. Actualizados el apéndice §N (§7 viejo → cerrado en §14), §5 Nivel 3 y la cabecera del documento.

## [v11.57 — 2026-05-21] — Fase 2 Nivel 3: sincronización del conteo de categorías — paquete de registries cerrado

Cuarta y última pieza del paquete de registries del Nivel 3. Sincronizadas las 5 referencias activas que aún decían "17 categorías" para `gramatica-canonica.json` — stale desde v10.156 (alta de "Imperativo (tú)") y ahora 23 tras las 5 altas de v11.56: `PROCESO-MAESTRO.md` (árbol del repo), `reglas-operativas.md` (×2), `prompt-dry-run.md` y `glosario.md` (tabla de fuentes PCIC). Las menciones "17" en bitácora histórica (REVIEW, CHANGELOG archivado) no se tocan — describen estados pasados, no contrato vivo. **Con esto el paquete de registries del Nivel 3 queda cerrado** (4/4): `perifrasis-canonicas.json` creado · `_grupo` añadido · 5 altas de "Tiempos y modos verbales" · conteo sincronizado.

## [v11.56 — 2026-05-21] — Fase 2 Nivel 3: 5 altas en `gramatica-canonica.json` (Tiempos y modos verbales)

Tercera pieza del paquete de registries, parte 2: las altas. `gramatica-canonica.json` pasa de v1.6 a **v1.7**, de 18 a **23 categorías** — 5 altas nuevas en el grupo "Tiempos y modos verbales", como primera aplicación del procedimiento §2-bis: **Paradigma regular del presente (-ar/-er/-ir)**, **Irregularidad vocálica e→ie (presente)**, **Irregularidad vocálica o→ue (presente)**, **Infinitivo simple** (carril flexión) y **Uso del imperativo — instrucciones y peticiones** (carril uso). Cada una con `_grupo`, `_pcic_ref`, `_apariciones` (verificado por unidad — solo evidencia material con cuadro/sistematización) e `items` (testigos del patrón / ejemplos del cuadro). De los 7 candidatos del relevo, **2 no se canonizan**: los usos del presente ("actual"/"durativo" del PCIC, o el framing didáctico hábitos/describir) — NC1 usa el presente intensivamente pero no lo sistematiza con cuadro propio, así que por §2-bis quedan como **análisis interpretativo de fase 2** (`analisis_ia`/`detalle`), no como categoría de registry. §6.4 de `REDISEÑO-EN-CURSO.md` reformulado: la frontera de canonización se ancla al **umbral de evidencia material**, no al carril (un uso sí entra al registry si tiene cuadro — caso del imperativo). Pendiente (4/4 del paquete): sincronizar las referencias documentales que aún dicen "17 categorías".

## [v11.55 — 2026-05-21] — Fase 2 Nivel 3: §2-bis — procedimiento de canonización de categorías gramaticales

Tercera pieza del paquete de registries, parte 1: el **procedimiento**. Añadida §2-bis a `reglas-reciclaje.md` ("Canonización de categorías gramaticales nuevas"), colocada tras §2 (Naming canónico) sin renumerar §3-§13. Responde a la cuestión de replicabilidad planteada por el autor: las categorías canónicas son específicas del curso, pero el **método para darlas de alta debe ser reproducible** — con otro libro o nivel se re-ejecuta, no se improvisa. Cuatro pasos en orden: (1) fuentes admitidas (plan curricular del nivel + corpus del curso, ambas necesarias; ninguna otra base); (2) separación en dos carriles que no se mezclan — flexión/paradigmas vs usos de tiempos y modos; (3) criterio de alta con umbral de evidencia (evidencia material obligatoria, separación por paradigma/uso real, naming anclado al plan curricular, lo débil o lema-específico no se canoniza); (4) cierre humano (la IA propone, el autor decide, ninguna alta automática). Las 7 altas aprobadas para el grupo "Tiempos y modos verbales" se ejecutarán como primera aplicación de este procedimiento (parte 2, pendiente).

## [v11.54 — 2026-05-21] — Fase 2 Nivel 3: campo `_grupo` en `gramatica-canonica.json`

Segunda pieza del paquete de registries del Nivel 3. Añadido el campo `_grupo` a las 18 categorías de `gramatica-canonica.json` (registry `_meta.version` 1.5→1.6). No es canon nuevo: es una capa de organización interna ya decidida en `REDISEÑO-EN-CURSO.md` §6.3, mapeada sobre categorías que ya existen. Cada categoría se asigna a uno de los 7 grupos por subsistema gramatical — Determinantes (4), Pronombres (3), Sintagma nominal y concordancia (3), Construcciones (3), Adverbios y marcadores (3), Preposiciones (1), Tiempos y modos verbales (1, `Imperativo (tú)` — crecerá en la 3.ª pieza con flexión + usos). Casos frontera resueltos con el autor: `Interrogativos` se queda en Pronombres (la función adverbial de dónde/cuándo/cómo se resuelve en el análisis de fase 2, no abriendo categoría); `Hay` y `Construcción gustar/doler` en Construcciones (construcciones oracionales con verbo fijo, no flexión); `Adverbios y marcadores` se mantiene como grupo único (no se parte en mono-específicos: `_grupo` organiza lectura, la unidad analítica sigue siendo la categoría). No se tocaron nombres canónicos ni `_pcic_ref`. *(Las referencias "17 categorías" en docs de fase 1 — PROCESO-MAESTRO, reglas-operativas, prompt-dry-run — quedan stale desde v10.156; se sincronizan en la 4.ª pieza del paquete, junto al conteo final tras añadir las categorías de "Tiempos y modos verbales".)*

## [v11.53 — 2026-05-21] — Fase 2 Nivel 3: registry `perifrasis-canonicas.json`

Primera pieza del paquete de registries del Nivel 3. Creado `fases/2-reciclaje/perifrasis-canonicas.json` — el 5.º registry del universo cerrado, derivado y propio de fase 2 (ubicado en `fases/2-reciclaje/` por propiedad de fase: fase 1 no lo gobierna ni lo valida, solo transporta `estructura_perifrastica` como dato libre). Poblado desde el relevo del campo `estructura_perifrastica` en los inventarios U0-U9 (solo lectura, sin tocar canon de fase 1): dos perífrasis con evidencia material — `ir a + infinitivo` (U2, U4; con respaldo PCIC A1 §9.1.1) y `querer + infinitivo` (U6; entra por evidencia material de NC1 — PCIC A1 lo trata como infinitivo objeto, no como perífrasis). Documentadas en `_meta`: la deuda de codificación U4↔U6 de `querer + infinitivo` (U4 no la etiquetó como `estructura_perifrastica`; `_apariciones` registra solo U6 hasta corregir U4) y la exclusión de `tener que + infinitivo` del primer corte (sin evidencia material). El universo cerrado pasa a 5 registries — físicamente 4 (fase 1) + 1 (fase 2); path explícito añadido en `reglas-reciclaje.md` §2.

## [v11.52 — 2026-05-21] — REDISEÑO fase 2 §11: procedimiento de la Capa 1 (Nivel 3 arranca)

Arranca el Nivel 3 (implementación) del rediseño de fase 2. Nueva §11 en `REDISEÑO-EN-CURSO.md` — procedimiento de la Capa 1 como contrato de implementación del script determinista. (1) **Inputs**: 4 — `nc1-curso.json`, inventarios cerrados, los 5 registries canónicos, y el estado actual de `nc1-reciclaje.json` (no como fuente del contenido mecánico sino para preservar `propuestas[]` y cierres humanos). (2) **Qué genera**: la proyección mecánica válida contra el schema — hilos (`id`, `bloque`, `titulo`, `_grupo`, `nivel_analisis`) y eventos básicos; nunca `reconciliado`/`nuevo`, `explicacion`, `detalle` ni etiquetas editoriales. (3) **Qué precomputa**: solo lo literal y determinista (`procedencia_indice: declarado`, `formas`, `tiempo`, `evidencias`, `_meta`). (4) **10 invariantes** que la Capa 2 puede dar por garantizados (identidad, canonicidad, tipado, no-duplicación de eventos, no-invención editorial, preservación de `propuestas[]`). (5) **Ejecución**: un mismo algoritmo parametrizado por alcance (incremental/íntegro). Es diseño del procedimiento; el código Python se escribe en la reactivación, cuando los registries estén poblados.

## [v11.51 — 2026-05-21] — Fase 2: limpieza de drift documental antes del Nivel 3

Dos correcciones de coherencia señaladas por el revisor. (1) `CLAUDE.md` de fase 2 §"Cómo se invoca" decía que la pausa de fase 2 dura "mientras el canon semántico de fase 1 está en desarrollo" — contradice el estado real (fase 1 cerrada en v10.164); reformulado: la pausa dura mientras esté pendiente la implementación del Nivel 3 del rediseño. (2) `REDISEÑO-EN-CURSO.md` §6.5 punto 2 seguía diciendo que el `CLAUDE.md` de fase 2 estaba "sincronizado parcialmente" — ya está sincronizado del todo (v11.38/46/48/50); marcado como resuelto. Sin cambios de modelo.

## [v11.50 — 2026-05-21] — Fase 2: sincronización de cabecera del `CLAUDE.md`

Dos ajustes de frescura en `fases/2-reciclaje/CLAUDE.md` señalados por el revisor tras v11.49. (1) El banner "Estado actual" seguía fechado en 2026-05-15 / v10.120 aunque el contenido se había ido actualizando — reescrito a 2026-05-21 / v11.49, reflejando que Nivel 1 y Nivel 2 del rediseño están cerrados y Nivel 3/4 pendientes, sin el detalle obsoleto del bloqueo v10.114. (2) La tabla de `nivel_analisis` presentaba `mapa`/`auto`/`detalle` como "tres niveles que se generan por separado" con los scripts viejos como generador — reformulada al modelo recursivo (grado de población de un mismo hilo, §4.2) y atribuida al pipeline de fase 2 (Capa 1/Capa 2, Nivel 3 pendiente). Sin cambios de modelo; solo coherencia documental.

## [v11.49 — 2026-05-21] — Fase 2 Nivel 2 COMPLETO: prompt envoltorio

Cerrada la última pieza del Nivel 2: nuevo `fases/2-reciclaje/prompt.md`, entry point operativo de fase 2 por unidad — espeja `prompt.md` de fase 1. Cubre: gate de arranque (declarar lectura de los 3 contratos), input/output, flujo Capa 1 (esqueleto determinista) / Capa 2 (sesión IA: 3 momentos de análisis, etiquetas, triage, propuestas), criterio de cierre (§13), y "lo que no se hace". Es un esqueleto-contrato: el detalle del pipeline (scripts de Capa 1, validadores) es Nivel 3, y el prompt lo deja explícito sin fingir que existen. Sincronizado el `CLAUDE.md` de fase 2 ("Cómo se invoca" distingue modelo nuevo/viejo). **Con esto el Nivel 2 (contrato operativo) queda COMPLETO**: fase 2 tiene contrato corto + schema + reglas + prompt, al estándar de fase 1. Siguiente: Nivel 3 (implementación de Capa 1/Capa 2 y validadores).

## [v11.48 — 2026-05-21] — Fase 2 Nivel 2: validación y criterio de cierre

Cerrada la pieza "comandos de validación + criterio de cierre" del Nivel 2. Nueva §13 en `reglas-reciclaje.md`: la validación del reciclaje de una unidad tiene tres partes — (a) chequeo estructural contra `schema-reciclaje.md` (0 errores), (b) validador cross-unidad R1-R5 (sin alertas sin resolver), (c) revisión editorial del autor. El criterio de cierre por unidad exige las 5 condiciones (generado + estructural + R1-R5 + `propuestas[]` resueltas/diferidas + revisión del autor). Los validadores como script son Nivel 3 (pendientes); §13 fija qué deben comprobar. Sincronizado el `CLAUDE.md` de fase 2: corregida la línea desfasada que daba P1 como pendiente (ya ratificada en §12), y la sección "Cómo validar" pasa a apuntar a §13 en vez de a los comandos del modelo viejo. En el Nivel 2 solo queda el prompt envoltorio.

## [v11.47 — 2026-05-21] — Fase 2 Nivel 2: P1 ratificada — contrato de regeneración

Ratificada y formalizada la decisión P1 (almacenamiento de datos enriquecidos), último residuo del Nivel 1. Nueva §12 en `reglas-reciclaje.md` con el contrato de ciclo de vida de `nc1-reciclaje.json`: (1) archivo único canónico `unidades/nc1-reciclaje.json`; (2) los hilos/eventos de nivel mapa/auto no se editan a mano — se regeneran desde los inputs fuente vía el pipeline (excepción: `propuestas[]` y cierres humanos sí se escriben); (3) disparadores — incremental al integrar cada unidad, revisión cross-unidad ampliada tras 3 unidades, regeneración íntegra solo al cierre de bloque; (4) Capa 1 determinista reproducible vs Capa 2 IA con cierre humano persistido en `propuestas[]`; (5) "reciclaje cerrado por unidad" = generado + pasa el criterio de cierre vigente + `propuestas[]` resueltas/diferidas; mientras fase 2 siga PAUSADA, ninguna unidad tiene reciclaje cerrado. Registrada la ratificación en `REDISEÑO-EN-CURSO.md` — el Nivel 1 queda sin residuos.

## [v11.46 — 2026-05-21] — Fase 2 Nivel 2: `reglas-reciclaje.md` reescrito al modelo nuevo

`reglas-reciclaje.md` reescrito íntegro. El archivo arrastraba el modelo viejo (clave `campo_semantico`, `accion` única, `impacto`, lógica de los 2 scripts mapa/auto, comunicación/estrategia como hilos). Reescrito como **autoridad decisional estable de fase 2** destilando el modelo cerrado `REDISEÑO-EN-CURSO.md` §1-§10: §1 granularidad por bloque, §2 naming canónico, §3 etiquetas (lista coexistente, las 7), §4 triage `procedencia_indice`, §5 anticipación híbrida, §6 formas verbales, §7 explicación, §8 siempre-presentes, §9 marcas internas, §10 sufijo `@R`, §11 cuándo escalar como propuesta. Fuera: lógica de scripts (es Nivel 3) y narrativa de transición. Complementa a `schema-reciclaje.md` (shape) con precedencia `schema > reglas`. Sincronizado el `CLAUDE.md` de fase 2: tabla "Para qué consultar" apunta a las nuevas secciones, regla crítica de "acciones" pasa a "etiquetas". Arquitectura documental de fase 2 ahora espeja la de fase 1 (contrato corto + schema + reglas); `REDISEÑO-EN-CURSO.md` queda como documento de diseño, a archivar cuando el rediseño cierre.

## [v11.45 — 2026-05-21] — Fase 2 Nivel 2: schema de `nc1-reciclaje.json`

Arranca el Nivel 2 (contrato operativo) del rediseño de fase 2. Nuevo documento de contrato `fases/2-reciclaje/schema-reciclaje.md` — espeja el rol de `schema-inventario.md` en fase 1, con la misma usabilidad (contrato que un agente puede seguir). Define el shape canónico de `nc1-reciclaje.json`: top-level `_meta` + `hilos[]` (lista plana) + `propuestas[]`; el hilo con `id` slug estable (clave primaria independiente del `titulo`, apta para BD), `bloque`, `titulo`, `_grupo`, `nivel_analisis`, `eventos`, `detalle`; el evento con `etiquetas`, `procedencia_indice`, `formas`, `explicacion`, `evidencias`; el objeto `explicacion` y la propuesta. Shape funcional tanto como archivo JSON (hoy) como en base de datos (futuro) — lista plana = un registro por hilo. Resuelve de paso la pieza "persistencia de decisiones IA" del Nivel 2: bloque `propuestas[]` con `estado` (pendiente/aceptada/rechazada). El `detalle` queda con contrato mínimo (nodos/enlaces); su shape fino se difiere al diseño del modal del dashboard. Referenciado desde `REDISEÑO-EN-CURSO.md` §5 Nivel 2 y la navegación del `CLAUDE.md` de fase 2.

## [v11.44 — 2026-05-21] — REDISEÑO fase 2 §10: componentes "siempre presentes" — Nivel 1 completo

Procesada la última pieza conceptual del Nivel 1: los componentes "siempre presentes no indexados" (conjunciones `y/e`, `o/u`; adverbios `sí/no/también/tampoco`). Movidos del Reservorio §R.2 a sección propia §10 y reconciliados con el modelo §1-§9: un "siempre presente" es un patrón cross-unidad del triage §9 — un contenido que el triage marca `nuevo` sistemáticamente curso a curso. §10 define: detección por la Capa 2 IA en los hitos cross-unidad; tres salidas de propuesta al autor (canonizar en registry de fase 1 / modelar como bloque analítico / ignorar); criterio de ampliación de la lista (presencia sistemática + no declarado + función pragmática). Con esto el **Nivel 1 del roadmap queda completo** — residuo único: ratificación formal de P1, que se hará en el Nivel 2. Actualizados §5, apéndice §N, Reservorio §R (queda solo §R.1) y el puntero de `gramatica-canonica.json._meta`.

## [v11.43 — 2026-05-21] — REDISEÑO fase 2: §9 generalizado + D1 absorbida

Cierre de la pieza D1 (tabla de equivalencias) en `REDISEÑO-EN-CURSO.md`. (1) El triage §9 se **generaliza a los 5 bloques** — la lógica declarado/reconciliable/nuevo no era específica de gramática, vale para vocabulario, gramática, pron/orto, verbal y perífrasis. (2) Nueva §9.5: `procedencia_indice` (triage) y `etiquetas` (§2.3) son **dos ejes ortogonales** del evento — el triage añade un eje, no sustituye las etiquetas; un evento lleva los dos. (3) Nueva §9.6: **D1 queda absorbida por el triage** — el archivo curado `nc1-equivalencias-hilos.json` del rediseño viejo es obsoleto; la reconciliación índice↔canónico es la salida `reconciliado` del triage, resuelta evento a evento como propuesta IA con cierre humano. Actualizados §5 Nivel 1 (D1 retirada) y apéndice §N. Con esto el Nivel 1 del roadmap queda completo salvo §R.2 (siempre-presentes).

## [v11.42 — 2026-05-21] — REDISEÑO fase 2 §9: triage índice

Cerrada la pieza "triage declarado/reconciliable/contenido nuevo" en `REDISEÑO-EN-CURSO.md` (nueva §9). Para gramática y pron/orto: cada aparición de una categoría se clasifica respecto al índice del curso en tres salidas — `declarado`, `reconciliado` o `nuevo`. El declarado literal lo precomputa la Capa 1 (coincidencia mecánica); reconciliable y nuevo los analiza la Capa 2 IA como propuestas con cierre humano (una categoría nueva genera propuesta al autor: canonizar en registry de fase 1 o dejar como hallazgo, tipo §R.2). El estatus se marca por evento (categoría-unidad), registrado en el campo `procedencia_indice`. Además: anclada en §5 Nivel 2 la nota de §8.4 (serialización de `que_dice_el_libro`). Actualizado §5 Nivel 1.

## [v11.41 — 2026-05-21] — REDISEÑO fase 2 §8: carril de explicaciones

Cerrada la pieza "carril propio para las explicaciones gramaticales" en `REDISEÑO-EN-CURSO.md` (nueva §8). La explicación que el libro da de un contenido (el cuadro "cómo se forma X") es un **atributo del evento** — campo `explicacion` — no un hilo propio (un hilo aparte duplicaría el recorrido de la categoría). El campo tiene dos partes: `que_dice_el_libro` (lo que el cuadro expone literalmente) y `analisis_ia` (el trabajo de fase 2: relaciones lógicas, prerrequisitos, incoherencias — fase 2 no copia la fuente, la analiza). Alcance a los 5 bloques, no solo gramática. Es insumo del nivel `detalle` (§4.4), sin solaparse: el `analisis_ia` es local al evento, el `detalle` razona la cadena cross-unidad completa. Además, anclada en §5 Nivel 3 la nota de que el desglose de `formas` por unidad exige leer `actividad.tiempos_y_verbos` al diseñar Capa 1. Actualizado §5 Nivel 1.

## [v11.40 — 2026-05-21] — REDISEÑO fase 2 §7: tratamiento detallado de formas verbales

Cerrada la pieza "tratamiento detallado de formas verbales" en `REDISEÑO-EN-CURSO.md` (nueva §7). (1) El evento verbal (lema-tiempo-unidad) lleva un campo `formas` con las formas conjugadas concretas que esa unidad trabaja — opción A: la forma es dato del evento, no sub-entidad con recorrido propio. La progresión del paradigma se lee comparando los `formas` de eventos sucesivos. (2) `rasgo_por_tiempo` (regular/irregular del lema) se mantiene en el hilo verbal; frontera trazada con el grupo gramatical "Tiempos y modos verbales" (§6.4): atributo del verbo concreto vs flexión abstracta como contenido enseñado. (3) Anticipación de formas en modelo híbrido — fase 2 lee el registro transitorio de fase 1 (`_migracion_rediseno`) y completa el análisis por su cuenta; cierra la costura §6.5 punto 1, incluida la perífrasis anticipatoria (ya no depende de `estructura_perifrastica`). Actualizados §3.2, §5 Nivel 1 y §6.5. Población del desglose por unidad: tarea diferida a la Capa 1.

## [v11.39 — 2026-05-20] — Glosario transversal del proyecto

Nuevo `glosario.md` en la raíz: índice semántico transversal del proyecto (opción B de la decisión documental). El único glosario existente, `fases/1-extraccion-inventario/glosario.md`, no es un glosario general sino la referencia campo por campo del schema del inventario — se mantiene intacto en su sitio. El nuevo glosario global es corto y de orientación: Bloque 1 — 12 términos globales (repo A/B, inventario, registry canónico, PCIC, unidad/unidad atípica, fase, dashboard, modelo IA-first, dry-run, publicación canónica, mirror snapshot, source of truth); Bloque 2 — 10 términos de fase 2 marcados "en estabilización" (hilo, evento, etiqueta, mapa, auto, detalle, Capa 1, Capa 2, reciclaje, anticipación); Bloque 3 — tabla de glosarios de fase con enlaces. Cada entrada: definición breve + "ver detalle en fase X" cuando aplica. Añadida fila en "Documentos clave" del `CLAUDE.md` raíz como documento de Consulta. Los glosarios de fase (fase 2 y siguientes) se crearán cuando su terminología se estabilice.

## [v11.38 — 2026-05-20] — Fase 2: sincronización post-D2

Cierra las tres costuras señaladas por el revisor tras v11.37. (1) `REDISEÑO-EN-CURSO.md` §6.1 precisa la fórmula del universo de hilos: no "los registries de fase 1" sin más, sino los **4 registries de fase 1 + `perifrasis-canonicas.json`** (5.º, derivado, propio de fase 2). (2) Nueva §6.5 que anota explícitamente las dos sincronizaciones que D2 arrastra: la fuente real para detectar perífrasis anticipatorias (fase 1 excluye de `tiempos_y_verbos` los auxiliares anticipatorios, así que `estructura_perifrastica` puede no transportarlas — se resolverá en el paso "formas verbales") y el contrato corto de fase 2 desactualizado. (3) `fases/2-reciclaje/CLAUDE.md` sincronizado: el nivel `auto` ya no se describe solo desde `vocabulario_consolidado` sino desde los 5 bloques; la regla "un hilo por campo semántico" se generaliza a granularidad por bloque (§2.2). Sin cambios operativos — fase 2 sigue PAUSADA.

## [v11.37 — 2026-05-20] — REDISEÑO fase 2 §6: D2 — universo de hilos y sub-organización de gramática

Cerrada la pieza D2 en `REDISEÑO-EN-CURSO.md` (nueva §6). (1) Universo de hilos válidos = los registries canónicos de fase 1; la lista PCIC curada del viejo queda obsoleta. Cerrado para escritura (fase 2 no inventa canónicos), abierto para detección (estructuras no declaradas → hallazgo escalado). (2) Perífrasis gana registry propio `perifrasis-canonicas.json` (5.º registry); la tabla de bloques de §2.2 pasa de 4 a 5 — cierra la incoherencia §2.2↔§3.3. (3) El bloque gramática se sub-organiza con un campo `_grupo` por subsistema gramatical (7 grupos: Determinantes, Pronombres, Sintagma nominal y concordancia, Construcciones, Tiempos y modos verbales, Adverbios y marcadores, Preposiciones). (4) El grupo "Tiempos y modos verbales" integra flexión/paradigmas (regular, irregularidad vocálica, imperativo) + usos de tiempos/modos, canonizados desde PCIC A1 — plano distinto del bloque `verbal` (lista de cada verbo del libro). Población de `perifrasis-canonicas.json` y de las categorías nuevas de `gramatica-canonica.json`: tareas diferidas. Actualizados §2.2, §5 Nivel 1 y apéndice §N.

## [v11.36 — 2026-05-20] — `CLAUDE.md` raíz: árbol del repositorio a mapa de alto nivel

El árbol de "Estructura del repositorio" mezclaba orientación estable (dónde vive cada cosa) con detalle de drift: enumeración exhaustiva de los archivos de `propuesta/`, sello de versión `v10.127` y nota de UI ("7.ª columna del dashboard"). Adelgazado el sub-árbol de `unidades/UX/` a sus 4 subcarpetas canónicas con propósito general. El árbol sigue en CLAUDE.md — es arquitectura/orientación legítima — pero ahora responde solo a "¿dónde vive cada cosa?", no a "¿qué contiene exactamente hoy?". El detalle fino vive en los `CLAUDE.md` de fase o se descubre al vuelo.

## [v11.35 — 2026-05-20] — Adelgazado de `CLAUDE.md` raíz: estado fuera de la autoridad operativa

El `CLAUDE.md` raíz contenía el bloque `## Estado fase 1` (~55 líneas: registries con versiones, convenciones de corrección, comandos, deudas residuales, procedimiento), contradiciendo su propia regla "no añadir aquí historia, estado, planes". Reparto en 3 destinos: (A) el contrato operativo de fase 1 — registries como autoridad de naming (sin columna de versión), convenciones críticas de corrección (sin precedentes con versión), comandos canónicos y procedimiento de corrección — se traslada a `fases/1-extraccion-inventario/CLAUDE.md` (su sitio natural, auto-cargado al trabajar en fase 1); (B) el estado vivo — cierre de fase y deudas — ya vivía en `REVIEW.md`; se compacta la deuda matcher (cerrada en v11.3-v11.5) dejando solo las deudas abiertas; (C) el bloque se elimina del raíz. Resultado: `CLAUDE.md` raíz baja de 209 a 153 líneas, deja de mezclar capas y respeta la separación de funciones que el propio repo declara (CLAUDE = reglas vigentes · REVIEW = estado · CHANGELOG = cambios · PROCESO-MAESTRO = decisiones). Sin pérdida de contenido operativo.

## [v11.34 — 2026-05-20] — Fase 2: integración a documento único de rediseño

`REDISEÑO-EN-CURSO-viejo.md` archivado en `docs/historico/` (`git mv`). El rediseño de fase 2 pasa a vivir en un **documento único**, `REDISEÑO-EN-CURSO.md`. Análisis pieza por pieza del viejo: de sus 8 secciones, §1/§5/§6 son obsoletas, §2/§3-D3/§4-P1 ya estaban migradas, §3-D1 y §3-D2 siguen vivas pero su formulación vieja está superada (D2: la lista PCIC curada queda superada por los 4 registries de fase 1; la pieza sigue pendiente de redefinir), y §7 (R1-R5) + §8 (siempre-presentes) son material vivo sin procesar. Cambios: (1) nuevo apéndice §R "Reservorio" en el activo con §7 y §8 copiados verbatim + prefacio de procedencia/estado; (2) apéndice §N reescrito con la disposición final de cada pieza en tres estados (ya migrado / superado en formulación vieja / en reservorio); (3) §5 Nivel 1/3 actualizado — D2 reformulado, §8 y R1-R5 apuntan al Reservorio, retirada la fila obsoleta "hallazgos del revisor"; (4) referencias activas al viejo actualizadas en el mismo lote: `PROCESO-MAESTRO.md` (árbol), `gramatica-canonica.json` (`_meta.siempre_presentes_no_indexados`), `fases/2-reciclaje/CLAUDE.md` (banner de estado) y header de `REDISEÑO-EN-CURSO.md`. Sin referencias colgantes.

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

