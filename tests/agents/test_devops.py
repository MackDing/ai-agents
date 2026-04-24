"""Tools tests for devops agent."""
from agents.devops.tools import TOOLS, handle_tool_call


def test_tools_not_empty():
    assert len(TOOLS) > 0


def test_tools_have_required_fields():
    for tool in TOOLS:
        assert "name" in tool
        assert "description" in tool
        assert "input_schema" in tool


def test_handle_known_tool_returns_dict():
    result = handle_tool_call("run_shell_command", {})
    assert isinstance(result, dict)


def test_handle_unknown_tool_returns_error():
    result = handle_tool_call("nonexistent_tool", {})
    assert "error" in result
