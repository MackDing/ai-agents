"""Tool definitions for social-agent."""
from typing import Any

TOOLS: list[dict] = [
    {
        "name": "draft_post",
        "description": "Draft a social media post for a given platform and topic",
        "input_schema": {
            "type": "object",
            "properties": {
            "platform": {"type": "string", "description": "Platform: 'twitter', 'linkedin', 'instagram'"},
            "topic": {"type": "string", "description": "What the post is about"},
            "tone": {"type": "string", "description": "Post tone: 'casual', 'professional', 'promotional'"},
            },
            "required": ['platform', 'topic'],
        },
    },
    {
        "name": "schedule_post",
        "description": "Schedule a post for publishing at a specific datetime",
        "input_schema": {
            "type": "object",
            "properties": {
            "content": {"type": "string", "description": "Post content"},
            "platform": {"type": "string", "description": "Target platform"},
            "publish_at": {"type": "string", "description": "ISO 8601 datetime string"},
            },
            "required": ['content', 'platform', 'publish_at'],
        },
    },
    {
        "name": "get_engagement_stats",
        "description": "Retrieve engagement metrics for recent posts",
        "input_schema": {
            "type": "object",
            "properties": {
            "platform": {"type": "string", "description": "Platform name"},
            "days": {"type": "integer", "description": "Number of days to look back"},
            },
            "required": ['platform'],
        },
    },
]


def handle_tool_call(name: str, inputs: dict[str, Any]) -> dict[str, Any]:
    """Dispatch a tool call and return the result dict."""
    if name == "draft_post":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "schedule_post":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "get_engagement_stats":
        return {"result": f"[mock] {name} called with {inputs}"}
    return {"error": f"Unknown tool: {name}"}
