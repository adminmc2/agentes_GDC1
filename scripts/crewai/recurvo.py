#!/usr/bin/env python3
"""
Crew Recurvo — Vocabulary card generation pipeline.
Run with: python scripts/crewai/recurvo.py [unidad]

Architecture: 3 sequential agents, each with its own LLM.
  Agent 1 (Generator):  reads BD → produces JSON array of cards
  Agent 2 (Verifier):   validates cards against source data → corrected JSON
  Agent 3 (Writer):     persists cards to BD + exports CSV

Agent config (role, goal, backstory, task_description, task_expected_output,
max_iter) lives in the crew_agents table in Neon PostgreSQL.
Tools and LLM params stay in code / env vars.
"""

import os
import sys
import time

import psycopg2
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, Process, LLM
from tools import (
    ConsultarInventario,
    ConsultarTarjetasPrevias,
    ConsultarCorrecciones,
    EscribirTarjetas,
    ExportarCSV,
)

# --- Langfuse (trazabilidad via litellm callback) ---
if os.environ.get("LANGFUSE_PUBLIC_KEY"):
    import litellm
    litellm.success_callback = ["langfuse"]
    litellm.failure_callback = ["langfuse"]
    print("[Langfuse] Trazabilidad ACTIVA — cada llamada LLM se registra en cloud.langfuse.com")
else:
    print("[Langfuse] No configurado — ejecutando sin trazabilidad")

# --- LLMs (one per agent, each with its own model + params) ---
LLM_CFG = {
    "gen": {
        "model": os.environ.get("RECURVO_LLM_GEN",
                                os.environ.get("RECURVO_LLM", "groq/openai/gpt-oss-120b")),
        "max_tokens": int(os.environ.get("RECURVO_MAXTOK_GEN", "8192")),
        "temperature": float(os.environ.get("RECURVO_TEMP_GEN", "0.7")),
        "top_p": float(os.environ.get("RECURVO_TOPP_GEN", "1.0")),
    },
    "ver": {
        "model": os.environ.get("RECURVO_LLM_VER", "groq/llama-3.3-70b-versatile"),
        "max_tokens": int(os.environ.get("RECURVO_MAXTOK_VER", "8192")),
        "temperature": float(os.environ.get("RECURVO_TEMP_VER", "0.2")),
        "top_p": float(os.environ.get("RECURVO_TOPP_VER", "1.0")),
    },
    "wr": {
        "model": os.environ.get("RECURVO_LLM_WR", "groq/llama-3.1-8b-instant"),
        "max_tokens": int(os.environ.get("RECURVO_MAXTOK_WR", "2048")),
        "temperature": float(os.environ.get("RECURVO_TEMP_WR", "0.0")),
        "top_p": float(os.environ.get("RECURVO_TOPP_WR", "1.0")),
    },
}

# --- Tools by agent_key (stays in code, not in BD) ---
TOOLS_MAP = {
    "generador": [
        ConsultarInventario(),
        ConsultarTarjetasPrevias(),
        ConsultarCorrecciones(),
    ],
    "verificador": [
        ConsultarInventario(),
    ],
    "escritor": [
        EscribirTarjetas(),
        ExportarCSV(),
    ],
}

# --- LLM by agent_key (stays in code/env vars, not in BD) ---
LLM_KEY_MAP = {
    "generador": "gen",
    "verificador": "ver",
    "escritor": "wr",
}


def _render(template: str, unidad: int) -> str:
    """Replace {unidad} and {unidad:02d} placeholders in BD templates."""
    return (template
            .replace("{unidad:02d}", f"{unidad:02d}")
            .replace("{unidad}", str(unidad)))


def cargar_config_bd(crew_name: str) -> list[dict]:
    """Load agent configs from crew_agents table, ordered by agent_order."""
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()
    cur.execute(
        "SELECT agent_key, agent_order, role, goal, backstory, "
        "task_description, task_expected_output, max_iter "
        "FROM crew_agents WHERE crew = %s ORDER BY agent_order",
        (crew_name,),
    )
    cols = [d[0] for d in cur.description]
    rows = [dict(zip(cols, row)) for row in cur.fetchall()]
    conn.close()
    if not rows:
        raise RuntimeError(
            f"No agent configs found in crew_agents for crew='{crew_name}'. "
            "Run scripts/crear_crew_agents.py first."
        )
    return rows


def crear_crew(unidad: int) -> Crew:
    """Build agents, tasks and Crew from BD config + code-level tools/LLMs."""
    configs = cargar_config_bd("recurvo")

    agents = []
    tasks = []
    prev_task = None

    for cfg in configs:
        key = cfg["agent_key"]
        llm_key = LLM_KEY_MAP.get(key)
        if not llm_key:
            raise RuntimeError(f"No LLM mapping for agent_key='{key}'")

        llm = LLM(**LLM_CFG[llm_key])

        agent = Agent(
            name=f"recurvo_{key}",
            role=cfg["role"],
            goal=cfg["goal"],
            backstory=cfg["backstory"],
            tools=TOOLS_MAP.get(key, []),
            llm=llm,
            verbose=True,
            max_iter=cfg["max_iter"],
        )
        agents.append(agent)

        task = Task(
            description=_render(cfg["task_description"], unidad),
            expected_output=_render(cfg["task_expected_output"], unidad),
            agent=agent,
            context=[prev_task] if prev_task else [],
        )
        tasks.append(task)
        prev_task = task

    crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
        memory=False,
    )
    return crew


def main():
    unidad = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    t0 = time.time()

    def _fmt(cfg):
        return f"{cfg['model']}  temp={cfg['temperature']}  max={cfg['max_tokens']}  top_p={cfg['top_p']}"

    print(f"\n{'='*70}")
    print(f"  CREW RECURVO — Unidad {unidad}")
    print(f"  Generador:   {_fmt(LLM_CFG['gen'])}")
    print(f"  Verificador: {_fmt(LLM_CFG['ver'])}")
    print(f"  Escritor:    {_fmt(LLM_CFG['wr'])}")
    print(f"  Config:      crew_agents table (Neon PostgreSQL)")
    print(f"  Pipeline:    generador → verificador → escritor")
    print(f"{'='*70}\n")

    crew = crear_crew(unidad)
    resultado = crew.kickoff()
    duracion = time.time() - t0

    print(f"\n{'='*60}")
    print("  RESULTADO")
    print(f"{'='*60}")
    print(resultado)

    # Save raw output
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "datos", "tarjetas",
    )
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"U{unidad:02d}-recurvo-output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(str(resultado))
    print(f"\nOutput guardado en: {output_path}")
    print(f"Duración: {duracion:.1f}s")

    print("[Langfuse] Trazas enviadas automáticamente via litellm callback")


if __name__ == "__main__":
    main()
