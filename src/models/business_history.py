from dataclasses import dataclass

import pandas as pd

from src.utils.helpers import clean


@dataclass(slots=True)
class UserBusinessHistory:
    why_user_knows_account: str
    last_activity_at: str
    allows_promotions: bool
    promotions_opted_out_at: str | None
    activity_count_180d: int
    messages_opened_30d: int
    messages_dismissed_30d: int
    messages_replied_30d: int
    last_reply_at: str | None

    @classmethod
    def from_series(cls, row: pd.Series):

        return cls(
            why_user_knows_account=clean(row["why_user_knows_account"]),
            last_activity_at=clean(row["last_activity_at"]),
            allows_promotions=bool(row["allows_promotions"]),
            promotions_opted_out_at=clean(row["promotions_opted_out_at"]),
            activity_count_180d=int(row["activity_count_180d"]),
            messages_opened_30d=int(row["messages_opened_30d"]),
            messages_dismissed_30d=int(row["messages_dismissed_30d"]),
            messages_replied_30d=int(row["messages_replied_30d"]),
            last_reply_at=clean(row["last_reply_at"]),
        )