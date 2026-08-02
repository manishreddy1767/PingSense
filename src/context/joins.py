"""
Join helper functions for ContextBuilder.
"""

from src.data.repository import Repository


class ContextJoins:

    def __init__(self, repo: Repository):
        self.repo = repo

    def message(self, message_id):
        return self.repo.get_message(message_id)

    def user(self, user_id):
        return self.repo.get_user(user_id)

    def group(self, group_id):
        return self.repo.get_group(group_id)

    def business(self, business_id):
        return self.repo.get_business(business_id)

    def media(self, media_type, media_id):
        return self.repo.get_media(media_type, media_id)

    def events(self, message_id, user_id):
        return self.repo.get_message_events(
            message_id,
            user_id,
        )

    def business_history(self, user_id, business_id):
        return self.repo.get_business_history(
            user_id,
            business_id,
        )

    def group_membership(self, group_id, user_id):
        return self.repo.get_group_membership(
            group_id,
            user_id,
        )