# Convenciones editoriales y casos resueltos

> **Responsabilidad:** convenciones de transcripción del libro al JSON + memoria editorial de casos resueltos en extracciones reales + política de mejora continua del sistema de extracción.
>
> **No contiene:** schema (vive en `schema-inventario.md`) ni reglas estables de clasificación o decisión (viven en `reglas-operativas.md`).
>
> **Nota de mantenimiento:** este archivo mezcla deliberadamente convenciones estables con casebook append-only. Si en el futuro el casebook crece y empieza a competir con las convenciones por visibilidad, se separarán entonces.

---

## 1. Convenciones de transcripción del libro al JSON

### 1.1 Sílaba tónica subrayada hasta U3

El libro indica explícitamente (nota a pie en U0 p.9): *"Para facilitar el aprendizaje de la pronunciación, se subraya la sílaba tónica de las palabras de la sección Vocabulario hasta la unidad 3."*

Esto significa:
- **U0, U1, U2, U3:** las palabras de las actividades de vocabulario aparecen con la sílaba tónica subrayada en el libro (ej: `<u>be</u>`, `bo<u>lí</u>grafo`).
- **U4, U5...U9:** sin subrayado en las actividades.

Cuando aparezca esta marca tipográfica en el libro:
- En `datos.items_libro`, marcar la sílaba subrayada con guiones bajos: `_palabra_`. Ejemplo: `"_be_ bolígrafo"` o `"bo_lí_grafo"`.
- Añadir clave `datos._nota` aclarando: `"Las palabras tienen la sílaba tónica subrayada en el libro (convención hasta U3)."`

> **Nota separada:** en las **tarjetas de vocabulario** (output de fase 3), la sílaba tónica está marcada en TODO el libro, no solo hasta U3. Esa convención aplica a fase 3, no a esta fase.

### 1.2 Patrón "primer ítem resuelto como ejemplo"

Muy frecuente en el libro: en actividades numeradas, el libro da el **primer ítem ya resuelto** como modelo, después comienzan los items numerados que el alumno debe resolver.

Ejemplos en U0:
- Act 3 (relacionar): `banco — h` (dado), después `1. león — k`, etc.
- Act 7 (deletrear): `Colombia: ce–o–ele–o–eme–be–i–a` (dado), después `1. España`...
- Act 8 (escucha y escribe): `1. F-ú-t-b-o-l` (dado), después `2. _____`...

Cuando aparezca este patrón:
- El ítem resuelto va a `datos.ejemplo_libro` (string) — el alumno lo ve resuelto, no lo tiene que hacer.
- Los items numerados restantes van a `datos.items_libro` (lista) — el alumno los resuelve.
- Las soluciones de los items numerados van a `respuestas`.

### 1.3 Textos de lectura

Cuando la actividad es leer un texto largo (carta, descripción, artículo), va en `datos.texto_completo` como un único string que reproduce el texto íntegro, **conservando puntuación, mayúsculas y nombres propios tal cual**.

### 1.4 Diálogos

Cuando hay un diálogo (de video, audio o lectura), va en `datos.dialogo_completo` como lista de strings, una por turno:

```jsonc
"dialogo_completo": [
  "PABLO: Son las once. ¡Por fin el recreo!",
  "GRACIELA: ¡Sí! Julia, ¿[1] _____ hermanos?",
  "JULIA: No, soy hija única ¿y tú?"
]
```

Los huecos van como `[1]`, `[2]`... (números) y la lista de palabras del recuadro va en `datos.palabras_recuadro`.

### 1.5 Sopas de letras y juegos

Sopa de letras:

```jsonc
"datos": {
  "subtipo": "sopa_de_letras",
  "cuadricula": [
    ["P","R","I","M","O","A","G","E","H"],
    ["O","C","B","A","I","L","J","M","Z"],
    ...
  ],
  "objetivo_palabras": 6
}
"respuestas": ["PRIMO", "HIJO", "TÍO", "HERMANO", "ABUELO", "PADRE"]
```

---

## 2. Ejemplos canónicos de `items_libro` por tipo de actividad

> Regla de literalidad obligatoria: ver `reglas-operativas.md` §5.7. Aquí van los ejemplos concretos.

### 2.1 Cloze (completar huecos)

```jsonc
"items_libro": [
  "1. Pablo y Jorge (estudiar) _____ en el mismo colegio.",
  "2. Yo (comer) _____ a las dos y veinte."
]
```

### 2.2 Selección múltiple (mostrar las opciones)

```jsonc
"items_libro": [
  "1. ¿Dónde / Cuál viven tus abuelos? — En Marbella.",
  "2. ¿Cómo / Cuál os llamáis vosotras? — Yo me llamo Rosa y ella, Alicia."
]
```

### 2.3 Cuestionario con opciones

```jsonc
"datos": {
  "preguntas_opciones": [
    {"pregunta": "¿Qué es el cómic?", "opciones": {"a": "Una fotografía", "b": "Una novela", "c": "Una mezcla de dibujo y texto"}}
  ]
}
```

### 2.4 ⚠ Ejemplos INCORRECTOS — lo que NO se hace

❌ Solo poner `respuestas` sin `items_libro` para actividades de cloze:

```jsonc
"respuestas": ["1. Pablo y Jorge estudian en el mismo colegio."]
"datos": {}   // ← MAL: no se ve el enunciado original
```

❌ Inventar el enunciado:

```jsonc
"items_libro": ["1. Conjuga el verbo estudiar para Pablo y Jorge"]   // ← MAL: no es lo que pone el libro
```

---

## 3. Ejemplo canónico de unidad atípica (U0)

> Reglas decisionales sobre cuándo añadir `_nota_unidad_atipica` y cómo mapear secciones inaplicables: ver `reglas-operativas.md` §7. Aquí va el JSON canónico.

```jsonc
"_nota_unidad_atipica": "Punto de partida (U0) es introductoria pre-A1.1. No sigue la estructura canónica de 5 secciones. Su contenido (países, abecedario, ortografía, números, saludos, instrucciones de aula) se mapea íntegramente a la sección 'vocabulario' por ser principalmente léxico."
```

---

## 4. Casebook — casos resueltos en extracciones reales

### 4.1 Errores detectados y corregidos

**"Para aprender" confundido con cuadro gramatical.** En extracción real de una unidad, la caja "Para aprender" de la sección de Gramática (con verbo imperativo dirigido al alumno) fue clasificada inicialmente como `cuadros` con `tipo_cuadro: gramatical`. **Era incorrecto en ese caso** porque tenía tarea: se reclasificó como actividad. La regla bifurca por naturaleza (ver `reglas-operativas.md` §4): con verbo imperativo → actividad; solo informativa → cuadro.

### 4.2 Casos resueltos en U3

- **Sopa de letras (p.43 act.5):** cuadrícula 10x9, palabras a buscar como respuestas.
- **Diálogo con video y huecos (p.38 act.1):** `dialogo_completo` con marcadores `[1]`...`[7]`, `palabras_recuadro` con la lista, `respuestas` con `"[1] tienes"`.
- **Programación TV (p.41 act.4):** `programas_tv` + `horarios_digitales` + `respuestas` con relación 1→d, 2→c, etc.
- **Pronunciación con z/c (p.39 act.9):** `items_libro` con `"c/zine"`, `"on c/ze"`, etc.
- **Correo electrónico (p.40 act.1):** `texto_correo` con el correo entero + `afirmaciones_a_corregir` como lista + `respuestas` con la corrección de cada una.
- **Lecturas Javier/Lucía (p.35 acts.6 y 8):** `texto_completo` con el texto íntegro de cada lectura.

---

## 5. Política de mejora continua

Cuando se haga una extracción y aparezca un caso no contemplado en los archivos del sistema:

1. El autor lo señala.
2. Se añade el caso al archivo apropiado:
   - **Schema** (forma del JSON) → `schema-inventario.md` + ajuste en `validar_inventario.py` (regla de no-divergencia).
   - **Decisión / clasificación** → `reglas-operativas.md`.
   - **Convención de transcripción o caso editorial** → este archivo (`convenciones-y-casos.md`), sección 1 o sección 4.
3. La siguiente extracción ya lo cubre sin volver a fallar.

**Estos artefactos son fuente viva.** Cada error documentado mejora el sistema.
