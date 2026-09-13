from src.document_loader import split_text

def test_split_text():
    chunks = split_text("A" * 2000, 500, 50)
    assert len(chunks) > 1
