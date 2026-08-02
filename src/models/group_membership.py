from dataclasses import dataclass
import pandas as pd


@dataclass(slots=True)
class GroupMembership:
    role: str
    joined_at: str
    messages_sent_30d: int
    messages_read_30d: int
    replies_sent_30d: int
    notifications_dismissed_30d: int
    group_muted_by_user: bool

    @classmethod
    def from_series(cls, row: pd.Series):

        return cls(
            role=row["role"],
            joined_at=row["joined_at"],
            messages_sent_30d=int(row["messages_sent_30d"]),
            messages_read_30d=int(row["messages_read_30d"]),
            replies_sent_30d=int(row["replies_sent_30d"]),
            notifications_dismissed_30d=int(
                row["notifications_dismissed_30d"]
            ),
            group_muted_by_user=bool(
                row["group_muted_by_user"]
            ),
        )