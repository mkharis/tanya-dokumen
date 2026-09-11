from langchain_core.documents import Document

from src.generation.llm import build_context, extract_citations
from src.ingestion.chunker import chunk_documents


def test_chunker_preserves_metadata():
    doc = Document(page_content="word " * 1000, metadata={"page": 3, "source": "sample.pdf"})
    chunks = chunk_documents([doc], document_id="sample.pdf")
    assert len(chunks) > 1
    for c in chunks:
        assert c.metadata["document_id"] == "sample.pdf"
        assert c.metadata["page"] == 3


def test_build_context_lists_chunks():
    chunks = [Document(page_content="hello world", metadata={"document_id": "a.pdf", "page": 1})]
    context = build_context(chunks)
    assert "[1]" in context
    assert "a.pdf" in context
    assert "page: 1" in context


def test_extract_citations():
    chunks = [Document(page_content="hello world", metadata={"document_id": "a.pdf", "page": 1})]
    citations = extract_citations(chunks)
    assert citations[0]["document_id"] == "a.pdf"
    assert citations[0]["page"] == 1
    assert citations[0]["snippet"] == "hello world"
