from dataclasses import dataclass
from typing import Optional


@dataclass
class DocumentChunk:
    chunk_id: str
    document: str
    section: str
    text: str
    embedding: Optional[object] = None


@dataclass
class RetrievalResult:
    chunk: DocumentChunk
    score: float


@dataclass
class ToolResult:
    success: bool
    message: str
    request_id: Optional[str] = None