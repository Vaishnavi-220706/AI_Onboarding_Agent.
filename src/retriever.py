import re

from src.config import (
    APPROVED_DOCUMENTS,
    RELEVANCE_THRESHOLD,
    TOP_K
)

from src.embeddings import TfidfEmbedder
from src.loader import load_documents
from src.models import RetrievedPassage


STOP_WORDS = {
    "what",
    "how",
    "where",
    "when",
    "why",
    "who",
    "is",
    "are",
    "the",
    "a",
    "an",
    "to",
    "of",
    "for",
    "do",
    "does",
    "can",
    "could",
    "would",
    "should",
    "i",
    "my",
    "me",
    "we",
    "our",
    "company",
    "please",
    "tell",
    "about"
}


class Retriever:

    def __init__(self):

        self.documents = load_documents(
            APPROVED_DOCUMENTS
        )

        self.embedder = TfidfEmbedder(
            [document.text for document in self.documents]
        )

    def _keywords(self, text):

        words = re.findall(
            r"\b[a-zA-Z0-9-]+\b",
            text.lower()
        )

        return {
            word
            for word in words
            if word not in STOP_WORDS
            and len(word) > 2
        }

    def _keyword_overlap(
        self,
        query,
        document_text
    ):

        query_words = self._keywords(query)

        document_words = self._keywords(
            document_text
        )

        if not query_words:
            return 0.0

        overlap = query_words.intersection(
            document_words
        )

        return len(overlap) / len(query_words)

    def retrieve(
        self,
        query,
        top_k=TOP_K
    ):

        results = []

        for index, score in self.embedder.search(
            query,
            top_k
        ):

            document = self.documents[index]

            results.append(
                RetrievedPassage(
                    source=document.source,
                    section=document.section,
                    text=document.text,
                    score=score
                )
            )

        return results

    def retrieve_relevant(
        self,
        query,
        top_k=TOP_K
    ):

        results = []

        query_words = self._keywords(query)

        for index, score in self.embedder.search(
            query,
            top_k
        ):

            document = self.documents[index]

            overlap = self._keyword_overlap(
                query,
                document.text
            )

            # A passage must satisfy BOTH:
            # 1. TF-IDF relevance threshold
            # 2. Meaningful query-word overlap

            if (
                score >= RELEVANCE_THRESHOLD
                and
                overlap >= 0.30
            ):

                results.append(
                    RetrievedPassage(
                        source=document.source,
                        section=document.section,
                        text=document.text,
                        score=score
                    )
                )

        return results