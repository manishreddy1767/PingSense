import json
from pathlib import Path

from src.config.settings import LLM

ROOT = Path(__file__).parent

SYSTEM_TEMPLATE = (
    ROOT / "prompts" / "system.txt"
).read_text(encoding="utf-8")

USER_TEMPLATE = (
    ROOT / "prompts" / "user.txt"
).read_text(encoding="utf-8")


class PromptBuilder:

    def build(self, context):

        rule_result = context.rule_features

        evidence = []

        for item in context.retrieved_evidence:

            evidence.append(
                {
                    "message_id": item.message_id,
                    "score": item.score,
                    "reason": item.reason,
                }
            )

        history = []

        for item in context.retrieved_evidence:

            history.append(
                {
                    "opened": item.opened,
                    "dismissed": item.dismissed,
                    "reported": item.reported,
                }
            )

        # ======================================================
        # MOCK MODE
        # ======================================================

        if LLM["mode"] == "mock":

            payload = {

                "message": context.effective_text,

                "retrieved_evidence": evidence,

                "rule_result": {

                    "features": {

                        "verified_business":
                            rule_result.features.verified_business,

                        "trusted_sender":
                            rule_result.features.trusted_sender,

                        "quiet_hours":
                            rule_result.features.quiet_hours,

                        "promotion_opted_out":
                            rule_result.features.promotion_opted_out,

                        "high_forward_count":
                            rule_result.features.high_forward_count,

                        "has_link":
                            rule_result.features.has_link,

                        "otp_request":
                            rule_result.features.otp_request,

                        "payment_request":
                            rule_result.features.payment_request,

                        "urgent_language":
                            rule_result.features.urgent_language,

                        "direct_message":
                            rule_result.features.direct_message,

                        "direct_mention":
                            rule_result.features.direct_mention,

                        "suspicious":
                            rule_result.features.suspicious,

                    },

                    "triggered_rules":
                        rule_result.triggered_rules,

                    "risk_score":
                        rule_result.risk_score,

                },

                "history": history,

            }

            return "", json.dumps(payload)

        # ======================================================
        # LIVE MODE
        # ======================================================

        user_prompt = USER_TEMPLATE

        user_prompt = user_prompt.replace(
            "{{message}}",
            context.effective_text,
        )

        user_prompt = user_prompt.replace(
            "{{evidence}}",
            json.dumps(
                evidence,
                indent=2,
            ),
        )

        user_prompt = user_prompt.replace(
            "{{rules}}",
            json.dumps(
                rule_result.triggered_rules,
                indent=2,
            ),
        )

        user_prompt = user_prompt.replace(
            "{{risk_score}}",
            str(
                rule_result.risk_score
            ),
        )

        user_prompt = user_prompt.replace(
            "{{history}}",
            json.dumps(
                history,
                indent=2,
            ),
        )

        return (
            SYSTEM_TEMPLATE,
            user_prompt,
        )