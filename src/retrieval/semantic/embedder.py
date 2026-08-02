from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SemanticEmbedder:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def similarity(
        self,
        text1,
        text2,
    ):

        text1 = "" if text1 is None else str(text1)

        text2 = "" if text2 is None else str(text2)

        emb = self.model.encode(
            [text1, text2],
            normalize_embeddings=True,
        )

        return float(
            cosine_similarity(
                [emb[0]],
                [emb[1]],
            )[0][0]
        )