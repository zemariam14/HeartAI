import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from pathlib import Path
import os

def load_data(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)

def preprocess_data(df: pd.DataFrame):
    # Drop rows with missing values
    df = df.dropna()

    # Convert categorical fields to numeric
    df["sex"] = df["sex"].map({"Male": 1, "Female": 0})
    df["fbs"] = df["fbs"].astype(int)
    df["exang"] = df["exang"].astype(int)
    
    # Binary classification: 0 = no disease, 1 = disease
    df["target"] = df["num"].apply(lambda x: 1 if x > 0 else 0)

    # Drop unnecessary columns
    drop_cols = ["id", "dataset", "num"]
    df = df.drop(columns=drop_cols)

    # One-hot encode categorical variables
    df = pd.get_dummies(df, columns=["cp", "restecg", "slope", "thal"])

    # Separate features and target
    X = df.drop(columns=["target"])
    y = df["target"]

    return X, y


def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def save_model(model, output_path: str):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)
    print(f" Model saved to {output_path}")

def evaluate(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f" Accuracy: {acc:.4f}")

if __name__ == "__main__":
    csv_path = "data/heart.csv"
    model_path = "app/models/model.pkl"

    df = load_data(csv_path)
    X, y = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = train_model(X_train, y_train)
    evaluate(model, X_test, y_test)
    save_model(model, model_path)
