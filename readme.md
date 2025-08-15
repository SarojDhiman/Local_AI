# Local-First AI Assistant for Offline Learning

This project demonstrates how to build a powerful AI assistant that runs entirely on your local machine, using a Retrieval-Augmented Generation (RAG) framework. This system is perfect for learners, researchers, and anyone who needs access to a specific body of knowledge without an internet connection.

It uses [LlamaIndex](https://www.llamaindex.ai/) as the core orchestration framework, [Ollama](https://ollama.com) to manage the local AI models, and [ChromaDB](https://www.trychroma.com) as a private, on-device vector database.

## Features

- **Offline Functionality:** Once models and data are ingested, the system works completely offline.
- **Privacy:** All data and interactions remain on your local machine.
- **Context-Aware:** The AI's responses are grounded in your specific files, preventing hallucinations.

## Setup

1.  **Clone this repository:**
    ```bash
    git clone <your-repo-link>
    cd <your-repo-name>
    ```

2.  **Install Ollama:**
    Download and install Ollama from [ollama.com](https://ollama.com).

3.  **Pull the necessary models:**
    Open your terminal and run these commands to download the models. **(This step requires an internet connection).**
    ```bash
    ollama pull llama3
    ollama pull nomic-embed-text
    ```

4.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # For macOS/Linux:
    source venv/bin/activate
    # For Windows:
    venv\Scripts\activate
    ```

5.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Add your data:**
    Place all your educational documents (PDFs, `.txt` files, etc.) into the `data/` directory.

2.  **Ingest the data:**
    Run the ingestion script to process your files and build the vector database.
    ```bash
    python ingestion.py
    ```

3.  **Start the AI assistant:**
    Now, you can run the query script to start asking questions.
    ```bash
    python query.py
    ```
    The assistant will be ready to answer your questions based on the content you provided, even if you are offline!