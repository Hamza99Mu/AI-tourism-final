from pathlib import Path

DOCUMENT_DIR = Path("data/documents")

def load_documents():
    documents = []
    if not DOCUMENT_DIR.exists():
        return documents
    for path in sorted(DOCUMENT_DIR.iterdir()):
        if path.suffix.lower() in {".txt", ".md"}:
            try:
                text = path.read_text(encoding="utf-8")
                if text.strip():
                    documents.append({"source": path.name, "text": text})
            except UnicodeDecodeError:
                pass
    return documents

def split_text(text: str, chunk_size: int = 900, overlap: int = 120):
    chunks, start = [], 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = max(0, end - overlap)
    return chunks
