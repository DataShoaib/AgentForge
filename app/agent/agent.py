from langchain.agents import create_openai_tools_agent, AgentExecutor
from langchain_groq import ChatGroq
from app.rag import retriever
from langchain_groq import ChatGroq

from app.agent.prompt import get_agent_prompt
from app.agent.tools_registry import get_tools
from app.memory.memory import get_memory
from app.config.settings import MODEL_NAME, TEMPERATURE


def build_agent():

    llm = ChatGroq(
          model=MODEL_NAME,
          temperature=TEMPERATURE
    )

    tools = get_tools()
    prompt = get_agent_prompt()
    memory = get_memory()

    agent = create_openai_tools_agent(llm, tools, prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True
    )