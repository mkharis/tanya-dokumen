import os

from dotenv import load_dotenv

from src.generation.llm import answer, extract_citations
from src.ingestion.chunker import chunk_documents
from src.ingestion.embedder import get_embeddings
from src.ingestion.loader import load_pdf
from src.retrieval.vectorstore import add_documents, get_vectorstore, retrieve

load_dotenv()


def ingest(path, document_id=None):
    document_id = document_id or os.path.basename(path)
    embeddings = get_embeddings()
    store = get_vectorstore(embeddings)
    docs = load_pdf(path)
    chunks = chunk_documents(docs, document_id)
    add_documents(store, chunks)
    return {"document_id": document_id, "chunks": len(chunks)}


def query(question, k=4):
    embeddings = get_embeddings()
    store = get_vectorstore(embeddings)
    chunks = retrieve(store, question, k=k)
    return {"answer": answer(question, chunks), "citations": extract_citations(chunks)}
