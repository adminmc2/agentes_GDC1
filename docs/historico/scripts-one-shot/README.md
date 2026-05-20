# Scripts one-shot archivados

Scripts que cumplieron una función única (migración, inicialización) y ya no se ejecutan en el flujo normal. Se conservan como registro histórico — no como herramientas vigentes.

| Script | Qué hizo | Cuándo |
|---|---|---|
| `inicializar_canon_semantico.py` | Pobló por primera vez `campos-semanticos-canonicos.json` desde `nc1-curso.json` + subset PCIC A1. | v10.x (canon ya poblado y mantenido a mano desde entonces) |

> No confundir con `scripts/migrate_at_r_v10145.py`: ese tiene nombre de one-shot pero **sigue activo** — es el módulo matcher que importa `scripts/cleanup_v150.py`. No se archiva.
