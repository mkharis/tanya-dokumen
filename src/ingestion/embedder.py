import os

from langchain_huggingface import HuggingFaceEmbeddings


def get_embeddings():
    model = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    return HuggingFaceEmbeddings(model_name=model)
