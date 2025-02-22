# scripts/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

# Load dataset
data = pd.read_csv("../backend/creditcard.csv")

# Split features and target
X = data.drop("Class", axis=1)
y = data["Class"]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = XGBClassifier(random_state=42)
#model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "../backend/fraud_detection_model.pkl")