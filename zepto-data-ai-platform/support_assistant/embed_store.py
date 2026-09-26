from sentence_transformers import SentenceTransformer
import chromadb

# Load documents
docs = []
for i in range(1,9):
    with open(f"docs/doc_{i:02}.txt") as f:
        docs.append(f.read())

# Generate embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(docs)

# Store in ChromaDB
client = chromadb.Client()
collection = client.create_collection("zepto_policies")

for i,doc in enumerate(docs):
    collection.add(documents=[doc], embeddings=[embeddings[i]], ids=[f"doc_{i+1}"])

print("Embeddings stored in ChromaDB collection 'zepto_policies'")
