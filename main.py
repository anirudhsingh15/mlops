from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# ... imports ...

app = FastAPI(
    title="Iris Species Predictor",
    description="A production-ready API for classifying Iris flowers using Logistic Regression.",
    version="1.0.0"
)

# ... load model ...

class IrisFeatures(BaseModel):
    """
    Input schema for the Iris prediction model.
    Values should be in centimeters.
    """
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict", tags=["Inference"])
def predict_species(features: IrisFeatures):
    """
    Predicts the species of an Iris flower based on sepal and petal measurements.

    Args:
        features (IrisFeatures): The physical measurements of the flower.

    Returns:
        dict: The predicted class ID and species name.
    """
    # ... your existing code ...
    
# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Define the Input Data Structure (Validation)
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI()
model = None

# 2. Load the Model on Startup
@app.on_event("startup")
def load_model():
    global model
    model = joblib.load("iris_model.pkl")
    print("ML Model Loaded.")

@app.get("/")
def read_root():
    return {"project": "mlops-api", "status": "ready"}

# 3. The Prediction Endpoint
@app.post("/predict")
def predict_species(features: IrisFeatures):
    # Prepare data for the model
    data = [[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width
    ]]
    
    # Make Prediction
    prediction = model.predict(data)[0]
    class_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
    
    return {
        "prediction_class": int(prediction),
        "prediction_name": class_map[prediction]
    }
