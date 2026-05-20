# Rediseño de fase 2 — documento de trabajo (VERSIÓN VIEJA)

> 🗄️ **VERSIÓN VIEJA — renombrado a `-viejo.md` el 2026-05-15 (v10.126).**
>
> El rediseño activo vive ahora en `fases/2-reciclaje/REDISEÑO-EN-CURSO.md` (modelo IA-first, en construcción). Este documento se conserva como reservorio histórico de las decisiones tomadas en la versión anterior, mientras se va integrando lo aprovechable en el documento nuevo paso a paso.
>
> **Reglas para este archivo durante la transición:**
> - **No se sigue actualizando** con decisiones nuevas. Las decisiones nuevas viven en el documento activo.
> - **Se consulta como referencia histórica** (D1, D2, D3, R1-R5, §8 son piezas potencialmente aprovechables).
> - **Cuando el documento activo cubra todo lo vigente de aquí**, este `-viejo` se archiva en `docs/historico/`.

> **Estado original (preservado por trazabilidad):** EN CONSTRUCCIÓN. Se elimina cuando el rediseño se cierre y la decisión final viva en `CLAUDE.md`, `reglas-reciclaje.md` y PROCESO-MAESTRO.
>
> **Audiencia:** autor + revisor. Ejecutor (Claude) lo va actualizando con cada decisión cerrada y cada hallazgo del revisor.

---

## 1. Punto de partida — el problema

El modelo actual (post v10.97) trata `mapa` y `auto` como tipos paralelos de hilo: cada script genera hilos independientes. Eso produce **duplicación cuando el mismo contenido editorial aparece en ambos niveles**.

**Estado del JSON vivo (post-U7):**
- 92 hilos `mapa`
- 79 hilos `auto`
- Total: 171 hilos

**Hallazgo Alta del revisor (2026-05-10):** la fusión por igualdad de títulos es ingenua. De los 161 hilos al momento de la observación (92 + 69, antes de U7):
- Solo 18 coinciden por título normalizado.
- 51 son `auto`-only.
- 74 son `mapa`-only.
- Hay equivalencias semánticas no literales que la igualdad ingenua no detecta.

**Análisis post-U7 sobre los huérfanos (campos en inventario pero no en `nc1-curso.json`):** 61 huérfanos detectados, agrupados en tres patrones:
- **Patrón 1 — campos válidos sin entrada en el índice (~25):** "Establecimientos", "Medios de transporte", "Animales domésticos", "Marcadores de lugar", "Saludos y despedidas", "Verbos regulares (presente)", etc.
- **Patrón 2 — ruido de codificación del ejecutor (~10):** `_descripcion`, `lugares_publicos`, `descripcion_habitaciones`, `expresiones_de_lugar`, `vivienda_ecologica`, `verbos`. Errores de extractor a corregir en los inventarios.
- **Patrón 3 — campos contextuales/parches (~26):** "Vocabulario del diálogo", "Texto Un día en el zoo", "Otros", "Cartagena de Indias", etc. El ejecutor metió bloques sin categoría clara.

**Decisión operativa (autor):** los nombres del índice del libro (`nc1-curso.json`) son inmutables; solo se revisan los campos huérfanos. Las correcciones de los huérfanos del patrón 2 y 3 se documentan en `convenciones-y-casos.md` cuando se modifiquen los inventarios.

**Conclusión:** sin tabla de equivalencias canónica + universo cerrado de hilos válidos, el rediseño replica el problema actual.

---

## 2. Modelo objetivo

**Un único hilo por contenido editorial, con tres capas progresivas de información:**

| Capa | Origen | Información que añade |
|---|---|---|
| `mapa` | `nc1-curso.json` | Identidad del hilo: id, título, tipo. Eventos básicos `(unidad, seccion, accion)`. Esqueleto. **Nombres inmutables — vienen del libro publicado.** |
| `auto` | `vocabulario_consolidado` del inventario aprobado | Palabras concretas por unidad, separadas en `principal` / `recurrente` / `comprension`. Enriquece eventos existentes en cada unidad donde aparece el hilo. **Codificación corregible**. |
| `detalle` | Recorrido fino de actividades del inventario | Presentación real en la sección. Pendiente de definir cómo se captura. |

**El campo `nivel_analisis` deja de ser clasificación de hilo y pasa a indicar el grado de población del hilo:** `mapa` (solo esqueleto) → `auto` (enriquecido con palabras) → `detalle` (completo con presentación).

**Restricción operativa de codificación:** el campo semántico que el ejecutor 2 escribe en el inventario debe coincidir con un canónico válido del universo de hilos (sección 3 D2). Si no coincide, es error de codificación a corregir.

---

## 3. Decisiones cerradas

### D1 — Tabla de equivalencias canónica externa (2026-05-10)

**Decisión:** la fusión `mapa` ↔ `auto` no se hace por similitud de strings. Se hace consultando una tabla de equivalencias canónica curada por el autor.

**Motivación:** hallazgo Alta del revisor (sección 1). Sin tabla canónica, el rediseño replica el problema actual.

**Artefacto:** `unidades/nc1-equivalencias-hilos.json`. Estructura:

```jsonc
{
  "_nota": "Tabla canónica que vincula títulos del índice editorial (mapa) con campos semánticos de los inventarios (auto). Curada por el autor. Single source of truth para la fusión.",
  "equivalencias": [
    {
      "canonico": "Países hispanohablantes",
      "origen": "indice",
      "mapa": ["Países que hablan español", "Países hispanohablantes"],
      "auto": ["Países hispanohablantes"]
    },
    {
      "canonico": "Establecimientos",
      "origen": "pcic_a1",
      "mapa": [],
      "auto": ["Establecimientos", "Establecimientos: cine, restaurante, farmacia..."]
    }
  ]
}
```

- `canonico`: título único del hilo final.
- `origen`: `indice` (viene del índice del libro) o `pcic_a1` (no en índice pero en universo válido D2).
- `mapa`: aliases que el script de mapa puede encontrar en `nc1-curso.json`.
- `auto`: aliases que el script de auto puede encontrar en los inventarios.

**Reglas:**
- Si un título no aparece en la tabla → el script aborta con error claro: *"el campo 'X' no está en `nc1-equivalencias-hilos.json`. Añádelo antes de seguir."* Cero adivinanza programática.
- La tabla la cura el autor. Un script auxiliar puede generar un borrador inicial (CSV con sugerencias) que el autor revisa y completa a mano.

### D2 — Universo cerrado de hilos canónicos válidos (2026-05-10)

**Decisión:** el sistema acepta como `canonico` válido únicamente entradas que pertenezcan a uno de estos dos conjuntos:

**(a) Entradas del índice editorial — `nc1-curso.json`:** todos los `vocabulario`, `gramatica`, `comunicacion`, `pronunciacion_ortografia`, `para_aprender`, `contenido_general` literalmente como aparecen en el JSON del curso. **Nombres inmutables.**

**(b) Subcategorías curadas del PCIC A1 (Cervantes):** lista cerrada extraída de `caes complete system/references/plan_curricular/by_level/a1/a1_nociones_especificas_completo.json`, filtrada por relevancia para libro escolar A1 dirigido a adolescentes 12-15. Excluyen subcategorías fuera del alcance editorial (justicia, ejército, religión, economía empresarial, derechos laborales, pesca, etc.).

**Listado curado (~55 subcategorías PCIC A1):**

```
DIMENSIÓN FÍSICA Y PERCEPTIVA
- Partes del cuerpo
- Características físicas
- Acciones y posiciones que se realizan con el cuerpo
- Carácter y personalidad

IDENTIDAD PERSONAL
- Nombre
- Dirección
- Número de teléfono
- Lugar y fecha de nacimiento
- Nacionalidad
- Edad
- Sexo
- Profesión
- Documentación
- Objetos personales

RELACIONES HUMANAS Y SOCIALES
- Relaciones familiares
- Relaciones sociales
- Celebraciones y actos familiares, sociales y religiosos

ALIMENTACIÓN
- Dieta y nutrición
- Bebida
- Alimentos
- Platos
- Restaurante

EDUCACIÓN
- Centros e instituciones educativas
- Profesorado y alumnado
- Sistema educativo
- Aprendizaje y enseñanza
- Exámenes y calificaciones
- Lenguaje de aula
- Material educativo y mobiliario de aula

TRABAJO
- Profesiones y cargos
- Lugares, herramientas y ropa de trabajo
- Actividad laboral

OCIO
- Tiempo libre y entretenimiento
- Espectáculos y exposiciones
- Deportes

INFORMACIÓN Y MEDIOS DE COMUNICACIÓN
- Correspondencia escrita
- Teléfono
- Prensa escrita
- Televisión y radio
- Internet

VIVIENDA
- Acciones relacionadas con la vivienda - Ocupación
- Características de la vivienda - Tipos
- Características de la vivienda - Partes
- Objetos domésticos - Muebles y objetos domésticos
- Objetos domésticos - Electrodomésticos

SERVICIOS
- Servicios sanitarios
- Servicios sociales

COMPRAS
- Lugares, personas y actividades
- Ropa, calzado y complementos
- Pagos

SALUD E HIGIENE
- Salud y enfermedades
- Síntomas
- Centros de asistencia sanitaria
- Higiene

VIAJES, ALOJAMIENTO Y TRANSPORTE
- Tipos de viajes
- La playa
- La montaña
- Alojamiento
- Sistema de transporte - Tipos de transporte por tierra
- Sistema de transporte - Tipos de transporte aéreo

CIENCIA Y TECNOLOGÍA
- Cuestiones generales
- Matemáticas
- Informática y nuevas tecnologías

CULTURA Y ARTE
- Música y danza
- Cine y teatro

GEOGRAFÍA Y NATURALEZA
- Universo y espacio
- Geografía física, humana y política
- Paisaje y accidentes geográficos
- Ciudad
- Campo
- Clima y tiempo atmosférico
- Fauna
- Flora
```

**Regla absoluta:** un campo semántico que aparezca en un inventario y NO esté en (a) ni en (b) → el sistema notifica al humano. El autor decide caso por caso si:
- es error de codificación del ejecutor → corregir el inventario.
- es subcategoría PCIC A1 que faltaba en la lista curada → ampliar D2.
- es excepción legítima fuera de A1 → registrar como `origen: "excepcion"` con nota.

La lista de D2 puede ampliarse con el tiempo conforme aparezcan necesidades reales. Cualquier ampliación se documenta en este archivo y luego en `reglas-reciclaje.md` cuando se cierre.

---

## 4. Decisiones pendientes

### P1 — Almacenamiento de los datos enriquecidos: opción A vs opción B

**Opción A — Los datos viven en `nc1-reciclaje.json`.** Cada evento contiene las palabras `principal` / `recurrente` / `comprension` para esa unidad. Se regenera al integrar cada unidad. El dashboard solo lee el JSON.

**Opción B — Los datos NO viven en `nc1-reciclaje.json`.** El JSON solo tiene la estructura mapa. Cuando el dashboard abre el modal de un hilo, lee al vuelo el inventario de las unidades correspondientes y extrae las palabras del campo semántico.

**Respuestas del autor (2026-05-10):**
- El JSON será consumido por agentes IA en el futuro → favor A.
- El JSON se edita a través de Claude Code directamente → favor A.
- Tamaño no es bloqueante → A viable.
- Mutabilidad: los nombres son inmutables (vienen del libro), pero la codificación es corregible. Cualquier corrección de inventario debe regenerar el reciclaje → compatible con A.

**Estado:** P1 → **opción A confirmada**, queda formalizar el paso de "regenerar tras corrección" (sección P2).

### ~~P2~~ → D3 — Disparador de regeneración: Claude Code (2026-05-10)

**Decisión:** la regeneración del reciclaje tras una corrección post-integración se invoca **a través de Claude Code** como agente operativo. No hay hook git ni comando periódico programado.

**Modelo operativo (mismo que fase 1):** el autor trabaja en sesión con Claude Code; cuando se corrige un inventario, Claude Code ejecuta `scripts/regenerar_reciclaje_vocabulario.py` como parte del flujo. Los futuros agentes IA del sistema seguirán el mismo patrón (Claude Code + scripts).

---

## 5. Hallazgos del revisor (registro)

| Fecha | Severidad | Hallazgo | Estado |
|---|---|---|---|
| 2026-05-10 | Alta | Fusión por igualdad de títulos es ingenua. Solo 18/161 coinciden. Hay equivalencias semánticas no literales. Sin tabla canónica, el rediseño replica el problema. | ✅ Cerrado por D1 + D2 |

---

## 6. Pasos de migración (borrador, sujeto a las decisiones pendientes)

1. Construir `nc1-equivalencias-hilos.json` con dos fuentes:
   - índice del libro (D2.a) → entradas `origen: "indice"`.
   - lista curada PCIC A1 (D2.b) → entradas `origen: "pcic_a1"`.
   Genera un borrador automático que el autor cura a mano.
2. Decidir P2 (regeneración tras corrección).
3. Reescribir `regenerar_reciclaje_mapa.py` para que consulte la tabla y use el `canonico` como `titulo` del hilo.
4. Reescribir `regenerar_reciclaje_vocabulario.py` para enriquecer el evento del hilo canónico (opción A) en vez de generar hilos paralelos.
5. Migrar el `nc1-reciclaje.json` actual al nuevo modelo (script one-off).
6. Detectar y reportar los huérfanos del patrón 2 y 3 (sección 1) para corrección de los inventarios. Cada corrección se documenta en `convenciones-y-casos.md`.
7. Actualizar `fases/2-reciclaje/CLAUDE.md` y `reglas-reciclaje.md` al nuevo modelo. Cerrar deuda de naming con PROCESO-MAESTRO.
8. Ajustar el render del dashboard: timeline con estructura mapa + modal con datos auto al hacer clic.
9. Eliminar este documento (`REDISEÑO-EN-CURSO.md`) cuando todo esté en producción.

---

## 7. Capa 1 — Validación cruzada cross-unidad (post-rediseño cuestión 1, 2026-05-12)

> **Origen:** decisiones derivadas del rediseño de fase 1 que requieren chequeos cross-unidad. Estas reglas viven en el validador `scripts/validar_inventarios_cross.py` (capa 1 del pipeline de fase 2 redefinida, ver `docs/historico/REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md` §6 — archivado 2026-05-14).
>
> **Nota:** este bloque sustituye conceptualmente al viejo modelo "mapa + auto" en lo relativo a coherencia cross-unidad. La materialización (código del validador) se hace en E4a del plan del rediseño de fase 1, no aquí.

### R1 — Detección de anticipación de léxico

**Premisa:** fase 1 codifica `recurrente` solo si el léxico aparece con frecuencia, no está en el índice de la propia unidad, **y** no es canónico en una unidad posterior. Lo que cumple las dos primeras condiciones pero falla la tercera lo deja silenciosamente fuera. Fase 2 lo detecta y reporta.

**Algoritmo (4 pasos):**

1. **Leer el índice editorial completo** (`nc1-curso.json`): para cada unidad U(n), conocer su `vocabulario[]` canónico.
2. **Leer el `principal` declarado por fase 1** en cada `UX-nc1-inventario.json`.
3. **Leer el `recurrente` declarado por fase 1** en cada `UX-nc1-inventario.json`.
4. **Re-ejecutar análisis de frecuencias** sobre las actividades de cada unidad. Para cada término frecuente que **no** está en `principal` ni en `recurrente` de U(n):
   - Si el término es canónico en una unidad **posterior** U(n+k) → **alerta de anticipación**.
   - Si el término es canónico solo en una unidad **anterior** U(n−k) o en ninguna → no es alerta.

**Output:** lista de alertas estructuradas con `{unidad: U(n), termino, unidad_canónica: U(n+k), frecuencia, ejemplos: [actividad_id]}`.

### R2 — Detección de inventos (validación intra-unidad asumida como pre-condición)

"No inventar palabras" es regla de fase 1 (intra-unidad). Fase 2 ejecuta un chequeo redundante: verifica que cada palabra de `vocabulario_consolidado` aparece literalmente en alguna actividad/cuadro de la unidad. Si fase 1 hace su trabajo, este chequeo siempre pasa; si falla, indica bug del extractor.

### R3 — Detección de errores de clasificación semántica

Fase 2 usa el canon (`campos-semanticos-canonicos.json`) para detectar palabras categorizadas incorrectamente. Ejemplos: `campeón` en `Nacionalidades`, `mesa` en `Colores`. Es regla intra-unidad (de fase 1), pero fase 2 la usa como sanity check post-extracción.

### R4 — Inconsistencias de progresión (regla preexistente)

Casos cubiertos por el modelo viejo que se preservan en el nuevo modelo:
- Léxico marcado como `recurrente` en U(n) que no fue `principal` en ninguna U(n−k). Indica que el término aparece sin haberse introducido formalmente.
- Dos unidades usan nombres distintos para el mismo contenido semántico (los aliases del canon ayudan, pero residuos pueden quedar).
- Verbos que aparecen en `vocabulario_consolidado` cuando deberían vivir en `tiempos_y_verbos_consolidado` (caso histórico documentado en U1: "Verbos básicos formas singulares" estaba en `recurrente` de `vocabulario_consolidado`).

### R5 — Coherencia bidireccional de trazabilidad (asumida como pre-condición)

La coherencia bidireccional entre `actividad.X` y `top-level.X.fuentes` la chequea el validador intra-unidad de fase 1. Fase 2 la asume como pre-condición y aborta si no se cumple.

### Estado

- Diseño de las reglas: ✅ cerrado el 2026-05-12.
- Implementación en `validar_inventarios_cross.py`: pendiente de E4a del rediseño de fase 1.

---

## 8. Componentes "siempre presentes no indexados" — responsabilidad analítica de fase 2 (registrado 2026-05-15, v10.117)

### Definición

Componentes lingüísticos que **aparecen sistemáticamente en el corpus de NC1** pero **el libro NO los enseña como contenido en el índice editorial** (`gramatica[]` / `vocabulario[]` / etc. de `nc1-curso.json`). Su omnipresencia es un fenómeno cross-unidad detectable; su tratamiento canónico no es trivial.

### Por qué no se canonizan en fase 1

El registry de fase 1 (`gramatica-canonica.json`, `campos-semanticos-canonicos.json`, etc.) se ancla al criterio **"materialmente presente y analíticamente necesario"** (referencia: docs/historico/REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md §14, criterio aclarado 2026-05-15). Eso excluye material que aparece como **input pragmático del corpus** pero no se trabaja como contenido enseñado. Si fase 1 los canonizase automáticamente, el registry se inflaría con material que NC1 no codifica como aprendizaje.

### Responsabilidad de fase 2

**Fase 2 debe proponer al autor el tratamiento canónico** de estos componentes cuando detecte el patrón de presencia sistemática cross-unidad. La propuesta puede ser:
- Canonizar como categoría cross-unidad en el registry correspondiente.
- Tratarlos como fenómeno transversal modelado en un bloque analítico nuevo de `nc1-reciclaje.json`.
- Ignorarlos si no aportan valor de análisis.

La decisión la toma el autor; fase 2 hace la propuesta lógica basada en evidencia (frecuencia, distribución por unidades, función pragmática vs gramatical).

### Lista inicial de candidatos (detectados durante v10.117)

Identificados al materializar `gramatica-canonica.json` y comparar con el corpus disponible:

| Candidato | Estado actual | Evidencia | Pregunta para fase 2 |
|---|---|---|---|
| Conjunciones copulativas (`y`, `e`) | NO canonizadas en fase 1 | Aparición omnipresente en todas las unidades como coordinador de constituyentes | ¿Se modela como categoría gramatical cross-unidad, o queda como input pragmático? |
| Conjunciones disyuntivas (`o`, `u`) | NO canonizadas | Aparición frecuente, especialmente en cuestionarios y opciones | Idem |
| Adverbios de afirmación y negación (`sí`, `no`, `también`, `tampoco`) | NO canonizadas | "sí"/"no" omnipresente desde U1; "también"/"tampoco" tardío (U6+ probablemente) | ¿Se separan por momento de aparición? ¿"también"/"tampoco" sí se codifican y "sí"/"no" no? |

### Política operativa

1. **Fase 1 no los canoniza automáticamente.** Si una extracción surfacea uno de estos componentes con anclaje material claro (cuadro explícito, actividad de contenido enseñado), se escala al autor por §0.1 de `reglas-operativas.md`.
2. **Fase 2 los detecta como patrón** cuando agrega inventarios cross-unidad. La detección produce un `hallazgo` en la corrida de fase 2, no una modificación silenciosa del registry.
3. **El autor decide** caso por caso. La decisión se documenta aquí (§8) cuando se cierra cada candidato.
4. **Si el autor canoniza**, se añade al registry correspondiente de fase 1 con `_pcic_ref` y `_apariciones` documentados, y se actualiza `_meta.siempre_presentes_no_indexados` del registry para retirar el candidato.

### Criterio de ampliación

Esta lista se amplía cuando una corrida real de fase 1 o fase 2 detecta un nuevo componente "siempre presente pero no indexado" que merezca consideración. No es lista cerrada.