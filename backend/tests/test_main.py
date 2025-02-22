import pytest
from fastapi.testclient import TestClient
from app.main import app

# Initialize TestClient
client = TestClient(app)

# Test data for single prediction
single_input = {
    "Time": 0.0,
    "V1": -1.359807,
    "V2": -0.072781,
    "V3": 2.536347,
    "V4": 1.378155,
    "V5": -0.338321,
    "V6": 0.462388,
    "V7": 0.239599,
    "V8": 0.098698,
    "V9": 0.363787,
    "V10": 0.090794,
    "V11": -0.551600,
    "V12": -0.617801,
    "V13": -0.991390,
    "V14": -0.311169,
    "V15": 1.468177,
    "V16": -0.470401,
    "V17": 0.207971,
    "V18": 0.025791,
    "V19": 0.403993,
    "V20": 0.251412,
    "V21": -0.018307,
    "V22": 0.277838,
    "V23": -0.110474,
    "V24": 0.066928,
    "V25": 0.128539,
    "V26": -0.189115,
    "V27": 0.133558,
    "V28": -0.021053,
    "Amount": 149.62
}

# Test data for batch prediction
batch_input = {
    "data": [
        {
            "Time": 0.0,
            "V1": -1.359807,
            "V2": -0.072781,
            "V3": 2.536347,
            "V4": 1.378155,
            "V5": -0.338321,
            "V6": 0.462388,
            "V7": 0.239599,
            "V8": 0.098698,
            "V9": 0.363787,
            "V10": 0.090794,
            "V11": -0.551600,
            "V12": -0.617801,
            "V13": -0.991390,
            "V14": -0.311169,
            "V15": 1.468177,
            "V16": -0.470401,
            "V17": 0.207971,
            "V18": 0.025791,
            "V19": 0.403993,
            "V20": 0.251412,
            "V21": -0.018307,
            "V22": 0.277838,
            "V23": -0.110474,
            "V24": 0.066928,
            "V25": 0.128539,
            "V26": -0.189115,
            "V27": 0.133558,
            "V28": -0.021053,
            "Amount": 149.62
        },
        {
            "Time": 0.0,
            "V1": 1.191857,
            "V2": 0.266151,
            "V3": 0.166480,
            "V4": 0.448154,
            "V5": 0.060018,
            "V6": -0.082361,
            "V7": -0.078803,
            "V8": 0.085102,
            "V9": -0.255425,
            "V10": -0.166974,
            "V11": 1.612727,
            "V12": 1.065235,
            "V13": 0.489095,
            "V14": -0.143772,
            "V15": 0.635558,
            "V16": 0.463917,
            "V17": -0.114805,
            "V18": -0.183361,
            "V19": -0.145783,
            "V20": -0.069083,
            "V21": -0.225775,
            "V22": -0.638672,
            "V23": 0.101288,
            "V24": -0.339846,
            "V25": 0.167170,
            "V26": 0.125895,
            "V27": -0.008983,
            "V28": 0.014724,
            "Amount": 2.69
        }
    ]
}

# Test single prediction endpoint
def test_predict_single():
    response = client.post("/predict", json=single_input)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert isinstance(response.json()["prediction"], int)

# Test batch prediction endpoint
def test_predict_batch():
    response = client.post("/predict_batch", json=batch_input)
    assert response.status_code == 200
    assert "predictions" in response.json()
    assert isinstance(response.json()["predictions"], list)
    assert len(response.json()["predictions"]) == 2