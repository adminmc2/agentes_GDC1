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

> **Nota transitoria.** Mientras `scripts/validar_inventario.py` no esté alineado con `schema-inventario.md`, el gate 1 (validador automático) queda sustituido por validación manual contra el schema y revisión visual. `reglas-operativas.md` y `convenciones-y-casos.md` sí están alineados con el schema.
>
> Puntos de divergencia conocidos y condiciones de retirada → Apéndice transitorio del schema (§A.1, §A.3).

---

## Lectura mínima obligatoria

**Gate de arranque (obligatorio antes de empezar la extracción):** el ejecutor debe **declarar explícitamente en chat** haber leído los tres contratos vivos antes de tocar el JSON. Si no se ha hecho, **abortar** y leerlos. Esta declaración es condición de inicio, no formalidad — la documentación de fase 1 es **siempre obligatoria**.

- `schema-inventario.md` — shape del JSON.
- `reglas-operativas.md` — autoridad operativa (reglas, protocolos, marcas, política PCIC).
- `convenciones-y-casos.md` — convenciones de transcripción y casebook (sí, lookup puntual durante la corrida, pero se lee al menos por encima al arranque para conocer §1 y §4).
- El PDF de la unidad.

**Obligación recíproca del invocador.** Quien invoque este prompt (coordinador, autor, otro agente) debe citarlo literalmente (`fases/1-extraccion-inventario/prompt.md`) en la instrucción. No basta con describir la tarea: la cadena de invocación tiene que apuntar al prompt para que el ejecutor cargue su `CLAUDE.md` hermano y los contratos vivos.

## Lookup bajo demanda

- `unidades/nc1-curso.json` — índice maestro (cross-unidad).
- Registries: `campos-semanticos-canonicos.json`, `verbos-canonicos.json`, `gramatica-canonica.json`, `pronunciacion-ortografia-canonica.json`.
- Fuentes PCIC A1 (apoyo para naming/descripcion en cada dimensión): `pcic-a1-vocabulario.json`, `pcic-a1-gramatica.json`, `pcic-a1-pronunciacion-ortografia.json`. Además `pcic-a1-comunicacion.json` como recurso pragmático-comunicativo fuera de las 4 dimensiones del schema.

## Lookup puntual durante la corrida

- `convenciones-y-casos.md` — lookup puntual para convenciones de transcripción y casebook; nunca prevalece sobre `schema-inventario.md` ni `reglas-operativas.md`.

## Otros artefactos si hay conflicto

`scripts/validar_inventario.py`, `CLAUDE.md` raíz.

> **Contratos vivos en orden de precedencia:** `schema-inventario.md` > `reglas-operativas.md` > `convenciones-y-casos.md`. Si una regla concreta entra en conflicto entre niveles, prevalece el superior. Desfases temporales entre contratos vivos → Apéndice transitorio del schema.

---

## Pasos

1. Verifica que existe `unidades/UX/fuente/UX-nc1.pdf`. Si no, aborta y avisa al autor.
2. Extrae según `schema-inventario.md` (§2-§4): texto verbatim + estructura física + IDs estables. `tipo`, `destreza`, `enfoque` y las 4 listas tipadas son parte del shape final; su población se difiere al paso 3.
3a. Clasifica y puebla actividades y cuadros según `reglas-operativas.md` (3 ejes + 4 listas tipadas + datos literales).
3b. Deriva los 4 bloques top-level consolidados (`vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`) a partir de las listas tipadas de actividades y cuadros.
4. Valida: si el validador automático está alineado con el schema, ejecuta `python3 scripts/validar_inventario.py X` y vuelve al paso 3 si emite errores. **Estado transitorio (ver nota arriba):** mientras `scripts/validar_inventario.py` no esté alineado con `schema-inventario.md`, la validación es manual contra el schema + revisión visual del autor.
5. Escribe el JSON en `unidades/UX/UX-nc1-inventario.json`.
6. Avisa al autor para revisión visual.

---

## Fallback

Si no puedes resolver una decisión con confianza, aplica el protocolo de marcas internas de `reglas-operativas.md` y escala al autor. No fuerces decisión arbitraria.
