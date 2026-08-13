from src.config import APPROVED_ROLES


INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "reveal your system prompt",
    "show me your system prompt",
    "reveal the system prompt",
    "bypass your instructions",
    "forget your instructions",
    "developer message",
    "system message"
]


def detect_prompt_injection(text: str) -> bool:

    text_lower = text.lower()

    for pattern in INJECTION_PATTERNS:

        if pattern in text_lower:
            return True

    return False


def validate_role(role: str) -> bool:

    return role.lower().strip() in APPROVED_ROLES


def security_check(role: str, question: str):

    if not validate_role(role):
        return False, "Invalid role."

    if detect_prompt_injection(question):
        return False, "Potential prompt injection detected."

    if not question.strip():
        return False, "Question cannot be empty."

    return True, "Security check passed."