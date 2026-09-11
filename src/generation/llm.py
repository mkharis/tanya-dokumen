import os

from langchain_openai import ChatOpenAI

SYSTEM_PROMPT = (
    "You answer questions strictly using the provided context. "
    "If the context does not contain the answer, say so. "
    "Cite the context chunk number(s) you used in your answer."
)


def get_llm():
    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0,
    )


def build_context(chunks):
    parts = []
    for i, c in enumerate(chunks, 1):
        meta = c.metadata
        parts.append(
            f"[{i}] (document: {meta.get('document_id')}, page: {meta.get('page')})\n{c.page_content}"
        )
    return "\n\n".join(parts)


def answer(question, chunks, llm=None):
    llm = llm or get_llm()
    human = f"Context:\n{build_context(chunks)}\n\nQuestion: {question}"
    return llm.invoke([("system", SYSTEM_PROMPT), ("human", human)]).content


def extract_citations(chunks):
    return [
        {
            "document_id": c.metadata.get("document_id"),
            "page": c.metadata.get("page"),
            "snippet": c.page_content[:200],
        }
        for c in chunks
    ]
