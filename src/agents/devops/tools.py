"""Tool definitions for devops-agent."""
from typing import Any

TOOLS: list[dict] = [
    {
        "name": "run_shell_command",
        "description": "Run a shell command and return stdout",
        "input_schema": {
            "type": "object",
            "properties": {
            "command": {"type": "string", "description": "The shell command to execute"},
            },
            "required": ['command'],
        },
    },
    {
        "name": "check_service_status",
        "description": "Check whether a named service is running",
        "input_schema": {
            "type": "object",
            "properties": {
            "service_name": {"type": "string", "description": "The service name"},
            },
            "required": ['service_name'],
        },
    },
    {
        "name": "parse_log_file",
        "description": "Read and return the last N lines of a log file",
        "input_schema": {
            "type": "object",
            "properties": {
            "path": {"type": "string", "description": "Absolute path to the log file"},
            "lines": {"type": "integer", "description": "Number of tail lines to return"},
            },
            "required": ['path'],
        },
    },
]


def handle_tool_call(name: str, inputs: dict[str, Any]) -> dict[str, Any]:
    """Dispatch a tool call and return the result dict."""
    if name == "run_shell_command":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "check_service_status":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "parse_log_file":
        return {"result": f"[mock] {name} called with {inputs}"}
    return {"error": f"Unknown tool: {name}"}
