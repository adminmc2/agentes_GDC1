# Changelog — Guía Didáctica del Profesor (IA)
## Sistema de Agentes v5.0 — Nuevo Compañeros 1

> **Rol de este archivo:** registro cronológico de qué cambió. **NO es autoridad operativa** — la autoridad de cómo actuar es `CLAUDE.md`. Si una entrada antigua contradice a `CLAUDE.md`, manda `CLAUDE.md`.
>
> **Regla editorial:** entradas nuevas **cortas y operativas** (2-4 líneas: qué cambió + por qué + archivos). El detalle extenso de versiones antiguas ya está resuelto; no se replica ni se reescribe.
>
> **Histórico archivado** (consulta puntual, no relectura):
>
> | Rango | Archivo | Contenido |
> |---|---|---|
> | pre-v10.40 | `docs/historico/CHANGELOG-pre-refactor.md` | Sistema anterior al refactor |
> | v10.40–v10.164 | `docs/historico/CHANGELOG-fase1-cierre-y-fase2-paralela.md` | Cierre de fase 1 (U0-U9) + trabajo paralelo de fase 2 |
> | v11.0+ | este archivo | Post-fase 1: infraestructura, dashboard, deuda matcher |

---

## [v12.111 — 2026-08-24] — Retro FEEDBACK→REVISIÓN FOCALIZADA descartada por el autor

Decisión del autor: las unidades cerradas U2-U7 no se reabren — conservan el rótulo *FEEDBACK FOCALIZADO* en sus Evaluaciones (U3 no lo usa); *REVISIÓN FOCALIZADA* rige de U8 en adelante. Cierra el pendiente abierto en v12.105. Sin cambios en archivos editoriales; el manual no codifica este rótulo.

## [v12.110 — 2026-08-24] — Estilo de itinerarios §5 codificado + fila del paseo-galería en repo B

Criterio del autor (sesión U8, aplicado en v12.107) codificado como fuente única en `docs/estilo-itinerarios.md` §5: máximo 4 materiales complementarios por sección del extendido; el excedente se reubica por contenido, no se recorta. En repo B, aplicada la fila §1 pendiente desde v12.105: paseo-galería de los monstruos de U8 Evaluación (variante en mesas del Gallery Walk #61, precedente U4D; commit `16ec205` de repo B).

## [v12.109 — 2026-08-24] — U5: `video2.png` commiteado como depósito pendiente de identificar

Fotograma de un chico guardando la mochila en su habitación, depositado en `unidades/U5/recursos/` desde v12.96 sin identificar (la fila de vídeo de U5 ya está cubierta por `videou5.png`). Entra al repo como material depositado; identificación y fila del itinerario pendientes de aclarar con el autor.

## [v12.108 — 2026-08-23] — U8: fotograma del vídeo de Comunicación depositado

`vid8.png` (los dos amigos conversando en el patio del instituto) depositado en `recursos/` e incorporado a la tabla del diseñador de `U8-itinerarios.md` con la fórmula U6/U7: se resuelve el «pendiente de depósito» del fotograma; título y enlace del vídeo siguen por verificar (la nota *Buscar Vídeo* de `final/comunicacion.md` sigue viva).

## [v12.107 — 2026-08-23] — U8 itinerario: tope de 4 materiales por sección en el extendido

Regla nueva del autor: máximo 4 materiales complementarios por sección. Comunicación tenía 6 → *Actividades Extra 8 Descripciones* pasa a Vocabulario (Ejercicios 6-8; su objetivo impreso es el vocabulario del cuerpo y la descripción de personas) y *Gamificación El mentiroso* pasa a Destrezas (Ejercicio 7; misma mecánica que la adivinanza de famosos). Queda V 4 · G 2 · C 4 · D 3 · Cu+E 1; tablas del diseñador reordenadas (`unidades/U8/U8-itinerarios.md`).

## [v12.106 — 2026-08-23] — U8: itinerario redactado

`unidades/U8/U8-itinerarios.md` nuevo, derivado de los seis `final/` + inventario, patrón U7 y `docs/estilo-itinerarios.md`: básico con 15 bloques [CLASE] + 4 [CASA] (reparto acordado con el autor: V 3-4 en par, G 3, C 4, D 5; Cultura entera en aula), las 8 pistas 83-90 asignadas y las píldoras 8.1/8.2 marcadas con su nombre real. Estación de servicio verificada contra CSVs (Caja 1: 56 = 23+24+9; Caja 2: `1 {comunicación} + 1 {mediación}`, precedente U3); extendido con los materiales SGEL de `recursos/` mapeados con página exacta para el diseñador (*Twister* pp. 42-43 y *El mentiroso* pp. 44-45 del cuaderno; la Actividad global 2 queda en U9). Pendientes de depósito: fotograma del vídeo de Comunicación y PPTX de unidad (solo captura). Materiales depositados en el commit.

## [v12.105 — 2026-08-23] — U8: Evaluación derivada a `final/` — U8 completa

Sexta y última sección de U8 en la capa final (943 palabras): siete ejercicios de la página 91 en dos versiones canónicas A/B, objetivo Dirección B (*Consolidar los contenidos trabajados en la unidad*). Caen las **pizarras individuales** (→ escritura en la pizarra del aula por personas voluntarias), la **tarjeta-abanico** (Evaluación no añade material → clave proyectada) y el recap de insignias; rótulo **REVISIÓN FOCALIZADA** sustituye al anglicismo *FEEDBACK FOCALIZADO* (retro U2-U7 pendiente); conexión a la **unidad 9** verificada (ropa + primeros indefinidos de *ir* y *estar*). Auditoría /check-final: **13 ✅ / 2 ⚠ / 0 ❌** (`unidades/U8/final/evaluacion.md`).

## [v12.104 — 2026-08-23] — Manual §2.1 Cultura invertida, /check-final sincronizado y ajuste de U8C

La regla §2.1 *Cultura — bloque único sin objetivo propio* se **invierte** a *Cultura — bloque único con objetivo propio en grano distinto* (decisión del autor: un objetivo específico igual o casi igual al general no sirve; retro-derivación de U1C-U7C **pendiente**), con el checklist de `/check-final` sincronizado en el mismo lote. Auditoría de U8C: **14 ✅ / 1 ⚠ / 0 ❌** — las dos candidatas §10.6 (síntesis-ancla en pizarra) se mantienen por decisión del autor y la entrega alinea *hecho hipótesis* con la obtención (`docs/manual-estilo-final.md`, `.claude/skills/check-final/SKILL.md`, `unidades/U8/final/cultura.md`).

## [v12.103 — 2026-08-23] — U8: Cultura derivada a `final/`

Quinta y última sección lingüística de U8 en la capa final (748 palabras): dos ejercicios de la página 90 en bloque único, ficha 8.6 e insignia renombrada **¡MENUDO PLANAZO!** (cae *azul* por catalogar el elemento vehículo). Decisiones del autor: objetivo general **Contrastar la semana azul como modelo de viaje escolar con la experiencia del propio centro**, **objetivo de bloque propio** (**Formular un plan sencillo de viaje escolar**) — contradice §2.1 del manual, actualización de la regla y retro U1C-U7C **pendientes** — y rótulo **COORDINE LA COMPRENSIÓN DETALLADA DEL TEXTO** en lugar del de la propuesta. Registro §4/§4bis/§6 de repo B alineado (`unidades/U8/final/cultura.md`).

## [v12.102 — 2026-08-23] — U8: Destrezas derivada a `final/`

Cuarta sección de U8 en la capa final (1397 palabras): 9 ejercicios de las páginas 88-89 en tres bloques, **pista 90** en el ejercicio 6, tarjeta nueva de **mediación oral *Cuenta cómo es*** (primera del corpus), píldora 8.2 renombrada **Escuchar la descripción de una persona** y ficha 8.5. Las **parejas espejo con cambio de pareja** sustituyen al trío mediador de la propuesta; los cuatro objetivos re-derivados con el autor. Registro §1/§3 de repo B alineado (`unidades/U8/final/destrezas.md`).

## [v12.101 — 2026-08-22] — U8 Comunicación: objetivo del bloque 3 y escucha del ejercicio 7 corregidos por el autor

Dos correcciones sobre v12.100: el objetivo del bloque 3 pasa a **Describir a un familiar de otra persona** (*retratar… a partir de sus respuestas* nombraba actividad con coletilla de medios); la explotación del **ejercicio 7** sustituye la predicción de colores sin contexto por la tabla como guía de escucha — leer las casillas antes de oír, dos escuchas (captar → completar y comprobar), cotejo en parejas y reposición solo sobre desacuerdos. 1293 palabras (`unidades/U8/final/comunicacion.md`).

## [v12.100 — 2026-08-21] — U8 Comunicación: comprobación del ejercicio 4 rediseñada por el autor

Corrección sobre v12.99: cada estudiante resuelve el **ejercicio 4** solo y la comprobación es el emparejamiento de contrarios — se mezclan los mazos *Características físicas* y *Carácter y personalidad* completos y se reparten todas las tarjetas (quien recibe dos juega las dos); las parejas formadas comprueban el ejercicio y los adjetivos sin contrario se constatan al final. Verificado contra los CSV: las 16 palabras del ejercicio están en las tarjetas (12 físicas + 4 de carácter). 1310 palabras. Registro de repo B alineado (`unidades/U8/final/comunicacion.md`).

## [v12.99 — 2026-08-21] — U8: Comunicación derivada a `final/`

Tercera sección de U8 en `final/` (`unidades/U8/final/comunicacion.md`, 1269 palabras, 0 bloqueadores en /check-final): los 12 ejercicios de las páginas 86-87 en cuatro bloques, las cuatro pistas (86-89) en su ejercicio exacto, línea canónica de vídeo (pista 86 si no hay proyector) y tarjeta de estrategia *Describir a una persona* (interacción oral). Objetivo general fijado por el autor (*Describir a una persona conocida combinando su físico y su carácter*); bloque 1 reformulado a objetivo de procesamiento (*Identificar en un diálogo los datos que describen a una persona*) tras descartar *representar la adivinanza* por nombrar actividad y no aprendizaje. El *duelo de opuestos* de la propuesta cae por aritmética de reparto y entra el **emparejamiento de contrarios con tarjetas** (diseño del autor: el ejercicio se resuelve solo; la comprobación es la actividad). Ficha nueva **8.4 — Tarjetas de retratos** (`unidades/U8/recursos/ficha-8.4-tarjetas-retratos.md`) para la dinámica del vídeo; insignias de Destrezas y Cultura renumeradas a 8.5/8.6 en el registro de repo B.

## [v12.98 — 2026-08-21] — U8: Gramática derivada a `final/`

Segunda sección de U8 en `final/` (`unidades/U8/final/gramatica.md`, 1410 palabras, 0 bloqueadores en /check-final): los 8 ejercicios de las páginas 84-85 en cuatro bloques, con los tres cuadros integrados y sin pistas de audio (la sección no tiene). Objetivo general reformulado con el autor tras descartar el de la propuesta (*construir frases con gustar y doler*: `gustar` es reciclaje de U4, no contenido de U8) — queda **conjugar doler con sus pronombres átonos y graduar la frase con los adverbios de cantidad**, con el objetivo del tercer bloque alineado (*graduar con muy los adjetivos y adverbios, y con mucho/-a/-os/-as los nombres y verbos*). Píldora 8.1 titulada **Muy y mucho** por decisión del autor; las tres alternativas de autoría siguen en la propuesta. Etiqueta *de objeto indirecto* fuera de los objetivos y pasada de redacción sobre toda la sección.

## [v12.97 — 2026-08-20] — U8: Vocabulario derivado a `final/`

Primera sección de U8 en `final/` (`unidades/U8/final/vocabulario.md`, 910 palabras, 0 bloqueadores en /check-final): derivación de la propuesta con rediseño en sesión con el autor de toda la capa de tarjetas — adivinanza por imagen con intercambio entre parejas (ejercicio 1) y *Simón dice* opcional (ejercicio 2, `dinamicas-101` #54) sustituyen a cognados, combinatoria de tres mazos y especialistas, inviables por depender del número de estudiantes; insignia 8.1 renombrada **¡DE PIES A CABEZA!**. Registro de repo B actualizado (§1 + tablas de insignias); newline final añadido a `partes-del-cuerpo.csv` (precedente v12.94).

## [v12.96 — 2026-08-18] — U7: fotogramas de los dos vídeos depositados

`video1.png` (conversación telefónica de Pablo y Jorge — vídeo de sección de Comunicación) y `video2.png` (desayuno de Marcos con su padre — vídeo final *La vida de Marcos*) depositados en `recursos/` e incorporados a la tabla del diseñador de `U7-itinerarios.md`: se resuelve el «pendiente de depósito» de Comunicación y el fotograma sustituye a la cabecera del PDF como imagen de maqueta del vídeo final. El `video2.png` de U5 queda fuera hasta aclarar a qué corresponde.

## [v12.95 — 2026-08-18] — U7: itinerario revisado con el autor

Segunda pasada sobre `U7-itinerarios.md` con decisiones del autor: un [CASA] por sección (V6, G3, C7, D3), retoques de redacción en títulos y descripciones, píldoras con su nombre real y Caja 2 en `1 {comunicación} + 1 {expresión oral}`. Criterio nuevo codificado en `docs/estilo-itinerarios.md` §4: la expresión oral se cuenta aparte en Caja 2 (deroga el cruce IO↔EO de la plantilla congelada). La Actividad global 2 (cuaderno pp. 49-55) queda para el itinerario de U9, precedente de la global 1 en U5.

## [v12.94 — 2026-08-17] — U7: itinerario redactado

`unidades/U7/U7-itinerarios.md` nuevo: básico con 18 bloques [CLASE] y 7 [CASA] (10 ejercicios, reparto revisado con el autor), las 11 pistas 72-82 asignadas y las píldoras 7.1/7.2 marcadas; extendido con estación de servicio (29 {animales} + 2 {comunicación}) y los materiales SGEL de `recursos/` mapeados con página exacta para el diseñador. Dos vídeos distinguidos: el de sección de Comunicación (fijo, pendiente de depósito) y el vídeo final *La vida de Marcos* (U6-7) en Cultura y Evaluación. Materiales depositados en el commit y newline final añadido a `tarjetas/animales.csv` (cierra el falso recuento 28/29).

## [v12.93 — 2026-08-17] — §2.1: la excepción de Cultura, codificada

Subsección nueva *Cultura — bloque único sin objetivo propio* en `docs/manual-estilo-final.md` §2.1: Cultura ocupa una sola página, se resuelve en un solo bloque y su header va seguido directamente del primer rótulo. Codifica un patrón unánime del corpus (U1C-U7C: 1 header y 1 objetivo, frente a N y N+1 en las secciones de varios bloques) que `/check-final` marcaba como ⚠ por no estar escrito. Checklist del skill sincronizado en el mismo lote. Commit propio de manual (§11.3), sin contenido editorial.

## [v12.92 — 2026-08-17] — Cierre de los avisos de `/check-final` sobre U7 Cultura y Evaluación

Auditoría de las dos secciones: 0 bloqueadores. Resueltos los cuatro avisos accionables — desespecificadas en Cultura la serie de preguntas-modelo y el mapeo cerrado pregunta→léxico (§10.1, mismo criterio que el autor aplicó en Evaluación), y en Evaluación sustituidas la predicción de error del ejercicio 1 y la enumeración sin criterio del ejercicio 2. Cultura 736 palabras, Evaluación 942. Registro §1 de repo B alineado. Detalle en la bitácora de REVIEW.

## [v12.91 — 2026-08-17] — U7 Evaluación en `final/`: **U7 completa**

`unidades/U7/final/evaluacion.md` nuevo (941 palabras, techo ≤950), sexta y última sección de U7. 6/6 ejercicios de la página 81 contra inventario y PDF. **Pizarras individuales y cuaderno en alto quedan prohibidos** como modo de corrección (decisión del autor, aplica a todo el corpus): el ejercicio 1 pasa a cadena oral. Corregidos dos errores de la propuesta y desespecificados tres focos que predecían dudas en vez de nombrar rasgos. Detalle en la bitácora de REVIEW.

## [v12.90 — 2026-08-16] — Errata de imagen del inventario de U7 corregida

`U7-p80-act01.imagen.descripcion` decia *«Fotografias de delfines en espectaculo acuatico, flamingos y cabras»*; la pagina 80 trae **una sola foto** de delfines y ninguna de flamencos ni de cabras (verificado contra el PDF al derivar U7 Cultura, v12.89). Reescrita con el formato de recuento de las demas entradas de U7. `validar_inventario.py 7` limpio.

## [v12.89 — 2026-08-16] — U7 Cultura en `final/`

`unidades/U7/final/cultura.md` nuevo (766 palabras, techo ≤800), quinta sección de `final/` de U7: 2/2 ejercicios de la página 80 y la pista 82 contra inventario. Foto verificada contra el PDF: **una sola foto de delfines**, sin flamencos ni cabras — el inventario está equivocado (deuda abierta). Mecánica de lectura sustituida por elección justificada con recuento, porque el reparto por partes repetía el jigsaw de U3 Cultura y no escala a 10+ parejas. Detalle en la bitácora de REVIEW.

## [v12.88 — 2026-08-15] — Cierre de las tres deudas abiertas antes de U7 Cultura

Rótulo huérfano del ejercicio 4 de `unidades/U7/final/comunicacion.md` corregido: *DÉ PASO A UNA RUEDA DE PREGUNTAS* → *DÉ PASO A LAS PREGUNTAS POR TURNOS EN PAREJAS* (la rueda se había sustituido en v12.86 por modelado + parejas). Deuda de transcripciones cerrada por verificación: ninguna frase de U7 Comunicación ni de U7 Destrezas afirma contenido sonoro no verificable — el diálogo de la pista 77 y las frases de la 79 están impresos en el inventario. Back-audit de dinámicas U1-U6 en `final/` completado (v12.84): 73 filas nuevas en `§1bis` del registro de repo B. Detalle en la bitácora de REVIEW.

## [v12.87 — 2026-08-13] — U7 Destrezas en `final/`

`unidades/U7/final/destrezas.md` nuevo (1375 palabras, techo ≤1400): 8/8 ejercicios de las páginas 78-79 y la pista 81 contra inventario (transcripción pendiente). Objetivos de los dos bloques receptivos con *identificar* —*reconocer* rechazado por presuponer conocimiento previo—; el del ejercicio 5 desespecificado a *«Identificar información concreta al escuchar una historia sencilla»*. Píldora 7.2 retitulada *Leer un texto descriptivo*. Las dos tarjetas se presentan por lo que se hace con ellas, sin jerga de cara ni de banco; «línea del día» sustituida por el día de Pedro en la pizarra. Registro de repo B: §3 con el título nuevo de P7.2 y §4 con las mayúsculas de la insignia 7.4. Detalle en la bitácora de REVIEW.

## [v12.86 — 2026-08-12] — U7 Comunicación en `final/`

`unidades/U7/final/comunicacion.md` nuevo (1419 palabras, techo ≤1450): 13/13 ejercicios y pistas 77-80 contra inventario (escuchas pendientes de transcripción). Bloque de entonación solo con ¿? / ¡! —fuera el punto y la declarativa de la propuesta; errata «audio 81» → pista 80—; ejercicio 3 profundizado (orden por bloques + autocorrección contra el diálogo); vídeo del ejercicio 10 remitido al Cuaderno de actividades (icono confirmado en PDF). Detalle en la bitácora de REVIEW.

## [v12.85 — 2026-08-10] — U7 Gramática en `final/` + figura del mapa de preposiciones

`unidades/U7/final/gramatica.md` nuevo (1392 palabras, techo ≤1600): 9/9 ejercicios y los tres cuadros de las páginas 74-75. Objetivo general con núcleo compuesto (verbos de la rutina + preposiciones, regla G1); presentación de los reflexivos rehecha por par contrastivo *Yo ducho a mi hermano / Yo me ducho* —fuera el espejo y toda mecánica corporal—; párrafo nuevo de regulares e irregulares anclado a la bota de la **unidad 6**; el mapa de preposiciones lo colocan los estudiantes y el cuadro lo confirma. `unidades/U7/recursos/mapa-dia-lucia.svg` y `.png` nuevos: representación del cuadro de la página 75 con figura, punto de referencia y trayectoria. Detalle en la bitácora de REVIEW.

## [v12.84 — 2026-08-09] — Registro de recursos declarado vivo pese al congelamiento de repo B

`CLAUDE.md`: excepción explícita al congelamiento — `unidades/registro-recursos.md` de repo B sigue siendo **registro vivo** (journaling de uso: consulta de no-repetición + actualización al cerrar cada sección de `final/`), codificada en el bullet de «Lo que NO se hace» y en la fila «repo B — capa pedagógica». Origen: incoherencia detectada en la sesión U7 Vocabulario. En repo B quedan registradas las tres dinámicas/reactivaciones de U7V `final/` y corregido §5 (meses = set no llevado al aula; animales 14→29). Detalle en la bitácora de REVIEW.

## [v12.83 — 2026-08-09] — U7 Vocabulario en `final/`: primera sección de U7, revisada frase a frase

`unidades/U7/final/vocabulario.md` nuevo (1484 palabras, techo ≤1500): derivado de la propuesta y revisado frase a frase por el autor; el ejercicio 4 se redacta contra la transcripción de la pista 73 (Día de la Madre sin número de día); las tarjetas de meses del año quedan fuera de la referencia por decisión del autor (el CSV se conserva); entran el fútbol de vocabulario (#51) y una adaptación en dos fases de *Conexiones misteriosas* (#10) con las tarjetas de animales, y se reutiliza la tarjeta de estrategia *Caza el dato*. Detalle en la bitácora de REVIEW.

## [v12.82 — 2026-08-08] — U5 Itinerarios: entran los 5 ejercicios de Blinklearning en el extendido

`unidades/U5/U5-itinerarios.md`: la línea «pendiente: ejercicios y capturas» se sustituye por los ejercicios reales, analizados y anclados — Vocabulario (Ej. 1, 2, 4: mobiliario, crucigrama de partes de la casa, correo de alojamientos) y Gramática (Ej. 3, 5: escucha de posiciones con marcadores y elección *ser/estar*); notas del diseñador actualizadas con las 7 capturas depositadas en `unidades/U5/recursos/` (renumeración de la tabla de Gramática). Detalle en la bitácora de REVIEW.

## [v12.81 — 2026-08-08] — Estilo de itinerarios codificado en `docs/`

`docs/estilo-itinerarios.md` nuevo (fuente única de los criterios de redacción de itinerarios post-congelamiento de repo B: descripción `[CLASE]` = acción global + ancla, sin detalle micro; tarjetas en títulos de bloque; `[CASA]` como tarea concreta) + fila nueva en la tabla de documentos clave de `CLAUDE.md`. Origen: criterio formulado por el autor durante la sesión U6 (v12.80).

## [v12.80 — 2026-08-08] — U6 Itinerarios: básico, estación de servicio y extendido con el material complementario analizado

`unidades/U6/U6-itinerarios.md` nuevo (patrón U5 v12.70): básico derivado de los seis `final/` con 5 bloques [CASA] acordados con el autor; estación de servicio verificada contra registro §5/§5bis y CSVs (Caja 1: 20 tarjetas; Caja 2: 2); extendido con los seis materiales depositados en `unidades/U6/recursos/` analizados uno a uno y anclados (tiempos de fuente en los dos juegos del cuaderno; el resto, estimaciones aprobadas). Novedad de curso: Proyecto WEB 2 *Un folleto turístico* (Unidades 4-6). Pendiente marcado: PPTX de unidad (solo captura); el fotograma del vídeo (`videou6.png`) entró durante el cierre. Entran también los archivos fuente depositados. Detalle en la bitácora de REVIEW.

## [v12.79 — 2026-08-08] — U6 Evaluación en `final/` + fila U6 de objetivos de Evaluación: entra el trabajo de la sesión paralela

`unidades/U6/final/evaluacion.md` (920 palabras, techo ≤950), redactada en sesión paralela, entra por orden del autor: Versión A (deberes y revisión con semáforo de comprensión) y Versión B (en clase), objetivo Dirección B *Consolidar los contenidos trabajados en la unidad* y conexión a la **unidad 7**. `docs/formulacion-objetivos.md`: fila U6 de la tabla ❌/✅ de §2.2 Evaluación al formato U5/U7 tras el rechazo del objetivo de evidencia. Con esto `unidades/U6/final/` queda completa (6/6 secciones). Detalle en la bitácora de REVIEW.

## [v12.78 — 2026-08-08] — U6 Cultura en `final/`: pre-enseñanza léxica con misión de detalle y cierre en el techo justo

`unidades/U6/final/cultura.md` (800 palabras, techo ≤800), derivada de `unidades/U6/propuesta/cultura.md` y revisada frase a frase con el autor. Página 70, 3 ejercicios, pista 71, insignia ficha 6.5 **¡UNA CIUDAD, MIL CARAS!**, sin tarjeta ni píldora. Cambios de fondo: la pre-enseñanza lineal del léxico pasa a primer vistazo + misión de detalle por tercios (adaptación de *El zoom cultural*, elegida por el autor entre tres alternativas de los bancos de repo B); la tarea del ejercicio 1 se declara con estrategia de apoyo tras descartar una falsa «pregunta guía»; el reciclaje se corrige contra inventario (sin *estar* ni colores: queda *ser* y *tener* con fechas y siglos). Retiradas autorizadas §10.6/§10.8/Patrón 7; P1 rechazada. Detalle en la bitácora de REVIEW.

## [v12.77 — 2026-08-06] — U6 Destrezas en `final/`: ejercicios 6 y 7 reescritos contra las transcripciones

`unidades/U6/final/destrezas.md` (1381 palabras, techo ≤1400), derivada de la propuesta y revisada frase a frase con el autor. Páginas 68-69, 11 ejercicios en tres bloques, pistas 69-70, insignia ficha 6.4 **¡MI LUGAR IDEAL!**, tarjeta nueva *Pregúntale al texto* (comprensión lectora), píldora 6.2 *Del plano al texto*. Cambios de fondo: la escucha de Daniela pasa a pregunta rectora con dos opciones de respuesta y corrección centrada en lo no literal (la trampa «cambia un dato de un lugar al otro» solo era cierta en 2 de 5 ítems); el ejercicio 7 se reescribe con la transcripción (todo se ejecuta en el cuaderno, órdenes en imperativo de tú con marcadores de lugar, la primera instrucción como base); el léxico nuevo del texto de Madrid se trabaja por deducción en contexto (patrón U5D); objetivo general nuevo (*Identificar información sobre otros lugares y describir el barrio de sus sueños*) y bloque final *en un texto breve*; rótulos al banco canónico (ORIENTE · DIRIJA · ORGANICE por CONTINÚE y GUÍE ×3). Detalle en la bitácora de REVIEW.

## [v12.76 — 2026-08-06] — U6 Vocabulario en `final/` + tarjetas de profesiones: entra el lote pendiente

`unidades/U6/final/vocabulario.md` (1470 palabras, techo ≤1500; pistas 64-66, insignia ficha 6.1 **¡MI BARRIO AL DETALLE!**, bloques 1-4 · 5-6 · 7-8), redactada en sesión previa, entra en el repo por decisión del autor. `unidades/U6/recursos/tarjetas/profesiones.csv`: combos de las diez tarjetas revisados — patrón *el/la + [profesión] + trabaja en + el/la + [lugar]* en todas, *hablar con + el/la + [profesión]* sustituye a *ir a…* en la mayoría y *querer ser + [profesión]* en PROFESOR, con ejemplos ajustados. `destrezas.md` (redactada hoy, pendiente de tres decisiones del autor) queda fuera del lote.

## [v12.75 — 2026-08-06] — U6 Comunicación en `final/`: el cuadro *Observa* pasa de línea de lectura a explicación de las cinco partes del día

`unidades/U6/final/comunicacion.md` (1450 palabras, techo ≤1450), derivada de `unidades/U6/propuesta/comunicacion.md`. Doble página 66-67, 10 ejercicios en cuatro bloques, pistas 67 y 68, cuadros *Observa* y *b = v*, insignia ficha 6.3 **¡QUEDAMOS!** y tarjeta de estrategia de Caja 2. Sesión larga, con el cuerpo revisado frase a frase por el autor.

**(1) El cuadro *Observa* explicado, no leído.** La propuesta lo despachaba con *«Lea con la clase el cuadro Observa, las cinco partes del día»*. Comprobado contra los inventarios U0-U6 que las franjas horarias son **contenido nuevo**: U3 enseña la hora (*es/son*, *y/menos*, *cuarto*, *media*) y no contiene ninguna ocurrencia de *de la mañana / de la tarde / de la noche / mediodía / madrugada*. Ahora el rótulo da la regla —la parte del día se añade detrás de la hora, en el formato de 12 horas, aunque los carteles la escriban en el de 24—, los cinco tramos del cuadro uno a uno, *del mediodía* como única forma con *del*, y el aviso de que esas horas son simplificación del aula: en español el corte lo marca la luz (DPD), y por eso el propio ejemplo del libro llama *las ocho y media de la tarde* a un cierre de las 20:30. La práctica del ejercicio 6 pasa a exigir la parte del día en la respuesta (*abre a las cinco de la tarde*), que es la operación real que el ejercicio pide y que ni el cuadro ni el enunciado explicitan.

**(2) Dos objetivos de bloque rehechos.** Ejercicios 1-3: *«Reconocer las tres preguntas que organizan un plan: a dónde, a qué hora y cómo»* — sustituye a *«Comprender una situación de invitación a hacer planes»*, con verbo vetado por `formulacion-objetivos.md` §4.2 y sin anclaje a lo que el bloque extrae. Ejercicio 8: *«Quedar con alguien para hacer un plan de fin de semana»* — sustituye a *«Preguntar y responder en una situación para organizar planes»*, que abría igual que el bloque anterior y arrastraba una condición vacía. El objetivo general se conserva de la propuesta, sin marca de género.

**(3) Rótulos y nombre de la tarjeta.** El rótulo del ejercicio 7 pasa a `CONDUZCA LA PRÁCTICA DE LOS MEDIOS DE TRANSPORTE` (había dos `PROPICIE` en el mismo archivo). La tarjeta se nombra en las tres menciones como *Preguntar por los planes de **otra persona*** por decisión del autor: **diverge del título registrado en `registro-recursos.md` de repo B** (*…de otro*), que está congelado.

**(4) Retiradas de contenido visible (§10.6, con OK del autor).** La reformulación de los seis pasos del ejercicio 8, la cita de las expresiones del paso 4, la lista de las ocho palabras de la pista 68, los cuatro nombres del ejercicio 7 y el cierre sobre la grafía, que repetía *«el oído no ayuda: hay que conocer la palabra»* tres renglones antes. Retirado también *«El libro pide la práctica por escrito»*: única ocurrencia de esa fórmula en toda la capa `final/`.

**(5) Vídeo y lengua del estudiante.** Las pausas de predicción se sitúan **antes** de cada decisión, no en ella, para que haya algo que predecir; y la activación admite recoger respuestas en la lengua del estudiante, como ya hacía la Gramática de esta unidad.

Fuera del lote por decisión del autor: `unidades/U6/final/vocabulario.md` y `unidades/U6/recursos/tarjetas/profesiones.csv`, sin commitear.

## [v12.74 — 2026-08-05] — U3 Vocabulario: el *¿quién es quién?* de cierre pasa de "pistas cruzadas" a dos rondas explícitas

`unidades/U3/final/vocabulario.md`. El cierre del bloque 6-10 instruía *«Empiece con pistas de una sola familia y pase a pistas cruzadas»*: la etiqueta *cruzadas* solo se entiende si ya se conoce el juego. Reescrito como dos rondas con su ejemplo cada una — primera ronda anunciando la familia (*de la familia de Javier: es enfermera* → *es la madre de Javier*), segunda sin anunciarla (*es agricultor y tiene vacas* → *es el padre de Lucía*), que es lo que obliga a nombrar el parentesco completo. Añadido el aviso de que la familia de David (pistas 32-33) solo se describe por parentesco, sin profesiones: el modelo *es enfermera* no le sirve.

**Colisión §8.1 resuelta.** *pista* como indicio convivía con **pista 31-35** (audio, forma canónica reservada) — mismo caso documentado en U4 Vocabulario B1, sin resolver en U3. En el cierre desaparece el sustantivo al reformular con el verbo *describir*; en la línea de las Tarjetas de Vocabulario - familia, *dan pistas* → *dan indicios*.

---

## [v12.73 — 2026-08-04] — U6 Gramática en `final/`: el imperativo de *tú* pasa a explicarse por la tercera persona del presente

`unidades/U6/final/gramatica.md` (1224 palabras, techo ≤1600), derivada de `unidades/U6/propuesta/gramatica.md`. Sección sin audio; 5 ejercicios en las páginas 64-65 y dos cuadros (presente de irregulares + imperativo). Sesión de redacción larga, con el cuerpo revisado frase a frase por el autor.

**(1) Cambio de regla del imperativo.** La propuesta explicaba la orden de *tú* como transformación del infinitivo (*-ar → -a*, *-er/-ir → -e*), lo que deja *cerrar → cierra* como excepción que hay que parchear. Sustituida por la regla estándar —el imperativo afirmativo de *tú* coincide con la tercera persona del singular del presente (marcoELE, ProfeDeELE, RAE)—, que además explota que los dos cuadros están en la misma página 64. Consecuencias: *cierra*, *juega* y *duerme* dejan de necesitar explicación propia; el reparto del ejercicio 4 pasa de «cuatro regulares + tres memorizados + *cerrar* aparte» a **cinco que cumplen la regla + tres que se memorizan** (*haz, pon, ven*); y las excepciones se descubren probando la regla contra los verbos del cuadro del presente. Rótulo nuevo: `ENLACE LA FORMA DE LA TERCERA PERSONA DEL PRESENTE CON EL IMPERATIVO TÚ`.

**(2) Explicación del presente irregular reorganizada.** La lectura por filas de la propuesta enunciaba una zona segura que *ir* no cumple y una bota que *hacer* tampoco, dejando dos de seis verbos como parches finales. Ahora se clasifica tomando *tener* (unidades 1-2, ya explicado con su *-go* y su diptongo) como modelo: *venir* es su caso idéntico, *hacer* solo tiene primera persona en *-go*, e *ir* es totalmente irregular como *ser*. La bota se dibuja solo donde existe y sirve para fijar que *nosotros* y *vosotros* quedan al margen.

**(3) Objetivos.** General *«Aplicar las formas irregulares del presente y del imperativo de tú para hablar de acciones y dar órdenes»* (los de la propuesta y las primeras derivaciones eran aditivos o mecánicos). Bloques: *«Conjugar los verbos irregulares en presente»* y *«Formular órdenes e instrucciones con el imperativo afirmativo de tú»*.

**(4) Dos dinámicas sustituidas.** El dictado de cierre del bloque 1 —instrumento que `gramatica-pautas.md` §15 #8 propone para materializar el interleaving— pasa a **tres en raya gramatical** (#50 del banco de dinámicas, sin usar en el curso): seis irregulares y tres regulares en el mismo tablero. Y la activación abre con dos situaciones imaginarias planteadas con nombres del grupo, de las que la clase saca la orden.

**(5) Tarjetas retiradas.** Comprobada la adecuación del set *establecimientos* a los ejercicios 1-2: solo cuatro de las veinte tarjetas tienen frase donde aparecer, y una de ellas está en el ejemplo. Uso pasivo según `tarjetas-vocabulario-pautas.md` §10bis; fuera de la sección.

**(6) Errata editorial del libro** en p65-act4 (ya registrada en el inventario como `P-p65-act4-error-editorial`) trasladada como aviso operativo: el solucionario numera su primera respuesta sobre el ejemplo, la numeración va desplazada y añade una décima orden sin ítem.

## [v12.72 — 2026-08-03] — U2 Comunicación y Evaluación: retirada de *apetecer* + frase ilegible del juego de adivinanzas

`unidades/U2/final/comunicacion.md` (1104 palabras, techo ≤1450) · `unidades/U2/final/evaluacion.md` (949, techo ≤950).

**(1) Comunicación, ejercicio 10.** *Apetecer* no aparece en ningún inventario de U0-U9 ni en la propuesta de U2: entró al redactar `final/`. Es peninsular (en América el hueco lo ocupan *tener ganas de*, *provocar*, *antojarse*) y es verbo de afección con pronombre átono, misma estructura que *gustar*, que la unidad aplaza explícitamente. Sustituido por *(no) tengo ganas de* + infinitivo presentado con Sentence Builder (`repertorios/comunicacion.md` §3.4B): esquema de tres casillas en pizarra, tres combinaciones modeladas, producción con esquema a la vista y después sin él. *Querer* se descartó por pragmática — *no quiero* rechaza sin mitigar, y el bloque enseña a rechazar una invitación. Dos arrastres de coherencia en el mismo bloque.

**(2) Evaluación, ejercicio 8.** *«Recoja en plenaria una pareja personaje-pregunta-clave que les haya resultado especialmente útil»* → *«Recoja en plenaria dos o tres personajes con la pregunta que más ayudó a adivinarlos»*. *Pareja* colisionaba con su acepción canónica (dos estudiantes, tres usos en el mismo archivo; §8.1 nota de formas reservadas), el compuesto de dos guiones era imparseable y *les* no tenía antecedente.

## [v12.71 — 2026-08-02] — U5 Cultura incorporada al repo: unidad 5 completa en final/

`unidades/U5/final/cultura.md` (733 palabras, techo ≤800) entra en el repo por decisión del autor tras permanecer sin trackear desde su redacción (v12.66-v12.69, intacta desde entonces; greps §7.1 limpios). Con esto U5 queda completa y versionada: 6 secciones en `final/` + `U5-itinerarios.md`. La carpeta `unidades/U6/final/` (sesión U6 en curso) queda fuera del lote.

## [v12.70 — 2026-08-01] — U5 itinerario imprimible cerrado (patrón U4 v12.60, derivado de final/)

`unidades/U5/U5-itinerarios.md` (nuevo): básico con 15 bloques CLASE + 5 CASA (6 ejercicios a casa, análogos U1-U4) y píldoras 5.1/5.2 marcadas; estación de servicio con Caja 1 = 59 tarjetas en 5 campos (verificada contra `registro-recursos.md §5` + CSVs) y Caja 2 = 3 (2 {comunicación} + 1 {escritura}); materiales complementarios con anclajes y tiempos desde los 4 archivos SGEL + 3 capturas depositados en `unidades/U5/recursos/` (se commitean, patrón U4) + tablas del diseñador. Pendiente: capturas Blinklearning y título/enlace del vídeo. `cultura.md` intacta y fuera del lote.

## [v12.69 — 2026-08-01] — U5 Comunicación y Destrezas: lote de correcciones post-v12.66 revisado por el autor

`unidades/U5/final/comunicacion.md` (1448 palabras, techo ≤1450) · `unidades/U5/final/destrezas.md` (1315, techo ≤1400).

**(1) Comunicación — tres retoques.** *parejas voluntarias* → *parejas que se ofrezcan* en los dos cierres de dramatización (§7.1) y compactación menor en la fase 1 del ejercicio 5 (*pase por las mesas resolviendo dudas* → *pase resolviendo dudas*).

**(2) Destrezas — resolución de la valoración de fondo de la píldora 5.2 pendiente desde v12.66.** El procedimiento de cuatro columnas (*quién · qué · cuándo · dónde*) con descarte dato a dato — que dejaba dos columnas vacías sobre un texto de 75 palabras — se sustituye por mediación basada en necesidades: subrayado de las necesidades de la familia González distinguiendo imprescindibles de preferibles, conexión necesidad→casa respaldada por la descripción y verificada por otra persona del grupo, y gestión explícita del caso sin casa (*necesidades pendientes* / el grupo explica qué falta). Fórmulas *del mediador* → *de la tarjeta* Cuenta lo que oyes, con línea nueva *Deje a la vista la tarjeta*. Además: objetivo del bloque 6-8 *Describir una casa y la distribución de sus espacios* → *Presentar la vivienda que mejor responde a las necesidades de una familia* (capacidad final productiva, §1.2 de `formulacion-objetivos.md`); revisión entre pares con foco en concordancia y precisión en lugar del juego de adivinar la frase de partida (ejercicio 7, sin cuantificar frases); preparación de la escucha del ejercicio 4 sin la introducción forzada de léxico (*chimenea, escaleras, terraza, leña*) y con aclaración de léxico tras la primera escucha.

`cultura.md` queda intacta y fuera del lote por decisión del autor; su publicación se decidirá como lote independiente.

## [v12.68 — 2026-08-01] — Hotfix: género en U5 Evaluación + fila U5 de `formulacion-objetivos.md` §2.2

`unidades/U5/final/evaluacion.md` (947 palabras, techo ≤950) · `docs/formulacion-objetivos.md`. **(1)** *tres parejas voluntarias* → *tres parejas que se ofrezcan* en las dos ocurrencias (Versión A y B) — infracción de §7.1 del manual. **(2)** Con OK explícito del autor, la fila U5 de la tabla ❌/✅ de §2.2 Evaluación pasa al formato de la fila U7: el *«Demostrar que puede describir…»* (rechazado en v12.67 por arrastrar verbos comunicativos encadenados) deja de ser ejemplo validado y la ✅ queda en *«Consolidar los contenidos trabajados en la unidad.»* (Dirección B). Registro de actualizaciones del propio documento al día. Cierra la primera deuda de v12.67.

## [v12.67 — 2026-08-01] — U5 Evaluación cerrada — última sección de U5 en `final/`

`unidades/U5/final/evaluacion.md` (nueva, 943 palabras, techo §11.5 ≤950).

**(1) Derivada de `propuesta/evaluacion.md` (2089 palabras) y auditada.** Checklist v1 de `check-final`: 14 ✅ / 1 ⚠ / 0 ❌. Estructura §2.1 Evaluación completa (apertura solo *Objetivo*, headers canónicos Versión A/B, cierre B con *«Igual que en la Versión A.»*, conexión a la **unidad 6** en una sola frase verificada contra su inventario). Rótulo *Propuesta A/B* → *Versión A/B*; *DESCRIBIR Y UBICAR EN DIÁLOGO* → *DIÁLOGOS DE DESCRIPCIÓN Y UBICACIÓN* (etiqueta sin verbo, §2.1); Caja 1/Caja 2 y cara A → formato canónico §6.1 y *«la cara del esquema de funciones»* (naming de U5 Comunicación); *actividad* → *ejercicio*, *mingle* y *whisper correction* → lengua de aula. Recapitulación de las cinco insignias mantenida (lemas en MAYÚSCULAS y negrita) sin la frase-balance (§10.1); referencia a la evaluación sumativa externa fuera (ningún precedente la lleva).

**(2) Objetivo por Dirección B tras rechazo del autor a la fórmula de evidencia.** La derivación aplicó primero la versión de la tabla ❌/✅ de `formulacion-objetivos.md` §2.2 (*«Demostrar que puede describir la propia casa y ubicar personas y objetos en español»*); el autor la descartó (*demostrar* + verbos comunicativos encadenados, mismo patrón que la fila U7). Cierre con la Dirección B: *«Consolidar los contenidos trabajados en la unidad.»* — igual que U2E y U4E.

**Deudas abiertas.** La fila U5 de la tabla §2.2 de `formulacion-objetivos.md` sigue marcando como ✅ la versión *demostrar* que el autor acaba de descartar — actualización pendiente de OK. Zonas §10.6 de `evaluacion.md` sin OK explícito (citas de ítems críticos del ejercicio 1 y modelo de preguntas del ejercicio 5). Sin commitear de la sesión anterior: `cultura.md` (sin trackear) y ediciones en `comunicacion.md` y `destrezas.md`.

## [v12.66 — 2026-07-31] — U5 Destrezas cerrada + saneamiento de U5 Comunicación + unificación del nombre de la tarjeta de mediación

`unidades/U5/final/destrezas.md` (nueva, 1336 palabras) · `unidades/U5/final/comunicacion.md` (nueva, 1447) · `unidades/U5/final/gramatica.md` (nueva, 1605) · `unidades/U3/final/destrezas.md`.

**(1) U5 Destrezas derivada y auditada.** Sección nueva a partir de `propuesta/destrezas.md`. Checklist v1 de `check-final` pasado: único ❌ (§10.3, *"Vuelvan a la página 58"* con imperativo dirigido a la clase) corregido; verbo de rótulo repetido en el bloque 3 corregido. Fuera de la derivación: canción, consolidación distribuida, specs de tarjeta y píldora, notación A/B, mapeo cerrado de personajes, paletas de pizarra y los cuatro pasos recitados de *Lee en cuatro pasos* (§2, §10.1).

**(2) Los cuatro objetivos rehechos contra la doctrina de sección.** `destrezas-pautas.md` §11 de repo B (lista de verbos validados + *medio ≠ objetivo*) y `formulacion-objetivos.md` §1.2 (⚠ Destrezas: el objetivo de bloque nombra la capacidad de la destreza, no los recursos ni la lista de sub-tareas). Los objetivos derivados de la propuesta eran aditivos o llevaban coletilla de medios. Resultado: general *Presentar la vivienda que mejor encaja con las necesidades de una familia*; bloques *Identificar la información principal de una descripción de habitación* · *Comparar una vivienda ideal con viviendas reales* · *Describir una casa y la distribución de sus espacios*.

**(3) Nombre de la tarjeta de mediación unificado a *Cuenta lo que oyes*.** U3 `final/` la llamaba *Cuenta lo que dice otra persona*, nombre introducido en la derivación y sin respaldo en ninguna fuente: la spec de la tarjeta (`U03-destrezas.md` §D de repo B), `registro-recursos.md`, `U03-itinerarios.md`, `U4-itinerarios.md` y las propuestas de U4-U6 usan todas *Cuenta lo que oyes*. Corregidas las dos menciones de U3 y alineada la de U5. U4 ya era correcta. Propuestas y repo B sin tocar.

**(4) Rótulo de mediación realineado con la propuesta.** La píldora 5.2 pasa a abrir el rótulo, en el lugar donde la propuesta pone `Buscar web SGEL--Píldora formativa 5.2`; eliminada la frase de reintroducción de la tarjeta, que era invención de la derivación (la propuesta da la tarjeta por ya en mano); las cuatro columnas se nombran desde la píldora —quién · qué · cuándo · dónde— con el aviso de que la de *dónde* queda vacía porque el texto no da ciudad. Cierra de paso la duplicación tarjeta↔píldora (§10.1).

**(5) Ejercicio 6 — el biombo no tapaba nada.** El dormitorio de quien dicta no está sobre la mesa, así que la barrera resolvía un problema inexistente y *"comparar el plano con el dormitorio descrito"* no tenía referente: la actividad no cerraba, y menos en un aula de 25. Sustituido por dibujar el plano propio antes de emparejar; al terminar se comparan los dos planos. La pareja se autocorrige sin depender de que el docente llegue a trece mesas.

**(6) U5 Comunicación — cuatro saneamientos.** Cierre del ejercicio 7 reescrito: la frase *"para preparar la transición al sonido /x/"* era hilo fabricado (§10.1) —la concordancia de plural no prepara nada fonético— y el puente real ya existía en *rojo* y *jugador*; el cierre pasa a una ronda de adjetivos sobre objetos del aula donde la concordancia es la clave que resuelve. Objetivo del bloque de pronunciación *Relacionar* → *Reconocer*: `formulacion-objetivos.md` §1.1 paso 3 y §1.2 paso 3 catalogan *relacionar* como mecánica de ejercicio a descartar. *fotografías* → *fotos* (§8.1). *voluntarios* → *intervenciones* / *quienes se ofrezcan* (§7.1).

**Deudas abiertas.** `gramatica.md` cierra en 1605 palabras, 5 por encima del techo §11.5 (≤1600). Valoración de fondo de la píldora 5.2 pendiente de decisión del autor: dos de sus cuatro columnas quedan vacías sobre el texto del ejercicio 8, el descarte elimina dos datos de un texto de 75 palabras y las candidatas a comparar son casas inventadas libremente, que pueden no discriminar. Zonas §10.6 (L39, L43) y §10.10 (L90) de `destrezas.md` sin OK explícito.

## [v12.65 — 2026-07-30] — U1 Gramática: triángulo único → tres triángulos por verbo + *pañuelo conjugador* reescrito

`unidades/U1/final/gramatica.md` — cuatro correcciones editoriales autorizadas por el autor sobre unidad bloqueada (`.claude/rules/u1-final-locked.md`). La versión de `propuesta/` no se toca (fuente rica intacta).

**(1) Rediseño del worked example de apertura — de un triángulo a tres.** El esquema original colgaba las **nueve formas** (3 verbos × 3 personas) de un único triángulo con el nombre del docente en el centro: nueve frases repartidas por las esquinas, con el triángulo sin función organizadora. Incumplía `gramatica-pautas.md` §7.1 de repo B (*máximo 5 elementos nuevos por segmento; si hay más, segmentar persona por persona en conjugación*) y entraba por la forma, contra §7.3 (*significado antes que forma*). Sustituido por **tres triángulos, uno por verbo**, con el dato en el centro (*llamarse* → nombre, *ser* → ciudad, *tener* → edad) y la forma conjugada en cada vértice: cada vértice se lee hacia el centro y cierra frase. Tres elementos nuevos por figura, y la posición del vértice pasa a significar la persona en las tres (principio CLT de pares mínimos lado a lado, misma pauta §1bis). Consecuencias en el cuerpo: desaparece la lista de cuatro marcas del final (cada aviso cae ahora dentro de su verbo: pronombre obligatorio en *llamarse*, irregularidad total en *ser*, doble irregularidad en *tener*); desaparece la descripción de la geometría (posición de vértices y centro), que pasa a estar cubierta por la ilustración — §10.1, el cuerpo remite al material editorial en vez de duplicarlo; recuperada la nota de uso *"esta es la forma que usan entre ellos siempre"* sobre el *tú*, perdida en la derivación. Pasada de coherencia §8.4: la referencia posterior *"el aviso del triángulo"* (ejercicio 2) pasa a *"el aviso del triángulo de tener"*. **Deuda documental abierta:** el banco canónico §8.1 del manual cubre elementos visuales *del libro* (`foto`, `dibujo`, `ilustración`, `imagen`) pero no ilustraciones propias de la guía del profesor; provisionalmente se cita como *"los tres triángulos del modelo"*, pendiente de fijar convención antes de que el caso reaparezca en U2-U9.

**(2) Mecánica del *pañuelo conjugador*.** El cierre opcional del bloque *Ejercicios 1-3* era ininteligible: la compactación a `final/` había borrado el pañuelo, el centro y la carrera (*"corren al centro"* → *"se enfrentan"*), dejando el nombre de la dinámica sin referente; además fundía en una sola secuencia (*"lance pronombre + verbo + número"*) dos funciones distintas — el número **selecciona** a los dos duelistas, el pronombre + verbo es la **consigna** cuya respuesta es la forma conjugada. Reescrito con la mecánica completa: numerar, pañuelo en el centro, consigna, criterio de punto, y los *nueve casos* explicitados. Recuperada la condición de viabilidad *si el aula tiene espacio*, que justifica el carácter opcional.

**(3) Contradicción en la cadena oral.** El tercer ejemplo (*La silla es roja*, glosado *"cambia objeto y color"*) violaba la consigna que ilustraba (*cambiar solo una cosa, no las dos a la vez*). Eliminado; los dos ejemplos restantes cubren los dos casos que importan (cambio de color en masculino, cambio de objeto con ajuste a femenino).

**(4) Compactación §11.4 compensatoria.** La reescritura del pañuelo llevó la sección de 1590 a 1626 palabras (techo §11.5 = 1600); compensación solo sobre redundancia y relleno (6 recortes: *rápidamente*, *su propio*, duplicación de *solo cambia el artículo*, metadiscurso *conectando con lo aprendido*, *al repetir* redundante, fusión de dos frases que se reformulaban en el modelado del ejercicio 9). Sección cerrada en **1593 palabras**.

## [v12.64 — 2026-06-14] — `manual-estilo-final.md` §11.5 nueva: techos de longitud por sección (sin suelo)

`docs/manual-estilo-final.md` §11.5 nueva (tras §11.4 *Criterio de aplicación: compactación y consulta*) — techos operativos de palabras por sección tras la pasada de compactación: Vocabulario ≤1500, Gramática ≤1600, Comunicación ≤1450, Destrezas ≤1400, Evaluación ≤950, Cultura ≤800. Si la derivación inicial supera el techo, aplicar §11.4 hasta entrar en rango; si sigue por encima tras compactar, consultar al editor antes de seguir recortando o de cerrar. **Sin suelo**: la economía pedagógica puede sostener secciones más cortas (caso real U3 Cultura en 529 palabras). Bandas observadas del corpus U1-U4 (*Vocabulario 1200-1500, Gramática 1300-1600, Comunicación 1100-1450, Destrezas 1050-1400, Evaluación 800-950, Cultura 500-800*) incluidas como referencia analítica, no gate normativo. Medición canónica: `wc -w` sobre archivo cerrado. §12 sincronizado con fila nueva. Cierra la Cuestión A del Informe consolidado U4 con dictamen del revisor en dos pasos: (1) validación empírica del corpus (medición real → bandas observadas con ajustes a la baja en Destrezas/Evaluación/Cultura para no dejar fuera valores reales ya cerrados); (2) decisión doctrinal — techos absolutos sin suelo, no rangos duros, porque el problema real del proyecto es la inflación inicial y un suelo incentivaría relleno artificial. **Cierre de las dos cuestiones abiertas (A y B) del Informe consolidado U4.**

## [v12.63 — 2026-06-14] — `CLAUDE.md` raíz: cross-reference repo A → capa pedagógica de repo B

`CLAUDE.md` — dos cambios coordinados que hacen visible el router documental hacia la capa pedagógica de repo B (congelado editorialmente, pero fuente única viva para decisiones metodológicas): (a) párrafo nuevo *"Consulta pedagógica activa"* en §*Modelo de dos repositorios (A / B)* — cuando una edición en `unidades/**/final/*.md` toque una decisión de diseño didáctico (activación, secuenciación, mecánicas, viabilidad de aula), consultar el pauta correspondiente antes de decidir; (b) fila nueva en la tabla *Documentos clave* listando *repo B — capa pedagógica* como bloque documental (`*-pautas.md`, `proceso-operativo.md`, `marco-teorico-metodologico.md`). La doctrina pedagógica no se duplica en repo A; sigue siendo fuente única en repo B. Cierre de la Cuestión B del Informe consolidado U4 con reformulación arquitectónica del revisor: descartada la propuesta original de `docs/criterios-pedagogicos-NC1.md` (duplicaba doctrina existente en repo B); aplicada la opción 3 (cross-reference mínimo). Aparcada la opción complementaria de regla path-scoped `.claude/rules/final-pedagogia.md` para segunda fase si el cross-reference no basta (riesgo de inflado de contexto con imports masivos). Cuestión A del Informe (diana de longitud) sigue abierta.

## [v12.62 — 2026-06-14] — U5 `final/` arranque: vocabulario.md

`unidades/U5/final/vocabulario.md` nuevo (8792 bytes). Primera sección del piloto U5 *La familia* en versión `final/`. Sigue el modelo metodológico estabilizado en U1-U4 (manual de estilo `final/` con las 12 secciones doctrinales + §13 patrones observados, schema v2.0 de material complementario, plantilla de itinerario imprimible). Próximas secciones U5 pendientes: gramática, comunicación, destrezas, cultura, evaluación + itinerario + inventario material complementario.

## [v12.61 — 2026-06-14] — Diagnóstico NC1 para asesores + pipeline `pdf-tools/`

`docs/diagnostico-nc1-asesores.md` nuevo (1289 líneas) — bitácora del asesor pedagógico de NC1, documento entregable a asesores externos para revisión editorial del libro. `pdf-tools/` nuevo — pipeline de generación PDF del diagnóstico: `build.sh` (sed → pandoc → xelatex), `preamble.tex` (estilos LaTeX con paleta NC1, fuentes Helvetica Neue + Menlo + Arial Unicode MS), `README.md` y `.gitignore`. Stack sin Node.js: pandoc + xelatex + bash + fuentes del sistema. Salida en `pdf-tools/out/diagnostico-nc1-asesores.pdf` (gitignored).

## [v12.60 — 2026-06-14] — U4 cierre completo: 6 secciones `final/` + itinerario + material complementario + recursos fuente

`unidades/U4/` — cierre del piloto U4 *Comidas y bebidas*: las 6 secciones `final/` (vocabulario, gramática, comunicación, destrezas, cultura, evaluación) listas para imprenta; itinerario imprimible `U4-itinerarios.md` (144 líneas); inventario `U4-nc1-material-complementario.json` (1145 líneas); 3 PDFs fuente SGEL (*Actividades Extra 4*, *Evaluación 4*, *Gamificación*) + 1 PPTX (*UNIDAD4NUEVOCOMPANEROS*) en `unidades/U4/recursos/`; actualización del CSV `unidades/U4/recursos/tarjetas/comidas-preparadas.csv` (+3 entradas). U4 sigue el mismo patrón de cierre de U1-U3 (commit `126526a` para U3). Las 11 reglas del manual derivadas del piloto U4 ya están integradas en v12.49→v12.59.

## [v12.59 — 2026-06-14] — `manual-estilo-final.md` §12: 10 entradas nuevas de *Cambios y versiones*

`docs/manual-estilo-final.md` §12 — 10 filas nuevas en la tabla *Cambios y versiones*, todas con fecha 2026-06-14, una por cada regla efectivamente aplicada al manual en el procesamiento del Informe consolidado U4: §2.1 coherencia A↔B; §4.2 referencia interna apartado de X; §8.1 formas canónicas reservadas; §8.4 nueva coherencia terminológica; §10.1 ampliación bullet sobre-prescripción; §10.3 persona gramatical; §10.6 bullet 6 mecánica global; §10.7 ampliación a jerga editorial interna; §11.4 límite de la compactación; §13 ampliación Patrón 3 + Patrones 6 y 7 nuevos (agrupados en una fila). Ajustes del revisor frente al draft inicial: (a) eliminada la fila dedicada al descarte de P-2.1.c — §12 documenta cambios efectivos del manual, no propuestas descartadas; la trazabilidad del descarte ya queda en CHANGELOG/REVIEW; (b) las tres anotaciones de §13 agrupadas en una sola fila (mismo destino, misma fecha, mismo tipo de cambio). **Cierre completo del procesamiento del Informe consolidado U4**: 9 propuestas firmes aplicadas + 1 descartada por error de marco + 3 anotaciones a §13 + sincronización de §12. Total de la sesión: v12.49 a v12.59 (11 bumps).

## [v12.58 — 2026-06-14] — `manual-estilo-final.md` §13: ampliación de Patrón 3 + Patrones 6 y 7 nuevos

`docs/manual-estilo-final.md` §13 — tres anotaciones del Informe consolidado U4 sobre patrones observados sin codificar: (1) **Patrón 3 ampliado** — *Caso piloto* → *Casos piloto* (lista plural, formato Patrón 5) con segunda ocurrencia U4 Vocabulario *"Cinco rondas activan el género y el plural"*; estado actualizado a *"dos ocurrencias directas no alcanzan masa crítica para regla de §10. Revisar al cerrar U5"*; (2) **Patrón 6 nuevo** — *Repetición monotemática de conector entre rótulos o entre frases de inicio de párrafo*: casos piloto U4 Gramática (*Pase al* ×9) y U4 Comunicación (*Para el* ×6), variación distribuida en piloto, sin codificar como regla — exige juicio editorial; (3) **Patrón 7 candidato** — *Variables algebraicas (X, Y) en cuerpo docente*: caso piloto U4 Cultura (*"trae una frase modelo en X se come Y por la calle"*), una sola ocurrencia, sin masa crítica. Aplica las 3 anotaciones del Informe consolidado U4 tal cual aprobadas por el revisor (Anotación 1 con formato plural + actualización de estado; Anotaciones 2 y 3 verbatim; cita literal de Patrón 7 preservada en minúscula inicial como cita-evidencia). Fecha de aplicación 2026-06-14 (no la fecha 2026-06-XX placeholder del informe). Lote 10 del procesamiento del Informe consolidado U4.

## [v12.57 — 2026-06-14] — `manual-estilo-final.md` §11.4: bloque *Límite de la compactación*

`docs/manual-estilo-final.md` §11.4 — bloque nuevo *Límite de la compactación — unicidad de interpretación y separación de acciones* insertado tras los *Criterios de la pasada de compactación* y antes del bloque *Cuándo SÍ se abre consulta*. La compactación preserva dos invariantes: (1) **unicidad de interpretación** — sin formulaciones de doble lectura por economía (*"una vez completa"*, *"entre turnos"* sin antecedente, *"Verificación en plenaria"* sin objeto); (2) **separación de acciones en lugares distintos del aula** — cuando docente o estudiantes actúan en soportes o espacios distintos (cuaderno, libro, pizarra, voz), cada acción mantiene su sujeto y verbo. **Filtro de cierre** de la pasada (a escala macro, complementario al filtro pre-recorte ya existente en §11.4): si la frase compactada admite dos lecturas o funde acciones, deshacer la compactación. Casos de origen: U4 Destrezas (cuatro frases compactadas con pérdida de unicidad o fusión). Aplica P-11.4.a del Informe consolidado U4 con ajuste del revisor: compresión ligera de la redacción + confirmación explícita de que ambos filtros (pre-recorte y cierre) coexisten. Lote 9 del procesamiento del Informe consolidado U4 — cierre del bloque de 10 propuestas firmes (P-2.1.d a P-11.4.a; P-2.1.c descartada).

## [v12.56 — 2026-06-14] — `manual-estilo-final.md` §10.7: ampliación a *rótulo* como jerga editorial interna

`docs/manual-estilo-final.md` §10.7 — cuatro cambios coordinados que generalizan el apartado de vetar la palabra *"bloque"* a vetar la **jerga editorial interna** completa (*bloque* + *rótulo*): (a) título reemplazado por *Sin jerga editorial interna en el cuerpo del docente (bloque, rótulo)*; (b) introducción reescrita incluyendo *rótulo* (etiqueta imperativa en MAYÚSCULAS que abre cada paso) junto a *bloque*; (c) cabecera de la tabla *Casos a evitar* actualizada de *"❌ Con 'bloque'"* a *"❌ Jerga editorial interna"* para acomodar los nuevos casos; (d) dos filas nuevas (*"Haga la transición desde el rótulo anterior…"* y *"En el rótulo siguiente verán…"*). Caso de origen: U4 Comunicación. Aplica P-10.7.a del Informe consolidado U4 con ajuste del revisor: incluido el cambio de cabecera de la tabla (cubría asimetría que la propuesta original dejaba abierta) + microcompresión de la intro. Mismo principio editorial; cobertura ampliada de un término a una categoría. Lote 8 del procesamiento del Informe consolidado U4.

## [v12.55 — 2026-06-14] — `manual-estilo-final.md` §10.6: bullet 6 nuevo (mecánica global vs inventario de ítems)

`docs/manual-estilo-final.md` §10.6 — bullet 6 nuevo en *Formas en que aparecen* (tras *Descripciones del enunciado…*): cuando el rótulo propone una mecánica que se aplica a todo el ejercicio (mano alzada rápida, lectura + respuesta, dictado completo, corrección en parejas), enumerar ítem por ítem el inventario visible convierte en obligación explícita lo que ya está implícito en la mecánica global. Los ítems concretos solo se citan si son foco lingüístico genuino (error frecuente, contraste relevante, opción ambigua). Mismo principio de §10.6; régimen ⚠ + gate de consulta previa siguen intactos. Casos de origen: U4 Evaluación (ej. 2, ej. 3, ej. 6 GUSTAR Y PRONOMBRES OI). Aplica P-10.6.a del Informe consolidado U4 con ajuste de compresión del revisor: bullet más denso (definición operativa + criterio de excepción + dos microejemplos) acorde a la textura de la lista taxonómica. Lote 7 del procesamiento del Informe consolidado U4.

## [v12.54 — 2026-06-14] — `manual-estilo-final.md` §10.3: nota persona gramatical del cuerpo

`docs/manual-estilo-final.md` §10.3 — nota nueva tras el *Filtro de detección*: el cuerpo se redacta siempre en **imperativo de cortesía (usted)** dirigido al docente, nunca en tercera persona descriptiva (*El docente formula la pregunta*). El lapsus es más frecuente en mecánicas con varios actores encadenados (docente, clase, voluntario); aplicar pasada de coherencia de voz en esos rótulos. Tabla ❌/✅ con tres casos. Caso de origen: U4 Comunicación (rótulos GUÍE ej. 2 y ACOMPAÑE ej. 10). Aplica P-10.3.a del Informe consolidado U4 con microajustes léxicos del revisor: título acortado (*Persona gramatical del cuerpo* en vez de *del cuerpo del docente*), sintaxis natural del enlace ("aplicar una pasada"), reformulación de la cadena de actores. Complementaria a §10.3 actual (asignación de acción) sin solape. Lote 6 del procesamiento del Informe consolidado U4.

## [v12.53 — 2026-06-14] — `manual-estilo-final.md` §10.1: ampliación del bullet de sobre-prescripción de decisiones libres

`docs/manual-estilo-final.md` §10.1 — bullet *Prescripción de decisiones libres del docente* ampliado con tres patrones adicionales del mismo principio: **reescritura en pizarra de cuadros/ejemplos/ítems que el libro ya presenta** (U4 Gramática), **notación abstracta de roles** (*A/B*, *alumno 1/alumno 2*) cuando la mecánica no requiere etiquetas funcionales (U4 Comunicación), y **series cerradas de preguntas-modelo** en sondeos o activaciones cuando el docente puede formularlas (U4 Destrezas). Sustituciones de instrucción abierta actualizadas a cuatro ejemplos que cubren los seis patrones. Misma doctrina; no invade §10.10 (proporcionalidad), cuya distinción ya está documentada en el propio bullet de §10.10. Aplica P-10.1.a del Informe consolidado U4 con ajustes de redacción del revisor: bullet único (no sub-bulletizar), compresión léxica (*uso de pizarra* → *reescritura en pizarra*; *paletas concretas de preguntas* → *series cerradas de preguntas-modelo*), sintaxis más agrupada. Lote 5 del procesamiento del Informe consolidado U4.

## [v12.52 — 2026-06-14] — `manual-estilo-final.md` §8.4 nueva: coherencia terminológica entre objetivo, rótulo y cuerpo

`docs/manual-estilo-final.md` §8.4 nueva (tras §8.3 *Sin siglas*) — el cuerpo del docente mantiene la terminología elegida en objetivo de sección + objetivo de bloque + rótulo imperativo. No se introduce capa coloquial paralela en el cuerpo cuando las otras dos capas usan forma técnica o precisa. Si por decisión editorial se opta por formulación menos técnica, se mantiene en las tres capas. **Pasada de coherencia transversal** tras cualquier edición terminológica: alinear todas las menciones posteriores. Tabla ❌/✅ con caso U4 Gramática B1 (*PRONOMBRES ÁTONOS* vs *palabras pequeñas*). Aplica P-8.b del Informe consolidado U4 con ajuste del revisor: eliminada la pseudo-decisión difusa sobre "opacidad para A1.1" — sustituida por cláusula neutra de consistencia ("si por decisión editorial se opta por formulación menos técnica"). Cierre del lote compuesto P-4.2.a + P-8.a + P-8.b (referencias internas intraunidad + reserva de formas canónicas + coherencia terminológica transversal). Lote 4 del procesamiento del Informe consolidado U4.

## [v12.51 — 2026-06-14] — `manual-estilo-final.md` §8.1: nota formas canónicas reservadas + filtro de cierre

`docs/manual-estilo-final.md` §8.1 — nota nueva tras la tabla del banco canónico: las formas designadas (*ejercicio*, *pista*, *página*, *foto*, *docente*, *cuadro*…) quedan **reservadas para su referente canónico**; si en un mismo archivo una de esas formas convive con una segunda acepción potencialmente confundible, la segunda se sustituye por sinónimo no canónico (*adivinanza*, *indicio*, *clave*). Filtro de cierre: al cerrar el archivo, comprobar que ninguna forma canónica del banco convive con acepción ambigua dentro de la misma pieza editorial. Caso de origen: U4 Vocabulario B1 (*"pista 43"* + *"la primera pista"* / *"las cuatro pistas restantes"* / *"justifiquen con la pista"* como adivinanza léxica). Aplica P-8.a del Informe consolidado U4 con ajustes del revisor: condición de activación reformulada como filtro ejecutable de cierre + alcance afinado a "convivencia potencialmente confundible en la misma pieza editorial" (no veto rígido en todo el archivo). Lote 3 del procesamiento del Informe consolidado U4.

## [v12.50 — 2026-06-14] — `manual-estilo-final.md` §4.2: nota referencia interna apartado de X vs unidad X

`docs/manual-estilo-final.md` §4.2 — nota nueva tras la tabla de *Convenciones del proyecto*: dentro del **cuerpo del docente**, las referencias a otra sección de la misma unidad usan *"el apartado de [Sección]"* en minúscula y redonda; la forma *"unidad X [Sección]"* queda reservada a referencias inter-unidad. Listado cerrado de secciones inline. Caso de origen: U4 Destrezas (*"recordando las fórmulas de la unidad 4 Gramática"* desde dentro de U4). Aplica P-4.2.a del Informe consolidado U4 con ajustes del revisor (ámbito al cuerpo del docente, plano explícito en el ❌). Negrita de `**unidad X**` ya declarada en §6 *Nombres de unidad* — sin sync. Lote 2 del procesamiento del Informe consolidado U4.

## [v12.49 — 2026-06-14] — `manual-estilo-final.md` §2.1: coherencia Versión A↔B en Evaluación + descarte P-2.1.c

`docs/manual-estilo-final.md` §2.1 — subsección nueva *"Evaluación — coherencia entre Versión A y Versión B"*: si una mecánica se edita en la Versión A, reescribir en la Versión B la sinopsis correspondiente con la nueva mecánica de A. Afecta a las sinopsis de *CORRECCIÓN COLECTIVA* y de *REALIZACIÓN ESCALONADA*. Caso de origen: drift U4 Evaluación (ej. 6). **Descartada P-2.1.c** por error de marco: partía de subtipos estructurales de tarjeta que el sistema no reconoce; no entra en manual ni en §13. Lote 1 del procesamiento del Informe consolidado U4.

## [v12.48 — 2026-06-07] — `formulacion-objetivos.md` §2.2 Cultura: refuerzo abstracción del rasgo + par ❌/✅

`docs/formulacion-objetivos.md` §2.2 Cultura — añadido bullet de principio explícito ("Abstracción del rasgo cultural, no enumeración del contenido") + tabla par ❌/✅ siguiendo el patrón ya usado para Evaluación en la misma §2.2. Principio: el objetivo de Cultura nombra el **rasgo cultural** que la sección trabaja (el *uso*, el *papel*, las *ocasiones*, los *sistemas*); no enumera el inventario de contenido específico (qué tres trajes, qué tres regiones, qué tres marcadores). El contenido específico vive en los rótulos del cuerpo. Par ❌/✅ con ❌ literal del caso U9 Cultura primera ronda + ✅ ejemplo normativo derivado (Bloom 3, *Contrastar*) — no fingido como cita final literal porque el post-mortem no fija una. Caso de origen: brecha real codificable B.2 del triage U9 Cultura. Sin sync de check-final: el ítem 3 del checklist v1 ya audita "naturaleza correcta por sección" como bloque, sin necesidad de comprobación separable nueva. Registro de actualizaciones del propio `formulacion-objetivos.md` también actualizado. Primer lote (de 3) del triage doctrinal U9 Cultura.

## [v12.47 — 2026-06-07] — CLAUDE.md raíz: fila nueva en la tabla de documentos clave para `contratos-recursos-editoriales.md`

`CLAUDE.md` — añadida fila para `docs/contratos-recursos-editoriales.md` en la tabla *Documentos clave (índice de navegación)*, insertada tras `docs/formulacion-objetivos.md`. Cierre de la deuda de sincronización documental abierta en v12.41 (creación del documento sin actualización paralela del índice raíz). Sin cambios de doctrina.

## [v12.46 — 2026-06-07] — Cierre formal de la ronda autónoma post-U9D + decisión declarada sobre brecha #5

Cierre de la ronda doctrinal post-U9D. 4 brechas codificadas en v12.42-v12.45: #1 lengua profesional natural (§10.1 bullet, cierre asimetría con criterio #23 de repo B), #2 invención de hilo temático no sostenido por la fuente (§10.1 bullet), #3 papel activo del estudiante (§10.11 ortogonal a §10.3), #4 proporcionalidad mecánica↔finalidad (§10.10). Checker `check-final` pasó de 12 a 15 ítems durante la ronda. **Decisión declarada sobre brecha #5 — viabilidad de aula 25-30 estudiantes**: queda **fuera del scope del manual de estilo**. Es criterio de proceso/operativa de aula (en repo B vive como ítem #29 del checklist canónico, codificado en el mismo lote 3/5 del triage U8C que dio origen a #27 = §10.10 y #12 = §10.11), no de redacción del cuerpo del docente. Pendiente de canalizar a su fuente operativa cuando aparezca (skill específica de viabilidad, gate ex-ante de proceso, o documento operativo aparte); hasta entonces no se vuelca al manual ni al checker. Sin cambios de código o doctrina — solo trazabilidad.

## [v12.45 — 2026-06-07] — §10.11 nueva (papel activo del estudiante) + sync check-final 14→15 ítems

`docs/manual-estilo-final.md` §10.11 nueva — cuando un rótulo activa trabajo del estudiante, ese trabajo debe ser activo, nombrable y observable. El estudiante no puede quedar reducido a *escuchar*, *mirar*, *copiar*, *indicar* o *reaccionar* sin operación cognitiva o interactiva añadida. Subsección con principio condicional (no absoluto: hay rótulos legítimos más docentes o de preparación) + formas en que aparece la mecánica pasiva + filtro orientativo + régimen ⚠ por defecto + cláusula explícita de ortogonalidad con §10.3 (§10.3 regula quién ejecuta físicamente la acción; §10.11 regula si la acción atribuida al estudiante lo coloca en un papel activo, nombrable y observable; las dos se aplican juntas). Caso de origen: brecha estructural del triage U8 Cultura de repo B (post-mortem A.1: *"Lance el léxico de palabra en palabra"* — docente lanza, clase indica casilla) convertida en el ítem #12 *Comprobación real — papel activo del estudiante* del checklist canónico de aquel repo; patrón crónico documentado con reincidencias en U7C, U8V y U8G. `.claude/skills/check-final/SKILL.md` — sincronizado al checklist v1 de 15 ítems: cuatro toques (header del procedimiento 14→15, header del checklist 14→15, ítem 15 nuevo con heurísticas y formulación *"posible §10.11 — confirmar"*, cláusula de zonas de consulta ampliada a §10.6+§10.9+§10.10+§10.11). El nuevo ítem 15 incluye cláusula explícita de distinción con el ítem 7 (§10.3). Brecha #3 de 5 de la ronda autónoma post-U9D — la más delicada por tocar frontera de §10.3, resuelta con ortogonalidad declarada. Solo queda #5 (viabilidad aula 25-30, probable fuera de manual).

## [v12.44 — 2026-06-07] — §10.10 nueva (proporcionalidad mecánica↔finalidad) + sync check-final 13→14 ítems

`docs/manual-estilo-final.md` §10.10 nueva — las mecánicas didácticas que el cuerpo del rótulo propone deben estar proporcionadas al objetivo que el rótulo persigue. Si la mecánica consume más tiempo, atención, infraestructura o andamiaje del docente que el aprendizaje que produce, hay desproporción y se simplifica o sustituye. Subsección con principio + formas en que aparece + filtro orientativo + régimen ⚠ por defecto + cláusula de distinción explícita con §10.1 *Prescripción de decisiones libres del docente* (allí se veta quién decide; aquí se veta el peso de la mecánica con independencia de quién decide los detalles). Caso de origen: criterio trasladado del endurecimiento del checklist post-triage U8 Cultura de repo B (#27 *Test de proporcionalidad*; brecha estructural mayor C.1 del post-mortem U8C). `.claude/skills/check-final/SKILL.md` — sincronizado al checklist v1 de 14 ítems: cuatro toques (header del procedimiento 13→14, header del checklist 13→14, ítem 14 nuevo con heurísticas y formulación *"posible §10.10 — confirmar"*, cláusula de zonas de consulta ampliada a §10.6+§10.9+§10.10). Brecha #4 de 5 de la ronda autónoma post-U9D (#4 antes que #3 por menor riesgo doctrinal — #3 toca frontera ya activa de §10.3).

## [v12.43 — 2026-06-07] — §10.1 — bullet nuevo: invención de hilo temático no sostenido por la fuente

`docs/manual-estilo-final.md` §10.1 — bullet nuevo con cláusula afirmativa y veto. **Sí** se puede sostener un hilo o marco temático cuando el material del libro lo trae y la secuencia de ejercicios lo sostiene (título del diálogo, enunciado del ejercicio, contenido sostenido del audio o del texto). **No** es válido elevar una mención circunstancial del material a eje organizador del bloque o de la sección, ni fabricar un marco narrativo añadido para dar cohesión retórica. Caso de origen: U9 Comunicación — diálogo *¿Qué hiciste ayer?* con la queja circunstancial *"No me gustan los lunes"* de Graciela elevada a hilo organizador con 13 ocurrencias fabricadas (*"diálogo del lunes"*, *"fórmula social del lunes"*, *"el rato del lunes en clase"*…). Filtro orientativo incorporado al estilo de §10.6/§10.9. Sin sync de check-final — ítem 8 audita §10.1 como bloque. Cierre de la brecha estructural mayor detectada en triage U9C (B.1) — anomalía cuantitativa más alta de aquella sesión. Brecha #2 de 5 de la ronda autónoma post-U9D.

## [v12.42 — 2026-06-07] — §10.1 — bullet nuevo: lengua profesional natural (cierre asimetría con #23 de repo B)

`docs/manual-estilo-final.md` §10.1 — bullet nuevo que veta cuatro registros adicionales del cuerpo del docente: (a) coloquialismos (*soltar la actividad, lanzar el juego*), (b) muletillas mecánicas (*a la señal, pulse play y reproduzca*), (c) fórmulas o valoraciones de coaching (*marque la ronda con energía, suba la intensidad*), (d) jerga emocional (*engancharse al grupo, vibrar con la actividad*). Distinto del bullet ya existente sobre *jerga didáctica metodológica* (técnico-pedagógica): el nuevo veta los registros coloquial, ritual y motivacional. Cierra la asimetría con el criterio #23 de repo B (codificado tras triage U9C, lote 4/4) que repo A no había trasladado todavía. Estructura: un bullet único compacto con (a)-(d) para mantener densidad de §10.1. Caso detectado en U9 Comunicación (5 ocurrencias). Sin sync de check-final — el ítem 8 del checklist v1 ya audita §10.1 como bloque.

## [v12.41 — 2026-06-07] — `contratos-recursos-editoriales.md` nuevo (D1 + D2 del triage U9D)

`docs/contratos-recursos-editoriales.md` — documento canónico nuevo que regula la **spec textual interna** de tarjetas de estrategia y píldoras formativas. Codifica dos brechas estructurales del post-mortem U9D: (D1) la tarjeta entrega el frame literal con inicios prefijados y huecos, no enseña a construirlo (antipatrón origen *USA EL ANDAMIO*; modelo de referencia Wray & Lewis 1997 *writing frames*); (D2) la píldora desarrolla habilidad nuclear A1 transferible a cualquier material futuro del mismo tipo, no mecánica-tarea sobre el audio/texto concreto del libro (antipatrón origen: 5 candidatas iniciales píldora 9.3). Sin activación path-scoped — doctrina de consulta sobre redacción de tarjetas/píldoras. `docs/manual-estilo-final.md` §1 *Lo que NO redefine este manual* — añadida línea de cruce que remite a este nuevo documento; el manual sigue regulando cómo se nombran y dónde aparecen las menciones en `final/`, no qué dicen los recursos por dentro.

## [v12.40 — 2026-06-07] — §10.9 nueva (misión verificable) + sync check-final 12→13 ítems

`docs/manual-estilo-final.md` — §10.9 nueva codifica que la consigna al estudiante de leer/oír/buscar debe **requerir realmente** el material; si la respuesta ya es visible (pies de foto, titulares, descarte trivial, único candidato), la misión es ritual y se reformula. Sibling semántico de §10.6 pero distinto plano: §10.6 regula el cuerpo del docente, §10.9 la operatividad de la consigna al estudiante. Régimen ⚠ por defecto, sin retroactividad automática. Caso de origen: U9 Destrezas R1 ("encontrar 3 monumentos" cuyos nombres estaban ya en los pies de foto). Codificación derivada del triage del post-mortem U9D (lote D4 de 5). `.claude/skills/check-final/SKILL.md` — sincronizado al checklist v1 de 13 ítems: nuevo ítem 13 con heurísticas por palabras-señal (*encontrar*, *busca*, *señala*, *cuente cuántos*…) y formulación canónica *"posible §10.9 — confirmar"*. Sin tocar archivos `final/` existentes.

## [v12.39 — 2026-05-29] — Fix bug latente: merge no destructivo protege `hilo.relaciones[]`

`generar_reciclaje_capa1.py` — el detector de pérdidas y la lógica de fusión del merge no destructivo (v11.76) reconocían `etiquetas`, `explicacion`, `detalle` y procedencia verbal como enriquecimiento editorial, pero **no `hilo.relaciones[]`** (campo añadido en v11.86, posterior al detector). Cualquier regeneración íntegra borraba silenciosamente las relaciones cross-hilo cerradas. Bug detectado al ejecutar el paso de higiene tras v12.37: las 15 entradas U2/U3 cerradas (v12.10/v12.18) desaparecían sin abortar. Fix: `_hilo_tiene_enriquecimiento` reconoce ahora `relaciones` no vacías; `merge_no_destructivo` preserva el array del previo si la salida nueva no lo trae. Test verificado: regeneración íntegra conserva las 15 entradas; diff sobre canónico = solo bump automático de `_meta` (`v12.18 → v12.39`). Validadores estructural + cross-unidad sin regresión (0 errores; 197 avisos legacy + alertas R1/R4 conocidas).

## [v12.38 — 2026-05-29] — Erratum documental: corrige descripción técnica del re-saneado en v12.37

Solo documental. La entrada de v12.37 contenía dos frases técnicamente incorrectas que se rectifican aquí sin tocar datos:

- (1) v12.37 afirmaba: *«el agregado bucket-level `fuentes` incorpora `p13-act9@R`»*. **Falso**: la verificación `git show e60945a^:U1` contra `git show e60945a:U1` muestra que el array `fuentes` del bucket `Números cardinales` ya contenía `p13-act9@R` antes del commit. El diff real de v12.37 solo redistribuyó `p13-act9` y `p13-act9@R` entre los items `nueve` y `trece`, sin alterar el agregado del bucket.

- (2) Briefing al ejecutor 2 (mensajería, no committed) afirmaba: *«Capa 1 proyecta `cat.fuentes` desde item-level, no desde bucket-level»*. **Falso**: `generar_reciclaje_capa1.py:563-564` literalmente hace `evidencias = cat.get("fuentes") or []`, consumiendo el agregado del bucket. Capa 1 lee bucket-level.

**Consecuencia operativa**: la regeneración de Capa 1 sobre el inventario corregido por v12.37 no debería producir diff (el input que consume Capa 1 — el fuentes agregado del bucket — no cambió). Regenerar es verificación de higiene, no necesidad probada. El grep unívoco sobre `nc1-reciclaje.json` (strings imposibles tras el fix: «3 Nueve», «La cartera es marrón», «Yo eres polaco», «6.ª Miércoles: Informática», «6.ª Viernes: Informática») da 0 matches: no hay deuda editorial literal detectada.

Sin cambios en datos, registry, inventarios ni código.

---

## [v12.37 — 2026-05-29] — Lote de corrección PDF↔JSON (U1 + U2) + protocolo §11 en reglas-operativas

Lote de correcciones detectadas en revisión sistemática PDF↔JSON, framing A (el libro fuente imprime las formas correctas; las versiones anteriores del inventario las habían transcrito mal). **Cinco correcciones de datos en `unidades/U1/U1-nc1-inventario.json` y `unidades/U2/U2-nc1-inventario.json`:**

- **U1-p13-act9 respuesta 3**: «Nueve» → «Trece» (Beatriz dice «tengo trece años»). `_nota` actualizada para reflejar que la transcripción anterior era una lectura errónea del PDF, no una errata del libro.
- **U1-p15-act7 respuesta 5**: «La cartera es marrón» → «La mochila es marrón» (el ítem visible es «mochila» y la respuesta impresa también). `_nota` actualizada.
- **U1-p21-act4 respuesta 4**: «eres» → «soy» («Yo soy polaco»; «Yo eres polaco» es gramaticalmente imposible). `_nota` actualizada.
- **U2-p23-act11**: paquete unificado de coherencia en el horario. (a) Falta agregada: `«5.ª Jueves: C. Sociales»` en `respuestas[]` y `audio.transcripcion`. (b) Realineamiento de la 6.ª fila: la respuesta era `«6.ª Miércoles: Informática»` cuando el PDF imprime Informática en Lunes y Jueves; corregido a `«6.ª Jueves: Informática»` + cuadrícula de la 6.ª fila pasa de `["6.ª", "_____", "", "_____", "", "Informática"]` a `["6.ª", "_____", "", "", "_____", ""]` (Viernes deja de estar pre-impreso, Miércoles deja de ser hueco, Jueves pasa a ser hueco). (c) `audio.transcripcion` realineada con respuestas corregidas.
- **U2-p26-act1 respuesta [3]**: añadido `¿` inicial → «¿Cuántos años tienes?» (coherencia con `palabras_recuadro` que ya tenía la forma con `¿`).

**Re-saneado y validador 10/10 0/0/0.** Tras el fix E2 se realinearon las fuentes del bucket `Números cardinales` de U1 con la actividad p13-act9 corregida: (a) `nueve` pierde sus fuentes `p13-act9` y `p13-act9@R` (la palabra ya no aparece literalmente en la actividad — el saneo automático retiró `p13-act9@R`, la `p13-act9` se retiró manualmente por coherencia); (b) `trece` gana `p13-act9` (texto de Beatriz «tengo trece años») y `p13-act9@R` (respuesta corregida «3 Trece»); (c) el agregado bucket-level `fuentes` incorpora `p13-act9@R`.

**Protocolo §11 en `reglas-operativas.md`**: añadida sección «Corrección de errores detectados en revisión PDF↔JSON» — clasificación obligatoria (codificación / editorial del libro / inconsistencia interna del JSON) + regla de coherencia de campos acoplados (`respuestas[]` ↔ `audio.transcripcion` ↔ `datos.cuadricula` ↔ `vocabulario_consolidado.*.fuentes` ↔ `_nota`/`_decisiones_ia` que justifican el dato antiguo). El workflow (validar, bump, coordinación con ejecutor 2) sigue viviendo en `CLAUDE.md` §«Cómo aplicar una corrección sin romper la estructura»; §11 cubre solo criterio + coherencia, no duplica workflow.

**Sin tocar**: registry léxico, `nc1-curso.json`, `nc1-reciclaje.json`, dashboard (lee respuestas dinámicamente). Capa 2 explicaciones no afectadas (no citan literalmente las respuestas corregidas).

**Fuera del lote (revisor)**: E1 propuesto (U0-p11-act8 item 8 «lila») se descarta — el PDF fuente del repo imprime `ele-i-eme-o-ene` en ambos items 7 y 8, JSON coincide, sin error.

---

## [v12.36 — 2026-05-28] — U1 final/ bloqueada con regla path-scoped

Nueva: `.claude/rules/u1-final-locked.md` con frontmatter `paths: ["unidades/U1/final/*.md"]`. Prohíbe editar las 6 secciones cerradas sin permiso explícito previo del autor. Mecanismo path-scoped (mismo patrón que `final-style.md`) para escalar al cierre de U2-U9. No interfiere con `U1-itinerarios.md`, `U1-nc1-*.json` ni `recursos/`.

## [v12.35 — 2026-05-28] — U1 piloto cerrado completo (final/ + itinerario + material)

Hito de cierre del piloto U1. Todas las piezas editoriales de la unidad están terminadas y listas para imprenta:

- **`unidades/U1/final/`**: las 6 secciones cerradas (vocabulario, gramática, comunicación, destrezas, cultura, evaluación) con manual de estilo y manual de objetivos aplicados.
- **`unidades/U1/U1-itinerarios.md`**: itinerario imprimible BÁSICO + EXTENDIDO con páginas/diapositivas listas para insertar en imprenta.
- **`unidades/U1/U1-nc1-material-complementario.json`**: inventario completo de 15 ítems (mc-001 a mc-015) cubriendo PPT, Actividades Extra, Cuaderno de juegos, BLINKLEARNING y vídeo Blinklearning. FT-cuaderno-juegos-NC1 catalogado.
- **`unidades/U1/recursos/`**: PPTX + 3 PDFs fuente + tarjetas.

Marco metodológico estabilizado durante el piloto y reutilizable para U2-U9:

- Manual de estilo (`docs/manual-estilo-final.md`) ampliado en §2.1, §8.1, §10.3-10.8, §11.4, §13. La regla léxica *actividad → ejercicio* vetada también para bloques editoriales (no solo tareas numeradas).
- Plantilla de itinerario en repo B con reglas nuevas: [CASA] una línea, fusión de consecutivos, mini-descripción concreta tipo *Repaso de X / Práctica de X*.
- Schema v2.0 del inventario de material complementario validado en U1 (esquema reutilizable para todas las unidades restantes).

Próximo paso: aplicar el mismo flujo a U2 (final/, itinerario, material complementario). Los 4 archivos fuente de U2 ya están depositados en `unidades/U2/recursos/` y pendientes de procesamiento.

## [v12.34 — 2026-05-28] — U1 itinerario imprimible cerrado + regla léxica ampliada

Nuevo: `unidades/U1/U1-itinerarios.md`. Itinerario imprimible completo (BÁSICO 5 secciones color-coded + EXTENDIDO con Estación de servicio y Materiales complementarios). Reglas nuevas aplicadas y codificadas en plantilla repo B: [CASA] una sola línea, fusión obligatoria de [CASA] consecutivos, mini-descripción de [CASA] en estilo *Repaso de X / Práctica de X / Producción escrita: X*. Reducción sistemática de descripciones [CLASE] largas (~90-100 char). Etiqueta píldora 1.2 corregida (`destreza` → `expresión oral`). Reformulación Destrezas Ej 1 (centrado en comprensión lectora). Evaluación bifurcada en Versión A / Versión B en paralelo.

Ampliado JSON `U1-nc1-material-complementario.json`: 15 ítems (mc-001 a mc-015, BLINKLEARNING completo + mc-015 entrada mínima del vídeo Blinklearning). Páginas/diapositivas añadidas a todas las entradas relevantes del itinerario para inserción imprenta.

Regla léxica `actividad → ejercicio` ampliada en §8.1 manual: ahora cubre también bloques editoriales y referencias internas, no solo tareas numeradas. Excepciones documentadas (nombres propios SGEL: *Actividades Extra*, *Actividad global 1/2*; filenames `actividades_extra.pdf`). Aplicación retroactiva en `U1-nc1-material-complementario.json` (campo schema renombrado + ~13 menciones en texto libre).

## [v12.33 — 2026-05-27] — U1 Evaluación cerrada + material complementario inventariado

Nueva: `unidades/U1/final/evaluacion.md`. Sin insignia. Dos versiones (A — deberes + revisión en clase / B — sesión completa). Iteración fina con el autor: eliminado FEEDBACK FOCALIZADO en ambas; AUTOEVALUACIÓN (B) sintetizada a *"Igual que en la versión A"*. Corrección retroactiva en `destrezas.md`: *actividad/actividades* → *ejercicio/ejercicios* (regla §8.1 ya codificada que se violó por descuido).

Inventario del material complementario: `unidades/U1/U1-nc1-material-complementario.json` (schema v2.0, 9 ítems descritos como actividades/dinámicas) producido por chat separado de extracción. Renombrado para alinear con la convención `U1-nc1-*` del inventario del libro. Material fuente añadido en `unidades/U1/recursos/`: PPTX presentación + 3 PDFs (actividades extra, evaluaciones, cuaderno de juegos NC1).

## [v12.32 — 2026-05-27] — U1 Cultura cerrada

Nueva: `unidades/U1/final/cultura.md`. Sección breve (1 ejercicio + 6 rótulos del docente) sobre tratamiento *tú/usted/vos*. Sin píldora, sin tarjeta de estrategia. Ficha 1.6 (insignia) + ficha 1.7 (tarjetas de rol para dinámica). Iteración fina con el autor: eliminada la reproducción de las 4 fórmulas del cuadro (§10.6) y eliminado el caso *plurilingüe/monolingüe* (NC1 asume lengua común del grupo).

## [v12.31 — 2026-05-26] — U1 Destrezas cerrada (con tarjeta + píldora)

Nueva: `unidades/U1/final/destrezas.md`. Derivación íntegra desde propuesta con aplicación del manual de estilo + protocolo de objetivos + tratamiento de la tarjeta de estrategia *Caza el dato* (comprensión auditiva) y de la píldora formativa 1.2 *Te presento a mi compañero*. Iteración fina con el autor: rótulo *PRESENTE Y PRACTIQUE LA MEDIACIÓN ORAL*, tabla de cambio de persona reformulada (6 filas, columnas YO / MI COMPAÑERO/A), me gusta/le gusta presentado como chunks, presentación oral compactada.

## [v12.30 — 2026-05-26] — U1 Comunicación iterada + 4 reglas nuevas en manual

Iteración fina de `unidades/U1/final/comunicacion.md`: fusión de rótulos (CONTEXTUALICE + PRESENTE EL VÍDEO), referencias a las caras de la tarjeta por contenido (no CARA A/B), eliminación de citas textuales reproducidas del libro, eliminación de referencias a "bloque", restructuración de ENTREGA DE INSIGNIA (rótulo + frase única). Aplicación retroactiva del nuevo estilo de entrega en `vocabulario.md` y `gramatica.md`. Manual ampliado con §10.6 (cuarto bullet), §10.7 (sin bloques en cuerpo), §10.8 (ENTREGA DE INSIGNIA), §2.1 (caras de tarjeta por contenido). §13 con patrón 4 (fusión de rótulos).

## [v12.29 — 2026-05-26] — U1 final/: gramática + comunicación cerradas; manual ampliado

Pieza 2 del piloto `final/`. Nuevos: `unidades/U1/final/gramatica.md`, `unidades/U1/final/comunicacion.md`. Manual `docs/manual-estilo-final.md` con 8 reglas adicionales (§10.3-10.6, §11.4, §2.1, retítulo §10, §13 patrones pendientes). Renombrado masivo *PÍLDORA PROYECTABLE* → *PÍLDORA FORMATIVA* en 13 propuestas de repo A. Aplicación retroactiva §10.4 a `unidades/U1/final/vocabulario.md`.

## [v12.28 — 2026-05-26] — Capa `final/` abierta + piloto U1 vocabulario

Capa `unidades/UX/final/` para versión limpia editable post-InDesign. Piloto cerrado en `unidades/U1/final/vocabulario.md`. Manual de estilo en `docs/manual-estilo-final.md` (autoridad path-scoped vía `.claude/rules/final-style.md`). Migrado `docs/formulacion-objetivos.md` desde repo B. CLAUDE.md raíz reconoce capa `final/` y congelación de repo B desde 2026-05-25.

## [v12.27 — 2026-05-25] — Publicación canónica de U9 — 6 secciones + 1 tarjeta CSV

Mirror al repo A del trabajo editorial de U9 *Ropa* cerrado en repo B (`temporal-antiguo-guia-ia/unidades/U09-propuesta/`). Renaming sin prefijo `U09-propuesta-` según `CLAUDE.md §Flujo de publicación canónica`. Archivos publicados:

- `unidades/U9/propuesta/vocabulario.md`, `gramatica.md`, `comunicacion.md`, `destrezas.md`, `cultura.md`, `evaluacion.md`.
- `unidades/U9/recursos/tarjetas/ropa.csv`.

Snapshot publicado; repo B queda congelado editorialmente — ediciones futuras directamente en repo A.

## [v12.26 — 2026-05-25] — Publicación canónica de U8 — 6 secciones + 3 tarjetas CSV

Mirror al repo A del trabajo editorial de U8 *Descripciones* cerrado en repo B (`temporal-antiguo-guia-ia/unidades/U08-propuesta/`). Renaming sin prefijo `U08-propuesta-` según `CLAUDE.md §Flujo de publicación canónica`. Archivos publicados:

- `unidades/U8/propuesta/vocabulario.md`, `gramatica.md`, `comunicacion.md`, `destrezas.md`, `cultura.md`, `evaluacion.md`.
- `unidades/U8/recursos/tarjetas/caracter-y-personalidad.csv`, `caracteristicas-fisicas.csv`, `partes-del-cuerpo.csv`.

Snapshot publicado; ediciones futuras siempre en repo B y re-publicación canónica al cerrar la siguiente vuelta.

## [v12.25 — 2026-05-25] — Higiene UI: distinguir 3 casos en panel sin explicación

`web/index.html` — `renderRecPanelExplicacion`: cuando un evento no tiene `explicacion`, la UI distingue ahora 3 casos (a) Capa 2 no procesado, (b) etiqueta sin cuadro material, (c) etiqueta y cuadro pero sin explicación redactada. El caso (b) lleva mensaje neutro ("Explicación pendiente — alcance del campo en revisión, Nivel 5") en lugar de la afirmación previa "No requiere explicación editorial" — que pre-juzga la decisión sobre el alcance de `explicacion` que el Nivel 5 punto 5 dejará cerrada (cuadro-bound vs ampliada). Sin tocar lógica de render ni schema.

## [v12.24 — 2026-05-25] — Ampliación §15 cross-hilo multifuente + canal avisos validador (Nivel 5 punto 3)

`schema-reciclaje.md` §6: nuevo shape `relacion_candidata` con `fuente_deteccion` (enum cerrado: `cuadro_compartido`/`actividad`/`indice_curso`/`encuadre_editorial`) + `evidencia` (referencias con formato cerrado por fuente + razonamiento obligatorio para fuentes editoriales). `reglas-reciclaje.md` §15: detección deja de ser cuadro-bound; 3 fuentes editoriales con contrato mínimo de evidencia; política proposal first uniforme para todas las fuentes. `proponer_relaciones_cuadro.py` emite el nuevo shape; `validar_reciclaje.py` valida nuevo shape + retro-compatibilidad legacy con aviso (canal nuevo, separado de errores). REDISEÑO §5 reordenado: 3b reemplazado, abiertos puntos 4-10 (marco lingüístico, rúbrica `explicacion`, 3a verbal, piloto U4, visualización dashboard, retrofit, consolidación mapa A1 como **registro derivado versionado de relaciones canónicas por nivel** — artefacto distinto de los 5 registries de identidades). Migración de las 197 propuestas legacy + materialización de 8 sin espejo: lote posterior. Validador post-cambio: 0 errores, 197 avisos legacy (esperado).

## [v12.23 — 2026-05-24] — Fix despliegue Railway: `Procfile` para Railpack

El build de v12.22 falló porque el panel de Railway tiene **Railpack** (no Dockerfile) como builder activo del proyecto, y Railpack ignora `railway.toml builder=DOCKERFILE`. Error reportado: «No start command detected». Como cambiar el builder del proyecto en el panel no era viable, se añade un `Procfile` en la raíz:

```
web: python diagrama.py
```

Railpack lo interpreta automáticamente como start command. El `Dockerfile` y el `railway.toml` se conservan (siguen siendo válidos si en algún momento se vuelve a forzar Dockerfile como builder en el panel) — no rompen Railpack.

Sin cambios en código (`diagrama.py`, `web/index.html`), datos, registry ni inventarios.

---

## [v12.22 — 2026-05-24] — Reactivación del despliegue del dashboard en Railway (entornoeditorial.up.railway.app)

A petición del autor se **revierte parcialmente la decisión v11.21** y se reabre el carril de despliegue público del dashboard. Se restauran 3 archivos en la raíz del repo:

- **`Dockerfile`** (idéntico al pre-v11.21): `python:3.12-slim` + `gcc`/`libpq-dev` (psycopg2) + `pip install -r requirements.txt` + `EXPOSE 8081` + `CMD ["python", "diagrama.py"]`.
- **`railway.toml`** (idéntico al pre-v11.21): builder `DOCKERFILE`, healthcheck en `/api/status`, restart `ON_FAILURE` x3.
- **`.dockerignore`** (saneado respecto al pre-v11.21): retiradas las 7 líneas `viejo/` muertas (`viejo/` ya no existe en repo A tras la migración a dos repos); conservado `.env`, `.git`, `.claude`, `__pycache__`, `*.pyc`, `unidades/**/fuente/*.pdf`, `*.indd`/`*.ai`/`*.psd`.

**Verificaciones previas:** `/api/status` existe en `diagrama.py:1276` (healthcheck OK); `diagrama.py:1425` lee `os.environ.get("PORT", 8081)` (Railway puede sobrescribir puerto). Sin tocar `requirements.txt`, `diagrama.py`, `web/index.html`, inventarios ni registry. Causa del despliegue fallido reportado: tras v11.21, Railway intentaba autodetectar build sin Dockerfile/railway.toml y fallaba en el paso «Build image». Con estos 3 archivos restaurados, el push reactiva el build.

Bloque B5 de REVIEW deja de estar ⊘ SUPERADO. Variables de entorno del panel de Railway (DATABASE_URL, etc.) las configura el autor directamente en la UI si hacen falta.

---

## [v12.21 — 2026-05-24] — Matriz de decisión para `etiquetas[]` cerrada (Nivel 5 punto 2)

`reglas-reciclaje.md` §3.1 (nueva): matriz determinista para 5 etiquetas (`introduce`/`amplia`/`aplica`/`sistematiza`/`anticipacion`) con 6 predicados (A primera aparición efectiva · B unidad canónica · C unidad canónica posterior · D_any/D_ant evento previo · E cuadro/regla). Dos capas (función principal + 3 coexistencias documentadas). Fuente de B/C: los 5 registries del rediseño, no literalidad de `nc1-curso.json`. Excepción explícita conservada: `amplia` vs `sistematiza` (único juicio editorial residual). §3-bis: `contrasta`/`discrimina` fuera del cierre determinista, con condiciones de reapertura. Matriz validada contra los 89 eventos U0-U3. Punto 2 marcado ✅ en `REDISEÑO-EN-CURSO.md`. Sin tocar schema, scripts, validadores ni canónico.

## [v12.20 — 2026-05-24] — Sincronización documental sobre estado de Capa 2 (Nivel 5 punto 1)

Ejecutado el punto 1 del Nivel 5 (v12.19): `README.md` (tabla de fases L14 + párrafo de estado L162), `fases/2-reciclaje/CLAUDE.md` (banner ⚠️ L7 + coletillas L25 y L44) y `fases/2-reciclaje/prompt.md` (banner ⚠️ L7 + "Lo que NO se hace" L50) dejan de afirmar "Capa 2 no se ha estrenado". Reflejan el estado real: Capa 2 corrida como shakedown en U0-U3 (v11.80, v11.84, v12.4, v12.10, v12.18); contrato sub-procedimentado (etiquetas sin árbol de decisión cerrado, procedencia verbal como excepción, cierre cross-hilo con `tipo`+dirección al humano); cierre operativo abierto en Nivel 5. Añadida regla de gate en CLAUDE.md y prompt.md: **no abrir Capa 2 sobre U4-U9 hasta que el Nivel 5 cierre los puntos 2-4 del plan**.

**Higiene documental adicional** (micro-revisión Anthropic-first sobre `fases/2-reciclaje/CLAUDE.md` y `prompt.md`): (a) eliminada la línea obsoleta `CLAUDE.md:86` que afirmaba "Implementación en código: Nivel 4 (pendiente)" — Nivel 4 está ✅ desde v11.69; sustituida por enlace a los tres scripts + mención del Nivel 5 en curso. (b) Banner de reactivación en `CLAUDE.md:5` y `prompt.md:5` reformulado: "los cuatro niveles" → "los cuatro niveles **originales**" + mención explícita de Nivel 5 abierto en v12.19. Evita que un lector (humano o agente) interprete el rediseño como cerrado y omita el Nivel 5.

Sin tocar contrato (schema, reglas) ni código (scripts, validadores). Punto 1 del Nivel 5 marcado ✅ en `fases/2-reciclaje/REDISEÑO-EN-CURSO.md`.

## [v12.19 — 2026-05-24] — Nivel 5 abierto en REDISEÑO: procedimentalización de Capa 2

Tras revisión crítica del estado de fase 2 (¿es funcional end-to-end si la ejecuta un agente?), diagnóstico cerrado: el modelo, el shape, la Capa 1 y los validadores están vigentes y operativos; lo que está sub-procedimentado es **Capa 2** (etiquetas como definición semántica sin árbol de decisión cerrado; procedencia verbal como excepción explícita; cierre cross-hilo con `tipo` y dirección al humano). Además la doc afirma "Capa 2 no se ha estrenado" mientras U0-U3 ya están enriquecidas en el canónico.

Cambio: nueva sección **Nivel 5 — Procedimentalización de Capa 2** en `fases/2-reciclaje/REDISEÑO-EN-CURSO.md` §5, con 7 puntos ordenados (sincronización documental → matriz de etiquetas → anexos verbal+cross-hilo → decisión `explicacion` → piloto U4 → retrofit U0-U3 → script diferido). Objetivo: contrato ejecutable bajo dos regímenes — Claude Code supervisado hoy y agente autónomo mañana — sin reescritura. No se toca contrato ni schema en este lote; el Nivel 5 declara el plan, no ejecuta los pasos.

## [v12.18 — 2026-05-24] — Capa 2 sobre U3 cerrada (etiquetas + explicaciones + cierres cross-hilo)

Cuarta sesión de Capa 2 IA (después de U0 v11.80, U1 v11.84/v12.4, U2 v12.10). Aplicada sobre los 36 eventos U3 del canónico `nc1-reciclaje.json`:

(a) **36 etiquetas asignadas** según `reglas-reciclaje.md` §3 + lectura del índice del curso U3 (vocabulario principal: Parientes; gramática principal: Presente de los verbos regulares + Interrogativos + Posesivos; pron/orto: sonido /θ/; comunicación con cuadro: La hora). Reparto: 11 `introduce` (Parientes principal U3 + La hora primera aparición canónica + Cine y teatro/Televisión y radio campos culturales nuevos + 3 principales gramaticales + 4 lemas verbales nuevos: comer/escribir/merendar/trabajar), 16 `aplica` (léxico/gramática previa que se reutiliza sin sistematización nueva: Asignaturas/Centros/Días/Edad/N. cardinales/Saludos; Artículos/Concordancia género-número/Pron. sujeto; verbos previos estudiar/hablar/llamarse/ser/tener/vivir), 1 `sistematiza` (Sonidos y correspondencias ortográficas — anticipado en U0, sistematizado primero sonido /θ/ con cuadro@p37#2), 8 `anticipacion` (Profesiones→U6; verbos estar→U5/gustar→U4/hacer Inf→U6/interesar→U4 con gustar/jugar→U6/venir Inf+Pres→U6).

(b) **10 explicaciones editoriales** para los 10 eventos U3 con cuadro (anclados a 5 cuadros únicos: p34#1 paradigma regular, p34#2 interrogativos, p35#1 posesivos, p37#1 La hora, p37#2 sonido /θ/). Mismo criterio que v12.4/v12.10: flujo didáctico, prerrequisitos, arco del curso, contexto de tiempos y formas para verbos. Taxonomía explícita en cada `analisis_ia`: principal U3 / recurrente material / anticipación. Convención v12.10 sobre lemas-modelo respetada: estudiar/vivir en cuadro@p34#1 quedan `aplica` (introducidos U2), comer queda `introduce` (lema nuevo en U3 simultáneamente al cuadro paradigmático).

(c) **15 cierres editoriales de `hilo.relaciones[]`** sobre cuadros U3 (sumados a los 8 de U2, total proyecto 23): 6 `comparte` (paradigma regular: Pron sujeto ↔ {comer, estudiar, vivir} + lemas entre sí), 1 `prerrequisito` direccional (Paradigma regular → Pron sujeto: el cuadro de conjugación depende del paradigma de 6 personas del pronombre), 8 `usa` direccionales (Paradigma → cada lema modelo como vehículo; Interrogativos → Concordancia para Cuánto/-a/-os/-as; Interrogativos → Paradigma para preguntas verbales; Posesivos → Concordancia para nuestro/vuestro; Pron sujeto → Concordancia para nosotros/-as/vosotros/-as; Posesivos → Pron sujeto como columna estructural).

(d) **1 rechazo razonado** — `gram-concordancia-de-genero ↔ gram-paradigma-regular-del-presente-ar-er-ir` (cuadro@p34#2): coocurrencia accidental sin vínculo didáctico. Los verbos regulares NO flexionan en género; ambos aparecen en el mismo cuadro porque los ejemplos de interrogativos llevan verbos conjugados Y el interrogativo Cuánto/-a flexiona, pero entre paradigma verbal y concordancia de género no hay relación operativa.

Validadores: estructural fase 2 en verde (0 errores). Cross-unidad: 14 alertas R1/R4 idénticas a sesiones anteriores, sin regresión. Capa 1 sin tocar. Cuarta unidad enriquecida en NC1 (U0+U1+U2+U3); quedan U4-U9 para futuras sesiones Capa 2.

## [v12.17 — 2026-05-24] — Paso 2b adicional: cierre del split «Práctica del surf» + filtro deprecated en Capa 1

Tras v12.16 el reciclaje seguía arrastrando un hilo huérfano `voc-practica-del-surf` (nivel `mapa`, 0 evidencias, 0 etiquetas) — Capa 1 lo proyectaba porque `nc1-curso.json` U8 sigue diciendo «Práctica del surf» (verbatim del libro, decisión firme), aunque el registry tiene el canónico marcado como `_deprecated` desde v12.13/v12.15. Mismo problema latente con `voc-adjetivos-descriptivos` en U5: regenerar volvía a crear el hilo huérfano.

(a) **Filtro en Capa 1** (`scripts/generar_reciclaje_capa1.py`): nuevo método `Registries.es_deprecated(bloque, titulo)` chequea si la entry del registry lleva campo `_deprecated`. `Constructor.add_evento_mapa` se salta los canónicos deprecated — la entry histórica del registry se conserva como trazabilidad pero ya no produce hilo mapa huérfano en el reciclaje. nc1-curso.json puede seguir mencionando el canónico viejo por convención de verbatim del libro: el filtro vive en Capa 1, no en el índice. Aplica a vocabulario, gramática, pron/orto y perífrasis (verbal queda fuera porque su clave es `lema`).

(b) **`nc1-reciclaje.json` regenerado**: `voc-practica-del-surf` y `voc-adjetivos-descriptivos` desaparecen. Los 5 hilos vigentes del split (`voc-deportes`, `voc-paisaje-y-accidentes-geograficos`, `voc-cualidades-de-objetos-y-lugares`, `voc-caracteristicas-fisicas`, `voc-caracter-y-personalidad`) siguen poblados con sus evidencias completas. Total: 125 hilos.

(c) **Saneo documental del registry léxico**: `_meta.version` pasa de `v1.10` (con prefijo) a `1.11` (sin prefijo, coherente con `version` raíz que ya estaba en `1.11`). `_meta.fecha` actualizada. Narrativa de `_meta.descripcion` extendida con la nota de v1.11.

Validador fase 1: 10/10 0/0/0. Estructural fase 2: 0 errores. Cross-unidad: 14 alertas R1/R4 idénticas, sin regresión. La regla de oro #1 (verbatim del libro en `nc1-curso.json`) queda preservada; los canónicos vigentes son los del registry.

---

## [v12.16 — 2026-05-24] — Paso 2b: regeneración de `nc1-reciclaje.json` tras la recanonización de «Adjetivos descriptivos»

Cierre operativo del briefing del Paso 2b. Antes de este bump, los inventarios + el registry ya reflejaban el split del bucket viejo en 3 buckets nuevos (Paso 2a, v12.11/v12.13), pero `unidades/nc1-reciclaje.json` seguía arrastrando el hilo `voc-adjetivos-descriptivos` proyectado por Capa 1 desde el estado anterior.

(a) **Regeneración determinista**: `python3 scripts/generar_reciclaje_capa1.py` reescribe el canónico leyendo los inventarios saneados (Paso 2a). Resultado: `voc-adjetivos-descriptivos` desaparece como hilo `auto` (queda solo como entry `mapa` derivada del índice del curso, que sigue diciendo «Adjetivos descriptivos» como verbatim del libro — comportamiento esperado, no se toca el índice). Aparecen los 3 hilos nuevos poblados con sus eventos: `voc-cualidades-de-objetos-y-lugares` (auto, U5/U6/U9), `voc-caracteristicas-fisicas` (auto, U8), `voc-caracter-y-personalidad` (auto, U8).

(b) **Limpieza de propuestas obsoletas**: 2 propuestas pendientes `relacion_cross_hilo` que apuntaban al hilo viejo (`prop-rel-gram-adverbios-de-cantidad-voc-adjetivos-descriptivos` y `prop-rel-verb-tener-voc-adjetivos-descriptivos`) eliminadas del array — referenciaban un hilo que ya no existe como auto; la trazabilidad queda en git history.

(c) **Re-detección automática de candidatos**: ejecutado `proponer_relaciones_cuadro.py` (idempotente). Detecta 26 nuevas propuestas cross-hilo con los nombres de los hilos nuevos como pares. Total propuestas: 200 (189 pendientes + 8 aceptadas + 3 rechazadas).

(d) **Saneo del registry — entry `Adjetivos descriptivos`**: a `_deprecated` (v1.9 del otro chat) se le añade en v1.10 el cambio `origen: indice → excepcion` + campo `nota` editorial obligatorio para entradas con `origen=excepcion`. La entry queda como histórica deprecated sin romper el contrato del validador estructural inv-7. Registry: v1.9 → v1.10.

Validador fase 1 (`verificar_integridad.py`): 0/0/0 en los 10 chequeos. Validador estructural fase 2 (`validar_reciclaje.py`): 0 errores contra schema. Validador cross-unidad (`validar_cross_unidad.py`): 14 alertas R1/R4 idénticas al estado anterior, sin regresión. Capa 1 sin tocar (contrato determinista intacto).

Nota: este commit absorbe también los cambios del otro chat al CHANGELOG/REVIEW/registry/U8-inventario que estaban en working tree sin commitear (entrada v12.15 + materialización v12.13 de datos), porque están entrelazados con el saneo del registry que tuve que hacer para que el validador volviera al verde.

---

## [v12.15 — 2026-05-24] — Materialización de los datos de v12.13 (registry + U8) + saneo de referencias fantasma

Aplica los cambios de datos descritos en la entrada v12.13 de este CHANGELOG, que estaba documentada pero no commiteada (la entrada documental llegó a `main` vía el commit v12.14 del otro chat, que tocó CHANGELOG/REVIEW/web sin tocar los datos). Este commit cierra la diferencia.

- `fases/1-extraccion-inventario/campos-semanticos-canonicos.json`: registry v1.9→v1.11. Entry «Deportes» con `_pcic_ref` + `_nc1_ref` + nota; entry «Práctica del surf» con `_deprecated`.
- `unidades/U8/U8-nc1-inventario.json`: bucket «Práctica del surf» eliminado; «Deportes» con scope estricto (surf, surfista, tabla, correa) y «Paisaje y accidentes geográficos» reutilizado para ola/Cantábrico. Listas tipadas p83-act06/07/08 alineadas. `ola.fuentes` saneada (+p83-act7). `_decisiones_ia` actualizada.

**Saneo de trazas fantasma (atendiendo dictamen del revisor):** todas las referencias internas a una versión intermedia `v12.12` / `v1.10` (que existió como working state pero nunca llegó a commitearse) se han colapsado para hablar directamente de `v12.13` / `v1.11`. Afecta a 4 puntos: `_deprecated` y `_nc1_ref` y `nota` del registry, y la entrada `D-Deportes-corrige-Practica-del-surf` de `_decisiones_ia` en U8.

**Working tree saneado:** se descarta una modificación a `unidades/nc1-curso.json` que cambiaba `vocabulario[3]` de U5 de «Adjetivos descriptivos» (verbatim del libro) a «Cualidades de objetos y lugares» (canónico vigente) — modificación no autorizada que rompía regla de oro 1 (verbatim de portada U5) y además hacía fallar el validador `inv-7` (la entry deprecada del registry con `origen=indice` deja de tener literal en nc1-curso.json). Precedente fijado: U8 vocab en nc1-curso.json sigue diciendo «Práctica del surf» (verbatim) aunque el canónico vigente sea «Deportes»; nc1-curso.json espeja el libro, no los canónicos.

Validador 10/10 unidades en 0/0/0 (reproducible desde runtime limpio). Sin tocar `nc1-reciclaje.json` ni `web/index.html`.

---

## [v12.14 — 2026-05-24] — Dashboard reciclaje: vista única «subway» de relacionados + sistema de chips unificado por CSS

Cierre del rediseño del modal del reciclaje tras varias iteraciones exploratorias (variantes A/B/C, P1-P4, radial SVG):

(a) **Vista única «subway»** — tabla con principal arriba (etiquetas en cada celda U0-U9) + relacionados debajo (tipo de relación en celdas de convergencia, vacío fuera). Sin columna "Relación" separada, sin duplicación del principal, sin segunda tabla. Anchos de columna fijos y alineados entre cabecera y cuerpo. Toggle de variantes eliminado.

(b) **Sistema de chips unificado** — clase CSS `.rec-chip` con tamaño, padding, tipografía y border-radius fijos. 4 helpers JS centralizan la creación (`_recChipPastel`, `_recChipBloque`, `_recChipPendiente`, `_recChipGhost`). Todos los chips inline existentes pasan por estos helpers — cambio futuro de tamaño/forma toca solo `.rec-chip`, sin drift posible. Fondos de celda neutros (`var(--md-surface)`); el chip carga el color, no la celda.

(c) **Limpieza masiva de código muerto** — eliminadas ~710 líneas de funciones obsoletas de las exploraciones previas: `_renderRelLayout`, `_filaRelP1`, `_renderRelP2/P3-viejo/P4`, `_renderRelRadial`, `_renderRelV1-V4`, `renderRecMapaSatelites_DEPRECATED`, `renderRecMapaCarriles_DEPRECATED` (comentada), `renderRecCronologia` y `renderRecRamas` deprecated. Variable `window._recRelLayout` retirada.

Sintaxis JS verificada con `node --check`. Sin cambios en datos ni schema; solo CSS/JS.

## [v12.13 — 2026-05-24] — Corrección canónica «Práctica del surf» → «Deportes» + «Paisaje y accidentes geográficos» en U8 (Opción A del revisor)

Decisión editorial en dos pasos consolidados en un solo lote:

**(a) Corrección canónica:** el libro NC1 etiquetó en la portada U8 el campo léxico como «Práctica del surf» — etiqueta hiperespecífica que no es la categoría semántica adecuada para los items que cubre. El canónico vigente pasa a ser **«Deportes»** (PCIC §17, ya existente en el registry desde origen `pcic_a1` v10.115). «Práctica del surf» queda con `_deprecated`.

**(b) Refinamiento del scope (Opción A del revisor):** «Deportes» en sentido amplio forzaba bajo un único canónico léxico heterogéneo (surf/surfista/tabla = deporte y equipamiento; ola/Cantábrico = geografía/topónimo) — `reglas-operativas.md §5.2` prohíbe forzar un único campo cuando el léxico no encaja semánticamente. Se splita en **2 buckets coherentes**:

- **«Deportes»** (PCIC §17): surf, surfista, tabla, correa (4 items deportivos + equipamiento).
- **«Paisaje y accidentes geográficos»** (PCIC §Geo, canónico ya existente desde origen `pcic_a1`): ola, Cantábrico (2 items).

**Listas tipadas U8 p83 alineadas con el split** (corrige incoherencia interna pre-existente):
- `p83-act06`: `['Deportes', 'Paisaje y accidentes geográficos']` (el texto introduce ambas dimensiones).
- `p83-act07`: idem (los V/F trabajan los Cantábricos, olas y surf/tabla).
- `p83-act08`: añadido `'Deportes'` a la lista existente `['Características físicas', 'El cuerpo humano', 'Colores']` (la actividad menciona tabla/surfistas como contexto visual). Coherente con `surfista`/`tabla` cuyas `fuentes` incluyen p83-act8.
- **Fuentes saneadas**: `ola.fuentes` se completa con p83-act7 (estaba pre-existentemente incompleta — «Las olas del Cantábrico son bajas»).

**Registry (`campos-semanticos-canonicos.json` v1.9 → v1.11):**
- Entry «Deportes» enriquecida con `_pcic_ref` + `_nc1_ref` (preservando «Práctica del surf» como traza editorial) + nota con scope estricto.
- «Práctica del surf» con `_deprecated`.
- Versiones meta + raíz sincronizadas.

**`_decisiones_ia` en U8** (`D-Deportes-corrige-Practica-del-surf`) actualizada con la decisión final v12.13 (Opción A).

**Verbatim preservado**: portada U8 sigue diciendo «VOCABULARIO El cuerpo humano. Práctica del surf» (regla de oro 1); `nc1-curso.json` igual. La etiqueta del libro vive como traza editorial en `_nc1_ref`. **Validador: 10/10 unidades 0/0/0.** Sin tocar `nc1-reciclaje.json` (regeneración por el otro chat).

---

## [v12.11 — 2026-05-24] — Ejecución mecánica de la deuda «Adjetivos descriptivos» (Paso 2a — sin regeneración de reciclaje)

Aplicada la migración definida en v12.5/v12.8/v12.9. Cambios estructurales sobre **5 archivos** (inventarios U5/U6/U8/U9 + registry léxico):

- **U5 (`vocabulario_consolidado.principal`)**: bucket `Adjetivos descriptivos` (13 items) → renombrado a `Cualidades de objetos y lugares`. Listas tipadas de actividades/cuadros actualizadas (13 refs).
- **U6 (`vocabulario_consolidado.recurrente`)**: bucket → `Cualidades de objetos y lugares`. 5 refs actualizadas (incluye `famoso/-a` que aquí se confirma como atributo de lugar — Madrid).
- **U9 (`vocabulario_consolidado.recurrente`)**: bucket → `Cualidades de objetos y lugares`. 4 refs actualizadas.
- **U8 (split + movimiento de bucket)**: el bucket `recurrente.Adjetivos descriptivos` se elimina; se crean en `principal` los buckets `Características físicas` (24 items: alto/bajo, guapo/feo, delgado/gordo, joven/mayor, moreno/rubio/pelirrojo/canoso/castaño/calvo, rizado/liso/ondulado, largo/corto, grande/pequeño/oscuro, fuerte, enorme) y `Carácter y personalidad` (9 items: simpático/antipático, divertido/aburrido, trabajador, inteligente, sociable, cariñoso, serio). `famoso/-a` (p89-act7) y `favorito/-a` (p86-act1@R) **expulsados del consolidado** sin canónico nuevo. 22 refs en listas tipadas reescritas: cada actividad recibe el subconjunto de buckets nuevos que realmente contiene (algunas reciben los 2, otras solo 1, las que solo contenían famoso/favorito pierden el tag — ninguna queda huérfana porque todas tenían otros adjetivos).
- **Registry (`campos-semanticos-canonicos.json` v1.8 → v1.9)**: alta de `Cualidades de objetos y lugares` (origen `excepcion`, con `_pcic_ref` + `_nc1_ref` + `nota` por convención obligatoria); `Adjetivos descriptivos` queda como entry con campo `_deprecated`. `Características físicas` (línea 184) y `Carácter y personalidad` (línea 196) **se reutilizan tal cual** sin tocar — ya existían con origen `pcic_a1` desde v10.115.

**Validador:** 10/10 unidades en 0/0/0. **Sin tocar `nc1-reciclaje.json` ni el generador** — la regeneración del reciclaje queda para el otro chat tras coordinación. Sin tocar `web/index.html` (en working tree del otro chat).

---

## [v12.10 — 2026-05-24] — Capa 2 sobre U2 cerrada (etiquetas + explicaciones + cierres cross-hilo)

Tercera sesión de Capa 2 IA (después de U0 v11.80 y U1 v11.84/v12.4). Aplicada sobre los 27 eventos U2 del canónico `nc1-reciclaje.json`:

(a) **27 etiquetas asignadas** según `reglas-reciclaje.md` §3. Reparto: 12 `introduce` (primera aparición canónica — Países hispanohablantes, Asignaturas, Centros e instituciones educativas, Días de la semana, Números ordinales, Adjetivos de nacionalidad, Demostrativos, Mayúsculas, Vocales, estudiar, hablar, vivir), 5 `amplia` (Números cardinales U0+U1→U2 con 21-100, Concordancia de número U1→U2 con pauta -es, Pronombre sujeto U1 3 personas→U2 6 personas, ser/tener U1 singular→U2 plural según índice del curso), 4 `aplica` (Edad/Saludos/Artículos determinados/Concordancia de género/llamarse — contenido ya activo desde U0 o U1), 5 `anticipacion` (Interrogativos→U3, estar→U5, gustar→U4, ir→U6/U7, ir a + infinitivo→nunca sistematizada formalmente).

(b) **9 explicaciones editoriales** escritas para los 9 eventos U2 con cuadro — Pronombre sujeto (p24#1), ser (p24#1), tener (p24#1), Artículos determinados (p24#2), Concordancia de género (p24#2), Concordancia de número (p24#2), Demostrativos (p24#3), llamarse (p25), Mayúsculas (p25). Mismo criterio que v12.4 sobre U1: flujo didáctico, prerrequisitos, arco del curso, contexto de tiempos y formas para verbos. Notable: la explicación de Demostrativos articula la **convergencia de 3 principales U2 en una escena pragmática** (demostrativos forma + ser plural verbo + mayúsculas nombres propios → "Este es Juan, Estas son Laura y Rosa"); Concordancia de género documenta la **primera evidencia de adjetivo invariable** (`grande`) como semilla para U8.

(c) **Primeros 8 cierres editoriales de `hilo.relaciones[]` del proyecto** — todas con sede en U2. 7 `comparte` (Pronombre sujeto↔ser, Pronombre sujeto↔tener, ser↔tener, Concordancia género↔número, Artículos determinados↔Concordancia género, Artículos determinados↔Concordancia número, Mayúsculas↔llamarse) y 1 `prerrequisito` direccional (Demostrativos *requiere* Concordancia de género — los demostrativos U2 aplican la regla -o/-a ya canonizada en U1). De los 173 candidatos cross-hilo pendientes, 8 cerrados; los 86 que tocaban U2 pero compartían cuadros @p20 (cuadro multi-tema de U1) quedan pendientes hasta sesión cross-hilo de U1 explícita; los 79 restantes no tocan U2 directamente. Total propuestas cross-hilo: 8 aceptadas + 165 pendientes.

(d) **`prop-gentilicios-alias-adjetivos-nacionalidad`** rechazada con motivo: la distinción es semánticamente válida (nacionalidad-país vs gentilicio-ciudad/región/continente); decisión editorial fase 1 v10.124 ya separó los buckets; fusionarlos perdería granularidad. Se mantienen ambos hilos autónomos.

Validadores: estructural en verde (0 errores). Cross-unidad: 14 alertas R1/R4 idénticas a la sesión anterior, sin regresión. Capa 1 sin tocar. Tercera unidad enriquecida en NC1 (U0+U1+U2); quedan U3-U9 para futuras sesiones Capa 2.

## [v12.9 — 2026-05-24] — Tabla operativa cerrada para la deuda de «Adjetivos descriptivos» (74 items + 2 expulsados)

Cierre item × destino sobre la taxonomía de v12.8, leyendo fuentes en U5/U6/U8/U9. **Resultado:** 74 items canonizados (24→#1 «Características físicas», 9→#2 «Carácter y personalidad», 41→#3 «Cualidades de objetos y lugares») **+ 2 expulsados del consolidado en U8** sin abrir canónico nuevo: `famoso/-a` (p89-act7 «personajes famosos» — contexto de actividad, no campo léxico nuclear; no se crea canónico de «atributos sociales» sin base material en NC1) y `favorito/-a` (p86-act1@R — palabra de apoyo, no base para canónico «Preferencias» con un único item). Residuo previo resuelto por fuente: `enorme` → #1 (U8 p83-act5 «cabeza enorme» del monstruo, tamaño corporal); `fuerte` → #1 (U8 p86-act1 «joven, fuerte» referido a persona); `famoso/-a` en U6 → #3 (texto sobre Madrid, atributo de lugar). En U8 el bucket pasa a **principal**. **Ejecución mecánica pendiente (Paso 2):** reescritura de las listas tipadas `vocabulario: [...]` en actividades y cuadros de U5/U6/U8/U9 + **alta solo del bucket #3** «Cualidades de objetos y lugares» en `campos-semanticos-canonicos.json` (los #1 y #2 ya existen en el registry desde v10.115 con origen `pcic_a1` — se reutilizan sin duplicar) + retirar canónico viejo «Adjetivos descriptivos» (o deprecated alias) + borrar refs huérfanas a «Adjetivos descriptivos» en U8 p89-act7 y p86-act1@R sin reemplazo + revalidar 10/10 0/0/0 + regenerar `nc1-reciclaje.json`. **Requiere coordinación con el otro chat antes de ejecutar.** Sin cambios de código, registry ni inventarios en este bump. Tabla completa documentada en `REVIEW.md` (Bloque B).

---

## [v12.8 — 2026-05-24] — Taxonomía cerrada para la deuda de «Adjetivos descriptivos» (3 buckets canónicos)

Avance documental sobre la deuda léxica abierta en v12.5: se cierran los **nombres canónicos** de la partición. Los 3 buckets que sustituirán al actual `Adjetivos descriptivos` son: (1) **«Características físicas»** — PCIC §1.1, cubre descripción de personas (cuerpo, cara, pelo, ojos); destino U8 principal. (2) **«Carácter y personalidad»** — PCIC §1.2, cubre rasgos sociales/anímicos; destino U8 principal. (3) **«Cualidades de objetos y lugares»** — sin PCIC A1 directo único (respaldo disperso §43, §3, §52), cubre **todo lo no-persona** (vivienda, objetos, lugares, ropa, entornos); destino U5 principal, U6/U9 recurrente. Decisión deliberada: no se subdivide #3 por dominio (casa/ropa/lugares) porque hay solape masivo entre dominios; la frontera operativa real es «persona vs no-persona». Residuo disuelto caso a caso: `enorme` → #3; `fuerte` → #1 o #3 según fuente; `famoso/-a` → #3; `favorito/-a` → fuera de la taxonomía (es marcador de preferencia, no descriptor). En U8 el bucket pasa a **principal** (la unidad se titula «Descripciones»). **Ejecución sigue diferida al ejecutor 2** como lote único sobre U5/U6/U8/U9; el canónico viejo se retira o queda como deprecated alias. Sin cambios de código, registry ni inventarios. Deuda actualizada en `REVIEW.md`.

---

## [v12.7 — 2026-05-24] — Dashboard reciclaje: tiempos verbales pasan a eje visual neutro

Fix de colisión cromática detectado en revisión: las 4 siglas de tiempo verbal (PRE/IND/IMP/INF) usaban azul/verde/naranja/lila — los mismos colores que las etiquetas editoriales `introduce`/`amplia`/`aplica`/`sistematiza`. El choque más visible: PRE y `introduce` compartían azul. Sustituido por un **eje visual neutro único**: las 4 siglas comparten ahora un cuadradito gris-azulado oscuro (`#455A64`) con la sigla en blanco. Las letras (PRE/IND/IMP/INF) son lo que distingue el tiempo; el color no necesita variar. Mismo lenguaje visual que las iniciales de procedencia (I/E/P/F en gris oscuro con letra blanca) — los dos ejes "neutros" (procedencia + tiempo) quedan agrupados visualmente, los chips de colores se reservan a las etiquetas editoriales. Una sola constante `REC_TIEMPO_VISUAL` reemplaza la tabla anterior por tiempo. Cambio mínimo, sin tocar dato ni schema. JS válido.

## [v12.6 — 2026-05-24] — Dashboard reciclaje: cuadrados, color por tiempo verbal, leyenda rediseñada

Iteración estética del dashboard reciclaje (`web/index.html`) tras revisión visual del autor:

(a) **Círculos → cuadrados redondeados** en toda la timeline (vista principal + modal matriz). Dots de evento, dots vacíos y marcadores de leyenda comparten ahora la misma geometría (cuadrado con border-radius 3-4px) — lenguaje visual unificado con los chips de las celdas.

(b) **Color por tiempo verbal** (nueva `REC_PASTEL_TIEMPO`): PRE Presente → azul, IND Pretérito indefinido → verde, IMP Imperativo → naranja, INF Infinitivo → lila. Cada sigla aparece como cuadradito de color tanto en la timeline (bajo el dot del evento verbal/perifrástico) como en la leyenda y en el modal matriz. Antes era gris neutro y se confundía con el resto del fondo.

(c) **Paleta de etiquetas más saturada** (Material 200 en lugar de 50). Las pastel previas (`#E3F2FD`, `#E8F5E9`…) no tenían contraste sobre el fondo crema; las nuevas (`#90CAF9`, `#A5D6A7`…) mantienen el lenguaje pastel pero se ven. Aplica también a bloques (vocabulario azul, gramática lila, pron-orto cian, verbal coral, perífrasis marrón) y a tipos de relación cross-hilo.

(d) **Leyenda rediseñada como tarjeta** con 3 secciones internas ("Etiqueta del evento" / "Procedencia del índice" / "Tiempo verbal") separadas por líneas divisorias. Cabeceras en 13px mayúsculas con letter-spacing; grid de 260px mínimo por chip para que entradas largas como "reconciliado según el PCIC" entren en una sola línea. Nombres de etiqueta en mayúsculas con peso 600 para empatar con los chips de las celdas.

(e) **Chips sin borde, más minimalistas**: el color de fondo identifica la categoría; el borde era redundante. Tamaño bajado a 9px con padding 2×7. Aplica a chips de etiqueta, tipo de relación, bloque y PENDIENTE.

(f) **Celdas uniformes**: fondo blanco en todas (las filas relacionadas pierden el tinte cream que generaba ruido). La fila del hilo principal del modal se distingue solo por un borde lateral fino del color del bloque a la izquierda del título; la celda seleccionada por sombra sutil + borde interior, sin recuadro grueso azul.

(g) **Línea de fondo de timeline** con gradiente sutil (`transparent → var(--md-outline) → transparent`) y halo blanco alrededor de cada cuadradito para aislarlo de la línea.

Sintaxis JS verificada con `node --check`. Sin cambios en datos ni schema; solo CSS/JS. Cierra la afinación visual sobre Fase 1 + Fase 2 del plan editorial.

## [v12.5 — 2026-05-24] — Deuda léxica catalogada: recanonización **global** del campo «Adjetivos descriptivos»

El canónico único `Adjetivos descriptivos` (`campos-semanticos-canonicos.json:120`) está **sobregeneralizado a escala del curso**, no es un problema local de U8. El mismo bucket vive en U5 (principal, casa/objetos), U6 (recurrente, mixto), U8 (recurrente, mezcla físicas + carácter + residuo) y U9 (recurrente, ropa). U8 es el **caso disparador más evidente**, no el alcance. PCIC separa al menos dos familias: §1.1 «Características Físicas» y §1.2 «Carácter y Personalidad». **Partición mínima a decidir:** (1) «Características físicas» (PCIC §1.1) → bloque físico de U8 + parte de U9 corporal; (2) «Carácter y personalidad» (PCIC §1.2) → bloque social/anímico de U8; (3) tratamiento del residuo heterogéneo (favorito, famoso, fuerte, enorme, grande, pequeño, oscuro en U8) que no encaja en PCIC — decidir si se reasigna, elimina o mantiene canónico genérico; (4) revisión paralela del bucket vivienda/objetos de U5 (probable PCIC §43 Vivienda) y del bucket ropa de U9 (probable PCIC §3 Vestuario). En U8, además, el bucket debería pasar a **principal** (la unidad se titula «Descripciones»), no recurrente. **Resolución diferida al ejecutor 2** con deliverable explícito que cubra **U5, U6, U8 y U9 simultáneamente**: tabla completa de items por unidad con columnas (a) PCIC destino, (b) decisión canónica, (c) bucket destino (principal/recurrente), (d) impacto en hilos cross-unidad y relato histórico. **Convención obligatoria al canonizar (aplicable a todo nuevo campo léxico):** cada entry del registry debe declarar (a) `_pcic_ref` (PCIC de respaldo) **y** (b) la categoría literal del libro NC1 que lo introduce (índice general, portada de unidad o etiqueta interna del cuadro) — preserva trazabilidad libro↔PCIC↔canon. **Prohibición de ejecución parcial:** la partición se ejecuta como lote único sobre el conjunto del canónico, o no se ejecuta. Sin cambios de código, registry ni inventarios en este bump. Deuda registrada en `REVIEW.md` (Bloque B).

---

## [v12.4 — 2026-05-24] — Capa 2 sobre U1 — explicaciones editoriales + paleta pastel unificada

Dos hitos en un lote:

(a) **Fase 2 del plan editorial cerrada — explicaciones de cuadros U1**. Se redactan e inyectan en `unidades/nc1-reciclaje.json` las 12 explicaciones pendientes desde v11.84: 4 de vocabulario (Adjetivos de nacionalidad, Colores, Objetos de clase, Saludos y despedidas), 5 de gramática (Artículos determinados, Concordancia de género, Concordancia de número, Interrogativos, Pronombre sujeto) y 3 verbales (llamarse, ser, tener — Presente). Cada `explicacion` lleva `que_dice_el_libro` (volcado literal del cuadro elegido como fuente representativa), `fuente` (el cuadro principal) y `analisis_ia` con rigor pedagógico — flujo didáctico (no descripción de actividad), prerrequisitos y arco del curso, convivencia con plano verbal (`rasgo_por_tiempo`) cuando aplica, contexto de tiempos y formas para los verbos. Convención aplicada para resolver fuente cuando hay varios cuadros: el cuadro más representativo del paradigma o uso de la categoría (por ejemplo Pronombre sujeto → `cuadro@p14#1` donde aparece como columna del paradigma verbal; Interrogativos → `cuadro@p20#3` donde sistematiza la oposición formal/informal). Helper de escritura en `/tmp/aplicar_explicaciones_u1.py` (no se versiona — uso puntual). Validador estructural en verde tras la inyección. Observación: typo `"Me lllamo"` de `verb-llamarse` U1 anotado en su explicación como deuda menor de verificación de fase 1.

(b) **Paleta pastel unificada en dashboard reciclaje** (web/index.html). Sustituye los chips saturados (texto blanco sobre fondo intenso) del modal por chips pastel (fondo claro + texto oscuro + borde sutil) coherentes con el sistema `cat-tag.p-*` del inventario. Definidos `REC_PASTEL_ETIQUETA`, `REC_PASTEL_REL`, `REC_PASTEL_BLOQUE` + helper `_recChipPastel`. Cambios visibles: (1) section-headers de los bloques (Vocabulario / Gramática / Pron-Orto / Verbal / Perífrasis) pasan de barra saturada con texto blanco a fondo pastel del bloque + texto del mismo tono oscuro. (2) Sub-encabezados de grupo gramatical (Determinantes, Pronombres, …, Tiempos y modos verbales, …) con tipografía más sobria, línea inferior `--md-outline-variant`. (3) Dots de la timeline en pastel — fondo claro, borde sutil, sin halo blanco grueso. (4) Modal matriz: celda seleccionada con sombra ligera + borde interior sutil (sin recuadro grueso azul); chips de etiqueta y de tipo de relación en pastel; cabeceras de tabla con variables `--md-*` globales. (5) Badge de nivel (mapa/auto/detalle) también pastel. Sintaxis JS verificada con `node --check`. Cierra la Fase 1 + Fase 2 del plan editorial; abre paso a Fase 3 (Capa 2 sobre U2-U9 + cierre de propuestas cross-hilo por unidad).

## [v12.3 — 2026-05-24] — Modal del reciclaje rediseñado (cronología → mapa matriz hilos × unidades) + siglas de tiempo en timeline

Rediseño visual del modal del hilo (`web/index.html`, REDISEÑO §4.4). El strip de dots de v11.85-v11.87 se sustituye por un **mapa matriz hilos × unidades** que enseña la trayectoria del hilo actual y las relaciones cross-hilo como filas paralelas. Cada celda U0..U9 lleva la etiqueta del evento como chip en color de la etiqueta + sigla del tiempo (PRE/IND/IMP/INF) si el bloque es verbal/perífrasis. Fila del hilo actual destacada en color del bloque; filas de hilos relacionados debajo con columna "Relación" que lleva el `tipo` (USA, PRERREQUISITO, ACTIVA, CONTRASTA, COMPARTE) en chip de color o PENDIENTE en ámbar para candidatos no cerrados. Click en celda del hilo principal selecciona ese evento (panel de explicación + evidencias se actualizan); click en celda de hilo relacionado abre el modal de ese hilo. Celdas amplias (78×60px) sin monospace. Helper `_recRelacionados(h)` consolida relaciones cerradas + candidatos por cuadro compartido en una sola lista. **Render de tiempos verbales en timeline principal**: para hilos de bloque `verbal` y `perifrasis`, bajo cada dot aparece la sigla del tiempo. Variantes exploradas y descartadas en la misma sesión (carriles paralelos, nodo + satélites) quedan comentadas en el código. Sintaxis JS verificada con `node --check`. Cierra la Fase 1 del plan editorial (infra visual lista para Fase 2: explicaciones de cuadros U1).

## [v12.2 — 2026-05-24] — Dashboard: sub-agrupado por `_grupo` en el bloque gramatical + deuda B.D1 abierta

Cierra el REDISEÑO §6.3 que quedó sin implementar en el dashboard. La vista Reciclaje agrupaba los hilos solo por `bloque`; los 22 hilos gramaticales aparecían en una lista plana, sin sub-secciones por subsistema gramatical. Tras v12.1 (que duplicó visiblemente el grupo "Tiempos y modos verbales" de 1 a 5 hilos), el problema se hizo evidente: el sub-grupo no aparecía como apartado propio. Cambio acotado en `web/index.html` (`renderRecTimeline`): dentro del bloque "Gramática" sub-agrupa por `_grupo` siguiendo el orden canónico del REDISEÑO §6.3 (Determinantes → Pronombres → Sintagma nominal y concordancia → Construcciones → Tiempos y modos verbales → Adverbios y marcadores → Preposiciones). Cada sub-grupo lleva encabezado en color del bloque + conteo de hilos. Sin tocar datos ni schema; retrocompatible (hilos sin `_grupo` caen en "Sin grupo"). Sintaxis JS verificada con `node --check`. **Deuda B.D1 abierta en REVIEW.md** — política general de recurrentes post-principal de paradigmas abstractos (qué entra como `recurrente` en U(>N) cuando hay material atestado sin nuevo cuadro). Derivada del scope B de v12.1 que dejó fuera 3 grupos (paradigma regular del presente como recurrente en U4-U7, Uso del imperativo recurrente en U7, o→ue recurrente en U8 con caso mixto `doler`). No bloquea cierres actuales — es completitud editorial.

## [v12.1 — 2026-05-23] — Reconciliación fase 1 ↔ registry v1.7 grupo "Tiempos y modos verbales"

Cierra la divergencia entre `gramatica-canonica.json` v1.7 (que dio de alta 5 categorías nuevas del grupo "Tiempos y modos verbales" el 2026-05-21 vía §2-bis) y los inventarios U3/U4/U6/U7, que no las consolidaban. Editorialmente cerrado siguiendo el criterio §6.4 REDISEÑO (canonización anclada a evidencia material). Cambios: (a) **5 entradas nuevas en `gramatica_consolidada`**: U3 principal "Paradigma regular del presente (-ar/-er/-ir)" (lemas modelo del cuadro@p34#1: estudiar/comer/vivir, 18 formas paradigmáticas completas), U4 principal "Irreg. vocálica e→ie" (lema testigo querer, 6 formas), U6 recurrente "Irreg. vocálica e→ie" (lema testigo cerrar, 5 formas), U7 principal "Irreg. vocálica o→ue" (lemas testigos del cuadro@p74 y cuadro@p75#1: acostarse paradigma completo, dormir y volver con formas atestadas, 13 formas), U6 principal "Uso del imperativo — instrucciones y peticiones" (7 enunciados pragmáticos, eje distinto de "Imperativo (tú)" flexión). (b) **Registry**: `_nota` añadida a "Infinitivo simple" — el alta v1.7 se conserva pero la categoría no baja a inventarios ni se proyecta como hilo, sin evidencia material suficiente para bajar a gramatica_consolidada ni proyectarse como hilo propio (las apariciones registradas son flexión paradigmática del imperativo o uso distribuido como segundo elemento de perífrasis y forma de cita de reflexivos, sin cuadro propio de las funciones PCIC §9.4.1). (c) **Notas en `_decisiones_ia`**: anticipaciones documentadas editorialmente en U1, U2 (regular del presente), U5, U6 (o→ue) — quedan como contexto para futura revisión de fase 2 / Capa 2; no las detectan automáticamente ni R1 ni la Capa 1 actual. U6 añade matización a la decisión v10.156 (no la contradice: aquella rechazó una formulación-saco, las altas v1.7 son paradigmas separados). (d) **`nc1-reciclaje.json` regenerado** sin tocar el generador; los 5 hilos faltantes quedan proyectados por Capa 1 (grupo "Tiempos y modos verbales" pasa de 1 a 5 hilos). Validadores estructural en verde; cross-unidad sin regresiones (14 alertas R1/R4 idénticas, son de datos preexistentes). Scope B: no se reabre la cola recurrente del paradigma regular del presente en U4-U7 ni la del imperativo en U7 — queda como debate de política general aparte.

## [v12.0 — 2026-05-23] — Nota correctiva: v11.57 no cerró la proyección end-to-end del registry gramatical

v11.57 cerró el **paquete documental** del registry gramatical (5 categorías nuevas del grupo «Tiempos y modos verbales» canonizadas en `gramatica-canonica.json` v1.7), **no la proyección end-to-end** hacia inventarios y fase 2. Concretamente: las 5 categorías no se retroinyectaron en `gramatica_consolidada` de U3/U4/U6/U7, y `generar_reciclaje_capa1.py` (que lee inventario + índice, no `_apariciones` del registry) no las proyecta a `nc1-reciclaje.json`. Esta divergencia entre registry, inventarios y Capa 1 queda documentada como deuda viva en `REVIEW.md` (Bloque B). **Resolución diferida al ejecutor 2** — exige decidir frontera de modelo verbal/gramatical antes de reescribir inventarios. Sin cambios de código en este bump (`generar_reciclaje_capa1.py` intacto; inventarios U3/U4/U6/U7 intactos).

---

## [v11.99 — 2026-05-23] — Fix U8: foto de portada tiene 5 personas, no 4

Rectificación de `portada.descripcion` en U8 (revisión del autor): la foto lateral de p.82 muestra cinco jóvenes, no cuatro como se había anotado en v11.97. Validador 0/0/0.

---

## [v11.98 — 2026-05-23] — Portada U9 (Ropa, p.92) — cobertura completa U0-U9

Añadido `portada` a U9: número «9», título, foto de chica en tienda de ropa y los 5 epígrafes del índice. **Cobertura completa**: U0-U9 ya tienen `portada` rellena. Validador 10/10 unidades 0/0/0.

---

## [v11.97 — 2026-05-23] — Portada U8 (Descripciones, p.82)

Añadido `portada` a U8: número «8», título, foto de grupo de 4 jóvenes con ropa de invierno y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.96 — 2026-05-23] — Portada U7 (Hábitos, p.72)

Añadido `portada` a U7: número «7», título, foto de manos enjabonadas bajo el grifo y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.95 — 2026-05-23] — Portada U6 (¿A dónde vas?, p.62)

Añadido `portada` a U6: número «6», título, foto de chica en sección de productos frescos y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.94 — 2026-05-23] — Portada U5 (¿Dónde están las llaves?, p.52)

Añadido `portada` a U5: número «5», título, foto de llavero con casita de madera y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.93 — 2026-05-23] — Portada U4 (Comidas y bebidas, p.42)

Añadido `portada` a U4: número «4», título, foto de platos servidos en mesa y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.92 — 2026-05-23] — Portada U3 (La Familia, p.32)

Añadido `portada` a U3: número «3», título, foto de pícnic familiar y los 5 epígrafes del índice. Validador 0/0/0.

---

## [v11.91 — 2026-05-23] — Portada U2 (Países de habla hispana, p.22)

Añadido `portada` a U2: número «2», título, foto de 3 jóvenes en piragua y los 5 epígrafes del índice. Errata del libro «datos pesonales» (sic) mantenida verbatim. Validador 0/0/0.

---

## [v11.90 — 2026-05-23] — Portada U1 (¡Hola!, p.12)

Añadido `portada` a U1: número «1», título «¡Hola!», foto de dos chicos y los 5 epígrafes del índice (VOCABULARIO/GRAMÁTICA/COMUNICACIÓN/DESTREZAS/CULTURA con sus contenidos). Validador 0/0/0.

---

## [v11.89 — 2026-05-23] — Portada U0 (Punto de partida, p.8)

Añadido `portada` al inventario de U0 (`unidades/U0/U0-nc1-inventario.json`). Unidad atípica sin numeración: capturados verbatim el título («Punto de partida»), la foto de cubos con letras del abecedario y el índice de cuatro epígrafes. Validador 0/0/0.

---

## [v11.88 — 2026-05-23] — Schema fase 1: campo `portada` opcional (apertura de unidad)

Nuevo campo top-level opcional `portada` en el inventario, para capturar la columna de apertura de cada unidad (número + título + fotos temáticas, siempre 1.ª página de Vocabulario, columna izquierda). Es metadato de unidad — ni actividad ni cuadro — por eso va al nivel de `titulo`/`nivel`. Shape: `{pagina: int, descripcion: str (verbatim)}`. **Campo opcional**: no rompe U0-U9 (validador 0/0/0 tras el cambio). `schema-inventario.md` §1 (recuento + jsonc) + nueva §1.1 con shape y semántica. `validar_inventario.py`: `portada` en `CLAVES_TOP_OPCIONALES` + chequeo de shape (si presente: ambas subclaves obligatorias, `pagina` int, `descripcion` str no vacío). Corregida también la inconsistencia preexistente en §1: recuento decía "13 obligatorias" pero L54 ya decía 12 (tras la eliminación de `contenidos_indice` en v11.67). Próximo: rellenar `portada` unidad por unidad leyendo el PDF, empezando por U0.

---

## [v11.86 — 2026-05-23] — Relaciones cross-hilo: contrato + helper de candidatos por cuadro compartido

Capa contractual de las **relaciones cross-hilo** (qué se apoya en qué, qué contrasta con qué). `schema-reciclaje.md` §6 amplía el enum de `propuestas.tipo` con `relacion_cross_hilo` y añade el payload **no dirigido** `relacion_candidata: {hilos: [a, b] ordenados, cuadros_compartidos}` — la propuesta candidata identifica un par sin asignar origen ni destino; la dirección (cuando el `tipo` la requiere) se decide solo al aceptar, evitando sesgar editorialmente por orden alfabético. Nueva §7 introduce `hilo.relaciones[]` (lectura editorial cerrada — `hilo_ref`, `tipo` enum cerrado de 5 valores, `detalle`, `unidad_relevante?`) con frontera explícita frente a `detalle.enlaces`; §7-Notas renumerada a §8. `reglas-reciclaje.md` §15 define los 5 tipos (`usa`, `prerrequisito`, `activa` direccionales; `contrasta`, `comparte` simétricos) con criterio + ejemplo, política de extensión del enum y política de cierre (en aceptación el humano elige `tipo` y, si direccional, qué hilo del par actúa como origen). `glosario.md` añade entrada para `hilo.relaciones[]`. `scripts/proponer_relaciones_cuadro.py` detecta pares de hilos que comparten cuadro en una misma unidad y crea/actualiza propuestas pendientes idempotentemente (id canónico del par ordenado vía `id_relacion_par(a, b)` — único constructor compartido por helper y futuro flujo de cierre). `scripts/validar_reciclaje.py` endurece el gate: valida `hilo.relaciones[]` (referencia existente, sin autorreferencia, tipo enum, `unidad_relevante` en `_meta.unidades_cubiertas`) y `relacion_candidata` cuando tipo=relacion_cross_hilo (`hilos` lista de 2 strings distintos, ordenados, ambos existentes; cuadros con prefijo `cuadro@`; `hilo_ref` y `hilo_destino` rechazados explícitamente para este tipo). Helper en dry-run sobre el canónico v11.85 detecta 173 candidatos — no se escribe ni se ejecuta sin orden explícita. Rediseño visual del modal queda para v11.87 (cuando haya `relaciones` cerradas que visualizar).

## [v11.85 — 2026-05-23] — Dashboard: drawer lateral → modal centrado (REDISEÑO §4.4)

Refactor del drawer del reciclaje en `web/index.html`. La columna lateral de 480px no daba espacio para explicaciones largas ni para el modal a página completa que el rediseño pide para `nivel: detalle` (§4.4). Sustituido por un **modal centrado** sobre overlay semi-transparente (rgba 0.55), con ancho `min(760px, 94vw)`, altura `max 88vh`, scroll interno, bordes redondeados y sombra elevada. Click fuera (overlay) cierra como antes. El id `rec-drawer` se conserva por compatibilidad con el JS — solo cambia el posicionamiento CSS. Sin tocar lógica de render ni datos. Sintaxis JS validada con `node --check`. Prepara la infraestructura para la siguiente iteración de explicaciones detalladas de Capa 2.

## [v11.84 — 2026-05-23] — Capa 2 sobre U1: etiquetas + propuestas (explicaciones pendientes)

Segunda sesión real de Capa 2 IA, sobre U1. Aplicado a `unidades/nc1-reciclaje.json`:

- **21 eventos U1 con etiquetas editoriales**: 9 `introduce`; 1 `amplia` (Números cardinales — U0 introdujo 0-10, U1 amplía 1-20); 1 `aplica` (Para la clase); 4 `anticipacion` (Adjetivos de nacionalidad → U2; Interrogativos → U3; Signos de puntuación → U7; Sonidos y correspondencias); 2 `[introduce, sistematiza]` (Artículos determinados con cuadro@p14#2 paradigma completo; verbal · ser con cuadros sistematizadores); 2 `[introduce]` verbal (llamarse, tener); 1 `[sistematiza]` (`voc · Saludos y despedidas` U1 — corregido durante la sesión: si U0 marcó `[anticipacion]`, U1 no puede ser `[introduce]`; lo correcto es `sistematiza` — U1 recoge lo activado en U0 y añade despedidas + registro formal/informal); 1 evento sin etiqueta (`voc · Gentilicios` U1 — en limbo hasta resolver la propuesta de alias).
- **Procedencia verbal decidida por Capa 2**: los 3 lemas (ser, llamarse, tener) → `reconciliado · "indice:Verbos ser, llamarse y tener (formas singulares)"`.
- **2 propuestas de la sesión U0 resueltas (rechazadas)**: `prop-abecedario-cobertura-cross-unidad` (fase 1 separó correctamente Abecedario vs Nombres de las letras); `prop-saludos-y-despedidas-vocab-vs-cultura` (cultura fuera del scope; se queda como vocabulario).
- **1 propuesta nueva abierta**: `prop-gentilicios-alias-adjetivos-nacionalidad` — diferida a U2.

**Pendiente declarado**: las **explicaciones** de los cuadros de U1 quedan sin escribir. El autor señaló que el criterio editorial necesita más rigor — las explicaciones deben ser flujos didácticos detallados, no descripciones de actividades, y deben aplicarse a cada etiqueta (incluyendo verbos con contexto de tiempos y formas) no solo a eventos con cuadro. Se redactan en próxima iteración tras tener el modal centrado del dashboard activo. Observación: typo `"Me lllamo"` en `verb · llamarse` U1 heredado del inventario fase 1.

Validador estructural sin errores. `_meta.version` sincronizado por el hook v11.82.

## [v11.83 — 2026-05-23] — Rectificación cobertura U7 · campo "Animales domésticos y salvajes"

Detectado por el autor: el CSV `unidades/U07-propuesta/tarjetas/csv/animales.csv` solo cubría 14 animales, alineado con `items[]` del inventario. Pero la nota `D-Animales-amplios` (v10.161) declaraba 18 lemas como ampliación del campo desde los textos de Destrezas (p78, p79) y solo se habían materializado 3 (orangután, yegua, potro); los 15 restantes faltaban en `items[]`.

- **Inventario** `unidades/U7/U7-nc1-inventario.json`: `items[]` 14 → 29 (+mamífero, anfibio, reptil, ave, ciervo, cebra, rana, tortuga, cocodrilo, víbora, pitón, boa, paloma, loro, cacatúa, en singular canónico). `fuentes` del campo ampliadas con `p78-act1`, `p78-act2`. Nota `D-Animales-amplios` reformulada como registro de la rectificación. Validación: 0/0/0.
- **CSV** `unidades/U07-propuesta/tarjetas/csv/animales.csv` (repo B): 14 → 29 filas, mismo formato (9 traducciones, 3 combos, sílaba tónica, gramapop).
- **Reapertura puntual de fase 1** en alcance U7 (cerrada en v10.164). Rectificación de cobertura por nota mal materializada, no cambio de contrato.

## [v11.82 — 2026-05-23] — Sincronización automática de `_meta` del canónico (pre-commit hook)

Tras v11.81 (sync manual), el autor pidió que la actualización fuera automática para no depender de la memoria humana. Implementado:

- **`scripts/sync_meta_reciclaje.py`** — idempotente: lee `CHANGELOG.md` (máximo `vX.Y`) y la fecha de hoy, escribe `_meta.version` y `_meta.fecha` en `nc1-reciclaje.json` solo si cambian.
- **`scripts/hooks/pre-commit`** — hook git que detecta si `unidades/nc1-reciclaje.json` está staged en un commit y, si lo está, ejecuta el sync y re-stage del JSON. Si no toca el canónico, no hace nada.
- **Instalación:** `git config core.hooksPath scripts/hooks` (una sola vez por checkout).
- **Documentación:** sección nueva en `fases/2-reciclaje/CLAUDE.md`.

Desde ahora cualquier commit que incluya cambios al canónico (regeneración de Capa 1, escritura directa de Capa 2, ediciones manuales) llevará `_meta.version` actualizado automáticamente. El dashboard refleja siempre la versión real sin intervención.

## [v11.81 — 2026-05-23] — Sync `_meta.version` del canónico (dashboard muestra versión actual)

Higiene. `_meta.version` de `nc1-reciclaje.json` lo escribe el generador de Capa 1; la última corrida fue en v11.76 y se quedó en `v11.77` (lectura del CHANGELOG en ese momento). Tras v11.77→v11.80 el JSON cambió varias veces sin regenerar (Capa 2 sobre U0 en v11.80 escribió etiquetas, explicación y propuestas directamente). El dashboard mostraba `v11.77` en la cabecera, desfasado del estado real. Sincronizado a `v11.81` para reflejar el contenido actual. Solo `unidades/nc1-reciclaje.json` (campo `_meta.version`).

## [v11.80 — 2026-05-23] — Capa 2 sobre U0 cerrada (primera unidad enriquecida)

Primera sesión real de Capa 2 IA completada — shakedown del procedimiento §12 sobre U0 (atípica, "Punto de partida"). Cambios sobre `unidades/nc1-reciclaje.json`:

- **6 eventos U0 con etiquetas editoriales**: `voc · Abecedario español` [introduce]; `voc · Países que hablan español` [introduce]; `voc · Números cardinales` [introduce]; `voc · Para la clase` [introduce]; `voc · Saludos y despedidas` [anticipacion]; `pron · Sonidos y correspondencias ortográficas` [anticipacion]. Corrección de la sesión previa: se retira `sistematiza` de Abecedario y Países — `sistematiza` exige contenido "ya activo" (`reglas §3`), y U0 es primera aparición canónica. Las dos pasan a solo `[introduce]`.
- **Explicación en `voc · Saludos y despedidas` U0** según el cuadro@p11 ("Buenos días / Buenas tardes / Buenas noches") — `analisis_ia` sitúa el evento en el arco U0→U1.
- **2 propuestas editoriales abiertas** en `propuestas[]`:
  - `prop-abecedario-cobertura-cross-unidad` (tipo: `siempre_presente`) — ¿debería el hilo `voc · Abecedario español` recoger eventos en U1+ cuando el inventario alfabético reaparece transversalmente, o ya están cubiertas por otros hilos (sonidos, letras homófonas)?
  - `prop-saludos-y-despedidas-vocab-vs-cultura` (tipo: `reconciliacion`) — tensión entre fase 1 (lo categorizó como `vocabulario`) y el curso (lo declara como `cultura` en U1). El contenido es funcionalmente pragmático; decidir si reclasificar el hilo o aceptar la simplificación léxica.
- Ambas propuestas se difieren a la sesión de U1 — su naturaleza cross-unidad pide ver primero cómo reaparecen los contenidos antes de cerrar la decisión.

Validador estructural sin errores. U0 cumple los criterios §13 (a) chequeo estructural + (c) revisión editorial; las propuestas que afectan a U0 quedan explícitamente diferidas. Primera evidencia del flujo `Capa 1 mecánica → sesión Capa 2 → merge no destructivo` funcionando end-to-end sobre una unidad real.

## [v11.79 — 2026-05-23] — Glosario: documenta las iniciales I/E/P/F del dashboard en `procedencia_indice`

Deuda documental retroactiva. La tabla del glosario raíz para `procedencia_indice` describía los 4 casos editoriales del dashboard pero no enseñaba las iniciales (I/E/P/F) que el dashboard usa. Añadida columna "Inicial dashboard" + nota de que el JSON conserva 3 valores técnicos y las 4 iniciales viven solo en la vista (`REC_PROCEDENCIA_CATS`, `web/index.html`). Solo `glosario.md`.

## [v11.78 — 2026-05-23] — Dashboard drawer: `reconciliado_con` visible como texto persistente

Micro-UX. En v11.77 el chip de procedencia se afinó a 4 categorías (I/E/P/F), pero el `reconciliado_con` completo (`indice:Números 0-10`, `pcic:A1`, etc.) solo era visible al pasar el cursor por el chip (`title`) — invisible en móvil/touch y poco escaneable. v11.78 lo muestra **como texto persistente** en la fila del evento del drawer, en gris claro itálico, precedido por flecha (`→ indice:Números 0-10`). Sin perder el tooltip — el `title` con `procedencia · reconciliado_con` se mantiene como hover-detail. Solo `web/index.html`; sintaxis JS validada.

## [v11.77 — 2026-05-23] — Dashboard: leyenda de procedencia con 4 chips (separa `reconciliado` por prefijo)

Follow-up no bloqueante de v11.76. Ahora que `reconciliado_con` lleva prefijo (`indice:` o `pcic:`), la leyenda del dashboard que decía `[E] reconciliado según el PCIC` para todo era imprecisa. v11.77 divide visualmente la categoría:

| JSON | Rótulo en dashboard | Inicial |
|---|---|---|
| `procedencia: declarado` | contenido del índice | **I** |
| `procedencia: reconciliado` + `reconciliado_con: "indice:..."` | equivalente del índice | **E** |
| `procedencia: reconciliado` + `reconciliado_con: "pcic:..."` | reconciliado según el PCIC | **P** |
| `procedencia: nuevo` | fuera del índice | **F** |

El JSON sigue con 3 valores técnicos (`declarado`/`reconciliado`/`nuevo`) — la sub-división vive **solo en la vista**. Reparto visible hoy: I=78 · E=4 · P=44 · F=3 · sin asignar=154 (verbal). Solo `web/index.html`; sintaxis JS validada con `node --check`.

## [v11.76 — 2026-05-23] — Modelo: triage identitario mecánico (alias + PCIC) + merge no destructivo

Tras revisión del autor de v11.75: la cautela "Capa 1 sin aliases" era una sobrecorrección — `campos-semanticos-canonicos.json` (`origen` + `aliases_indice`) y `gramatica-canonica.json` / `pronunciacion-ortografia-canonica.json` / `perifrasis-canonicas.json` (`_pcic_ref`) ya traen el respaldo estructurado para resolver `reconciliado` mecánicamente. Tres cambios:

**Modelo (REDISEÑO §9, reglas §4, glosario, prompt fase 2, schema §3):**

- `procedencia_indice` se resuelve **íntegramente en Capa 1** para vocabulario, gramática, pron/orto y perífrasis (lee registries). El bloque **verbal queda como excepción** mientras `verbos-canonicos.json` no exponga respaldo estructurado equivalente — la procedencia sale sin asignar y la Capa 2 la decide. Documentado explícitamente.
- `reconciliado_con` amplía semántica con **prefijos obligatorios**: `"indice:<entrada>"` (alias del índice del curso) o `"pcic:<ref>"` (`"pcic:A1"` como fallback). Schema §3 + validador estructural actualizados.
- Capa 2 deja de tener procedencia en su núcleo de tareas: solo verbal o corrección excepcional.

**Generador (`scripts/generar_reciclaje_capa1.py`):**

- `IndiceCurso` preserva la entrada literal del índice para resolver `indice:<X>`; `Registries` expone `campos_raw`, `gramatica_raw`, `pronorto_raw`, `perifrasis_raw` con metadata cruda; nuevo `Constructor.resolver_procedencia()` aplica las reglas mecánicamente.
- **Merge no destructivo**: la regeneración fusiona con el archivo previo — sobreescribe campos mecánicos (`procedencia_indice`, `reconciliado_con`, `evidencias`, `formas`), preserva interpretativos (`etiquetas`, `explicacion`, `detalle`). En `verbal`, donde `procedencia_indice` y `reconciliado_con` son trabajo de Capa 2 (no mecánico), también se preservan — y el detector de pérdidas los considera enriquecimiento editorial. **Abort por defecto ante pérdida**. Flag `--permitir-perdidas` (opt-in) vuelca el detalle en `docs/historico/`.
- `validar_capa1()` relajada: acepta `declarado` / `reconciliado` / `nuevo` y exige prefijo en `reconciliado_con`.

**Reparto nuevo:** 78 declarado · 48 reconciliado (44 con `pcic:`, 4 con `indice:`) · 3 nuevo · 154 sin asignar (verbal). Validadores estructural + cross-unidad sin regresión (14 alertas idénticas, son de datos). Las etiquetas de Capa 2 ya escritas en U0 sobreviven al merge — 0 pérdidas detectadas en esta regeneración.

**Nota UX pendiente**: la leyenda del dashboard `[E] reconciliado según el PCIC` es ligeramente imprecisa ahora que algunos reconciliados llevan prefijo `indice:` (4 de 48). El drawer muestra el `reconciliado_con` completo y eso aclara el caso. Si se valora, una iteración v11.77 puede afinar la rotulación.

## [v11.75 — 2026-05-23] — Modelo: `procedencia_indice` pasa a eje identitario puro (curso-wide, sin aliases)

Corrección de modelo Nivel 1/2 tras feedback del autor en la sesión de Capa 2 sobre U0: el `procedencia_indice` antiguo (§9.1) **mezclaba dos ejes** — pertenencia al índice del curso y temporalidad respecto de la unidad canónica —, produciendo casos donde "Saludos y despedidas U0" salía como `nuevo` aunque el curso lo declara para U1. **Cambio:** `procedencia_indice` se redefine como **eje identitario puro**, evaluado **curso-wide**, sin uso de aliases del registry:

- `declarado` → el título canónico coincide literalmente con una entrada del índice del curso **en cualquier unidad** (no solo la del evento). Lo precomputa la Capa 1.
- `reconciliado` → alias / equivalencia PCIC. Decisión de Capa 2, propuesta + cierre humano. **La Capa 1 no usa aliases para `declarado`** (cautela importante: si se metiera el alias por la puerta de atrás, se re-mezclarían los ejes).
- `nuevo` → no aparece en el índice del curso en ninguna unidad ni es reconciliable.

La temporalidad (esta unidad vs la canónica) la lleva **enteramente la etiqueta**: `anticipacion` (antes), sin etiqueta temporal (en su unidad canónica), `aplica` (después).

Archivos: `REDISEÑO-EN-CURSO.md` §9 reformulado · `reglas-reciclaje.md` §4 + §14 R1 sincronizados · `glosario.md` raíz · `scripts/generar_reciclaje_capa1.py` (`IndiceCurso` simplificado a un solo set curso-wide; `declarado()` sin aliases; `add_evento_mapa` decide procedencia con la misma regla) · `nc1-reciclaje.json` regenerado. Reparto nuevo: **100 eventos `declarado`** (antes 41) y 183 sin asignar (para Capa 2 triar `reconciliado`/`nuevo`). Validador estructural y cross-unidad sin regresión (14 alertas R1/R4 idénticas, son de datos).

## [v11.74 — 2026-05-23] — Revisión R1/R4: diagnóstico y dos propuestas anotadas para Capa 2

Lectura una a una de las 14 alertas del validador cross-unidad sobre el canónico v11.68. Ninguna es bug de fase 1. **12 son insumo normal del pipeline**: las 6 R1 (anticipación material) alimentarán la etiqueta `anticipacion` cuando Capa 2 procese U1-U6; 6 de las 8 R4 son léxico PCIC incidental coherente con la unidad (`recurrente` de fondo, §3.6). **2 sospechosas anotadas en bitácora REVIEW** como propuestas a abrir en la sesión de Capa 2 — para no depender de memoria de sesión: `Gentilicios` U1 (posible alias de `Adjetivos de nacionalidad`) y `Bebida` U4 (tensión índice↔contenido — el título "Comidas y bebidas" no cuadra con el principal declarado). Sin tocar datos ni registries; solo registro de la revisión y las dos propuestas pendientes.

## [v11.73 — 2026-05-23] — Higiene: eliminar `diff_index.txt`

Artefacto suelto (140 líneas, un `git diff > …` antiguo, no funcional) colado en v11.72 al usar `git add -A`. Commit aislado solo con el borrado. Compromiso: usar pathspec explícito en `git add` también en repo A para que no se repita.

## [v11.72 — 2026-05-23] — Dashboard RECICLAJE: dos ejes visuales ortogonales (etiqueta + procedencia del índice) con rótulos editoriales

Itera sobre v11.71 a partir de feedback del autor mirando la vista: el evento tiene dos ejes ortogonales (`etiquetas` y `procedencia_indice`, `REDISEÑO §9.5`) y el dashboard solo mostraba uno. Cambios en `web/index.html`:

- **Quitadas las dos notas verbosas de arriba** (nivel + estado de etiquetas).
- **Dos leyendas compactas en su lugar**, una por eje. Cada chip lleva su marca + rótulo + `(n)` con el reparto real; los valores sin presencia se ven atenuados (no fingen estar).
- **Diferenciación no cromática** entre ejes para que ningún chip se pueda confundir con otro: etiqueta sigue como **círculo de color**; procedencia pasa a **cuadrito gris oscuro con inicial mnemotécnica** (`I` contenido del índice · `E` reconciliado según el PCIC · `F` fuera del índice). Los dos ejes hablan visualmente lenguajes distintos (color vs letra) — imposible solapamiento.
- **Rótulos editoriales** para `procedencia_indice` — los técnicos eran opacos al editor:

  | JSON | Dashboard |
  |---|---|
  | `declarado` | **contenido del índice** |
  | `reconciliado` | **reconciliado según el PCIC** |
  | `nuevo` | **fuera del índice** |

  El JSON conserva los valores técnicos; el mapeo a rótulos vive solo en la vista. El drawer también muestra el rótulo editorial.

Glosario raíz (`glosario.md` Bloque 2) actualizado: nueva entrada `procedencia_indice` con tabla técnico↔editorial y significado de cada valor.

Reparto actual visible: 41 eventos `[I]` contenido del índice, 0 `[E]` reconciliado según el PCIC (atenuado), 0 `[F]` fuera del índice (atenuado), 242 sin asignar. Etiquetas: 0/283 (las 7 atenuadas) + 283 sin etiquetar (Capa 2 aún sin estrenar).

## [v11.71 — 2026-05-23] — Dashboard RECICLAJE: corrección UX (badge `auto` y leyenda Capa 2)

Tres correcciones puntuales sobre v11.70, a partir de feedback del autor mirando la vista real:

1. El badge `AUTO` aparecía con fondo lila intenso en las 118 filas con el mismo valor — ruido visual sin información. Ahora solo se muestra como **marcador pequeño sin fondo** y **únicamente cuando el hilo se desvía del nivel dominante** (hoy: ningún hilo se desvía → 0 marcadores por fila).
2. Nueva **nota global discreta** arriba de la vista con el reparto de niveles ("118/118 hilos en `auto`. Esqueleto poblado desde inventarios; la Capa 2 IA aún no ha generado hilos en `detalle`.").
3. La leyenda de "Etiqueta del evento (Capa 2)" prometía 7 colores que **no aparecen** en el render (todos los puntos son grises hoy). Se sustituye por una **nota honesta** que describe el estado-esqueleto y enumera las etiquetas por nombre, no por chip de color. Cuando la Capa 2 corra y existan eventos etiquetados, la nota cambia automáticamente al modo "colores reales".

Solo `web/index.html`; sintaxis verificada con `node --check`. Sin tocar datos ni lógica.

## [v11.70 — 2026-05-22] — Dashboard: vista RECICLAJE adaptada al shape del rediseño

La vista RECICLAJE de `web/index.html` estaba construida para el shape pre-rediseño (`h.tipo`, `ev.accion`, `ev.impacto`, `ev.descripcion`, `h.usos`, `recData.actualizado`) y quedó rota tras la regeneración de `nc1-reciclaje.json` en v11.68 — un consumidor del archivo que la validación de v11.68 no cubrió. Rewire al modelo nuevo: agrupación por `bloque`, badge de `nivel_analisis`, eventos con `etiquetas[]` (chips múltiples), `procedencia_indice` y `evidencias[]`; drawer con `evidencias`/`formas`/`tiempo`; cabecera de la vista con `_meta.fecha`/`estado` y conteo de hilos/propuestas; bloque `propuestas[]` separado al final con estado vacío sobrio. El estado-esqueleto de Capa 1 (eventos con `etiquetas: []`) se representa como **válido** — dot gris, "sin etiquetar (Capa 1)" — sin fingir semántica de Capa 2 inexistente. Solo `web/index.html` (−119 líneas netas: el modelo nuevo es más plano, sin `usos`/`tipos_verbo` anidados); `diagrama.py` sin cambios (`/api/reciclaje` ya sirve el archivo tal cual). Sintaxis JS verificada con `node --check`.

## [v11.69 — 2026-05-22] — Fase 2 REACTIVADA (lote documental)

Levantada la pausa de la decisión 36. El Nivel 4 del rediseño cerró su parte de herramienta (v11.62-v11.68: Capa 1, los dos validadores del gate, `nc1-reciclaje.json` regenerado al shape del rediseño), así que la pausa deja de tener objeto. Lote **documental**, sin lógica nueva: `CLAUDE.md`/`prompt.md`/`reglas-reciclaje.md` de fase 2 actualizados (banners de estado → REACTIVADA; comandos reales del pipeline `generar_reciclaje_capa1.py` y del gate `validar_reciclaje.py`/`validar_cross_unidad.py`); `scripts/integrar_unidad.py` retira el flag `--regenerar-reciclaje` y la lógica de cuarentena — el reciclaje lo gestiona el pipeline de fase 2, no la integración (`REDISEÑO-EN-CURSO.md` §13.4); `CLAUDE.md` raíz, `README.md`, `REVIEW.md`, `PROCESO-MAESTRO.md` sincronizados. **Cautela explícita en los contratos:** la Capa 2 (sesión IA enriquecedora) nunca se ha ejecutado — su primera corrida real será también su shakedown. La reactivación habilita el pipeline; correr la Capa 2 unidad a unidad es la pieza siguiente, no parte de este lote.

## [v11.68 — 2026-05-22] — Fase 2 Nivel 4: regeneración del canónico `nc1-reciclaje.json`

`nc1-reciclaje.json` se regenera con el generador de Capa 1 (v11.62-v11.63): el archivo pasa del shape pre-rediseño v10.114 (181 hilos, claves `curso/_acciones_validas/...`) al shape del rediseño (`_meta/hilos/propuestas`, 118 hilos / 283 eventos). Validado: validador estructural 0 errores contra `schema-reciclaje.md`; validador cross-unidad R1-R5 — pre-condiciones R2/R5 OK, 14 alertas R1/R4 idénticas a v11.65 (son de datos, no regresión de generación). `propuestas[]` queda vacío (el archivo viejo no tenía). Con esto la Capa 1 del pipeline de fase 2 queda materializada de extremo a extremo. **Fase 2 sigue PAUSADA**: la regeneración produce el esqueleto mecánico, no reactiva la fase — pendientes la Capa 2 (sesión IA enriquecedora) y la reactivación operativa. Archivo: `unidades/nc1-reciclaje.json`.

## [v11.67 — 2026-05-22] — Eliminado `contenidos_indice` del inventario canónico

`contenidos_indice` era una copia del índice editorial dentro de cada inventario — duplicación de lo que ya vive en `nc1-curso.json`, desincronizada desde 2026-05-08 (deuda técnica conocida ya registrada en B1.4). Se **elimina**: el índice del curso tiene fuente única en `nc1-curso.json` (regla de oro 4). Campo retirado de los 10 inventarios U0-U9. `validar_inventario.py` deja de exigirlo; `verificar_integridad.py` chequeo 4 limpio (la comparación retirada en v11.66 pasa a definitiva). Contratos de fase 1 actualizados: `schema-inventario.md` (12 claves obligatorias, antes 13), `glosario.md`, `reglas-operativas.md`, `PROCESO-MAESTRO.md`. El dashboard conserva el bloque "Índice de contenidos" leyéndolo ahora de `nc1-curso.json` — `get_inventario` adjunta `_indice_curso` (`diagrama.py` + `web/index.html`). Validación: U0-U9 a 0/0/0, `verificar_integridad.py` 9/9 (0 errores), `validar_cross_unidad.py` sin regresión. Cierra de paso la contradicción glosario↔PROCESO-MAESTRO sobre si `contenidos_indice` debía coincidir o podía divergir.

## [v11.66 — 2026-05-22] — Fase 1: fix del chequeo 4 de `verificar_integridad.py`

Micro-fix de un comparador desactualizado, detectado al implementar v11.65. El chequeo 4 (cabecera↔`nc1-curso.json`) daba 55 falsos positivos: (a) comparaba `nivel` por unidad cuando es un campo **global** de `nc1-curso.json` — corregido a comparar contra el global; (b) comparaba `contenidos_indice` (texto concatenado del inventario, copia abreviada de ~2026-05-05) contra los campos de `nc1-curso.json` (listas, índice fiel al libro, creado 2026-05-08) — divergen en shape y contenido. Esa segunda comparación se **retira temporalmente**: el glosario de fase 1 exige coincidencia exacta de `contenidos_indice` con `nc1-curso.json`, y la vía limpia no es relajar el contrato sino **regenerar `contenidos_indice` desde la fuente canónica** — pieza aparte pendiente (incluye decidir si `contenidos_indice` pasa a listas o se compara texto↔`join(lista)`). Tras el fix, `verificar_integridad.py` pasa entero (0 errores, exit 0). No toca datos de inventario. Archivo: `scripts/verificar_integridad.py`.

## [v11.65 — 2026-05-22] — Fase 2 Nivel 4: validador cross-unidad R1-R5

Componente (b) del gate de cierre (`reglas-reciclaje.md` §13-§14). Nuevo `scripts/validar_cross_unidad.py`. R2 y R5 (pre-condiciones que abortan) se **delegan** a `verificar_integridad.py` (chequeos 1/2/3/5 — regla de oro 4, no se re-implementa lo que fase 1 ya valida); R1, R3, R4 (alertas) se calculan sobre los inventarios. R1 en **versión proxy determinista** (decisión 2026-05-22): detecta categorías `recurrente` en U(n) cuyo `principal` es posterior — anticipación material trazable, descartado el análisis de frecuencia sobre texto crudo por ruidoso. R3: categorías en la dimensión equivocada vs los registries. R4: `recurrente` que nunca es `principal` + lemas verbales en `vocabulario_consolidado`. Ejecución actual: pre-condiciones R2/R5 OK; 14 alertas (R1×6, R4×8, R3×0) — observaciones cross-unidad que el validador per-unidad de fase 1 no puede ver. Hallazgo informativo (no aborta): `verificar_integridad.py` chequeo 4 (cabecera↔`nc1-curso.json`) falla con 55 errores — **no es drift de datos**: el chequeo 4 quedó desactualizado respecto al shape actual de `nc1-curso.json` (compara `nivel` por unidad, que hoy es global, y `contenidos_indice` texto contra listas). Ajeno a R2/R5; arreglo trivial pendiente como pieza aparte de fase 1. Archivo: `scripts/validar_cross_unidad.py` (nuevo).

## [v11.64 — 2026-05-22] — Fase 2 Nivel 4: validador estructural como script

Componente (a) del gate de cierre (`reglas-reciclaje.md` §13). Nuevo `scripts/validar_reciclaje.py` — chequeo estructural de `nc1-reciclaje.json` contra `schema-reciclaje.md` (claves, tipos, enumeraciones); valida el archivo en cualquier estadio del pipeline (salida de Capa 1 o enriquecida por Capa 2 con etiquetas, `reconciliado`/`nuevo`, `explicacion`, `detalle`). `generar_reciclaje_capa1.py` se refactoriza para **importar** ese validador (fuente única, regla de oro 4): su `validar()` se parte en `validar_schema` (compartido) + `validar_capa1` (invariantes §11.4 propias de la salida de Capa 1, que no aplican a un archivo ya enriquecido). Dry-run del generador sin regresión (118 hilos / 283 eventos / OK); validador en seco sobre salida fresca de Capa 1: 0 errores. El canónico `nc1-reciclaje.json` sigue intacto (en shape pre-rediseño, no conforme — esperado hasta el Nivel 4). Archivos: `scripts/validar_reciclaje.py` (nuevo), `scripts/generar_reciclaje_capa1.py`.

## [v11.63 — 2026-05-22] — Fase 2 Nivel 4: proyección `mapa` de la Capa 1

Cierra la laguna declarada en v11.62. `scripts/generar_reciclaje_capa1.py` añade la proyección de nivel `mapa` (§4.2/§4.5): siembra desde el índice de `nc1-curso.json` con resolución **conservadora** — resuelve una entrada del índice a su título canónico solo si la coincidencia es inequívoca (§11.4 invariantes 2-3); las entradas que no resuelven (lemas verbales embebidos en `gramatica`, divergencias de naming con los registries, pron a nivel de subcategoría) se reportan como **avisos**, no se fuerzan. `nivel_analisis` pasa a calcularse según el grado de población (`auto` si el hilo tiene evento respaldado por inventario, `mapa` si solo está declarado en el índice). Dry-run: 118 hilos (auto 118 / mapa 0 — curso íntegramente cubierto) / 283 eventos / 41 con `procedencia_indice: declarado` / 25 avisos / validación OK. El canónico `nc1-reciclaje.json` sigue sin reescribirse. Archivo: `scripts/generar_reciclaje_capa1.py`.

## [v11.62 — 2026-05-22] — Fase 2 Nivel 4: generador de Capa 1 validado en dry-run

Primer paso del Nivel 4 (implementación en código), **checkpoint de herramienta, sin reactivar fase 2**. Nuevo `scripts/generar_reciclaje_capa1.py` — Capa 1 modo íntegro: materializa la **proyección `auto`** del contrato §11 (hilos de los 5 bloques desde inventarios, eventos, `evidencias`, `formas`, `procedencia_indice: declarado`), preserva `propuestas[]` y valida la salida contra `schema-reciclaje.md` + las 10 invariantes §11.4 antes de escribir. Dry-run: 118 hilos / 283 eventos / OK. Laguna conocida: la proyección de nivel `mapa` desde `nc1-curso.json` (§11, `REDISEÑO` §4.2) **aún no se materializa** — todos los hilos salen `auto`; pendiente del Nivel 4. El canónico `nc1-reciclaje.json` **no se reescribe**. Nota empírica diferida añadida en `REDISEÑO-EN-CURSO.md` §7.4. Archivos: `scripts/generar_reciclaje_capa1.py` (nuevo), `REDISEÑO-EN-CURSO.md`.

## [v11.61 — 2026-05-21] — Fase 2: cierre de la deriva terminológica Nivel 3/Nivel 4 en el `CLAUDE.md`

Micro-lote de coherencia tras v11.60. El `CLAUDE.md` de fase 2 aún tenía 6 referencias que situaban la implementación en código en "Nivel 3", contradiciendo el cierre del Nivel 3 (diseño) ya registrado en `REDISEÑO-EN-CURSO.md`: el banner (scripts viejos "se sustituirán en el Nivel 3"), la tabla `nivel_analisis`, "Cómo se invoca", "Cómo se invoca / nivel auto", "Cómo validar" y la tabla "Para qué consultar". Las 6 corregidas: la implementación en código y la sustitución de los scripts viejos son **Nivel 4**; el Nivel 3 (diseño del pipeline) está cerrado. Banner de estado actualizado a v11.61. Sin cambios de modelo — solo coherencia documental; cierra el riesgo documental señalado por el revisor.

## [v11.60 — 2026-05-21] — REDISEÑO fase 2 §13: wiring del pipeline — Nivel 3 (diseño) completo

Última pieza de diseño del Nivel 3. Nueva §13 en `REDISEÑO-EN-CURSO.md` — wiring del pipeline: consolida el encadenado end-to-end (no abre decisiones nuevas). Cinco bloques: propósito; flujo incremental por unidad (Capa 1 → Capa 2 → gate → integración); flujo en hitos cross-unidad (revisión ampliada, que no es regeneración íntegra) y cierre global; puntos de corte y abortos (el gate va después de Capa 2 y antes de integración — si falla, no hay integración a main; la integración la hace el ejecutor coordinador, no la sesión de Capa 2); y **frontera explícita Nivel 3 / Nivel 4** — Nivel 3 define el contrato del encadenado, Nivel 4 lo implementa en código, regenera `nc1-reciclaje.json` y reactiva la fase. **Con esto el Nivel 3 (diseño del pipeline) queda completo.** Corregida en el mismo lote la deriva terminológica que situaba el código en "Nivel 3": `CLAUDE.md` de fase 2 y `prompt.md` (×3) pasan a decir que la implementación en código es Nivel 4. Queda solo el Nivel 4.

## [v11.59 — 2026-05-21] — REDISEÑO fase 2 §12: procedimiento de la sesión de Capa 2

Segunda pieza del Nivel 3. Nueva §12 en `REDISEÑO-EN-CURSO.md` — procedimiento de la sesión IA enriquecedora (Capa 2), que opera sobre el esqueleto de Capa 1 sin reconstruirlo. (1) **Inputs**: el `nc1-reciclaje.json` salido de Capa 1, el inventario de la unidad, `nc1-curso.json`, los 5 registries, el reciclaje actual (para preservar `propuestas[]`), las marcas internas de fase 1 como contexto revisable (no autoridad) y el recorrido previo consolidado de unidades anteriores (necesario para `amplia`/`aplica`/`sistematiza`/`contrasta` y el triage). (2) **Secuencia** de 7 pasos en 3 fases que no se mezclan: precondiciones de arranque (pre-chequeo R2/R5 + shape) · trabajo editorial (3 momentos de análisis, etiquetas, triage, `explicacion`, `propuestas[]`) · gate de cierre. (3) El nivel **`detalle` no es salida obligatoria por unidad**: la pasada por unidad produce etiquetas/triage/`explicacion`/propuestas; el `detalle` se promueve en los hitos cross-unidad cuando el hilo tiene masa crítica. (4) **Régimen**: sesión IA supervisada por unidad en Chat B; la IA propone, el autor cierra o difiere; las `propuestas[]` basta con que queden resueltas o explícitamente diferidas. Queda en el Nivel 3 solo el wiring.

## [v11.58 — 2026-05-21] — Fase 2 Nivel 3: §R.1 procesado — validador cross-unidad R1-R5

Procesada la pieza §R.1 del Reservorio (R1-R5, validación cruzada cross-unidad heredada del rediseño viejo §7). Convertida en contrato operativo: nueva §14 en `reglas-reciclaje.md` — "Validador cross-unidad — R1-R5". Reformulaciones aplicadas sobre el material heredado: **R2** redefinido de "literalidad universal" a **materialidad y trazabilidad** (en vocabulario los ítems aparecen literalmente, en verbal las formas/lema atestiguados, en gramática/pron-orto la categoría trazada a actividades/cuadros — la etiqueta canónica no aparece literal en el libro); **R3** acotado a "errores de clasificación por dimensión". R2 y R5 son pre-condiciones (fallo = bug de fase 1, aborta); R1, R3, R4 producen alertas para el criterio de cierre §13. El nombre del script y el nivel de implementación no se cristalizan — "se difiere al bloque de implementación del pipeline". Con esto el **Reservorio §R queda vacío y se retira** de `REDISEÑO-EN-CURSO.md`: el rediseño ya no tiene material heredado sin procesar. Actualizados el apéndice §N (§7 viejo → cerrado en §14), §5 Nivel 3 y la cabecera del documento.

## [v11.57 — 2026-05-21] — Fase 2 Nivel 3: sincronización del conteo de categorías — paquete de registries cerrado

Cuarta y última pieza del paquete de registries del Nivel 3. Sincronizadas las 5 referencias activas que aún decían "17 categorías" para `gramatica-canonica.json` — stale desde v10.156 (alta de "Imperativo (tú)") y ahora 23 tras las 5 altas de v11.56: `PROCESO-MAESTRO.md` (árbol del repo), `reglas-operativas.md` (×2), `prompt-dry-run.md` y `glosario.md` (tabla de fuentes PCIC). Las menciones "17" en bitácora histórica (REVIEW, CHANGELOG archivado) no se tocan — describen estados pasados, no contrato vivo. **Con esto el paquete de registries del Nivel 3 queda cerrado** (4/4): `perifrasis-canonicas.json` creado · `_grupo` añadido · 5 altas de "Tiempos y modos verbales" · conteo sincronizado.

## [v11.56 — 2026-05-21] — Fase 2 Nivel 3: 5 altas en `gramatica-canonica.json` (Tiempos y modos verbales)

Tercera pieza del paquete de registries, parte 2: las altas. `gramatica-canonica.json` pasa de v1.6 a **v1.7**, de 18 a **23 categorías** — 5 altas nuevas en el grupo "Tiempos y modos verbales", como primera aplicación del procedimiento §2-bis: **Paradigma regular del presente (-ar/-er/-ir)**, **Irregularidad vocálica e→ie (presente)**, **Irregularidad vocálica o→ue (presente)**, **Infinitivo simple** (carril flexión) y **Uso del imperativo — instrucciones y peticiones** (carril uso). Cada una con `_grupo`, `_pcic_ref`, `_apariciones` (verificado por unidad — solo evidencia material con cuadro/sistematización) e `items` (testigos del patrón / ejemplos del cuadro). De los 7 candidatos del relevo, **2 no se canonizan**: los usos del presente ("actual"/"durativo" del PCIC, o el framing didáctico hábitos/describir) — NC1 usa el presente intensivamente pero no lo sistematiza con cuadro propio, así que por §2-bis quedan como **análisis interpretativo de fase 2** (`analisis_ia`/`detalle`), no como categoría de registry. §6.4 de `REDISEÑO-EN-CURSO.md` reformulado: la frontera de canonización se ancla al **umbral de evidencia material**, no al carril (un uso sí entra al registry si tiene cuadro — caso del imperativo). Pendiente (4/4 del paquete): sincronizar las referencias documentales que aún dicen "17 categorías".

## [v11.55 — 2026-05-21] — Fase 2 Nivel 3: §2-bis — procedimiento de canonización de categorías gramaticales

Tercera pieza del paquete de registries, parte 1: el **procedimiento**. Añadida §2-bis a `reglas-reciclaje.md` ("Canonización de categorías gramaticales nuevas"), colocada tras §2 (Naming canónico) sin renumerar §3-§13. Responde a la cuestión de replicabilidad planteada por el autor: las categorías canónicas son específicas del curso, pero el **método para darlas de alta debe ser reproducible** — con otro libro o nivel se re-ejecuta, no se improvisa. Cuatro pasos en orden: (1) fuentes admitidas (plan curricular del nivel + corpus del curso, ambas necesarias; ninguna otra base); (2) separación en dos carriles que no se mezclan — flexión/paradigmas vs usos de tiempos y modos; (3) criterio de alta con umbral de evidencia (evidencia material obligatoria, separación por paradigma/uso real, naming anclado al plan curricular, lo débil o lema-específico no se canoniza); (4) cierre humano (la IA propone, el autor decide, ninguna alta automática). Las 7 altas aprobadas para el grupo "Tiempos y modos verbales" se ejecutarán como primera aplicación de este procedimiento (parte 2, pendiente).

## [v11.54 — 2026-05-21] — Fase 2 Nivel 3: campo `_grupo` en `gramatica-canonica.json`

Segunda pieza del paquete de registries del Nivel 3. Añadido el campo `_grupo` a las 18 categorías de `gramatica-canonica.json` (registry `_meta.version` 1.5→1.6). No es canon nuevo: es una capa de organización interna ya decidida en `REDISEÑO-EN-CURSO.md` §6.3, mapeada sobre categorías que ya existen. Cada categoría se asigna a uno de los 7 grupos por subsistema gramatical — Determinantes (4), Pronombres (3), Sintagma nominal y concordancia (3), Construcciones (3), Adverbios y marcadores (3), Preposiciones (1), Tiempos y modos verbales (1, `Imperativo (tú)` — crecerá en la 3.ª pieza con flexión + usos). Casos frontera resueltos con el autor: `Interrogativos` se queda en Pronombres (la función adverbial de dónde/cuándo/cómo se resuelve en el análisis de fase 2, no abriendo categoría); `Hay` y `Construcción gustar/doler` en Construcciones (construcciones oracionales con verbo fijo, no flexión); `Adverbios y marcadores` se mantiene como grupo único (no se parte en mono-específicos: `_grupo` organiza lectura, la unidad analítica sigue siendo la categoría). No se tocaron nombres canónicos ni `_pcic_ref`. *(Las referencias "17 categorías" en docs de fase 1 — PROCESO-MAESTRO, reglas-operativas, prompt-dry-run — quedan stale desde v10.156; se sincronizan en la 4.ª pieza del paquete, junto al conteo final tras añadir las categorías de "Tiempos y modos verbales".)*

## [v11.53 — 2026-05-21] — Fase 2 Nivel 3: registry `perifrasis-canonicas.json`

Primera pieza del paquete de registries del Nivel 3. Creado `fases/2-reciclaje/perifrasis-canonicas.json` — el 5.º registry del universo cerrado, derivado y propio de fase 2 (ubicado en `fases/2-reciclaje/` por propiedad de fase: fase 1 no lo gobierna ni lo valida, solo transporta `estructura_perifrastica` como dato libre). Poblado desde el relevo del campo `estructura_perifrastica` en los inventarios U0-U9 (solo lectura, sin tocar canon de fase 1): dos perífrasis con evidencia material — `ir a + infinitivo` (U2, U4; con respaldo PCIC A1 §9.1.1) y `querer + infinitivo` (U6; entra por evidencia material de NC1 — PCIC A1 lo trata como infinitivo objeto, no como perífrasis). Documentadas en `_meta`: la deuda de codificación U4↔U6 de `querer + infinitivo` (U4 no la etiquetó como `estructura_perifrastica`; `_apariciones` registra solo U6 hasta corregir U4) y la exclusión de `tener que + infinitivo` del primer corte (sin evidencia material). El universo cerrado pasa a 5 registries — físicamente 4 (fase 1) + 1 (fase 2); path explícito añadido en `reglas-reciclaje.md` §2.

## [v11.52 — 2026-05-21] — REDISEÑO fase 2 §11: procedimiento de la Capa 1 (Nivel 3 arranca)

Arranca el Nivel 3 (implementación) del rediseño de fase 2. Nueva §11 en `REDISEÑO-EN-CURSO.md` — procedimiento de la Capa 1 como contrato de implementación del script determinista. (1) **Inputs**: 4 — `nc1-curso.json`, inventarios cerrados, los 5 registries canónicos, y el estado actual de `nc1-reciclaje.json` (no como fuente del contenido mecánico sino para preservar `propuestas[]` y cierres humanos). (2) **Qué genera**: la proyección mecánica válida contra el schema — hilos (`id`, `bloque`, `titulo`, `_grupo`, `nivel_analisis`) y eventos básicos; nunca `reconciliado`/`nuevo`, `explicacion`, `detalle` ni etiquetas editoriales. (3) **Qué precomputa**: solo lo literal y determinista (`procedencia_indice: declarado`, `formas`, `tiempo`, `evidencias`, `_meta`). (4) **10 invariantes** que la Capa 2 puede dar por garantizados (identidad, canonicidad, tipado, no-duplicación de eventos, no-invención editorial, preservación de `propuestas[]`). (5) **Ejecución**: un mismo algoritmo parametrizado por alcance (incremental/íntegro). Es diseño del procedimiento; el código Python se escribe en la reactivación, cuando los registries estén poblados.

## [v11.51 — 2026-05-21] — Fase 2: limpieza de drift documental antes del Nivel 3

Dos correcciones de coherencia señaladas por el revisor. (1) `CLAUDE.md` de fase 2 §"Cómo se invoca" decía que la pausa de fase 2 dura "mientras el canon semántico de fase 1 está en desarrollo" — contradice el estado real (fase 1 cerrada en v10.164); reformulado: la pausa dura mientras esté pendiente la implementación del Nivel 3 del rediseño. (2) `REDISEÑO-EN-CURSO.md` §6.5 punto 2 seguía diciendo que el `CLAUDE.md` de fase 2 estaba "sincronizado parcialmente" — ya está sincronizado del todo (v11.38/46/48/50); marcado como resuelto. Sin cambios de modelo.

## [v11.50 — 2026-05-21] — Fase 2: sincronización de cabecera del `CLAUDE.md`

Dos ajustes de frescura en `fases/2-reciclaje/CLAUDE.md` señalados por el revisor tras v11.49. (1) El banner "Estado actual" seguía fechado en 2026-05-15 / v10.120 aunque el contenido se había ido actualizando — reescrito a 2026-05-21 / v11.49, reflejando que Nivel 1 y Nivel 2 del rediseño están cerrados y Nivel 3/4 pendientes, sin el detalle obsoleto del bloqueo v10.114. (2) La tabla de `nivel_analisis` presentaba `mapa`/`auto`/`detalle` como "tres niveles que se generan por separado" con los scripts viejos como generador — reformulada al modelo recursivo (grado de población de un mismo hilo, §4.2) y atribuida al pipeline de fase 2 (Capa 1/Capa 2, Nivel 3 pendiente). Sin cambios de modelo; solo coherencia documental.

## [v11.49 — 2026-05-21] — Fase 2 Nivel 2 COMPLETO: prompt envoltorio

Cerrada la última pieza del Nivel 2: nuevo `fases/2-reciclaje/prompt.md`, entry point operativo de fase 2 por unidad — espeja `prompt.md` de fase 1. Cubre: gate de arranque (declarar lectura de los 3 contratos), input/output, flujo Capa 1 (esqueleto determinista) / Capa 2 (sesión IA: 3 momentos de análisis, etiquetas, triage, propuestas), criterio de cierre (§13), y "lo que no se hace". Es un esqueleto-contrato: el detalle del pipeline (scripts de Capa 1, validadores) es Nivel 3, y el prompt lo deja explícito sin fingir que existen. Sincronizado el `CLAUDE.md` de fase 2 ("Cómo se invoca" distingue modelo nuevo/viejo). **Con esto el Nivel 2 (contrato operativo) queda COMPLETO**: fase 2 tiene contrato corto + schema + reglas + prompt, al estándar de fase 1. Siguiente: Nivel 3 (implementación de Capa 1/Capa 2 y validadores).

## [v11.48 — 2026-05-21] — Fase 2 Nivel 2: validación y criterio de cierre

Cerrada la pieza "comandos de validación + criterio de cierre" del Nivel 2. Nueva §13 en `reglas-reciclaje.md`: la validación del reciclaje de una unidad tiene tres partes — (a) chequeo estructural contra `schema-reciclaje.md` (0 errores), (b) validador cross-unidad R1-R5 (sin alertas sin resolver), (c) revisión editorial del autor. El criterio de cierre por unidad exige las 5 condiciones (generado + estructural + R1-R5 + `propuestas[]` resueltas/diferidas + revisión del autor). Los validadores como script son Nivel 3 (pendientes); §13 fija qué deben comprobar. Sincronizado el `CLAUDE.md` de fase 2: corregida la línea desfasada que daba P1 como pendiente (ya ratificada en §12), y la sección "Cómo validar" pasa a apuntar a §13 en vez de a los comandos del modelo viejo. En el Nivel 2 solo queda el prompt envoltorio.

## [v11.47 — 2026-05-21] — Fase 2 Nivel 2: P1 ratificada — contrato de regeneración

Ratificada y formalizada la decisión P1 (almacenamiento de datos enriquecidos), último residuo del Nivel 1. Nueva §12 en `reglas-reciclaje.md` con el contrato de ciclo de vida de `nc1-reciclaje.json`: (1) archivo único canónico `unidades/nc1-reciclaje.json`; (2) los hilos/eventos de nivel mapa/auto no se editan a mano — se regeneran desde los inputs fuente vía el pipeline (excepción: `propuestas[]` y cierres humanos sí se escriben); (3) disparadores — incremental al integrar cada unidad, revisión cross-unidad ampliada tras 3 unidades, regeneración íntegra solo al cierre de bloque; (4) Capa 1 determinista reproducible vs Capa 2 IA con cierre humano persistido en `propuestas[]`; (5) "reciclaje cerrado por unidad" = generado + pasa el criterio de cierre vigente + `propuestas[]` resueltas/diferidas; mientras fase 2 siga PAUSADA, ninguna unidad tiene reciclaje cerrado. Registrada la ratificación en `REDISEÑO-EN-CURSO.md` — el Nivel 1 queda sin residuos.

## [v11.46 — 2026-05-21] — Fase 2 Nivel 2: `reglas-reciclaje.md` reescrito al modelo nuevo

`reglas-reciclaje.md` reescrito íntegro. El archivo arrastraba el modelo viejo (clave `campo_semantico`, `accion` única, `impacto`, lógica de los 2 scripts mapa/auto, comunicación/estrategia como hilos). Reescrito como **autoridad decisional estable de fase 2** destilando el modelo cerrado `REDISEÑO-EN-CURSO.md` §1-§10: §1 granularidad por bloque, §2 naming canónico, §3 etiquetas (lista coexistente, las 7), §4 triage `procedencia_indice`, §5 anticipación híbrida, §6 formas verbales, §7 explicación, §8 siempre-presentes, §9 marcas internas, §10 sufijo `@R`, §11 cuándo escalar como propuesta. Fuera: lógica de scripts (es Nivel 3) y narrativa de transición. Complementa a `schema-reciclaje.md` (shape) con precedencia `schema > reglas`. Sincronizado el `CLAUDE.md` de fase 2: tabla "Para qué consultar" apunta a las nuevas secciones, regla crítica de "acciones" pasa a "etiquetas". Arquitectura documental de fase 2 ahora espeja la de fase 1 (contrato corto + schema + reglas); `REDISEÑO-EN-CURSO.md` queda como documento de diseño, a archivar cuando el rediseño cierre.

## [v11.45 — 2026-05-21] — Fase 2 Nivel 2: schema de `nc1-reciclaje.json`

Arranca el Nivel 2 (contrato operativo) del rediseño de fase 2. Nuevo documento de contrato `fases/2-reciclaje/schema-reciclaje.md` — espeja el rol de `schema-inventario.md` en fase 1, con la misma usabilidad (contrato que un agente puede seguir). Define el shape canónico de `nc1-reciclaje.json`: top-level `_meta` + `hilos[]` (lista plana) + `propuestas[]`; el hilo con `id` slug estable (clave primaria independiente del `titulo`, apta para BD), `bloque`, `titulo`, `_grupo`, `nivel_analisis`, `eventos`, `detalle`; el evento con `etiquetas`, `procedencia_indice`, `formas`, `explicacion`, `evidencias`; el objeto `explicacion` y la propuesta. Shape funcional tanto como archivo JSON (hoy) como en base de datos (futuro) — lista plana = un registro por hilo. Resuelve de paso la pieza "persistencia de decisiones IA" del Nivel 2: bloque `propuestas[]` con `estado` (pendiente/aceptada/rechazada). El `detalle` queda con contrato mínimo (nodos/enlaces); su shape fino se difiere al diseño del modal del dashboard. Referenciado desde `REDISEÑO-EN-CURSO.md` §5 Nivel 2 y la navegación del `CLAUDE.md` de fase 2.

## [v11.44 — 2026-05-21] — REDISEÑO fase 2 §10: componentes "siempre presentes" — Nivel 1 completo

Procesada la última pieza conceptual del Nivel 1: los componentes "siempre presentes no indexados" (conjunciones `y/e`, `o/u`; adverbios `sí/no/también/tampoco`). Movidos del Reservorio §R.2 a sección propia §10 y reconciliados con el modelo §1-§9: un "siempre presente" es un patrón cross-unidad del triage §9 — un contenido que el triage marca `nuevo` sistemáticamente curso a curso. §10 define: detección por la Capa 2 IA en los hitos cross-unidad; tres salidas de propuesta al autor (canonizar en registry de fase 1 / modelar como bloque analítico / ignorar); criterio de ampliación de la lista (presencia sistemática + no declarado + función pragmática). Con esto el **Nivel 1 del roadmap queda completo** — residuo único: ratificación formal de P1, que se hará en el Nivel 2. Actualizados §5, apéndice §N, Reservorio §R (queda solo §R.1) y el puntero de `gramatica-canonica.json._meta`.

## [v11.43 — 2026-05-21] — REDISEÑO fase 2: §9 generalizado + D1 absorbida

Cierre de la pieza D1 (tabla de equivalencias) en `REDISEÑO-EN-CURSO.md`. (1) El triage §9 se **generaliza a los 5 bloques** — la lógica declarado/reconciliable/nuevo no era específica de gramática, vale para vocabulario, gramática, pron/orto, verbal y perífrasis. (2) Nueva §9.5: `procedencia_indice` (triage) y `etiquetas` (§2.3) son **dos ejes ortogonales** del evento — el triage añade un eje, no sustituye las etiquetas; un evento lleva los dos. (3) Nueva §9.6: **D1 queda absorbida por el triage** — el archivo curado `nc1-equivalencias-hilos.json` del rediseño viejo es obsoleto; la reconciliación índice↔canónico es la salida `reconciliado` del triage, resuelta evento a evento como propuesta IA con cierre humano. Actualizados §5 Nivel 1 (D1 retirada) y apéndice §N. Con esto el Nivel 1 del roadmap queda completo salvo §R.2 (siempre-presentes).

## [v11.42 — 2026-05-21] — REDISEÑO fase 2 §9: triage índice

Cerrada la pieza "triage declarado/reconciliable/contenido nuevo" en `REDISEÑO-EN-CURSO.md` (nueva §9). Para gramática y pron/orto: cada aparición de una categoría se clasifica respecto al índice del curso en tres salidas — `declarado`, `reconciliado` o `nuevo`. El declarado literal lo precomputa la Capa 1 (coincidencia mecánica); reconciliable y nuevo los analiza la Capa 2 IA como propuestas con cierre humano (una categoría nueva genera propuesta al autor: canonizar en registry de fase 1 o dejar como hallazgo, tipo §R.2). El estatus se marca por evento (categoría-unidad), registrado en el campo `procedencia_indice`. Además: anclada en §5 Nivel 2 la nota de §8.4 (serialización de `que_dice_el_libro`). Actualizado §5 Nivel 1.

## [v11.41 — 2026-05-21] — REDISEÑO fase 2 §8: carril de explicaciones

Cerrada la pieza "carril propio para las explicaciones gramaticales" en `REDISEÑO-EN-CURSO.md` (nueva §8). La explicación que el libro da de un contenido (el cuadro "cómo se forma X") es un **atributo del evento** — campo `explicacion` — no un hilo propio (un hilo aparte duplicaría el recorrido de la categoría). El campo tiene dos partes: `que_dice_el_libro` (lo que el cuadro expone literalmente) y `analisis_ia` (el trabajo de fase 2: relaciones lógicas, prerrequisitos, incoherencias — fase 2 no copia la fuente, la analiza). Alcance a los 5 bloques, no solo gramática. Es insumo del nivel `detalle` (§4.4), sin solaparse: el `analisis_ia` es local al evento, el `detalle` razona la cadena cross-unidad completa. Además, anclada en §5 Nivel 3 la nota de que el desglose de `formas` por unidad exige leer `actividad.tiempos_y_verbos` al diseñar Capa 1. Actualizado §5 Nivel 1.

## [v11.40 — 2026-05-21] — REDISEÑO fase 2 §7: tratamiento detallado de formas verbales

Cerrada la pieza "tratamiento detallado de formas verbales" en `REDISEÑO-EN-CURSO.md` (nueva §7). (1) El evento verbal (lema-tiempo-unidad) lleva un campo `formas` con las formas conjugadas concretas que esa unidad trabaja — opción A: la forma es dato del evento, no sub-entidad con recorrido propio. La progresión del paradigma se lee comparando los `formas` de eventos sucesivos. (2) `rasgo_por_tiempo` (regular/irregular del lema) se mantiene en el hilo verbal; frontera trazada con el grupo gramatical "Tiempos y modos verbales" (§6.4): atributo del verbo concreto vs flexión abstracta como contenido enseñado. (3) Anticipación de formas en modelo híbrido — fase 2 lee el registro transitorio de fase 1 (`_migracion_rediseno`) y completa el análisis por su cuenta; cierra la costura §6.5 punto 1, incluida la perífrasis anticipatoria (ya no depende de `estructura_perifrastica`). Actualizados §3.2, §5 Nivel 1 y §6.5. Población del desglose por unidad: tarea diferida a la Capa 1.

## [v11.39 — 2026-05-20] — Glosario transversal del proyecto

Nuevo `glosario.md` en la raíz: índice semántico transversal del proyecto (opción B de la decisión documental). El único glosario existente, `fases/1-extraccion-inventario/glosario.md`, no es un glosario general sino la referencia campo por campo del schema del inventario — se mantiene intacto en su sitio. El nuevo glosario global es corto y de orientación: Bloque 1 — 12 términos globales (repo A/B, inventario, registry canónico, PCIC, unidad/unidad atípica, fase, dashboard, modelo IA-first, dry-run, publicación canónica, mirror snapshot, source of truth); Bloque 2 — 10 términos de fase 2 marcados "en estabilización" (hilo, evento, etiqueta, mapa, auto, detalle, Capa 1, Capa 2, reciclaje, anticipación); Bloque 3 — tabla de glosarios de fase con enlaces. Cada entrada: definición breve + "ver detalle en fase X" cuando aplica. Añadida fila en "Documentos clave" del `CLAUDE.md` raíz como documento de Consulta. Los glosarios de fase (fase 2 y siguientes) se crearán cuando su terminología se estabilice.

## [v11.38 — 2026-05-20] — Fase 2: sincronización post-D2

Cierra las tres costuras señaladas por el revisor tras v11.37. (1) `REDISEÑO-EN-CURSO.md` §6.1 precisa la fórmula del universo de hilos: no "los registries de fase 1" sin más, sino los **4 registries de fase 1 + `perifrasis-canonicas.json`** (5.º, derivado, propio de fase 2). (2) Nueva §6.5 que anota explícitamente las dos sincronizaciones que D2 arrastra: la fuente real para detectar perífrasis anticipatorias (fase 1 excluye de `tiempos_y_verbos` los auxiliares anticipatorios, así que `estructura_perifrastica` puede no transportarlas — se resolverá en el paso "formas verbales") y el contrato corto de fase 2 desactualizado. (3) `fases/2-reciclaje/CLAUDE.md` sincronizado: el nivel `auto` ya no se describe solo desde `vocabulario_consolidado` sino desde los 5 bloques; la regla "un hilo por campo semántico" se generaliza a granularidad por bloque (§2.2). Sin cambios operativos — fase 2 sigue PAUSADA.

## [v11.37 — 2026-05-20] — REDISEÑO fase 2 §6: D2 — universo de hilos y sub-organización de gramática

Cerrada la pieza D2 en `REDISEÑO-EN-CURSO.md` (nueva §6). (1) Universo de hilos válidos = los registries canónicos de fase 1; la lista PCIC curada del viejo queda obsoleta. Cerrado para escritura (fase 2 no inventa canónicos), abierto para detección (estructuras no declaradas → hallazgo escalado). (2) Perífrasis gana registry propio `perifrasis-canonicas.json` (5.º registry); la tabla de bloques de §2.2 pasa de 4 a 5 — cierra la incoherencia §2.2↔§3.3. (3) El bloque gramática se sub-organiza con un campo `_grupo` por subsistema gramatical (7 grupos: Determinantes, Pronombres, Sintagma nominal y concordancia, Construcciones, Tiempos y modos verbales, Adverbios y marcadores, Preposiciones). (4) El grupo "Tiempos y modos verbales" integra flexión/paradigmas (regular, irregularidad vocálica, imperativo) + usos de tiempos/modos, canonizados desde PCIC A1 — plano distinto del bloque `verbal` (lista de cada verbo del libro). Población de `perifrasis-canonicas.json` y de las categorías nuevas de `gramatica-canonica.json`: tareas diferidas. Actualizados §2.2, §5 Nivel 1 y apéndice §N.

## [v11.36 — 2026-05-20] — `CLAUDE.md` raíz: árbol del repositorio a mapa de alto nivel

El árbol de "Estructura del repositorio" mezclaba orientación estable (dónde vive cada cosa) con detalle de drift: enumeración exhaustiva de los archivos de `propuesta/`, sello de versión `v10.127` y nota de UI ("7.ª columna del dashboard"). Adelgazado el sub-árbol de `unidades/UX/` a sus 4 subcarpetas canónicas con propósito general. El árbol sigue en CLAUDE.md — es arquitectura/orientación legítima — pero ahora responde solo a "¿dónde vive cada cosa?", no a "¿qué contiene exactamente hoy?". El detalle fino vive en los `CLAUDE.md` de fase o se descubre al vuelo.

## [v11.35 — 2026-05-20] — Adelgazado de `CLAUDE.md` raíz: estado fuera de la autoridad operativa

El `CLAUDE.md` raíz contenía el bloque `## Estado fase 1` (~55 líneas: registries con versiones, convenciones de corrección, comandos, deudas residuales, procedimiento), contradiciendo su propia regla "no añadir aquí historia, estado, planes". Reparto en 3 destinos: (A) el contrato operativo de fase 1 — registries como autoridad de naming (sin columna de versión), convenciones críticas de corrección (sin precedentes con versión), comandos canónicos y procedimiento de corrección — se traslada a `fases/1-extraccion-inventario/CLAUDE.md` (su sitio natural, auto-cargado al trabajar en fase 1); (B) el estado vivo — cierre de fase y deudas — ya vivía en `REVIEW.md`; se compacta la deuda matcher (cerrada en v11.3-v11.5) dejando solo las deudas abiertas; (C) el bloque se elimina del raíz. Resultado: `CLAUDE.md` raíz baja de 209 a 153 líneas, deja de mezclar capas y respeta la separación de funciones que el propio repo declara (CLAUDE = reglas vigentes · REVIEW = estado · CHANGELOG = cambios · PROCESO-MAESTRO = decisiones). Sin pérdida de contenido operativo.

## [v11.34 — 2026-05-20] — Fase 2: integración a documento único de rediseño

`REDISEÑO-EN-CURSO-viejo.md` archivado en `docs/historico/` (`git mv`). El rediseño de fase 2 pasa a vivir en un **documento único**, `REDISEÑO-EN-CURSO.md`. Análisis pieza por pieza del viejo: de sus 8 secciones, §1/§5/§6 son obsoletas, §2/§3-D3/§4-P1 ya estaban migradas, §3-D1 y §3-D2 siguen vivas pero su formulación vieja está superada (D2: la lista PCIC curada queda superada por los 4 registries de fase 1; la pieza sigue pendiente de redefinir), y §7 (R1-R5) + §8 (siempre-presentes) son material vivo sin procesar. Cambios: (1) nuevo apéndice §R "Reservorio" en el activo con §7 y §8 copiados verbatim + prefacio de procedencia/estado; (2) apéndice §N reescrito con la disposición final de cada pieza en tres estados (ya migrado / superado en formulación vieja / en reservorio); (3) §5 Nivel 1/3 actualizado — D2 reformulado, §8 y R1-R5 apuntan al Reservorio, retirada la fila obsoleta "hallazgos del revisor"; (4) referencias activas al viejo actualizadas en el mismo lote: `PROCESO-MAESTRO.md` (árbol), `gramatica-canonica.json` (`_meta.siempre_presentes_no_indexados`), `fases/2-reciclaje/CLAUDE.md` (banner de estado) y header de `REDISEÑO-EN-CURSO.md`. Sin referencias colgantes.

## [v11.33 — 2026-05-20] — Fase 2: decisión de alcance — `comunicacion` y `estrategia` pospuestas

Cerrada la pieza "Cierre de alcance" que estaba pendiente en `REDISEÑO-EN-CURSO.md` §5 Nivel 1. Decisión del autor: el rediseño activo de fase 2 cubre solo los **bloques lingüísticos** (vocabulario, gramática, pronunciación/ortografía, verbal + `perifrasis` derivado); las **funciones comunicativas** y las **estrategias** quedan pospuestas a desarrollo posterior. Sincronización documental: (1) `REDISEÑO-EN-CURSO.md` — pieza retirada de la tabla de pendientes, decisión registrada como nota destacada; (2) `fases/2-reciclaje/CLAUDE.md` — el contrato corto dejó de afirmar que fase 2 modela funciones comunicativas y estrategias, ahora declara el alcance pospuesto; (3) `PROCESO-MAESTRO.md` — entrada nueva en bitácora con el roadmap de reincorporación. Cierra la tensión documental señalada por el revisor tras v11.31.

## [v11.32 — 2026-05-20] — REDISEÑO fase 2: corregida la incoherencia de P1

Micro-lote de consistencia tras v11.31. P1 (almacenamiento de datos enriquecidos) figuraba como "pendiente decisión" en `REDISEÑO-EN-CURSO.md` (§5 Nivel 1 + apéndice), pero el reservorio viejo lo cerró en **opción A** el 2026-05-10 (datos enriquecidos viven en `nc1-reciclaje.json`, regenerado al integrar cada unidad). Reetiquetado en ambos sitios como **decisión heredada a ratificar/formalizar**, no pendiente. La tensión documental de `CLAUDE.md` de fase 2 (cita `comunicacion`/`estrategia` como modelados) se deja intacta a propósito: depende del "cierre de alcance" todavía pendiente en §5 Nivel 1.

## [v11.31 — 2026-05-20] — REDISEÑO fase 2 §5: hoja de ruta del trabajo pendiente

Añadida §5 a `fases/2-reciclaje/REDISEÑO-EN-CURSO.md`: hoja de ruta viva del trabajo pendiente para cerrar el rediseño de fase 2 al estándar de contrato de fase 1. Estructurada en 4 niveles: (1) decisiones de modelo pendientes — incluye cuestiones nuevas (tratamiento detallado de formas verbales, carril propio para explicaciones gramaticales, triage declarado/reconciliable/contenido-nuevo para gramática y pron/orto, cierre de alcance de `comunicacion`/`estrategia`) + piezas heredadas del viejo (D1, D2, P1, §8, hallazgos del revisor); (2) contrato operativo a producir (prompt, schema de `nc1-reciclaje.json`, reglas reescritas, persistencia de decisiones IA, validación y gates); (3) implementación de Capa 1/Capa 2 (procedimiento, validador R1-R5, wiring); (4) reactivación operativa (adaptar scripts, validador cross-unidad, regeneración íntegra, sincronización dashboard/docs). Solo documento de rediseño; fase 2 sigue PAUSADA.

## [v11.30 — 2026-05-20] — Fix de consistencia en `fases/1-extraccion-inventario/CLAUDE.md`

La tabla "Para qué consultar qué archivo" citaba "(regla crítica 6)" al hablar de la política de naming canónico, pero esa es la **regla crítica 7** ("Canon canónico literal"); la 6 es "Documentación de fase 1 obligatoria". Corregida la referencia. Sin cambios funcionales.

---

## [v11.29 — 2026-05-20] — Residuos `ROADMAP.md` / `GITHUB-MANIFEST.md` en REVIEW y PROCESO-MAESTRO

Micro-lote de cierre tras v11.27. Quedaban dos rastros de los archivos retirados: `REVIEW.md` los listaba como filas "⚠ Heredado, sin tocar" en la tabla maestra de archivos del sistema; `PROCESO-MAESTRO.md` los mostraba en el árbol de estructura de raíz. `GITHUB-MANIFEST.md` ya no existe y `ROADMAP.md` nunca existió — ambas referencias retiradas. Cierra el carril de limpieza de raíz.

---

## [v11.28 — 2026-05-20] — Corrección del nombre de repo B en la autoridad documental

CLAUDE.md, README.md y PROCESO-MAESTRO.md nombraban repo B como `guia-sistema-trabajo` (el nombre planeado en v11.13), pero el repo B real es `temporal-antiguo-guia-ia` (renombrado por el otro chat en v11.14). 7 referencias activas corregidas (CLAUDE.md ×4, README.md ×2, PROCESO-MAESTRO.md ×1). Confirmado por el autor (Caso 1): repo B es el sistema de trabajo vivo donde sucede la redacción — el "Modelo de dos repos" y el "Flujo de publicación canónica" siguen válidos, solo el nombre estaba mal. Bitácora histórica de REVIEW intacta (en v11.13 el nombre planeado sí era `guia-sistema-trabajo`). Además: comentario de `integrar_unidad.py` en Comandos básicos actualizado (el flujo ya no usa worktree; el flag de reciclaje quedó en cuarentena en v11.19).

---

## [v11.27 — 2026-05-20] — Eliminado `GITHUB-MANIFEST.md` obsoleto

`GITHUB-MANIFEST.md` (118 líneas, gitignorado, nunca versionado) eliminado. Era el manifiesto de despliegue del sistema de agentes CrewAI en Railway (fechado 2026-03-16): listaba `scripts/crewai/`, `eval/`, `Dockerfile`, `railway.toml`, rutas `datos/inventarios/` — todo migrado a repo B, eliminado o en rutas viejas. Documento muerto que desinformaba. `.gitignore`: retiradas las líneas `ROADMAP.md` (inexistente) y `GITHUB-MANIFEST.md` de la sección de planificación local; `.github/` se conserva ignorado.

---

## [v11.26 — 2026-05-20] — Borrado de backups muertos `.bak.v10.150`

Efecto colateral de v11.25 detectado por el revisor: el patrón genérico `*.bak` no cubre los backups antiguos `*.bak.v10.150` (terminan en `.v10.150`, no en `.bak`), así que 6 archivos `unidades/U{1,2,3,7,8,9}/U*-nc1-inventario.json.bak.v10.150` quedaron como untracked. Son backups de la migración de saneamiento v10.150, cerrada hace tiempo; los inventarios están en v11.x validando 0/0/0. Eliminados — no se re-ignoran (cruft muerto). El patrón `*.bak` se mantiene para backups futuros.

---

## [v11.25 — 2026-05-20] — Limpieza `.gitignore` + coherencia de estructura

`.gitignore`: retirados los patrones de backup de migraciones cerradas (`*.bak.v10.145`, `*.bak.v10.150`) y sustituidos por un genérico `*.bak`. Coherencia documental: `ROADMAP.md` (no existe) y `GITHUB-MANIFEST.md` (existe pero gitignorado como planificación local, fuera de la autoridad documental) se retiran de la estructura del repo en `README.md` y `CLAUDE.md` — los docs los listaban como archivos del proyecto pese a no versionarse. Patrones binarios/diseño del `.gitignore` se dejan intactos (ignores defensivos).

---

## [v11.24 — 2026-05-20] — Adelgazado de `.env.example` para repo A

`.env.example` pasó de ~70 a ~24 líneas. Repo A es dashboard local + validador: no usa agentes en su flujo vigente, no necesita claves de API, y ninguna variable es obligatoria (el dashboard arranca sin `.env`). Retirado: API keys (ANTHROPIC/GROQ/DEEPSEEK — de agentes, repo B), bloque Crew Recurvo, bloque DeepEval, `PORT=8080` (puerto viejo). Conservado como opcional: `PORT`/`HOST`/`EXTRA_UNIDADES_PATHS`/`DEBUG` (servidor del dashboard) + bloque comentado `DATABASE_URL`/`LANGFUSE_*` (superficies de BD/trazas heredadas y dormidas — el código de `diagrama.py` aún las lee). Verificado contra el uso real de `os.environ` en `diagrama.py`. `.env` real (con claves) intacto y gitignorado.

---

## [v11.23 — 2026-05-20] — Residuo `.dockerignore` en el paso E3 de REVIEW

Hallazgo del revisor tras v11.22: el paso futuro E3 de `REVIEW.md` (Meta-lista de archivos a limpiar) aún nombraba `.dockerignore`, que no existe desde v11.21. Añadida nota inline aclarando que ya no aplica. Cierra el último rastro de `.dockerignore` en el plan vivo.

---

## [v11.22 — 2026-05-20] — Residuo `.dockerignore` en PROCESO-MAESTRO

Hallazgo del revisor tras v11.21: `PROCESO-MAESTRO.md:255` mencionaba `.dockerignore` en una lista de tarea sin marcar como superada. Añadida nota inline "tarea histórica ya superada; `.dockerignore` eliminado en v11.21". Sin más cambios.

---

## [v11.21 — 2026-05-20] — Retirada del stack de despliegue (Docker/Railway)

Repo A ya no se despliega en la nube — el dashboard es herramienta local (`python3 diagrama.py`). Eliminados `Dockerfile`, `.dockerignore` y `railway.toml`. Razón: el despliegue tenía sentido cuando se compartía el dashboard con el equipo y los módulos de agentes vivían aquí; tras la migración a dos repos (agentes en repo B) y la decisión de no desplegar repo A, el stack quedó sin uso (y `.dockerignore` arrastraba 7 líneas `viejo/` muertas). `requirements.txt` se mantiene (lo necesita el `.venv` local). Referencias actualizadas: `CLAUDE.md` y `PROCESO-MAESTRO.md` (estructura del repo), `README.md` (estructura + fila "Ejecución" del stack), `REVIEW.md` (estado global, B5 marcado ⊘ SUPERADO, tablas de archivos/código). Bitácora histórica de CHANGELOG/REVIEW no se reescribe.

---

## [v11.20 — 2026-05-20] — Renombrado de scripts: `sanear_inventario.py` y `matcher.py`

Lote 3 (naming) de la revisión de `scripts/`. Renombrado limpio con `git mv` + actualización de todas las referencias activas: `cleanup_v150.py` → `sanear_inventario.py` (el `v150` sugería one-shot, pero es la herramienta de saneamiento activa del flujo de fase 1); `migrate_at_r_v10145.py` → `matcher.py` (su nombre era de la CLI de migración v10.145 — one-shot cumplida — pero su valor vivo es la librería matcher que importa `sanear_inventario.py`). Referencias actualizadas: `CLAUDE.md`, `prompt.md`, `validar_inventario.py` (2 comentarios), `schema-inventario.md`, el import de `sanear_inventario.py` y los docstrings de ambos. Histórico de CHANGELOG/REVIEW no se reescribe (nombres de la época). Verificado: import OK, `sanear_inventario.py` corre, validador 0/0/0.

---

## [v11.19 — 2026-05-20] — Cuarentena de `regenerar_reciclaje_vocabulario.py`

Lote 2 de la revisión de `scripts/`. `regenerar_reciclaje_vocabulario.py` está roto (asume shape v10.114 pre-rediseño; los inventarios son post-v10.153). No se archiva — sigue colgado del flag opcional de `integrar_unidad.py`. Cambios: (1) guard fail-fast `_cuarentena()` al inicio de `main()` — el script se rechaza con mensaje explícito salvo `RECICLAJE_VOCAB_OVERRIDE=1`; (2) `integrar_unidad.py` ya no dispara el script roto desde `--regenerar-reciclaje` — imprime aviso de cuarentena y completa la integración del inventario sin abortar; el commit es solo el inventario. `regenerar_reciclaje_mapa.py` se deja intacto (sigue operativo, fase 2 pausada).

---

## [v11.18 — 2026-05-20] — Archivado del one-shot `inicializar_canon_semantico.py`

`scripts/inicializar_canon_semantico.py` (one-off que pobló el canon semántico; cumplido — el canon se mantiene a mano desde entonces) movido a `docs/historico/scripts-one-shot/` con README. Referencias activas actualizadas antes de mover: `validar_inventario.py` (mensaje de ayuda del error de canon ausente → ahora apunta a "restaurar desde git") y `PROCESO-MAESTRO.md` (nota de archivado). **`migrate_at_r_v10145.py` NO se archiva** pese al nombre one-shot: `cleanup_v150.py` lo importa como módulo matcher — sigue activo. Su renombrado queda para un lote posterior de naming.

---

## [v11.17 — 2026-05-20] — `eval/` movido a `temporal-antiguo-guia-ia`

`eval/` (3 archivos, 28K — `promptfoo.yaml`, `evaluar_tarjetas.py`, `provider_crewai.py`) era tooling de evaluación del sistema CrewAI/Recurvo, no infraestructura viva de este repo. Estaba **roto** desde v11.14: `provider_crewai.py` importa de `scripts/crewai/`, que se fue a `temporal-antiguo-guia-ia` con el borrado de `viejo/`. Copiado a `temporal-antiguo-guia-ia` (commit `cf5da5e`) y eliminado de aquí. `CLAUDE.md` y `README.md` — retirada la referencia a `eval/` de la estructura del repositorio. Fase 3 (tarjetas), cuando se construya, tendrá su evaluación propia si la necesita; no depende de este `eval/` atado a Recurvo.

---

## [v11.16 — 2026-05-20] — Higiene `.gitignore` + limpieza de carpetas sueltas

Pasada de limpieza de carpetas de raíz. `.gitignore`: añadidos `.venv/` (654M, virtualenv regenerable que estaba untracked sin ignorar — riesgo de commit accidental) y `.deepeval/` (carpeta que el framework recrea). Eliminadas carpetas sin valor: `.deepeval/` (vacía), `.github/copilot-instructions.md` (obsoleto — describía un workspace antiguo con rutas inexistentes, era para Copilot no Claude Code), `.claude/claude-code-chat-images/` (26 screenshots viejos, 6.1M).

---

## [v11.15 — 2026-05-20] — Limpieza de `.claude/` tras la migración

`.claude/` de repo A queda mínimo: solo `commands/check-fase1.md` + `settings.json` (config de infraestructura/inventarios). Retirados de repo A los archivos de trabajo editorial y del sistema CrewAI antiguo — ya copiados a repo B (`temporal-antiguo-guia-ia`, verificado idéntico, con rutas `viejo/`→`unidades/` adaptadas): `rules/{agent-prompt-design,tool-design,criterios-generacion-texto}.md`, `agents/auditor-seccion.md`, `skills/auditar-seccion/`, `commands/audit.md`. Borrado el `.bak` huérfano. `.gitignore`: `.claude/` deja de ignorarse en bloque — ahora se versiona `settings.json` + `commands/check-fase1.md`; siguen ignorados `settings.local.json` y `claude-code-chat-images/`. Carpeta `claude-code-chat-images/` (26 screenshots viejos, 6.1M) eliminada — no aportan nada; el ignore se mantiene por si la extensión la recrea.

---

## [v11.14 — 2026-05-20] — Migración a dos repos · Mitad 2 paso 2: borrado físico de `viejo/`

`viejo/` eliminado de repo A (disco + índice git): 8 archivos tracked + el resto ignorado. Su copia íntegra y verificada (`diff -rq` sin diferencias) vive en repo B `temporal-antiguo-guia-ia` (local `~/Desktop/temporal-antiguo-guia-ia`, GitHub privado `adminmc2/temporal-antiguo-guia-ia`, commits `8164c2f`+`6cdf342`). `.gitignore` — retirado el bloque "Contenido editorial" completo (~15 líneas que ignoraban `viejo/...`) + la línea de PDFs `viejo/unidades/**/fuente/`. Hook `.git/hooks/pre-commit` (bloqueaba commits con rutas `viejo/`) retirado: sin objeto. Repo A queda sin `viejo/`; el sistema de trabajo es ya exclusivamente repo B. Cierra la Mitad 2 de la migración.

---

## [v11.13 — 2026-05-20] — Migración a dos repos · Mitad 2 paso 1: coherencia documental

Repo A queda autocoherente sin `viejo/` como fuente de trabajo (aunque `viejo/` siga existiendo físicamente una iteración más; se borra en v11.14). Cambios: `CLAUDE.md` — nuevo bloque "Modelo de dos repos A/B", flujo de publicación reapuntado a repo B, reglas de oro y "Lo que NO se hace" sin "editar en viejo", `viejo/` fuera de la estructura. `README.md` — sección "Modelo de dos repositorios" sustituye a "Sobre el sistema anterior". `diagrama.py` — dict `AGENTS` (código muerto que apuntaba a `viejo/repertorios/`) retirado; comentario documenta la feature "repertorios por sección" como diferida (reintroducir desde repo B vía `GUIA_TRABAJO_REPO`). `PROCESO-MAESTRO.md` — nota de migración global: sus ~82 referencias `viejo/...` son punteros históricos a material que vive en repo B (reescritura completa pendiente de pasada posterior). Criterio de cierre: ningún documento activo presenta `viejo/` como zona de trabajo vigente.

---

## [v11.12 — 2026-05-20] — Versionar mirrors editoriales en repo A

Las propuestas editoriales publicadas (`unidades/U{0,1,2,4,5}/propuesta/*.md`) y los recursos (`recursos/tarjetas/*.csv`) estaban untracked — existían en disco pero fuera de git. Al ser el entregable de repo A, se commitean: 37 archivos, 6362 líneas. Preludio de la Mitad 2 (migración a dos repos).

---

## [v11.11 — 2026-05-20] — Compactación de CHANGELOG

`CHANGELOG.md` pasó de 4252 a ~250 líneas. El bloque v10.40–v10.164 (cierre de fase 1 + fase 2 paralela) se movió a `docs/historico/CHANGELOG-fase1-cierre-y-fase2-paralela.md` con cabecera fuerte que lo declara fuente documental de lo hecho en ambas fases. Header del activo gana índice de históricos por rango. Corte validado por contenido: todo v10.x es era fase 1; v11.0 es el milestone post-fase-1. README/CLAUDE sin tocar; REVIEW solo como meta-doc (banner + bitácora, por convención).

---

## [v11.10 — 2026-05-20] — Jerarquía de autoridad documental + regla editorial

Cierre del problema de crecimiento perpetuo de CHANGELOG/REVIEW sin rearchivar nada. Cambios: (1) cabeceras de CHANGELOG.md y REVIEW.md declaran su rol (registro/estado, NO autoridad) y la regla editorial de entradas cortas; (2) CLAUDE.md § "Documentos clave" añade columna ¿Autoridad? + bloque "Regla editorial" — CLAUDE.md manda, el resto apunta; (3) README.md añade línea "dónde mirar histórico" (`docs/historico/`). Sin mover archivos. Archivos: CLAUDE.md, README.md, CHANGELOG.md, REVIEW.md.

---

## [v11.9 — 2026-05-20] — Dashboard "Inventarios": tarjetas con A+B+C+D (stats, consolidados, propuesta, keywords)

Tarjetas de la vista Inventarios del dashboard ampliadas para mostrar contexto operativo y editorial de cada unidad de un vistazo. Las cards anteriores mostraban solo título, nivel, páginas y archivo; ahora también:

**Bloque A — Stats del inventario:** `📋 N actividades · N cuadros · N decisiones` (lectura directa del JSON: paginas_detalle, _decisiones_ia).

**Bloque B — Consolidados resumidos:** `📚 Léx N P/N R · ⚙ Gram N P/N R · 🔤 P/O N P/N R · 📖 Nv` (recuento de categorías principal/recurrente en las 4 dimensiones canónicas + lemas verbales).

**Bloque C — Propuesta editorial mini-grid:** 7 chips compactos `Voc ✓ · Gram ⏳ · Com · · ...` reutilizando el scanner ya existente de fase 1 (lectura de `unidades/UN/propuesta/<seccion>.md`). Cada chip tiene tooltip con el estado y usa la misma paleta de la grid "Estado de unidades" del proyecto.

**Bloque D — Keywords del inventario:** hasta 5 chips con los canónicos léxicos y gramaticales principales (ej. U6: `Establecimientos · Marcadores de lugar · Profesiones y lugares de trabajo · Imperativo (tú)`).

**Cambios:**

- `diagrama.py` `_scan_zona`: añadidos 4 campos al payload de cada unidad (`stats`, `consolidados`, `keywords`, `propuesta`). Reutiliza `scan_section` para no duplicar lógica.
- `web/index.html` `loadInventarios`: card más ancha (`minmax(340px, 1fr)` en lugar de 260px) y renderiza los 4 bloques compactamente. Tooltips en chips de propuesta. Archivo path se trunca con ellipsis.

**Higiene del commit:** `diagrama.py` + `web/index.html` + meta docs.

---

## [v11.8 — 2026-05-20] — Sync de puerto 8080→8081 fuera del subsistema dashboard

Hallazgo del revisor tras v11.7: aunque el subsistema dashboard quedó sincronizado, seguían 4 referencias activas a `8080` fuera de ese subsistema, mientras `diagrama.py` PORT = 8081 desde v10.127.

**Cambios — unificación a 8081 en todas las referencias activas:**

- `README.md:80`: comando de arranque (`# → http://localhost:8081`).
- `Dockerfile:16`: `EXPOSE 8081` (antes 8080, no coincidía con el puerto al que liga el server).
- `fases/1-extraccion-inventario/CLAUDE.md:38`: comando de validación visual.
- `fases/2-reciclaje/CLAUDE.md:54`: comando de revisión de timeline.

**Verificación:** `grep -rn "8080"` en `*.md` / `*.py` / `Dockerfile` (excluyendo `viejo/`, `docs/historico/`, y entradas históricas de CHANGELOG/REVIEW) → 0 coincidencias activas.

**Higiene del commit:** `README.md` + `Dockerfile` + 2 × CLAUDE.md de fase + meta docs.

---

## [v11.7 — 2026-05-19] — Cleanup-sync: drifts menores tras auditoría v11.6

Auditoría tras v11.6 detectó tres drifts del mismo subsistema. Lote único para cerrar todo en una sola pasada.

**Cambios:**

1. **`diagrama.py`**: eliminada la clave huérfana `"reflexion": "Reflexión"` de `SECTION_LABELS`. Era residuo inerte tras la retirada de la columna Reflexión en v11.1 (no participaba en `SECTIONS`, no afectaba runtime).
2. **`diagrama.py:5`**: docstring decía `http://127.0.0.1:8080`; corregido a `8081` (PORT real definido en `diagrama.py:29`).
3. **`CLAUDE.md:88`**: comentario en sección "Comandos básicos" decía `http://localhost:8080`; unificado a `8081` (coincide ya con § "Estado fase 1 — Comandos canónicos" en `CLAUDE.md:153`).
4. **`CLAUDE.md:24`**: estructura del repositorio mencionaba solo 6 secciones canónicas en `propuesta/` (vocabulario, gramatica, comunicacion, destrezas, cultura, evaluacion). El dashboard pinta una 7.ª columna `itinerarios` desde v11.1. Anotado en la estructura como opcional: planificación cross-unidad mostrada como 7.ª columna del dashboard.

**Higiene del commit:** `diagrama.py` + `CLAUDE.md` + meta docs.

**Próximo paso:** ya sin drifts pendientes, decidir entre reactivar fase 2 (reciclaje) o continuar con producto editorial.

---

## [v11.6 — 2026-05-19] — Sync CLAUDE.md raíz tras cierre de deuda matcher

Hallazgo del revisor tras v11.5: la sección "Estado fase 1 — Deudas residuales" de `CLAUDE.md` raíz seguía afirmando las 3 deudas matcher como abiertas, aunque ya quedaron resueltas en v11.3-v11.5. Bug puramente documental — no rompe runtime ni validación, pero deja una fuente normativa incorrecta para sesiones futuras (CLAUDE.md es la autoridad que cargan automáticamente todas las nuevas sesiones de Claude Code).

**Cambios:**

- `CLAUDE.md` § "Estado fase 1 — Deudas residuales catalogadas" reescrita:
  - Bloque nuevo "Deuda matcher: CERRADA en v11.3-v11.5" con check de cada bug y la versión que lo resolvió.
  - Bloque "Deudas todavía abiertas" conserva los canónicos huérfanos (`Abreviaturas de los diccionarios`, `vegetariano`) y la auditoría retroactiva U0-U5.

**Higiene del commit:** solo `CLAUDE.md` + meta docs.

---

## [v11.5 — 2026-05-19] — Deuda matcher bug 3: `_gather_text` recoge claves de dict

Tercer y último fix de la deuda técnica del matcher catalogada al cierre de fase 1. Con este commit, la deuda matcher queda cerrada por completo.

**Problema:**

`_gather_text(o, out)` iteraba sobre dicts recorriendo solo los valores (`o.values()`), nunca las claves. Caso real (U6 v10.158): la agenda semanal de Lorena en `p66-act4` se modelaba como dict `{"Lunes": "Piscina", "Martes": "Supermercado", ...}`. El matcher recogía solo los valores (las actividades), pero no los días — y `Días de la semana` solo aparecía con `Lunes` (capturado en otra actividad). Investigando se descubrió la causa: las claves del dict no se gathereaban.

**Fix:**

- `scripts/validar_inventario.py`: `_gather_text` ahora itera con `o.items()` y añade la clave al output si es string, además de recursar sobre el valor. Comportamiento idéntico para listas y strings.

**Resultado:**

- Para futuros inventarios, dicts con claves significativas (días, personajes, secciones, etc.) ya no obligan a reestructurar a lista de objetos solo para satisfacer al matcher.
- Las 10 unidades siguen validando 0/0/0 tras el fix (sin regresión).

**Decisión: U6 agenda NO se revierte a dict.**

El workaround de v10.158 (agenda lista de objetos `[{"dia": "Lunes", "actividad": "Piscina"}, ...]`) se mantiene. Razones: (a) revertir es un cambio estructural sin ganancia funcional (el matcher ya lee ambos shapes); (b) otros consumidores potenciales (dashboard, agentes) pueden depender del shape actual; (c) el fix elimina la necesidad del workaround **para nuevos inventarios**, que es lo importante.

**Trade-off aceptado:**

Recoger claves de dict aumenta levemente la superficie de match. Las claves del proyecto son normalmente etiquetas semánticas (`Lunes`, `Martes`, `personaje`, `texto_modelo`, etc.). Si una clave técnica coincidiera con un item canónico por casualidad, generaría falso positivo. Riesgo bajo; si emergiera se documentaría.

**Cierre de la deuda matcher:**

Las 3 deudas técnicas catalogadas al cierre de fase 1 quedan resueltas en v11.3-v11.5:
- ✅ Bug 1 (acentos): `_norm_text` aplica `_strip_accents` (v11.3).
- ✅ Bug 2 (imágenes): `imagen` en `INPUT_FIELDS_LIST` (v11.4).
- ✅ Bug 3 (claves de dict): `_gather_text` recoge claves (v11.5).

**Próximo paso:** reactivar fase 2 (reciclaje) o continuar con producto editorial.

**Higiene del commit:** solo `scripts/validar_inventario.py` + meta docs.

---

## [v11.4 — 2026-05-19] — Deuda matcher bug 2: matcher recoge `imagen.descripcion`

Segundo fix de la deuda técnica del matcher catalogada al cierre de fase 1.

**Problema:**

El validador `_activity_input_text` solo iteraba sobre `INPUT_FIELDS_LIST` = `(instruccion_original, datos, dialogo, dialogo_completo, texto, texto_completo, items_libro, muestra_de_lengua, opciones, audio)`. El campo `imagen.descripcion` no estaba incluido. Caso real (U9 v10.164): `morado/-a` aparecía en el libro como color de prendas en `p101-act04`, pero solo dentro de `imagen.descripcion` ("Siete fotos de prendas... 1 falda morada, ... 7 jersey morado"). El validador no lo veía → no se podía codificar como item de Colores y el contenido material se perdía.

**Razón editorial del fix** (autor en chat): la descripción de imagen es contexto editorial real que el alumno ve. Para entender una actividad es necesario saber qué muestra la imagen — no es metadato. El campo `respuestas`, en contraste, tiene función distinta (clave para profesor / contexto para agentes), pero esa decisión se mantiene fuera del alcance de este fix.

**Fix:**

- `scripts/validar_inventario.py`: añadido `"imagen"` a `INPUT_FIELDS_LIST`. `_gather_text` recurre sobre el dict `imagen` y recoge automáticamente todas las strings (incluido `descripcion`).

**Resultado:**

- `morado/-a` en U9 ahora codificado en bucket `Colores` recurrente con fuente `p101-act4` (recuperado tras workaround vacío de v10.164).
- Refs de actividad p101-act04 ampliadas con `Colores`.
- Las 10 unidades siguen validando 0/0/0 tras el fix.

**Trade-off aceptado:**

Algunas descripciones de imagen son verbosas (ej. p100-act01 con tres trajes tradicionales). Podrían generar falsos positivos puntuales para lemas cortos. Riesgo bajo y simétrico al que ya existe con `texto_completo`; si emergiera, se documentaría como deuda específica.

**Pendiente:**

- Bug 3 (matcher no recoge claves de dict) — caso `agenda` U6 v10.158.

**Higiene del commit:** `scripts/validar_inventario.py` + `unidades/U9/U9-nc1-inventario.json` + meta docs.

---

## [v11.3 — 2026-05-19] — Deuda matcher bug 1: normalización de acentos en `_norm_text`

Primer fix de la deuda técnica del matcher catalogada al cierre de fase 1 (v10.164).

**Problema:**

El validador `_norm_text` solo aplicaba lowercase + collapse de whitespace, sin normalizar tildes. Caso real (U8 v10.163): la palabra del libro era `marrones` (plural sin tilde). El item canónico debía ser `marrón` (singular con tilde, por §5.11). Pero `marrón` ≠ substring de `marrones` por la diferencia `ó`/`o` → matcher fallaba, obligando a escribir `marrones` como item (violando §5.11 unificación a singular).

**Fix:**

- Nueva función `_strip_accents(s)` en `scripts/validar_inventario.py` que descompone NFD y descarta los marks de tilde aguda/grave/circumflex, preservando `ñ` (re-componiendo `n + U+0303` → `ñ`).
- `_norm_text(s)` ahora aplica `_strip_accents` tras lowercase + whitespace collapse. Se aplica simétricamente a needle y haystack → comparación substring funciona con tildes ausentes en plural.

**Resultado:**

- `marrón` (item singular) atrapa `marrones` en texto ✓
- `años` atrapa `año` ✓
- `período` atrapa `periodo` ✓
- Las 10 unidades siguen validando 0/0/0 tras el fix (sin regresión).

**Rectificación de workaround:**

- `unidades/U8/U8-nc1-inventario.json`: `marrones` → `marrón` (forma singular canónica restaurada en bucket `Colores` recurrente). El workaround de v10.163 queda eliminado.

**Trade-off aceptado:**

La normalización acepta como match casos como `tu` ↔ `tú` (posesivo vs pronombre sujeto). En el inventario actual, ambos items declaran sus propias fuentes y la práctica editorial mantiene la disambiguación. Si emergiera una falsa coincidencia, se documentaría como deuda específica.

**Pendiente:**

- Bug 2 (matcher no recoge `image.descripcion`) — caso `morado/-a` U9.
- Bug 3 (matcher no recoge claves de dict) — caso `agenda` U6.

**Higiene del commit:** `scripts/validar_inventario.py` + `unidades/U8/U8-nc1-inventario.json` + meta docs.

---

## [v11.2 — 2026-05-19] — Dashboard auto-refresh por polling con hash

El dashboard "Estado de unidades" no detectaba cambios sin recargar manualmente la página. Implementado auto-refresh por polling con hash check, sin nuevas dependencias.

**Cómo funciona:**

- Cada **5 segundos**, el frontend hace `fetch('/api/diagrams')` en silencio.
- El endpoint ya devuelve un campo `hash` (md5 del `status` object) calculado en backend.
- Si el `hash` recibido coincide con el último renderizado → no se re-renderiza nada (sin DOM churn).
- Si el `hash` cambió → se re-renderiza la grid de estado, las tabs de diagrama y el diagrama activo.

**Resultado:** cualquier modificación en `unidades/UN/propuesta/<seccion>.md` (creación, edición, borrado, añadir/quitar `*pendiente*`) se refleja automáticamente en el dashboard en ≤5 segundos sin recargar la pestaña.

**Cambios:**

- `web/index.html`: `loadProjectData()` ahora acepta opciones (`{silent: true}` para polling), guarda `_projectHash`, y solo re-renderiza cuando el hash cambia. Añadido `setInterval(..., 5000)` para el polling silencioso.

**Higiene del commit:** solo `web/index.html` + meta docs.

**Próximo paso (v11.3+):** decidir entre deuda matcher (`_expand_needle` / `_gather_text`) o reactivación de fase 2.

---

## [v11.1 — 2026-05-19] — Dashboard "Estado de unidades": ajustes UX

Ajustes UX al panel "Estado de unidades" del dashboard tras revisión visual del autor.

**Cambios:**

1. **Retirada de columna "Reflexión"** — no se trabaja como sección editorial independiente; era ruido en la tabla. Grid pasa de 8 a 7 columnas.
2. **Criterio `complete` simplificado** — el conteo de líneas no es señal de calidad. Nuevo criterio: `complete` = archivo existe sin marcadores `*pendiente*`; `in-progress` = tiene pendientes; `missing` = no hay archivo.
3. **Celdas con marcas semánticas** en lugar de número de líneas: `✓` (complete), `N⏳` (in-progress con N pendientes), `·` (missing). El conteo de líneas dejó de mostrarse porque no aportaba info accionable.
4. **U0 atípica reconocida**: la unidad atípica tiene un único archivo `unidades/U0/propuesta/punto-de-partida.md` que cubre la unidad entera. El scanner ahora propaga ese archivo a las 7 celdas de U0.
5. **CSS grid alineado** a las nuevas 7 columnas (`grid-template-columns: 50px repeat(7, 1fr)`) — el ajuste sin esto provocaba desplazamiento de etiquetas U0/U1/... dentro de las celdas.

**Resultado:** dashboard pasa de `0/80` (estado v10.164 con scanner roto) a `31/70 completas` automáticamente. Cada celda comunica algo accionable.

**Próximo paso (v11.2):** auto-refresh por file-watcher cuando se añadan o modifiquen archivos en `propuesta/`.

**Higiene del commit:** `diagrama.py` + `web/index.html` + meta docs.

---

## [v11.0 — 2026-05-19] — Milestone post-fase 1: bump + fix scanner dashboard

Primera versión tras el cierre de fase 1 (v10.164). Bump de major para marcar el hito: la parte mecanizable de extracción de inventario queda consolidada y las nuevas iteraciones se centran en infraestructura y producto (no en saneamiento retrospectivo).

**Cambios:**

1. **Bump major v10.164 → v11.0** — milestone de cierre de extracción canónica + apertura del bloque de infraestructura/producto.
2. **Fix scanner del dashboard** (`diagrama.py` `scan_section`): el scanner buscaba el patrón legacy `unidades/UN/UN-<seccion>*.md` y devolvía `missing` para todo el material editorial nuevo, que vive en `unidades/UN/propuesta/<seccion>.md` (sin prefijo) según el flujo de publicación canónica documentado en CLAUDE.md raíz. Ahora busca primero en `propuesta/<seccion>.md` (nueva canónica) y luego en el patrón legacy (compatibilidad hacia atrás).

**Resultado verificable:** el dashboard "Estado de unidades" pasa de `0/80 completas` a `20/80 completas` automáticamente (U1, U2, U4, U5 con 5 secciones cada una en estado `complete` + 4 con `in-progress` en evaluación). U0 atípica + U3, U6-U9 sin propuesta = `missing` legítimo.

**Próximo paso (v11.1):** auto-refresh del dashboard cuando se añadan archivos en `propuesta/`.

**Higiene del commit:** solo `diagrama.py` + meta docs.

