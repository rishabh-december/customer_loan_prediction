#  Imports
import sys
import os
import yaml
from yaml.loader import SafeLoader
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import seaborn as sns
import pandas as pd

# Custom utility import
from utils.utility import load_dataset

# Adding Project Root to Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Extract paths from config
with open('src/config/config.yaml') as f:
        config = yaml.load(f, Loader=SafeLoader)

#Load and Preprocess Dataset
base_path, data= config["base_path"], config["data"]
df = load_dataset(base_path, data)


# Encode target variable: "Y" -> 1, "N" -> 
y = df['Loan_Status'].map({"Y": 1, "N": 0})

# Drop target column to form features
X = X = df.drop("Loan_Status", axis=1)

# One-hot encoding of categorical variables
X = pd.get_dummies(X, drop_first=True)


# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Train Model (XGBoost)
model = XGBClassifier(random_state = 42, eval_metric = 'logloss')
model.fit(X_train, y_train)

#Evaluate Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
