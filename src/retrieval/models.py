from dataclasses import dataclass


@dataclass(slots=True)
class Evidence:
    message_id: str

    score: float

    similarity: float

    reason: str

    opened: bool

    dismissed: bool

    reported: bool