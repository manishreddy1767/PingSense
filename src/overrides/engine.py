from src.output.decision import Decision
from src.overrides.models import OverrideResult
from src.overrides.rules import OverrideRules


class OverrideEngine:

    def run(self, context):

        llm = context.llm_result

        decision = Decision(
            action=llm.action,
            message_type=llm.message_type,
            reason=llm.reason,
            confidence=llm.confidence,
            evidence_ids=llm.evidence_ids,
        )

        # OTP messages
        if OverrideRules.force_notify_for_otp(context):

            decision.action = "notify"

            decision.override = OverrideResult(
                overridden=True,
                reason="OTP messages must always notify.",
            )

        # Suspicious messages
        elif OverrideRules.force_notify_for_suspicious(context):

            decision.action = "notify"

            decision.override = OverrideResult(
                overridden=True,
                reason="Suspicious message.",
            )

        # Verified businesses should not become spam
        elif (
            OverrideRules.verified_business(context)
            and decision.message_type == "spam"
        ):

            decision.message_type = "business"

            decision.override = OverrideResult(
                overridden=True,
                reason="Verified business cannot be spam.",
            )

        # Promotions opted out
        elif (
            OverrideRules.promotions_opted_out(context)
            and decision.message_type == "promotion"
        ):

            decision.action = "summarize"

            decision.override = OverrideResult(
                overridden=True,
                reason="User opted out of promotions.",
            )

        # Quiet hours
        elif (
            OverrideRules.quiet_hours(context)
            and decision.action == "notify"
            and decision.confidence < 0.8
        ):

            decision.action = "summarize"

            decision.override = OverrideResult(
                overridden=True,
                reason="Quiet hours.",
            )

        return decision