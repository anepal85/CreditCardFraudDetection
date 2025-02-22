from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import joblib
import numpy as np
import os 

# Initialize FastAPI app
app = FastAPI()

# Load the trained XGBoost model
model_path = os.path.join(os.path.dirname(__file__), "..", "fraud_detection_model.pkl")
model = joblib.load(model_path)

# Define input data schema for single prediction
class SingleInput(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

# Define input data schema for batch prediction
class BatchInput(BaseModel):
    data: List[SingleInput]

# Single prediction endpoint
@app.post("/predict")
def predict_single(input_data: SingleInput):
    try:
        # Convert input data to numpy array
        input_array = np.array(list(input_data.model_dump().values())).reshape(1, -1)
        # Make prediction
        prediction = model.predict(input_array)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Batch prediction endpoint
@app.post("/predict_batch")
def predict_batch(input_data: BatchInput):
    try:
        # Convert input data to numpy array
        input_list = [list(row.model_dump().values()) for row in input_data.data]
        input_array = np.array(input_list)
        # Make predictions
        predictions = model.predict(input_array)
        return {"predictions": predictions.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Fraud Detection API"}