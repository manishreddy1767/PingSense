import pandas as pd


def clean(value):
    """
    Convert pandas NaN/NA values to Python None.
    """
    return None if pd.isna(value) else value