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

---

## 🦞 OPC Ecosystem

Part of the [OPC (One-Person Company)](https://opc.ren) open-source ecosystem by [Mack Ding](https://github.com/MackDing):

| Project | Description |
|---------|-------------|
| [awesome-ai-api](https://github.com/MackDing/awesome-ai-api) | Curated list of 200+ AI API providers with daily ranking |
| [CodexClaw](https://github.com/MackDing/CodexClaw) | Telegram bot for Claude Code & Codex CLI |
| [ai-agents](https://github.com/MackDing/ai-agents) | AI agent fleet — devops, finance, media, office, social |
| [opc-daily-signal](https://github.com/MackDing/opc-daily-signal) | Daily decision intelligence for OPC founders |
| [claude-context-health](https://github.com/MackDing/claude-context-health) | Context health diagnostic guide for Claude Code |
| [doc-preprocess-hub](https://github.com/MackDing/doc-preprocess-hub) | Enterprise document preprocessing platform |
