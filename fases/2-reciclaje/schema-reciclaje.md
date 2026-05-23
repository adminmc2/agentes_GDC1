# Schema — `nc1-reciclaje.json` (contrato de fase 2)

> **Qué es:** shape canónico del archivo de reciclaje que produce la fase 2. Contrato de datos — define estructura, claves, tipos y enumeraciones. Espeja el rol de `schema-inventario.md` en fase 1.
>
> **Estado:** EN CONSTRUCCIÓN (Nivel 2 del rediseño, `REDISEÑO-EN-CURSO.md` §5). El modelo conceptual está cerrado en §1-§10 del rediseño; este documento lo materializa como contrato.
>
> **Funcional para dos destinos:** el shape sirve tal cual como **archivo JSON** (estado actual) y como **base de datos** (futuro) — la lista plana de hilos hace que cada hilo sea un registro/documento sin reestructurar.

---

## §1. Estructura top-level

```jsonc
{
  "_meta":      { … },        // metadatos del archivo
  "hilos":      [ {hilo}, … ],// lista plana — un hilo por contenido editorial
  "propuestas": [ {prop}, … ] // cola de decisiones IA pendientes de cierre humano
}
```

Lista **plana** de hilos: el agrupado por `bloque` y por `_grupo` es asunto de **vista** (el dashboard agrupa al renderizar), no de almacenamiento.

### §1.1. `_meta`

| Clave | Tipo | Contenido |
|---|---|---|
| `version` | string | Versión del archivo (alineada con `CHANGELOG.md`). |
| `fecha` | string | Fecha de la última regeneración. |
| `unidades_cubiertas` | lista de enteros | Unidades ya procesadas (ej. `[0,1,2]`). |
| `estado` | string | Estado del archivo (ej. `en construcción`, `cerrado`). |

---

## §2. El hilo

Un hilo = el recorrido de un contenido editorial a lo largo del curso.

| Clave | Tipo | Contenido |
|---|---|---|
| `id` | string | **Clave primaria estable.** Slug `<bloque>-<slug>` (`voc-colores`, `gram-ser-estar`, `verb-comer`, `perif-ir-a-inf`). Asignado al crear el hilo; **no se recalcula** si cambia el `titulo`. |
| `bloque` | enum | `vocabulario` \| `gramatica` \| `pronunciacion_ortografia` \| `verbal` \| `perifrasis`. |
| `titulo` | string | Nombre canónico del contenido, literal del registry correspondiente. Legible; puede corregirse sin romper el `id`. |
| `_grupo` | string | **Solo `bloque: gramatica`.** Subsistema gramatical (§6.3): Determinantes, Pronombres, Sintagma nominal y concordancia, Construcciones, Tiempos y modos verbales, Adverbios y marcadores, Preposiciones. |
| `nivel_analisis` | enum | Grado de población del hilo: `mapa` \| `auto` \| `detalle` (§4.2). |
| `eventos` | lista | Apariciones del contenido por unidad (§3). |
| `detalle` | objeto | **Solo cuando `nivel_analisis: detalle`.** Justificación lingüístico-pedagógica (§5). |

---

## §3. El evento

Un evento = una aparición del contenido en una unidad concreta.

| Clave | Tipo | Contenido |
|---|---|---|
| `unidad` | entero | Unidad del evento. |
| `tiempo` | enum | **Solo `verbal` y `perifrasis`.** Evento por lema-tiempo (§3.2): `Presente` \| `Pretérito indefinido` \| `Imperativo` \| `Infinitivo`. |
| `etiquetas` | lista de enum | Qué hace la unidad con el contenido (§2.3): `introduce`, `amplia`, `aplica`, `sistematiza`, `contrasta`, `anticipacion` (+ `discrimina` solo en pron/orto). Coexisten. |
| `procedencia_indice` | enum | Estatus identitario del título canónico (§9, reformulado v11.76): `declarado` \| `reconciliado` \| `nuevo`. Resuelto mecánicamente por Capa 1 leyendo los registries, **excepto en bloque `verbal`** (Capa 2 lo decide; v11.76). Si `reconciliado`, ver `reconciliado_con`. |
| `reconciliado_con` | string con prefijo | **Solo si `procedencia_indice: reconciliado`.** Referencia con prefijo obligatorio: `"indice:<entrada literal del curso>"` cuando es alias de una entrada del índice del curso; `"pcic:<referencia concreta>"` cuando el respaldo viene de PCIC sin entrada en el curso; `"pcic:A1"` como fallback para vocabulario con `origen=pcic_a1` sin referencia más fina. Semántica ampliada en v11.76. |
| `formas` | lista de string | **Solo `bloque: verbal`.** Formas conjugadas concretas que esa unidad trabaja de ese lema-tiempo (§7.1). |
| `explicacion` | objeto | Opcional — presente si el libro explica el contenido en esa unidad (§4). |
| `evidencias` | lista | Referencias a las actividades/cuadros del inventario que sustentan el evento (preservan el sufijo `@R` cuando aplica, §3.5). |

Ejes ortogonales (§9.5): `etiquetas` (qué hace la unidad) y `procedencia_indice` (estatus en el índice) conviven; un evento lleva los dos.

---

## §4. El objeto `explicacion`

Presente en un evento cuando el libro expone una explicación/cuadro del contenido (§8). Aplica a los 5 bloques.

| Clave | Tipo | Contenido |
|---|---|---|
| `que_dice_el_libro` | string | Lo que el cuadro expone literalmente. |
| `fuente` | string | Referencia al cuadro del inventario (ej. `cuadro@p47`). |
| `analisis_ia` | string | El trabajo de fase 2: relaciones lógicas, prerrequisitos, coherencia, incoherencias. |

---

## §5. El objeto `detalle` (esqueleto — sub-contrato diferido)

Presente cuando `nivel_analisis: detalle`. Modela la justificación lingüístico-pedagógica como grafo (§4.4).

```jsonc
"detalle": {
  "nodos":   [ … ],  // cada nodo = un evento con su análisis lingüístico-pedagógico
  "enlaces": [ … ]   // cada enlace = una relación lingüística entre dos nodos
}
```

**Contrato mínimo fijado ahora:** `detalle` tiene `nodos` y `enlaces`; un nodo corresponde a un evento; un enlace expresa una dependencia/relación lingüística (prerrequisito, contraste, ampliación) entre nodos.

**Diferido:** el shape exacto de `nodo` y `enlace` se cierra como sub-contrato junto con el diseño del modal a página completa del dashboard (§4.4) — no se fija aquí para no diseñar en el vacío.

---

## §6. La propuesta (cola de decisiones IA)

`propuestas[]` es la cola de lo que la Capa 2 IA propone y el humano aún no ha cerrado. Separada del contenido para que `hilos[]` sea firme y las propuestas sean una cola resoluble. En BD, su propia tabla.

| Clave | Tipo | Contenido |
|---|---|---|
| `id` | string | Identificador de la propuesta. |
| `tipo` | enum | `reconciliacion` \| `categoria_nueva` \| `siempre_presente`. |
| `descripcion` | string | Qué propone la IA, con su evidencia/razonamiento. |
| `hilo_ref` | string | `id` del hilo afectado, cuando aplica. |
| `estado` | enum | `pendiente` \| `aceptada` \| `rechazada`. |
| `resolucion` | string | Decisión del autor al cerrarla (cuando `estado ≠ pendiente`). |

El análisis IA **ya consolidado** (`explicacion.analisis_ia`, el razonamiento del `detalle`) NO va aquí — va inline en el hilo/evento. `propuestas[]` es solo lo **pendiente de cierre humano**.

---

## §7. Notas

- **Naming canónico:** `titulo` es literal del registry de su dimensión (universo cerrado, §6.1). Fase 2 no inventa títulos.
- **Granularidad del hilo por bloque** (§2.2): vocabulario → campo semántico; gramática → categoría; pron/orto → categoría; verbal → lema; perífrasis → perífrasis.
- Este documento está EN CONSTRUCCIÓN; las claves marcadas como diferidas (§5) se cierran en pasos siguientes del rediseño.