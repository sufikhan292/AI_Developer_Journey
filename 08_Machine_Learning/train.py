from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "iris_model.joblib"


def load_data():
    """Load the Iris dataset."""
    iris = load_iris()
    X = iris.data
    y = iris.target

    return X, y, iris.target_names, iris.feature_names


def train_model(X_train, y_train):
    """Create and train the classification model."""
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, target_names):
    """Evaluate model performance."""
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=target_names
        )
    )


def save_model(model, target_names, feature_names):
    """Save the trained model and its metadata."""
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    artifact = {
        "model": model,
        "target_names": target_names,
        "feature_names": feature_names
    }

    joblib.dump(artifact, MODEL_PATH)
    print(f"\nModel saved to: {MODEL_PATH}")


def main():
    X, y, target_names, feature_names = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = train_model(X_train, y_train)

    evaluate_model(
        model,
        X_test,
        y_test,
        target_names
    )

    save_model(model, target_names, feature_names)


if __name__ == "__main__":
    main()
