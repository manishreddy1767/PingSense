"""
Repository

Provides fast indexed access to datasets.
The Context Builder and later modules should only use this class.
"""

from src.data.manager import DataManager


class Repository:

    def __init__(self, data: DataManager):

        self.data = data

        # ----------------------------
        # Primary indexes
        # ----------------------------

        self.messages = data.messages.set_index("message_id")

        self.users = data.users.set_index("user_id")

        self.groups = data.groups.set_index("group_id")

        self.businesses = data.business_accounts.set_index("business_id")

        self.images = data.images.set_index("image_id")

        self.voice_notes = data.voice_notes.set_index("voice_note_id")

    # --------------------------------------------------

    def get_message(self, message_id):

        if message_id not in self.messages.index:
            return None

        return self.messages.loc[message_id]

    # --------------------------------------------------

    def get_user(self, user_id):

        if user_id not in self.users.index:
            return None

        return self.users.loc[user_id]

    # --------------------------------------------------

    def get_group(self, group_id):

        if group_id != group_id:
            return None

        if group_id not in self.groups.index:
            return None

        return self.groups.loc[group_id]

    # --------------------------------------------------

    def get_business(self, business_id):

        if business_id != business_id:
            return None

        if business_id not in self.businesses.index:
            return None

        return self.businesses.loc[business_id]

    # --------------------------------------------------

    def get_image(self, image_id):

        if image_id not in self.images.index:
            return None

        return self.images.loc[image_id]

    # --------------------------------------------------

    def get_voice(self, voice_id):

        if voice_id not in self.voice_notes.index:
            return None

        return self.voice_notes.loc[voice_id]

    # --------------------------------------------------

    def get_group_membership(self, group_id, user_id):

        df = self.data.group_members

        row = df[
            (df.group_id == group_id)
            &
            (df.user_id == user_id)
        ]

        if row.empty:
            return None

        return row.iloc[0]

    # --------------------------------------------------

    def get_message_events(self, message_id, user_id):

        df = self.data.message_events

        row = df[
            (df.message_id == message_id)
            &
            (df.user_id == user_id)
        ]

        if row.empty:
            return None

        return row.iloc[0]

    # --------------------------------------------------

    def get_business_history(self, user_id, business_id):

        df = self.data.user_business_history

        row = df[
            (df.user_id == user_id)
            &
            (df.business_id == business_id)
        ]

        if row.empty:
            return None

        return row.iloc[0]