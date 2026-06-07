# Contratos de recursos editoriales

## 1. Propósito y alcance

Este documento regula la **spec textual interna** de los recursos editoriales propios del proyecto que se materializan fuera de los archivos `final/` (tarjetas de estrategia, píldoras formativas y análogos futuros) pero que son **mencionados desde** `final/` y forman parte del contrato pedagógico de cada unidad.

### Qué cubre

- **Tarjeta de estrategia**: principio operativo, antipatrón canónico, modelo de referencia, criterio de nombre.
- **Píldora formativa**: principio operativo, antipatrón canónico, criterio de aceptación.

### Qué NO cubre

- Tipografía, nomenclatura o placement de la mención al recurso en el cuerpo de `final/` — eso vive en `docs/manual-estilo-final.md` §2.1 (*Comunicación — tarjetas de estrategia*) y §6.1 (*Tarjetas*).
- Producción material del recurso (CSVs, fichas imprimibles, registros de píldora).
- Capa `final/` en sí.

### Por qué fuente separada

`docs/manual-estilo-final.md` regula la capa `final/`. Su §1 *Lo que NO redefine este manual* excluye la spec interna de cara A/B de tarjeta y el brief detallado de píldora. Este documento cierra esa frontera con autoridad propia.

---

## 2. Tarjeta de estrategia

### 2.1 Principio operativo

La tarjeta de estrategia **entrega la operación** al estudiante (frame literal con inicios prefijados, huecos a rellenar, pasos accionables que se aplican directamente sobre la tarea). **No enseña a construir** el frame ni describe el proceso de uso desde fuera.

### 2.2 Antipatrón canónico

Cara A formulada como metainstrucción del tipo *"monta el andamio"* / *"crea tu plan en 3 pasos"*. Solapa con el cromático estructura/contenido del proyecto (criterio observacional P3.8) y vacía la función operativa de la tarjeta: el alumno no recibe nada con lo que escribir/hablar/leer, solo instrucciones sobre cómo prepararse.

**Ejemplo de origen.** *USA EL ANDAMIO* (U9 Destrezas) con cara A en tres pasos *MIRA EL MODELO · MONTA TU ANDAMIO · CONECTA CON PALABRAS-PUENTE*: la tarjeta no entregaba ningún frame literal; pedía al alumno construirlo.

### 2.3 Modelo de referencia

Wray & Lewis (1997) — *writing frames*. La tarjeta **ES** el frame: inicios de oración prefijados + conectores + huecos a rellenar con contenido propio. La cara entrega texto operable, no procedimiento.

### 2.4 Criterio de nombre

El nombre debe ser **específico a la destreza o función** que la tarjeta entrena. Las metáforas pedagógicas genéricas reutilizables en cualquier destreza (*ANDAMIO*, *PUENTE*, *MAPA*) no califican como nombre canónico de tarjeta: nombran un mecanismo didáctico transversal, no la operación concreta de esa tarjeta.

---

## 3. Píldora formativa

### 3.1 Principio operativo

La píldora desarrolla una **habilidad nuclear A1 transferible** que el alumno podrá aplicar sobre cualquier material futuro de su mismo tipo (cualquier audio nuevo, cualquier texto nuevo). **No es tarea de aula sobre el material concreto** del libro o del ejercicio que la dispara.

### 3.2 Antipatrón canónico

Candidata píldora formulada como **mecánica-tarea sobre el material específico**: verificación contra otra fuente del propio ejercicio, conteo de ocurrencias en el audio, clasificación de elementos del texto concreto. Esas formulaciones son cuerpo del rótulo o consigna del ejercicio, no habilidad nuclear transferible.

**Ejemplos de origen.** Entre las 5 candidatas iniciales rechazadas para la píldora 9.3: *Verifica con mapa* (mecánica-tarea sobre el audio de María, no habilidad de oyente); *Hechos y opiniones* (clasificación del contenido específico del audio, no operación de escucha transferible).

### 3.3 Criterio de aceptación

La habilidad descrita en la píldora debe ser **aplicable a un audio o texto distinto** del que la origina. Test rápido: *"¿esta píldora seguiría teniendo sentido si la escuchara/leyera un material completamente distinto?"* Si la respuesta es no, es ejercicio del libro, no píldora.

---

## 4. Relación con `docs/manual-estilo-final.md`

| Pregunta | Autoridad |
|---|---|
| ¿Qué dice el recurso (spec interna, cara A/B, brief)? | Este documento |
| ¿Cómo se nombra el recurso en `final/`? | Manual §2.1, §6.1 |
| ¿Dónde aparece la mención en el cuerpo del docente? | Manual §2.1 |
| ¿Qué tipografía lleva el título del recurso? | Manual §6.1 + §9 |
| ¿Cómo se materializa el recurso (CSV, ficha)? | Fuera de ambos — pautas de producción, no codificadas en `docs/` |

Cuando un caso de `final/` toca ambos planos (mención al recurso desde el cuerpo + spec interna del recurso), manda el manual en lo que toca al cuerpo de `final/`; manda este documento en lo que toca a la spec interna del recurso.

---

## 5. Criterio de actualización

Los patrones nuevos pueden incorporarse por **OK explícito del autor** cuando revelan una **brecha estructural o contractual clara** del recurso, aunque la ocurrencia sea única. La repetición en unidades distintas refuerza la necesidad de codificación pero no es requisito obligatorio.

Cualquier cambio se documenta en la tabla §6.

---

## 6. Cambios y versiones

| Fecha | Cambio |
|---|---|
| 2026-06-07 | Documento inicial. §2 (tarjeta de estrategia) y §3 (píldora formativa) codificadas desde el triage del post-mortem U9D (lotes D1 + D2). Brechas estructurales: tarjeta que enseña a construir el frame en lugar de entregarlo (caso *USA EL ANDAMIO*); píldora como mecánica-tarea sobre el material concreto en lugar de habilidad nuclear A1 transferible (5 candidatas iniciales píldora 9.3). Cross-reference añadido en `manual-estilo-final.md` §1 *Lo que NO redefine este manual*. |
