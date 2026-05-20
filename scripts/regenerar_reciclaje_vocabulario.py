#!/usr/bin/env python3
"""
Regenera los hilos automáticos de vocabulario en `unidades/nc1-reciclaje.json`
a partir de `vocabulario_consolidado` de cada inventario.

⚠️ ESTADO TRANSITORIO (2026-05-15, v10.120):
   Este script asume SHAPE v10.114 (pre-rediseño de fase 1):
     - actividad.campo_semantico presente
     - vocabulario_consolidado con 3 sub-bloques: principal/recurrente/comprension
     - enfoque admite valor 'fonetica' (no 'pronunciacion_ortografia')
   Tras el rediseño de fase 1 v10.115-118 el shape cambió:
     - campo_semantico eliminado del schema
     - vocabulario_consolidado reducido a 2 sub-bloques: principal/recurrente
     - 3 bloques top-level consolidados nuevos paralelos
       (tiempos_y_verbos_consolidado, gramatica_consolidada, pronunciacion_ortografia_consolidada)
     - 4 listas tipadas por actividad
   Este script FALLARÁ si se ejecuta contra inventarios en shape v10.117.
   Pendiente de adaptación cuando se reactive fase 2 (decisión 36, v10.108).
   Fase 2 actualmente PAUSADA por el procesamiento pendiente de U1-U9 al shape nuevo
   (U0 ya migrada en v10.119).

Comportamiento (modelo v10.114):
- Lee todos los inventarios `unidades/U*/U*-nc1-inventario.json` disponibles.
- Por cada `campo_semantico` único (en principal / recurrente / comprension),
  genera un hilo con `nivel_analisis: "auto"`.
- Eventos por unidad donde aparece ese campo:
    * primera unidad → accion `introduce` (si principal/recurrente) o `aplica` (si solo comprension)
    * unidades siguientes → accion `amplia` (si principal/recurrente) o `aplica` (si solo comprension)
- Preserva los hilos existentes con `nivel_analisis: "mapa"` o `"detalle"`.
- Sobrescribe únicamente los hilos `auto`.

Uso: python3 scripts/regenerar_reciclaje_vocabulario.py
"""
import json
import os
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
RECICLAJE = PROJECT / "unidades" / "nc1-reciclaje.json"


def _cuarentena():
    """v11.19: fail-fast. Este script asume shape v10.114 (pre-rediseño de fase 1).
    Los inventarios actuales son post-v10.153 — ejecutarlo falla o corrompe datos.
    Se rechaza la ejecución salvo override explícito de mantenimiento."""
    if os.environ.get("RECICLAJE_VOCAB_OVERRIDE") == "1":
        print("⚠️  RECICLAJE_VOCAB_OVERRIDE=1 — ejecutando script en cuarentena bajo tu responsabilidad.")
        return
    print("⛔ BLOQUEADO — regenerar_reciclaje_vocabulario.py está en cuarentena.")
    print("   Asume SHAPE v10.114 (pre-rediseño de fase 1): campo_semantico, 3 sub-bloques, enfoque 'fonetica'.")
    print("   Los inventarios actuales son post-v10.153 → este script FALLA o produce datos corruptos.")
    print("   Fase 2 (reciclaje) está pausada. Reactivarlo exige reescribirlo al shape nuevo.")
    print("   Override solo para depuración de mantenimiento: RECICLAJE_VOCAB_OVERRIDE=1")
    sys.exit(2)


def slug(s: str) -> str:
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    return s


def map_seccion_bloque(bloque: str) -> str:
    """Bloque del vocabulario_consolidado → seccion del schema."""
    return {
        "principal": "vocabulario",
        "recurrente": "vocabulario",
        "comprension": "vocabulario",
    }.get(bloque, "vocabulario")


def main():
    _cuarentena()
    inventarios = sorted(PROJECT.glob("unidades/U*/U*-nc1-inventario.json"))
    BLOQUE_ORDER = {"principal": 0, "recurrente": 1, "comprension": 2}
    # campo → list of (unidad, bloque, n_palabras, posicion_global)
    # primera_aparicion[campo] = (unidad, bloque_idx, posicion) — para orden de aparición
    campos = {}
    primera_aparicion = {}
    pos_global = 0
    for path in inventarios:
        d = json.loads(path.read_text(encoding="utf-8"))
        unidad = d["unidad"]
        voc = d.get("vocabulario_consolidado", {})
        for bloque in ("principal", "recurrente", "comprension"):
            b = voc.get(bloque, {})
            if not isinstance(b, dict):
                continue
            for campo, palabras in b.items():
                if campo.startswith("_"):
                    continue
                if not isinstance(palabras, list):
                    continue
                pos_global += 1
                campos.setdefault(campo, []).append((unidad, bloque, len(palabras)))
                if campo not in primera_aparicion:
                    primera_aparicion[campo] = (unidad, BLOQUE_ORDER[bloque], pos_global)

    # Orden de aparición: por unidad de primera aparición, luego bloque, luego posición global
    campos_ordenados = sorted(campos.keys(), key=lambda c: primera_aparicion[c])

    auto_hilos = []
    for campo in campos_ordenados:
        ocurrencias = campos[campo]
        ocurrencias.sort(key=lambda x: (x[0], ["principal", "recurrente", "comprension"].index(x[1])))
        eventos = []
        primera_productiva_dada = False
        for i, (unidad, bloque, n) in enumerate(ocurrencias):
            es_productivo = bloque in ("principal", "recurrente")
            if es_productivo:
                if not primera_productiva_dada:
                    accion = "introduce"
                    primera_productiva_dada = True
                else:
                    accion = "amplia"
            else:
                accion = "aplica"
            impacto = "alto" if bloque == "principal" else ("medio" if bloque == "recurrente" else "bajo")
            eventos.append({
                "unidad": unidad,
                "seccion": map_seccion_bloque(bloque),
                "accion": accion,
                "descripcion": f"[{bloque}] {n} entradas",
                "impacto": impacto,
            })
        auto_hilos.append({
            "id": f"hilo-voc-{slug(campo)}",
            "titulo": campo,
            "tipo": "vocabulario",
            "nivel_analisis": "auto",
            "eventos": eventos,
        })

    data = json.loads(RECICLAJE.read_text(encoding="utf-8"))
    manuales = [h for h in data.get("hilos", []) if h.get("nivel_analisis") != "auto"]

    def primer_unidad(h):
        evs = h.get("eventos", [])
        return min((e["unidad"] for e in evs), default=99)

    manuales.sort(key=primer_unidad)
    auto_hilos.sort(key=primer_unidad)
    # Estrategia final: intercalar manuales y auto por orden de aparición global
    todos = manuales + auto_hilos
    todos.sort(key=primer_unidad)
    data["hilos"] = todos
    data["actualizado"] = date.today().isoformat()
    RECICLAJE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Inventarios leídos: {len(inventarios)}")
    print(f"Campos semánticos únicos: {len(campos)}")
    print(f"Hilos auto generados: {len(auto_hilos)}")
    print(f"Hilos manuales preservados (mapa/detalle): {len(manuales)}")
    print(f"Total hilos en {RECICLAJE.relative_to(PROJECT)}: {len(todos)} (ordenados por unidad de primera aparición)")


if __name__ == "__main__":
    main()