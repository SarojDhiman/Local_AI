import os
import chromadb
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

# Define the paths
PERSIST_DIR = "./chroma_db"

# Check if the database has been created by the ingestion script
if not os.path.exists(PERSIST_DIR):
    print(f"Error: The vector database at '{PERSIST_DIR}' was not found.")
    print("Please run 'python ingestion.py' first to create the index.")
    exit()

print("--- Initializing Offline AI Assistant ---")

# 1. Set up the local Ollama models (no internet needed after initial download)
# The LLM (Llama 3) for generation
ollama_llm = Ollama(model="llama3", request_timeout=360.0)

# The embedding model for converting text to vectors
ollama_embedding = OllamaEmbedding(model_name="nomic-embed-text")

# 2. Connect to the existing local ChromaDB
print("Connecting to the local ChromaDB...")
db = chromadb.PersistentClient(path=PERSIST_DIR)
chroma_collection = db.get_or_create_collection("ai_syllabus")

# 3. Load the index from the database
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = load_index_from_storage(
    storage_context=storage_context,
    embed_model=ollama_embedding,
    llm=ollama_llm
)

# 4. Create a query engine
query_engine = index.as_query_engine()

print("AI Assistant is ready! You can now ask questions about the AI syllabus.")
print("Type 'exit' or 'quit' to end the conversation.")
print("---")

# 5. Main query loop
while True:
    try:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("Assistant: Goodbye!")
            break

        # Send the query to the local RAG engine
        response = query_engine.query(query)

        # Print the response
        print(f"Assistant: {response}")

    except Exception as e:
        print(f"An error occurred: {e}")