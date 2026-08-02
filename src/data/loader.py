from pathlib import Path
import pandas as pd


class DataLoader:
    """
    Loads all CSV datasets required by PingSense.
    """

    def __init__(self, data_dir):
        self.data_dir = Path(data_dir)

    def load_csv(self, filename):
        """
        Load a single CSV file.
        """
        path = self.data_dir / filename

        if not path.exists():
            raise FileNotFoundError(f"{filename} not found.")

        return pd.read_csv(path)

    def load_all(self):
        """
        Load every CSV inside the raw data folder.
        """
        datasets = {}

        for file in self.data_dir.glob("*.csv"):
            datasets[file.stem] = pd.read_csv(file)

        return datasets