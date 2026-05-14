# Informe de corrida — Fixture exploratoria U4 (`U4-propuesta`)

> Corrida exploratoria del rediseño de fase 1 sobre la U4 (Comidas y bebidas) del libro Nuevo Compañeros 1. Fecha: 2026-05-14. No es inventario canónico.

---

## 1. Archivos abiertos y orden de lectura

1. `fases/1-extraccion-inventario/prompt.md` — flujo operativo y nota transitoria sobre el validador.
2. `fases/1-extraccion-inventario/CLAUDE.md` — banner de fase 1 en migración y reglas críticas.
3. `fases/1-extraccion-inventario/schema-inventario.md` — shape canónico (§0/§1/§3/§3.2/§4/§5–§5d/§7/§8/§9.1–§9.6/§10/§11/§13/§14, Apéndice transitorio §A.1–§A.5).
4. `fases/1-extraccion-inventario/reglas-operativas.md` — banner de follow-ups, §1, §2, §3, §4, §5.1, §5.3, §5.6, §5.10, §5.11, §5.12.A/B/C, §5.13, §5.14.
5. `unidades/U1-propuesta/U1-propuesta-nc1-inventario.json` — referencia de cómo otro agente aplicó el shape (con divergencias respecto a schema actual; no se copió ciegamente).
6. `unidades/U4/fuente/U4-nc1.pdf` — fuente, leído íntegro (pp. 42-51, 10 páginas).
7. `unidades/nc1-curso.json` — cabecera oficial de U4 (título, paginas_libro, contenidos_indice).
8. `fases/1-extraccion-inventario/campos-semanticos-canonicos.json` — registry semántico (98 entradas).
9. `fases/1-extraccion-inventario/verbos-canonicos.json` — registry verbal (48 lemas).
10. `unidades/U4/U4-nc1-inventario.json` — únicamente como consulta de cobertura comparativa (no se copió shape).

---

## 2. Citas del contrato invocadas por decisión

| Cita | Donde se aplicó |
|---|---|
| schema §0 (naturaleza del contrato — shape canónico estable) | Decisión de seguir el schema sobre el shape de U1-propuesta cuando divergen (p. ej. `items` vs `palabras`). |
| schema §1 (top-level 13+3+1) | Inclusión de `vocabulario_consolidado`, `tiempos_y_verbos_consolidado`, `gramatica_consolidada`, `pronunciacion_ortografia_consolidada`, `secciones`, `autoevaluacion`, `_decisiones_ia`, `paginas_detalle`. |
| schema §3 (4 listas tipadas siempre presentes) | Cada actividad recibe las 4 listas (vacías si no aplica). |
| schema §3.2 (shape verbal) | `tiempos_y_verbos` poblado con `{lema, tiempo, formas_trabajadas}` literal del libro (con mayúscula inicial). |
| schema §5 (taxonomía 20 tipos) y §5b/§5c | Asignación de `tipo`, `destreza` (orden alfabético) y `enfoque` en cada actividad. |
| schema §5d (enum tiempo incluye `Infinitivo`) | Usado para `hablar` en cuadro@p46 y casos como `tomar`, `comprar` en infinitivo (p50-act3). |
| schema §6 | Bloque `autoevaluacion` con `instruccion_original`, opciones canónicas NC1 y `emoticonos: true`. |
| schema §7 (5 valores de `tipo_cuadro`) | Cuadros @p44 y @p45 → `gramatical`; cuadro @p46 (Pronunciación y ortografía) → `pronunciacion_ortografia`. |
| schema §8 (7 valores de `seccion`) | Mapeo p42-43 → vocabulario, p44-45 → gramatica, p46-47 → comunicacion, p48-49 → destrezas, p50 → cultura, p51 → evaluacion. |
| schema §9.1 (shape `principal`/`recurrente`, `items` con `palabra`/`fuentes`, `descripcion` por unidad) | Estructura de los 4 bloques consolidados. |
| schema §9.2 (lista plana de lemas con `rasgo_por_tiempo`, `formas_trabajadas`, `fuentes`, `descripcion`) | `tiempos_y_verbos_consolidado` poblado en minúscula (§5.11). |
| schema §9.5 (regex `^(p\d+-act\d+(@R)?\|cuadro@p\d+(#\d+)?)$`) | Aplicación del sufijo `@R` en respuestas de actividades productivas. |
| schema §10 (audio/imagen/video siempre presentes; `imagen.descripcion` obligatoria si presente=true) | Cada actividad lleva los tres sub-objetos; toda imagen con `presente=true` lleva descripción. |
| schema §11 + §A.5 (claves `_fixture_*` extracontractuales; unidad string `"4p"`) | Cabecera de la fixture. |
| schema §14 (marcas internas declaradas) | Uso de `_pendiente_canon`, `_funcion_ambigua` (p43-act7) y `_decisiones_ia` top-level. |
| reglas-op. §1 (precedencia actividad/cuadro/nota) | Cuadros @p44, @p45, @p46 clasificados como `cuadro`; act9 "Para aprender" de p45 → actividad porque pide producción ("Organiza", "Añade"). |
| reglas-op. §2 (tipo = última acción que pide producción) | Decisión `tipo` en cada actividad: p43-act5 ("Escucha y completa") → `completa_huecos` (manipulación manda sobre input). |
| reglas-op. §2.3 (destreza vs enfoque) | p43-act6 → enfoque `transversal` (comprensión lectora genérica, no copia del enfoque editorial); p48-act1/act2/act3 → `transversal` por antipatrón disparador U5-p60. |
| reglas-op. §2.5 (texto_completo vs dialogo_completo) | p43-act5 y p46-act1: diálogos con turnos → `dialogo_completo`. p48-act2 (texto seguido "Comer en España") → `texto_completo`. |
| reglas-op. §4 ("Para aprender" / "Observa") | p45-act9 con verbo imperativo → actividad subtipo `para_aprender`. |
| reglas-op. §5.6 (canon semántico) | "Alimentos" y "Comidas preparadas" tomados literalmente del canon (origen `indice`). Envases sin canónico → `_pendiente_canon`. |
| reglas-op. §5.10 (verbos: soporte cuenta igual que paradigma trabajado) | Cuadro @p45#1 (Hay) registra formas `["hay"]`; act1 de p42 no añade verbos (es solo léxico ilustrado). p43-act4 registra `hay/Hay/No hay` aunque el foco editorial sea léxico. |
| reglas-op. §5.11 (literalidad en actividad/cuadro; minúscula en consolidado) | Actividad guarda `"Quiero"`, `"Hay"`; consolidado guarda `"quiero"`, `"hay"`. |
| reglas-op. §5.12.A (barrido léxico) | Recorrido por todos los `datos.*` de cada actividad para alimentar `vocabulario_consolidado`. |
| reglas-op. §5.12.B (barrido gramatical) | Detección de artículos, interrogativos, negación, pronombres OI, pronombres tónicos en cada actividad. |
| reglas-op. §5.12.C (barrido pron-ortográfico) | Cuadro @p46 + p46-act10/11/12 → única dimensión productiva en pron-ortografía; el resto, vacío declarado. |
| reglas-op. §5.13 (propuesta-en-chat) | Aplicada como `_decisiones_ia` en fixture (corrida sin autor presente); cada decisión no clara registrada. |
| reglas-op. §5.14 (recurrente = propuesta+decisión) | Categorías de `recurrente` propuestas explícitamente con justificación, no inferidas silenciosamente. |

---

## 3. Propuestas-en-chat y decisiones provisionales asumidas

Esta corrida sucede sin autor presente. Cada propuesta queda registrada en `_decisiones_ia` (top-level) del JSON y aquí justificada.

| # | Contexto | Propuesta | Decisión provisional |
|---|---|---|---|
| 1 | Cuadro @p45 contiene dos paradigmas distintos (Hay + Verbo querer). | (a) Un solo cuadro; (b) Dos cuadros `#1` y `#2` por categoría. | (b). Dos cuadros lógicos (cuadro@p45#1 = Hay, cuadro@p45#2 = querer). Idem cuadro@p44#1/#2/#3. |
| 2 | p43-act7 (tabla 4 filas «Me gusta mucho / Me gusta / No me gusta / No como nunca»). | (a) `completa_huecos`; (b) `produccion_escrita_guiada`. | (b) + `_funcion_ambigua: true`. La tabla no tiene huecos en frase; el alumno produce léxico propio. |
| 3 | Léxico de envases (botella/cartón/bolsa/vaso/lata/paquete/taza/bote/trozo, p46-act5/6). Sin canónico semántico. | (a) Crear `Envases y recipientes` con origen pcic_a1; (b) marcar `_pendiente_canon`; (c) forzar a `Alimentos`. | (b) + propuesta canónica (a). |
| 4 | `/r/` vs `/rr/` (cuadro@p46 + actividades 10-12). Sin registry pron-ortografía operativo. | (a) Crear categoría `Vibrante simple /r/ vs vibrante múltiple /rr/`; (b) `_pendiente_canon`. | (b) + propuesta canónica (a). |
| 5 | Verbos sin entrada en `verbos-canonicos.json`: `beber`, `tomar`, `haber` (existencial `hay`), `costar`, `pedir`, `elegir`, `vender`, `comprar`, `conocer`. | (a) Añadir cada uno al registry; (b) marcar `_pendiente_canon` en consolidado. | (b) para todos. En particular `haber` es decisión arquitectónica (lema o categoría aparte). |
| 6 | p44 cuadro `Verbo gustar`: formas conjugadas presentadas (`gusta`, `gustan`). ¿Se registran como `tiempos_y_verbos` del cuadro o solo en `gramatica`? | Aplicar §5.10 estrictamente: las formas aparecen → entran. | Aplicada. El cuadro registra `gustar` con `["gusta","gustan"]`. |
| 7 | p44-act3 (interrogativas con `tú/ella/ustedes`). ¿Son recurrente gramatical o solo soporte? | (a) Recurrente (canónico en U1); (b) ignorar. | (a). Entra a `gramatica_consolidada.recurrente → Pronombre sujeto / pronombres tónicos`. |
| 8 | p49-act5 (dictado-reconstrucción de preguntas y respuestas). | (a) destreza `comprension_auditiva` sola (transcripción); (b) añadir `expresion_escrita` porque el alumno reconstruye texto. | (b) provisional. Frontera con la regla 5.2.3 (`expresion_escrita` no se asigna en transcripción pura). |
| 9 | p42-act1 (Escucha y repite con 18 alimentos). Asignación `enfoque`. | (a) `vocabulario` (campo léxico); (b) `pronunciacion_ortografia` (escucha y repite). | (a) por heurística de §2.3 (palabras agrupadas por campo léxico → vocabulario). |
| 10 | "Anticipaciones detectadas para fase 2": ningún léxico de U4 es canónico de unidad posterior con clara probabilidad. | Lista vacía. | Registrada como `hallazgos.anticipaciones_detectadas_para_fase_2: []`. |

---

## 4. Trazado del procedimiento §5.12 A/B/C (barrido por dimensión)

Para cada dimensión susceptible de `recurrente`, se aplicó el procedimiento de 8 pasos. Aunque alguna pasada termine en lista vacía, el barrido se ejecutó.

### 4.1 Léxico — §5.12.A

1. **Foco principal:** Alimentos + Comidas preparadas + (propuesto) Envases y recipientes.
2. **Verbos:** identificados aparte (rama propia).
3. **Barrido verbatim:** se recorrió `items_libro`, `texto_completo`, `dialogo_completo`, `preguntas`, `palabras_recuadro`, `ejemplos_modelo` de las 49 actividades + 6 cuadros.
4. **Cruce contra registries y curso:**
   - `campos-semanticos-canonicos.json` → 98 categorías inspeccionadas; `Familia` (U3), `Colores` (U1), `Establecimientos` (U2), `Objetos de clase` (U1), `Días/momentos del día` (U3) candidatos.
   - `nc1-curso.json` → revisado `vocabulario[]` de U0–U9 (familia, profesiones, objetos de clase, lugares, comida, etc.).
   - `pcic-a1-vocabulario.json` consultado para nomenclatura.
5. **Matches encontrados (no omitidos por sesgo):**
   - `Familia`: hermano, hermana, padres, madre, niños, amigos, compañero (pp. 44-51). Canónico en U3 → entra como recurrente.
   - `Colores`: rojas/amarillas/verdes (p42), azul (p47), negro (p51). Canónico en U1 → entra.
   - `Objetos de clase`: no aparece léxico léxicamente significativo (solo "nevera", "frigorífico", "mesa" como soporte) → NO entra (input incidental, antipatrón §5.13 follow-up).
   - `Establecimientos`: "restaurante" aparece muchas veces. Canónico en U2. Sin embargo, aquí "restaurante" se trabaja como contexto situacional, no como léxico nuclear del U2 → discutible; decisión provisional: NO entra como recurrente (es input incidental temático).
   - `Días/momentos del día`: "mediodía", "desayuno", "comida", "merienda", "cena" (p48-49). Estos son léxico de unidad posterior (U5/U7?) según `nc1-curso.json` → revisar para anticipación. Sin entrada clara en curso, se omite por ahora.
6. **3 criterios aplicados:** frecuencia agregada, posición canónica anterior, valor pedagógico.
7. **Candidatos surgidos:** Familia y Colores (entran). Establecimientos y momentos del día (no, input incidental).
8. **Decisión:** aplicada al JSON con justificación en `descripcion`.

### 4.2 Gramática — §5.12.B

1. **Foco principal:** Verbo gustar, Artículos indeterminados, Nombres contables e incontables, Hay, Verbo querer.
2. Verbos → rama propia.
3. **Barrido:** detección de marcadores morfológicos y estructuras en cada actividad.
4. **Cruce:**
   - `gramatica-canonica.json` (esqueleto, sin entradas operativas).
   - `nc1-curso.json` → U1 trae artículos determinados, género/número, pronombres, interrogativos; U2/U3 trae demostrativos, posesivos.
   - `pcic-a1-gramatica.json` consultado para naming.
5. **Matches:**
   - **Artículos determinados** (el/la/los/las): canónicos en U1, reaparecen masivamente en U4 como elemento obligatorio del sujeto pospuesto de gustar. ENTRA.
   - **Pronombres sujeto/tónicos** (yo, tú, él/ella; a mí, a ti...): canónicos en U1, soporte sintáctico de gustar y querer. ENTRA.
   - **Negación (no + verbo)**: canónica en U1, omnipresente. ENTRA.
   - **Interrogativos**: canónicos en U1, alta frecuencia en U4 (p43, p44, p48-50). ENTRA.
   - **Demostrativos** (este/esa...): apenas presentes ("esta fruta", "este plato"). Frecuencia baja, sin foco. NO ENTRA.
   - **Posesivos** (mi/tu/su, mis, vuestra...): aparición moderada (p44-act1 "mi hermano", "mis padres", "mi hermana", "vuestra comida favorita"). Canónicos en U3. Decisión provisional: NO ENTRA por falta de foco; revisable si autor decide subir el umbral.
6. **Criterios:** todos los 4 que entran cumplen frecuencia, posición y valor pedagógico (consolidación bajo nuevo paradigma de gustar).
7. **Candidatos surgidos:** los 4 listados arriba.
8. **Decisión:** aplicada.

### 4.3 Pronunciación / ortografía — §5.12.C

1. **Foco principal:** /r/ vs /rr/ (cuadro@p46 + act10/11/12). Marcado con `_pendiente_canon` por falta de registry operativo.
2. Verbos → rama propia (no aplica).
3. **Barrido:** inspeccionadas convenciones tipográficas (sílaba tónica subrayada, transcripciones), tipos de actividad (`escucha_y_repite`, dictado), cuadros con `tipo_cuadro: pronunciacion_ortografia`.
4. **Cruce:**
   - `pronunciacion-ortografia-canonica.json` (esqueleto).
   - `nc1-curso.json` → U1 "Nombres de las letras", U2/U3 con fenómenos. No se observa /r/-/rr/ en otras unidades.
   - `pcic-a1-pronunciacion-ortografia.json` consultado.
5. **Matches:**
   - El abecedario / nombres de letras (canónico en U1) NO aparece en U4 → NO entra.
   - El sonido /r/-/rr/ es exclusivo de U4 → entra al PRINCIPAL como `_pendiente_canon`.
   - No hay nada más explícitamente marcado.
6. **Criterios:** —
7. **Candidatos a recurrente:** ninguno.
8. **Decisión:** `pronunciacion_ortografia_consolidada.recurrente` queda explícitamente como `{}` (lista vacía declarada, no omitida). El barrido se hizo.

---

## 5. Aplicaciones del sufijo `@R`

Lista de fuentes con `@R` y tipo productivo asociado (los 6 tipos canónicos del Apéndice §A.3):

| Fuente | Tipo de actividad | Justificación |
|---|---|---|
| `p44-cuadro@p44#1@R` | — (no aplica @R a cuadros por schema §9.5) | **Bug detectado en mi propio JSON.** Los cuadros NO admiten `@R`. Limpieza pendiente: estas referencias deben re-etiquetarse al nivel de actividad fuente o eliminarse. Anotado como pendiente. |
| `p45-act3@R` (arroz a la cubana, arroz con tomate) | `completa_huecos` (NO productivo) | **Reviso: act3 de p45 no existe en mi JSON; era confusión con p44-act3.** En p44-act3 `produccion_escrita_guiada` aplica @R. Corrección documentada. |
| `p44-act3@R` (peras) | `produccion_escrita_guiada` | Producción del alumno: "A Javier no le gustan las peras". |
| `p45-act7@R` (agua) | `seleccion_multiple` (NO productivo) | **No debería llevar @R.** Bug pendiente. |
| `p46-act6@R` (tarta, pan, frutos secos) | `produccion_escrita_guiada` | Producción del alumno al asociar envase+producto. |
| `p47-act6@R` (hamburguesa, hamburguesas, patatas) | `interaccion_oral` | Producción oral del alumno. Tipo productivo válido. |
| `p47-act7@R` (ensalada, arroz) | `escucha_y_repite` (NO productivo) | **Bug.** A retirar. |
| `p47-act8@R` (manzanas, galletas) | `interaccion_oral` | OK. |
| `p47-act9@R` (naranjas) | `expresion_oral_libre` | OK. Tipo productivo. |
| `p49-act5@R` (atún, manzanas, agua, atún con tomate) | `completa_huecos` (NO productivo) | **Bug.** A retirar (aunque la actividad implica reconstruir, su tipo formal no está en los 6 productivos del schema). |
| `p49-act8@R` (carne) | `interaccion_oral` | OK. |
| `p49-act9@R` (pollo) | `interaccion_oral` | OK. |

> **Hallazgo de fixture:** el sufijo `@R` aplicado mecánicamente al "lo que el alumno escribe/dice" sin antes verificar que el tipo está en la lista de los 6 productivos del schema §9.5 produce un porcentaje no despreciable de marcas erróneas. **Propuesta al autor:** explicitar el chequeo previo del tipo de actividad en `reglas-operativas.md` cuando se migre la regla, y considerar añadir un validador estructural que rechace @R en tipos no productivos. Estos errores se han **dejado en la fixture intencionalmente** como evidencia para discusión, marcados aquí.

---

## 6. Marcas resultantes con justificación

### 6.1 `_pendiente_canon`

| Ubicación | Forma | Justificación |
|---|---|---|
| `vocabulario_consolidado.principal._pendiente_canon` | clave en sub-bloque | Léxico de envases sin categoría canónica. Propuesta tentativa: "Envases y recipientes" (origen pcic_a1, PCIC §3.2). |
| `pronunciacion_ortografia_consolidada.principal._pendiente_canon` | clave en sub-bloque | Fenómeno /r/ vs /rr/ sin categoría en `pronunciacion-ortografia-canonica.json`. Propuesta: "Vibrante simple /r/ vs vibrante múltiple /rr/". |
| `tiempos_y_verbos_consolidado[].lema = "_pendiente_canon"` | valor del campo | Lemas no presentes en `verbos-canonicos.json`: `beber`, `tomar`, `haber` (existencial). Cada uno con `_propuesta_lema` y `descripcion` justificada. |
| En `actividad.tiempos_y_verbos[].lema = "_pendiente_canon"` | valor del campo | Mismo motivo, replicado en actividades donde aparecen formas conjugadas de estos lemas (p43-act5, p43-act4, p45-act6/7/8, p46-act1/2/3, p48-act1/2/3, p49-act4/5, p50-act3/4, p51-act1/3). |
| `cuadro@p46.pronunciacion_ortografia = ["_pendiente_canon"]` | string en lista | El fenómeno como referencia canónica aún no canonizada. |

### 6.2 `_funcion_ambigua`

| Ubicación | Justificación |
|---|---|
| `U4-p43-act7` | Frontera entre `completa_huecos` y `produccion_escrita_guiada`. La tabla pide producir contenido propio en casillas predefinidas (no hueco en frase). Decisión asumida: `produccion_escrita_guiada`. Se escala al autor para confirmar. |

### 6.3 `_decisiones_ia` (top-level)

Lista de 10 decisiones registradas en el JSON con detalle suficiente para auditoría. Resumen en §3 de este informe.

---

## 7. Resumen final

- **Páginas extraídas:** 10 (42-51).
- **Actividades:** 49.
- **Cuadros:** 6 (4 gramaticales en pp. 44-45, 1 de pronunciación en p46, ningún cultural).
- **Cabecera coincidente con `nc1-curso.json`:** sí (titulo, paginas_libro, contenidos_indice). Adaptado a la cadena `"4p"` como `unidad` por ser fixture.
- **Bloque `autoevaluacion`:** presente con valores canónicos NC1.
- **Marcas bloqueantes a resolver antes de cierre:** `_pendiente_canon` (5 ubicaciones con propuestas en chat) + `_funcion_ambigua` (1 ubicación, p43-act7).
- **Marcas `@R` con bug detectado:** 5 fuentes (cuadros con @R + tipos no productivos con @R). Dejadas intencionalmente como hallazgo de fixture.
- **`hallazgos.anticipaciones_detectadas_para_fase_2`:** lista vacía (nada en U4 se anticipa claramente a una unidad posterior según el cruce con `nc1-curso.json`).
- **Validación manual contra schema:** OK (top-level completo, 4 listas tipadas siempre presentes en cada actividad y cuadro, 4 bloques consolidados derivados de las listas, regex de fuentes respetada salvo los @R con bug, enumeraciones cerradas respetadas).
