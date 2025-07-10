import uuid
import google.generativeai as genai

genai.configure(api_key="Write your API key here")

class LLMResponseAgent:
    def __init__(self, model="models/gemini-1.5-flash"):
        self.model = genai.GenerativeModel(model)

    def generate_answer(self, retrieval_message):
        query = retrieval_message["payload"]["query"]
        context_chunks = retrieval_message["payload"]["retrieved_context"]

        context = "\n\n".join(context_chunks)

        prompt = f"""
You are a helpful assistant. Use the below context to answer the user question.

Context:
{context}

Question: {query}
Answer:
"""

        response = self.model.generate_content(prompt)
        answer = response.text.strip()

        return {
            "sender": "LLMResponseAgent",
            "receiver": "ChatUI",
            "type": "FINAL_ANSWER",
            "trace_id": retrieval_message["trace_id"],
            "payload": {
                "answer": answer,
                "source_chunks": context_chunks,
                "query": query
            }
        }