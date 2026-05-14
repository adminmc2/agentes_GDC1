# Prompt: procesamiento de inventario de una unidad

> **Cómo se invoca:** `Procesa la unidad UX siguiendo fases/1-extraccion-inventario/prompt.md.`
> **Convención de comandos:** comandos root-relative desde la raíz del repo.

---

## Contrato

- **Input:** `unidades/UX/fuente/UX-nc1.pdf`.
- **Output:** `unidades/UX/UX-nc1-inventario.json` (congelado tras cierre).

**Definición de éxito** (4 gates simultáneos):

1. `python3 scripts/validar_inventario.py X` → 0 errores y 0 avisos (1 aviso aceptable si la unidad es atípica con `_nota_unidad_atipica`).
2. Cero marcas internas no resueltas en el JSON. Política y ciclo de vida → `reglas-operativas.md`.
3. Revisión visual del autor (2-3 páginas al azar contra PDF) → OK explícito.
4. Cualquier caso no contemplado en los contratos vivos ha sido escalado al autor antes del cierre.

> **Nota transitoria.** Mientras `scripts/validar_inventario.py` y `reglas-operativas.md` no estén alineados con `schema-inventario.md`:
> - el gate 1 (validador automático) queda sustituido por validación manual contra el schema y revisión visual;
> - en el paso 3, `reglas-operativas.md` se aplica como guía operativa, pero si una regla concreta entra en conflicto con el schema **prevalece el schema**.
>
> Puntos de divergencia conocidos y condiciones de retirada → Apéndice transitorio del schema (§A.1, §A.3).

> **Deuda transitoria — `convenciones-y-casos.md`.** El archivo vivo de convenciones todavía no ha sido reescrito bajo el modelo IA-first (lote siguiente). Mientras tanto:
> - `convenciones-y-casos.md` puede estar desalineado o ausente; las referencias desde otros docs pueden quedar rotas temporalmente.
> - El contenido histórico vigente vive en `convenciones-y-casos-viejo.md` como reservorio consultable solo para localizar convenciones de transcripción concretas (sílaba tónica, primer ítem resuelto, marcadores de diálogos, sopas de letras, casebook).
> - Si una convención del viejo entra en conflicto con `schema-inventario.md` o `reglas-operativas.md`, **prevalecen schema y reglas vivos**.

---

## Lectura mínima obligatoria

- `schema-inventario.md` — shape del JSON.
- `reglas-operativas.md` — autoridad operativa (reglas, protocolos, marcas, política PCIC).
- `convenciones-y-casos-viejo.md` — **solo durante la deuda transitoria** (ver nota arriba): consulta puntual para convenciones de transcripción concretas (sílaba tónica, primer ítem resuelto, marcadores de diálogos, sopas de letras) y casebook histórico. Nunca prevalece sobre schema o reglas vivos.
- El PDF de la unidad.

## Lookup bajo demanda

- `unidades/nc1-curso.json` — índice maestro (cross-unidad).
- Registries: `campos-semanticos-canonicos.json`, `verbos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`.
- Fuentes PCIC A1 (apoyo para naming/descripcion en cada dimensión): `pcic-a1-vocabulario.json`, `pcic-a1-gramatica.json`, `pcic-a1-pronunciacion-ortografia.json`. Además `pcic-a1-comunicacion.json` como recurso pragmático-comunicativo fuera de las 4 dimensiones del schema.

## Otros artefactos si hay conflicto

`scripts/validar_inventario.py`, `CLAUDE.md` raíz, `convenciones-y-casos-viejo.md` casebook (consulta puntual durante la deuda transitoria).

> **No leer durante la corrida:** `REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md`. Es discusión arquitectónica, no contrato. Contratos vivos: `schema-inventario.md` y `reglas-operativas.md`. `convenciones-y-casos.md` aún no está reescrito bajo el modelo IA-first (deuda transitoria declarada arriba); su contenido histórico se consulta en `convenciones-y-casos-viejo.md` solo para convenciones concretas de transcripción, y nunca prevalece sobre schema o reglas vivos. Desfases temporales entre contratos vivos → Apéndice transitorio del schema.

---

## Pasos

1. Verifica que existe `unidades/UX/fuente/UX-nc1.pdf`. Si no, aborta y avisa al autor.
2. Extrae según `schema-inventario.md` (§2-§4): texto verbatim + estructura física + IDs estables. `tipo`, `destreza`, `enfoque` y las 4 listas tipadas son parte del shape final; su población se difiere al paso 3.
3a. Clasifica y puebla actividades y cuadros según `reglas-operativas.md` (3 ejes + 4 listas tipadas + datos literales).
3b. Deriva los 4 bloques top-level consolidados (`vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`) a partir de las listas tipadas de actividades y cuadros.
4. Valida con `python3 scripts/validar_inventario.py X`. Si emite errores, vuelve al paso 3.
5. Escribe el JSON en `unidades/UX/UX-nc1-inventario.json`.
6. Avisa al autor para revisión visual.

---

## Fallback

Si no puedes resolver una decisión con confianza, aplica el protocolo de marcas internas de `reglas-operativas.md` y escala al autor. No fuerces decisión arbitraria.
