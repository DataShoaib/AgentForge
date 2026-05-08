from langchain_core.prompts import ChatPromptTemplate
from app.utils.logger import logger

def get_agent_prompt():
    logger.info('Loading agent prompt template...')
    return ChatPromptTemplate.from_messages([
        ("system", """
You are an advanced AI agent.

Rules:
- Think step-by-step
- Use tools when required
- Do not hallucinate
- Prefer factual sources
- Be concise but accurate
"""),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}")
    ])