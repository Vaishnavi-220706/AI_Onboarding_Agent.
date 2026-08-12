from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class AgentRequest:
    question: str
    role: str


@dataclass
class RetrievedPassage:
    source: str
    section: str
    text: str
    score: float


@dataclass
class TraceStep:
    name: str
    detail: str


@dataclass
class PendingAction:
    action: str
    role: str
    parameters: dict


@dataclass
class AgentResult:
    final_response: str
    trace: List[TraceStep] = field(default_factory=list)
    retrieved: List[RetrievedPassage] = field(default_factory=list)
    pending_action: Optional[PendingAction] = None