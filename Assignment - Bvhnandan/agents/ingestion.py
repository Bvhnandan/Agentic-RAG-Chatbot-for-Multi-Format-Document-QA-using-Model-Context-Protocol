import uuid
from utils.parser import parse_file

def IngestionAgent(uploaded_files):
    messages = []

    for file in uploaded_files:
        try:
            content = parse_file(file)
            chunks = chunk_text(content)

            mcp_message = {
                "sender": "IngestionAgent",
                "receiver": "RetrievalAgent",
                "type": "DOCUMENT_INGESTED",
                "trace_id": str(uuid.uuid4()),
                "payload": {
                    "filename": file.name,
                    "chunks": chunks
                }
            }

            messages.append(mcp_message)
        except Exception as e:
            print(f"Error processing {file.name}: {e}")

    return messages

def chunk_text(text, chunk_size=500):
    # Simple fixed-length chunking (can be improved later)
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
