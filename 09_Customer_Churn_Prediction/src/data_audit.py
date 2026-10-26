
import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "raw" / "Telco-Customer-Churn.csv"


def load_data():
    df = pd.read_csv(DATA_PATH)

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"].str.strip(), errors="coerce"
    )

    missing_charges = (df["tenure"] == 0) & df["TotalCharges"].isna()
    df.loc[missing_charges, "TotalCharges"] = 0.0

    return df, missing_charges


def audit_data(df, missing_charges):
    print("\n--- DATASET OVERVIEW ---")
    print("Shape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nFirst 5 rows:\n", df.head())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nTotal missing cells:", df.isnull().sum().sum())
    print("Duplicate rows:", df.duplicated().sum())
    print("\nCustomers assigned zero TotalCharges:")
    print(df.loc[missing_charges, ["customerID", "tenure", "TotalCharges"]])


def analyze_churn(df):
    print("\n--- OVERALL CHURN ---")
    print(df["Churn"].value_counts())
    print("\nChurn percentages:")
    print((df["Churn"].value_counts(normalize=True) * 100).round(2))

    print("\n--- CHURN BY CONTRACT ---")
    print(pd.crosstab(df["Contract"], df["Churn"]))

    print("\nContract-wise churn percentages:")
    print(
        pd.crosstab(df["Contract"], df["Churn"], normalize="index")
        .mul(100).round(2)
    )


def analyze_numeric(df, columns):
    print("\n--- NUMERIC ANALYSIS BY CHURN ---")

    for column in columns:
        print(f"\n{column}:")
        print(
            df.groupby("Churn")[column]
            .agg(["count", "mean", "median", "min", "max"])
            .round(2)
        )


if __name__ == "__main__":
    df, missing_charges = load_data()
    audit_data(df, missing_charges)
    analyze_churn(df)
    analyze_numeric(df, ["tenure", "MonthlyCharges", "TotalCharges"])
