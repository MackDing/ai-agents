"""Office agent — wraps shared loop with domain-specific tools."""
from shared.agent import run as _run
from .tools import TOOLS, handle_tool_call


def run(prompt: str) -> str:
    """Run the office agent."""
    return _run(prompt, TOOLS, handle_tool_call)
