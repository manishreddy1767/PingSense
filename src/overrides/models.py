from dataclasses import dataclass


@dataclass(slots=True)
class OverrideResult:

    overridden: bool

    reason: str