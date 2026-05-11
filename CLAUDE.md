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
├── fases/<N>-<nombre>/            ← una carpeta por fase con CLAUDE.md + prompt + artefactos
├── scripts/                       ← código Python ejecutable (validación, regeneración)
├── web/, diagrama.py, eval/       ← infraestructura (dashboard, evaluación)
├── viejo/                         ← archivo del sistema CrewAI v5 anterior — INTOCABLE
├── PROCESO-MAESTRO.md             ← decisiones cerradas + bitácora
├── REVIEW.md                      ← plan ejecutable con gates (estado actual del proyecto)
├── README.md                      ← descripción del proyecto + estado de las 8 fases
└── CHANGELOG.md, ROADMAP.md, GITHUB-MANIFEST.md, Dockerfile, etc.
```

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
# → http://localhost:8080

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

## Documentos clave (índice de navegación)

| Archivo | Para qué |
|---|---|
| `README.md` | Descripción del proyecto, estado de las 8 fases, cómo se trabaja |
| `PROCESO-MAESTRO.md` | Modelo conceptual completo, decisiones cerradas, esquemas, bitácora |
| `REVIEW.md` | Plan ejecutable con gates, estado vivo, próximos pasos |
| `CHANGELOG.md` | Historial técnico de commits |
| `fases/<N>-<nombre>/CLAUDE.md` | Contexto operativo de cada fase (auto-cargado al trabajar ahí) |
| `fases/<N>-<nombre>/prompt.md` | Instrucciones detalladas de cada fase |
