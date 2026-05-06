# Setup del worktree para el refactor de fase 1

> **Para qué sirve este documento:** explicarte cómo está montado el trabajo del refactor en este momento, para que cuando vuelvas no tengas que reconstruir el contexto. Lectura una vez: 5 minutos.

---

## TL;DR — qué hay ahora en tu Desktop

Tienes **dos carpetas hermanas** en `/Users/armandocruz/Desktop/`:

```
Desktop/
├── guia-didactica-profesor-IA/   ← directorio "original", checked out a main
└── guia-didactica-refactor/      ← directorio "del refactor", checked out a refactor/prompt-fase-1
```

Las dos comparten el **mismo repositorio git** por debajo. No es una copia. No es un fork. Es un **git worktree**: un mecanismo de git que permite tener varias ramas checked out a la vez en directorios distintos, sobre la misma base de datos `.git`.

---

## Por qué se hizo así (decidido 2026-05-06 16:30)

El refactor documental de fase 1 (paso A4 en `REVIEW.md`) requiere editar muchos archivos en cadena. Antes del worktree, el directorio original ya tenía:

- Carpeta `unidades/U2/` sin trackear (otro carril de trabajo, no del refactor).
- Carpeta `viejo/_template/` sin trackear (scaffold).

Ese ruido convivía con la rama del refactor cuando estaba checked out allí. Para evitar contaminación accidental durante los próximos commits del refactor (A4.1 → A4.6), se ha movido la rama a su propio directorio aislado.

**Propiedad clave de los worktrees:** un `git worktree add` crea un checkout fresco. **Los archivos sin trackear del checkout original NO se copian al nuevo worktree.** Por eso `guia-didactica-refactor/` no tiene `U2/` ni `_template/`. Verificado al crearlo.

Esto está alineado con la guía de Anthropic sobre Claude Code: usar worktrees como mecanismo de aislamiento cuando el árbol principal acumula ruido.

---

## Cuándo usar cada directorio

| Si quieres… | Usa este directorio |
|---|---|
| Inspeccionar el estado de `main` | `guia-didactica-profesor-IA/` |
| Ver el dashboard como está en producción | `guia-didactica-profesor-IA/` (Railway despliega de `main`) |
| Trabajar en el refactor de fase 1 (todo A4.1-A4.6) | `guia-didactica-refactor/` |
| Hacer cualquier otro trabajo que NO sea el refactor | `guia-didactica-profesor-IA/` |

**Regla simple:** el refactor vive en `guia-didactica-refactor/`. Todo lo demás vive en `guia-didactica-profesor-IA/`.

---

## Cómo verificar dónde estás

En cualquier terminal:

```bash
pwd
git branch --show-current
```

- En `guia-didactica-profesor-IA/` debe mostrar `main`.
- En `guia-didactica-refactor/` debe mostrar `refactor/prompt-fase-1`.

Para ver ambos worktrees a la vez desde cualquiera de los dos:

```bash
git worktree list
```

Salida esperada:

```
/Users/armandocruz/Desktop/guia-didactica-profesor-IA  cc1f18b [main]
/Users/armandocruz/Desktop/guia-didactica-refactor     <SHA> [refactor/prompt-fase-1]
```

(El SHA del segundo cambia con cada commit del refactor. El de `main` se queda fijo en `cc1f18b` hasta que se mergee A4.6.)

---

## Cómo se cierra esto al final del refactor (A4.6)

Cuando A4.5 (prueba empírica) y A4.5.5 (cross-check schema↔validador) pasen sus gates, llega el merge:

1. **Merge de la rama a main**, desde el directorio original:
   ```bash
   cd /Users/armandocruz/Desktop/guia-didactica-profesor-IA
   git checkout main
   git merge refactor/prompt-fase-1
   git push origin main
   ```

2. **Eliminar el worktree** (ya cumplió su función):
   ```bash
   git worktree remove /Users/armandocruz/Desktop/guia-didactica-refactor
   ```
   Esto borra el directorio físico `guia-didactica-refactor/`. La rama `refactor/prompt-fase-1` sigue existiendo en git por si quieres conservarla; opcionalmente:
   ```bash
   git branch -d refactor/prompt-fase-1
   git push origin --delete refactor/prompt-fase-1
   ```

3. **Conservar el tag de baseline** (no se borra):
   ```bash
   git tag --list | grep pre-refactor
   ```
   El tag `pre-refactor-prompt-fase1` apunta a `cc1f18b` y queda como punto de retorno permanente por si alguien quiere ver el estado pre-refactor.

---

## Cómo se aborta esto si decides no mergear

Si por lo que sea el refactor no llega al merge:

```bash
cd /Users/armandocruz/Desktop/guia-didactica-profesor-IA
git worktree remove /Users/armandocruz/Desktop/guia-didactica-refactor --force
git branch -D refactor/prompt-fase-1
git push origin --delete refactor/prompt-fase-1
git tag -d pre-refactor-prompt-fase1   # opcional
git push origin --delete pre-refactor-prompt-fase1   # opcional
```

`main` no se ha tocado en ningún momento, así que el repo vuelve a su estado anterior sin gymnasia adicional.

---

## Comandos de referencia rápida

```bash
# Listar worktrees
git worktree list

# Cambiar entre directorios (tu shell, no git)
cd /Users/armandocruz/Desktop/guia-didactica-profesor-IA
cd /Users/armandocruz/Desktop/guia-didactica-refactor

# Ver qué rama tiene el directorio actual
git branch --show-current

# Ver el SHA del HEAD actual
git rev-parse HEAD

# Comparar main vs rama del refactor sin moverte (desde cualquiera)
git log --oneline main..refactor/prompt-fase-1

# Ver el tag de baseline
git rev-parse pre-refactor-prompt-fase1
```

---

## Resumen de un vistazo

- **Dos directorios físicos.** Una `.git` compartida.
- **Refactor en `guia-didactica-refactor/`.** Resto en `guia-didactica-profesor-IA/`.
- **Si dudas dónde estás, `pwd` + `git branch --show-current`.**
- **Cierre del refactor:** merge desde el directorio original, luego `git worktree remove`.
- **Si abortas:** `git worktree remove --force` + borrar rama. `main` está intacto en `cc1f18b`.

Documentado por Claude Code el 2026-05-06 16:30 al ejecutar la migración a worktree (commit posterior bumpeará la versión a v10.44).