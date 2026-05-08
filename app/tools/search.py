from langchain_community.tools import TavilySearchResults
from app.utils.logger import logger


def get_search_tool(max_results=3):

    logger.info("Initializing Tavily search tool...")

    search_tool = TavilySearchResults(max_results=max_results)
    logger.info("Search tool initialized successfully.")

    return search_tool