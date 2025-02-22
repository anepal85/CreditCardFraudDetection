import os
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

# Define paths
current_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of this script
backend_dir = os.path.dirname(current_dir)  # Parent directory (backend/)
creditcard_path = os.path.join(backend_dir, "creditcard.csv")  # Path to creditcard.csv
model_path = os.path.join(backend_dir, "fraud_detection_model.pkl")  # Path to save the model
test_data_path = os.path.join(backend_dir, "test.csv")  # Path to save test.csv

# Load dataset
print(f"Loading dataset from: {creditcard_path}")
data = pd.read_csv(creditcard_path)

# Split features and target
X = data.drop("Class", axis=1)
y = data["Class"]

# Split into train and test sets
print("Splitting dataset into train and test sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the test dataset
test_data = X_test.copy()
test_data["Class"] = y_test
print(f"Saving test dataset to: {test_data_path}")
test_data.to_csv(test_data_path, index=False)

# Train XGBoost model
print("Training XGBoost model...")
model = XGBClassifier(random_state=42)
model.fit(X_train, y_train)

# Save the model
print(f"Saving trained model to: {model_path}")
joblib.dump(model, model_path)

print("Training completed and files saved successfully!")