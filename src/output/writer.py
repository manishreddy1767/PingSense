import json
from pathlib import Path

import pandas as pd


class OutputWriter:

    def __init__(self):

        self.output_dir = Path("outputs")

        self.output_dir.mkdir(exist_ok=True)

    def write_json(self, results):

        file = self.output_dir / "results.json"

        if isinstance(results, dict):
            results = [results]

        with open(file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)

        return file

    def write_csv(self, results):

        file = self.output_dir / "results.csv"

        if isinstance(results, dict):
            results = [results]

        pd.DataFrame(results).to_csv(
            file,
            index=False,
        )

        return file