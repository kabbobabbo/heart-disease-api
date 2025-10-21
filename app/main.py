from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from app.schemas import HeartData  # Your Pydantic model

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
model = joblib.load("model/heart_model.joblib")

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
    features = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach",
                "exang","oldpeak","slope","ca","thal"]
    return {"model": "RandomForestClassifier", "features": features}

# -----------------------
# Step 5: Predict endpoint
# -----------------------
@app.post("/predict")
def predict(data: HeartData):
    # Convert Pydantic model to DataFrame with column names
    df = pd.DataFrame([data.dict()])  
    
    # Predict using the trained model
    prediction = model.predict(df)[0]
    
    # Convert 0/1 to True/False
    result = bool(prediction)
    
    return {"heart_disease": result}
