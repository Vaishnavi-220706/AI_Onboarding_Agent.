EMBEDDING_MODEL = "all-MiniLM-L6-v2"

TOP_K = 3

# Adjust this based on your retrieval results.
RELEVANCE_THRESHOLD = 0.35

DOCUMENTS_PATH = "documents"

# Set True only if Ollama is installed and running.
USE_OLLAMA = False

OLLAMA_URL = "http://localhost:11434/api/generate"

OLLAMA_MODEL = "llama3.2"

APPROVED_ROLES = [
    "employee",
    "manager"
]