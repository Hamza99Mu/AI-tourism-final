import os
from groq import Groq
from config import get_secret

def _get_client():
    api_key = get_secret("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in Streamlit secrets or environment variables.")
    return Groq(api_key=api_key)

def answer_with_rag(query: str, context: str) -> str:
    client = _get_client()
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful tourism assistant. Use the provided context to answer."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuery: {query}"}
        ],
        temperature=0.7,
        max_tokens=1024
    )
    return response.choices[0].message.content
