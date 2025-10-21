from fastapi import FastAPI
from app.schemas import HeartData
from app.model_loader import load_model

import pandas as pd

# -----------------------
# Step 1: Initialize app
# -----------------------
app = FastAPI(
    title="Heart Disease Prediction API",
    description="Predicts the presence of heart disease using a trained ML model",
    version="1.0"
)

# -----------------------
# Step 2: Load model
# -----------------------
model = load_model()  # uses the function from model_loader.py

# -----------------------
# Step 3: Health endpoint
# -----------------------
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}

# -----------------------
# Step 4: Info endpoint
# -----------------------
@app.get("/info")
def model_info():
    features = [
        "age","sex","cp","trestbps","chol","fbs","restecg","thalach",
        "exang","oldpeak","slope","ca","thal"
    ]
    return {"model": "RandomForestClassifier", "features": features}

# -----------------------
# Step 5: Predict endpoint
# -----------------------
@app.post("/predict")
def predict(data: HeartData):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]
    return {"heart_disease": bool(prediction)}
