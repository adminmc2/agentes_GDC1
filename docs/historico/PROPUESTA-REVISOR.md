# Diagnóstico del revisor sobre el sistema documental de instrucciones — v2

> Documento consolidado el 2026-05-17 · Revisión v2 con ajustes de operabilidad.
> Sustituye el seguimiento previo por fases y conserva solo lo útil para decidir sobre el sistema real de `CLAUDE.md` + pautas. El problema principal ya no es validar pilotos, sino reducir el riesgo de error sustancial en los documentos base.
>
> **Cambios de v1 → v2:** §3.1 reforzada con contradicción interna dentro de `gramatica-pautas.md`; §3.2 reformulada como "redacción/scope mal acotado", no choque estructural; §3.3 conectada con la regla de gobierno de §5.1; §6 con criterios de aceptación binarios, autoridad de decisión, disciplina de git, orden interno de barrido y estimación de esfuerzo; §10 condición 4 con formulación medible.

---

## 1. Dictamen ejecutivo

El modelo de operación basado en un `CLAUDE.md` transversal más pautas específicas por sección **sí es válido** para este repositorio. No conviene desmontarlo. El problema no es la arquitectura conceptual, sino el estado actual de sus fuentes de verdad.

Mi juicio es este:

1. **La arquitectura es buena.** Existe una separación razonable entre contrato transversal, pautas de sección, criterios de estilo y herramientas de auditoría.
2. **La implementación documental no está cerrada.** Hay contradicciones entre archivos, duplicaciones normativas y términos operativos usados sin definición canónica única.
3. **El riesgo real no está en la falta de tooling.** El riesgo real está en que dos documentos distintos pueden dar órdenes incompatibles sobre la misma decisión editorial.
4. **La prioridad correcta es saneamiento documental.** Skills, subagents y hooks solo tienen sentido cuando el contrato base ya no se contradice.

Conclusión operativa: **el sistema está bien planteado, pero todavía no está lo bastante normalizado como para considerarlo una base segura sin supervisión fuerte**.

---

## 2. Qué sí funciona y conviene conservar

### 2.1 Capa transversal + capas por sección

La división entre un contrato común y pautas específicas por sección es correcta. En este proyecto tiene sentido que exista:

- un nivel **repo** para reglas generales de trabajo;
- un nivel **transversal de unidades** para criterios editoriales compartidos;
- un nivel **específico de sección** para Vocabulario, Gramática, Comunicación, Destrezas, Cultura y Evaluación.

Esto evita meter toda la lógica en un único archivo y también evita dispersar reglas críticas por decenas de documentos sin centro.

### 2.2 Regla estilística separada del protocolo operativo

`.claude/rules/criterios-generacion-texto.md` está bien orientado como documento aparte. La separación entre:

- **cómo debe sonar** el texto del profesor,
- y **cómo debe construirse** una sección,

es sana y debería mantenerse.

### 2.3 Pautas como documentos vivos

La idea de que cada pauta acumule errores recurrentes y patrones refinados es buena. Permite aprendizaje editorial acumulativo. El problema no es que sean documentos vivos; el problema es que hoy esa evolución no está lo bastante gobernada y termina generando solapamientos.

### 2.4 Carril de auditoría aislada

La skill F2 y el subagent F3 han demostrado utilidad como infraestructura de auditoría. Ese carril sí aporta valor, pero como herramienta secundaria. No resuelve por sí mismo los defectos de la fuente contractual.

---

## 3. Dónde están hoy los riesgos sustanciales

### 3.1 Fractura de fuente de verdad en la regla más sensible: el verbo del rótulo

Este es el problema más serio del sistema actual.

Evidencia observada:

- `viejo/unidades/CLAUDE.md` establece en el checklist que el verbo del rótulo debe ser del docente y pone como no válidos, entre otros, `construya`, `practique`, `anime` y `modele`.
- `viejo/unidades/vocabulario-pautas.md` incluye `ANIME` como verbo validado en activación y `PRACTIQUE · ANIME · JUEGUE · APROVECHE` como verbos validados en producción/práctica.
- `viejo/unidades/gramatica-pautas.md:182` prohíbe `practique`, `combine`, `construya`, `complete`, `conjugue` y `transforme` como verbo principal del rótulo, porque los considera verbos del alumno.
- **Contradicción interna dentro de la misma pauta de Gramática** (refuerzo v2): `gramatica-pautas.md:370` (fila 4 de la tabla de errores recurrentes) propone `MUESTRE, CONSTRUYA` como verbos válidos del banco §8 para corregir rótulos con `MODELE, ANIME`. Pero ocho filas después, `gramatica-pautas.md:378` (fila 12 de la misma tabla) lista `CONSTRUYA` como verbo del **alumno** que debe reformularse con verbo de facilitación del docente. La incoherencia está **dentro de un único archivo y dentro de una única tabla**, no solo entre pautas. Es la evidencia más fuerte del hallazgo.

Riesgo:

- un agente puede obedecer cualquiera de las dos fuentes y producir resultados opuestos;
- una auditoría puede marcar como error algo que otra pauta valida;
- cualquier hook sobre verbos generará falsos positivos o falsos negativos.

Dictamen:

Esta contradicción no es un detalle local. Es una prueba de que la regla transversal más importante todavía no tiene una formulación canónica cerrada.

### 3.2 Regla con scope mal acotado en el `CLAUDE.md` raíz (reformulado v2)

En `CLAUDE.md` de la raíz conviven dos formulaciones que **leídas literalmente** se contradicen, aunque en la práctica el sistema funciona porque hay una distinción implícita por subcarpeta:

- `CLAUDE.md:30` y `CLAUDE.md:53` describen `viejo/` como zona donde se redactan las propuestas activas y reside todo el material editorial de referencia.
- `CLAUDE.md:70` (regla de oro #5) dice literalmente *"No tocar `viejo/`"*.

La distinción real, que el sistema asume sin enunciar, es que la regla de oro aplica a la subcarpeta del sistema CrewAI v5 anterior dentro de `viejo/`, mientras que `viejo/unidades/` es la zona de trabajo viva del rediseño. La contradicción no es estructural ni conceptual: es **de redacción y scope mal acotado**.

Riesgo (atenuado respecto a v1):

- un agente o un colaborador nuevo que solo lea la regla de oro puede bloquearse innecesariamente;
- el revisor humano todavía puede reconstruir la intención sin esfuerzo;
- el coste real es de fricción de incorporación y de auditoría, no de funcionamiento diario.

Dictamen v2:

No es un choque conceptual. Es una regla cuyo scope se debe acotar explícitamente. Solución previsible: reescribir la regla de oro #5 como *"No tocar la subcarpeta del sistema CrewAI v5 anterior dentro de `viejo/`; la zona viva del rediseño es `viejo/unidades/`"*. Cambio menor de redacción, no rediseño.

### 3.3 Sobrecarga del `CLAUDE.md` transversal de unidades

`viejo/unidades/CLAUDE.md` hace hoy demasiadas funciones a la vez:

- índice de documentos a consultar;
- checklist de cierre;
- proceso operativo;
- estructura del archivo;
- glosario de vocabulario prohibido;
- reglas de tono;
- reglas de rótulos;
- reglas sobre fichas, insignia y canción;
- meta-reglas de gobierno.

Riesgo:

- el archivo es útil como manual humano, pero demasiado heterogéneo como contrato automático siempre activo;
- las pautas remiten constantemente a él, lo que lo convierte en cuello de botella editorial;
- cuanto más material metes en el hub, más fácil es duplicarlo o reinterpretarlo desde las pautas.

Dictamen:

No hay que adelgazarlo de forma agresiva ni "podarlo porque sí", pero sí **limitarlo a reglas transversales estables**. Ahora mismo mezcla norma, explicación, flujo, inventario y memoria histórica.

**Criterio operacional (conexión con §5.1, añadido v2).** La pregunta a aplicar cada vez que se evalúa si un contenido pertenece al hub es la regla de §5.1 reformulada como filtro binario: *"¿Esta regla aplica a todas las secciones, o solo a algunas?"*. Si aplica a todas, se queda en el hub. Si solo aplica a algunas (aunque sean varias), sale del hub a la pauta correspondiente. Lo mismo para casuísticas locales: si una regla solo se ha invocado desde una pauta, no es transversal todavía, aunque parezca general.

### 3.4 Referencias cruzadas frágiles e inestables

El sistema depende demasiado de referencias del tipo `§10`, `§14`, `§15`, `§13bis`, `§10bis`, `§14bis`, `§5bis`, etc.

Riesgo:

- si una pauta crece o se reordena, las referencias dejan de apuntar de forma fiable;
- el revisor humano todavía puede reconstruir la intención, pero un agente o auditor pierde precisión;
- la trazabilidad queda ligada a numeraciones cambiantes, no a conceptos estables.

Dictamen:

La referencia canónica debe ser el **título exacto de la sección**, no solo su número. El número puede mantenerse como ayuda, pero no como ancla única.

### 3.5 Distinción esencial pero infra-definida: metanota, cuerpo del rótulo y anexo

Muchísimas reglas dependen de la diferencia entre:

- lo que puede vivir en **metanota**,
- lo que puede vivir en **cuerpo del rótulo**,
- y lo que debe ir en **anexos**.

Esa distinción aparece usada de forma constante para tiempos, metalenguaje, bloques Suno, residuos de proceso, integración de píldora y trazabilidad metodológica.

Riesgo:

- se usa como si fuera un concepto cerrado, pero no está definido en un único sitio con precisión formal suficiente;
- una auditoría humana puede inferirlo por contexto, pero un guardarraíl automático no;
- provoca derrames de metalenguaje técnico o de notas de proceso en el cuerpo final.

Dictamen:

Mientras esta distinción no tenga definición canónica, cualquier automatización sobre “cuerpo” y “metanota” es prematura.

### 3.6 Ruptura práctica de la regla “una fuente única”

El repositorio dice correctamente que cada criterio editorial debe vivir en un solo sitio. En la práctica, hoy no sucede.

Casos visibles:

- regla del verbo del docente duplicada entre hub y pautas;
- vocabulario prohibido tratado en capa transversal y reaparecido por secciones;
- reglas de metanota/cuerpo reapareciendo en varios documentos;
- algunos errores recurrentes de sección invadiendo decisiones que en realidad son transversales.

Riesgo:

- el sistema aprende, pero también deriva;
- cada nueva pauta puede introducir una “microconstitución” paralela;
- el coste de mantenimiento sube sin que se note de inmediato.

Dictamen:

La regla “una fuente única” existe como principio, pero todavía no está ejecutada como diseño real.

### 3.7 Falsa sensación de seguridad por validar tooling antes que contrato

La validación de la skill y del subagent fue útil, pero crea un riesgo de lectura equivocada: pensar que el sistema ya está maduro porque el carril de auditoría funciona.

Riesgo:

- desplazar la atención desde los documentos base hacia la infraestructura;
- auditar con éxito contra reglas todavía inconsistentes;
- sentir progreso sin haber reducido todavía el riesgo de error sustancial en la producción real.

Dictamen:

El tooling validado debe mantenerse, pero como infraestructura secundaria. No puede convertirse en prueba de calidad del contrato base.

---

## 4. Valoración final del modelo `CLAUDE.md` + pautas

### 4.1 Respuesta corta

Sí, el modelo está bien elegido.

No, el estado actual todavía no está bien cerrado.

### 4.2 Por qué el modelo es bueno

Porque este proyecto no es una base de código clásica. Es un sistema editorial con alta dependencia de:

- reglas de redacción;
- excepciones por tipo de sección;
- reutilización de criterios comunes;
- trazabilidad de decisiones didácticas.

En un sistema así, un contrato central más pautas especializadas es mejor que:

- un único mega-documento monolítico;
- o una dispersión total sin centro normativo.

### 4.3 Por qué hoy todavía no está bien

Porque el sistema tiene forma correcta pero disciplina documental insuficiente. El problema no es el patrón; el problema es el gobierno de ese patrón.

Ahora mismo el modelo falla en tres puntos:

1. **centraliza bien, pero no normaliza del todo**;
2. **especializa bien, pero duplica demasiado**;
3. **audita bien, pero contra una base todavía imperfecta**.

---

## 5. Modelo objetivo recomendado de fuentes de verdad

| Capa | Función correcta | Debe contener | No debe contener |
|---|---|---|---|
| `CLAUDE.md` raíz | Contrato de repo | alcance del repositorio, zonas de trabajo, flujo canónico, reglas globales de seguridad y edición | reglas didácticas de sección, contradicciones sobre qué carpetas se editan |
| `viejo/unidades/CLAUDE.md` | Contrato transversal editorial | reglas estables comunes a todas las secciones, definiciones canónicas, checklist verdaderamente transversal | bancos específicos de verbos por sección, casuística demasiado local, memoria histórica extensa |
| `*-pautas.md` | Especificidad por sección | repertorios propios, errores específicos, decisiones de estructura y protocolo de esa sección | redefinir reglas transversales ya cerradas |
| `.claude/rules/criterios-generacion-texto.md` | Estilo de salida | tono, densidad, prohibiciones de registro, uso de tiempos y metalenguaje en cuerpo | protocolo didáctico de cada sección |
| skills / subagents | Infraestructura de auditoría | lectura, contraste, checklist, informe | criterios nuevos, enforcement, mutación de archivos base |

### 5.1 Regla de gobierno recomendada

Toda regla debe clasificarse antes de escribirse:

1. **¿Es transversal y estable?** Va al `CLAUDE.md` de `viejo/unidades/`.
2. **¿Es propia de una sección?** Va solo a su `*-pautas.md`.
3. **¿Es puramente estilística de redacción final?** Va a `criterios-generacion-texto.md`.
4. **¿Es un patrón detectado en un caso concreto?** Entra primero como error recurrente específico y solo se eleva a transversal si reaparece en varias secciones.

---

## 6. Orden real de intervención recomendado

> **Adiciones v2.** Cada prioridad lleva criterio de aceptación binario verificable. Antes del bloque de prioridades se fijan tres reglas marco: autoridad de decisión sobre conflictos sustantivos, disciplina de git, y estimación de esfuerzo orientativa.

### 6.0 Reglas marco del saneamiento (añadido v2)

**Autoridad de decisión.** Cuando dos documentos enuncian la misma regla con redacciones incompatibles, la decisión sobre cuál queda como canónica la toma **el autor del proyecto**. El ejecutor no decide entre A y B por iniciativa propia: propone variantes (A / B / síntesis C) y espera criterio. Aplica especialmente al verbo del rótulo, donde Vocabulario y Gramática difieren sustantivamente y la propia pauta de Gramática se contradice internamente (§3.1).

**Disciplina de git.** El saneamiento se hace en **rama dedicada** (`saneamiento-documental` o similar), con **un commit por prioridad cerrada** (excepción: dentro de Prioridad 2 conviene un commit por archivo para granularidad de reversión). Cada commit lleva en su mensaje: prioridad cerrada, archivos tocados, decisión humana invocada si aplica. La integración a `main` se hace al cerrar todas las prioridades 0-3, no antes. Esto preserva reversibilidad y permite que F2/F3 sigan funcionando contra `main` durante el saneamiento.

**Estimación de esfuerzo orientativa.** Esto no es un proyecto de semanas. La intervención completa de prioridades 0-3 es trabajo concentrado de **una sesión larga del autor (3-5 horas)** con apoyo del ejecutor para los barridos mecánicos. Prioridad 0 sola: 1-2 horas. Prioridad 1: 30-45 minutos. Prioridad 2: 1-2 horas (depende del volumen real de cruces `§N`). Prioridad 3: 1 hora. La validación de Prioridad 4 sobre una unidad real es trabajo aparte, no parte del saneamiento.

### 6.1 Prioridad 0 — resolver contradicciones bloqueantes

Archivos:

1. `CLAUDE.md` raíz
2. `viejo/unidades/CLAUDE.md`
3. `viejo/unidades/vocabulario-pautas.md`
4. `viejo/unidades/gramatica-pautas.md`

Objetivo:

- acotar el scope mal redactado de la regla de oro #5 sobre `viejo/` (§3.2);
- cerrar la contradicción sobre verbos del rótulo, **incluida la incoherencia interna de `gramatica-pautas.md:370` vs `:378`** (§3.1);
- decidir dónde vive de forma canónica la regla transversal y dónde viven solo los repertorios específicos.

**Criterios de aceptación (v2).**

- La regla de oro #5 del `CLAUDE.md` raíz, en su versión reescrita, cumple **las dos** propiedades siguientes simultáneamente: (a) menciona explícitamente `viejo/unidades/` como zona viva del rediseño donde sí se trabaja; (b) acota la prohibición de edición a un subconjunto identificable de `viejo/` (la subcarpeta del sistema CrewAI v5 anterior y cualquier otra que el autor designe como archivo). El criterio se verifica por **lectura humana del párrafo reescrito**, no por grep, porque la redacción literal puede variar sin que cambie la intención. Como apoyo, `grep -niE "viejo/?unidades" CLAUDE.md` debe encontrar al menos una mención positiva de `viejo/unidades/` como zona de trabajo activa.
- `grep -nE "PRACTIQUE|ANIME|CONSTRUYA|MODELE" viejo/unidades/CLAUDE.md viejo/unidades/*-pautas.md` produce un conjunto **coherente**: cada verbo aparece o validado o prohibido en todos los sitios, nunca las dos cosas.
- Las filas 4 y 12 de la tabla de errores recurrentes de `gramatica-pautas.md` ya no usan `CONSTRUYA` con polaridades opuestas.
- Una sola formulación canónica de "verbo del rótulo" reside en `viejo/unidades/CLAUDE.md`; las pautas solo contienen repertorios específicos, no redefinen la norma.

Sin esta pasada no merece la pena mover nada más.

### 6.2 Prioridad 1 — formalizar definiciones operativas básicas

Archivos:

1. `viejo/unidades/CLAUDE.md`
2. `.claude/rules/criterios-generacion-texto.md`

Objetivo:

- definir de forma única `metanota`, `cuerpo del rótulo` y `anexo`;
- asegurar que ambos documentos usan exactamente la misma frontera conceptual.

**Criterios de aceptación (v2).**

- Existe en `viejo/unidades/CLAUDE.md` una sección con título único (ej. *"Convenciones del bloque"*) con las tres definiciones.
- `criterios-generacion-texto.md` referencia esa sección por título exacto y **no redefine** los términos.
- `grep -nE "metanota|cuerpo del r" .claude/rules/criterios-generacion-texto.md viejo/unidades/CLAUDE.md viejo/unidades/*-pautas.md` no produce ninguna definición competidora.

### 6.3 Prioridad 2 — sustituir referencias frágiles

Archivos:

- todos los `*-pautas.md` que remiten al hub o a otras pautas.

Objetivo:

- cambiar referencias basadas solo en `§N` por referencias basadas en título exacto;
- reducir `§bis` como ancla principal;
- dejar las referencias legibles y estables.

**Orden interno seguro del barrido (añadido v2).** El riesgo de regresión durante este barrido es real: si una pauta cambia título a mitad de ejecución, las referencias rotas se multiplican.

1. **Congelar títulos.** Antes de tocar referencias, pasada de revisión de títulos en todos los archivos del scope. Si un título debe cambiar, se cambia ahora. Tras esta sub-pasada, los títulos quedan estables durante el resto de la prioridad 2.
2. **Inventariar cruces.** `grep -nE "§[0-9]+|§[0-9]+bis"` sobre el scope. Lista completa archivo por archivo.
3. **Reescribir** referencias a título exacto, archivo por archivo. Un commit por archivo dentro de esta prioridad.
4. **Verificar.** Repetir el grep del paso 2. Las coincidencias que queden deben estar justificadas (referencia interna al mismo archivo, no cruce a otro).

**Criterios de aceptación (v2).**

- `grep -nE "§[0-9]+bis" viejo/unidades/CLAUDE.md viejo/unidades/*-pautas.md` produce ≤ 5 coincidencias justificadas.
- Ninguna cita `§N` cruzada entre archivos sobrevive sin acompañamiento de título exacto.

### 6.4 Prioridad 3 — limpiar duplicaciones normativas

Archivos:

- `viejo/unidades/CLAUDE.md`
- `vocabulario-pautas.md`
- `gramatica-pautas.md`
- después el resto.

Objetivo:

- sacar del nivel de sección lo que realmente ya es regla transversal (aplicando el filtro binario de §3.3 / §5.1);
- dejar en cada pauta solo lo que sea de verdad propio de esa sección.

**Criterios de aceptación (v2).**

- Ninguna regla transversal aparece literalmente reformulada en más de un archivo. Las pautas remiten al hub por título exacto cuando una regla transversal aplica.
- Cada bloque normativo que vive en una pauta pasa el test binario: *"¿esto aplicaría también a otras secciones?"*. Si la respuesta es sí en cualquier caso real, el bloque sube al hub.

### 6.5 Prioridad 4 — validar el sistema ya saneado con una unidad real

Objetivo:

- comprobar que la nueva distribución de reglas funciona sobre una unidad completa;
- revisar si el agente resuelve mejor y con menos ambigüedad;
- medir si caen los errores repetidos de interpretación.

**Criterios de aceptación (v2).**

- Una sección redactada después del saneamiento, auditada por la skill F2, produce un informe **con menos ⚠ por ambigüedad de criterio** que la baseline previa (U1 vocabulario / U1 gramática del trabajo anterior).
- Las preguntas que el ejecutor hace al autor durante la redacción bajan en frecuencia respecto a sesiones anteriores comparables.

### 6.6 Prioridad 5 — reevaluar automatización

Solo después de las prioridades 0-4:

- skill F2 como auditoría manual;
- subagent F3 como auditoría aislada en sesiones largas;
- hooks solo para reglas inequívocas y de detección estable.

---

## 7. Qué sobra y por qué se elimina de este documento

El seguimiento anterior por fases ya no es el documento adecuado. Se elimina del documento consolidado porque hoy aporta más ruido que decisión.

Se considera prescindible, dentro de este documento:

1. el diario detallado F1/F2/F3/H3;
2. la narrativa paso a paso de autorizaciones entre fases;
3. la repetición de estados de piloto ya cerrados;
4. los logs largos sobre si F2 abría o no F3;
5. la trazabilidad de debate meta sobre slash commands, skills y hooks cuando ya existe una conclusión madura.

No se elimina la conclusión útil extraída de ese trabajo; solo se elimina su formato de bitácora, porque ya no ayuda a tomar la decisión principal.

---

## 8. Qué sí se conserva del trabajo previo sobre tooling

Se conservan estas conclusiones, porque sí siguen siendo útiles:

1. **F2 skill de auditoría:** validada como carril seguro de lectura y checklist.
2. **F3 subagent auditor:** validado como carril opcional de aislamiento de contexto en sesiones largas.
3. **F4 hooks:** no recomendables todavía para reglas sensibles mientras el contrato base siga ambiguo.

Traducción práctica:

- la infraestructura de auditoría está razonablemente resuelta;
- el cuello de botella actual ya no es técnico, sino documental.

---

## 9. Plan de saneamiento documental mínimo viable

### 9.1 Resultado exigible del primer lote de edición

El primer lote de edición debería dejar cerradas estas cinco condiciones:

1. La regla sobre `viejo/` queda reescrita con scope acotado: `viejo/unidades/` reconocida como zona viva del rediseño y la prohibición de edición limitada a la subcarpeta del sistema CrewAI v5 anterior (§3.2).
2. La política de verbos del rótulo queda escrita una sola vez como norma transversal.
3. Vocabulario y Gramática dejan de contradecir esa política en sus repertorios y errores recurrentes.
4. `metanota`, `cuerpo del rótulo` y `anexo` quedan definidos en un solo punto canónico.
5. Las referencias más frágiles dejan de depender exclusivamente de `§N` y `§Nbis`.

### 9.2 Qué no intentar en el primer lote

No conviene mezclar ese saneamiento con:

- refactor arquitectónico grande;
- creación de nuevos comandos o agentes;
- reorganización de carpetas;
- migración masiva de contenido entre documentos;
- hooks de enforcement.

El primer lote debe ser quirúrgico, no ambicioso.

---

## 10. Criterio de cierre: cuándo este sistema pasará a estar realmente bien

Podrá decirse que el modelo `CLAUDE.md` + pautas está bien cerrado cuando se cumplan todas estas condiciones:

1. ninguna decisión editorial relevante dependa de elegir entre dos documentos que dicen cosas distintas;
2. las reglas transversales estén centralizadas de verdad, no solo declaradas como principio;
3. las pautas de sección añadan especificidad sin reescribir la constitución del sistema;
4. un auditor humano y la skill F2, sobre la misma sección, coincidan en ≥ 80% de los ítems del checklist 1-24 con veredicto idéntico (✅/❌/⚠) — medición caso a caso, no estimación;
5. el hook potencial futuro solo tenga que vigilar reglas inequívocas, no interpretar criterios abiertos.

Mientras eso no ocurra, el modelo será prometedor, pero todavía no completamente fiable.

---

## 11. Recomendación final del revisor

No recomiendo desmontar el sistema.

No recomiendo seguir acumulando validación de tooling como sustituto de la limpieza documental.

Sí recomiendo una pasada de saneamiento real, empezando por cuatro archivos:

1. `CLAUDE.md`
2. `viejo/unidades/CLAUDE.md`
3. `viejo/unidades/vocabulario-pautas.md`
4. `viejo/unidades/gramatica-pautas.md`

Ese es el punto donde hoy se concentra el mayor riesgo de error sustancial. Si esa base queda cerrada, el resto del sistema tiene buena pinta y merece mantenerse.
