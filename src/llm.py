import requests

from src.config import (
    USE_OLLAMA,
    OLLAMA_URL,
    OLLAMA_MODEL
)


def generate_with_ollama(prompt):

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "No response generated."
        )

    except Exception as error:

        print(
            f"\nOllama unavailable: {error}"
        )

        return None


def deterministic_answer(question, retrieval_results):

    best = retrieval_results[0]

    answer = (
        f"Based on the approved documentation, "
        f"the relevant information is:\n\n"
        f"{best.chunk.text}\n\n"
        f"Source: {best.chunk.document} "
        f"- {best.chunk.section}"
    )

    return answer


def generate_answer(question, retrieval_results):

    if USE_OLLAMA:

        from src.prompts import build_grounded_prompt

        prompt = build_grounded_prompt(
            question,
            retrieval_results
        )

        response = generate_with_ollama(prompt)

        if response:
            return response

    return deterministic_answer(
        question,
        retrieval_results
    )