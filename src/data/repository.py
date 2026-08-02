"""
Repository

Provides indexed access to all datasets and returns
domain model objects instead of pandas Series.
"""

import pandas as pd

from src.data.manager import DataManager

from src.models.message import Message
from src.models.user import User
from src.models.group import Group
from src.models.business import Business
from src.models.events import MessageEvents
from src.models.business_history import UserBusinessHistory
from src.models.group_membership import GroupMembership
from src.models.media import Media


class Repository:

    def __init__(self, data: DataManager):

        self.data = data

        # Primary indexes
        self.messages = data.messages.set_index("message_id")

        self.users = data.users.set_index("user_id")

        self.groups = data.groups.set_index("group_id")

        self.businesses = data.business_accounts.set_index("business_id")

        self.images = data.images.set_index("image_id")

        self.voice_notes = data.voice_notes.set_index("voice_note_id")

    # -------------------------------------------------

    @staticmethod
    def _is_missing(value):

        return pd.isna(value)

    # -------------------------------------------------

    def get_message(self, message_id):

        if message_id not in self.messages.index:
            return None

        row = self.messages.loc[message_id]

        return Message.from_series(row)

    # -------------------------------------------------

    def get_user(self, user_id):

        if user_id not in self.users.index:
            return None

        row = self.users.loc[user_id]

        return User.from_series(row)

    # -------------------------------------------------

    def get_group(self, group_id):

        if self._is_missing(group_id):
            return None

        if group_id not in self.groups.index:
            return None

        row = self.groups.loc[group_id]

        return Group.from_series(row)

    # -------------------------------------------------

    def get_business(self, business_id):

        if self._is_missing(business_id):
            return None

        if business_id not in self.businesses.index:
            return None

        row = self.businesses.loc[business_id]

        return Business.from_series(row)

    # -------------------------------------------------

    def get_media(self, media_type, media_id):

        if self._is_missing(media_type):
            return None

        if self._is_missing(media_id):
            return None

        media_type = str(media_type).lower()

        if media_type == "image":

            if media_id not in self.images.index:
                return None

            row = self.images.loc[media_id]

            return Media(
                media_id=media_id,
                media_type="image",
                file_path=row["file_path"]
            )

        if media_type == "voice":

            if media_id not in self.voice_notes.index:
                return None

            row = self.voice_notes.loc[media_id]

            return Media(
                media_id=media_id,
                media_type="voice",
                file_path=row["file_path"]
            )

        return None

    # -------------------------------------------------

    def get_message_events(self, message_id, user_id):

        df = self.data.message_events

        row = df[
            (df.message_id == message_id)
            &
            (df.user_id == user_id)
        ]

        if row.empty:
            return None

        return MessageEvents.from_series(row.iloc[0])

    # -------------------------------------------------

    def get_group_membership(self, group_id, user_id):

        if self._is_missing(group_id):
            return None

        df = self.data.group_members

        row = df[
            (df.group_id == group_id)
            &
            (df.user_id == user_id)
        ]

        if row.empty:
            return None

        return GroupMembership.from_series(row.iloc[0])

    # -------------------------------------------------

    def get_business_history(self, user_id, business_id):

        if self._is_missing(business_id):
            return None

        df = self.data.user_business_history

        row = df[
            (df.user_id == user_id)
            &
            (df.business_id == business_id)
        ]

        if row.empty:
            return None

        return UserBusinessHistory.from_series(row.iloc[0])