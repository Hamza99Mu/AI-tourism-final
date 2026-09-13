import numpy as np
from embeddings import LocalHashEmbeddings

class SimpleVectorStore:
    def __init__(self):
        self.embedder = LocalHashEmbeddings()
        self.items = []
        self.matrix = np.empty((0, self.embedder.dimensions), dtype=np.float32)

    def add(self, chunks):
        self.items.extend(chunks)
        self.matrix = self.embedder.embed_documents(
            [item["text"] for item in self.items]
        )

    def search(self, query, k=4):
        if not self.items:
            return []
        scores = self.matrix @ self.embedder.embed_query(query)
        indices = np.argsort(scores)[::-1][:k]
        return [
            {**self.items[int(i)], "score": float(scores[int(i)])}
            for i in indices
        ]
