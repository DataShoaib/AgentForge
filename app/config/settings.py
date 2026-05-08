import os
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0

LANGCHAIN_TRACING_V2 = "true"
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")