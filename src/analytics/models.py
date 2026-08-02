from dataclasses import dataclass


@dataclass(slots=True)
class Analytics:

    total_messages: int

    notify: int

    summarize: int

    mute: int

    business: int

    promotion: int

    scam: int

    group: int

    urgent: int

    average_confidence: float

    overrides: int