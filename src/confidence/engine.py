from src.confidence.models import ConfidenceResult


class ConfidenceEngine:

    def run(self, context, decision):

        # ----------------------------------
        # LLM confidence
        # ----------------------------------

        llm_score = decision.confidence

        # ----------------------------------
        # Retrieval confidence
        # ----------------------------------

        evidence = context.retrieved_evidence

        if evidence:

            retrieval_score = (
                sum(item.score for item in evidence)
                / len(evidence)
            )

        else:

            retrieval_score = 0.0

        # ----------------------------------
        # Rule confidence
        # Higher risk -> Lower confidence
        # ----------------------------------

        rule_score = (
            1.0
            - context.rule_features.risk_score
        )

        # ----------------------------------
        # Final weighted confidence
        # ----------------------------------

        final_score = (

            0.50 * llm_score

            +

            0.30 * retrieval_score

            +

            0.20 * rule_score

        )

        decision.confidence = round(
            final_score,
            3,
        )

        return ConfidenceResult(

            llm_score=round(
                llm_score,
                3,
            ),

            retrieval_score=round(
                retrieval_score,
                3,
            ),

            rule_score=round(
                rule_score,
                3,
            ),

            final_score=decision.confidence,

        )