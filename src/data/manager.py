"""
DataManager

Loads and stores all runtime datasets used by PingSense.
This class provides a single access point for all DataFrames.
"""

from dataclasses import dataclass

import pandas as pd

from src.data.loader import DataLoader
from src.utils.paths import RAW_DATA


@dataclass
class DataManager:
    business_accounts: pd.DataFrame
    daily_notification_summary: pd.DataFrame
    groups: pd.DataFrame
    group_members: pd.DataFrame
    images: pd.DataFrame
    messages: pd.DataFrame
    message_events: pd.DataFrame
    message_history: pd.DataFrame
    users: pd.DataFrame
    user_business_history: pd.DataFrame
    voice_notes: pd.DataFrame

    # Evaluation datasets
    sample_messages: pd.DataFrame | None = None
    output: pd.DataFrame | None = None

    @classmethod
    def load(cls):
        """
        Load all datasets from the raw data directory.
        """

        loader = DataLoader(RAW_DATA)
        datasets = loader.load_all()

        return cls(
            business_accounts=datasets.get("business_accounts"),
            daily_notification_summary=datasets.get("daily_notification_summary"),
            groups=datasets.get("groups"),
            group_members=datasets.get("group_members"),
            images=datasets.get("images"),
            messages=datasets.get("messages"),
            message_events=datasets.get("message_events"),
            message_history=datasets.get("message_history"),
            users=datasets.get("users"),
            user_business_history=datasets.get("user_business_history"),
            voice_notes=datasets.get("voice_notes"),

            # Optional evaluation datasets
            sample_messages=datasets.get("sample_messages"),
            output=datasets.get("output"),
        )

    def available_datasets(self):
        """
        Return names of datasets currently loaded.
        """

        loaded = {}

        for name, value in self.__dict__.items():
            loaded[name] = value is not None

        return loaded