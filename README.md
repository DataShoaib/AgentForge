# AgentForge 🤖

> **Production-Grade AI Agent** — LangChain · Tool Calling · RAG · FastAPI · Streamlit · Conversational Memory

[![LangSmith Traces](https://img.shields.io/badge/LangSmith-Traces%20Live-green?logo=langchain)](https://smith.langchain.com/o/0271ca3a-725c-4a8c-b006-7b9d7d49a351/projects/p/982d144e-fcd1-42b7-9931-afcdc41761c7)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-teal?logo=fastapi)](https://fastapi.tiangolo.com)
[![LangChain](https://img.shields.io/badge/LangChain-AgentExecutor-orange)](https://langchain.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## Overview

**AgentForge** is a modular, production-style AI Agent framework built to demonstrate real-world GenAI engineering practices.

The system implements an intelligent reasoning pipeline where the agent dynamically decides whether to answer directly, invoke a tool, or retrieve from an internal knowledge base — rather than using hardcoded logic.

**Live LangSmith Tracing →** [View Agent Traces](https://smith.langchain.com/o/0271ca3a-725c-4a8c-b006-7b9d7d49a351/projects/p/982d144e-fcd1-42b7-9931-afcdc41761c7)

---

## Key Features

| Feature | Description |
|---|---|
| 🧠 **Agentic Reasoning** | LangChain `AgentExecutor` with ReAct-style decision making |
| 🔧 **Dynamic Tool Calling** | Web Search, Calculator, RAG — selected contextually per query |
| 📚 **RAG Pipeline** | Document ingestion → chunking → FAISS vector store → semantic retrieval |
| 💬 **Conversational Memory** | Persistent chat history across multi-turn conversations |
| ⚡ **Streaming Responses** | Real-time token streaming for smooth UX |
| 🌐 **FastAPI Backend** | Async, production-ready REST API layer |
| 💻 **Streamlit Frontend** | Interactive chat UI with history support |
| 🪵 **LangSmith Tracing** | Full observability — prompts, tool calls, outputs, latency |

---

## System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        Streamlit UI                          │
│                    (ui/app.py — Port 8501)                   │
└─────────────────────────┬────────────────────────────────────┘
                          │  HTTP
                          ▼
┌──────────────────────────────────────────────────────────────┐
│                    FastAPI Backend                           │
│                  (api/main.py — Port 8000)                   │
└─────────────────────────┬────────────────────────────────────┘
                          │
                          ▼
┌──────────────────────────────────────────────────────────────┐
│               LangChain AgentExecutor Core                   │
│                                                              │
│    System Prompt → LLM Reasoning → Tool Decision → Response  │
│                                                              │
│    Memory: ConversationBufferMemory (multi-turn context)     │
└────────────┬─────────────────┬────────────────┬─────────────┘
             │                 │                │
             ▼                 ▼                ▼
  ┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
  │   Search Tool    │ │  Calculator  │ │     RAG Tool     │
  │  (Tavily API)    │ │    Tool      │ │  (FAISS + LLM)   │
  └──────────────────┘ └──────────────┘ └────────┬─────────┘
                                                  │
                                                  ▼
                                      ┌───────────────────────┐
                                      │   FAISS Vector Store  │
                                      │  (OpenAI Embeddings)  │
                                      └───────────────────────┘
```

---

## Agent Decision-Making Workflow

The agent evaluates every query through a reasoning phase before selecting an action:

```
User Query
    │
    ▼
LLM Reasoning Phase
    │
    ├─── Real-time data needed?  ──► Tavily Search Tool
    │
    ├─── Math operation?         ──► Calculator Tool
    │
    ├─── Internal documents?     ──► RAG Tool → FAISS Retrieval
    │
    └─── General knowledge?      ──► Direct LLM Response
```

### Example Routing Decisions

| Query | Agent Decision | Tool Used |
|---|---|---|
| `"Explain transformer architecture"` | General knowledge | Direct LLM |
| `"Latest AI news today"` | Real-time data required | Tavily Search |
| `"Calculate 987 * 654"` | Math operation detected | Calculator |
| `"Summarize my internal documents"` | Internal retrieval needed | RAG + FAISS |
| `"What did we discuss earlier?"` | Memory lookup | ConversationBufferMemory |

---

## RAG Pipeline

```
Raw Documents (data.txt)
        │
        ▼
   Text Chunking
  (RecursiveCharacterTextSplitter)
        │
        ▼
  OpenAI Embeddings
        │
        ▼
  FAISS Vector Store
        │
        ▼
  Similarity Search (Top-k)
        │
        ▼
  Context Injection → LLM → Final Response
```

---

## Project Structure

```
AgentForge/
│
├── app/
│   ├── agent/
│   │   ├── builder.py           # AgentExecutor initialization (LLM + Tools + Memory)
│   │   ├── prompt.py            # System prompt and agent behavior rules
│   │   └── tools_registry.py   # Centralized tool registry (plug-and-play)
│   │
│   ├── tools/
│   │   ├── search.py            # Tavily web search integration
│   │   ├── calculator.py        # Math/arithmetic tool
│   │   └── rag_tool.py          # FAISS semantic retrieval tool
│   │
│   ├── memory/
│   │   └── memory.py            # ConversationBufferMemory management
│   │
│   ├── rag/
│   │   ├── loader.py            # Document loading
│   │   ├── vectorstore.py       # Embedding + FAISS indexing
│   │   └── retriever.py         # Semantic similarity retrieval
│   │
│   ├── schemas/
│   │   └── response.py          # Pydantic request/response models
│   │
│   ├── config/
│   │   └── settings.py          # Environment variable management
│   │
│   └── utils/
│       └── logger.py            # Structured logging utilities
│
├── api/
│   └── main.py                  # FastAPI app — POST /chat endpoint
│
├── ui/
│   └── app.py                   # Streamlit chat interface
│
├── data.txt                     # Source documents for RAG
├── requirements.txt
├── .env
└── README.md
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | OpenAI GPT |
| **Agent Framework** | LangChain AgentExecutor |
| **Vector Database** | FAISS |
| **Embeddings** | OpenAI Embeddings |
| **Web Search** | Tavily Search API |
| **Backend** | FastAPI (Async) |
| **Frontend** | Streamlit |
| **Observability** | LangSmith |
| **Validation** | Pydantic |
| **Language** | Python 3.10+ |

---

## Quickstart

### 1. Clone & Setup

```bash
git clone https://github.com/DataShoaib/AgentForge.git
cd AgentForge
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment

```env
# .env
OPENAI_API_KEY=your_openai_key
TAVILY_API_KEY=your_tavily_key
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=AgentForge
```

### 3. Run Backend

```bash
uvicorn api.main:app --reload
# Running at http://localhost:8000
```

### 4. Run Frontend

```bash
streamlit run ui/app.py
# Running at http://localhost:8501
```

---

## API Reference

### `POST /chat`

**Request**
```json
{
  "question": "What is retrieval-augmented generation?"
}
```

**Response**
```json
{
  "answer": "Retrieval-Augmented Generation (RAG) is a technique..."
}
```

---

## Observability — LangSmith

All agent runs are traced end-to-end in LangSmith, capturing:

- Full prompt construction
- Tool selection reasoning
- Tool inputs and outputs
- LLM response and token usage
- End-to-end latency

**Live Project Dashboard →** [LangSmith Traces](https://smith.langchain.com/o/0271ca3a-725c-4a8c-b006-7b9d7d49a351/projects/p/982d144e-fcd1-42b7-9931-afcdc41761c7)

---

## Production Concepts Demonstrated

- ✅ Modular, separation-of-concerns architecture
- ✅ Agentic reasoning with dynamic tool selection
- ✅ Full RAG pipeline with vector similarity search
- ✅ Conversational memory for multi-turn coherence
- ✅ Async FastAPI backend with Pydantic validation
- ✅ Real-time token streaming
- ✅ LangSmith observability and tracing
- ✅ Clean API layer isolation

---

## Roadmap

- [ ] LangGraph multi-agent orchestration
- [ ] PDF and multi-format document ingestion
- [ ] Async parallel tool execution
- [ ] Docker + Docker Compose deployment
- [ ] Persistent database-backed memory
- [ ] Authentication and rate limiting
- [ ] Voice interface integration

---

## Author

**Md Shoaib Akhtar**  
B.Tech — Artificial Intelligence & Data Science  
GitHub: [@DataShoaib](https://github.com/DataShoaib)

---

## License

MIT License — see [LICENSE](LICENSE) for details.