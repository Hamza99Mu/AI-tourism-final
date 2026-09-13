import streamlit as st

from document_loader import load_documents, split_text
from vectorstore import SimpleVectorStore
from config import get_secret

@st.cache_resource
def build_vector_store():
    store = SimpleVectorStore()
    for document in load_documents():
        chunks = [
            {"source": document["source"], "text": chunk}
            for chunk in split_text(document["text"])
        ]
        store.add(chunks)
    return store

def fallback_answer(language):
    if language == "Urdu":
        return ("Knowledge base میں ابھی کافی tourism documents موجود نہیں ہیں۔ "
                "data/documents/ میں official documents شامل کریں۔")
    return ("The tourism knowledge base does not contain enough documents yet. "
            "Add official tourism documents to data/documents/.")

def call_llm(question, context, language):
    key = get_secret("OPENAI_API_KEY")
    if not key:
        return fallback_answer(language)
    try:
        from openai import OpenAI
        client = OpenAI(api_key=key)
        response = client.chat.completions.create(
            model=get_secret("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {"role": "system", "content":
                 f"You are a careful Pakistan tourism assistant. Use only the supplied context, "
                 f"do not invent facts, and answer in {language}."},
                {"role": "user", "content":
                 f"Context:\n{context}\n\nQuestion:\n{question}"}
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content
    except Exception as exc:
        return f"LLM service could not be reached: {exc}"

def answer_with_rag(question, language="English"):
    results = build_vector_store().search(question, k=4)
    if not results:
        return {"answer": fallback_answer(language), "sources": []}
    context = "\n\n".join(
        f"[Source: {r['source']}]\n{r['text']}" for r in results
    )
    return {
        "answer": call_llm(question, context, language),
        "sources": list(dict.fromkeys(r["source"] for r in results)),
    }
