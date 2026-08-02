import json

from src.llm.schemas import LLMResult


class LLMParser:

    def parse(self, response):

        data = json.loads(response)

        return LLMResult(
            action=data["action"],
            message_type=data["message_type"],
            reason=data["reason"],
            confidence=float(data["confidence"]),
            evidence_ids=data["evidence_ids"],
        )