#!/usr/bin/env python3
"""Diagrama de procesos del proyecto - Guía Didáctica del Profesor.

Genera diagramas Mermaid desde el estado real del proyecto.
Uso: python3 diagrama.py -> http://127.0.0.1:8080
"""

import http.server
import json
import hashlib
import os
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import psycopg2
from psycopg2.extras import RealDictCursor

PROJECT = Path(__file__).parent
PORT = 8080
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_DU3EHycC7KhT@ep-floral-unit-anln8vly.c-6.us-east-1.aws.neon.tech/neondb?sslmode=require",
)


def _db():
    return psycopg2.connect(DATABASE_URL)


def get_tarjetas(unidad):
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("""
        SELECT t.id, t.palabra, t.genero, t.color_genero, t.silaba_tonica,
               t.regla, t.campo_semantico, t.color_campo, t.ejemplo,
               t.frecuencia, t.irregularidad, t.combos,
               t.trad_it, t.trad_fr, t.trad_pt_br, t.trad_en,
               t.trad_cs, t.trad_pl, t.trad_tr,
               t.seccion, t.pagina, t.nivel_jerarquia, t.estado, t.unidad_origen
        FROM tarjetas_vocabulario t
        JOIN unidades u ON t.unidad_id = u.id
        WHERE u.numero = %s
        ORDER BY t.nivel_jerarquia, t.campo_semantico, t.palabra
    """, (unidad,))
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def get_correcciones(unidad=None):
    conn = _db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    if unidad:
        cur.execute("""
            SELECT id, agente, unidad, palabra, campo, valor_original,
                   valor_corregido, tipo_error, fecha
            FROM correcciones WHERE unidad = %s ORDER BY fecha DESC
        """, (unidad,))
    else:
        cur.execute("""
            SELECT id, agente, unidad, palabra, campo, valor_original,
                   valor_corregido, tipo_error, fecha
            FROM correcciones ORDER BY fecha DESC LIMIT 100
        """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


def insert_correccion(data):
    conn = _db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO correcciones (agente, unidad, palabra, campo,
                                  valor_original, valor_corregido, tipo_error)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (
        data.get("agente", "recurso_vocabulario"),
        data["unidad"],
        data["palabra"],
        data["campo"],
        data["valor_original"],
        data["valor_corregido"],
        data["tipo_error"],
    ))
    new_id = cur.fetchone()[0]
    conn.commit()
    conn.close()
    return new_id


def delete_tarjeta(tarjeta_id):
    conn = _db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tarjetas_vocabulario WHERE id = %s", (tarjeta_id,))
    conn.commit()
    conn.close()


def update_tarjeta_field(tarjeta_id, campo, valor):
    allowed = {
        "palabra", "genero", "color_genero", "silaba_tonica", "regla",
        "campo_semantico", "color_campo", "ejemplo", "frecuencia",
        "irregularidad", "trad_it", "trad_fr", "trad_pt_br", "trad_en",
        "trad_cs", "trad_pl", "trad_tr", "seccion", "pagina",
        "nivel_jerarquia", "estado", "unidad_origen",
    }
    if campo not in allowed:
        return False
    conn = _db()
    cur = conn.cursor()
    cur.execute(
        f"UPDATE tarjetas_vocabulario SET {campo} = %s, fecha_modificacion = NOW() WHERE id = %s",
        (valor, tarjeta_id),
    )
    conn.commit()
    conn.close()
    return True

UNITS = [f"U{i:02d}" for i in range(1, 10)]
SECTIONS = ["vocabulario", "gramatica", "comunicacion", "destrezas",
            "cultura", "reflexion", "evaluacion", "itinerarios"]
SECTION_LABELS = {
    "vocabulario": "Vocabulario",
    "gramatica": "Gramática",
    "comunicacion": "Comunicación",
    "destrezas": "Destrezas",
    "cultura": "Cultura",
    "reflexion": "Reflexión",
    "evaluacion": "Evaluación",
    "itinerarios": "Itinerarios",
}

AGENTS = {
    "vocabulario": {"name": "Vocabulario", "rep": "repertorios/vocabulario.md"},
    "gramatica": {"name": "Gramática", "rep": "repertorios/gramatica.md"},
    "comunicacion": {"name": "Comunicación", "rep": "repertorios/comunicacion.md"},
    "destrezas": {"name": "Destrezas", "rep": "repertorios/destrezas.md"},
    "cultura": {"name": "Cultura", "rep": "repertorios/cultura.md"},
    "evaluacion": {"name": "Evaluación", "rep": "repertorios/evaluacion.md"},
}


def scan_section(unit_dir, unit, section):
    candidates = list(unit_dir.glob(f"{unit}-{section}*.md"))
    main = [f for f in candidates if "-paginas" not in f.name]
    if not main:
        return {"status": "missing", "lines": 0, "pendiente": 0, "path": ""}
    f = main[0]
    text = f.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    pend = sum(1 for l in lines if "*pendiente*" in l)
    n = len(lines)
    if pend == 0 and n > 100:
        st = "complete"
    elif n > 50:
        st = "in-progress"
    else:
        st = "structure-only"
    return {"status": st, "lines": n, "pendiente": pend,
            "path": str(f.relative_to(PROJECT))}


def scan_all():
    result = {}
    for u in UNITS:
        d = PROJECT / "unidades" / u
        result[u] = {}
        for s in SECTIONS:
            if d.exists():
                result[u][s] = scan_section(d, u, s)
            else:
                result[u][s] = {"status": "missing", "lines": 0, "pendiente": 0, "path": ""}
    return result


def color_for(status):
    if status == "complete": return "#2ecc71"
    if status == "in-progress": return "#f39c12"
    if status == "structure-only": return "#e67e22"
    return "#bdc3c7"


def mermaid_level1():
    return """graph TD
    LIBRO["Libro de texto - Nuevo Compañeros 1"]
    FUENTE["Material fuente - datos/fuente/ - PDF embebido por unidad"]
    INV["Inventario JSON - datos/inventarios/UXX-inventario.json"]
    BD[("Neon PostgreSQL - Base de datos - Fuente de verdad")]

    subgraph INFRA["Infraestructura pedagógica"]
        MT["Marco teórico - 72 KB"]
        CG["Curso general - 50 KB"]
        REF["10 bancos de técnicas - 800+ técnicas"]
    end

    subgraph REPS["Repertorios - opciones de explotación"]
        R_V["rep/vocabulario"]
        R_G["rep/gramática"]
        R_C["rep/comunicación"]
        R_D["rep/destrezas"]
        R_CU["rep/cultura"]
        R_E["rep/evaluación"]
    end

    subgraph AGENTES["Sistema de agentes - prompts v5.0"]
        AG_V["Vocabulario"]
        AG_G["Gramática"]
        AG_C["Comunicación"]
        AG_D["Destrezas"]
        AG_CU["Cultura"]
        AG_E["Evaluación"]
    end

    subgraph OUTPUT["Output por unidad"]
        EXP["Explotación didáctica - 7 secciones"]
        PIL["Píldoras formativas - 10 por unidad"]
        TAR["Tarjetas - vocabulario + gramática"]
        ITI["Itinerarios - 8 sesiones"]
    end

    LIBRO --> FUENTE
    FUENTE --> INV
    INV -->|"importación"| BD
    BD --> AGENTES
    INFRA --> AGENTES
    REPS --> AGENTES
    AGENTES --> OUTPUT

    OUTPUT --> GUIA["CAPA 1 - Guía impresa SGEL"]
    BD -.->|"consultas"| PERS["CAPA 3 - Guías personalizadas - futuro"]
    OUTPUT -.-> PERS

    style LIBRO fill:#3498db,color:#fff
    style FUENTE fill:#2980b9,color:#fff
    style INV fill:#8e44ad,color:#fff
    style BD fill:#e74c3c,color:#fff
    style GUIA fill:#2ecc71,color:#fff
    style PERS fill:#95a5a6,color:#fff,stroke-dasharray: 5 5
    style INFRA fill:#e8eaf6
    style AGENTES fill:#fff3e0
    style REPS fill:#e8f5e9
    style OUTPUT fill:#fce4ec"""


def mermaid_level2():
    return """graph LR
    subgraph PREP["1 - Preparación manual"]
        P1["Extraer actividades del inventario"]
        P2["Filtrar repertorio aplicable"]
        P3["Compilar reciclaje previo"]
        P4["Compilar contexto lingüístico"]
        P1 --> P2 --> P3 --> P4
    end

    subgraph GEN["2 - Generación con Claude Code"]
        G1["Cargar prompt del agente"]
        G2["Proporcionar inputs"]
        G3["Generar explotación + píldoras"]
        G1 --> G2 --> G3
    end

    subgraph POST["3 - Post-producción"]
        V1["Horas total máx. 7h"]
        V2["Variedad de opciones"]
        V3["Reciclaje mín. 30%"]
        V4["Ritmo máx. 15 min"]
        V5["Coherencia inter-sección"]
        V1 --- V2 --- V3 --- V4 --- V5
    end

    PREP --> GEN --> POST
    POST -->|OK| DONE["Sección validada"]
    POST -->|Falla| GEN

    style PREP fill:#e3f2fd
    style GEN fill:#fff3e0
    style POST fill:#f3e5f5
    style DONE fill:#2ecc71,color:#fff"""


def mermaid_level3():
    return """graph TD
    VOC["S1 Vocabulario - Ciclo 5 fases"]
    GRA["S2 Gramática - Ciclo 5 fases"]
    COM["S3 Comunicación - Protocolo A/C"]
    DES["S4 Destrezas - Protocolos L/E/CO/H"]
    CUL["S5 Cultura - Protocolo CU"]
    EVA["S7 Reflexión y Evaluación - Protocolo RE"]

    VOC -->|"exposición incidental"| GRA
    VOC -->|"vocabulario formalizado"| COM
    GRA -->|"gramática formalizada"| COM
    VOC -->|"reciclaje"| DES
    GRA -->|"reciclaje"| DES
    COM -->|"funciones comunicativas"| DES
    VOC -->|"contenedor mapeado"| CUL
    GRA -->|"contenedor mapeado"| CUL
    COM -->|"contenedor mapeado"| CUL
    DES -->|"estrategias"| CUL
    VOC -->|"100% reciclaje"| EVA
    GRA -->|"100% reciclaje"| EVA
    COM -->|"100% reciclaje"| EVA
    DES -->|"100% reciclaje"| EVA
    CUL -->|"100% reciclaje"| EVA

    subgraph CAJA["Estación de Servicio - tarjetas acumulativas"]
        C1["Caja 1 Vocabulario"]
        C2["Caja 2 Tips y esquemas"]
        C3["Caja 3 Gramatips"]
        C4["Caja 4 Estrategias destreza"]
        C5["Caja 5 Estrategia intercultural"]
    end

    VOC -.-> C1
    COM -.-> C2
    GRA -.-> C3
    DES -.-> C4
    CUL -.-> C5

    style VOC fill:#3498db,color:#fff
    style GRA fill:#2ecc71,color:#fff
    style COM fill:#e74c3c,color:#fff
    style DES fill:#9b59b6,color:#fff
    style CUL fill:#f39c12,color:#fff
    style EVA fill:#1abc9c,color:#fff
    style CAJA fill:#f5f5f5"""


def mermaid_level4(status):
    lines = ["graph LR"]
    for sid, info in AGENTS.items():
        s = status.get("U03", {}).get(sid, {})
        st = s.get("status", "missing")
        c = color_for(st)
        n = s.get("lines", 0)
        label = f'{info["name"]} - {n} líneas - {st}'
        lines.append(f'    AG_{sid}["{label}"]')
        lines.append(f'    REP_{sid}["{info["rep"]}"]')
        lines.append(f"    REP_{sid} --> AG_{sid}")
        lines.append(f"    style AG_{sid} fill:{c},color:#fff")
    lines.append('    INV["datos/inventarios/U03-inventario.json"] --> AG_vocabulario')
    lines.append("    INV --> AG_gramatica")
    lines.append("    INV --> AG_comunicacion")
    lines.append("    INV --> AG_destrezas")
    lines.append("    INV --> AG_cultura")
    lines.append("    INV --> AG_evaluacion")
    lines.append("    style INV fill:#3498db,color:#fff")
    return "\n".join(lines)


def mermaid_database():
    return """erDiagram
    unidades {
        int id PK
        int numero UK
        text curso
        text titulo
        text paginas
        text nivel
        jsonb contenidos_indice
    }
    paginas {
        int id PK
        int unidad_id FK
        int numero
        text seccion
    }
    actividades {
        int id PK
        int pagina_id FK
        text codigo UK
        int numero
        text tipo
        text instruccion
        jsonb contenido_linguistico
        text destreza
        boolean tiene_audio
        int pista_audio
        boolean tiene_imagen
        text descripcion
    }
    respuestas {
        int id PK
        int actividad_id FK
        int orden
        text texto
    }
    cuadros_gramaticales {
        int id PK
        int pagina_id FK
        text titulo
        jsonb contenido
    }
    reciclaje {
        int id PK
        int actividad_origen_id FK
        int actividad_destino_id FK
        text contenido
        text tipo
    }
    profesores {
        int id PK
        text nombre
        text centro
        text pais
        text nivel_escolar
    }
    grupos {
        int id PK
        int profesor_id FK
        text nombre_grupo
        int cantidad_estudiantes
        boolean nee
        text nee_detalle
        numeric horas_semana
        int duracion_clase
        numeric horas_ano
    }
    personalizaciones {
        int id PK
        int grupo_id FK
        int actividad_id FK
        int tiempo_custom
        text variante
        text notas
        boolean completada
    }

    unidades ||--o{ paginas : "tiene"
    paginas ||--o{ actividades : "contiene"
    paginas ||--o{ cuadros_gramaticales : "incluye"
    actividades ||--o{ respuestas : "tiene"
    actividades ||--o{ reciclaje : "origen"
    actividades ||--o{ reciclaje : "destino"
    profesores ||--o{ grupos : "tiene"
    grupos ||--o{ personalizaciones : "crea"
    actividades ||--o{ personalizaciones : "recibe"
"""


def build_diagrams_json():
    """Return all diagram codes + status as JSON for live polling."""
    status = scan_all()
    return json.dumps({
        "nivel1": mermaid_level1(),
        "nivel2": mermaid_level2(),
        "nivel3": mermaid_level3(),
        "nivel4": mermaid_level4(status),
        "database": mermaid_database(),
        "status": status,
        "hash": hashlib.md5(json.dumps(status, sort_keys=True).encode()).hexdigest()[:8],
    }, ensure_ascii=False)


HTML_FILE = PROJECT / "web" / "index.html"


def load_html_template():
    """Lee el HTML desde disco en cada request (hot reload)."""
    return HTML_FILE.read_text(encoding="utf-8")


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def _respond(self, code, ctype, body):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        if parsed.path == "/api/status":
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(scan_all(), ensure_ascii=False))
        elif parsed.path == "/api/diagrams":
            self._respond(200, "application/json; charset=utf-8",
                          build_diagrams_json())
        elif parsed.path == "/api/tarjetas":
            unidad = int(qs.get("unidad", [3])[0])
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_tarjetas(unidad), ensure_ascii=False, default=str))
        elif parsed.path == "/api/correcciones":
            unidad = qs.get("unidad", [None])[0]
            unidad = int(unidad) if unidad else None
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps(get_correcciones(unidad), ensure_ascii=False, default=str))
        elif parsed.path == "/":
            html = load_html_template()
            html = html.replace("SECTIONS_JSON", json.dumps(SECTIONS))
            html = html.replace("LABELS_JSON", json.dumps(SECTION_LABELS, ensure_ascii=False))
            self._respond(200, "text/html; charset=utf-8", html)
        else:
            self.send_error(404)

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length)) if length else {}

        if parsed.path == "/api/correcciones":
            new_id = insert_correccion(body)
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"id": new_id, "ok": True}))
        elif parsed.path == "/api/tarjetas/delete":
            delete_tarjeta(body["id"])
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"ok": True}))
        elif parsed.path == "/api/tarjetas/update":
            ok = update_tarjeta_field(body["id"], body["campo"], body["valor"])
            self._respond(200, "application/json; charset=utf-8",
                          json.dumps({"ok": ok}))
        else:
            self.send_error(404)


if __name__ == "__main__":
    server = http.server.HTTPServer(("127.0.0.1", PORT), Handler)
    print(f"Sistema de gestión: http://127.0.0.1:{PORT}")
    print("En vivo - se actualiza cada 3 segundos")
    print("Ctrl+C para detener")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDetenido.")
