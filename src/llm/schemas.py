from dataclasses import dataclass


@dataclass(slots=True)
class LLMResult:

    action: str

    message_type: str

    reason: str

    confidence: float

    evidence_ids: list[str]