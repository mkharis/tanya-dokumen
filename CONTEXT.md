# tanya-dokumen

A retrieval-augmented generation (RAG) chatbot that answers questions from uploaded PDF documents, citing the source pages it used.

## Language

**Document**:
An uploaded PDF; the unit of ingestion.
_Avoid_: file, source doc

**Chunk**:
A ~250-token slice of a Document; the unit of retrieval and citation.
_Avoid_: passage, snippet

**Query**:
The user's question.
_Avoid_: prompt, input

**Context**:
The retrieved Chunks handed to the LLM to ground its Answer.

**Answer**:
The LLM's response to a Query.

**Citation**:
A (document, page, text) pointer backing an Answer.
_Avoid_: reference, footnote
