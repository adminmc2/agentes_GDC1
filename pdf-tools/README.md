# pdf-tools — Diagnóstico NC1

Generador de PDF del documento `docs/diagnostico-nc1-asesores.md` para entregar a los asesores pedagógicos como **bitácora de revisión editorial** de *Nuevo Compañeros 1*.

## Stack

Pipeline simple, sin Node.js:

- **Pandoc** (3.x) — convierte el Markdown fuente a LaTeX.
- **xelatex** (BasicTeX o MacTeX) — compila LaTeX → PDF.
- **Bash + sed** — preprocesa el MD para inyectar checkboxes y arreglar Unicode.
- **fuentes del sistema** (Helvetica Neue + Menlo + Arial Unicode MS para símbolos).

## Requisitos previos

```bash
brew install pandoc
brew install --cask basictex   # si no tienes ya MacTeX/TeXLive
```

## Uso

```bash
./build.sh
```

Salida: `pdf-tools/out/diagnostico-nc1-asesores.pdf`.

El build:

1. Lee `docs/diagnostico-nc1-asesores.md` del repo.
2. Preprocesa con `sed`:
   - Añade `☐ ` delante de cada código de error (`V-T01`, `I-Te01`, etc.) para que el asesor pueda marcarlo a mano o en Acrobat Reader.
   - Sustituye caracteres Unicode que Helvetica Neue no cubre (`→`, `↔`, `✅`, `❌`, `☐`, `▸`) por su equivalente en Arial Unicode MS.
3. Llama a `pandoc` con `--pdf-engine=xelatex` y el preamble en `preamble.tex`.
4. Genera el PDF en `out/`.

## Por qué este stack

- **Hifenación nativa española**: xelatex parte palabras correctamente según las reglas del español, sin cortes raros.
- **Tipografía publicación**: kerning, microtipografía y composición de párrafos de calidad LaTeX.
- **TOC automático**: índice con páginas, generado por pandoc.
- **Sin Node.js**: sin `node_modules`, sin transpilación, sin frameworks JS. Solo dos comandos del sistema.
- **MD como fuente única**: el contenido vive en el MD; el PDF se regenera cuando el MD cambia.

## Estructura

```
pdf-tools/
├── README.md
├── .gitignore
├── build.sh           # script de build (sed → pandoc → xelatex)
├── preamble.tex       # estilos LaTeX (colores NC1, fuentes, layout)
└── out/
    └── diagnostico-nc1-asesores.pdf
```

## Filosofía del PDF

- **Bitácora del asesor**: cada error trae un cuadro `☐` para marcar a mano o en Acrobat Reader.
- **Color por sección**: la paleta NC1 está disponible como colores LaTeX (`\color{ncvocab}` salmón, `\color{ncgram}` azul, etc.) para futuras personalizaciones.
- **Anotación canónica**: cada error indica con qué herramienta de Acrobat Reader anotarlo (`Reemplazar texto`, `Resaltar + nota` o `Nota`).
- **MD como fuente única**: el contenido vive en `docs/diagnostico-nc1-asesores.md`. El PDF se regenera al cambiar el MD.

## Solución de problemas

- **`pandoc: command not found`**: `brew install pandoc`.
- **`xelatex: command not found`**: `brew install --cask basictex` y luego reinicia el terminal.
- **`Missing character: There is no <X>`**: hay un símbolo Unicode no cubierto por Helvetica Neue ni Arial Unicode MS. Añade una línea más al `sed` de `build.sh` mapeándolo a `\uchar{X}` o a un equivalente LaTeX.
- **`File <X>.sty not found`**: paquete LaTeX no instalado. Instálalo con `sudo tlmgr install <paquete>`.

## Ubicación provisional

Este pipeline vive en este repo (`guia-didactica-profesor-IA`) por proximidad al MD fuente. Cuando el flujo se estabilice puede moverse a un repo propio o integrarse en el sistema de generación editorial de SGEL.
