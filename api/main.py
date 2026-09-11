import os
import tempfile
from pathlib import Path

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from src.pipeline import ingest, query

app = FastAPI(title="Tanya Dokumen")


class QueryRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/documents")
def upload_document(file: UploadFile = File(...)):
    suffix = Path(file.filename or "doc").suffix or ".pdf"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(file.file.read())
        path = tmp.name
    try:
        return ingest(path)
    finally:
        os.unlink(path)


@app.post("/query")
def ask(req: QueryRequest):
    return query(req.question)
