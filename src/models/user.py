from dataclasses import dataclass
import pandas as pd


@dataclass(slots=True)
class User:
    user_id: str

    do_not_disturb_window: str

    messages_opened_30d: int
    messages_replied_30d: int
    notifications_dismissed_30d: int
    messages_reported_30d: int

    @classmethod
    def from_series(cls, row: pd.Series):

        return cls(
            user_id=row.name,
            do_not_disturb_window=row["do_not_disturb_window"],
            messages_opened_30d=int(row["messages_opened_30d"]),
            messages_replied_30d=int(row["messages_replied_30d"]),
            notifications_dismissed_30d=int(
                row["notifications_dismissed_30d"]
            ),
            messages_reported_30d=int(
                row["messages_reported_30d"]
            ),
        )