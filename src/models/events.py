from dataclasses import dataclass
import pandas as pd


@dataclass(slots=True)
class MessageEvents:
    message_opened: bool
    message_replied: bool
    reaction_time_minutes: float
    notification_dismissed: bool
    muted_after_message: bool
    message_reported: bool

    @classmethod
    def from_series(cls, row: pd.Series):

        return cls(
            message_opened=bool(row["message_opened"]),
            message_replied=bool(row["message_replied"]),
            reaction_time_minutes=float(
                row["reaction_time_minutes"]
            ),
            notification_dismissed=bool(
                row["notification_dismissed"]
            ),
            muted_after_message=bool(
                row["muted_after_message"]
            ),
            message_reported=bool(
                row["message_reported"]
            ),
        )