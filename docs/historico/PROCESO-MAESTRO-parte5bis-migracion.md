# PROCESO-MAESTRO — Parte 5.bis: Histórico de la estrategia de migración (CERRADA)

Archivo de la Parte 5.bis del `PROCESO-MAESTRO.md`, declarada explícitamente como CERRADA en su propio título. Recoge la cronología y el plan de la migración que dio lugar a la estructura actual del repo. Texto íntegro, sin reescribir.

Esta parte se trasladó a histórico en v10.76 porque ya no describe trabajo activo: la migración está cerrada y su estado actual se ve en el árbol vivo de la Parte 3.

---

## Parte 5.bis — Histórico de la estrategia de migración (CERRADA)

**Cronología:**
- **2026-05-05 12:15** — Split ejecutado: contenido editorial movido a `viejo/`; carpeta `nuevo/` creada como zona de construcción.
- **2026-05-05 16:00** — `nuevo/` **disuelta**: su contenido se promocionó a raíz directamente (decisión del autor para evitar futuros renombrados).

### Estado actual del repositorio (post-disolución)
- **`viejo/`** existe en la raíz. Contiene el sistema CrewAI v5 anterior y materiales editoriales originales. Solo local (gitignored). Intocable hasta su eliminación final.
- **El sistema activo vive en raíz**: `unidades/`, `scripts/`, `fases/`, `web/`, `diagrama.py`, `eval/`.
- **Documentos en raíz**: `CLAUDE.md`, `README.md`, `CHANGELOG.md`, `PROCESO-MAESTRO.md`, `REVIEW.md`, `ROADMAP.md`, `GITHUB-MANIFEST.md`.
- **Config en raíz**: `Dockerfile`, `railway.toml`, `requirements.txt`, `.env.example`, `.gitignore`, `.dockerignore`.

### Limpieza final pendiente (cuando todas las fases estén operativas)
Ver bloque E del `REVIEW.md`. En resumen:
1. Migrar de `viejo/` lo aprovechable (criterio caso por caso).
2. Eliminar `viejo/`.
3. Eliminar `PROCESO-MAESTRO.md` y `REVIEW.md` (integrar su contenido en `CLAUDE.md`, `README.md` y CLAUDE.md por fase).

---
