import uuid
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class RetrievalAgent:
    def __init__(self, embedding_model="all-MiniLM-L6-v2"):
        self.embedding_model = SentenceTransformer(embedding_model)
        self.index = None
        self.chunk_map = {}

    def get_embedding(self, text):
        emb = self.embedding_model.encode(text)
        return np.array(emb)

    def build_index(self, ingestion_messages):
        vectors = []
        chunk_id = 0

        for msg in ingestion_messages:
            filename = msg['payload']['filename']
            for chunk in msg['payload']['chunks']:
                emb = self.get_embedding(chunk)
                vectors.append(emb)
                self.chunk_map[chunk_id] = {"text": chunk, "filename": filename}
                chunk_id += 1

        dim = len(vectors[0])
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(np.array(vectors).astype("float32"))

    def retrieve(self, query, top_k=3):
        query_emb = self.get_embedding(query).astype("float32").reshape(1, -1)
        distances, indices = self.index.search(query_emb, top_k)

        top_chunks = []
        for idx in indices[0]:
            if idx in self.chunk_map:
                top_chunks.append(self.chunk_map[idx]["text"])

        mcp_message = {
            "sender": "RetrievalAgent",
            "receiver": "LLMResponseAgent",
            "type": "RETRIEVAL_RESULT",
            "trace_id": str(uuid.uuid4()),
            "payload": {
                "retrieved_context": top_chunks,
                "query": query
            }
        }
        return mcp_message
