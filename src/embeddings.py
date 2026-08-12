from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TfidfEmbedder:

    def __init__(self, texts):

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
        )

        self.matrix = self.vectorizer.fit_transform(texts)

    def search(self, query, top_k=3):

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            self.matrix
        )[0]

        ranked_indices = scores.argsort()[::-1][:top_k]

        return [
            (int(index), float(scores[index]))
            for index in ranked_indices
        ]