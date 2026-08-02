from src.config.settings import RETRIEVAL

from src.retrieval.semantic.embedder import SemanticEmbedder
from src.retrieval.models import Evidence
from src.retrieval.search import CandidateSearch


class EvidenceRetriever:

    def __init__(self, repo):

        self.repo = repo

        self.search = CandidateSearch(repo)

        self.embedder = SemanticEmbedder()

        self.weights = RETRIEVAL["weights"]

        self.top_k = RETRIEVAL["top_k"]

        self.semantic_enabled = RETRIEVAL["semantic"]["enabled"]

        self.semantic_weight = RETRIEVAL["semantic"]["weight"]

    # ---------------------------------------------------------

    def retrieve(self, context):

        candidates = self.search.search(context)

        evidence = []

        for _, row in candidates.iterrows():

            score = 0.0

            reason = []

            # ---------------------------------------
            # Same Business
            # ---------------------------------------

            if row["business_id"] == context.message.business_id:

                score += self.weights["same_business"]

                reason.append("same business")

            # ---------------------------------------
            # Same Sender
            # ---------------------------------------

            if row["sender_user_id"] == context.message.sender_user_id:

                score += self.weights["same_sender"]

                reason.append("same sender")

            # ---------------------------------------
            # Same Group
            # ---------------------------------------

            if row["group_id"] == context.message.group_id:

                score += self.weights["same_group"]

                reason.append("same group")

            # ---------------------------------------
            # Token Overlap
            # ---------------------------------------

            token_similarity = self.search.token_overlap(

                row["message_text"],

                context.effective_text,

            )

            score += (

                token_similarity

                * self.weights["text_similarity"]

            )

            # ---------------------------------------
            # Semantic Similarity
            # ---------------------------------------

            semantic_similarity = 0.0

            if self.semantic_enabled:

                semantic_similarity = self.embedder.similarity(

                    row["message_text"],

                    context.effective_text,

                )

                score += (

                    semantic_similarity

                    * self.semantic_weight

                )

                if semantic_similarity > 0.70:

                    reason.append("semantic match")

            # ---------------------------------------
            # Default reason
            # ---------------------------------------

            if not reason:

                reason.append("same user history")

            # ---------------------------------------
            # Previous User Behaviour
            # ---------------------------------------

            events = self.repo.get_message_events(

                row["message_id"],

                row["user_id"],

            )

            if events is not None:

                if events.message_opened:

                    score += 0.05

                    reason.append("previously opened")

                if events.message_replied:

                    score += 0.05

                    reason.append("previously replied")

                if events.notification_dismissed:

                    score -= 0.05

                    reason.append("previously dismissed")

                if events.message_reported:

                    score -= 0.10

                    reason.append("previously reported")

            # ---------------------------------------
            # Clamp Score
            # ---------------------------------------

            score = max(

                0.0,

                min(score, 1.0),

            )

            evidence.append(

                Evidence(

                    message_id=row["message_id"],

                    score=round(score, 3),

                    similarity=round(semantic_similarity, 3),

                    reason=", ".join(reason),

                    opened=False if events is None
                    else events.message_opened,

                    dismissed=False if events is None
                    else events.notification_dismissed,

                    reported=False if events is None
                    else events.message_reported,

                )

            )

        evidence.sort(

            key=lambda x: x.score,

            reverse=True,

        )

        context.retrieved_evidence = evidence[: self.top_k]

        return context