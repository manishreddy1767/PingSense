from datetime import datetime

from src.rules.keywords import (
    OTP_KEYWORDS,
    PAYMENT_KEYWORDS,
    URGENT_KEYWORDS,
)

from src.rules.models import (
    RuleFeatures,
    RuleResult,
)

from src.rules.utils import (
    contains_keywords,
    contains_link,
)


class RuleEngine:

    def run(self, context):

        features = RuleFeatures()

        triggered = []

        self._business_rules(
            context,
            features,
            triggered,
        )

        self._user_rules(
            context,
            features,
            triggered,
        )

        self._message_rules(
            context,
            features,
            triggered,
        )

        self._group_rules(
            context,
            features,
            triggered,
        )

        self._risk_rules(
            features,
            triggered,
        )

        risk = self._calculate_risk(features)

        explanation = self._build_explanation(
            triggered
        )

        context.rule_features = RuleResult(

            features=features,

            triggered_rules=triggered,

            risk_score=round(risk, 2),

            explanation=explanation,

        )

        return context

    # --------------------------------------------------

    def _business_rules(
        self,
        context,
        features,
        triggered,
    ):

        if context.business is None:
            return

        if context.business.verified:

            features.verified_business = True

            triggered.append(
                "verified_business"
            )

        if context.business.user_reports_30d < 10:

            features.trusted_sender = True

            triggered.append(
                "trusted_sender"
            )

    # --------------------------------------------------

    def _user_rules(
        self,
        context,
        features,
        triggered,
    ):

        history = context.business_history

        if history is not None:

            if not history.allows_promotions:

                features.promotion_opted_out = True

                triggered.append(
                    "promotion_opted_out"
                )

        window = context.user.do_not_disturb_window

        if not window:
            return

        start, end = window.split("-")

        now = datetime.now().strftime("%H:%M")

        if start > end:

            quiet = (
                now >= start
                or now <= end
            )

        else:

            quiet = (
                start <= now <= end
            )

        if quiet:

            features.quiet_hours = True

            triggered.append(
                "quiet_hours"
            )

    # --------------------------------------------------

    def _message_rules(
        self,
        context,
        features,
        triggered,
    ):

        text = context.effective_text or ""

        if context.message.forwarded_count >= 5:

            features.high_forward_count = True

            triggered.append(
                "high_forward_count"
            )

        if contains_link(text):

            features.has_link = True

            triggered.append(
                "has_link"
            )

        if contains_keywords(
            text,
            OTP_KEYWORDS,
        ):

            features.otp_request = True

            triggered.append(
                "otp_request"
            )

        if contains_keywords(
            text,
            PAYMENT_KEYWORDS,
        ):

            features.payment_request = True

            triggered.append(
                "payment_request"
            )

        if contains_keywords(
            text,
            URGENT_KEYWORDS,
        ):

            features.urgent_language = True

            triggered.append(
                "urgent_language"
            )

    # --------------------------------------------------

    def _group_rules(
        self,
        context,
        features,
        triggered,
    ):

        if (
            context.message.conversation_type
            ==
            "direct"
        ):

            features.direct_message = True

            triggered.append(
                "direct_message"
            )

        if (
            context.group_membership
            and context.effective_text
        ):

            mention = (
                "@"
                + context.user.user_id
            )

            if mention in context.effective_text:

                features.direct_mention = True

                triggered.append(
                    "direct_mention"
                )

    # --------------------------------------------------

    def _risk_rules(
        self,
        features,
        triggered,
    ):

        suspicious = False

        if (
            features.otp_request
            and features.payment_request
        ):
            suspicious = True

        if (
            features.has_link
            and features.urgent_language
        ):
            suspicious = True

        if (
            not features.verified_business
            and features.payment_request
        ):
            suspicious = True

        if suspicious:

            features.suspicious = True

            triggered.append(
                "suspicious"
            )

    # --------------------------------------------------

    def _calculate_risk(
        self,
        features,
    ):

        risk = 0.0

        if features.payment_request:
            risk += 0.20

        if features.otp_request:
            risk += 0.30

        if features.urgent_language:
            risk += 0.15

        if features.has_link:
            risk += 0.15

        if features.high_forward_count:
            risk += 0.10

        if not features.verified_business:
            risk += 0.20

        return min(risk, 1.0)

    # --------------------------------------------------

    def _build_explanation(
        self,
        triggered,
    ):

        if not triggered:
            return "No significant deterministic rules triggered."

        return (
            "Triggered rules: "
            + ", ".join(triggered)
        )