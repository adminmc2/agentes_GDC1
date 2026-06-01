---
description: Carga el contexto mínimo para redactar o revisar una sección de final a partir de una unidad y una sección. Úsalo antes de editar `unidades/U*/final/*.md`.
argument-hint: U[X] [seccion]
arguments:
  - unidad
  - seccion
disable-model-invocation: true
---

# Contexto de redacción para $unidad / $seccion

Objetivo: preparar el contexto de trabajo para redactar o revisar una sección de `final/` sin escribir todavía el texto final.

## Lectura mínima obligatoria

1. Lee el inventario de la unidad:
   - `unidades/$unidad/$unidad-nc1-inventario.json`

2. Si la sesión tiene acceso a repo B y existe el PDF correspondiente, léelo como fuente autoritativa para fichas, píldoras y tarjetas referenciadas:
   - `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X/U0X $seccion.pdf` (donde U0X es la forma de dos dígitos de $unidad)
   - si no existe o no es accesible, dilo explícitamente y sigue con el contexto disponible.

3. Lee la propuesta rica de la sección si existe:
   - `unidades/$unidad/propuesta/$seccion.md`

4. Lee el archivo final de la sección si ya existe:
   - `unidades/$unidad/final/$seccion.md`

5. Relee las autoridades del sistema:
   - `docs/manual-estilo-final.md`
   - `docs/formulacion-objetivos.md`

6. Lee el contexto observacional:
   - `docs/tecnicas-recurrentes.md`

7. Busca precedentes cercanos ya cerrados:
   - primero `U1`
   - luego `U2`
   - solo para la misma sección `$seccion`
   - si no existen, dilo explícitamente.

8. Si la sesión tiene acceso a los MDs antiguos de repo B y existen notas de migración, revísalas y lista qué componentes deben eliminarse o reasignarse:
   - `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X/U0X-$seccion.md`
   - `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X/U0X-$seccion-paginas.md`
   - busca marcadores `⚠ NOTA DE MIGRACIÓN` o equivalentes.
   - si no, dilo explícitamente y sigue con el contexto disponible.

## Qué debes devolver

Devuelve un paquete breve con estos bloques:

### 1. Encargo de la sección
- objetivo operativo
- contenido del libro que articula la sección
- producto o cierre esperado

### 2. Materiales y apoyos
- líneas `Imprimir`
- audios, vídeos, tarjetas o insignias implicadas
- recursos que condicionan la dinámica

### 3. Restricciones activas
- reglas del manual especialmente relevantes para esta sección
- posibles zonas de consulta previa
- si hay una unidad bloqueada cuyo texto solo puede usarse como precedente, indícalo

### 4. Técnicas plausibles
- técnicas observadas en el corpus que aquí sí podrían encajar
- técnicas que aquí no conviene forzar
- recuerda que `docs/tecnicas-recurrentes.md` no impone obligación

### 5. Precedentes útiles
- qué patrón de `U1` o `U2` conviene imitar
- qué patrón no conviene copiar aunque exista

### 6. Riesgos de redacción
- sobreprescripción del docente
- recuento redundante del libro
- técnica innecesaria o demasiado pesada para la sección
- cualquier otra colisión visible entre propuesta, sección y manual

## Límites

- No redactes todavía el archivo final salvo que el usuario lo pida después.
- No propongas reglas nuevas como si ya estuvieran codificadas.
- Si falta una pieza clave del contexto, dilo y detén la preparación ahí.
- **Degradación controlada — si repo B o el PDF no están accesibles, dilo explícitamente y sigue con el contexto disponible; no sustituyas esa ausencia con inferencias desde registros secundarios.**