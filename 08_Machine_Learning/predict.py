from pathlib import Path

import joblib

BASE_DIR=Path(__file__).resolve().parent
MODEL_PATH=BASE_DIR/"models"/"iris_model.joblib"

def load_model():
    """Saved model ko load karna."""
    artifact=joblib.load(MODEL_PATH)

    return(
        artifact["model"],
        artifact["target_names"],
        artifact["feature_names"]
    )


def predict_flower():
    """Naye flower ki type predict karna."""
    model,target_names,feature_names=load_model()

    measurements=[[5.1,3.5,1.4,0.2]]

    prediction=model.predict(measurements)

    flower_name=target_names[prediction[0]]

    print("Flower measurement",measurements[0])
    print("Prediction flower",flower_name)

if __name__=="__main__":
    predict_flower()