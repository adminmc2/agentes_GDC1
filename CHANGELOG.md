# Changelog — Guía Didáctica del Profesor (IA)
## Sistema de Agentes v5.0 — Nuevo Compañeros 1

---

## [2026-02-20] — Píldoras Formativas, mejoras estructurales de agentes y reescritura U03

### Modificado — Agentes (mejoras estructurales derivadas de la revisión de U03)
- `agentes/ag-vocabulario.md` — §9 ampliada con transiciones anticipatorias entre fases (CLT: carga extrínseca). Regla de posición de píldora formativa añadida al template: ANTES de la fase que la necesita (VanPatten). Añadidas §10 (Nivel de detalle y confianza en el profesor), §11 (Integración de estación de servicio en fases, MCER aprender a aprender), §12 (Dinámicas de gestión de aula: banco de 7 dinámicas para práctica oral, solo en F2b y práctica libre).
- `agentes/ag-gramatica.md` — Template de output actualizado: eliminadas cajas ASCII, píldora reposicionada ANTES de la fase, doble título (técnico + funcional). Añadidas §7-§11 (versiones comprimidas de §9-§12 de ag-vocabulario.md con referencia cruzada).

### Modificado — Píldoras Formativas
- `agentes/ag-vocabulario.md` — Sección "Notas Lingüísticas" reescrita completamente como "Píldoras Formativas". Añadido banco de acciones con 6 categorías y ~40 acciones concretas. Lógica de selección con 4 variables contextuales.
- `agentes/ag-gramatica.md` — Sección "Notas Lingüísticas" renombrada a "Píldoras Formativas". Referencia al banco de acciones compartido en ag-vocabulario.md.
- `unidades/U03-familia.md` — 4 "NOTA LINGÜÍSTICA" renombradas a "PÍLDORA FORMATIVA". Encabezado §2 actualizado.
- `unidades/U01-U09` — Encabezado §2 "Notas lingüísticas para el profesor" → "Píldoras formativas para el profesor" en todos los templates.

### Modificado — U03 Familia (Bloque 1 Vocabulario)
- `datos/U03-inventario.json` — Reescritura completa contra imágenes del libro del profesor: añadido campo `respuestas` a todas las actividades, pistas de audio 31-42, corrección p.38 (4 personajes + vídeo), corrección p.36 act.1 tipo y act.2 nueva, p.37 act.5 ampliada a 9 ítems, recuadros naranjas como campos separados.
- `unidades/U03-familia.md` — Fases 4, 5 y 6 reescritas según propuesta del autor: Fase 4 simplificada (escucha activa + transición tarjetas), Fase 5 con píldora proyectada ANTES + alumnos preguntan con libros cerrados + tarjetas como comprobación autónoma, Fase 6 con instrucción marco + 4 dinámicas opcionales (palmada, doble palmada, sí/no, L1→L2).

---

## [2026-02-16] — Revisión completa, JSON actualizado y "escucha y repite"

### Modificado
- `datos/U03-inventario.json` — Actualizado Vocabulario (p.34-35) para nueva edición del libro: act. 2 cambia de "relaciona" a "forma frases"; act. 5 texto modelo corregido (Ana tiene 6 años, no 8); act. 6 texto de Javier actualizado (Getafe = ciudad, no pueblo; añadida edad Alejandra y fútbol); acts. 7-10 reorganizadas (7 = completa frases sobre Javier, 8 = texto de Lucía Alonso de Cantabria en lugar de Leonora arahuaca de Colombia, 9 = preguntas sobre Lucía, 10 = síntesis comparativa Javier/Lucía con 6 frases); reducido de 11 a 10 actividades.
- `unidades/U03-familia.md` — Fase 2 reescrita: "escucha y repite" es ahora el eje central de la fase, como pide la actividad 1 del libro. Secuencia: (1) el profesor señala brevemente las 3 generaciones del árbol, (2) primera escucha global del audio, (3) segunda escucha con repetición oral de cada término, (4) refuerzo con el árbol de la pizarra. Antes: la presentación oral del profesor era el eje y el audio era accesorio al final.
- `unidades/U03-familia.md` — Título funcional de Fase 2 actualizado: de "PRESENTE EL VOCABULARIO CON EL ÁRBOL GENEALÓGICO" a "ESCUCHE Y REPITA LOS TÉRMINOS DE PARENTESCO".
- `unidades/U03-familia.md` — Texto corrupto de act. 6 corregido (duplicación "Madrid. La madre, Catalina, estudia..." eliminada).
- `unidades/U03-familia.md` — Etiquetas internas restantes eliminadas: "Weaning off —" en Fase 6, "(F4)" en Reflexión final, "(F5)" en Consolidación distribuida, "F1a del Ciclo de 5 fases: modelling" y "Agente Gramática" en notas lingüísticas. Sustituidas por lenguaje neutro para el profesor.
- `unidades/U03-familia.md` — Frase 2 de act. 10 corregida (punto espurio eliminado).
- `unidades/U03-familia.md` — Fase 3 reescrita completamente: de "Descubra el patrón de género -o/-a" a "Active la conciencia gramatical". Cambios principales: (1) el descubrimiento del patrón -o/-a pasa a la píldora formativa gramatical (inductiva, enfoque VanPatten/Conti) que se proyecta; (2) se introduce el posesivo "su" con la estructura "Su + parentesco se llama ___"; (3) los alumnos clasifican los 11 nombres del árbol en masculinos/femeninos en sus cuadernos ANTES de la escucha, como estrategia de comprensión; (4) el género funciona como herramienta para la Actividad 2, no como conocimiento abstracto. Fase 4 ajustada: eliminada pre-escucha redundante (los alumnos ya tienen los nombres clasificados desde Fase 3), la escucha 1 conecta con las hipótesis previas. Eliminado refuerzo post-corrección (ya innecesario). Nota lingüística simplificada.

---

## [2026-02-16] — Formato de output, formulación de objetivos y fundamentación teórica

### Añadido
- `referencias/formulacion-objetivos.md` — Documento de referencia v2 para formulación de objetivos. Incorpora: 3 tipos de objetivos (comunicativo/lingüístico/gramatical), objetivos de procesamiento del input (VanPatten), regla del "no 2 por 1", correspondencia ACTFL-MCER (A1 ≈ Novice High), modelo SMART completo (5 componentes con temporalización), regla del 40% para número de objetivos, 5 errores frecuentes, matiz de Conti sobre Bloom en lenguas. Fuentes: MCER, PCIC, ACTFL, VanPatten, Canale y Swain, Long, Ellis, Dörnyei, Deci y Ryan, Vygotsky, Marzano, Wiggins y McTighe.
- `unidades/U03-vocabulario-tarjetas.csv` — Archivo CSV independiente (18 palabras, delimitador punto y coma, UTF-8) listo para importar en InDesign mediante data merge.

### Modificado
- `agentes/ag-vocabulario.md` — Eliminadas todas las cajas ASCII (┌─┐│└─┘) del formato de output. Sustituidas por encabezados markdown en negrita. Concepto de "Caja" preservado como instrucción funcional para el profesor (qué material preparar/imprimir). Añadida referencia a `formulacion-objetivos.md` para verbos observables.
- `unidades/U03-familia.md` — Reescritura completa de §3.1 Vocabulario ajustada al contenido real de la nueva versión del libro (p.34-35). 10 actividades en 3 bloques (B1: acts. 1-4, B2: acts. 5-7, B3: acts. 8-10), 13 fases. Nombres del árbol genealógico corregidos (Carmen, Roberto, Carlos, Alicia, María, Nacho, Juana, Luis, Álvaro, Paloma, Pilar). Segundo personaje: Lucía Alonso (Cantabria) en lugar de Leonora (arahuaca, Colombia). Nota intercultural actualizada (contraste urbano/rural en España). Textos del libro transcritos. Objetivos verificados contra `formulacion-objetivos.md` v2. CSV y tabla de tarjetas actualizados.
- `unidades/U03-vocabulario-tarjetas.csv` — Ejemplos actualizados con personajes reales del libro (David, Javier, Lucía, Alicia, Luis, Carmen, etc.).
- `unidades/U03-familia.md` — Objetivo Bloque 1 reformulado a nivel macro: "Reconocer y nombrar los términos de parentesco básicos en español" (eliminada referencia al árbol genealógico como medio de aprendizaje).
- `referencias/formulacion-objetivos.md` — Añadida §7.6: confundir medio de aprendizaje con objetivo + formular a nivel de actividad individual. Regla para agentes: el objetivo describe el resultado macro del bloque.
- `agentes/ag-vocabulario.md` — Añadida instrucción de §7.6 en formato de objetivo de bloque.
- `unidades/U03-familia.md` — Gamificación simplificada: insignia renombrada de "GENEALOGISTA" a "Esa es la familia mía". Eliminado sistema de puntos por bloque. Obtención descrita en términos generales. Eliminados bloques de "Gamificación — Bloque X". Cierre de sección sin recuento de puntos.
- `agentes/ag-vocabulario.md` — Template de gamificación actualizado: nuevo formato (Objetivo + Imprimir + Insignia y obtención general). Eliminado desglose de puntos por bloque. El profesor decide el mecanismo de evaluación.
- `unidades/U03-familia.md` — Gamificación confirmada como UNA por sección: eliminadas 2 referencias a "Reto GENEALOGISTA" en actividades 4 y 9 (sustituidas por "¡Reto!" genérico). Justificación de act. 9 clarificada ("elemento lúdico competitivo", no "gamificación").
- `agentes/ag-vocabulario.md` — Gamificación clarificada como UNA por sección en §6 Decisiones y en template de output. 3 reglas explícitas: (1) una gamificación por sección, (2) obtención general, (3) retos en actividades ≠ gamificación (no llevan nombre de insignia).
- `unidades/U03-familia.md` — Fase 1 reescrita: explotación de foto introductoria (p.34 izquierda) como punto de partida obligatorio. Versión limpia instruccional sin justificaciones teóricas. Preguntas con reciclaje de vocabulario conocido. Modelado inicial de 3 pares señalando la foto.
- `agentes/ag-vocabulario.md` — Añadida §7: Foto introductoria como punto de partida obligatorio (regla general para todas las secciones de vocabulario). Función pedagógica: pre-input simplificado (CLT), activación de conocimientos previos (reciclaje 70/30), modelado F1a de 2-3 pares, conexión personal sin preguntas intrusivas. Restricciones explícitas.
- `agentes/ag-vocabulario.md` — Añadida §8: Separación documento / agente. Regla general: el output para el profesor contiene solo instrucciones operativas; las justificaciones teóricas y anotaciones internas no aparecen en el producto final.
- `unidades/U03-familia.md` — Fase 1: corregido modelado (padre/madre + hijo/hija en lugar de abuelo/a, ajustado a lo visible en la foto). Doble título añadido a TODAS las fases (1-13) + cierre de sección: título técnico (trazabilidad) + TÍTULO FUNCIONAL EN MAYÚSCULAS para el profesor.
- `agentes/ag-vocabulario.md` — Template de fases actualizado con sistema de doble título: (1) Fase N técnica para trazabilidad, (2) TÍTULO FUNCIONAL EN MAYÚSCULAS para el profesor. Nota explicativa con ejemplos.
- `unidades/U03-familia.md` — Secuencialidad entre fases: eliminadas instrucciones redundantes (abrir libro cuando ya está abierto, preparar lo que ya está preparado). Eliminadas etiquetas internas del agente: *F1a — Modelling:*, *F1b — Awareness:*, Segmentación léxica (CLT), Reciclaje 70/30, (worked example obligatorio en A1), (CLT §5.7), "fomenta la metacognición".
- `agentes/ag-vocabulario.md` — §8 ampliada con lista explícita de etiquetas internas prohibidas en el output. Añadida §9: Secuencialidad entre fases (no repetir instrucciones ya ejecutadas).

---

## [2026-02-01] — Generación de U03 Vocabulario

### Añadido
- `unidades/U03-familia.md` §3.1 — Explotación completa de Vocabulario (Parientes, p.34-35) generada por Agente Vocabulario v5.0. 11 actividades en 3 bloques, 14 fases, 4 notas lingüísticas, insignia GENEALOGISTA, reciclaje 70/30 integrado.
- `pruebas/U03-vocabulario-razonamiento.md` — Documento de trazabilidad con las 10 secciones de decisiones del agente.

---

## [2025-02-01] — Sistema de agentes v5.0

### Añadido
- `propuesta-v5-sistema-agentes.md` — Propuesta completa del sistema de 14 agentes (7 de sección + 7 de soporte).
- `agentes/ag-vocabulario.md` — Prompt operativo del Agente Vocabulario.
- Repertorios de explotación por tipo de actividad.

### Modificado
- `unidades/U03-familia.md` — Actualizado de v4.0 a v5.0: eliminada explotación manual, preparado para generación por agentes.

---

## [2025-01-31] — Estructura inicial del proyecto

### Añadido
- `unidades/U03-familia.md` — Creación inicial con contenidos extraídos del índice y contexto secuencial.
- `00-curso-general.md` — Descripción general del curso.
- `marco-teorico-metodologico.md` — Fundamentación teórica (CLT, VanPatten, Bloom, MCER).
