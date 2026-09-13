import numpy as np

class LocalHashEmbeddings:
    """Simple dependency-light embeddings for the starter MVP."""

    def __init__(self, dimensions=384):
        self.dimensions = dimensions

    def _vector(self, text):
        vector = np.zeros(self.dimensions, dtype=np.float32)
        for word in text.lower().split():
            vector[hash(word) % self.dimensions] += 1
        norm = np.linalg.norm(vector)
        if norm:
            vector /= norm
        return vector

    def embed_documents(self, texts):
        return (np.vstack([self._vector(t) for t in texts])
                if texts else np.empty((0, self.dimensions)))

    def embed_query(self, text):
        return self._vector(text)
