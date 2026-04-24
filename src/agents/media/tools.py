"""Tool definitions for media-agent."""
from typing import Any

TOOLS: list[dict] = [
    {
        "name": "extract_file_metadata",
        "description": "Return basic metadata (size, type, modified) for a media file",
        "input_schema": {
            "type": "object",
            "properties": {
            "path": {"type": "string", "description": "Path to the media file"},
            },
            "required": ['path'],
        },
    },
    {
        "name": "generate_caption",
        "description": "Generate an AI caption for an image given its path",
        "input_schema": {
            "type": "object",
            "properties": {
            "image_path": {"type": "string", "description": "Path to the image file"},
            "style": {"type": "string", "description": "Caption style: 'social', 'formal', 'creative'"},
            },
            "required": ['image_path'],
        },
    },
    {
        "name": "list_media_files",
        "description": "List all media files in a directory by extension",
        "input_schema": {
            "type": "object",
            "properties": {
            "directory": {"type": "string", "description": "Directory to scan"},
            "extensions": {"type": "array", "description": "e.g. ['.jpg', '.mp4']"},
            },
            "required": ['directory'],
        },
    },
]


def handle_tool_call(name: str, inputs: dict[str, Any]) -> dict[str, Any]:
    """Dispatch a tool call and return the result dict."""
    if name == "extract_file_metadata":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "generate_caption":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "list_media_files":
        return {"result": f"[mock] {name} called with {inputs}"}
    return {"error": f"Unknown tool: {name}"}
