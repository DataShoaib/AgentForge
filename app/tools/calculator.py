from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluate math expression."""
    return str(eval(expression))