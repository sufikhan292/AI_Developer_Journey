
from pathlib import Path

import joblib
import pandas as pd

from data_audit import load_data

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


# -------------------- PROJECT PATHS --------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT_DIR / "reports"
MODELS_DIR = PROJECT_DIR / "models"

RESULTS_PATH = REPORTS_DIR / "model_comparison.csv"
MODEL_PATH = MODELS_DIR / "best_churn_model.joblib"


# -------------------- DATA PREPARATION --------------------

def prepare_features(df):
    """Separate input features and encode the target."""
    X = df.drop(columns=["customerID", "Churn"])
    y = df["Churn"].map({"No": 0, "Yes": 1})
    return X, y


def identify_columns(X):
    """Identify numeric and categorical feature columns."""
    numeric_columns = X.select_dtypes(include="number").columns.tolist()
    categorical_columns = X.select_dtypes(exclude="number").columns.tolist()
    return numeric_columns, categorical_columns


def split_data(X, y):
    """Split data into training, validation, and testing sets."""
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val,
        y_train_val,
        test_size=0.25,
        random_state=42,
        stratify=y_train_val,
    )

    return X_train, X_val, X_test, y_train, y_val, y_test


# -------------------- MODEL PIPELINE --------------------

def build_preprocessor(numeric_columns, categorical_columns):
    """Build preprocessing steps for numeric and categorical data."""
    return ColumnTransformer(
        transformers=[
            ("numeric", StandardScaler(), numeric_columns),
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_columns,
            ),
        ]
    )


def build_model(numeric_columns, categorical_columns, classifier):
    """Combine preprocessing with the selected classifier."""
    preprocessor = build_preprocessor(
        numeric_columns,
        categorical_columns,
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", classifier),
        ]
    )


# -------------------- VALIDATION --------------------

def select_threshold(model, X_val, y_val):
    """Choose the probability threshold with the best validation F1."""
    y_proba = model.predict_proba(X_val)[:, 1]

    thresholds = [0.2, 0.3, 0.4, 0.5, 0.6]
    best_threshold = 0.5
    best_f1 = -1

    print("\n--- THRESHOLD VALIDATION ---")

    for threshold in thresholds:
        y_pred = (y_proba >= threshold).astype(int)

        precision = precision_score(
            y_val, y_pred, zero_division=0
        )
        recall = recall_score(
            y_val, y_pred, zero_division=0
        )
        f1 = f1_score(
            y_val, y_pred, zero_division=0
        )

        print(
            f"Threshold: {threshold:.1f} | "
            f"Precision: {precision:.3f} | "
            f"Recall: {recall:.3f} | "
            f"F1: {f1:.3f}"
        )

        if f1 > best_f1:
            best_f1 = f1
            best_threshold = threshold

    print(f"\nSelected threshold: {best_threshold}")
    print(f"Best validation F1: {best_f1:.4f}")

    return best_threshold, best_f1


# -------------------- FINAL EVALUATION --------------------

def evaluate_model(model, X_test, y_test, threshold):
    """Evaluate the selected model on untouched test data."""
    y_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_proba >= threshold).astype(int)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test, y_pred, zero_division=0
    )
    recall = recall_score(
        y_test, y_pred, zero_division=0
    )
    f1 = f1_score(
        y_test, y_pred, zero_division=0
    )

    print(f"\n========== FINAL TEST: THRESHOLD {threshold} ==========")
    print("Accuracy:", round(accuracy, 4))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            y_pred,
            target_names=["Stayed (0)", "Churned (1)"],
            zero_division=0,
        )
    )

    return {
        "test_accuracy": accuracy,
        "test_churn_precision": precision,
        "test_churn_recall": recall,
        "test_churn_f1": f1,
    }


# -------------------- SAVE AND LOAD --------------------

def save_model(model, model_name, threshold, validation_f1):
    """Save the fitted pipeline and its prediction settings."""
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    model_bundle = {
        "model": model,
        "model_name": model_name,
        "threshold": threshold,
        "validation_f1": validation_f1,
    }

    joblib.dump(model_bundle, MODEL_PATH)
    print(f"\nTrained model saved to: {MODEL_PATH}")


def load_saved_model():
    """Load the saved pipeline and prediction settings."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Saved model not found: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


def save_results(results):
    """Save validation comparison and final test results to CSV."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    results_df = pd.DataFrame(results)
    results_df.to_csv(RESULTS_PATH, index=False)

    print(f"\nModel comparison saved to: {RESULTS_PATH}")
    print("\n--- MODEL COMPARISON SUMMARY ---")
    print(results_df.round(4).to_string(index=False))


# -------------------- MAIN WORKFLOW --------------------

def main():
    """Train, select, evaluate, and save the best model."""
    df, _ = load_data()
    print("Dataset shape:", df.shape)

    X, y = prepare_features(df)
    print("Features shape:", X.shape)
    print("Target shape:", y.shape)

    numeric_columns, categorical_columns = identify_columns(X)

    print("\nNumeric columns:", numeric_columns)
    print("Categorical columns:", categorical_columns)

    X_train, X_val, X_test, y_train, y_val, y_test = split_data(X, y)

    print("\nTraining rows:", len(X_train))
    print("Validation rows:", len(X_val))
    print("Testing rows:", len(X_test))

    models = [
        (
            "Logistic Regression",
            LogisticRegression(max_iter=1000),
        ),
        (
            "Random Forest",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42,
            ),
        ),
    ]

    candidates = []

    # Train and compare using validation data only.
    for name, classifier in models:
        print(f"\n{'=' * 50}")
        print(f"MODEL: {name}")
        print(f"{'=' * 50}")

        model = build_model(
            numeric_columns,
            categorical_columns,
            classifier,
        )

        model.fit(X_train, y_train)

        threshold, validation_f1 = select_threshold(
            model,
            X_val,
            y_val,
        )

        candidates.append(
            {
                "model_name": name,
                "model": model,
                "threshold": threshold,
                "validation_f1": validation_f1,
            }
        )

    # Select the best candidate using validation F1.
    best_candidate = max(
        candidates,
        key=lambda candidate: candidate["validation_f1"],
    )

    best_model = best_candidate["model"]
    best_name = best_candidate["model_name"]
    best_threshold = best_candidate["threshold"]
    best_validation_f1 = best_candidate["validation_f1"]

    print("\n" + "=" * 50)
    print("SELECTED MODEL:", best_name)
    print("Validation F1:", round(best_validation_f1, 4))
    print("Selected threshold:", best_threshold)
    print("=" * 50)

    # Evaluate the selected model on the test set only once.
    test_metrics = evaluate_model(
        best_model,
        X_test,
        y_test,
        best_threshold,
    )

    # Save the selected pipeline, threshold, and metadata.
    save_model(
        best_model,
        best_name,
        best_threshold,
        best_validation_f1,
    )

    # Save the comparison results.
    results = []

    for candidate in candidates:
        row = {
            "model": candidate["model_name"],
            "threshold": candidate["threshold"],
            "validation_f1": candidate["validation_f1"],
            "selected": candidate["model_name"] == best_name,
        }

        if candidate["model_name"] == best_name:
            row.update(test_metrics)

        results.append(row)

    save_results(results)

    print("\nTraining and model selection completed!")


if __name__ == "__main__":
    main()
