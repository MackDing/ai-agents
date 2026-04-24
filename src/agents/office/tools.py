"""Tool definitions for office-agent."""
from typing import Any

TOOLS: list[dict] = [
    {
        "name": "read_text_file",
        "description": "Read and return the contents of a text file",
        "input_schema": {
            "type": "object",
            "properties": {
            "path": {"type": "string", "description": "Path to the file"},
            },
            "required": ['path'],
        },
    },
    {
        "name": "draft_email",
        "description": "Draft a professional email given subject, recipient, and key points",
        "input_schema": {
            "type": "object",
            "properties": {
            "to": {"type": "string", "description": "Recipient name"},
            "subject": {"type": "string", "description": "Email subject"},
            "points": {"type": "array", "description": "Key points to cover"},
            },
            "required": ['to', 'subject', 'points'],
        },
    },
    {
        "name": "create_meeting_agenda",
        "description": "Generate a structured meeting agenda",
        "input_schema": {
            "type": "object",
            "properties": {
            "title": {"type": "string", "description": "Meeting title"},
            "duration_minutes": {"type": "integer", "description": "Total meeting duration"},
            "topics": {"type": "array", "description": "List of agenda topics"},
            },
            "required": ['title', 'duration_minutes', 'topics'],
        },
    },
]


def handle_tool_call(name: str, inputs: dict[str, Any]) -> dict[str, Any]:
    """Dispatch a tool call and return the result dict."""
    if name == "read_text_file":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "draft_email":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "create_meeting_agenda":
        return {"result": f"[mock] {name} called with {inputs}"}
    return {"error": f"Unknown tool: {name}"}
