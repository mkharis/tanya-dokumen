import os

from langchain_chroma import Chroma


def get_vectorstore(embeddings):
    persist_dir = os.getenv("CHROMA_DIR", "./data/chroma")
    return Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings,
        collection_name="documents",
    )


def add_documents(vectorstore, chunks):
    vectorstore.add_documents(chunks)


def retrieve(vectorstore, question, k=4):
    return vectorstore.similarity_search(question, k=k)
