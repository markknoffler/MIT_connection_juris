from langchain_ollama import OllamaEmbeddings


def get_embedding_function():
    return OllamaEmbeddings(model="llama3")
