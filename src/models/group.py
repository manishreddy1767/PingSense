from dataclasses import dataclass
import pandas as pd


@dataclass(slots=True)
class Group:
    group_id: str

    group_name: str
    group_type: str

    member_count: int
    admin_count: int

    created_at: str

    messages_30d: int

    @classmethod
    def from_series(cls, row: pd.Series):

        return cls(
            group_id=row.name,
            group_name=row["group_name"],
            group_type=row["group_type"],
            member_count=int(row["member_count"]),
            admin_count=int(row["admin_count"]),
            created_at=row["created_at"],
            messages_30d=int(row["messages_30d"]),
        )