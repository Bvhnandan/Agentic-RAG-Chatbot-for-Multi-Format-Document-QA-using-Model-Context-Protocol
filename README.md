# 🤖 Agentic RAG Chatbot for Multi-Format Document QA using Model Context Protocol

This project implements a Retrieval-Augmented Generation (RAG)-based chatbot that can answer questions based on **uploaded documents** (PDF, DOCX, PPTX, CSV, TXT, MD). It uses an **Agentic Architecture** where agents communicate using a custom **Message Communication Protocol (MCP)**.

---

## 🚀 Features

- 🔍 Document Ingestion & Parsing (Multi-format support)
- 🧩 Retrieval using FAISS and Sentence Transformers
- 🧠 LLM Answer Generation using Gemini
- 💬 Streamlit Chat UI
- 📦 Agent-based modular architecture with traceable communication (via MCP)

---

## 🧠 Architecture Overview
[Upload Documents] 
        ↓
[IngestionAgent → Parsing + Chunking]
        ↓
[RetrievalAgent → Embedding + FAISS Index]
        ↓
[LLMResponseAgent → Gemini API]
        ↓
[Streamlit Chat UI → Answer + Source Context]

Multi-agents

| Agent                | Responsibility                                                         |
| -------------------- | ---------------------------------------------------------------------- |
| **IngestionAgent**   | Parses uploaded documents and chunks the content                       |
| **RetrievalAgent**   | Embeds chunks and retrieves top matches using FAISS                    |
| **LLMResponseAgent** | Sends query + retrieved context to Gemini and returns the final answer |
| **Chat UI**          | Streamlit interface to upload files and chat with the system           |

Message Communication Protocol (MCP)
All communication between agents is done via a standard MCP message structure:
{
  "sender": "IngestionAgent",
  "receiver": "RetrievalAgent",
  "type": "DOCUMENT_INGESTED",
  "trace_id": "uuid-123",
  "payload": {
    "filename": "abc.pdf",
    "chunks": ["chunk1 text...", "chunk2 text..."]
  }
}

Supported Document Formats
.pdf, .docx, .pptx, .csv, .txt, .md

 Use Cases
AI-powered Document Assistants
Enterprise Knowledge Base Q&A
Legal, Research, or Academic Document Chatbots

👨‍💻 Author
Venkata Harsha Nandan Billala
🎓 Recent B.Tech Graduate | 📁 ML & AI Enthusiast


