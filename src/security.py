import re


INJECTION_PATTERNS = [

    r"ignore\s+(all\s+)?previous\s+instructions",

    r"ignore\s+(the\s+)?system\s+prompt",

    r"reveal\s+(the\s+)?system\s+prompt",

    r"show\s+(me\s+)?your\s+hidden\s+instructions",

    r"bypass\s+(the\s+)?approval",

    r"skip\s+(the\s+)?approval",

    r"pretend\s+you\s+already\s+have\s+approval",

    r"execute\s+without\s+approval",
]


def is_prompt_injection(text: str) -> bool:

    lowered_text = text.lower()

    return any(
        re.search(
            pattern,
            lowered_text
        )
        for pattern in INJECTION_PATTERNS
    )


def safe_role(role: str) -> bool:

    return role.lower().strip() in {
        "employee",
        "manager",
        "it_admin",
        "hr_admin"
    }