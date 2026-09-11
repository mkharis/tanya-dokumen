from langchain_text_splitters import RecursiveCharacterTextSplitter

CHUNK_SIZE = 1000   # ~250 tokens at ~4 chars/token, under MiniLM's 256-token window
CHUNK_OVERLAP = 100


def chunk_documents(docs, document_id, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    for d in docs:
        d.metadata["document_id"] = document_id
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(docs)
    for c in chunks:
        c.metadata.setdefault("document_id", document_id)
        c.metadata.setdefault("page", 0)
    return chunks
