from src.analytics.engine import AnalyticsEngine

from src.data.manager import DataManager
from src.data.repository import Repository

from src.context.builder import ContextBuilder
from src.context.joins import ContextJoins

from src.multimodal.normalizer import MultimodalNormalizer

from src.retrieval.retriever import EvidenceRetriever

from src.rules.engine import RuleEngine

from src.llm.router import LLMRouter

from src.overrides.engine import OverrideEngine

from src.confidence.engine import ConfidenceEngine

from src.output.formatter import OutputFormatter
from src.output.writer import OutputWriter


class PipelineOrchestrator:

    def __init__(self):

        self.data = DataManager.load()

        self.repo = Repository(self.data)

        self.builder = ContextBuilder(
            ContextJoins(self.repo)
        )

        self.normalizer = MultimodalNormalizer()

        self.retriever = EvidenceRetriever(
            self.repo
        )

        self.rule_engine = RuleEngine()

        self.llm = LLMRouter()

        self.override = OverrideEngine()

        self.confidence = ConfidenceEngine()

        self.formatter = OutputFormatter()

        self.writer = OutputWriter()

        self.analytics = AnalyticsEngine()

    # ------------------------------------------------

    def run(self, message_id):

        context = self.builder.build(
            message_id
        )

        context = self.normalizer.normalize(
            context
        )

        context = self.retriever.retrieve(
            context
        )

        context = self.rule_engine.run(
            context
        )

        context = self.llm.run(
            context
        )

        decision = self.override.run(
            context
        )

        self.confidence.run(
            context,
            decision,
        )

        result = self.formatter.format(
            context,
            decision,
        )

        return result

    # ------------------------------------------------

    def run_single(self):

        message_id = self.data.messages.iloc[0][
            "message_id"
        ]

        result = self.run(message_id)

        self.writer.write_json(result)

        self.writer.write_csv(result)

        return result

    # ------------------------------------------------

    def run_batch(self):

        results = []

        for message_id in self.data.messages["message_id"]:

            try:

                result = self.run(
                    message_id
                )

                results.append(result)

            except Exception as e:

                print(
                    f"Failed: {message_id} -> {e}"
                )

        json_file = self.writer.write_json(
            results
        )

        csv_file = self.writer.write_csv(
            results
        )

        analytics = self.analytics.summarize(
            results
        )

        return {

            "results": results,

            "analytics": analytics,

            "output_json": str(
                json_file
            ),

            "output_csv": str(
                csv_file
            ),
        }