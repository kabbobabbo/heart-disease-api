import joblib
import os

# Ensure the path is correct for Docker/Render
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'heart_model.joblib')
model = joblib.load(MODEL_PATH)
