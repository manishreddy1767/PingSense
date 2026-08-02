import json
from pathlib import Path

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

        user_prompt = USER_TEMPLATE

        user_prompt = user_prompt.replace(
            "{{message}}",
            context.effective_text,
        )

        user_prompt = user_prompt.replace(
            "{{evidence}}",
            json.dumps(evidence, indent=2),
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
            str(rule_result.risk_score),
        )

        user_prompt = user_prompt.replace(
            "{{history}}",
            json.dumps(history, indent=2),
        )

        return SYSTEM_TEMPLATE, user_prompt