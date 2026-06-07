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
│   ├── UX-nc1-inventario.json     (extracción de fase 1)
│   ├── fuente/                    (PDF del libro, gitignored)
│   ├── propuesta/                 (material editorial elaborado por sección)
│   ├── final/                     (versión limpia para InDesign + ajustes finales)
│   └── recursos/                  (CSVs de tarjetas, audios, imágenes…)
├── fases/<N>-<nombre>/            ← una carpeta por fase con CLAUDE.md + prompt + artefactos
├── scripts/                       ← código Python ejecutable (validación, regeneración)
├── web/, diagrama.py              ← infraestructura (dashboard)
├── docs/historico/                ← histórico archivado (changelog/review/docs superados)
├── PROCESO-MAESTRO.md             ← decisiones cerradas + bitácora
├── REVIEW.md                      ← plan ejecutable con gates (estado actual del proyecto)
├── README.md                      ← descripción del proyecto + estado de las 8 fases
└── CHANGELOG.md, requirements.txt, .env.example, .gitignore
```

---

## Modelo de dos repositorios (A / B)

El proyecto vivió en **dos repositorios separados**:

- **Repo A — este** (`guia-didactica-profesor-IA`): el **entregable publicado + infraestructura + capa editorial activa**. Contiene `unidades/UX/propuesta/` (fuente rica con metanotas, snapshot publicado desde repo B) y `unidades/UX/final/` (versión limpia para InDesign, donde sucede toda la edición editorial actual). Inventarios canónicos, fases, scripts, dashboard, docs raíz.
- **Repo B — externo** (`~/Desktop/temporal-antiguo-guia-ia/`): **congelado editorialmente desde 2026-05-25**. Mantiene el sistema metodológico histórico (hub, pautas, plantillas, referencias, registro), las propuestas originales y el archivo del sistema CrewAI v5. Solo se consulta como referencia; no se edita.

**Desde 2026-05-25 toda edición editorial ocurre en repo A**, capa `unidades/UX/final/`. La capa `propuesta/` queda como fuente rica intacta.

## Flujo de publicación canónica (histórico — repo B congelado desde 2026-05-25)

> Este flujo describe cómo se publicaron las propuestas de U0-U9 desde repo B a repo A entre 2026-05-19 y 2026-05-25. Desde el congelamiento de repo B, ya no se aplica para edición nueva: la edición ocurre directamente en `unidades/UX/final/` de repo A. Se conserva para entender el origen de los snapshots en `propuesta/`.

La redacción de cada unidad sucede en **repo B** (`~/Desktop/temporal-antiguo-guia-ia/unidades/UXX-propuesta/`). Cuando la unidad entera está cerrada y validada, las propuestas se publican (copian) a la **ruta canónica versionada de repo A** `unidades/UX/propuesta/` con renaming sin prefijo:

```
[repo B] unidades/U02-propuesta/U02-propuesta-vocabulario.md
                                          → [repo A] unidades/U2/propuesta/vocabulario.md

[repo B] unidades/U02-propuesta/tarjetas/<archivo>.csv
                                          → [repo A] unidades/U2/recursos/tarjetas/<archivo>.csv
```

- La canónica `unidades/UX/` de repo A es **mirror snapshot publicado**, no fuente.
- **Ediciones futuras siempre en repo B**; la canónica de repo A se actualiza re-publicando.
- Para unidades atípicas (U0, sin secciones canónicas): un archivo único en `unidades/U0/propuesta/<nombre-descriptivo>.md`.

Razón: repo B mantiene a mano todo el sistema de trabajo mientras se redacta (pautas, plantillas, registro, propuestas previas como referencia). La canónica de repo A es el entregable versionado que GitHub incluye y que cualquier máquina o colaborador puede consultar.

> **Nota histórica:** las propuestas ya publicadas en `unidades/U*/propuesta/*.md` pueden contener referencias a rutas `viejo/...` — son snapshot histórico de cuando el sistema de trabajo vivía en `viejo/` dentro de repo A; no se reescriben retroactivamente.

---

## Reglas de oro (no negociables, globales)

Aplican a **cualquier** trabajo en el repositorio. Reglas específicas de cada fase viven en `fases/<N>-<nombre>/CLAUDE.md`.

1. **No transformar sin razón.** Si una decisión editorial no requiere cambio, no se cambia. Cualquier transformación se documenta.
2. **Validar antes de cerrar.** Cada artefacto producido pasa por validación (script, revisión visual o ambas) antes de declararse cerrado.
3. **No inventar.** Si una palabra, fecha o dato no está en la fuente original, no se añade. Marcar como "verificación pendiente" y consultar al autor.
4. **Una fuente única.** Cada criterio editorial vive en un único archivo. La duplicación lleva a desincronización.
5. **Edición editorial en repo A, capa `final/`.** Desde 2026-05-25 toda edición editorial ocurre en `unidades/UX/final/` de este repo. La capa `propuesta/` se conserva intacta como fuente rica. Repo B queda congelado.

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

# Integrar el inventario de una unidad a main (copia + valida + commit del inventario)
# El reciclaje no lo toca: lo gestiona el pipeline de fase 2 (generar_reciclaje_capa1.py + Capa 2).
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

- No editar la capa `propuesta/` — es fuente rica intacta. La edición editorial ocurre en `unidades/UX/final/`.
- No editar en repo B — congelado editorialmente desde 2026-05-25.
- No ejecutar el sistema CrewAI antiguo (archivado en repo B, no conectado al sistema actual).
- No saltarse la validación antes de cerrar un artefacto.
- No inventar contenido editorial.
- No duplicar instrucciones operativas en este CLAUDE.md raíz si ya viven en el CLAUDE.md de una fase.
- No añadir aquí: historia, estado, planes futuros, meta-decisiones. Eso vive en PROCESO-MAESTRO, REVIEW, README según corresponda.

---

## Documentos clave (índice de navegación)

| Archivo | Para qué | ¿Autoridad? |
|---|---|---|
| `CLAUDE.md` (raíz + de fase) | Cómo actuar **hoy** — reglas vigentes | ✅ **MANDA** |
| `fases/1-extraccion-inventario/{schema,reglas,convenciones}.md` | Contratos de fase 1 | ✅ Manda (en fase 1) |
| `docs/manual-estilo-final.md` | Manual de estilo de la capa `final/` — autoridad de estilo, tipografía, terminología, metadiscurso | ✅ Manda (en `unidades/**/final/*.md`, activado vía `.claude/rules/final-style.md`) |
| `docs/formulacion-objetivos.md` | Criterios de formulación de objetivos generales y específicos (Bloom, verbos, naturaleza por sección) | ✅ Manda (objetivos en `final/`) |
| `docs/contratos-recursos-editoriales.md` | Spec textual interna de recursos editoriales propios del proyecto: tarjetas de estrategia (principio operativo, antipatrones, modelo de referencia, criterio de nombre) y píldoras formativas (principio operativo, antipatrones, criterio de aceptación). Frontera con `manual-estilo-final.md`: el manual regula cómo se nombran y dónde aparecen las menciones en `final/`; este documento regula qué dicen los recursos por dentro. | ✅ Manda (spec interna de tarjeta/píldora) |
| `README.md` | Descripción del proyecto, estado de las 8 fases, cómo se trabaja | Apunta |
| `PROCESO-MAESTRO.md` | Modelo conceptual, decisiones cerradas, esquemas, bitácora | Consulta |
| `REVIEW.md` | Plan ejecutable con gates, estado vivo, próximos pasos | Estado, no manda reglas |
| `CHANGELOG.md` | Registro cronológico de commits | Consulta, no manda |
| `docs/historico/` | Histórico archivado (changelog/review/docs superados) | Consulta puntual |
| `fases/<N>-<nombre>/prompt.md` | Instrucciones detalladas de cada fase | Apunta |
| `glosario.md` | Índice semántico transversal del proyecto; punto de entrada a la terminología global y a los glosarios de fase | Consulta |

**Si CHANGELOG/REVIEW contradicen a CLAUDE.md → manda CLAUDE.md.** Una sesión futura solo necesita leer CLAUDE.md para operar; no debe re-analizar logs antiguos.

### Regla editorial de CHANGELOG / REVIEW

- Entradas nuevas **cortas y operativas** (2-4 líneas: qué cambió + por qué + archivos). No reescribir entradas antiguas.
- La bitácora de REVIEW se centra en **estado y decisiones vivas**; cuando una entrada deja de ser operativa, se compacta y se referencia `docs/historico/` en lugar de replicar el detalle.
- El histórico ya resuelto vive en `docs/historico/` — no se replica en los archivos activos.
