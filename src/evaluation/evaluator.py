import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
)

from src.evaluation.metrics import Metrics


class Evaluator:

    def evaluate(

        self,

        predictions_csv,

        ground_truth_csv,

    ):

        pred = pd.read_csv(
            predictions_csv
        )

        truth = pd.read_csv(
            ground_truth_csv
        )

        merged = pred.merge(

            truth,

            on="message_id",

            suffixes=(
                "_pred",
                "_true",
            ),

        )

        accuracy = accuracy_score(

            merged["action_true"],

            merged["action_pred"],

        )

        precision, recall, f1, _ = (

            precision_recall_fscore_support(

                merged["action_true"],

                merged["action_pred"],

                average="weighted",

                zero_division=0,

            )

        )

        return Metrics(

            accuracy=round(
                accuracy,
                3,
            ),

            precision=round(
                precision,
                3,
            ),

            recall=round(
                recall,
                3,
            ),

            f1_score=round(
                f1,
                3,
            ),

        )