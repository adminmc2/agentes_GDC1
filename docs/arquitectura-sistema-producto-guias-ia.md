# Arquitectura del sistema producto para guias didacticas con IA

> Estado: borrador de arquitectura; documento de definicion, no norma operativa.
> Ultima revision: 2026-09-05.
> Funcion: fijar el objetivo real del sistema futuro, ordenar su construccion por fases y separar claramente el producto final de las herramientas transitorias de ingenieria.
> Criterio de lectura: toda decision externa entra como candidata y debe revalidarse con fuente primaria y prueba en contexto.

## 1. Correccion de marco

El objetivo final no es operar este proyecto dentro de VS Code.

El sistema puede construirse con Claude Code, pero su operacion final no debe depender de Claude Code como interfaz de uso.

El objetivo final es construir un sistema robusto al que el usuario entra directamente, aporta contenido o fuente, y desde ahi se ejecuta todo el flujo operativo con apoyo de IA y revision humana.

Consecuencia directa:

- Claude Code sirve ahora para auditar, definir, prototipar y ordenar.
- Claude Code no debe confundirse con el producto final.
- VS Code puede seguir siendo entorno de ingenieria, pero no interfaz obligatoria del usuario final.

## 1.1 Principio de construccion

El sistema no debe decidirse entero antes de empezar a construirse.

La estrategia correcta es:

- prototipar por fases;
- probar cada funcion en pequeño;
- conservar lo que ya funciona;
- sustituir o rediseñar solo lo que se demuestre insuficiente;
- evitar una arquitectura cerrada por anticipacion sin validacion real.

Dictamen:

- la fase 1 actual fue practicamente funcional como proceso;
- por tanto no hay que destruirla por moda arquitectonica;
- hay que reutilizarla como punto de partida y convertirla poco a poco en parte de un sistema mayor.

## 1.2 Regla de decision

Este documento no debe convertir una propuesta en decision solo porque exista un analisis previo sobre ella.

Jerarquia correcta de evidencia:

1. funcionamiento real ya probado en este proyecto;
2. contratos, scripts y artefactos reales del repositorio actual;
3. documentacion oficial o fuente primaria del producto o framework;
4. analisis comparativos del repositorio de propuestas;
5. opinion o preferencia arquitectonica.

**Nivel y estatuto son dos ejes distintos.** El nivel dice **que tipo** de evidencia es. El estatuto dice **cuanto dura**: una evidencia esta *formalizada* cuando vive en un artefacto versionado del repositorio, y es *de sesion* cuando solo existe en el hilo de trabajo que la produjo.

Los dos ejes no se mezclan. Un prototipo ejecutado contra los artefactos reales del proyecto es evidencia de **nivel 1 con estatuto de sesion**: no baja a nivel 3 por no estar formalizada, y formalizarla no la sube de nivel, le cambia el estatuto. Confundir los dos ejes lleva a dos errores simetricos: descartar evidencia buena por provisional, o tratar como probado lo que solo esta escrito.

Consecuencia:

- el repositorio de propuestas sirve para abrir caminos y ahorrar exploracion ciega;
- no obliga a adoptar nada;
- toda pieza externa que entre en la arquitectura debe revalidarse con fuente primaria y con prueba en contexto.

**El veredicto de un catalogo ajeno no viaja.** El repositorio de propuestas se construyo para decidir que entra en APEX: un producto clinico regulado, multiusuario, con sus propias lineas rojas de datos personales y de compliance. Sus etiquetas de estado —adoptado, a probar, referencia— son decisiones **de aquel dominio**.

De una ficha transfiere su contenido tecnico verificable. No transfiere su veredicto. Una pieza marcada como adoptada alli entra aqui como candidato de nivel 3, igual que cualquier otra, y no cambia de nivel hasta probarse contra material real de este proyecto. Confundir las dos cosas es la version silenciosa de cerrar por anticipacion: se hereda una decision sin haberla tomado.

## 2. Diagnostico rector

El sistema actual funciona, pero funciona como procedimiento asistido, no como producto unificado.

Hoy el trabajo esta repartido entre:

- documentos operativos;
- scripts;
- validaciones parciales;
- decisiones manuales;
- dos repositorios con fronteras todavia imperfectas.

Esto permite producir, pero no cumple todavia el objetivo de un sistema unico en el que el usuario entra y todo el proceso ocurre ahi de forma robusta.

El problema de fondo no es solo de repositorios. Es de arquitectura operativa.

Tambien es un problema de cierre prematuro de decisiones:

- hoy ya sabemos bastante del flujo real;
- pero todavia no conviene fijar demasiado pronto ni el storage final, ni el runtime final, ni el proveedor final de LLM;
- esas decisiones deben resolverse segun lo que vaya demostrando cada prototipo.

## 3. Definicion correcta del sistema futuro

El sistema futuro debe tener cuatro capas separadas:

### 3.1 Capa de producto

Es la interfaz real para el usuario.

Desde ahi el usuario debe poder:

- subir o seleccionar la fuente;
- lanzar una tarea;
- ver el estado;
- revisar resultados;
- aprobar, devolver o cerrar una fase.

### 3.2 Capa de orquestacion

Es el motor que gobierna el flujo.

Debe decidir:

- que tarea se ejecuta;
- en que orden;
- con que dependencias;
- con que reintentos;
- con que gates de validacion;
- en que puntos hace falta intervencion humana.

### 3.3 Capa de inteligencia

Aqui viven los LLM, vision models, parseres y herramientas auxiliares.

Decision clave:

- no hay que casar el sistema con un unico LLM por ideologia;
- hay que elegir la mejor herramienta por tarea;
- una misma operacion puede combinar IA multimodal, parser textual y validadores deterministas.

### 3.4 Capa de persistencia

Aqui viven:

- repositorios;
- base de datos o indices;
- almacenamiento de PDFs y artefactos;
- memorias correctivas;
- logs;
- trazabilidad y estados.

## 3.5 Alcance de producto

La solucion no se diseña solo para NC1 como artefacto aislado.

La idea de fondo es una solucion que permita desarrollar guias didacticas del profesorado a partir de libros base, marcos metodologicos y recursos complementarios.

NC1 es el caso actual.

NC2 es el siguiente caso real que ya condiciona el diseño.

Consecuencia:

- no hace falta sobredisenar desde ya un sistema universal para cualquier editorial;
- pero tampoco conviene dejarlo tan pegado a NC1 que no sirva para Companeros 2.

Cautela: NC2 no puede usarse como fuerza de diseno mientras no este medido que hay atado a NC1. Hoy el acoplamiento es real y verificable en el repositorio: `"curso": "nc1"` en el schema, valores fijos de autoevaluacion NC1, un enum de tiempos verbales que excluye Participio y Gerundio porque NC1 no los usa, el acoplamiento de cabecera con `unidades/nc1-curso.json`, la convencion de nombres `nc1-` y unas 6.700 lineas de registries de nivel A1. El inventario explicito de esas ataduras es tarea de Fase 0.

## 3.6 Topologia de repositorios de construccion

La construccion del sistema nuevo no se repartira entre varios repositorios de aplicacion.

La separacion correcta es esta:

- **este repositorio actual** sirve para cerrar la definicion, auditar el sistema existente y conservar el contexto editorial y los artefactos que actuan como fuente de contraste;
- **repo B** sigue siendo fuente metodologica viva de consulta, pero no lugar de construccion;
- **el sistema nuevo** se construye entero en un **unico repositorio nuevo** de producto, con topologia **monorepo**.

Consecuencia operativa: frontend, servicio web, worker, modelo de datos, migraciones, tests, configuracion de Railway y artefactos de Spec Kit viven en ese unico repositorio nuevo. Puede haber varios servicios desplegados, pero no varios repositorios de producto desde el arranque.

Hay una frontera material que el monorepo no elimina: los inventarios viven versionados aqui, pero los PDFs fuente estan fuera de Git por derechos (`unidades/**/fuente/*.pdf` en `.gitignore`). El repositorio nuevo no los hereda al clonarse. Antes de cualquier spike que toque fuente debe declararse un mecanismo explicito de acceso —ruta local configurable, copia controlada o almacenamiento autorizado— y registrarlo segun §7.

Mientras el contrato de fase 1 siga gobernado en este repositorio, el repo nuevo lo consume como insumo auditado. Mover la autoridad de ese contrato exige una decision explicita, no una mudanza tacita por arrastre.

Matiz de arranque: la lista de arriba es el **destino** del repositorio, no su contenido del primer dia. Lo primero que vive alli son los prototipos de Fase 0 —tareas 1 y 2—, no un andamiaje de cuatro servicios vacios esperando contenido.

## 3.7 Modo de operacion inicial: Railway

Para la **primera version operativa** del sistema, la plataforma objetivo del repositorio nuevo pasa a ser **Railway**. Esto no decide todavia la plataforma final de largo plazo, pero si fija el primer entorno real donde el producto debe correr de punta a punta.

La decision no nace de cero, y conviene separar dos planos que la version anterior mezclaba.

Los **archivos** son evidencia de nivel 2: `railway.toml` y `Dockerfile` fijan builder, healthcheck y comando de arranque; `diagrama.py` prueba un patron de servicio HTTP con `/api/status` y uso de `DATABASE_URL`; `web/index.html` prueba que ya existe una shell de interfaz y un repertorio de endpoints. `Procfile` queda como rastro historico, no como anclaje de arranque vigente.

El **despliegue** es evidencia de nivel 1 con estatuto formalizado: este repositorio ya estuvo desplegado en Railway con gate cumplido —HTTP 200 en la URL publica, `/api/version` sirviendo la version del CHANGELOG, build slim funcional con dos dependencias—. El stack se retiro en v11.21 y se **reactivo en v12.22**, que es de donde vienen los archivos actuales. La entrada `B5` de `REVIEW.md` conserva ese gate; su nota de estado quedo obsoleta y se corrige aparte.

Todo esto ancla Railway como camino operativo **ya probado** y una base conceptual web/API. No prueba que el modelo de datos actual ni el codigo del dashboard deban migrarse tal cual al producto nuevo.

La organizacion inicial correcta no es un mosaico difuso de scripts, sino un sistema con **cuatro componentes operativos**:

1. **Frontend web.** Interfaz para entrar al sistema, seleccionar o subir fuente, lanzar tareas, ver estados, revisar incidencias y aprobar cierres. Puede reaprovechar ideas de navegacion y analitica del dashboard actual, no necesariamente su codigo ni su lenguaje visual.
2. **Servicio web / API.** Capa HTTP que aplica el control de acceso que se cierre en Fase A, expone acciones, registra estados, coordina aprobaciones y entrega al frontend el estado vivo del sistema. No presupone todavia un sistema completo de cuentas si la v1 arranca con acceso restringido.
3. **Worker de tareas largas.** Proceso separado del HTTP para extraccion, parseo documental, validaciones, generacion y tareas que no deben bloquear la interfaz. La frontera HTTP / jobs largos si queda fijada desde el principio; la forma concreta de la cola no.
4. **Persistencia y artefactos.** Separar desde el principio la persistencia operativa de la persistencia canonica del contenido. La operativa —estados, jobs, aprobaciones y control de acceso— si puede vivir en Postgres desde la v1. La canonica del contenido editorial y la trazabilidad fina de artefactos siguen abiertas a prueba (§5.4, §6.3.3). Los PDFs y artefactos viven fuera de Git con un mecanismo de almacenamiento todavia por cerrar.

En Railway esto se traduce, como minimo, en **tres piezas desplegadas**: un servicio web, un worker y una base de datos Postgres para la capa operativa. La separacion entre frontend y API puede arrancar en un solo servicio mientras el producto se estabiliza, pero la separacion entre HTTP y jobs largos conviene existir desde el principio. El almacenamiento de artefactos no queda resuelto por nombrar Railway: antes del paso 5 de §3.8 hay que decidir si la v1 trabaja con volumen controlado, bucket autorizado o acceso local restringido.

## 3.8 Orden practico de construccion de componentes

La construccion no debe empezar por todos los componentes a la vez. El primer recorrido end-to-end que da sentido a este orden no es generico: es el **gate de fidelidad fuente -> inventario**, desde la seleccion de una unidad o PDF hasta la revision humana de incidencias y el cierre de la tarea.

Ese gate no se inventa aqui: existe ya como prototipo por la tarea 1 de Fase 0. Lo que este orden construye no es el gate, sino el recorrido operativo que lo envuelve —interfaz, estados, API, worker— alrededor de algo que a esas alturas ya funciona.

Antes del paso 1 hay una precondicion material: declarar como accede el repositorio nuevo a los PDFs con derechos sin violar §7.

El orden util es este:

1. **Cerrar la interfaz minima.** Un frontend utilizable para entrar, elegir una unidad o PDF, lanzar el gate de fidelidad y ver su estado e incidencias.
2. **Cerrar el modelo de estados.** Definir en base de datos que es una tarea, que estados tiene, quien la lanza, quien la revisa y que significa aprobar o devolver.
3. **Cerrar la API del flujo minimo.** Crear los endpoints que unen frontend, persistencia operativa y ejecucion de la tarea en un solo recorrido visible.
4. **Separar el worker y declarar la cola minima.** Sacar del servicio web toda tarea larga: extraccion, comparacion, parseo, validacion y generacion, con un mecanismo explicito de entrega de trabajos aunque al principio sea simple.
5. **Cerrar el almacenamiento de artefactos.** Elegir y montar el mecanismo que guarda PDFs fuente, salidas intermedias y artefactos finales fuera de Git, con referencias trazables desde la capa operativa.
6. **Ampliar capacidad por capacidad.** Una vez exista ese esqueleto operativo, integrar gates, parseres, modelos y fases nuevas sin rehacer la base.

La regla de fondo es simple: **primero un flujo end-to-end visible en Railway; despues crecimiento por componentes**, no una arquitectura completa dibujada pero sin recorrido operativo.

## 3.9 Plano de operacion y plano de construccion

Operacion y construccion no deben describirse como si fueran la misma cosa.

- **Plano de operacion del producto.** Lo componen el frontend, la API, el worker, la base de datos y el almacenamiento de artefactos desplegados en Railway. Este plano responde a la pregunta: **como usa el sistema un usuario real cuando ya esta encendido**.
- **Plano de construccion del producto.** Lo componen la constitution del repositorio nuevo, Spec Kit, superpowers, `CLAUDE.md`, VS Code, Claude Code, tests, migraciones y despliegues del monorepo nuevo. Este plano responde a la pregunta: **como se diseña, implementa, valida y despliega cada componente del sistema**.

El primero gobierna la experiencia del usuario final. El segundo gobierna el trabajo de ingenieria.

Papel de cada pieza en el plano de construccion:

- **La constitution del repositorio nuevo** es el contrato rector del plano de construccion. `CLAUDE.md` y las reglas path-scoped aterrizan esa constitution a operativa local; no la sustituyen.
- **Spec Kit y superpowers** cubren dos mitades del mismo metodo de construccion: el primero define constitution, specify, plan, tasks, implement y converge; el segundo disciplina implementacion y verificacion. Su adopcion formal sigue sujeta al criterio de §5.1.1.
- **Claude Code** ejecuta trabajo de ingenieria sobre el repositorio: analiza, edita, valida y automatiza.
- **VS Code** es una de las superficies posibles de trabajo para esa construccion.
- **Railway** no define como se construye el codigo: define donde se despliega y opera el resultado.

La consecuencia practica es que frontend, backend, worker y persistencia no se "hacen con Spec Kit" ni "operan con Claude Code": se **construyen** con ese workflow y despues **operan** como servicios propios del producto.

## 4. Que papel tiene Claude Code entonces

Claude Code encaja como herramienta de ingenieria del sistema, no como sistema final de operacion.

Su utilidad real aqui es:

- ayudar a auditar el flujo actual;
- ayudar a definir contratos y reglas;
- ayudar a implementar scripts, validadores y prototipos;
- servir como banco de pruebas para agentes, memoria y gates.

La documentacion oficial de Claude Code confirma varias piezas reutilizables para la ingenieria del sistema:

- `CLAUDE.md` sirve para reglas y contexto, no como enforcement duro.
- Las restricciones duras deben vivir en hooks o validaciones ejecutables.
- Los subagentes sirven para roles repetibles y acotados.
- Los worktrees sirven para aislamiento seguro en corridas paralelas o de riesgo.
- GitHub Actions sirve mejor como automatizacion remota posterior, no como punto de partida del producto.

Anclaje real en el repositorio: este punto no es solo doctrina externa de nivel 3. La separacion entre reglas blandas y enforcement duro ya esta parcialmente implementada aqui —existen `scripts/hooks/pre-commit` y reglas path-scoped en `.claude/rules/` (`final-style.md`, `redaccion-fase.md`, `u1-final-locked.md`)— y por tanto cuenta como evidencia de nivel 2.

Dictamen:

- Claude Code puede ayudar a construir el sistema.
- Claude Code no es el sistema que el usuario final debe usar.

## 4.1 Criterio de proveedor y coste

El sistema futuro no debe quedar atado a una suscripcion de uso interactivo.

Punto practico de arquitectura:

- para un producto que ejecuta tareas de forma programatica, la capa de modelos debe pensarse como capa API o capa de proveedores intercambiables;
- no debe darse por hecho que una suscripcion de consumo resuelva por si sola el backend del producto;
- la separacion observada entre consumo y plataforma comercial refuerza que el sistema debe diseñarse como BYOK o proveedor abstracto.

Consecuencia de coste:

- Claude puede seguir siendo candidato para tareas de alto valor;
- pero el sistema debe permitir enrutar subtareas a modelos mas baratos o locales cuando no haga falta el mejor modelo;
- la unidad economica correcta no es precio por token aislado, sino coste por tarea cerrada.

## 5. Estado actual auditado

### 5.1 Lo que ya existe y es aprovechable

- una fase 1 de extraccion ya definida;
- un contrato JSON canonico por unidad;
- validadores parciales;
- scripts de integracion y soporte;
- una capa editorial final en repo A;
- doctrina metodologica relevante en repo B.

Tambien existe un repositorio de propuestas y analisis ya cribado que debe seguir tratandose como fuente activa de exploracion.

Pero su valor correcto no es "decidir por nosotros", sino reducir el espacio de busqueda y proponer candidatos que luego se revalidan.

### 5.1.1 Espacio de busqueda de candidatos externos — cero adoptados

Ninguno de los candidatos de esta seccion esta adoptado ni preseleccionado. La seccion mezcla dos planos de evidencia: **nivel 3** cuando cita documentacion oficial o fuente primaria de cada pieza, y **nivel 4** cuando resume como el repositorio de propuestas las compara, agrupa o prioriza. La funcion de la seccion es reducir el espacio de busqueda, no crear inercia de adopcion.

**Regla de spike previo.** Ninguna pieza externa entra en la arquitectura sin una prueba contra una tarea real de este proyecto, y el criterio de exito de esa prueba debe estar **escrito antes de ejecutarla**. Un spike sin criterio previo no cuenta como evidencia de nivel 1, porque siempre se puede leer como confirmacion de lo que ya se queria hacer.

Estado tras una segunda pasada de contraste:

- `spec-kit`: la documentacion oficial de GitHub lo presenta como toolkit de build spec-driven con constitution, specify, plan, tasks, implement y converge. Por tanto sirve como candidato de metodologia de construccion del sistema. No sirve, por si mismo, como runtime del producto.
- `langgraph`: la documentacion oficial lo presenta como framework de orquestacion para agentes stateful con durable execution, human-in-the-loop y memoria. Por tanto es candidato real para la capa de orquestacion si en fases posteriores se demuestra que hace falta ese nivel de durabilidad.
- `n8n`: la documentacion oficial lo presenta como plataforma de workflows y agentes con canvas visual, codigo, integraciones, human-in-the-loop y despliegue en infraestructura propia o cloud. Por tanto es candidato real para automatizacion e integraciones, no una decision automatica sobre el nucleo del producto.
- `Claude Platform API`: la documentacion oficial presenta una capa programatica con acceso API, pricing por uso, modelos, tools, structured outputs y batch processing. Por tanto la capa de modelos debe pensarse como backend programatico y no como extension de una interfaz de consumo.
- `Claude Code`: la documentacion oficial lo presenta como herramienta de desarrollo multi-superficie y menciona Agent SDK para construir workflows propios. Por tanto sigue siendo valido como herramienta de ingenieria, no como prueba de que deba ser la interfaz final del sistema.

**Tercera pasada, con el repositorio de propuestas leido entero** (150 fichas, 14 protocolos y el tracker de solapes). Aparecen dos grupos que las dos pasadas anteriores no habian mirado.

**Grupo 1 — ingesta y parseo documental.** Es el hallazgo importante de la pasada, porque toca de lleno la capacidad 1 y no estaba considerado en ninguna parte de este documento:

- `Docling` (IBM / LF AI, MIT): PDF a Markdown o JSON conservando **layout, orden de lectura y estructura de tablas**, con OCR, en ejecucion local sin servicio externo. Disponible como CLI, libreria y servicio.
- `MarkItDown` (Microsoft, MIT): conversion rapida de documentos digitales; **no hace OCR**.
- `Chandra`: OCR local de alta fidelidad. El codigo es permisivo pero el modelo lleva otra licencia, que hay que leer antes de contar con el.
- `Mistral OCR`: extraccion estructurada potente, con opcion de contenedor propio.
- `anydoc`: conversion muy rapida, solo capa de texto.

El catalogo ya formula un reparto por tipo de documento —parser ligero para el limpio, parser con layout para el complejo— que aqui vale como punto de partida a validar, no como conclusion.

**Grupo 2 — metodo de construccion.** Cuatro piezas que gobiernan **como** se construye, no que se construye:

- `spec-kit` y `superpowers` funcionan como par: el primero define el que y las reglas, el segundo construye y verifica el como con prueba primero, revision y evidencia. Por separado cada uno pierde la mitad de su valor, y este documento solo habia mirado el primero.
- contrato de diseno escrito, en la linea del patron `DESIGN.md`: la direccion estetica se fija en un documento que el agente obedece, no en una herramienta que la genera en cada pantalla.
- `ponytail`: ruleset contra la sobreconstruccion. Es disciplina de implementacion, subordinada al metodo; no es pieza rectora del arranque y no debe tratarse como tal.

Ninguna de estas nueve piezas esta adoptada. **Hoy todo este bloque es de nivel 4**: llega leido del catalogo, no contrastado en fuente primaria. Abrir la documentacion oficial de cada pieza lo sube a nivel 3, y solo el spike de Fase 0 puede llevarlo mas arriba. Todas arrastran el aviso de veredicto ajeno de §1.2 y a todas les aplica la regla de spike previo con criterio escrito.

### 5.1.2 Candidatos utiles pero todavia no ratificados por fuente primaria suficiente o por prueba local

- `agentic-sdlc`: hoy sirve como marco conceptual de reparto humano decide, agente ejecuta. No debe tomarse como arquitectura adoptada sin mas.
- `orquestacion-agentes-caminos`: hoy sirve como criterio de analisis para separar carril determinista y carril agentico. El criterio es util; la eleccion de framework sigue abierta.
- `decision-memoria-agente`: hoy sirve como alerta metodologica correcta: separar memoria canonica, memoria de trabajo y memoria runtime. La implementacion concreta sigue abierta.
- `loops-agentes`: hoy sirve como catalogo de patrones de bucles cerrados. Su adopcion debe depender de probar si realmente mejora el flujo de este proyecto.
- `blueprint-local-first-mac`: hoy sirve como patron de routing por coste, sensibilidad y complejidad. No debe entrar en el nucleo del diseño sin una prueba posterior sobre tareas reales del proyecto.

Dictamen de esta segunda pasada:

- las propuestas revisadas si valen como mapa de candidatos;
- no valen como justificacion suficiente para cerrar una decision de arquitectura;
- toda adopcion futura debe pasar por fuente primaria y prueba funcional en contexto.

### 5.2 Lo que falta para que eso sea producto

- una interfaz unica de entrada para el usuario;
- una orquestacion explicita del flujo completo;
- un modelo claro de estados y aprobaciones;
- gates de fidelidad mas fuertes;
- configuracion portable no atada a una maquina concreta;
- una frontera cerrada entre conocimiento historico, ejecucion y publicacion.

### 5.3 Fuentes de referencia que habra que integrar

La extraccion del PDF no es el producto final. Es la primera capa.

Despues de extraer y estructurar la informacion, el sistema debe poder integrar fuentes de referencia ya definidas para construir el material posterior.

Eso incluye, como minimo:

- marco teorico metodologico;
- pautas operativas y criterios didacticos del sistema actual;
- fuentes por dominio como gramatica, vocabulario, dinamicas, dramatizacion y recursos editoriales;
- contratos de tarjetas, pildoras y materiales complementarios;
- criterios de dashboard y de analisis transversal ya existentes.

Dictamen:

- estas fuentes no deben reescribirse cada vez;
- deben integrarse como capa de referencia estable que el sistema consulta para construir la propuesta final.

### 5.4 Lo que aun no debe decidirse por adelantado

Con la evidencia actual, todavia no conviene fijar como decisiones cerradas:

- el runtime final de agentes;
- la forma canonica final de persistencia del contenido editorial;
- el proveedor principal de modelos, y tampoco el gateway o agregador por el que se acceda a ellos;
- la plataforma final de despliegue, aunque la primera version operativa se montara en Railway;
- si el producto consume un sistema de diseno ya existente o solo su patron de contrato escrito;
- si el dashboard seguira separado o se integrara;
- si la capa de automatizacion visual tendra o no un papel relevante.

Aviso sobre dos de ellas. **Railway queda fijado aqui como plataforma operativa provisional** para la primera version del **repositorio nuevo de producto**, porque ya hay anclaje tecnico suficiente en el repositorio actual y hace falta un destino real de construccion. Eso decide **donde correra primero** el sistema; no resuelve por si solo la entrega, que depende de usuario, derechos, alcance y modelo de uso (§9.0a), ni obliga a que Railway sea la plataforma final. Y el gateway de modelos es una pieza de implementacion: la decision que va antes es la regla de exposicion de la fuente (§7), no la configuracion de un proveedor concreto.

La distincion que evita contradicciones es esta: **persistencia operativa** de tareas, estados, jobs y control de acceso puede fijarse ya; **persistencia canonica del contenido editorial y de su trazabilidad final** sigue abierta y debe resolverse con la prueba diferida de §6.3.3.

Estas piezas deben resolverse cuando cada fase haya producido evidencia funcional suficiente.

### 5.5 Matriz de decisiones abiertas

La forma correcta de cerrar las decisiones abiertas no es por preferencia tecnica, sino por evidencia y por prueba minima suficiente.

| Decision abierta | Evidencia actual | Prueba minima necesaria | Cuando decidir |
|---|---|---|---|
| Runtime de orquestacion | Hoy ya existe flujo real, pero repartido entre documentos, scripts, decisiones humanas y validaciones parciales. Tambien esta claro que el sistema necesita gates y estado, pero no esta demostrado que necesite ya un runtime agentico complejo. | Construir un primer recorrido end-to-end de una sola capacidad con estados visibles, reintentos simples y aprobacion humana. Si ese flujo no cabe con claridad en una orquestacion ligera, se justifica evaluar runtime mas fuerte. | Despues de cerrar el primer recorrido end-to-end operativo de una fase real. |
| Persistencia canonica final del contenido editorial | El JSON por unidad ya funciona para extraer, validar y conservar artefactos. Lo no probado todavia es si basta para consulta transversal, versionado operativo, trazabilidad fina y reutilizacion NC2. | Comparar un mismo caso real en tres modos: solo JSON, JSON + indice derivado, y modelo con almacenamiento mas estructurado. Medir coste de escritura, consulta transversal, trazabilidad y facilidad de alimentar fases posteriores. | Despues de probar el primer flujo completo desde PDF hasta artefacto reutilizable. |
| Proveedor principal de modelos | Esta probado que la capa debe ser programatica y no depender de una interfaz de consumo. No esta probado todavia que un solo proveedor cubra bien coste, vision, fiabilidad y tareas auxiliares. | Ejecutar un banco pequeno de tareas reales del proyecto separando vision, estructuracion, verificacion y redaccion asistida. Comparar calidad cerrada por tarea y coste por tarea, no solo coste por token. | Cuando exista una bateria minima de tareas reales repetibles y medibles. |
| Dashboard separado o interfaz unificada | El dashboard actual ya demuestra valor analitico, pero no esta probado si debe seguir separado o convertirse en parte de la interfaz principal del producto. | Probar una version minima donde un mismo usuario haga una tarea completa y consulte incidencias y analitica sin cambiar de contexto. Si el dashboard separado introduce friccion o duplicacion, se integra. | Despues del primer prototipo de interfaz operativa. |
| Papel de una automatizacion visual tipo canvas | Hay evidencia de que puede servir para integraciones o automatizaciones externas, pero no de que sea la mejor base del nucleo operativo. | Probar una sola automatizacion periférica real, por ejemplo notificacion, ingestión o sincronizacion de artefactos, y medir si aporta claridad operativa o solo otra capa de complejidad. | Solo despues de que el nucleo del flujo principal este claro. |

Antes del primer recorrido end-to-end deben quedar escritas cuatro precondiciones operativas: mecanismo de acceso a la fuente con derechos, mecanismo de almacenamiento de artefactos, mecanismo de entrega de trabajos al worker y alcance real del control de acceso de la v1.

## 6. Capacidad 1: leer PDFs del libro por unidad y extraer la informacion

### 6.1 Objetivo funcional

El sistema debe poder tomar el PDF de una unidad didactica, extraer toda la informacion relevante y dejarla en una salida estructurada, validable y reutilizable por el resto del proyecto.

Precisiones ya confirmadas:

- la fuente siempre sera PDF;
- a veces el PDF vendra anotado o con soluciones y a veces no;
- el flujo no es puramente textual;
- el contrato exige tambien informacion visual y segmentacion editorial.

### 6.2 Estado real

Hoy esta capacidad existe como proceso asistido.

Ya tiene:

- contrato;
- formato canonico actual;
- validacion parcial;
- integracion;
- soporte documental;
- casos reales ya producidos.

No tiene todavia:

- una herramienta autonoma cerrada accesible como producto final;
- un gate de fidelidad suficientemente fuerte entre fuente y JSON.

### 6.3 Decision tecnica actual

Hay que separar dos funciones:

- extraccion primaria;
- control de fidelidad.

Extraccion primaria:

- debe seguir siendo multimodal;
- hoy puede seguir apoyandose en IA guiada;
- no debe degradarse a un parser textual plano si eso rompe el contrato.

Control de fidelidad:

- debe ser independiente del canal primario;
- `pdftotext` y equivalentes sirven para el drift textual, y solo para eso: devuelven cadenas sin posicion en la pagina;
- la separacion entre texto del alumno y anotacion del profesor **no es un problema de cadenas sino de disposicion**, y para eso hace falta un parser que conserve layout y orden de lectura (§5.1.1);
- su funcion es detectar divergencia, no sustituir la extraccion completa.

Dictamen:

- el problema principal no es falta de OCR;
- el problema principal es falta de un gate de fidelidad previo a integrar;
- y el carril de control no puede quedarse en `pdftotext`, porque la separacion que el contrato no cubre exige informacion que `pdftotext` no emite.

### 6.3.1 Analisis principal de este momento: la fuente real y el gate

Este analisis ocupa el lugar que antes tenia la persistencia, porque es la unica decision abierta de esta capacidad con evidencia disponible hoy.

#### La fuente no es la que declara el contrato

El contrato de fase 1 describe la entrada como *"PDF del libro del alumno con texto embebido"* (`fases/1-extraccion-inventario/prompt.md` y el `CLAUDE.md` de la fase). Es inexacto: la fuente real es la **edicion anotada del profesor**, con las soluciones sobreimpresas encima de la pagina del alumno.

Esto no es un hallazgo nuevo. El propio repositorio ya lo tenia escrito en otro documento: `docs/diagnostico-nc1-asesores.md` describe *"respuestas a los ejercicios en color lila sobre la pagina del alumno: texto editorial en lila que muestra las soluciones al docente (no presentes en el libro real del alumno)"*.

Por tanto el problema no es de descubrimiento sino de **contradiccion interna del repositorio**: dos documentos versionados dicen cosas distintas sobre la misma fuente, y el que gobierna la extraccion es el equivocado. Dos consecuencias:

- sube la prioridad, porque es un fallo activo y no una incognita abierta;
- baja el coste, porque la tarea es sincronizar dos documentos, no investigar.

#### Lo que el contrato no cubre

Ninguna regla vigente separa dos capas que conviven en la misma pagina fisica:

- el contenido del alumno, que es lo que el inventario debe capturar como texto visible;
- la anotacion del profesor —soluciones sobreimpresas y cajas de respuestas—, que tiene otro estatuto editorial.

Mientras esa separacion no este en el contrato, el extractor lee las dos capas sin ningun criterio para distinguirlas.

#### Requisitos del gate de fidelidad

El gate fuente -> JSON debe cumplir tres condiciones que la formulacion original de Fase C no recogia:

1. **Clasificar, no solo senalar.** Un gate que reporta fallos crudos es ruido y deja de leerse en una semana. El requisito es que separe divergencia real de artefacto de comparacion y que lo haga de forma legible. Que la clasificacion sea buena es el requisito; **como se implemente no se cierra aqui**.
2. **Cubrir la separacion alumno/anotacion**, no solo la coincidencia literal de cadenas.
3. **Declarar su coste de revision**, segun la regla transversal de §7.

**Punto de partida observado, no forma cerrada.** El prototipo de sesion sugiere tres regimenes de comparacion: cotejo contiguo para texto sin hueco; cotejo por palabras cuando la solucion sobreimpresa parte la frase en la capa de texto; y neutralizacion explicita de los glifos decorativos que el JSON transcribe por lectura visual y que la capa de texto no emite. Es un punto de partida util, no la forma definitiva del gate: se valida o se sustituye en Fase 0, con el mismo criterio que este documento exige a cualquier otra pieza. Fijar aqui la implementacion exacta seria cerrar por anticipacion justo lo que prohibe §1.1.

#### Estatuto de la evidencia disponible

Existe evidencia operativa de sesion —un prototipo de gate ejecutado sobre las diez unidades— que apunta a divergencias reales entre inventario y fuente.

Su clasificacion correcta, segun los dos ejes de §1.2, es: **nivel 1 por tipo** —es funcionamiento real probado contra los artefactos de este proyecto, no documentacion externa ni preferencia— con **estatuto de sesion**, porque no vive todavia en ningun artefacto versionado del repositorio. Formalizarla es tarea de Fase 0, y eso no la sube de nivel: le cambia el estatuto.

Consecuencia practica: no se cita como hecho establecido del repositorio, pero tampoco se descarta ni se degrada a indicio de segunda como si fuera material externo.

Aviso de no confusion: las entradas de `REVIEW.md` sobre U9 p101 con `imagen.descripcion` y `respuestas` corresponden al **bug 2 del matcher** —el validador no leia `imagen.descripcion`—, no a contaminacion de fuente. Coinciden en el mismo lugar del corpus y no deben apilarse como el mismo problema.

### 6.3.2 Estructura de almacenamiento: decision abierta, no cerrada todavia

Hoy la salida funcional es un JSON por unidad y eso ha servido.

Pero para el sistema futuro no conviene dar por cerrada todavia la forma canonica final de persistencia.

Decision provisional correcta:

- el JSON actual puede seguir siendo artefacto intermedio o artefacto de trabajo probado;
- la persistencia final debe decidirse segun su utilidad para todo lo que viene despues;
- hay que comparar al menos tres funciones antes de decidir: extraccion, consulta transversal y alimentacion de fases posteriores.

Por tanto, lo que debe definirse no es solo el formato de salida de fase 1, sino la mejor estructura para que la informacion extraida alimente:

- propuesta editorial final;
- materiales complementarios;
- analisis transversales;
- dashboard;
- reutilizacion futura en NC2.

Separacion provisional para la **primera version operativa en Railway**:

- **Postgres** guarda usuarios, tareas, estados, aprobaciones, auditoria y referencias a artefactos.
- **Almacenamiento de ficheros** guarda PDFs fuente, salidas intermedias y artefactos generados; no deben vivir en Git.
- **JSON por unidad** puede seguir existiendo como artefacto de trabajo o exportacion versionable, pero no debe confundirse con todo el almacenamiento operativo del sistema.

Regla de cierre para esta decision:

- no elegir formato por costumbre;
- no elegir BD por reflejo de ingenieria;
- elegir la estructura que mejor sirva al flujo completo una vez probado el primer recorrido end-to-end.

### 6.3.3 Persistencia: prueba diferida, no analisis principal de este momento

Esta prueba diferida se refiere a la **persistencia canonica del contenido editorial**, no a la persistencia operativa minima de tareas, estados y jobs que el primer prototipo ya puede montar para funcionar.

Esta decision estaba desarrollada aqui como el analisis profundo principal del documento. Se degrada a **prueba diferida** por tres razones:

1. La matriz de §5.5 ya fija que la persistencia se decide *despues de probar el primer flujo completo desde PDF hasta artefacto reutilizable*. Desarrollarla ahora en profundidad contradice el calendario que el propio documento establece.
2. Sus dos tests de falsacion —consulta transversal y trazabilidad de estados— exigen un modelo de estados y aprobaciones que todavia no existe. No son ejecutables hoy.
3. No se parte de cero, y el analisis lo trataba como si asi fuera. La fase 2 (reciclaje) **ya es** un computo cross-unidad sobre los JSON de unidad: `unidades/nc1-reciclaje.json` pesa hoy 354 KB, y existen `scripts/validar_cross_unidad.py`, `unidades/nc1-curso.json` y las vistas transversales del dashboard. Esa es evidencia de nivel 1 y 2, y hay que auditarla **antes** de disenar pruebas nuevas.

Nada de esto descarta la cuestion de persistencia ni la resuelve: la degrada de prioridad y corrige su punto de partida. El analisis que sigue se conserva integro como guion de la prueba futura, no como decision en curso.

Razon original por la que se priorizo (se conserva para trazabilidad del cambio):

- ya existe una persistencia real en produccion de trabajo, aunque sea provisional;
- ya existen artefactos, consultas y validaciones que permiten probarla;
- decidirla bien condiciona menos ideologicamente el sistema que decidir demasiado pronto el runtime;
- una mala decision de persistencia puede romper trazabilidad, consultas cross-unidad y reutilizacion posterior.

La pregunta correcta no es "JSON o base de datos".

La pregunta correcta es esta:

> ¿que forma de persistencia sirve mejor al primer flujo completo del producto sin destruir lo que ya funciona?

#### Hipotesis de trabajo

La hipotesis mas fuerte con la evidencia actual es:

- el JSON por unidad debe mantenerse como artefacto canonico de trabajo durante el primer prototipo operativo;
- si aparece una necesidad real de consulta transversal, estados finos o indexacion costosa, conviene añadir primero una capa derivada de indice o almacenamiento secundario;
- solo si esa capa derivada se demuestra insuficiente deberia plantearse una migracion a persistencia principal mas estructurada.

Esta hipotesis es falsable.

Quedaria debilitada si, en pruebas reales, ocurre alguna de estas tres cosas:

1. las consultas transversales necesarias son demasiado lentas o demasiado frágiles sobre JSON;
2. la trazabilidad de estados, revisiones y aprobaciones se vuelve torpe o ambigua;
3. alimentar fases posteriores desde JSON obliga a demasiadas transformaciones intermedias o duplicaciones.

#### Opciones reales a comparar

No hace falta comparar veinte arquitecturas. Basta con tres escalones reales:

1. JSON canonico por unidad como almacenamiento principal.
2. JSON canonico + indice derivado para consultas, estados o analitica.
3. Persistencia estructurada principal con exportacion o snapshot a JSON cuando haga falta.

La comparacion no debe hacerse con argumentos teoricos, sino con un mismo caso de uso real.

#### Caso de prueba minimo

El caso de prueba minimo deberia obligar a la persistencia a soportar cuatro cosas a la vez:

1. guardar el resultado de extraccion de una unidad con trazabilidad de origen;
2. registrar validaciones y estado de revision humana;
3. permitir una consulta transversal real, por ejemplo localizar un contenido o patron entre unidades;
4. alimentar un artefacto posterior sin reescritura manual completa.

Si una opcion resuelve bien 1 pero falla claramente en 2, 3 o 4, no sirve como persistencia suficiente del producto.

#### Criterios de evaluacion

La decision debe cerrarse con una rejilla corta y dura:

| Criterio | Pregunta de prueba |
|---|---|
| Escritura | ¿es simple y robusto registrar una nueva unidad sin operaciones frágiles o manuales? |
| Trazabilidad | ¿puede verse con claridad de dónde sale cada artefacto, validacion y aprobacion? |
| Consulta transversal | ¿pueden resolverse preguntas cross-unidad sin bricolaje continuo? |
| Alimentacion aguas abajo | ¿sirve bien como base para propuesta, materiales y analitica posterior? |
| Coste de evolucion | ¿añadir nuevos campos, estados o relaciones rompe poco y obliga a pocas migraciones? |

#### Secuencia de decision correcta

1. Mantener JSON como base de trabajo del primer prototipo.
2. Instrumentar una prueba real de consulta transversal y otra de estados de revision.
3. Si ambas pasan con coste razonable, no migrar todavia.
4. Si fallan, introducir una capa derivada antes de sustituir la base canonica.
5. Solo migrar a una persistencia principal mas estructurada si el fallo es repetido y afecta al flujo real, no por gusto de ingenieria.

#### Dictamen operativo sobre persistencia

Con la evidencia actual, la decision correcta no es "seguir para siempre con JSON" ni "migrar ya a base de datos".

La decision correcta es esta:

- conservar JSON como canon provisional del primer producto operativo;
- someterlo a dos pruebas reales: consulta transversal y trazabilidad de estados;
- usar el resultado de esas pruebas para decidir si basta con indice derivado o si hace falta una persistencia principal nueva.

### 6.4 Implicacion de producto

En el sistema futuro, el usuario no deberia lanzar esta fase desde un editor.

Deberia entrar a una interfaz, elegir la unidad o cargar el PDF, y el sistema deberia:

1. registrar la entrada;
2. ejecutar la extraccion;
3. correr validaciones;
4. marcar incidencias;
5. pedir revision humana cuando toque;
6. integrar solo cuando pase los gates.

## 6.5 Paso siguiente tras la extraccion: integrar conocimiento de referencia

Una vez extraida y almacenada la informacion, el siguiente paso del sistema no es simplemente guardar datos.

El siguiente paso es convertir esa base estructurada en materia prima para construir todo lo demas.

Eso exige una capa de integracion entre:

- lo que dice el libro;
- lo que exige el marco teorico metodologico;
- lo que dictan las fuentes especificas por dominio;
- lo que pide cada producto derivado.

Productos derivados ya identificados:

- propuesta final para profesorado;
- tarjetas;
- pildoras formativas;
- materiales complementarios;
- cualquier otro recurso editorial que el sistema defina.

Dictamen:

- esta capa de integracion es tan importante como la extraccion;
- si no se modela bien, el sistema solo sera un extractor, no una fabrica de guias didacticas.

## 6.6 Dashboard y analitica transversal

El dashboard actual no debe darse ni por conservado ni por descartado.

Debe reevaluarse como parte del producto futuro.

Preguntas correctas:

- que valor real aporta hoy;
- que partes son solo visualizacion;
- que partes son analitica necesaria para el sistema;
- si debe seguir como dashboard separado o integrarse en la interfaz principal del producto.

Minimo que debe preservarse conceptualmente:

- analisis de vocabulario;
- analisis gramatical;
- recursividad y recorridos cross-unidad;
- cualquier vista transversal que sirva para construir mejor la propuesta editorial.

## 7. Arquitectura objetivo por fases

### Regla transversal a todas las fases: coste en minutos de autor

Cada gate debe declarar su **coste en minutos de autor**. La automatizacion se prioriza por minutos de revision ahorrados, no por elegancia tecnica.

Razon: todos los gates de este documento terminan en "revision humana", y el revisor es una sola persona. El cuello de botella real del sistema no es el runtime ni el storage: es el tiempo de revision humana. Un gate que anade mas trabajo humano del que quita es una regresion aunque funcione tecnicamente.

Ejemplo de aplicacion correcta: el gate de fidelidad convierte "revisar dos o tres paginas al azar contra el PDF" en "revisar una lista corta de divergencias ya clasificadas". Ahorra minutos y ademas cubre mas superficie.

**Correccion: los minutos son telemetria, no criterio de aprobacion.** Un ahorro en minutos estimado por el propio revisor es justo el tipo de medida que la ley de Goodhart corrompe. Percibir que se va mas rapido y ir mas rapido no son la misma cosa, y aqui quien estima es la misma persona que se beneficia de la estimacion.

Por tanto los minutos se registran como referencia, y la aprobacion se decide con metricas que ya existen en el trabajo real y que nadie fabrico para esta ocasion:

- divergencias detectadas antes de cerrar una unidad;
- falsos positivos que la revision deja de tener que descartar;
- avisos de auditoria que quedan sin resolver al cerrar;
- deuda de revision pendiente al final de cada unidad.

Y una prueba que no necesita numero: si se retirase la pieza, ¿se volveria al metodo anterior sin notarlo? Si la respuesta es que si, no estaba aportando.

### Regla transversal a todas las fases: exposicion de la fuente

La materia prima de este sistema son paginas literales de un libro con derechos de una editorial, en su edicion anotada del profesor. Esa materia prima no cruza a terceros por defecto, y la regla que lo impide **no puede vivir en la configuracion de una herramienta**.

- ninguna fase envia texto de la fuente a un servicio de terceros sin decision expresa y registrada para esa fase;
- cuando una tarea se pueda resolver en local con calidad suficiente, se resuelve en local;
- entre piezas comparables, la ejecucion local cuenta como criterio de seleccion, no como extra;
- si una tarea exige un servicio externo, se declara que sale, hacia donde y con que retencion **antes** de la primera llamada.

Ejemplo del nivel equivocado: decidir "no activar el registro de prompts en el gateway" es una precaucion de herramienta, y llega tarde. La decision de proyecto es anterior y mas alta: que parte de la fuente puede cruzar a un tercero, y con que autorizacion.

### Mapa minimo de protocolos por fase

La seguridad de este sistema no debe quedar a memoria de sesion. La pasada actual deja identificado este mapa minimo de protocolos a fijar por fase:

- **Ya, en todo el repositorio sin excepcion:** `P5 · R2, R3, R4` para secretos, permisos minimos y logs.
- **Fase 0 / tarea 2:** `P5 · R1`. Los PDFs que se parsean son datos no confiables; lo extraido se trata como dato, nunca como instruccion.
- **Fase A:** `P12`. Identidad y acceso dejan de ser opcion cuando el sistema tenga varios usuarios reales dentro de SGEL.
- **Fase B:** `P2 · P3 · P6`. Van a la constitution del repositorio nuevo y a sus validaciones duras, no a notas blandas de sesion.
- **Fase C:** `P5 · R1` y `P2`. El gate de fidelidad es tambien validacion adversarial de la extraccion.
- **Fase F:** `P8 · P12`. Scope explicito y ejecuciones auditables.
- **Fase G:** `P10 · checklist · P11`. Paso obligatorio antes de cualquier despliegue con cliente o equipo usando el sistema vivo.

No todo se transfiere tal cual. El criterio de otro contexto de "empezar amplio y recortar" no pasa automaticamente a este sistema, y los checklists pensados para otra superficie con modelo deben rederivarse antes de gobernar extraccion o generacion editorial.

### Fase 0. Evidencia barata

Va antes que A porque no depende del runtime final ni de cerrar toda la arquitectura. Combina auditoria del sistema actual en este repositorio con prototipos minimos en el repositorio nuevo. Si el producto tarda meses o no llega a existir nunca, la parte de auditoria sigue rindiendo igual.

Por eso Fase 0 no pertenece entera a un solo lado: las tareas 1 y 2 se ejecutan y formalizan en el repositorio nuevo; las tareas 3 a 6 auditan el sistema actual y se ejecutan aqui.

1. Cerrar una **linea base operativa** del gate de fidelidad y pasarlo por las diez unidades; **formalizar el resultado en un artefacto versionado del repositorio nuevo**. No es una subida de nivel —la evidencia ya es de nivel 1 por tipo— sino un cambio de estatuto: de evidencia de sesion a evidencia formalizada (§1.2). En esta misma tarea no se da por final la forma del gate: se deja escrita y estable la vara provisional con la que el spike del punto 2 va a comparar los candidatos que preserven mejor la pagina. La linea base incluye tambien una **clasificacion provisional** de divergencia real frente a artefacto de comparacion, suficientemente legible para revision humana —es el requisito 1 de §6.3.1, y su sitio es el gate base, no el banco de pruebas entre parsers—; el spike del punto 2 podra confirmarla, mejorarla o sustituirla.
2. **Spike de parseo y control documental sobre PDFs reales**, con el criterio de exito escrito antes de ejecutarlo. Es el **primer spike tecnico del proyecto** —antes que el runtime y antes que la interfaz— porque despeja la incertidumbre mas barata de una capacidad fundacional. Se ejecuta **en el repositorio nuevo del producto**, usando como muestra de contraste la fuente y el inventario auditados en este repositorio. No empieza hasta declarar como accede ese repo a los PDFs con derechos conforme a §7. Compara los candidatos del §5.1.1 contra la linea base del punto 1. Responde a cuatro preguntas, y solo a esas:
   - si mejora la separacion entre texto del alumno y anotacion del profesor;
   - si conserva mejor el orden de lectura y los bloques de la pagina;
   - si reduce divergencias falsas frente al inventario;
   - si puede ejecutarse sin violar la regla de exposicion de la fuente (§7).

   Ninguno de los candidatos de §5.1.1 llega elegido: llegan como espacio de busqueda, y el resultado de este spike es lo unico que puede cambiarles el nivel.
3. Corregir el contrato de la fuente: declarar que es edicion anotada y anadir la separacion alumno/anotacion (§6.3.1). **Esta tarea se ejecuta en este repositorio**, porque aqui vive hoy la autoridad del contrato de fase 1.
4. Inventario de ataduras a NC1: que exactamente hay que tocar para que el sistema sirva a Companeros 2 (§3.5). **Esta tarea se ejecuta en este repositorio**, porque aqui estan el schema, los registries y la cabecera canonica actual.
5. Auditar que demuestra ya la fase 2 sobre consulta transversal en JSON, antes de disenar pruebas nuevas de persistencia (§6.3.3). **Esta tarea se ejecuta en este repositorio**, porque aqui viven hoy los artefactos y validadores que hay que contrastar.
6. Medir minutos de revision por unidad, como telemetria de referencia y no como criterio de aprobacion (§7). **Esta tarea se ejecuta sobre el trabajo editorial de este repositorio**.

Durante Fase 0, el repositorio nuevo no reescribe el contrato de fase 1: consume la version auditada de este repositorio. Si mas adelante ese contrato migra, la autoridad cambia por decision explicita.

### Fase A. Definicion del producto

- definir exactamente que ve el usuario;
- definir que puede subir o editar;
- definir que salidas recibe;
- definir que estados existen y que significa cerrar una tarea.
- definir que parte del sistema actual ya sirve como prototipo aprovechable.

### Fase B. Constitucion operativa

- fijar que decide la IA;
- fijar que decide el humano;
- fijar que validaciones son obligatorias;
- fijar que nunca se publica sin aprobacion.
- fijar que decisiones quedan abiertas hasta que el prototipo las pruebe.
- fijar la jerarquia de evidencia para no cerrar decisiones por moda o por material secundario.

### Fase C. Extraccion fiable

- corregir el contrato de la fuente real;
- mantener la extraccion multimodal como canal principal provisional;
- anadir el gate de fidelidad fuente -> JSON, con clasificacion de hallazgos y no solo senalizacion (§6.3.1);
- anadir al contrato la separacion entre texto del alumno y anotacion del profesor (§6.3.1);
- registrar errores recurrentes en memoria correctiva.

Nota de secuencia: en Fase 0 se adelantan la correccion del contrato y la definicion experimental del gate por ser baratos y no depender del runtime final. Fase C consolida y formaliza lo que Fase 0 haya probado, no lo descubre.

### Fase D. Persistencia y estructura de conocimiento

- decidir donde vive la informacion extraida para alimentar todo el sistema;
- comparar si el JSON actual basta, si debe convivir con BD, o si debe pasar a otra estructura canonica;
- no cerrar esta decision por preferencia previa sino por utilidad transversal.

### Fase E. Integracion metodologica y editorial

- conectar la base extraida con el marco teorico metodologico;
- integrar las fuentes especificas por dominio;
- modelar como se generan propuesta final, tarjetas, pildoras y otros recursos.

### Fase F. Orquestacion

- modelar tareas, estados, colas y reintentos;
- decidir que pasos son deterministas y cuales son agenticos;
- encapsular cada operacion en una tarea trazable.

Decision apoyada por el analisis ya hecho:

- lo fijo, repetible y predecible debe ir por carril determinista;
- lo variable, interpretativo o editorialmente ambiguo debe ir por carril agentico con revision humana.

Decisiones explicitamente abiertas en esta fase:

- si ese carril agentico se construye con runtime propio, con framework externo o con solucion hibrida;
- si conviene interfaz visual de automatizacion para una parte del sistema;
- si la primera version necesita realmente multiagente o solo tareas encadenadas con gates.

### Fase G. Producto utilizable

- construir una interfaz propia;
- ocultar al usuario la complejidad de prompts, repos y scripts;
- permitir revision humana y cierre desde el propio sistema.

### Fase H. Dashboard y analitica integrada

- decidir el destino del dashboard actual;
- conservar las vistas transversales que de verdad ayudan al trabajo;
- integrar o reemplazar lo que haga falta segun el producto final.

### Fase I. Automatizacion remota selectiva

- mover a ejecucion remota solo lo que ya funcione bien en local;
- usar GitHub Actions o equivalente para informes, revisiones o tareas programadas;
- no usar la automatizacion remota para descubrir el proceso sobre la marcha.

## 8. Decision de arquitectura ya aclarada

La decision ya no es "como trabajar mejor con Claude Code en VS Code".

La decision correcta es esta:

- construir un producto operativo propio;
- usar IA por debajo como motor de tareas;
- mantener revision humana en puntos de control;
- dejar VS Code y Claude Code como herramientas de construccion, no como interfaz final del trabajo.

Y hacerlo con este criterio:

- primero prototipo probado;
- despues consolidacion por fases;
- despues ampliacion a nuevas funciones y a Companeros 2.

## 9. Preguntas de cierre que ahora si corresponden

Dos preguntas previas condicionan a todas las demas y hoy no estan formuladas en el documento:

**0a. Quien es el usuario del producto y que regimen de derechos aplica a los PDFs que entran.** §3.1 habla de "la interfaz real para el usuario" sin definir si ese usuario es el autor interno, SGEL, un docente externo o varios perfiles a la vez. La respuesta condiciona autenticacion, hosting, tenancy y modelo de coste. Y hay una segunda mitad que el documento no menciona ni una vez: la entrada son PDFs de editorial, gitignorados por copyright, que ademas pueden incluir la capa docente con soluciones. Sin regimen de derechos definido no esta claro que el producto pueda existir fuera de uso interno.

**Respondida el 2026-09-05.** El usuario son **varios perfiles dentro de SGEL**; el producto es del autor y **se entrega** a SGEL; y la fuente son libros de la propia editorial que va a operar la herramienta. Eso cierra como bloqueo inmediato la duda de **titularidad y uso interno** —quien aporta el material es quien usa el sistema— pero no cierra por si solo la exposicion a terceros, la retencion ni las condiciones contractuales de los proveedores. Aun asi deja tres consecuencias vivas:

- hay un momento de entrega, asi que nada del sistema puede depender de la maquina del autor ni de como la tiene montada;
- la capa de modelos no puede colgar de una suscripcion personal: quien opera, paga (§4.1);
- varios usuarios en **una sola** organizacion piden identidad y roles, no multi-tenencia. No se construye en la primera version, pero tampoco puede quedar clausurado por como se construya.

Y una precision que la respuesta no cierra: que la editorial aporte el material no autoriza por si solo a que ese material cruce a terceros. Eso lo gobierna la regla de exposicion de la fuente (§7).

**0b. Que pasa con NC1 mientras se construyen las fases A-I.** El documento describe nueve fases y no menciona ni una vez el entregable editorial en curso. Es el riesgo mayor del plan: que la construccion de la plataforma se coma el libro que hay que entregar.

Estado a 2026-09-05: las diez unidades tienen ya capa `final/` —55 archivos mas nueve itinerarios, con U0 como unidad atipica— asi que el corpus ha llegado a meseta y el riesgo es hoy menor que hace un mes. Lo que queda son deudas declaradas (avisos de auditoria sin resolver, registro de repo B sin actualizar, bloques de la presentacion sin aplicar), y todas se pagan en el mismo recurso escaso: horas del autor.

Y despues de esas dos:

1. Cual es la primera interfaz minima del producto: web interna, escritorio o panel local.
2. Cual es el primer flujo end-to-end que debe quedar cerrado dentro del sistema.
3. Cual es la mejor estructura para persistir la informacion extraida, sin asumir todavia que deba ser JSON para siempre.
4. Como se integran formalmente el marco teorico metodologico y las fuentes especificas en la construccion de la propuesta final.
5. Que parte del dashboard actual se conserva, se integra o se reemplaza.
6. Que artefacto exacto entra el usuario y que artefacto exacto sale en esa primera version.
7. Que gates son obligatorios antes de pasar a la siguiente fase.
8. Que partes del sistema actual se conservan como backend y cuales se reemplazan.
9. Que estrategia de proveedores y coste se adopta para la capa de modelos.

## 10. Criterio para convertir este borrador en norma

Este documento solo debe subir de rango cuando ocurra lo siguiente:

1. Se cierre la definicion del producto minimo.
2. Se cierre la constitucion operativa basica.
3. Se ratifique el primer flujo end-to-end.
4. Se actualicen de forma coherente los documentos raiz para reflejar este nuevo marco.

Hasta entonces, este archivo funciona como documento de definicion y reencuadre, no como autoridad final.