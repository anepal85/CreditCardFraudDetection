from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import joblib
import os
import logging
from .model import SingleInput, BatchInput

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from React app
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the trained XGBoost model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "..", "fraud_detection_model.pkl")
model = joblib.load(model_path)

# Single prediction endpoint
@app.post("/predict")
def predict_single(input_data: SingleInput):
    try:
        logger.info(f"Received input data: {input_data}")
        # Convert input data to numpy array
        input_array = np.array(list(input_data.dict().values())).reshape(1, -1)
        logger.info(f"Input array: {input_array}")
        # Make prediction
        prediction = model.predict(input_array)
        logger.info(f"Prediction: {prediction}")
        return {"prediction": int(prediction[0])}
    except Exception as e:
        logger.error(f"Error making prediction: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Batch prediction endpoint
@app.post("/predict_batch")
def predict_batch(input_data: BatchInput):
    try:
        logger.info(f"Received batch input data: {input_data}")
        # Convert input data to numpy array
        input_list = [list(row.dict().values()) for row in input_data.data]
        input_array = np.array(input_list)
        logger.info(f"Input array: {input_array}")
        # Make predictions
        predictions = model.predict(input_array)
        logger.info(f"Predictions: {predictions}")
        return {"predictions": predictions.tolist()}
    except Exception as e:
        logger.error(f"Error making batch prediction: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint to serve the test dataset
@app.get("/test_data")
def get_test_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(current_dir, "..", "test.csv")
    return FileResponse(test_data_path)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Fraud Detection API"}