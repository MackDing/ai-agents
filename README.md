# ai-agents

AI agent fleet built on the Anthropic Claude API. Five domain agents sharing a common agentic loop — only the tools differ.

## Agents

| Agent | Domain | Entry point |
|-------|--------|-------------|
| devops | CI/CD · infrastructure · incident response | `agents.devops` |
| finance | Portfolio · market data · budget analysis | `agents.finance` |
| media | Content creation · metadata · distribution | `agents.media` |
| office | Document automation · scheduling · email | `agents.office` |
| social | Social media · content scheduling · cross-platform | `agents.social` |

## Architecture

```
src/
├── shared/       # agent loop + config (single source of truth)
│   ├── agent.py  # run(prompt, tools, handle_tool_call)
│   └── config.py # ANTHROPIC_API_KEY / ANTHROPIC_MODEL
└── agents/
    ├── devops/tools.py
    ├── finance/tools.py
    ├── media/tools.py
    ├── office/tools.py
    └── social/tools.py
```

Adding a new domain = create `agents/<name>/tools.py` + `__init__.py`. Zero changes to the loop.

## Setup

```bash
cp .env.example .env   # add ANTHROPIC_API_KEY
uv venv && uv pip install -e ".[dev]"
```

## Run

```bash
python examples/run_agent.py finance "Give me a Q1 budget summary"
python examples/run_agent.py devops "Check nginx service status"
```

## Test

```bash
pytest          # 30 tests: shared loop + per-agent tool checks
ruff check .
```
