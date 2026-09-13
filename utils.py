from pathlib import Path

def ensure_directories():
    Path("data/documents").mkdir(parents=True, exist_ok=True)
    Path("vectorstore").mkdir(parents=True, exist_ok=True)
