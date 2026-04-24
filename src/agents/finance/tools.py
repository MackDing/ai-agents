"""Tool definitions for finance-agent."""
from typing import Any

TOOLS: list[dict] = [
    {
        "name": "get_stock_price",
        "description": "Fetch the latest price for a stock ticker symbol",
        "input_schema": {
            "type": "object",
            "properties": {
            "ticker": {"type": "string", "description": "Stock ticker, e.g. AAPL"},
            },
            "required": ['ticker'],
        },
    },
    {
        "name": "calculate_budget",
        "description": "Compute total, spent, and remaining amounts from a budget dict",
        "input_schema": {
            "type": "object",
            "properties": {
            "budget": {"type": "object", "description": "Map of category -> amount"},
            "spent": {"type": "object", "description": "Map of category -> spent"},
            },
            "required": ['budget', 'spent'],
        },
    },
    {
        "name": "summarize_csv_report",
        "description": "Read a CSV file and return summary statistics",
        "input_schema": {
            "type": "object",
            "properties": {
            "path": {"type": "string", "description": "Path to the CSV file"},
            },
            "required": ['path'],
        },
    },
]


def handle_tool_call(name: str, inputs: dict[str, Any]) -> dict[str, Any]:
    """Dispatch a tool call and return the result dict."""
    if name == "get_stock_price":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "calculate_budget":
        return {"result": f"[mock] {name} called with {inputs}"}
    if name == "summarize_csv_report":
        return {"result": f"[mock] {name} called with {inputs}"}
    return {"error": f"Unknown tool: {name}"}
