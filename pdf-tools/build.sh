#!/usr/bin/env bash
# =============================================================
# Build del PDF Diagnóstico NC1
# Pipeline: MD --(sed preprocesado)--> MD' --(pandoc/xelatex)--> PDF
# Requisitos: pandoc + xelatex (TeXLive/MacTeX o BasicTeX)
# =============================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
MD_SOURCE="$ROOT/docs/diagnostico-nc1-asesores.md"
OUT_DIR="$SCRIPT_DIR/out"
OUT_PDF="$OUT_DIR/diagnostico-nc1-asesores.pdf"
PREAMBLE="$SCRIPT_DIR/preamble.tex"
TMP_MD="$OUT_DIR/_preprocessed.md"

mkdir -p "$OUT_DIR"

if [[ ! -f "$MD_SOURCE" ]]; then
  echo "❌ No existe el MD fuente: $MD_SOURCE" >&2
  exit 1
fi

echo "📄 Fuente: $MD_SOURCE"
echo "🧪 Preprocesando MD…"

# Sed: añade ☐ delante de los códigos de error tipo "- **V-T01 —" o "- **I-Te01 —"
# Después sustituye caracteres unicode que Helvetica Neue no tiene, envolviéndolos en
# \uchar{...} (definido en preamble) para que use Arial Unicode MS.
sed -E 's/^- \*\*([A-Za-z]{1,3}-[A-Za-z]{1,3}[0-9]+) — /- ☐ **\1 — /g' "$MD_SOURCE" \
  | sed -e 's/→/\`\\uchar{→}\`{=latex}/g' \
        -e 's/↔/\`\\uchar{↔}\`{=latex}/g' \
        -e 's/✅/\`\\uchar{✓}\`{=latex}/g' \
        -e 's/❌/\`\\uchar{✗}\`{=latex}/g' \
        -e 's/☐/\`\\uchar{☐}\`{=latex}/g' \
        -e 's/▸/\`\\textbullet{}\`{=latex} /g' \
        -e 's/⚠/\`{\\bfseries\\color{ncnar}\\(\\triangle\\)}\`{=latex} /g' \
  | awk '/^# Diagnóstico/ { print "\\newpage"; print ""; print $0; next } { print }' \
  > "$TMP_MD"

echo "📦 Compilando con pandoc + xelatex…"

pandoc "$TMP_MD" \
  --pdf-engine=xelatex \
  -H "$PREAMBLE" \
  --toc \
  --toc-depth=3 \
  -V documentclass=article \
  -V classoption=titlepage \
  -V colorlinks=false \
  -V lang=es-ES \
  -V title="Diagnóstico de Nuevo Compañeros 1" \
  -V subtitle="Bitácora del asesor pedagógico" \
  -V author="SGEL" \
  -o "$OUT_PDF"

rm -f "$TMP_MD"

if [[ -f "$OUT_PDF" ]]; then
  SIZE=$(ls -lh "$OUT_PDF" | awk '{print $5}')
  PAGES=$(pdfinfo "$OUT_PDF" 2>/dev/null | grep -E '^Pages:' | awk '{print $2}' || echo "?")
  echo "✅ PDF generado: $OUT_PDF ($SIZE · ${PAGES} páginas)"
else
  echo "❌ No se generó el PDF." >&2
  exit 1
fi
