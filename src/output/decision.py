from dataclasses import dataclass

from src.overrides.models import OverrideResult


@dataclass(slots=True)
class Decision:

    action: str

    message_type: str

    reason: str

    confidence: float

    evidence_ids: list[str]

    override: OverrideResult | None = None