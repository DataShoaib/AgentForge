# AgentForge 🤖

> **Production-Grade AI Agent** — LangChain · Tool Calling · RAG · FastAPI · Streamlit · Conversational Memory · Docker

[![FastAPI](https://img.shields.io/badge/FastAPI-Live-009688?logo=fastapi&logoColor=white)](https://ai-agent-latest-64mk.onrender.com/docs)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live-FF4B4B?logo=streamlit&logoColor=white)](https://agentforge-776mvmaaaugaj4wrnjjg8l.streamlit.app/)
[![LangSmith](https://img.shields.io/badge/LangSmith-Traces%20Live-1C3C3C?logo=langchain&logoColor=white)](https://smith.langchain.com/o/0271ca3a-725c-4a8c-b006-7b9d7d49a351/projects/p/4771effe-81a0-43e1-b90d-89952ce6d41a)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)](https://hub.docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🔗 Live Demos

| Service | URL |
|---|---|
| 🚀 FastAPI Backend | https://ai-agent-latest-64mk.onrender.com/chat |
| 💻 Streamlit Frontend | https://agentforge-776mvmaaaugaj4wrnjjg8l.streamlit.app/ |
| 🔍 LangSmith Traces | [View Live Agent Traces](https://smith.langchain.com/o/0271ca3a-725c-4a8c-b006-7b9d7d49a351/projects/p/4771effe-81a0-43e1-b90d-89952ce6d41a) |

---

## Overview

**AgentForge** is a modular, production-style AI Agent built to demonstrate real-world GenAI engineering practices.

The system implements an intelligent reasoning pipeline where the agent dynamically decides whether to answer directly from LLM knowledge, invoke an external tool (web search, calculator), or retrieve from an internal vector knowledge base — without any hardcoded routing logic. Every decision is made at runtime based on query semantics.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🧠 **Agentic Reasoning** | LangChain `AgentExecutor` with open-api tool calling agent decision making |
| 🔧 **Dynamic Tool Calling** | Web Search (Tavily), Calculator, RAG — selected contextually per query |
| 📚 **RAG Pipeline** | Document ingestion → chunking → FAISS vector store → semantic retrieval |
| 💬 **Conversational Memory** | Persistent multi-turn chat history via `ConversationBufferMemory` |
| 🌐 **FastAPI Backend** | production-ready REST API with Pydantic validation |
| 💻 **Streamlit Frontend** | Interactive chat UI |
| 🪵 **LangSmith Tracing** | Full observability — prompts, tool calls, outputs, and latency |
| 🐳 **Docker Support** | Containerized deployment with `.dockerignore` and environment isolation |

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        Streamlit UI                          │
│                    (ui/app.py — Port 8501)                   │
└─────────────────────────┬────────────────────────────────────┘
                          │  HTTP POST /chat
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
└──────────┬──────────────────┬───────────────┬───────────────┘
           │                  │               │
           ▼                  ▼               ▼
┌──────────────────┐ ┌───────────────┐ ┌──────────────────────┐
│   Search Tool    │ │  Calculator   │ │      RAG Tool        │
│  (Tavily API)    │ │     Tool      │ │   (FAISS + LLM)      │
└──────────────────┘ └───────────────┘ └──────────┬───────────┘
                                                   │
                                                   ▼
                                     ┌─────────────────────────┐
                                     │   FAISS Vector Store    │
                                     │  (Sentence Transformers │
                                     │     Embeddings)         │
                                     └─────────────────────────┘
```

---

## 🧭 Agent Decision-Making Flow

The agent evaluates every query through a reasoning phase before taking any action:

```
User Query
    │
    ▼
LLM Reasoning (ReAct Chain-of-Thought)
    │
    ├── Real-time data needed?   ──► Tavily Search Tool
    │
    ├── Math/calculation?        ──► Calculator Tool
    │
    ├── Internal documents?      ──► RAG Tool → FAISS Retrieval
    │
    └── General knowledge?       ──► Direct LLM Response
```

### Example Routing Decisions

| Query | Agent Decision | Tool Used |
|---|---|---|
| `"Explain transformer architecture"` | General knowledge | Direct LLM |
| `"Latest AI news today"` | Real-time data required | Tavily Search |
| `"Calculate 987 * 654"` | Math operation detected | Calculator |
| `"Summarize the internal documents"` | Internal retrieval needed | RAG + FAISS |
| `"What did we discuss earlier?"` | Context lookup | ConversationBufferMemory |

---

## 📦 RAG Pipeline

```
Raw Documents (data.txt)
        │
        ▼
   Text Chunking
  (RecursiveCharacterTextSplitter)
        │
        ▼
  Sentence Transformers Embeddings
        │
        ▼
  FAISS Vector Store (In-Memory Index)
        │
        ▼
  Similarity Search (Top-k Retrieval)
        │
        ▼
  Context Injection → LLM → Final Response
```

---

## 📁 Project Structure

```
AgentForge/
│
├── api/
│   └── main.py                  # FastAPI app — POST /chat endpoint
│
├── app/
│   ├── agent/
│   │   ├── agent.py             # AgentExecutor initialization (LLM + Tools + Memory)
│   │   ├── prompt.py            # System prompt and agent behavior rules
│   │   └── tools_registry.py   # Centralized tool registry (plug-and-play)
│   │
│   ├── config/
│   │   └── settings.py          # Environment variable management (pydantic-settings)
│   │
│   ├── memory/
│   │   └── memory.py            # ConversationBufferMemory management
│   │
│   ├── rag/
│   │   ├── chunking.py          # RecursiveCharacterTextSplitter config
│   │   ├── embeddings.py        # Sentence Transformers embedding model
│   │   ├── loader.py            # Document loading from data.txt
│   │   ├── retriever.py         # Semantic similarity retrieval
│   │   └── vectorstore.py       # FAISS index creation and persistence
│   │
│   ├── schema/
│   │   └── response.py          # Pydantic request/response models
│   │
│   ├── tools/
│   │   ├── calculator.py        # Math/arithmetic tool
│   │   ├── rag.py               # FAISS semantic retrieval tool
│   │   └── search.py            # Tavily web search integration
│   │
│   └── utils/
│       └── logger.py            # Structured logging utilities
│
├── ui/                          # Streamlit chat interface
├── data.txt                     # Source documents for RAG knowledge base
├── Dockerfile
├── .dockerignore
├── .env                         # API keys (not committed)
├── pyproject.toml               # uv dependency management
├── uv.lock
└── README.md
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | Groq (LLaMA 3) / OpenAI GPT |
| **Agent Framework** | LangChain AgentExecutor  |
| **Vector Database** | FAISS (CPU) |
| **Embeddings** | Sentence Transformers |
| **Web Search** | Tavily Search API |
| **Backend** | FastAPI + Uvicorn |
| **Frontend** | Streamlit |
| **Observability** | LangSmith |
| **Validation** | Pydantic v2 |
| **Package Manager** | uv |
| **Containerization** | Docker |
| **Language** | Python 3.11+ |

---

## ⚡ Quickstart

### Option 1 — Local (uv)

```bash
# 1. Clone the repo
git clone https://github.com/DataShoaib/AgentForge.git
cd AgentForge

# 2. Install uv (if not installed)
pip install uv

# 3. Install dependencies
uv sync

# 4. Configure environment
cp .env.example .env
# Fill in your API keys in .env

# 5. Run the backend
uvicorn api.main:app --reload
# → http://localhost:8000

# 6. Run the frontend (new terminal)
streamlit run ui/app.py
# → http://localhost:8501
```

### Option 2 — Docker

```bash
# Build image
docker build -t agentforge .

# Run container
docker run -p 8000:8000 --env-file .env agentforge
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
# LLM Provider (choose one)
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key

# Tools
TAVILY_API_KEY=your_tavily_api_key

# Observability
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=AgentForge
```

---

## 📡 API Reference

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
  "answer": "Retrieval-Augmented Generation (RAG) is a technique that combines..."
}
```

**Try it live:**
```bash
curl -X POST https://ai-agent-latest-64mk.onrender.com/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is LangChain?"}'
```

---

## 🔭 Observability — LangSmith

All agent runs are traced end-to-end in LangSmith, capturing:

- Full prompt construction and system context
- Tool selection reasoning (chain-of-thought)
- Tool inputs and outputs per call
- LLM response and token usage
- End-to-end latency per request

**Live Project Dashboard →** [LangSmith Traces](https://smith.langchain.com/o/0271ca3a-725c-4a8c-b006-7b9d7d49a351/projects/p/4771effe-81a0-43e1-b90d-89952ce6d41a)

---

## ✅ Production Concepts Demonstrated

- Modular architecture with clean separation of concerns (`agent/`, `tools/`, `rag/`, `memory/`, `schema/`)
- Agentic reasoning with dynamic, runtime tool selection
- Full RAG pipeline — ingestion, chunking, embedding, indexing, retrieval
- Conversational memory for multi-turn coherence
- FastAPI backend with Pydantic v2 validation
- LangSmith observability and full trace logging
- Dockerized deployment with environment isolation
- `uv` for fast, reproducible dependency management

---

## 🗺️ Roadmap

- [ ] LangGraph multi-agent orchestration
- [ ] PDF and multi-format document ingestion
- [ ] Async parallel tool execution
- [ ] Persistent database-backed memory (PostgreSQL / Redis)
- [ ] Authentication and rate limiting middleware
- [ ] Hybrid BM25 + dense retrieval (EnsembleRetriever)
- [ ] Evaluation suite with RAGAS metrics

---

## 👤 Author

**Md Shoaib Akhtar**
B.Tech — Artificial Intelligence & Data Science
GitHub: [@DataShoaib](https://github.com/DataShoaib) · Portfolio: [datashoaib.github.io](https://datashoaib.github.io)

---.
