"""Train and persist the divorce prediction model (mirrors backend.ipynb)."""

from pathlib import Path

import pandas as pd
from joblib import dump
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "csv" / "Marriage_Divorce_4.csv"
MODEL_PATH = BASE_DIR / "divorce_model.joblib"

DROP_COLUMNS = [
    "Social Gap",
    "The Proportion of Common Genes",
    "Previous Trading",
    "Height Ratio",
    "Trading in",
    "Relation with Non-spouse Before Marriage",
    "Economic Similarity",
    "Social Similarities",
    "Cultural Similarities",
    "Religion Compatibility",
    "Love",
    "Commitment",
    "Loyalty",
    "Relationship with the Spouse Family",
    "Spouse Confirmed by Family",
    "Good Income",
    "No of Children from Previous Marriage",
    "Desire to Marry",
    "Quality Time Spent Together",
    "Start Socializing with the Opposite Sex Age",
    "Independency",
    "Education",
    "Self Confidence",
    "Previous Marriage",
    "Inherited_Relationship_Risk_Index",
    "Mental Health",
    "Addiction",
    "The Sense of Having Children",
    "Region",
]

FEATURE_COLUMNS = [
    "Age Gap",
    "Common Interests",
    "Divorce in the Family of Grade 1",
    "Compatibility_Score",
    "Relationship_Strength",
    "Family_Support",
    "Economic_Stability",
    "Marriage_Quality",
    "Partner_Attractiveness_Score",
]


def load_and_prepare_data() -> tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv(CSV_PATH, low_memory=False)
    df = df.apply(pd.to_numeric, errors="coerce")
    df = df.astype("int").round(2)
    df.drop(columns=DROP_COLUMNS, inplace=True, errors="ignore")
    X = df.drop(columns=["Divorce Probability"], errors="ignore")
    y = df["Divorce Probability"]
    return X, y


def train_and_save() -> None:
    X, y = load_and_prepare_data()
    X_train, _, y_train, _ = train_test_split(X, y, random_state=42)
    model = RandomForestClassifier(n_estimators=20, random_state=42)
    model.fit(X_train, y_train)
    dump({"model": model, "feature_columns": FEATURE_COLUMNS}, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    train_and_save()
