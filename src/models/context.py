from dataclasses import dataclass
from typing import Optional

from src.models.message import Message
from src.models.user import User
from src.models.group import Group
from src.models.business import Business
from src.models.media import Media
from src.models.events import MessageEvents
from src.models.business_history import UserBusinessHistory
from src.models.group_membership import GroupMembership


@dataclass(slots=True)
class Context:
    # Core objects
    message: Message
    user: User

    group: Optional[Group]
    business: Optional[Business]

    media: Optional[Media]

    events: Optional[MessageEvents]

    business_history: Optional[UserBusinessHistory]

    group_membership: Optional[GroupMembership]

    # Added by the Multimodal Normalizer
    effective_text: Optional[str] = None

    # Metadata produced later in the pipeline
    retrieved_evidence: Optional[list] = None

    rule_features: Optional[dict] = None

    llm_result: Optional[dict] = None

    final_action: Optional[str] = None

    confidence: Optional[float] = None