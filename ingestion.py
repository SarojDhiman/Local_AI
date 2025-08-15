import os
import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

# Define the paths
PERSIST_DIR = "./chroma_db"
DATA_DIR = "./data"

# Ensure the data directory exists
if not os.path.exists(DATA_DIR):
    print(f"Error: Data directory '{DATA_DIR}' not found.")
    print("Please create the 'data' folder and add your files inside it.")
    exit()

print("--- Starting Data Ingestion ---")

# 1. Load your documents from the data directory
print("Loading documents...")
documents = SimpleDirectoryReader(input_dir=DATA_DIR).load_data()
print(f"Loaded {len(documents)} documents from '{DATA_DIR}'.")

# 2. Set up the local Ollama models
# The LLM (Llama 3) for generation
ollama_llm = Ollama(model="llama3", request_timeout=360.0)

# The embedding model for converting text to vectors
ollama_embedding = OllamaEmbedding(model_name="nomic-embed-text")

# 3. Create a local ChromaDB client and a collection
print("Creating a local ChromaDB collection...")
db = chromadb.PersistentClient(path=PERSIST_DIR)
chroma_collection = db.get_or_create_collection("ai_syllabus")

# 4. Set up the storage context with the ChromaDB vector store
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 5. Create the index
# This process takes the documents, embeds them, and stores them in the database.
print("Creating the vector index. This may take a while depending on data size.")
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    embed_model=ollama_embedding,
)

print(f"Index created and stored at '{PERSIST_DIR}'.")
print("--- Data Ingestion Complete ---")