# Zona `nuevo/`

> **Qué es esto:** la versión en construcción de la estructura definitiva del repositorio. Aquí se va materializando lo que decidimos en chat (ver `../PROCESO-MAESTRO.md`).
>
> **Cómo se usa:** todo lo que llega a `nuevo/` se prueba primero con **U3** (la única unidad poblada hoy). Cuando esté validado, `nuevo/` se promueve a la raíz del repo.
>
> **Qué NO está aquí:** el código del dashboard (`web/`) no se duplica — vive en la raíz como hasta ahora. La integración del informe HTML por unidad se añade al dashboard existente como sección nueva.

---

## Estructura prevista (se va poblando)

```
nuevo/
├── unidades/
│   └── U3/                              ← caso piloto
│       ├── U3-nc1-inventario.json       ← (pendiente: copiar y migrar al nuevo schema)
│       ├── fuente/
│       │   └── U3-nc1.pdf               ← (pendiente: copiar)
│       ├── tarjetas/                    ← (pendiente: copiar de unidades/U03/tarjetas/)
│       ├── pildoras/                    ← (pendiente: copiar de unidades/U03/pildoras/)
│       └── secciones/                   ← (pendiente)
└── scripts/
    └── prompts/
        └── extraccion-inventario.md     ← (pendiente: escribir)
```

## Cuándo se completa cada cosa

Conforme se cierran decisiones en chat:

1. **Cerrado** — Esquema del `UX-nc1-inventario.json`. Ver `../PROCESO-MAESTRO.md` Parte 2 / Fase 1.
2. **Cerrado** — Convención de naming (`UX-nc1-`, `nc1-`, carpetas sin cero).
3. **Cerrado** — Estrategia de generación de los 4 JSONs.
4. **Pendiente** — Esquemas de los 3 JSONs globales (`nc1-reciclaje`, `nc1-tarjetas`, `nc1-pildoras`).
5. **Pendiente** — Plantilla HTML del informe por unidad e integración en dashboard.
6. **Pendiente** — Migración del contenido real de U3 a `nuevo/unidades/U3/` con el nuevo schema.
7. **Pendiente** — Escritura del prompt `scripts/prompts/extraccion-inventario.md`.

## Promoción a raíz

Cuando todo lo de `nuevo/` esté validado contra U3:
- Se renombra el actual `unidades/` viejo a `_archivo/unidades/` (o se elimina si ya está vaciado).
- `nuevo/unidades/` pasa a ser `unidades/`.
- Misma operación con cualquier otra carpeta migrada.
- Esta zona `nuevo/` deja de existir y `PROCESO-MAESTRO.md` se elimina al haber integrado todo en CLAUDE.md, README.md y los READMEs por sección.
