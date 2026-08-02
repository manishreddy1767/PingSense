from src.analytics.models import Analytics


class AnalyticsEngine:

    def summarize(self, results):

        total = len(results)

        notify = 0
        summarize = 0
        mute = 0

        business = 0
        promotion = 0
        scam = 0
        group = 0
        urgent = 0

        overrides = 0

        confidence_sum = 0.0

        for row in results:

            confidence_sum += row["confidence"]

            if row["action"] == "notify":
                notify += 1

            elif row["action"] == "summarize":
                summarize += 1

            elif row["action"] == "mute":
                mute += 1

            if row["message_type"] == "business":
                business += 1

            elif row["message_type"] == "promotion":
                promotion += 1

            elif row["message_type"] == "scam":
                scam += 1

            elif row["message_type"] == "group":
                group += 1

            elif row["message_type"] == "urgent":
                urgent += 1

            if row.get("override") is not None:
                overrides += 1

        average = 0

        if total:

            average = round(
                confidence_sum / total,
                3,
            )

        return Analytics(

            total_messages=total,

            notify=notify,

            summarize=summarize,

            mute=mute,

            business=business,

            promotion=promotion,

            scam=scam,

            group=group,

            urgent=urgent,

            average_confidence=average,

            overrides=overrides,
        )