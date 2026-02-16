# Changelog — Guía Didáctica del Profesor (IA)
## Sistema de Agentes v5.0 — Nuevo Compañeros 1

---

## [2026-02-16] — Formato de output, formulación de objetivos y fundamentación teórica

### Añadido
- `referencias/formulacion-objetivos.md` — Documento de referencia v2 para formulación de objetivos. Incorpora: 3 tipos de objetivos (comunicativo/lingüístico/gramatical), objetivos de procesamiento del input (VanPatten), regla del "no 2 por 1", correspondencia ACTFL-MCER (A1 ≈ Novice High), modelo SMART completo (5 componentes con temporalización), regla del 40% para número de objetivos, 5 errores frecuentes, matiz de Conti sobre Bloom en lenguas. Fuentes: MCER, PCIC, ACTFL, VanPatten, Canale y Swain, Long, Ellis, Dörnyei, Deci y Ryan, Vygotsky, Marzano, Wiggins y McTighe.
- `unidades/U03-vocabulario-tarjetas.csv` — Archivo CSV independiente (18 palabras, delimitador punto y coma, UTF-8) listo para importar en InDesign mediante data merge.

### Modificado
- `agentes/ag-vocabulario.md` — Eliminadas todas las cajas ASCII (┌─┐│└─┘) del formato de output. Sustituidas por encabezados markdown en negrita. Concepto de "Caja" preservado como instrucción funcional para el profesor (qué material preparar/imprimir). Añadida referencia a `formulacion-objetivos.md` para verbos observables.
- `unidades/U03-familia.md` — Objetivos corregidos según regla del "no 2 por 1": gamificación ahora con un solo verbo Bloom 3 ("Describir su propia familia y la de otros usando frases sencillas con al menos 6 términos de parentesco"), bloque 2 con un solo verbo Bloom 3 ("Producir un texto breve describiendo su propia familia usando las estructuras del texto modelo"). Eliminadas las 9 cajas ASCII. Añadido bloque CSV.

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
