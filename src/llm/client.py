import json

from anthropic import Anthropic

from src.config.settings import (
    CLAUDE_API_KEY,
    LLM,
)


class ClaudeClient:

    def __init__(self):

        self.mode = LLM["mode"]

        if self.mode == "live":

            if not CLAUDE_API_KEY:
                raise ValueError(
                    "Missing CLAUDE_API_KEY"
                )

            self.client = Anthropic(
                api_key=CLAUDE_API_KEY
            )

    def generate(
        self,
        system_prompt,
        user_prompt,
    ):

        # ---------------------------------
        # MOCK MODE
        # ---------------------------------

        if self.mode == "mock":

            payload = json.loads(user_prompt)

            rules = payload["rule_result"]["features"]

            evidence_ids = [
                item["message_id"]
                for item in payload["retrieved_evidence"][:2]
            ]

            action = "mute"
            message_type = "group"
            reason = "Routine group message."
            confidence = 0.65

            if rules["suspicious"]:

                action = "notify"
                message_type = "scam"
                reason = "Suspicious content detected."
                confidence = 0.98

            elif rules["otp_request"]:

                action = "notify"
                message_type = "urgent"
                reason = "OTP requires immediate attention."
                confidence = 0.97

            elif rules["payment_request"]:

                action = "notify"
                message_type = "business"
                reason = "Payment related message."
                confidence = 0.94

            elif rules["promotion_opted_out"]:

                action = "summarize"
                message_type = "promotion"
                reason = "Promotional message."
                confidence = 0.90

            elif rules["quiet_hours"]:

                action = "summarize"
                message_type = "group"
                reason = "Deferred because of quiet hours."
                confidence = 0.80

            elif rules["verified_business"]:

                action = "notify"
                message_type = "business"
                reason = "Verified business message."
                confidence = 0.88

            return json.dumps(
                {
                    "action": action,
                    "message_type": message_type,
                    "reason": reason,
                    "confidence": confidence,
                    "evidence_ids": evidence_ids,
                }
            )

        # ---------------------------------
        # LIVE MODE
        # ---------------------------------

        response = self.client.messages.create(

            model=LLM["model"],

            temperature=LLM["temperature"],

            max_tokens=LLM["max_tokens"],

            system=system_prompt,

            messages=[
                {
                    "role": "user",
                    "content": user_prompt,
                }
            ],
        )

        if not response.content:
            raise RuntimeError(
                "Claude returned an empty response."
            )

        return response.content[0].text.strip()