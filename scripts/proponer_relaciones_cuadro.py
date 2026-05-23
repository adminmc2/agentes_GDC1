#!/usr/bin/env python3
"""
Helper Capa 2 — propone candidatos de `relacion_cross_hilo` por cuadro compartido.

Lee `unidades/nc1-reciclaje.json`, detecta pares de hilos cuyos eventos
comparten ≥1 referencia `cuadro@*` en la misma unidad y crea (o actualiza,
si ya existen pendientes) propuestas con `tipo: relacion_cross_hilo` y
`relacion_candidata: {hilos: [a, b] ordenados, cuadros_compartidos}`.

Política (`reglas-reciclaje.md` §15):
  - Solo evidencias `cuadro@*` (las actividades son señal demasiado polifónica).
  - Candidata **no dirigida**: el payload guarda el par sin asignar origen ni
    destino. La dirección (cuando el `tipo` la requiere) la elige el humano al
    aceptar; aquí no se sesga editorialmente.
  - Idempotente: ID canónico del par ordenado `prop-rel-<menor>-<mayor>`.
    Mismo cálculo para crear, buscar duplicados y futuro cierre.
  - Propuestas existentes con estado `aceptada` o `rechazada` no se tocan
    (decisión humana cerrada — el helper no la revive).
  - Pendientes existentes se actualizan: se completa `cuadros_compartidos`
    con los cuadros nuevos detectados sin duplicar.

Uso:
    python3 scripts/proponer_relaciones_cuadro.py [--dry-run]
"""
import argparse
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
RECICLAJE = PROJECT / "unidades" / "nc1-reciclaje.json"

CUADRO_RE = re.compile(r"^cuadro@[^\s]+")


def id_relacion_par(hilo_a: str, hilo_b: str) -> str:
    """Constructor canónico de id del par ordenado (`reglas §15`).

    ÚNICO punto de cálculo — usado por el helper para crear/buscar duplicados
    y por el flujo de cierre manual. Mantener importable desde ahí evita
    desalineaciones sutiles.
    """
    a, b = sorted([hilo_a, hilo_b])
    return f"prop-rel-{a}-{b}"


def _cuadros_de_evento(ev: dict) -> set:
    """Devuelve el conjunto de referencias `cuadro@*` de un evento."""
    out = set()
    for ev_ref in ev.get("evidencias") or []:
        if isinstance(ev_ref, str):
            # preservar sufijos como '@R' si existieran tras el cuadro
            base = ev_ref.split(" ")[0]
            if CUADRO_RE.match(base):
                out.add(base)
    return out


def detectar_pares(hilos: list) -> dict:
    """Recorre los hilos y agrupa por (unidad, cuadro) → lista de hilo.id.

    Devuelve dict {frozenset({id_a, id_b}): {"cuadros": set, "unidades": set}}
    para cada par con ≥1 cuadro compartido.
    """
    # indice: (unidad, cuadro) -> {hilo_id, ...}
    idx = defaultdict(set)
    for h in hilos:
        hid = h.get("id")
        if not hid:
            continue
        for ev in h.get("eventos") or []:
            u = ev.get("unidad")
            if not isinstance(u, int):
                continue
            for c in _cuadros_de_evento(ev):
                idx[(u, c)].add(hid)

    pares = defaultdict(lambda: {"cuadros": set(), "unidades": set()})
    for (u, c), ids in idx.items():
        if len(ids) < 2:
            continue
        ids_list = sorted(ids)
        for i in range(len(ids_list)):
            for j in range(i + 1, len(ids_list)):
                key = frozenset({ids_list[i], ids_list[j]})
                pares[key]["cuadros"].add(c)
                pares[key]["unidades"].add(u)
    return pares


def sincronizar_propuestas(reciclaje: dict, pares: dict) -> dict:
    """Crea/actualiza propuestas pendientes. Devuelve resumen de cambios."""
    propuestas = reciclaje.setdefault("propuestas", [])
    por_id = {p.get("id"): p for p in propuestas if isinstance(p, dict)}

    creadas, actualizadas, omitidas = 0, 0, 0
    for par, info in pares.items():
        a, b = sorted(par)
        pid = id_relacion_par(a, b)
        cuadros = sorted(info["cuadros"])
        unidades = sorted(info["unidades"])

        existente = por_id.get(pid)
        if existente is not None:
            if existente.get("estado") != "pendiente":
                omitidas += 1
                continue
            payload = existente.setdefault("relacion_candidata", {
                "hilos": [a, b], "cuadros_compartidos": []
            })
            # par no dirigido canónico — siempre [a, b] con a < b
            payload["hilos"] = [a, b]
            previos = set(payload.get("cuadros_compartidos") or [])
            nuevos = previos.union(cuadros)
            if nuevos != previos:
                payload["cuadros_compartidos"] = sorted(nuevos)
                existente["descripcion"] = _descripcion(a, b, sorted(nuevos), unidades)
                actualizadas += 1
            continue

        # propuesta no dirigida: sin hilo_ref (schema §6 v11.86) —
        # la dirección se elige al aceptar
        propuestas.append({
            "id": pid,
            "tipo": "relacion_cross_hilo",
            "descripcion": _descripcion(a, b, cuadros, unidades),
            "estado": "pendiente",
            "relacion_candidata": {
                "hilos": [a, b],
                "cuadros_compartidos": cuadros,
            },
        })
        por_id[pid] = propuestas[-1]
        creadas += 1

    return {"creadas": creadas, "actualizadas": actualizadas, "omitidas": omitidas}


def _descripcion(a: str, b: str, cuadros: list, unidades: list) -> str:
    cuadros_str = ", ".join(cuadros)
    unidades_str = ", ".join(f"U{u}" for u in unidades)
    return (
        f"Candidato relación cross-hilo (par no dirigido) entre '{a}' y '{b}'. "
        f"Cuadros compartidos: {cuadros_str} ({unidades_str}). "
        f"Capa 2 debe decidir 'tipo' (usa/prerrequisito/activa/contrasta/comparte), "
        f"elegir dirección si el tipo lo requiere y redactar 'detalle' editorial; "
        f"ver reglas-reciclaje.md §15."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="no escribe, solo reporta qué cambiaría")
    parser.add_argument("--ruta", default=str(RECICLAJE),
                        help="ruta a nc1-reciclaje.json")
    args = parser.parse_args()

    ruta = Path(args.ruta)
    with open(ruta, encoding="utf-8") as fh:
        reciclaje = json.load(fh)

    pares = detectar_pares(reciclaje.get("hilos") or [])
    resumen = sincronizar_propuestas(reciclaje, pares)

    print(f"Helper relaciones por cuadro compartido — {ruta}")
    print(f"  Pares con cuadro compartido detectados: {len(pares)}")
    print(f"  Propuestas nuevas:           {resumen['creadas']}")
    print(f"  Propuestas actualizadas:     {resumen['actualizadas']}")
    print(f"  Pares omitidos (ya cerrados): {resumen['omitidas']}")

    if args.dry_run:
        print("\n(dry-run: no se escribe)")
        return 0

    if resumen["creadas"] or resumen["actualizadas"]:
        reciclaje.setdefault("_meta", {})["fecha"] = date.today().isoformat()
        with open(ruta, "w", encoding="utf-8") as fh:
            json.dump(reciclaje, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"\n✓ Escrito {ruta}")
    else:
        print("\n(sin cambios)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
