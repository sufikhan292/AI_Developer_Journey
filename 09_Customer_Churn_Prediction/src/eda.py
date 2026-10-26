from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from data_audit import load_data

PROJECT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_DIR / "reports"

def plot_churn_by_contract(df):
    churn_rate=(
        pd.crosstab(df["Contract"],df["Churn"],normalize="index")["Yes"]
        .mul(100)
        .sort_values()
    )

    ax=churn_rate.plot(kind="bar",figsize=(8,5))

    ax.set_title("Customer Churn Rate by Contract Type")
    ax.set_xlabel("Contract Type")
    ax.set_ylabel("Churn rate (%)")
    ax.set_ylim(0,100)

    plt.xticks(rotation=0)
    plt.tight_layout()

    REPORTS_DIR.mkdir(parents=True,exist_ok=True)
    plt.savefig(REPORTS_DIR/"churn_by_contract.png",dpi=150)

    print("\nChurn rate by contract:")
    print(churn_rate.round(2))
    print(f"\nGraph saved to: {REPORTS_DIR / 'churn_by_contract.png'}")

    plt.show()

if __name__=="__main__":
    df,_=load_data()
    plot_churn_by_contract(df)