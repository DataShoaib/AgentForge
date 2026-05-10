from langchain.tools import tool

from app.rag.loader import load_documents
from app.rag.chunking import chunk_documents
from app.rag.vectorstore import create_vectorstore
from app.rag.retriever import create_retriever
from app.rag.embeddings import get_embedding

from app.utils.logger import logger


logger.info("Initializing RAG Pipeline...")

documents = load_documents("data.txt")

chunks = chunk_documents(documents)

embedding = get_embedding()

vectorstore = create_vectorstore(chunks, embedding)

retriever = create_retriever(vectorstore, k=4)

logger.info("RAG Pipeline Ready.")


@tool("RAGTool")
def rag_tool(query: str) -> str:
    """
    Use this tool to answer questions from documents.
    """

    logger.info(f"RAG Tool Called: {query}")

    docs = retriever.invoke(query)

    if not docs:
        return "No relevant documents found."

    response = "\n\n".join([doc.page_content for doc in docs])

    logger.info("Documents retrieved successfully.")

    return response