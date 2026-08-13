from src.config import (
    RELEVANCE_THRESHOLD
)

from src.security import security_check

from src.llm import generate_answer

from src.tools import request_dashboard_access


class OnboardingAgent:

    def __init__(
        self,
        retriever
    ):

        self.retriever = retriever

    def detect_intent(self, question):

        text = question.lower()

        action_keywords = [
            "request access",
            "give me access",
            "grant access",
            "dashboard access",
            "request analytics",
            "enable access"
        ]

        for keyword in action_keywords:

            if keyword in text:
                return "ACTION_REQUEST"

        return "QUESTION"

    def answer_question(
        self,
        role,
        question
    ):

        print("\n[1] INPUT VALIDATION")

        valid, message = security_check(
            role,
            question
        )

        if not valid:

            print("\n[2] SECURITY CHECK")
            print("FAILED")

            return message

        print("\n[2] SECURITY CHECK")
        print("PASSED")

        intent = self.detect_intent(question)

        print("\n[3] INTENT DETECTION")
        print(f"Intent: {intent}")

        if intent == "ACTION_REQUEST":

            return self.handle_action(
                role,
                question
            )

        return self.handle_question(
            question
        )

    def handle_question(
        self,
        question
    ):

        print("\n[4] SEMANTIC RETRIEVAL")

        results = self.retriever.retrieve(
            question
        )

        if not results:

            return (
                "I don't have enough information "
                "in the approved documents to "
                "answer that question."
            )

        print("\nRetrieved Documents:")

        for result in results:

            print(
                f"- {result.chunk.document} | "
                f"{result.chunk.section} | "
                f"score={result.score:.3f}"
            )

        best_score = results[0].score

        print("\n[5] RELEVANCE CHECK")
        print(
            f"Best score: {best_score:.3f}"
        )

        print(
            f"Threshold: "
            f"{RELEVANCE_THRESHOLD:.3f}"
        )

        if best_score < RELEVANCE_THRESHOLD:

            print(
                "Result: INSUFFICIENT EVIDENCE"
            )

            return (
                "I don't have enough information "
                "in the approved documents to "
                "answer that question."
            )

        print("Result: SUFFICIENT EVIDENCE")

        print("\n[6] GROUNDED GENERATION")

        answer = generate_answer(
            question,
            results
        )

        print("\n[7] FINAL RESPONSE")

        return answer

    def handle_action(
        self,
        role,
        question
    ):

        print("\n[4] AUTHORIZATION")

        if role.lower() != "manager":

            return (
                "Authorization failed. "
                "Only a manager can request "
                "this access action."
            )

        print(
            "Authorization passed."
        )

        print("\n[5] HUMAN APPROVAL")

        print(
            "\nThe requested action is:"
        )

        print(
            "Request Analytics Dashboard access."
        )

        approval = input(
            "\nApprove this action? "
            "[yes/no]: "
        ).strip().lower()

        if approval not in ["yes", "y"]:

            print(
                "\nApproval rejected."
            )

            return (
                "Action cancelled. "
                "No access request was submitted."
            )

        print(
            "\nApproval granted."
        )

        print("\n[6] TOOL EXECUTION")

        result = request_dashboard_access(
            role=role,
            employee_name="Demo Employee"
        )

        if not result.success:

            return (
                "The access request could not "
                "be completed."
            )

        print(
            f"Tool success: {result.success}"
        )

        print(
            f"Request ID: {result.request_id}"
        )

        return (
            f"{result.message}\n"
            f"Request ID: {result.request_id}"
        )