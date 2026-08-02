from dataclasses import dataclass, field


@dataclass(slots=True)
class RuleFeatures:
    """
    Deterministic features extracted from the message.
    These are consumed by the LLM and the Safety Override layer.
    """

    # ---------- Business ----------

    verified_business: bool = False
    trusted_sender: bool = False

    # ---------- User ----------

    quiet_hours: bool = False
    promotion_opted_out: bool = False

    # ---------- Message ----------

    high_forward_count: bool = False
    has_link: bool = False

    otp_request: bool = False
    payment_request: bool = False
    urgent_language: bool = False

    # ---------- Conversation ----------

    direct_message: bool = False
    direct_mention: bool = False

    # ---------- Risk ----------

    suspicious: bool = False


@dataclass(slots=True)
class RuleResult:
    """
    Final output of the Rule Engine.
    """

    features: RuleFeatures

    triggered_rules: list[str] = field(default_factory=list)

    risk_score: float = 0.0

    explanation: str = ""