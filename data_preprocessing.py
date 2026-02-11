"""
Data Preprocessing Module
Handles cleaning, feature selection, and data preparation.
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load dataset from Excel file."""
    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip()
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove leakage columns and handle missing values."""
    drop_columns = [
        "Date",
        "Crude Outlet",
        "Delta T",
        "Other Inlet",
        "Other Outlet",
        "Other Flow",
        "Crude flow"
    ]

    df = df.drop(columns=drop_columns, errors="ignore")
    df = df.dropna()

    return df


def split_features_target(df: pd.DataFrame):
    """Split dataframe into features and target."""
    X = df.drop("Crude Inlet", axis=1)
    y = df["Crude Inlet"]
    return X, y
