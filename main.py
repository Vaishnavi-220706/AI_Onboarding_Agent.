from src.config import (
    EMBEDDING_MODEL,
    TOP_K,
    DOCUMENTS_PATH
)

from src.loader import load_documents

from src.embeddings import EmbeddingModel

from src.retriever import Retriever

from src.agent import OnboardingAgent


def main():

    print("=" * 60)
    print("AI EMPLOYEE ONBOARDING AGENT")
    print("=" * 60)

    print("\nLoading documents...")

    chunks = load_documents(
        DOCUMENTS_PATH
    )

    print(
        f"Loaded {len(chunks)} document chunks."
    )

    print(
        f"\nLoading embedding model: "
        f"{EMBEDDING_MODEL}"
    )

    embedding_model = EmbeddingModel(
        EMBEDDING_MODEL
    )

    print("\nBuilding semantic index...")

    retriever = Retriever(
        embedding_model=embedding_model,
        top_k=TOP_K
    )

    retriever.build_index(
        chunks
    )

    print("Semantic index ready.")

    agent = OnboardingAgent(
        retriever
    )

    print("\nSystem ready.")

    while True:

        print("\n" + "-" * 60)

        role = input(
            "Enter role "
            "(employee/manager): "
        ).strip()

        question = input(
            "Enter your question: "
        ).strip()

        response = agent.answer_question(
            role,
            question
        )

        print("\n" + "=" * 60)
        print("FINAL RESPONSE")
        print("=" * 60)

        print(response)

        again = input(
            "\nAsk another question? "
            "[y/n]: "
        ).strip().lower()

        if again != "y":
            break

    print("\nApplication closed.")


if __name__ == "__main__":
    main()