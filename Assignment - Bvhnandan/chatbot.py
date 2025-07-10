import streamlit as st
from agents.ingestion import IngestionAgent
from agents.retrieval import RetrievalAgent
from agents.response import LLMResponseAgent

st.set_page_config(page_title="Agentic RAG Chatbot")

st.title("📄 Upload your documents in the below formats")

uploaded_files = st.file_uploader(
    "Supported formats: PDF, DOCX, PPTX, CSV, TXT, Markdown",
    type=["pdf", "docx", "pptx", "csv", "txt", "md"],
    accept_multiple_files=True
)

if uploaded_files:
    if st.button("📥 Process Documents"):
        # Call ingestion as a function now
        st.session_state["ingestion_messages"] = IngestionAgent(uploaded_files)

        # Initialize retriever and LLM
        st.session_state["retriever"] = RetrievalAgent()
        st.session_state["retriever"].build_index(st.session_state["ingestion_messages"])
        st.session_state["llm_agent"] = LLMResponseAgent()

        st.success("✅ Documents processed and agents initialized!")

st.divider()
st.subheader("💬 Ask Questions Based on Uploaded Documents")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.chat_input("Type your question...")

if user_input:
    if "retriever" not in st.session_state or "llm_agent" not in st.session_state:
        st.warning("Please upload and process documents first.")
    else:
        st.session_state["messages"].append({"role": "user", "content": user_input})

        retrieval_message = st.session_state["retriever"].retrieve(user_input)

        response_message = st.session_state["llm_agent"].generate_answer(retrieval_message)
        answer = response_message["payload"]["answer"]
        source_chunks = response_message["payload"]["source_chunks"]

        st.session_state["messages"].append({"role": "assistant", "content": answer})

        for msg in st.session_state["messages"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        with st.expander("📄 View Source Context Used"):
            for i, chunk in enumerate(source_chunks, 1):
                st.markdown(f"**Chunk {i}:** {chunk}")
