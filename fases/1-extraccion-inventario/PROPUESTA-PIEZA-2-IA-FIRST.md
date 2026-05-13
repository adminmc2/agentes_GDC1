# Propuesta separada — principio IA-first y cierre de pieza 2

> Documento auxiliar de trabajo. No modifica ni sustituye `REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md`.
>
> Propósito: dejar formulada, en limpio y fuera del documento principal, una versión coherente de tres cosas:
> 1. un principio rector explícito para el sistema,
> 2. un reparto estable entre decisiones de IA y verificaciones de código,
> 3. una propuesta de cierre de la pieza 2 (registry verbal) alineada con una lógica IA-first.

---

## 1. Principio rector

**Principio rector propuesto:** el sistema es **IA-first con validación determinista**, no script-first con parches de IA.

Esto significa:

- La **IA** decide cuando el trabajo exige interpretación editorial, lectura contextual, clasificación lingüística, resolución de ambigüedad o cierre de canon.
- El **código** verifica estructura, consistencia, trazabilidad, formato y derivaciones repetibles una vez que la decisión editorial ya está tomada.
- El **humano** aprueba cierres, excepciones y cambios de contrato.

### Consecuencia práctica

No conviene empujar este repo hacia un modelo de scripts cerrados que “infieran” semántica como si fuera dato duro. En este proyecto, eso produciría rigidez falsa y deuda conceptual. Lo eficaz es:

- IA para extraer, interpretar, clasificar y proponer cierres.
- Scripts para validar, comparar, detectar contradicciones y regenerar vistas derivadas.
- Revisión final del autor o del revisor para cerrar cada pieza.

### Fórmula operativa resumida

**La IA decide. El código comprueba. El humano cierra.**

---

## 2. Reparto estable — IA vs código

La separación útil no es por herramienta, sino por tipo de trabajo.

| Capa | Decide IA | Verifica código |
|---|---|---|
| Extracción desde PDF | Sí | No |
| Identificación de contenido lingüístico real de una actividad | Sí | No |
| Clasificación verbal / gramatical / ortográfica / léxica | Sí | No |
| Cierre de canon y naming | Sí | No |
| Resolución de excepciones y fusiones | Sí | No |
| Validación de shape JSON | No | Sí |
| Validación de enums cerrados | No | Sí |
| Detección de claves ausentes o tipos inválidos | No | Sí |
| Trazabilidad mínima obligatoria | IA la declara; código la exige | Sí |
| Agregación derivada top-level | No decide | Sí, desde datos ya cerrados |
| Comparación cross-unidad | IA interpreta; código calcula | Sí |
| Etiquetas pedagógicas transversales (`introduce`, `amplía`, etc.) | Sí, si se generan | Sí, si se validan después |

### Regla de diseño

Un script puede verificar si una decisión editorial es coherente con el contrato. No debe fingir que puede tomarla solo.

### Regla complementaria

Si una categoría o lectura exige justificar por qué un caso entra o no entra, esa capa sigue siendo IA, aunque luego el resultado se congele en un enum o en un JSON.

---

## 3. Propuesta de cierre de pieza 2

### 3.1 Tesis

La pieza 2 puede cerrarse de forma coherente con una lógica IA-first si se formula así:

- **Fase 1 posee el contenido verbal observable y enseñado por el libro.**
- **Fase 2 posee la lectura analítica transversal de ese contenido.**

La clave no es expulsar tiempos y perífrasis de fase 1. La clave es no mezclar en fase 1 el **dato verbal observable** con la **interpretación didáctica profunda** que todavía requiere lectura transversal.

### 3.2 Qué entra en fase 1

Sí entra en fase 1 todo lo siguiente, siempre que esté respaldado por índice, cuadro, actividad o evidencia explícita del inventario:

- lema verbal,
- formas trabajadas,
- tiempo verbal nombrado o claramente trabajado,
- modo, si el libro lo presenta como tal,
- rasgo morfológico por tiempo,
- marca de reflexividad,
- perífrasis verbal, si el libro la trabaja como contenido y no solo como frase incidental,
- fuentes exactas donde ese contenido aparece.

### 3.3 Qué no debe entrar en fase 1 como cierre duro

No debe entrar en fase 1, como dato cerrado del registry, lo que ya depende de interpretación transversal o taxonomía analítica no explícita en el libro:

- `introduce / amplía / aplica / sistematiza / contrasta`,
- redes de progresión cross-unidad,
- relaciones entre verbos o familias verbales a escala de curso,
- usos del tiempo inferidos por el sistema si no están pedagógicamente explicitados,
- cierres de lista de perífrasis no demostrados aún por extracción exhaustiva.

### 3.4 Forma propuesta del registry verbal

```jsonc
"verbos-canonicos.json": {
  "verbos": {
    "hacer": {
      "reflexivo": false,
      "rasgo_por_tiempo": {
        "Presente": "irregularidad 1.ª persona",
        "Pretérito indefinido": "raíz irregular",
        "Imperativo": "irregular"
      },
      "apariciones": [
        { "unidad": "U6", "codigo": "PRE", "fuente": { "pagina": 64, "actividad_id": "U6-p64-act02" } },
        { "unidad": "U6", "codigo": "IMP", "fuente": { "pagina": 65, "cuadro_id": "U6-p65-cuadro01" } }
      ]
    }
  },
  "tiempos_verbales": ["Presente", "Pretérito indefinido", "Imperativo"],
  "perifrasis": [],
  "nota": "La lista de perífrasis se cierra tras extracción exhaustiva E1.5."
}
```

### 3.5 Regla de shape

- Cada **lema** vive una sola vez.
- `rasgo_por_tiempo` clasifica la **morfología por tiempo**, no el comportamiento gramatical completo del verbo.
- `reflexivo` es una marca ortogonal, no una clase morfológica.
- `apariciones` no es una agregación vaga por unidad: debe ser trazable a fuente concreta.

### 3.6 Enum cerrado de tiempos verbales en NC1

Los tiempos que hoy sí pueden cerrarse con base suficiente en NC1 son:

```text
Presente
Pretérito indefinido
Imperativo
```

`Infinitivo` y `Participio` no entran como tiempos verbales del enum.

### 3.7 Perífrasis — criterio de cierre

Las perífrasis pueden pertenecer a fase 1, pero no conviene cerrarlas todavía como lista definitiva solo por ocurrencia superficial.

Propuesta:

- El registry verbal **reserva** el bloque `perifrasis`.
- La **lista exacta** se cierra solo tras extracción exhaustiva E1.5.
- Mientras tanto, se admiten como **candidatas** las combinaciones que parezcan realmente trabajadas por el libro.

Formulación prudente:

```text
Bloque `perifrasis` previsto en el diseño.
La lista exacta no se declara cerrada hasta la extracción exhaustiva de U0-U9.
```

Esto evita inflar el cierre con expresiones incidentales o lenguaje de aula que no equivalen todavía a contenido canónico enseñado.

### 3.8 Usos del tiempo — reformulación coherente con IA-first

Aquí está el punto crítico.

Si se quiere que “los tiempos se trabajan aquí”, la formulación coherente no es meter una taxonomía analítica externa como dato duro del registry. La formulación coherente es esta:

- **Fase 1 puede capturar usos del tiempo solo cuando el libro los trabaja de forma explícita y trazable.**
- **Fase 2 interpreta, agrupa y proyecta esos usos a escala de curso.**

Por tanto, la versión prudente de este bloque no es un `usos_por_tiempo` cerrado con taxonomía RAE filtrada por el sistema, sino algo así:

```jsonc
"usos_observables": {
  "Presente": [
    {
      "etiqueta": "describir cómo es una persona",
      "unidad": "U1",
      "fuente": { "pagina": 13, "cuadro_id": "U1-p13-cuadro01" }
    }
  ]
}
```

Y aun así, solo si esa formulación sale del libro o de su aparato pedagógico de manera explícita.

Si no sale explícitamente, no entra en fase 1 como dato del registry; se queda para análisis de fase 2.

### 3.9 Categorías morfológicas por tiempo

Estas sí encajan bien en fase 1 porque describen rasgos del paradigma trabajado, no una lectura transversal del curso.

#### Presente

```text
regular -ar
regular -er
regular -ir
irregularidad vocálica e→ie
irregularidad vocálica o→ue
irregularidad vocálica e→i
irregularidad 1.ª persona
totalmente irregular
```

`tipo gustar` no debería vivir aquí como categoría morfológica general si lo que se quiere es mantener limpio el eje morfológico. Su comportamiento construccional pertenece al carril gramatical.

#### Pretérito indefinido

```text
regular
raíz irregular
totalmente irregular
ortográfico
```

#### Imperativo (tú)

```text
regular 2.ª persona singular
irregular
```

### 3.10 Doble dimensión verbal + gramatical

La doble dimensión debe formularse como regla controlada, no como expansión ilimitada.

Propuesta de regla:

> Un verbo entra en doble dimensión cuando el libro trabaja simultáneamente:
> 1. el lema o paradigma verbal,
> 2. y una construcción, oposición o función verbal específica tratada como contenido gramatical.

Eso cubre con claridad:

- `ser`, `estar`,
- `gustar`, `doler`,
- `haber` solo como `hay` mientras no se enseñe su paradigma,
- cualquier otro verbo que E1.5 confirme bajo ese mismo criterio.

Esto evita una inflación automática del tipo “todo verbo importante entra en ambos registries”.

### 3.11 Política de ingreso — exhaustiva, pero auditable

La decisión exhaustiva es correcta, pero solo si la trazabilidad es fuerte.

Propuesta:

- Se recorre el total de actividades y cuadros de U0-U9.
- Cada verbo extraído debe quedar ligado a una o más fuentes concretas.
- La matriz de cobertura verbal no se limita a “unidad + código”, sino a:
  - unidad,
  - página,
  - actividad o cuadro,
  - tiempo o perífrasis detectada,
  - motivo de inclusión.

Sin esa capa, el cierre “exhaustivo” sería demasiado opaco para revisión seria.

### 3.12 Límite fase 1 / fase 2 — versión coherente con tu decisión

| Capa | Fase |
|---|---|
| lema verbal | Fase 1 |
| formas trabajadas | Fase 1 |
| tiempo nombrado o explícitamente trabajado | Fase 1 |
| rasgo morfológico por tiempo | Fase 1 |
| reflexivo | Fase 1 |
| perífrasis confirmada por extracción exhaustiva | Fase 1 |
| uso verbal explícitamente enseñado y trazable | Fase 1 |
| lectura analítica del uso no explícito | Fase 2 |
| `introduce / amplía / aplica / sistematiza / contrasta` | Fase 2 |
| progresión cross-unidad | Fase 2 |
| redes y relaciones verbales | Fase 2 |
| visualización analítica en dashboard | Fase 2 |

### 3.13 Redacción de cierre propuesta

La redacción de cierre que sí considero defendible sería esta:

> **Pieza 2 — diseño del registry verbal**
>
> Se cierra el shape del registry verbal como artefacto IA-first con validación determinista posterior. El registry recoge el contenido verbal observable y enseñado por el libro: lema, formas trabajadas, tiempo verbal, rasgo morfológico por tiempo, reflexividad, fuentes exactas y, cuando proceda, perífrasis o usos verbales explícitamente enseñados.
>
> La interpretación transversal del curso no pertenece a este cierre. Las etiquetas pedagógicas (`introduce`, `amplía`, `aplica`, `sistematiza`, `contrasta`), la progresión cross-unidad y las relaciones entre verbos se reservan para fase 2.
>
> El bloque `perifrasis` queda previsto en el diseño, pero su lista exacta se cerrará solo tras la extracción exhaustiva E1.5. Los usos verbales solo entran en fase 1 cuando el libro los enseña de forma explícita y trazable; en caso contrario, su lectura pertenece a fase 2.

### 3.14 Estado recomendado

Dictamen propuesto:

- **Shape del registry verbal:** cerrable.
- **Enums de tiempos verbales:** cerrables.
- **Categorías morfológicas por tiempo:** cerrables con limpieza del eje morfológico.
- **Perífrasis:** no cerrables todavía como lista exacta.
- **Usos del tiempo:** cerrables solo como usos explícitos del libro; no como taxonomía interpretativa general.
- **Materialización del registry:** pendiente de extracción exhaustiva E1.5.

---

## 4. Siguiente uso recomendado

Este documento puede usarse de tres maneras:

1. Como borrador para renegociar la redacción de la pieza 2 sin tocar todavía el documento principal.
2. Como anexo de dictamen del revisor antes de modificar `REDISEÑO-CONTENIDOS-LINGUISTICOS-EN-CURSO.md`.
3. Como base para escribir una futura §15 reescrita, si el autor decide mover la frontera de fase 1 en sentido IA-first.