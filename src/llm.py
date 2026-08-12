import urllib.request
import json

from src.prompts import build_grounded_prompt


class LLMUnavailable(Exception):
    pass


class AnswerGenerator:

    def __init__(self, mode="deterministic"):

        self.mode = mode

    def generate(
        self,
        question,
        role,
        passages
    ):

        if self.mode == "ollama":

            return self._ollama(
                question,
                role,
                passages
            )

        return self._deterministic(
            question,
            passages
        )

    def _ollama(
        self,
        question,
        role,
        passages
    ):

        prompt = build_grounded_prompt(
            question,
            role,
            passages
        )

        payload = json.dumps({
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }).encode("utf-8")

        try:

            request = urllib.request.Request(
                "http://localhost:11434/api/generate",
                data=payload,
                headers={
                    "Content-Type": "application/json"
                }
            )

            with urllib.request.urlopen(
                request,
                timeout=15
            ) as response:

                data = json.loads(
                    response.read().decode("utf-8")
                )

            return data["response"].strip()

        except Exception as exc:

            raise LLMUnavailable(
                str(exc)
            ) from exc

    def _deterministic(
        self,
        question,
        passages
    ):

        question_lower = question.lower()

        selected = passages[:2]

        if any(
            word in question_lower
            for word in [
                "lost",
                "stolen",
                "laptop",
                "device"
            ]
        ):

            selected = [
                passage
                for passage in passages
                if (
                    "lost" in passage.text.lower()
                    or
                    "stolen" in passage.text.lower()
                )
            ] or selected

        elif any(
            word in question_lower
            for word in [
                "password",
                "mfa",
                "multi-factor",
                "phishing"
            ]
        ):

            selected = [
                passage
                for passage in passages
                if any(
                    keyword in passage.text.lower()
                    for keyword in [
                        "password",
                        "mfa",
                        "phishing"
                    ]
                )
            ] or selected

        elif any(
            word in question_lower
            for word in [
                "support",
                "ticket",
                "urgent",
                "escalat"
            ]
        ):

            selected = [
                passage
                for passage in passages
                if any(
                    keyword in passage.text.lower()
                    for keyword in [
                        "support",
                        "ticket",
                        "escalat"
                    ]
                )
            ] or selected

        elif any(
            word in question_lower
            for word in [
                "product",
                "dashboard",
                "workspace",
                "feature"
            ]
        ):

            selected = [
                passage
                for passage in passages
                if any(
                    keyword in passage.text.lower()
                    for keyword in [
                        "product",
                        "dashboard",
                        "workspace",
                        "feature"
                    ]
                )
            ] or selected

        statements = []

        for passage in selected[:2]:

            statements.append(
                passage.text.strip()
            )

        citations = "\n".join(
            f"[{passage.source} § {passage.section}]"
            for passage in selected[:2]
        )

        return (
            " ".join(statements)
            +
            f"\n\nSources:\n{citations}"
        )