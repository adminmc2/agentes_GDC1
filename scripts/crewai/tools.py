"""
Tools custom para agentes CrewAI — acceso a Neon PostgreSQL.
Todas las tools operan contra la BD (arquitectura BD-first).
"""

import json
import os

import psycopg2
from psycopg2.extras import Json, RealDictCursor
from crewai.tools import BaseTool
from pydantic import Field

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "",
)


def _get_conn():
    return psycopg2.connect(DATABASE_URL)


class ConsultarInventario(BaseTool):
    name: str = "consultar_inventario"
    description: str = (
        "Consulta el inventario completo de una unidad en la BD: "
        "páginas, actividades, respuestas y contenidos del índice. "
        "Parámetro: número de unidad (ej: 3)."
    )

    def _run(self, unidad: int = 0) -> str:
        unidad = int(unidad)
        conn = _get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)

        # Contenidos del índice
        cur.execute(
            "SELECT contenidos_indice FROM unidades WHERE numero = %s",
            (unidad,),
        )
        row = cur.fetchone()
        indice = row["contenidos_indice"] if row else {}

        # Páginas + actividades + respuestas
        cur.execute(
            """
            SELECT
                p.numero AS numero_pagina,
                p.seccion,
                a.numero AS numero_actividad,
                a.tipo,
                a.destreza,
                a.contenido_linguistico,
                a.instruccion,
                a.texto_completo,
                a.ejemplo_libro,
                array_agg(r.texto ORDER BY r.orden)
                    FILTER (WHERE r.id IS NOT NULL) AS respuestas
            FROM paginas p
            JOIN actividades a ON a.pagina_id = p.id
            LEFT JOIN respuestas r ON r.actividad_id = a.id
            WHERE p.unidad_id = (SELECT id FROM unidades WHERE numero = %s)
            GROUP BY p.numero, p.seccion, a.numero,
                     a.tipo, a.destreza, a.contenido_linguistico,
                     a.instruccion, a.texto_completo, a.ejemplo_libro
            ORDER BY p.numero, a.numero
            """,
            (unidad,),
        )
        actividades = [dict(r) for r in cur.fetchall()]

        conn.close()

        resultado = {
            "unidad": unidad,
            "contenidos_indice": indice,
            "total_actividades": len(actividades),
            "actividades": actividades,
        }
        return json.dumps(resultado, ensure_ascii=False, default=str)


class ConsultarTarjetasPrevias(BaseTool):
    name: str = "consultar_tarjetas_previas"
    description: str = (
        "Busca tarjetas de vocabulario de unidades anteriores a la indicada. "
        "Permite detectar palabras reutilizadas. "
        "Parámetro: número de unidad actual (ej: 3)."
    )

    def _run(self, unidad: int = 0) -> str:
        unidad = int(unidad)
        conn = _get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            """
            SELECT palabra, genero, campo_semantico, silaba_tonica,
                   regla, ejemplo, frecuencia, combos,
                   trad_it, trad_fr, trad_pt_br, trad_en,
                   trad_cs, trad_pl, trad_tr,
                   unidad_origen
            FROM tarjetas_vocabulario
            WHERE unidad_origen < %s
            ORDER BY palabra
            """,
            (unidad,),
        )
        tarjetas = [dict(r) for r in cur.fetchall()]
        conn.close()
        return json.dumps(
            {"unidad_actual": unidad, "tarjetas_previas": tarjetas, "total": len(tarjetas)},
            ensure_ascii=False,
            default=str,
        )


class ConsultarCorrecciones(BaseTool):
    name: str = "consultar_correcciones"
    description: str = (
        "Recupera correcciones del editor para el agente recurso_vocabulario. "
        "Estas correcciones son errores de ejecuciones anteriores que NO debes repetir."
    )

    def _run(self, agente: str = "recurso_vocabulario") -> str:
        conn = _get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            """
            SELECT unidad, palabra, campo, valor_original,
                   valor_corregido, tipo_error, fecha
            FROM correcciones
            WHERE agente = %s
            ORDER BY fecha DESC
            LIMIT 50
            """,
            (agente,),
        )
        correcciones = [dict(r) for r in cur.fetchall()]
        conn.close()
        return json.dumps(
            {"correcciones": correcciones, "total": len(correcciones)},
            ensure_ascii=False,
            default=str,
        )


class EscribirTarjetas(BaseTool):
    name: str = "escribir_tarjetas"
    description: str = (
        "Escribe tarjetas de vocabulario validadas en la BD. "
        "Parámetro: JSON string con array de tarjetas. "
        "Cada tarjeta debe tener: palabra, genero, color_genero, silaba_tonica, "
        "regla, campo_semantico, color_campo, ejemplo, frecuencia, irregularidad, "
        "combos (array de 4 strings), trad_it, trad_fr, trad_pt_br, trad_en, "
        "trad_cs, trad_pl, trad_tr, seccion, pagina, nivel_jerarquia, estado, "
        "unidad_origen, unidad."
    )

    def _run(self, tarjetas_json: str = "") -> str:
        if not tarjetas_json:
            return json.dumps({"error": "No se recibieron tarjetas"})
        tarjetas = json.loads(tarjetas_json)
        if not isinstance(tarjetas, list):
            tarjetas = [tarjetas]

        conn = _get_conn()
        cur = conn.cursor()

        insertadas = 0
        for t in tarjetas:
            unidad_num = t.get("unidad", t.get("unidad_origen", 0))
            # Get unidad_id
            cur.execute("SELECT id FROM unidades WHERE numero = %s", (unidad_num,))
            row = cur.fetchone()
            if not row:
                continue
            unidad_id = row[0]

            cur.execute(
                """
                INSERT INTO tarjetas_vocabulario (
                    unidad_id, seccion, pagina, palabra, genero, color_genero,
                    silaba_tonica, regla, campo_semantico, color_campo,
                    ejemplo, frecuencia, irregularidad, combos,
                    trad_it, trad_fr, trad_pt_br, trad_en,
                    trad_cs, trad_pl, trad_tr,
                    nivel_jerarquia, estado, unidad_origen
                ) VALUES (
                    %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s,
                    %s, %s, %s
                )
                ON CONFLICT (palabra, unidad_origen) DO UPDATE SET
                    frecuencia = EXCLUDED.frecuencia,
                    fecha_modificacion = NOW()
                """,
                (
                    unidad_id,
                    t.get("seccion", "vocabulario"),
                    t.get("pagina"),
                    t["palabra"],
                    t.get("genero"),
                    t.get("color_genero"),
                    t.get("silaba_tonica"),
                    t.get("regla"),
                    t.get("campo_semantico"),
                    t.get("color_campo"),
                    t.get("ejemplo"),
                    t.get("frecuencia"),
                    t.get("irregularidad", ""),
                    Json(t.get("combos", [])),
                    t.get("trad_it"),
                    t.get("trad_fr"),
                    t.get("trad_pt_br"),
                    t.get("trad_en"),
                    t.get("trad_cs"),
                    t.get("trad_pl"),
                    t.get("trad_tr"),
                    t.get("nivel_jerarquia", 1),
                    t.get("estado", "nueva"),
                    t.get("unidad_origen", unidad_num),
                ),
            )
            insertadas += 1

        conn.commit()
        conn.close()
        return json.dumps({"insertadas": insertadas, "total_recibidas": len(tarjetas)})


class ExportarCSV(BaseTool):
    name: str = "exportar_csv"
    description: str = (
        "Exporta tarjetas de vocabulario de una unidad a CSV para InDesign Data Merge. "
        "Delimitado por ';'. Solo campos impresos (sin campos de gestión). "
        "Parámetro: número de unidad (ej: 3)."
    )

    def _run(self, unidad: int = 0) -> str:
        unidad = int(unidad)
        conn = _get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            """
            SELECT palabra, genero, color_genero, silaba_tonica, regla,
                   campo_semantico, color_campo, ejemplo, frecuencia,
                   irregularidad, combos,
                   trad_it, trad_fr, trad_pt_br, trad_en,
                   trad_cs, trad_pl, trad_tr
            FROM tarjetas_vocabulario
            WHERE unidad_id = (SELECT id FROM unidades WHERE numero = %s)
            ORDER BY campo_semantico, palabra
            """,
            (unidad,),
        )
        tarjetas = cur.fetchall()
        conn.close()

        if not tarjetas:
            return json.dumps({"error": f"No hay tarjetas para U{unidad:02d}"})

        # Build CSV
        headers = [
            "palabra", "genero", "color_genero", "silaba_tonica", "regla",
            "campo_semantico", "color_campo", "ejemplo", "frecuencia",
            "irregularidad", "combo1", "combo2", "combo3", "combo4",
            "IT", "FR", "PT_BR", "EN", "CS", "PL", "TR",
        ]

        lines = [";".join(headers)]
        for t in tarjetas:
            combos = t["combos"] or []
            while len(combos) < 4:
                combos.append("")
            row = [
                t["palabra"] or "",
                t["genero"] or "",
                t["color_genero"] or "",
                t["silaba_tonica"] or "",
                t["regla"] or "",
                t["campo_semantico"] or "",
                t["color_campo"] or "",
                t["ejemplo"] or "",
                str(t["frecuencia"] or ""),
                t["irregularidad"] or "",
                combos[0], combos[1], combos[2], combos[3],
                t["trad_it"] or "",
                t["trad_fr"] or "",
                t["trad_pt_br"] or "",
                t["trad_en"] or "",
                t["trad_cs"] or "",
                t["trad_pl"] or "",
                t["trad_tr"] or "",
            ]
            lines.append(";".join(row))

        csv_content = "\n".join(lines)

        # Save file
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        csv_dir = os.path.join(base_dir, "datos", "tarjetas")
        os.makedirs(csv_dir, exist_ok=True)
        csv_path = os.path.join(csv_dir, f"U{unidad:02d}-vocabulario.csv")

        with open(csv_path, "w", encoding="utf-8") as f:
            f.write(csv_content)

        return json.dumps({
            "archivo": csv_path,
            "total_tarjetas": len(tarjetas),
            "preview": lines[:3],
        }, ensure_ascii=False)
