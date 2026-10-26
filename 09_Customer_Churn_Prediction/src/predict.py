import pandas as pd

from prepare_data import load_saved_model


def get_choice(prompt, options):
    print(f"\n{prompt}")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        try:
            choice = int(input("Apna option number enter karein: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print("Invalid option. Dobara try karein.")

        except ValueError:
            print("Please sirf number enter karein.")


def get_number(prompt, value_type):
    while True:
        try:
            return value_type(input(prompt))
        except ValueError:
            print("Invalid number. Dobara enter karein.")


def get_new_customer():
    print("\n===== NEW CUSTOMER INFORMATION =====")

    new_customer = {
        "gender": get_choice(
            "Gender", ["Male", "Female"]
        ),

        "SeniorCitizen": get_choice(
            "Senior citizen?", ["0 - No", "1 - Yes"]
        ),

        "Partner": get_choice(
            "Has partner?", ["Yes", "No"]
        ),

        "Dependents": get_choice(
            "Has dependents?", ["Yes", "No"]
        ),

        "tenure": get_number(
            "Tenure in months: ", int
        ),

        "PhoneService": get_choice(
            "Phone service?", ["Yes", "No"]
        ),

        "MultipleLines": get_choice(
            "Multiple lines",
            ["Yes", "No", "No phone service"]
        ),

        "InternetService": get_choice(
            "Internet service",
            ["DSL", "Fiber optic", "No"]
        ),

        "OnlineSecurity": get_choice(
            "Online security",
            ["Yes", "No", "No internet service"]
        ),

        "OnlineBackup": get_choice(
            "Online backup",
            ["Yes", "No", "No internet service"]
        ),

        "DeviceProtection": get_choice(
            "Device protection",
            ["Yes", "No", "No internet service"]
        ),

        "TechSupport": get_choice(
            "Tech support",
            ["Yes", "No", "No internet service"]
        ),

        "StreamingTV": get_choice(
            "Streaming TV",
            ["Yes", "No", "No internet service"]
        ),

        "StreamingMovies": get_choice(
            "Streaming movies",
            ["Yes", "No", "No internet service"]
        ),

        "Contract": get_choice(
            "Contract type",
            ["Month-to-month", "One year", "Two year"]
        ),

        "PaperlessBilling": get_choice(
            "Paperless billing", ["Yes", "No"]
        ),

        "PaymentMethod": get_choice(
            "Payment method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        ),

        "MonthlyCharges": get_number(
            "Monthly charges: ", float
        ),

        "TotalCharges": get_number(
            "Total charges: ", float
        ),
    }

    new_customer["SeniorCitizen"] = int(
        new_customer["SeniorCitizen"][0]
    )

    return pd.DataFrame([new_customer])


def predict_customer():
    bundle = load_saved_model()

    model = bundle["model"]
    threshold = bundle["threshold"]

    customer = get_new_customer()

    probability = model.predict_proba(customer)[0, 1]
    prediction = int(probability >= threshold)

    print("\n===== CHURN PREDICTION =====")
    print(f"Churn probability: {probability:.2%}")
    print(f"Selected threshold: {threshold}")

    if prediction == 1:
        print("Prediction: Customer may churn.")
    else:
        print("Prediction: Customer is less likely to churn.")


if __name__ == "__main__":
    predict_customer()
