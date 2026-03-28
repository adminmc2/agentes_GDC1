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
        "Consulta el inventario de una unidad en la BD: "
        "páginas, sección, contenido lingüístico, texto de actividades, "
        "respuestas y contenidos del índice. "
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

        # Páginas + actividades + respuestas (solo campos relevantes para vocabulario)
        cur.execute(
            """
            SELECT
                p.numero AS numero_pagina,
                p.seccion,
                a.contenido_linguistico,
                a.texto_completo,
                array_agg(r.texto ORDER BY r.orden)
                    FILTER (WHERE r.id IS NOT NULL) AS respuestas
            FROM paginas p
            JOIN actividades a ON a.pagina_id = p.id
            LEFT JOIN respuestas r ON r.actividad_id = a.id
            WHERE p.unidad_id = (SELECT id FROM unidades WHERE numero = %s)
            GROUP BY p.numero, p.seccion,
                     a.contenido_linguistico, a.texto_completo
            ORDER BY p.numero
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
            SELECT articulo, palabra, campo_semantico, silaba_tonica,
                   gramapop, ejemplo, combos,
                   trad_en, trad_fr, trad_pt, trad_al,
                   trad_pl, trad_nl, trad_gr, trad_tr, trad_cz,
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


class ConsultarReglas(BaseTool):
    name: str = "consultar_reglas"
    description: str = (
        "Retrieves learned rules distilled from accumulated editorial corrections. "
        "These are general patterns (not specific words) that MUST be applied to ALL cards. "
        "Rules take priority over any default behavior."
    )

    def _run(self, crew: str = "recurvo") -> str:
        conn = _get_conn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(
            """
            SELECT tipo_error, regla, ejemplos, n_correcciones
            FROM reglas_aprendidas
            WHERE crew = %s AND activa = true
            ORDER BY n_correcciones DESC
            """,
            (crew,),
        )
        reglas = [dict(r) for r in cur.fetchall()]
        conn.close()
        return json.dumps(
            {"reglas": reglas, "total": len(reglas)},
            ensure_ascii=False,
            default=str,
        )


class EscribirTarjetas(BaseTool):
    name: str = "escribir_tarjetas"
    description: str = (
        "Escribe tarjetas de vocabulario validadas en la BD. "
        "Parámetro: JSON string con array de tarjetas. "
        "Cada tarjeta debe tener: articulo, palabra, silaba_tonica, "
        "gramapop, campo_semantico, color_campo, ejemplo, "
        "combos (array de 3 strings), trad_en, trad_fr, trad_pt, trad_al, "
        "trad_pl, trad_nl, trad_gr, trad_tr, trad_cz, seccion, pagina, nivel_jerarquia, estado, "
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
                    unidad_id, seccion, pagina, articulo, palabra,
                    silaba_tonica, gramapop, campo_semantico, color_campo,
                    ejemplo, combos,
                    trad_en, trad_fr, trad_pt, trad_al,
                    trad_pl, trad_nl, trad_gr, trad_tr, trad_cz,
                    nivel_jerarquia, estado, unidad_origen
                ) VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s,
                    %s, %s,
                    %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s
                )
                ON CONFLICT (palabra, unidad_origen) DO UPDATE SET
                    articulo = EXCLUDED.articulo,
                    silaba_tonica = EXCLUDED.silaba_tonica,
                    gramapop = EXCLUDED.gramapop,
                    campo_semantico = EXCLUDED.campo_semantico,
                    color_campo = EXCLUDED.color_campo,
                    ejemplo = EXCLUDED.ejemplo,
                    combos = EXCLUDED.combos,
                    trad_en = EXCLUDED.trad_en,
                    trad_fr = EXCLUDED.trad_fr,
                    trad_pt = EXCLUDED.trad_pt,
                    trad_al = EXCLUDED.trad_al,
                    trad_pl = EXCLUDED.trad_pl,
                    trad_nl = EXCLUDED.trad_nl,
                    trad_gr = EXCLUDED.trad_gr,
                    trad_tr = EXCLUDED.trad_tr,
                    trad_cz = EXCLUDED.trad_cz,
                    nivel_jerarquia = EXCLUDED.nivel_jerarquia,
                    estado = EXCLUDED.estado,
                    fecha_modificacion = NOW()
                """,
                (
                    unidad_id,
                    t.get("seccion", "vocabulario"),
                    t.get("pagina"),
                    t.get("articulo"),
                    t["palabra"],
                    t.get("silaba_tonica"),
                    t.get("gramapop"),
                    t.get("campo_semantico"),
                    t.get("color_campo"),
                    t.get("ejemplo"),
                    Json(t.get("combos", [])),
                    t.get("trad_en"),
                    t.get("trad_fr"),
                    t.get("trad_pt"),
                    t.get("trad_al"),
                    t.get("trad_pl"),
                    t.get("trad_nl"),
                    t.get("trad_gr"),
                    t.get("trad_tr"),
                    t.get("trad_cz"),
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
            SELECT articulo, palabra, silaba_tonica,
                   campo_semantico, color_campo, ejemplo, gramapop,
                   combos,
                   trad_en, trad_fr, trad_pt, trad_al,
                   trad_pl, trad_nl, trad_gr, trad_tr, trad_cz
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
            "articulo", "palabra", "silaba_tonica",
            "campo_semantico", "color_campo", "ejemplo", "gramapop",
            "combo1_estructura", "combo1_ejemplo",
            "combo2_estructura", "combo2_ejemplo",
            "combo3_estructura", "combo3_ejemplo",
            "EN", "FR", "PT", "AL", "PL", "NL", "GR", "TR", "CZ",
        ]

        lines = [";".join(headers)]
        for t in tarjetas:
            combos = t["combos"] or []
            while len(combos) < 3:
                combos.append("")
            row = [
                t.get("articulo") or "",
                t["palabra"] or "",
                t["silaba_tonica"] or "",
                t["campo_semantico"] or "",
                t["color_campo"] or "",
                t["ejemplo"] or "",
                t.get("gramapop") or t.get("regla") or "",
                combos[0], "", combos[1], "", combos[2], "",
                t.get("trad_en") or "",
                t.get("trad_fr") or "",
                t.get("trad_pt") or t.get("trad_pt_br") or "",
                t.get("trad_al") or "",
                t.get("trad_pl") or "",
                t.get("trad_nl") or "",
                t.get("trad_gr") or "",
                t.get("trad_tr") or "",
                t.get("trad_cz") or t.get("trad_cs") or "",
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
