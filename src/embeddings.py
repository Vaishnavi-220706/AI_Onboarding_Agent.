from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingModel:
    """
    Wrapper around the Sentence Transformers embedding model.
    Converts text into normalized numerical vectors.
    """

    def __init__(self, model_name: str):
        print(f"Loading embedding model: {model_name}")

        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

        print("Embedding model loaded successfully.")

    def encode(self, texts):
        """
        Convert one or more texts into embeddings.

        Args:
            texts: A string or a list of strings.

        Returns:
            NumPy array containing embeddings.
        """

        if isinstance(texts, str):
            texts = [texts]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        return np.asarray(embeddings)