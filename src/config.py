from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"

APPROVED_DOCUMENTS = [
    DATA_DIR / "onboarding_guide.txt",
    DATA_DIR / "security_policy.txt",
    DATA_DIR / "support_escalation.txt",
    DATA_DIR / "product_faq.txt",
]

RELEVANCE_THRESHOLD = 0.16

TOP_K = 3