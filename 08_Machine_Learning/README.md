# Iris Flower Classification 🌸

This is one of my Machine Learning projects, where I built a model to predict the type of an Iris flower based on its measurements.

I used Python and Scikit-learn to train a Random Forest model and tested how well it could predict flower species. I also saved the trained model so I could use it later without training it again.

## What I Learned

- How to work with a dataset using Scikit-learn.
- How to split data into training and testing sets.
- How to train a Machine Learning model.
- How to check model performance using accuracy and a classification report.
- How to save a trained model and use it to make predictions.

## Tools & Libraries

- Python
- Scikit-learn
- Joblib

## About the Dataset

I used the built-in Iris dataset from Scikit-learn. It contains 150 flower samples from three species: Setosa, Versicolor, and Virginica.

The model uses four measurements to make a prediction:
- Sepal length
- Sepal width
- Petal length
- Petal width

## Project Structure

```text
08_Machine_Learning/
├── train.py
├── predict.py
├── requirements.txt
└── models/
    └── iris_model.joblib
```

## How to Run

First, install the required libraries:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train.py
```

Make a prediction:

```bash
python predict.py
```

## Results

The model achieved **90% accuracy** during my test run.

I built this project to get more practical experience with Machine Learning and understand how a model is trained, evaluated, saved, and used for predictions.

More projects coming as I continue learning AI and Machine Learning.
