# CLAUDE.md — Guía Didáctica del Profesor IA

> Auto-cargado por Claude Code en cada sesión. Define las reglas y convenciones que toda interacción con este repositorio debe respetar.
>
> Reglas operativas detalladas por fase: `fases/<N>-<nombre>/CLAUDE.md` (auto-cargado al trabajar en esa carpeta).

---

## Qué es este proyecto

Sistema editorial asistido por IA para producir la **guía didáctica del profesor** del libro "Nuevo Compañeros 1" (NC1, ELE A1.1, SGEL). El contenido editorial se genera siguiendo un proceso de 8 fases, partiendo del PDF del libro original.

---

## Estructura del repositorio

```
guia-didactica-profesor-IA/
├── unidades/UX/                   ← contenido editorial por unidad
│   ├── UX-nc1-inventario.json     (extracción fase 1, top-level)
│   ├── fuente/UX-nc1.pdf          (PDF embedido, gitignored)
│   ├── propuesta/                 (material editorial elaborado: vocabulario.md,
│   │                               gramatica.md, comunicacion.md, destrezas.md,
│   │                               cultura.md, evaluacion.md — capa editorial v10.127.
│   │                               Opcional: itinerarios.md (planificación cross-unidad,
│   │                               mostrada como 7.ª columna en el dashboard))
│   └── recursos/                  (CSVs de tarjetas, audios, imágenes, etc.)
├── fases/<N>-<nombre>/            ← una carpeta por fase con CLAUDE.md + prompt + artefactos
├── scripts/                       ← código Python ejecutable (validación, regeneración)
├── web/, diagrama.py, eval/       ← infraestructura (dashboard, evaluación)
├── viejo/                         ← archivo del sistema CrewAI v5 anterior + zona de trabajo
│                                    activa del rediseño (pautas, plantillas, registro,
│                                    propuestas en redacción). Ver flujo de publicación abajo.
├── PROCESO-MAESTRO.md             ← decisiones cerradas + bitácora
├── REVIEW.md                      ← plan ejecutable con gates (estado actual del proyecto)
├── README.md                      ← descripción del proyecto + estado de las 8 fases
└── CHANGELOG.md, ROADMAP.md, GITHUB-MANIFEST.md, Dockerfile, etc.
```

---

## Flujo de publicación canónica (al cerrar una unidad)

La redacción de cada unidad sucede en **`viejo/unidades/UXX-propuesta/`** (zona de trabajo, gitignored). Cuando la unidad entera está cerrada y validada, las propuestas se copian a la **ruta canónica versionada** `unidades/UX/propuesta/` con renaming sin prefijo:

```
viejo/unidades/U02-propuesta/U02-propuesta-vocabulario.md
                                                            → unidades/U2/propuesta/vocabulario.md

viejo/unidades/U02-propuesta/tarjetas/<archivo>.csv
                                                            → unidades/U2/recursos/tarjetas/<archivo>.csv
```

- La canónica `unidades/UX/` es **mirror snapshot**, no fuente.
- **Ediciones futuras siempre en `viejo/`**; canonical se actualiza re-copiando.
- Para unidades atípicas (U0, sin secciones canónicas): un archivo único en `unidades/U0/propuesta/<nombre-descriptivo>.md`.

Razón: `viejo/` mantiene todo a mano para Claude Code mientras se redacta (pautas, plantillas, registro, propuestas previas como referencia). La canónica es el entregable versionado que el repo git incluye y que cualquier máquina o colaborador puede consultar.

Detalle del paso 13 del proceso operativo en `viejo/unidades/CLAUDE.md`.

---

## Reglas de oro (no negociables, globales)

Aplican a **cualquier** trabajo en el repositorio. Reglas específicas de cada fase viven en `fases/<N>-<nombre>/CLAUDE.md`.

1. **No transformar sin razón.** Si una decisión editorial no requiere cambio, no se cambia. Cualquier transformación se documenta.
2. **Validar antes de cerrar.** Cada artefacto producido pasa por validación (script, revisión visual o ambas) antes de declararse cerrado.
3. **No inventar.** Si una palabra, fecha o dato no está en la fuente original, no se añade. Marcar como "verificación pendiente" y consultar al autor.
4. **Una fuente única.** Cada criterio editorial vive en un único archivo. La duplicación lleva a desincronización.
5. **No tocar `viejo/`.** Contiene el sistema anterior, intocable hasta su eliminación final autorizada por el autor.

---

## Convenciones de naming

- Carpetas de unidad: `U0/`, `U1/`, `U2/`...`U9/` (sin cero a la izquierda; válido para cursos ≤9 unidades, con U0 reservado a la unidad introductoria atípica "Punto de partida").
- Archivos por unidad: prefijo `UX-nc1-`. Ejemplo: `U3-nc1-inventario.json`.
- Archivos globales del curso: prefijo `nc1-`. Ejemplo: `nc1-tarjetas.json`.
- Curso: `nc1` = "Nuevo Compañeros 1".

---

## Comandos básicos

```bash
# Arrancar dashboard
python3 diagrama.py
# → http://localhost:8081

# Validar inventario de una unidad
python3 scripts/validar_inventario.py 3

# Integrar una unidad desde su worktree a main (copia + valida + commit del inventario)
# Por defecto NO regenera reciclaje (fase 2 pausada). Flag --regenerar-reciclaje para forzar.
python3 scripts/integrar_unidad.py 6
```

---

## Cómo invocar una fase

Claude Code carga automáticamente todos los `CLAUDE.md` desde el directorio de trabajo hacia arriba. Si trabajas dentro de `fases/N-<nombre>/`, el CLAUDE.md de esa fase se carga junto al raíz, sin hacer nada.

Si invocas una fase desde fuera (ej. desde la raíz), tienes que referenciarla explícitamente:

> Trabaja en fase X siguiendo `fases/N-<nombre>/CLAUDE.md` y `fases/N-<nombre>/prompt.md`.

Ejemplo concreto (fase 1, extracción de U4):

> Extrae el inventario de U4 siguiendo `fases/1-extraccion-inventario/CLAUDE.md` y `fases/1-extraccion-inventario/prompt.md`.

---

## Lo que NO se hace

- No modificar nada en `viejo/`.
- No ejecutar el sistema CrewAI antiguo (no está conectado al sistema actual).
- No saltarse la validación antes de cerrar un artefacto.
- No inventar contenido editorial.
- No duplicar instrucciones operativas en este CLAUDE.md raíz si ya viven en el CLAUDE.md de una fase.
- No añadir aquí: historia, estado, planes futuros, meta-decisiones. Eso vive en PROCESO-MAESTRO, REVIEW, README según corresponda.

---

## Estado fase 1 (extracción de inventario) — cerrada en v10.164

✅ **U0-U9 saneadas** con contrato canónico post-v10.153 + §5.10 + §5.11. Validador 0/0/0 en las 10 unidades.

### Registries vigentes (autoridad de naming, regla crítica §5.6)

| Dimensión | Archivo | Versión |
|---|---|---|
| Léxico | `fases/1-extraccion-inventario/campos-semanticos-canonicos.json` | v1.8 |
| Gramatical | `fases/1-extraccion-inventario/gramatica-canonica.json` | v1.5 |
| Pron/orto | `fases/1-extraccion-inventario/pronunciacion-ortografia-canonica.json` | v1.1 |
| Verbal | `fases/1-extraccion-inventario/verbos-canonicos.json` | v1.6 |

Soporte PCIC A1: `pcic-a1-{vocabulario,gramatica,pronunciacion-ortografia,comunicacion}.json`.

### Convenciones críticas para futuras correcciones

1. **Naming literal del registry** (regla §5.6). No inventar canónicos. Si falta uno, **escalar §0.1 al autor** en chat.
2. **Notación barra masc/fem** (`lema/-a`) cuando ambas flexiones aparecen materialmente. Matcher `_expand_needle` despliega masc + fem + plural por substring. Precedentes: `moderno/-a` U6 v10.158, `colombiano/-a` U4 v10.159, lotes U5/U6/U8/U9.
3. **Colores como categoría independiente** (recurrente desde U1), no mezclar con `Adjetivos descriptivos`.
4. **Fuentes verificadas literalmente**: cada `fuente` declarada en un item debe contener el item literal en el texto de la actividad (campos `INPUT_FIELDS_LIST`: instruccion_original, datos, dialogo, texto, texto_completo, items_libro, muestra_de_lengua, opciones, audio + respuestas). Si no, validador falla §5.10A.
5. **Bug sistémico conocido**: el extractor original perdía items en actividades-relaciona (`columnas_relaciona`, `items_libro` con flexiones). Verificar siempre actividades fundacionales del campo, no solo `palabras_recuadro` de actividades posteriores.

### Comandos canónicos

```bash
python3 scripts/validar_inventario.py N           # validar unidad N (0-9)
python3 scripts/cleanup_v150.py --unit N --apply  # sanear §5.10/§5.11 antes de validar
python3 diagrama.py                                # dashboard local (http://localhost:8081)
# Slash command: /check-fase1 — valida las 10 unidades en bucle
```

### Deudas residuales catalogadas

**Deuda matcher: CERRADA en v11.3-v11.5** (2026-05-19).

- ✅ Bug 1 acentos (`_norm_text` aplica `_strip_accents`, v11.3) — `marrón` atrapa `marrones`. Workaround U8 revertido.
- ✅ Bug 2 imágenes (`imagen` en `INPUT_FIELDS_LIST`, v11.4) — `morado/-a` recuperado en U9.
- ✅ Bug 3 claves de dict (`_gather_text` recoge claves, v11.5) — futuros inventarios no necesitan reestructurar dicts. Workaround U6 agenda se mantiene por compatibilidad estructural con otros consumidores.

**Deudas todavía abiertas (no bloquean validador):**

- **Canónicos huérfanos** (sin alta en registry): `Abreviaturas de los diccionarios` (U8), `vegetariano` (U4). Escalados §0.1.
- **Auditoría retroactiva U0-U5** parcialmente cubierta por rectificaciones manuales v10.162-v10.164; queda como ejercicio sistemático abierto.

### Cómo aplicar una corrección sin romper la estructura

1. Editar el JSON de la unidad afectada.
2. `python3 scripts/validar_inventario.py N` → debe dar 0/0/0.
3. Si falla §5.10A: revisar fuentes / aplicar barra `/-a` / mover canónico.
4. Documentar la decisión en `_decisiones_ia` del propio JSON.
5. Bumpear versión en `CHANGELOG.md` + bitácora en `REVIEW.md`.
6. Si toca registry: bumpear versión del registry + actualizar `_apariciones`.

---

## Documentos clave (índice de navegación)

| Archivo | Para qué |
|---|---|
| `README.md` | Descripción del proyecto, estado de las 8 fases, cómo se trabaja |
| `PROCESO-MAESTRO.md` | Modelo conceptual completo, decisiones cerradas, esquemas, bitácora |
| `REVIEW.md` | Plan ejecutable con gates, estado vivo, próximos pasos |
| `CHANGELOG.md` | Historial técnico de commits |
| `fases/<N>-<nombre>/CLAUDE.md` | Contexto operativo de cada fase (auto-cargado al trabajar ahí) |
| `fases/<N>-<nombre>/prompt.md` | Instrucciones detalladas de cada fase |
