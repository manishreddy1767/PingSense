from dataclasses import dataclass


@dataclass(slots=True)
class ConfidenceResult:

    llm_score: float

    retrieval_score: float

    rule_score: float

    final_score: float