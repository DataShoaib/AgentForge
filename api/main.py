from pydantic import BaseModel
from fastapi import FastAPI
from dotenv import load_dotenv

from app.agent.agent import build_agent
from app.schema.response import AgentResponse

load_dotenv()

app = FastAPI(
    title="AI Agent API",
    version="1.0",
    description="API for AI Agent built with LangChain and Groq"
)

agent = None


def get_agent():
    global agent

    if agent is None:
        agent = build_agent()

    return agent


class AgentRequest(BaseModel):
    question: str


@app.get("/")
async def root():
    return {"message": "Welcome to the AI Agent API"}


@app.post("/chat")
async def chat(req: AgentRequest):

    agent_instance = get_agent()

    response = agent_instance.invoke(
        {
            "input": req.question,
            "chat_history": []
        }
    )

    return AgentResponse(
        answer=response["output"]
    )