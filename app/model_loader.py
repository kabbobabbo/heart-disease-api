import joblib
import os

def load_model():
    """
    Load the trained RandomForest model.
    Handles deployment path inside Docker/Render.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "..", "model", "heart_model.joblib")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")
    
    model = joblib.load(model_path)
    return model
