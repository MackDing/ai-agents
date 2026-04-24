"""Run any agent from the CLI.

Usage:
    python examples/run_agent.py finance "Summarise my Q1 budget"
    python examples/run_agent.py devops "Check nginx status"
"""
import importlib
import sys

AGENTS = {"devops", "finance", "media", "office", "social"}


def main() -> None:
    if len(sys.argv) < 3 or sys.argv[1] not in AGENTS:
        print(f"Usage: run_agent.py <{'|'.join(sorted(AGENTS))}> <prompt>")
        sys.exit(1)
    domain, prompt = sys.argv[1], sys.argv[2]
    agent = importlib.import_module(f"agents.{domain}")
    print(agent.run(prompt))


if __name__ == "__main__":
    main()
