from dataclasses import dataclass


@dataclass(slots=True)
class Metrics:

    accuracy: float

    precision: float

    recall: float

    f1_score: float