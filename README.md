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

💡 How It Works
1.User Uploads Documents
2.IngestionAgent parses and chunks the content
3.RetrievalAgent embeds chunks and finds relevant context
4.LLMResponseAgent uses Gemini to generate an answer based on query and context
5.Streamlit UI displays the interaction

🛠 Technologies Used
🧠 Google Gemini API
🔎 FAISS (Facebook AI Similarity Search)
🧾 SentenceTransformers
🧰 Streamlit for frontend UI



Use Cases
AI-powered Document Assistants
Enterprise Knowledge Base Q&A
Legal, Research, or Academic Document Chatbots

## 🧱 System Requirements

- Python 3.8+
- pip

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Bvhnandan/Agentic-RAG-Chatbot-for-Multi-Format-Document-QA-using-Model-Context-Protocol.git
cd Agentic-RAG-Chatbot-for-Multi-Format-Document-QA-using-Model-Context-Protocol

Create Virtual Environment

python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

Install requirements
pip install -r requirements.txt

Set Google Gemini API Key
In agents/response.py, update the line with your API key:

Set your own api key
genai.configure(api_key="YOUR_GOOGLE_API_KEY")

Run the Application
streamlit run chatbot.py


👨‍💻 Author
Venkata Harsha Nandan Billala
🎓 Recent B.Tech Graduate | 📁 ML & AI Enthusiast


