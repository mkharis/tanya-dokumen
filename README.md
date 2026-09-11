# Tanya Dokumen

A retrieval-augmented generation (RAG) chatbot that answers questions from your own PDF documents, citing the source pages it used.

## How it works

1. **Ingest** — a PDF is loaded, split into ~250-token chunks, embedded, and stored in a ChromaDB vector store.
2. **Retrieve** — a query is embedded and the most similar chunks are fetched.
3. **Generate** — the retrieved chunks are handed to an LLM as context, which produces a grounded answer with citations.

## Tech stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| RAG | LangChain |
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector DB | ChromaDB |
| LLM | OpenAI (`gpt-4o-mini`) |
| API | FastAPI |
| UI | Streamlit |

## Getting started

```bash
git clone https://github.com/mkharis/tanya-dokumen.git
cd tanya-dokumen

# Install dependencies (creates .venv)
uv sync

# Configure
cp .env.example .env
# Edit .env and add OPENAI_API_KEY

# Run API
uv run uvicorn api.main:app --reload

# Run UI (in another terminal)
uv run streamlit run app/streamlit_app.py
```

Then open the Streamlit app, upload a PDF, and ask questions.

## API

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Health check |
| `POST` | `/documents` | Upload a PDF (multipart `file`) → indexes it |
| `POST` | `/query` | Body `{"question": "..."}` → `{"answer", "citations"}` |

## Project structure

```
src/
├── ingestion/       # Loader, chunker, embedder
├── retrieval/       # Vector store, retriever
├── generation/      # LLM client, prompt, citations
└── pipeline.py      # RAG orchestration
api/                 # FastAPI backend
app/                 # Streamlit UI
tests/               # Unit tests
```

## Testing

```bash
uv run pytest
```
