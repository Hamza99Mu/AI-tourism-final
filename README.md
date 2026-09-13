# 🏔️ AI Tourism Assistant

A beginner-friendly hackathon project for an AI-powered tourism assistant for
Pakistan, starting with KPK.

## Features
- Streamlit UI
- LLM-powered tourism Q&A
- RAG-ready knowledge base
- Local vector-search MVP
- Personalized itinerary generation
- Optional weather API
- Maps/Places extension point
- English/Urdu response selection
- Secure API-key handling

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Add official/verified `.txt` or `.md` tourism documents to:
`data/documents/`

## Secrets

Use environment variables or `.streamlit/secrets.toml` locally.
Never commit real API keys.

For Streamlit Community Cloud, put the secrets in the app's Secrets
configuration rather than GitHub.

## Deployment

1. Push the project to GitHub.
2. Create a Streamlit Community Cloud app.
3. Select the repository, branch and `app.py`.
4. Open Advanced settings / Secrets.
5. Add your real secret values.
6. Deploy.

## Future upgrades

PDF ingestion, FAISS/Chroma, stronger embeddings, live Places API,
route optimization, voice support and agent-based planning.
