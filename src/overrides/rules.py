class OverrideRules:

    @staticmethod
    def force_notify_for_otp(context):

        return context.rule_features.features.otp_request

    @staticmethod
    def force_notify_for_suspicious(context):

        return context.rule_features.features.suspicious

    @staticmethod
    def verified_business(context):

        return context.rule_features.features.verified_business

    @staticmethod
    def promotions_opted_out(context):

        return context.rule_features.features.promotion_opted_out

    @staticmethod
    def quiet_hours(context):

        return context.rule_features.features.quiet_hours