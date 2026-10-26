# Customer Churn Prediction

## Project Overview

This project uses Machine Learning to predict whether a telecom customer is likely to leave the company (churn) based on customer account information, subscribed services, contract type, and billing details.

The goal is to identify customers who may be at risk of leaving so that businesses can take proactive retention measures.

## Features

- Dataset auditing and exploratory data analysis (EDA)
- Handling missing values in `TotalCharges`
- Separating numerical and categorical features
- Numerical scaling using `StandardScaler`
- Categorical encoding using `OneHotEncoder`
- Machine Learning pipeline using Scikit-learn
- Comparison of Logistic Regression and Random Forest
- Threshold selection using validation F1-score
- Model evaluation on an independent test set
- Saving and loading the trained model
- Predicting churn for a new customer through a Python script

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn
- Joblib

## Project Structure

```text
09_Customer_Churn_Prediction/
├── data/
│   └── raw/
│       └── Telco-Customer-Churn.csv
├── src/
│   ├── data_audit.py
│   ├── eda.py
│   ├── prepare_data.py
│   └── predict.py
├── models/
│   └── best_churn_model.joblib
├── reports/
│   ├── churn_by_contract.png
│   └── model_comparison.csv
├── notebooks/
├── requirements.txt
└── README.md
```

## Dataset

The project uses the IBM Telco Customer Churn dataset containing 7,043 customer records and 21 columns.

The target column is `Churn`:

- `No` → 0 (customer stayed)
- `Yes` → 1 (customer churned)

The `customerID` column is excluded from model training because it is an identifier rather than a predictive customer feature.

For the 11 missing `TotalCharges` values associated with zero-tenure customers, the project assigns `0.0`. This is an assumption based on the customers' zero tenure and should be validated where possible.

## Model Training and Evaluation

The dataset is divided into training, validation, and test sets.

Two classifiers are compared:

1. Logistic Regression
2. Random Forest

The validation set is used to select the classification threshold based on F1-score. The test set is reserved for final evaluation of the selected model.

### Final Test Results

The selected model is Logistic Regression.

| Metric | Result |
|---|---:|
| Accuracy | 75.37% |
| Churn Precision | 52.51% |
| Churn Recall | 75.40% |
| Churn F1-score | 61.91% |
| Selected Threshold | 0.30 |

These results reflect the current experiment and are not a guarantee of future performance.

## Installation

Clone the repository and navigate to the project directory.

Install the required dependencies:

pip install -r requirements.txt

Ensure the dataset is available at:

data/raw/Telco-Customer-Churn.csv

Usage

Run the data audit:

python src/data_audit.py

Generate the EDA report:

python src/eda.py

Train, compare, evaluate, and save the selected model:

python src/prepare_data.py

Predict churn for a new customer:

python src/predict.py

The prediction script asks for customer information in the terminal and returns an estimated churn probability and a classification based on the selected threshold.

Important Notes

The selected threshold of 0.30 was chosen using validation data.

A predicted churn probability is a model estimate, not a guarantee.

Model performance may change when the model is applied to new data.

The current prediction script uses manually entered customer information.

Future Improvements

Build a FastAPI endpoint for churn predictions.

Add stronger input validation.

Create a web-based prediction form.

Monitor model performance on new customer data.

Reassess the missing-value assumption and threshold as appropriate.

Author

AI Developer Journey — Machine Learning Project