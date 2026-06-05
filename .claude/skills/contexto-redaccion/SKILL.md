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

2. Si la sesión tiene acceso a repo B, busca el PDF de la sección como fuente autoritativa para fichas, píldoras y tarjetas referenciadas:
   - busca cualquier PDF dentro de `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X/` y sus subcarpetas (donde U0X es la forma de dos dígitos de $unidad — U01, U02, U03, U04…) cuyo nombre contenga `$seccion` en cualquier capitalización.
   - si hay varios candidatos, lista los nombres encontrados antes de elegir.
   - si no hay PDF de la sección, ni en `U0X/` ni en sus subcarpetas, dilo explícitamente y sigue con el contexto disponible. No asumas que la ausencia de PDF implica ausencia de material — la sección puede tener otras fuentes; sigue con los pasos restantes.

3. Lee la propuesta rica de la sección. Mira en tres ubicaciones, en este orden de prioridad:
   - repo A (snapshot publicado): `unidades/$unidad/propuesta/$seccion.md`.
   - si no existe en repo A y la sesión tiene acceso a repo B: `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X-propuesta/U0X-propuesta-$seccion.md` (donde U0X es la forma de dos dígitos de $unidad).
   - si tampoco existe en formato `U0X-propuesta/`, fallback legacy: `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X/U0X-$seccion.md` (layout antiguo, presente en algunas unidades).
   - si ninguna existe o no es accesible, dilo explícitamente.

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

8. Si la sesión tiene acceso a repo B, busca notas de migración en los MDs antiguos. Revisa cruzadamente en este orden de prioridad, deduplicando notas idénticas:
   - propuesta antigua por sección: `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X-propuesta/U0X-propuesta-$seccion.md`.
   - MD de sección legacy: `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X/U0X-$seccion.md`.
   - MD de páginas legacy: `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X/U0X-$seccion-paginas.md`.
   - solo como tercer nivel, MD consolidado de unidad: cualquier otro MD dentro de `~/Desktop/temporal-antiguo-guia-ia/unidades/U0X/` cuyo contenido pueda incluir notas (ejemplos: `U0X-comidas.md` consolidado de U4).
   - en todos los candidatos accesibles, busca marcadores `⚠ NOTA DE MIGRACIÓN` o equivalentes. Deduplica notas que aparezcan literalmente en varios archivos.
   - reporta solo componentes con efecto operativo claro: eliminar, reasignar, mantener.
   - si ninguno existe o ninguno tiene notas, dilo explícitamente y sigue con el contexto disponible.

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