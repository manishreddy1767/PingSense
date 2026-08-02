from pprint import pprint

from src.data.manager import DataManager
from src.data.repository import Repository

from src.context.builder import ContextBuilder
from src.context.joins import ContextJoins

from src.multimodal.normalizer import MultimodalNormalizer
from src.retrieval.retriever import EvidenceRetriever
from src.rules.engine import RuleEngine


def main():

    data = DataManager.load()

    repo = Repository(data)

    builder = ContextBuilder(
        ContextJoins(repo)
    )

    normalizer = MultimodalNormalizer()

    retriever = EvidenceRetriever(repo)

    engine = RuleEngine()

    message_id = data.messages.iloc[0]["message_id"]

    context = builder.build(message_id)

    context = normalizer.normalize(context)

    context = retriever.retrieve(context)

    context = engine.run(context)

    print("\n================ MESSAGE ================\n")
    print(context.effective_text)

    print("\n================ EVIDENCE ================\n")

    for evidence in context.retrieved_evidence:
        print(evidence)

    print("\n================ RULE RESULT ================\n")

    pprint(context.rule_features)


if __name__ == "__main__":
    main()