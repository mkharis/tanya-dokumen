# 🚀 AI/ML Portfolio Projects

A curated collection of my AI & Machine Learning projects, from classical ML to modern LLM applications.

**Author:** [Mukhammad Kharis](https://github.com/mkharis)  
**Last Updated:** 2026

---

## 📊 Projects Overview

| # | Project | Domain | Tech Stack | Status | Demo |
|---|---------|--------|------------|--------|------|
| 1 | [Tanya Dokumen — RAG Chatbot](#1-tanya-dokumen--rag-chatbot) | NLP / LLM | Python, LangChain, ChromaDB, FastAPI, Streamlit | 🚧 In Progress | [Live](#) |
| 2 | [Coming Soon](#2-coming-soon) | - | - | 📅 Planned | - |
| 3 | [Coming Soon](#3-coming-soon) | - | - | 📅 Planned | - |

---

## 1. Tanya Dokumen — RAG Chatbot

> A Retrieval-Augmented Generation chatbot that answers questions based on your own documents (PDFs) with source citations.

### 🎯 Problem
Students, researchers, and professionals struggle to find specific information within long documents. Manual reading is time-consuming, and keyword search (Ctrl+F) fails for conceptual questions.

### 💡 Solution
An end-to-end RAG application that:
- Ingests PDF documents
- Chunks and embeds text into a vector database
- Retrieves relevant context for user questions
- Generates grounded answers using an LLM
- Displays **source citations** (page numbers + snippets)

### 🏗️ Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   User UI   │────▶│  FastAPI     │────▶│  Retriever  │
│ (Streamlit) │◀────│  Backend     │◀────│ (Vector DB) │
└─────────────┘     └──────────────┘     └─────────────┘
                            │                    ▲
                            ▼                    │
                    ┌──────────────┐     ┌──────────────┐
                    │  LLM         │     │  Embeddings  │
                    │  (OpenAI)    │     │  (SBERT)     │
                    └──────────────┘     └──────────────┘
```

### 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.12 |
| RAG Framework | LangChain |
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector DB | ChromaDB |
| LLM | OpenAI API (GPT-4o mini) |
| Backend | FastAPI + Uvicorn |
| Frontend | Streamlit |
| Deployment | HuggingFace Spaces |
| Container | Docker |

### ✨ Features

**MVP:**
- ✅ Upload PDF documents
- ✅ Text extraction & chunking
- ✅ Vector similarity search
- ✅ LLM-powered Q&A with citations
- ✅ REST API
- ✅ Interactive chat UI

**Bonus:**
- ⭐ Streaming responses
- ⭐ Multi-document support
- ⭐ Chat history
- ⭐ Re-ranking with cross-encoder
- ⭐ RAGAS evaluation

### 📈 Results

| Metric | Score | Target |
|--------|-------|--------|
| Faithfulness (RAGAS) | 0.89 | ≥ 0.85 |
| Answer Relevancy | 0.84 | ≥ 0.80 |
| Context Precision | 0.78 | ≥ 0.75 |
| Avg Response Time | 1.2s | < 3s |

### 📂 Repository Structure

```
tanya-dokumen/
├── src/
│   ├── ingestion/       # Loader, chunker, embedder
│   ├── retrieval/       # Vector store, retriever
│   ├── generation/      # LLM client, prompts
│   └── pipeline.py      # RAG orchestration
├── api/                 # FastAPI backend
├── app/                 # Streamlit UI
├── tests/               # Unit tests
└── Dockerfile
```

### 🚀 Quick Start

```bash
# Clone
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

### 🔗 Links
- **Live Demo:** [huggingface.co/spaces/mkharis/tanya-dokumen](#)
- **Source Code:** [github.com/mkharis/tanya-dokumen](#)
- **Blog Post:** [medium.com/@081332210xxx/...](#)

### 🧠 Key Learnings
- Chunking strategy significantly impacts retrieval accuracy
- Re-ranking improved relevance by ~15%
- Citations are essential for user trust in LLM answers
- Understanding RAG internals matters more than just using frameworks

---

## 2. Coming Soon

> Placeholder for the next project.

**Planned domain:** Computer Vision / Tabular ML / Time Series  
**Estimated start:** TBD

---

## 3. Coming Soon

> Placeholder for the next project.

**Planned domain:** MLOps / Production ML  
**Estimated start:** TBD

---

## 📚 Skills Demonstrated

### Programming & Tools
- **Languages:** Python, SQL
- **ML/DL:** scikit-learn, PyTorch, TensorFlow
- **LLM/NLP:** LangChain, HuggingFace, RAG, prompt engineering
- **Data:** pandas, NumPy, matplotlib, seaborn
- **MLOps:** Docker, Git, MLflow, Weights & Biases
- **Web:** FastAPI, Streamlit, Flask
- **Cloud:** HuggingFace Spaces, Railway, GCP

### Concepts
- Supervised & unsupervised learning
- Feature engineering & selection
- Model evaluation & hyperparameter tuning
- Retrieval-Augmented Generation (RAG)
- Vector databases & embeddings
- Prompt engineering
- End-to-end ML pipelines

---

## 🗺️ Learning Roadmap

### ✅ Completed
- [x] Classical ML (regression, classification, clustering)
- [x] Deep learning fundamentals
- [x] NLP basics (tokenization, embeddings)
- [x] LLM application development

### 🚧 In Progress
- [ ] Advanced RAG techniques
- [ ] Agentic AI (tool-using agents)
- [ ] MLOps & production ML
- [ ] LLM fine-tuning (LoRA, QLoRA)

### 📅 Planned
- [ ] Multi-modal AI (vision + language)
- [ ] Model deployment at scale
- [ ] Distributed training
- [ ] AI safety & evaluation

---

## 📬 Contact

- **GitHub:** [@mkharis](https://github.com/mkharis)
- **LinkedIn:** [linkedin.com/in/mukhammad-kharis-249167143](#)
- **Email:** 081332210xxx@gmail.com
- **Blog:** [medium.com/@081332210xxx](#)

---

## 📝 License

This portfolio is licensed under the MIT License. Individual projects may have their own licenses.

---

⭐ **If you find any of these projects useful, feel free to star the repos!**
