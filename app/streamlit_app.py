import os

import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Tanya Dokumen", page_icon="📄")
st.title("Tanya Dokumen")
st.caption("Ask questions about your PDF documents.")

uploaded = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded is not None:
    with st.spinner("Indexing document..."):
        r = requests.post(
            f"{API_URL}/documents",
            files={"file": (uploaded.name, uploaded.getvalue(), "application/pdf")},
        )
    if r.ok:
        data = r.json()
        st.success(f"Indexed {data['chunks']} chunks from {data['document_id']}")
    else:
        st.error(f"Ingestion failed: {r.text}")

question = st.chat_input("Ask a question about your documents")
if question:
    st.chat_message("user").write(question)
    with st.spinner("Thinking..."):
        r = requests.post(f"{API_URL}/query", json={"question": question})
    if r.ok:
        data = r.json()
        st.chat_message("assistant").write(data["answer"])
        with st.expander("Citations"):
            for c in data["citations"]:
                st.markdown(f"**{c['document_id']}** — page {c['page']}")
                st.caption(c["snippet"])
    else:
        st.error(f"Query failed: {r.text}")
