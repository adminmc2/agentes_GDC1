# Informe de corrida — U4-propuesta (fixture acotada pp.42-46)

Fecha: 2026-05-14
Branch: v10.115-wip
Worktree: /Users/armandocruz/Desktop/guia-prueba-v10.115

---

## Bloque A — Conformidad de setup

### Comandos verificados

```
$ git rev-parse --show-toplevel
/Users/armandocruz/Desktop/guia-prueba-v10.115           ✓ (esperado: guia-prueba-v10.115)

$ git branch --show-current
v10.115-wip                                              ✓ (esperado: v10.115-wip)
```

### Archivos leídos (orden cronológico)

| # | Archivo | Justificación contra cadena del prompt.md |
|---|---|---|
| 1 | `fases/1-extraccion-inventario/prompt.md` | Entry point operativo de la fase (ruta indicada en la invocación). |
| 2 | `fases/1-extraccion-inventario/CLAUDE.md` | Auto-cargado al trabajar en la carpeta de fase + reglas críticas. |
| 3 | `fases/1-extraccion-inventario/schema-inventario.md` | Lectura mínima obligatoria — shape del JSON. |
| 4 | `fases/1-extraccion-inventario/reglas-operativas.md` | Lectura mínima obligatoria — autoridad operativa de decisión. |
| 5 | `unidades/U4/fuente/U4-nc1.pdf` (pp.1-5 = pp.42-46 del libro) | PDF de la unidad (input declarado en §contrato del prompt). El PDF físico tiene 10 pp. mapeadas a libro 42-51; pp.42-46 = pp.1-5 físicas. |
| 6 | `unidades/nc1-curso.json` | Lookup bajo demanda — coincidencia cabecera + índice editorial U4 (vocabulario, gramática, comunicación, destrezas, cultura). |
| 7 | `fases/1-extraccion-inventario/verbos-canonicos.json` | Registry — lemas válidos para `tiempos_y_verbos[].lema`. |
| 8 | `fases/1-extraccion-inventario/campos-semanticos-canonicos.json` | Registry léxico — claves canónicas para `vocabulario_consolidado`. |
| 9 | `fases/1-extraccion-inventario/gramatica-canonica.json` | Registry gramatical — confirmado esqueleto vacío (impacta procedimiento §0.3.B). |
| 10 | `fases/1-extraccion-inventario/pronunciacion-ortografia-canonica.json` | Registry pron/orto — confirmado esqueleto vacío (impacta §0.3.C). |

### Exclusiones explícitas

- **NO** se ha abierto `unidades/U4/U4-nc1-inventario.json` (guardrail del usuario).
- **NO** se ha abierto `unidades/U1-propuesta/...` ni ningún `*-inventario.json` previo.
- **NO** se ha abierto `REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md` (declarado "no leer durante la corrida" en el prompt.md).
- **NO** se han abierto los PCIC (`pcic-a1-*.json`): no se necesitaron para esta fixture, los nombres canónicos usados ya estaban en `campos-semanticos-canonicos.json` o se documentan como propuesta abierta.
- **NO** se ha abierto `convenciones-y-casos-viejo.md`: la corrida no necesitó casebook puntual de transcripción más allá de lo cubierto por schema/reglas.

Declaración: ningún archivo `*-inventario.json` figura en la lista anterior. Si apareciera, la corrida estaría invalidada.

---

## Bloque B — Conformidad de salida

### Citas §X.Y invocadas (verificables contra reglas-operativas.md vigente)

| Cita | Aplicación en esta corrida |
|---|---|
| §0.1 (propuesta-en-chat) | Sin autor presente: TODA decisión ambigua queda como propuesta abierta en `_decisiones_ia` con texto "propuesta sin resolución de autor". Cero autoresoluciones. |
| §0.3.A | Barrido de léxico ejecutado sobre todos los `datos.*` de pp.42-46. |
| §0.3.B | Barrido gramatical ejecutado (pronombres OI, artículos, género/número, contables/incontables, hay, paradigma querer). |
| §0.3.C | Barrido pron/orto ejecutado, con resultado legítimamente vacío en alcance parcial. Documentado. |
| §1 (precedencias) | Aplicada para clasificar actividad/cuadro/nota. Cuadros de p44-p45 sin número → cuadro. "Para aprender" de p45 con imperativos → actividades 9 y 10 con `datos.subtipo: "para_aprender"` (§4). |
| §2.1 / §2.2 | Asignación de `tipo` con desempate por última acción de manipulación. |
| §2.3 | `destreza` y `enfoque` independientes de `tipo`. Anti-patrón del enfoque heredado de sección: enfoque NO copiado de `seccion`. |
| §5.1.1 (3 criterios principal/recurrente) | Aplicado a candidatos de `recurrente`: "Adjetivos de nacionalidad" (U2), "Parientes" (U3) cumplen los 3 criterios. |
| §5.2 (verbo soporte vs paradigma) | Verbos `tener`, `ser`, `comer`, `ir` (perífrasis) incluidos por aparición de formas concretas, aunque no sean foco. |
| §5.6 (canon léxico) | "Alimentos" y "Comidas preparadas" verificados literales en `campos-semanticos-canonicos.json`. PROHIBIDO inventar canónicos: "Colores", "Música" no existen → propuesta abierta, NO marcadas como `_pendiente_canon` (no cumple §5.9.1: requiere consulta previa al autor). |
| §5.9.1 / §5.9.2 | Marcas `_pendiente_canon` y `_funcion_ambigua` NO escritas porque no hubo autorización previa del autor. Las dudas viven en `_decisiones_ia`. |
| §6.5 (sufijo @R + chequeo previo obligatorio) | Ejecutado, ver sección "@R" abajo. |
| §6.6 (regla 11 audio.transcripcion) | Aplicada: actividades con audio + transcripción presente (act5 p43, act1 p46) cuentan como fuente; act1 p42 (escucha y repite sin transcripción explícita) NO genera entradas a consolidado vía audio — el léxico viene del input visible (etiquetas de imágenes), no del audio. |

### Trazado del procedimiento §0.3 (A/B/C)

**§0.3.A — vocabulario**:
- Paso 1 (foco principal): "Alimentos" y "Comidas preparadas" — coinciden con índice U4 → `principal`.
- Paso 3 (barrido verbatim): ejecutado sobre items_libro, dialogo_completo, palabras_recuadro, preguntas, ejemplos_modelo, expresiones_dadas, descripciones de imagen.
- Paso 4 (cruce): `campos-semanticos-canonicos.json` + `nc1-curso.json` unidades 1-3, 5-9. Hits: "Adjetivos de nacionalidad" (U2 índice), "Parientes" (U3 índice). "Colores" / "Música" / "Deportes" no canónicos seguros → propuesta abierta.
- Pasos 5-7: cumple criterios §5.1.1 → propuestos en `_decisiones_ia` para decisión del autor.
- Pasos 8: "Adjetivos de nacionalidad" y "Parientes" aplicados a `recurrente` por su solidez (declarados en índice de unidades anteriores + 3 criterios visibles).

**§0.3.B — gramática**:
- Paso 1: principal según índice U4 — "Verbo gustar", "Artículos indeterminados", "Nombres contables e incontables", "Hay", "Verbo querer", "Organizar el léxico".
- Paso 3 (barrido): pronombres OI (me/te/le/nos/os/les), pronombres tónicos (a mí/ti/...), artículo determinado (el/la/los/las), concordancia género/número, contables/incontables, paradigma de querer, "hay" impersonal.
- Paso 4 (cruce): `gramatica-canonica.json` = esqueleto vacío. `nc1-curso.json` U1: "Artículos determinados", "Masculino y femenino"; U2: "Plural de nombres y adjetivos". Recurrente potencial: "Pronombres personales OI" (no canónico declarado), "Artículos determinados" (recurre en frases tipo "los plátanos"). 
- Pasos 5-7: candidatos de recurrente declarados en `_decisiones_ia` como propuestas abiertas. NO aplicados al JSON (registry vacío + ausencia de autor).
- Resultado: `gramatica_consolidada.recurrente` queda **vacío declarado** (no por sesgo sino por falta de canónicos validados).

**§0.3.C — pronunciación/ortografía**:
- Paso 3 (barrido): convenciones tipográficas — la negrita en formas verbales (`qu**ie**res`) es marcador morfológico de raíz irregular, NO sílaba tónica (cf. nota §0.3.C). Tipos de actividad indicadores: `escucha_y_repite` en p42-act1 sí es `escucha_y_repite`, pero el contenido pedagógico es léxico (`enfoque: vocabulario`, no fonético — heurística §2.3 "palabras agrupadas por campo léxico"). No hay deletreo, dictado, ni transcripción fonética en pp.42-46.
- Paso 4 (cruce): `pronunciacion-ortografia-canonica.json` = esqueleto vacío. El bloque /r/ y /r̄/ del índice U4 está anunciado en p46 pero las actividades correspondientes residen en pp.47-51 (fuera del alcance).
- Resultado: `pronunciacion_ortografia_consolidada` legítimamente vacío. Documentado.

### Aplicaciones del sufijo @R (§6.5)

**Chequeo previo OBLIGATORIO**: para cada actividad candidata, verificación de `tipo` contra la lista cerrada de 5 productivos (`produccion_escrita_guiada`, `expresion_escrita_libre`, `expresion_oral_libre`, `tarea_final`, `interaccion_oral`):

| Actividad | tipo asignado | ¿En lista de 5? | ¿Hay palabras candidatas a @R? | @R aplicado |
|---|---|---|---|---|
| U4-p44-act3 | `produccion_escrita_guiada` | ✓ | No (todo léxico de respuestas aparece en items_libro) | No |
| U4-p44-act4 | `expresion_escrita_libre` | ✓ | respuestas vacías (libre) | No |
| U4-p45-act9 | `produccion_escrita_guiada` | ✓ | "hermano", "azul", "naranja", "fútbol" — figuran en `datos.ejemplos_modelo` (input visible) | No |
| U4-p45-act10 | `produccion_escrita_guiada` | ✓ | respuestas vacías | No |
| U4-p46-act4 | `interaccion_oral` | ✓ | léxico de postres ("manzana", "pera"...) figura en `datos.items_libro` y descripcion de imagen | No |

Cuadros: ningún `@R` posible (los cuadros no tienen `respuestas` — §9.5 schema). Verificado.

Resultado: **0 sufijos @R aplicados** en esta corrida. Cero falsos positivos por intuición. Cero `@R` sobre tipos no productivos.

### Coherencia semántica de `tiempos_y_verbos`

Para cada lema usado, declaración de qué forma del libro lo motivó y verificación contra `verbos-canonicos.json`:

| Lema | Forma motivadora | En registry | Tiempo | Coherente con paradigma |
|---|---|---|---|---|
| gustar | "gusta", "gustan" (cuadro p44 + actividades) | ✓ U4 PRE | Presente | ✓ tipo gustar |
| querer | "quiero/quieres/quiere/queremos/queréis/quieren" (cuadro p45) | ✓ U4 PRE,PER | Presente | ✓ irregularidad e→ie |
| tener | "tiene", "tengo", "tenemos", "tienen" | ✓ U1, U2 PRE | Presente | ✓ totalmente irregular |
| ser | "es", "son" | ✓ U1-U5 PRE | Presente | ✓ totalmente irregular |
| ir | "vamos a", "van a" (perífrasis) | ✓ U6, U7, U9 | Perífrasis | ✓ irregular; **uso anticipado en U4** (declarado en _decisiones_ia) |
| comer | "comemos", "come", "comen", "como" | ✓ U3 PRE | Presente | ✓ regular -er |

Lemas detectados pero EXCLUIDOS (con justificación):
- **haber** ("hay") — no en registry. Excluido + propuesta abierta en `_decisiones_ia`.
- **tomar** ("tomamos", "toman") — no en registry. Excluido + propuesta abierta.
- **hacer/hagamos** ("hacemos") en p43-act5 — `hacer` SÍ está en registry pero declarado U6 PRE. Aparición en U4 sería anticipación. Decisión IA: excluido para no contaminar fixture; documentar propuesta abierta. (Incluyo esta omisión aquí explícitamente.)
- **beber** — aparece como infinitivo léxico en "qué quieres beber" (p43-act5) y "Y de beber" (p46-act1). Forma léxica suelta tras querer (perífrasis querer+inf): no tiene paradigma trabajado → no entra en `tiempos_y_verbos` (regla §5.1.2 cierre operativa). Sí podría entrar como `vocabulario` de "Alimentos" (acción relacionada). Propuesta abierta.
- **preparar**, **comer** (infinitivo en "vamos a preparar" / "Quieres comer") — se trata como complemento de perífrasis ir+a y de querer+inf respectivamente; no se desglosan como entradas separadas.
- **poner** ("ponen las gallinas") en p42-act3 — no en registry. Excluido.

### Aplicación efectiva de §0.1 — propuestas abiertas registradas

Las 15 entradas de `_decisiones_ia` top-level del JSON son TODAS propuestas abiertas, ninguna autoresuelta. Resumen de las dudas escaladas:

1. Registries gramatica-canonica y pronunciacion-ortografia-canonica vacíos → canónicos por confirmar.
2. "Colores", "Música" no en registry léxico → confirmar canónicos.
3. Verbo "haber" no en registry → ¿añadir lema?
4. Verbo "tomar" no en registry → ¿añadir?
5. Política sobre imperativos de instrucción (Escucha, Completa…) en `tiempos_y_verbos`.
6. Frontera enfoque vocabulario/gramática en p43-act4 (foco "Hay" sobre alimentos).
7. Frontera completa_huecos vs produccion_escrita_guiada en p43-act7.
8. Frontera expresion_escrita_libre vs interaccion_oral en p44-act4.
9. Tipo no canónico de p45-act10 (copiar+memorizar).
10. Frontera enfoque vocabulario/cultura/comunicación en p43-act8.
11. Integración o desdoblamiento del campo PCIC "Bebida" bajo "Alimentos".
12. "ir" como perífrasis en U4 ¿anticipación o entrada legítima?
13. Declaración del chequeo previo @R con resultado 0 aplicaciones.
14. Cero contenido pron/orto en alcance parcial (legítimo).
15. Bloque autoevaluación ausente (vive en p51, fuera de alcance).

Adicionalmente, marcas internas dentro de actividades:
- U4-p43-act7 lleva `_decisiones_ia` propio para la frontera completa_huecos / produccion_escrita_guiada.
- Ningún `_pendiente_canon`, ningún `_funcion_ambigua: true` escritos en el JSON: §5.9 exige consulta previa al autor que no se ha producido. La política §0.1 prevalece — duda en chat (este informe), no marca silenciosa.

### Marcas resultantes con justificación

| Marca | Presente | Justificación |
|---|---|---|
| `_fixture_exploratoria` (top-level) | ✓ | Obligatoria por contrato de fixture (§Fixtures de CLAUDE.md de la fase). |
| `_decisiones_ia` (top-level) | ✓ | Auditoría persistente de propuestas abiertas (§5.9.3). NO bloquea cierre. |
| `_decisiones_ia` (en U4-p43-act7) | ✓ | Propuesta abierta sobre tipo. NO bloquea. |
| `_pendiente_canon` | ✗ | Requiere consulta previa al autor por §5.9.1 (no hubo). Aplicar sería violación. |
| `_funcion_ambigua` | ✗ | Misma razón (§5.9.2). Las ambigüedades viven en `_decisiones_ia`. |
| `_nota_unidad_atipica` | ✗ | U4 no es atípica. |
| `_migracion_rediseno` | ✗ | Es una fixture exploratoria, no migración de inventario heredado. |
| `unidad: "4p"` (string) | ✓ | Convención de fixture (no entero). |
| `paginas_libro: "42-46"` | ✓ | Acotado al alcance real. |

### Validador automático

NO ejecutado, conforme a la nota transitoria del prompt.md (gate 1 sustituido por validación manual mientras `validar_inventario.py` no esté alineado con `schema-inventario.md`).

---

## Conclusión operativa

Fixture U4-propuesta entregada con shape conforme al schema vigente (4 listas tipadas siempre presentes en cada actividad/cuadro, 4 bloques top-level consolidados, sufijo `@R` no aplicado tras chequeo previo §6.5, cero marcas bloqueantes silenciosas).

15 propuestas abiertas escaladas para decisión del autor. La fixture está lista para revisión humana en el dashboard pero NO es candidata a cierre canónico (es exploratoria por construcción).
