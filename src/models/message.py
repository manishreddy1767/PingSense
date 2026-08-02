from dataclasses import dataclass
from typing import Optional

import pandas as pd

from src.utils.helpers import clean


@dataclass(slots=True)
class Message:
    message_id: str
    user_id: str
    conversation_type: str

    group_id: Optional[str]
    business_id: Optional[str]
    sender_user_id: Optional[str]

    created_at: str
    message_text: str

    media_type: Optional[str]
    media_id: Optional[str]

    forwarded_count: int

    @classmethod
    def from_series(cls, row: pd.Series):

        return cls(
            message_id=row.name,
            user_id=clean(row["user_id"]),
            conversation_type=clean(row["conversation_type"]),
            group_id=clean(row["group_id"]),
            business_id=clean(row["business_id"]),
            sender_user_id=clean(row["sender_user_id"]),
            created_at=clean(row["created_at"]),
            message_text=clean(row["message_text"]),
            media_type=clean(row["media_type"]),
            media_id=clean(row["media_id"]),
            forwarded_count=int(row["forwarded_count"]),
        )