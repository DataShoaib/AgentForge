from langchain_core.runnables import chain
from pydantic import BaseModel 
from fastapi import FastAPI
from app.agent.agent import build_agent
from app.schema.response import AgentResponse



app=FastAPI(title='AI Agent API',version='1.0',description='API for AI Agent built with LangChain and Groq')
agent=build_agent()

class AgentRequest(BaseModel):
    question:str

@app.get('/')
async def root():
    return {"message": "Welcome to the AI Agent API"}

@app.post("/chat")
async def chat(req: AgentRequest):

    response = agent.invoke({
        "input": req.question,
        "chat_history": []
    })

    return AgentResponse(
        answer=response["output"]
    )