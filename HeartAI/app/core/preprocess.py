# app/core/preprocess.py

import pandas as pd

class Preprocessor:
    def __init__(self, expected_cols_path="app/models/columns.pkl"):
        from joblib import load
        self.expected_cols = load(expected_cols_path)

    def transform(self, input_dict: dict) -> pd.DataFrame:
        df = pd.DataFrame([input_dict])

        df["sex"] = df["sex"].astype(int)
        df["fbs"] = df["fbs"].astype(int)
        df["exang"] = df["exang"].astype(int)

        df = pd.get_dummies(df)

        # Add missing columns
        for col in self.expected_cols:
            if col not in df.columns:
                df[col] = 0
        df = df[self.expected_cols]

        return df
