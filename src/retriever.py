import numpy as np

from src.models import DocumentChunk, RetrievalResult


class Retriever:

    def __init__(self, embedding_model, top_k=3):
        self.embedding_model = embedding_model
        self.top_k = top_k
        self.chunks = []
        self.embeddings = None

    def build_index(self, chunks):

        self.chunks = chunks

        texts = [
            chunk.text
            for chunk in chunks
        ]

        self.embeddings = self.embedding_model.encode(texts)

    def retrieve(self, query):

        if not self.chunks:
            return []

        query_embedding = self.embedding_model.encode(
            [query]
        )[0]

        # Since embeddings are normalized,
        # dot product = cosine similarity.
        scores = np.dot(
            self.embeddings,
            query_embedding
        )

        ranked_indices = np.argsort(scores)[::-1]

        results = []

        for index in ranked_indices[:self.top_k]:

            results.append(
                RetrievalResult(
                    chunk=self.chunks[index],
                    score=float(scores[index])
                )
            )

        return results