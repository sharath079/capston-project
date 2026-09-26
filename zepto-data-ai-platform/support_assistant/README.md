# Support Assistant Module

This module builds a GenAI-powered support assistant for Zepto policies.

## Steps
1. Place the eight policy documents in `/support_assistant/docs/` (doc_01.txt … doc_08.txt).
2. Run `embed_store.py` → generates embeddings with `sentence-transformers` and stores them in ChromaDB.
3. Start the FastAPI app:
   ```bash
   uvicorn support_assistant.app:app --reload
