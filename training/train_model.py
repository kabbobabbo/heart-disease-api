import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

# 1. Load dataset
df = pd.read_csv("heart.csv")

# 2. Prepare features & target
X = df.drop("target", axis=1)
y = df["target"]

# 3. Split data into train/test (80%/20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train a simple Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Test accuracy (optional, just to check)
acc = model.score(X_test, y_test)
print(f"Model trained! Test accuracy: {acc:.2f}")

# 6. Save the model
dump(model, "model/heart_model.joblib")
print("Model saved as model/heart_model.joblib")
