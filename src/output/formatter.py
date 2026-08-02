class OutputFormatter:

    def format(self, context, decision):

        return {

            "message_id":
            context.message.message_id,

            "action":
            decision.action,

            "message_type":
            decision.message_type,

            "reason":
            decision.reason,

            "confidence":
            decision.confidence,

            "evidence_message_ids":
            ",".join(
                decision.evidence_ids
            ),

        }