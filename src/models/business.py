from dataclasses import dataclass

import pandas as pd

from src.utils.helpers import clean


@dataclass(slots=True)
class Business:
    business_id: str

    display_name: str
    brand_name: str
    category: str

    verified: bool

    official_domain: str
    domain_used_by_sender: str

    account_age_days: int
    messages_sent_30d: int
    user_reports_30d: int

    domain_used_by_sender_age_days: int

    @classmethod
    def from_series(cls, row: pd.Series):

        return cls(
            business_id=row.name,
            display_name=clean(row["display_name"]),
            brand_name=clean(row["brand_name"]),
            category=clean(row["category"]),
            verified=bool(row["verified"]),
            official_domain=clean(row["official_domain"]),
            domain_used_by_sender=clean(row["domain_used_by_sender"]),
            account_age_days=int(row["account_age_days"]),
            messages_sent_30d=int(row["messages_sent_30d"]),
            user_reports_30d=int(row["user_reports_30d"]),
            domain_used_by_sender_age_days=int(
                row["domain_used_by_sender_age_days"]
            ),
        )