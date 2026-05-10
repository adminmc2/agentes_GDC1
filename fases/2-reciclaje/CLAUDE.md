# Fase 2 — Reciclaje de contenidos

> Auto-cargado por Claude Code al trabajar dentro de `fases/2-reciclaje/`. Contrato corto de la fase: qué produce, dónde input/output, cómo validar, reglas críticas, navegación.

---

## Qué produce esta fase

Un mapa de hilos de reciclaje (`unidades/nc1-reciclaje.json`) que modela cómo cada contenido del curso (vocabulario, gramática, funciones comunicativas, estrategias) se introduce, amplía, aplica, sistematiza o contrasta a lo largo de las unidades.

El archivo tiene tres niveles de análisis que se generan por separado:

| nivel_analisis | Origen | Generado por |
|---|---|---|
| `mapa` | `nc1-curso.json` (índice editorial del curso) | Script `regenerar_reciclaje_mapa.py` |
| `auto` | Inventarios `UX-nc1-inventario.json` (vocabulario_consolidado) | Script `regenerar_reciclaje_vocabulario.py` |
| `detalle` | Inventarios (actividades individuales) | Fase futura |

## Input y output

- **Input mapa:** `unidades/nc1-curso.json` — índice editorial del curso con vocabulario, gramática, comunicación, etc. por unidad.
- **Input auto:** `unidades/UX/UX-nc1-inventario.json` — inventarios extraídos en fase 1.
- **Output:** `unidades/nc1-reciclaje.json` — único archivo con todos los hilos.

## Cómo se invoca

**Nivel mapa — una sola vez** (o cuando cambia `nc1-curso.json`):
```bash
python3 scripts/regenerar_reciclaje_mapa.py
```
Este script crea `nc1-reciclaje.json` si no existe. Debe ejecutarse antes que el de auto.

**Nivel auto — se ejecuta automáticamente al integrar cada unidad:**

No se invoca manualmente. Lo encadena `scripts/integrar_unidad.py` como parte del flujo de integración: valida el inventario aprobado, lo copia a main, actualiza el reciclaje y hace commit. Las correcciones que el humano haya hecho al inventario se propagan al reciclaje en ese mismo paso.

```bash
# Integrar una unidad (valida + actualiza reciclaje + commit)
python3 scripts/integrar_unidad.py 6
```

## Cómo validar

1. `python3 scripts/regenerar_reciclaje_mapa.py` → sin errores.
2. `python3 diagrama.py` → `http://localhost:8080` → vista RECICLAJE → revisar timeline.

---

## Reglas críticas

1. **Naming obligatorio:** el `titulo` de un hilo es siempre el nombre canónico del contenido tal como aparece en `nc1-curso.json` o en el `campo_semantico` del inventario. Nunca un nombre inventado o genérico.
2. **Un hilo por campo semántico:** si el nivel `auto` genera hilos separados para dos campos (ej. "Países hispanohablantes" y "Nacionalidades"), el nivel `mapa` también los separa. No se agrupan campos distintos en un mismo hilo.
3. **Acciones con criterio:** ver `reglas-reciclaje.md` §2 para la tabla de acciones (introduce/amplia/aplica/sistematiza/contrasta).
4. **Los scripts no inventan:** si un contenido no aparece en la fuente, no se genera hilo. Los scripts solo leen, no interpretan.
5. **No editar `nc1-reciclaje.json` a mano para hilos mapa/auto.** Para cambiar un hilo: editar `nc1-curso.json` (nivel mapa) o el inventario correspondiente (nivel auto) y regenerar con el script.

---

## Para qué consultar qué archivo

| Pregunta | Archivo |
|---|---|
| ¿Cuándo separar o agrupar hilos? ¿Qué nombre usar? | `reglas-reciclaje.md` §1 |
| ¿Qué acción asignar a cada evento? | `reglas-reciclaje.md` §2 |
| ¿Cómo funciona el script de mapa? | `regenerar_reciclaje_mapa.py` + `reglas-reciclaje.md` §3 |
| ¿Cómo funciona el script de auto? | `regenerar_reciclaje_vocabulario.py` + `reglas-reciclaje.md` §4 |
| ¿Qué shape tiene nc1-reciclaje.json? | `../../PROCESO-MAESTRO.md` §B1.5 |