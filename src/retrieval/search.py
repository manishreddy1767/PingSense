"""
Candidate Search

Returns historical candidate messages and
provides simple text similarity.
"""


class CandidateSearch:

    def __init__(self, repo):

        self.repo = repo

    def search(self, context):

        history = self.repo.data.message_history

        history = history[
            history.user_id == context.user.user_id
        ]

        history = history[
            history.message_id !=
            context.message.message_id
        ]

        return history

    @staticmethod
    def token_overlap(text1, text2):

        if not text1 or not text2:
            return 0.0

        s1 = set(str(text1).lower().split())
        s2 = set(str(text2).lower().split())

        if not s1 or not s2:
            return 0.0

        return len(s1 & s2) / len(s1 | s2)