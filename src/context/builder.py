"""
Context Builder

Builds one Context object from a message_id.
"""

from src.context.joins import ContextJoins
from src.models.context import Context


class ContextBuilder:

    def __init__(self, joins: ContextJoins):

        self.joins = joins

    def build(self, message_id):

        message = self.joins.message(message_id)

        if message is None:
            return None

        user = self.joins.user(message.user_id)

        group = self.joins.group(message.group_id)

        business = self.joins.business(
            message.business_id
        )

        media = self.joins.media(
            message.media_type,
            message.media_id,
        )

        events = self.joins.events(
            message.message_id,
            message.user_id,
        )

        business_history = self.joins.business_history(
            message.user_id,
            message.business_id,
        )

        group_membership = self.joins.group_membership(
            message.group_id,
            message.user_id,
        )

        return Context(
            message=message,
            user=user,
            group=group,
            business=business,
            media=media,
            events=events,
            business_history=business_history,
            group_membership=group_membership,
        )