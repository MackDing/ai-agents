"""Shared agent loop — used by all domain agents."""
import json
from collections.abc import Callable
from typing import Any

import anthropic

from .config import load_settings

MAX_TURNS = 20


def run(
    prompt: str,
    tools: list[dict],
    handle_tool_call: Callable[[str, dict[str, Any]], dict[str, Any]],
) -> str:
    """Run the agent with the given prompt and return the final text response."""
    settings = load_settings()
    client = anthropic.Anthropic(api_key=settings.api_key)
    messages: list[dict] = [{"role": "user", "content": prompt}]

    for _ in range(MAX_TURNS):
        try:
            response = client.messages.create(
                model=settings.model,
                max_tokens=4096,
                tools=tools,
                messages=messages,
            )
        except anthropic.APIError as exc:
            raise RuntimeError(f"Anthropic API error: {exc}") from exc

        if response.stop_reason == "end_turn":
            return "\n".join(
                block.text for block in response.content if block.type == "text"
            )

        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    try:
                        result = handle_tool_call(block.name, block.input)
                        content = json.dumps(result)
                    except Exception as exc:
                        content = json.dumps({"error": str(exc)})
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": content,
                    })
            messages.append({"role": "user", "content": tool_results})
            continue

        raise RuntimeError(f"Unexpected stop_reason: {response.stop_reason}")

    raise RuntimeError(f"Agent exceeded {MAX_TURNS} turns without completing")
