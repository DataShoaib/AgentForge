from app.tools.calculator import calculator
from app.tools.search import get_search_tool
from app.tools.rag import rag_tool

def get_tools(retriever=None):
    tools = [calculator, get_search_tool(), rag_tool]
    return tools