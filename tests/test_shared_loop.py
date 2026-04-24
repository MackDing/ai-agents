"""Shared loop tests — parametrized across all 5 agents."""
import json
from collections.abc import Callable
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from shared.config import Settings

# ── helpers ──────────────────────────────────────────────────────────────────

def _text_block(text: str = "reply") -> MagicMock:
    b = MagicMock()
    b.type = "text"
    b.text = text
    return b


def _tool_block(name: str = "noop", tool_id: str = "tu_001") -> MagicMock:
    b = MagicMock()
    b.type = "tool_use"
    b.id = tool_id
    b.name = name
    b.input = {}
    return b


def _response(stop_reason: str, blocks: list) -> MagicMock:
    r = MagicMock()
    r.stop_reason = stop_reason
    r.content = blocks
    return r


def _run_shared(responses: list, tools: list | None = None, handler: Callable | None = None):
    """Run shared.agent.run with mocked Anthropic client."""
    tools = tools or []
    handler = handler or (lambda name, inputs: {"result": "ok"})
    mock_client = MagicMock()
    mock_client.messages.create.side_effect = responses
    with (
        patch("shared.agent.load_settings", return_value=Settings(api_key="k", model="m")),
        patch("shared.agent.anthropic.Anthropic", return_value=mock_client),
    ):
        from shared.agent import run
        return run("hello", tools, handler), mock_client


# ── shared loop tests ─────────────────────────────────────────────────────────

def test_end_turn_single_text():
    result, _ = _run_shared([_response("end_turn", [_text_block("hi")])])
    assert result == "hi"


def test_end_turn_multiple_text_blocks():
    result, _ = _run_shared([_response("end_turn", [_text_block("a"), _text_block("b")])])
    assert result == "a\nb"


def test_end_turn_no_text_returns_empty():
    b = MagicMock()
    b.type = "image"
    result, _ = _run_shared([_response("end_turn", [b])])
    assert result == ""


def test_tool_use_then_end_turn():
    result, client = _run_shared([
        _response("tool_use", [_tool_block()]),
        _response("end_turn", [_text_block("done")]),
    ])
    assert result == "done"
    assert client.messages.create.call_count == 2


def test_tool_exception_becomes_error_result():
    tool_response = _response("tool_use", [_tool_block("boom")])
    final = _response("end_turn", [_text_block("ok")])
    mock_client = MagicMock()
    mock_client.messages.create.side_effect = [tool_response, final]

    def exploding_handler(name: str, inputs: dict) -> dict:
        raise ValueError("boom!")

    with (
        patch("shared.agent.load_settings", return_value=Settings(api_key="k", model="m")),
        patch("shared.agent.anthropic.Anthropic", return_value=mock_client),
    ):
        from shared.agent import run
        result = run("hi", [], exploding_handler)

    assert result == "ok"
    call_msgs = mock_client.messages.create.call_args_list[1][1]["messages"]
    payload = json.loads(call_msgs[-1]["content"][0]["content"])
    assert "error" in payload


def test_api_error_raises_runtime_error():
    import anthropic as _anthropic

    mock_client = MagicMock()
    mock_client.messages.create.side_effect = _anthropic.APIStatusError(
        "rate limited", response=MagicMock(status_code=429), body={}
    )
    with (
        patch("shared.agent.load_settings", return_value=Settings(api_key="k", model="m")),
        patch("shared.agent.anthropic.Anthropic", return_value=mock_client),
    ):
        from shared.agent import run
        with pytest.raises(RuntimeError, match="Anthropic API error"):
            run("hello", [], lambda n, i: {})


def test_max_turns_raises():
    from shared.agent import MAX_TURNS

    mock_client = MagicMock()
    mock_client.messages.create.return_value = _response("tool_use", [_tool_block()])
    with (
        patch("shared.agent.load_settings", return_value=Settings(api_key="k", model="m")),
        patch("shared.agent.anthropic.Anthropic", return_value=mock_client),
    ):
        from shared.agent import run
        with pytest.raises(RuntimeError, match="exceeded"):
            run("loop", [], lambda n, i: {})
    assert mock_client.messages.create.call_count == MAX_TURNS


def test_unexpected_stop_reason_raises():
    mock_client = MagicMock()
    mock_client.messages.create.return_value = _response("stop", [])
    with (
        patch("shared.agent.load_settings", return_value=Settings(api_key="k", model="m")),
        patch("shared.agent.anthropic.Anthropic", return_value=mock_client),
    ):
        from shared.agent import run
        with pytest.raises(RuntimeError, match="Unexpected stop_reason"):
            run("hello", [], lambda n, i: {})


def test_config_reads_model_from_env(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    monkeypatch.setenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")
    from importlib import reload
    import shared.config as cfg
    reload(cfg)
    s = cfg.load_settings()
    assert s.model == "claude-haiku-4-5-20251001"
