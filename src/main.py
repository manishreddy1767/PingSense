from src.data.manager import DataManager
from src.data.repository import Repository

from src.context.builder import ContextBuilder
from src.context.joins import ContextJoins

from src.multimodal.normalizer import MultimodalNormalizer

from src.retrieval.retriever import EvidenceRetriever


def main():

    data = DataManager.load()

    repo = Repository(data)

    builder = ContextBuilder(
        ContextJoins(repo)
    )

    normalizer = MultimodalNormalizer()

    retriever = EvidenceRetriever(repo)

    message_id = data.messages.iloc[0]["message_id"]

    context = builder.build(message_id)

    context = normalizer.normalize(context)

    context = retriever.retrieve(context)

    print()

    print(context.retrieved_evidence)


if __name__ == "__main__":
    main()