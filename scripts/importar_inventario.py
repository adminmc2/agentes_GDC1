#!/usr/bin/env python3
"""
Importa un inventario JSON de unidad a Neon PostgreSQL.

Uso:
    python scripts/importar_inventario.py unidades/U03/inventario.json

Idempotente: si la unidad ya existe, la borra (CASCADE) y la reimporta.
Diseñado para funcionar con cualquier unidad (U01-U09).
"""

import json
import os
import sys

import psycopg2
from psycopg2.extras import Json

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "",
)


def extraer_texto_completo(act):
    """Extrae texto largo de la actividad según el campo disponible."""
    if "texto_completo" in act:
        return act["texto_completo"]
    if "dialogo_completo" in act:
        return "\n".join(act["dialogo_completo"])
    if "texto_correo" in act:
        tc = act["texto_correo"]
        return f"De: {tc.get('de', '')}\nPara: {tc.get('para', '')}\n\n{tc.get('texto', '')}"
    return None


def extraer_respuestas(act):
    """Extrae respuestas de la actividad, manejando distintos formatos."""
    if "respuestas" in act:
        return act["respuestas"]
    if "preguntas_opciones" in act:
        return [
            f"{po['pregunta']} → {po['respuesta']}"
            for po in act["preguntas_opciones"]
        ]
    return []


def importar(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    numero_unidad = data["unidad"]
    titulo = data["titulo"]
    paginas_rango = data["paginas"]
    nivel = data.get("nivel", "A1.1")

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    try:
        # --- Borrar unidad existente (CASCADE borra paginas, actividades, etc.) ---
        cur.execute("DELETE FROM unidades WHERE numero = %s", (numero_unidad,))
        borrado = cur.rowcount

        # --- Insertar unidad ---
        cur.execute(
            """INSERT INTO unidades (numero, titulo, paginas, nivel)
               VALUES (%s, %s, %s, %s) RETURNING id""",
            (numero_unidad, titulo, paginas_rango, nivel),
        )
        unidad_id = cur.fetchone()[0]

        contadores = {
            "paginas": 0,
            "actividades": 0,
            "respuestas": 0,
            "cuadros": 0,
        }

        # --- Procesar cada página ---
        for pag in data["paginas_detalle"]:
            cur.execute(
                """INSERT INTO paginas (unidad_id, numero, seccion)
                   VALUES (%s, %s, %s) RETURNING id""",
                (unidad_id, pag["pagina"], pag["seccion"]),
            )
            pagina_id = cur.fetchone()[0]
            contadores["paginas"] += 1

            # --- Cuadros gramaticales ---
            for cuadro in pag.get("cuadros_gramaticales", []):
                titulo_cuadro = cuadro.get("titulo", cuadro.get("subtitulo", ""))
                contenido = {k: v for k, v in cuadro.items() if k != "titulo"}
                cur.execute(
                    """INSERT INTO cuadros_gramaticales (pagina_id, titulo, contenido)
                       VALUES (%s, %s, %s)""",
                    (pagina_id, titulo_cuadro, Json(contenido)),
                )
                contadores["cuadros"] += 1

            # --- Actividades ---
            for act in pag.get("actividades", []):
                texto_completo = extraer_texto_completo(act)

                cur.execute(
                    """INSERT INTO actividades
                       (pagina_id, codigo, numero, tipo, instruccion,
                        contenido_linguistico, destreza, tiene_audio, pista_audio,
                        tiene_imagen, descripcion_imagen, descripcion,
                        ejemplo_libro, texto_completo)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                       RETURNING id""",
                    (
                        pagina_id,
                        act["id"],
                        act["numero"],
                        act["tipo"],
                        act.get("instruccion_original"),
                        Json(act.get("contenido_linguistico", [])),
                        act.get("destreza"),
                        act.get("tiene_audio", False),
                        act.get("pista_audio"),
                        act.get("tiene_imagen", False),
                        act.get("descripcion_imagen"),
                        act.get("descripcion"),
                        act.get("ejemplo_libro"),
                        texto_completo,
                    ),
                )
                actividad_id = cur.fetchone()[0]
                contadores["actividades"] += 1

                # --- Respuestas ---
                respuestas = extraer_respuestas(act)
                for i, resp in enumerate(respuestas):
                    if isinstance(resp, dict):
                        texto_resp = json.dumps(resp, ensure_ascii=False)
                    else:
                        texto_resp = str(resp)

                    cur.execute(
                        """INSERT INTO respuestas (actividad_id, orden, texto)
                           VALUES (%s, %s, %s)""",
                        (actividad_id, i + 1, texto_resp),
                    )
                    contadores["respuestas"] += 1

        conn.commit()

        accion = "reimportada" if borrado else "importada"
        print(f"✓ Unidad {numero_unidad} ({titulo}) {accion}:")
        print(f"  {contadores['paginas']} páginas")
        print(f"  {contadores['actividades']} actividades")
        print(f"  {contadores['respuestas']} respuestas")
        print(f"  {contadores['cuadros']} cuadros gramaticales")

    except Exception as e:
        conn.rollback()
        print(f"✗ Error importando unidad {numero_unidad}: {e}", file=sys.stderr)
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python scripts/importar_inventario.py <inventario.json>")
        sys.exit(1)
    importar(sys.argv[1])
