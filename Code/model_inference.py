# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Developer details: 
    # Name: Mohini T
    # Role: Architect
    # Code ownership rights: Mohini T
# Version:
    # Version: V 1.0 (19 Mar 2024)
    # Developer: Mohini T
    # Unit test: Pass
    # Integration test: Pass

# Description: This code evaluates the K-Nearest Neighbors model on testing, validation, and supervalidation datasets.
    # MYSQL: No
    # NoSQL: Yes (MongoDB)
    # MQs: No
    # Cloud: No
    # Data versioning: No
    # Data masking: No

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Python 3.11.5
        # Pandas 2.2.2
        # scikit-learn 1.5.0
        # joblib 1.4.2

import pandas as pd
from sklearn.metrics import classification_report
import joblib

def evaluate_model(model, X, y): # Evaluate the model and return classification report
    y_pred = model.predict(X)
    return (classification_report(y, y_pred))

def infer_model(database):
    model = joblib.load('D:\PreProd Corp\DIY-SupervisedClassifiers\knn_model.pkl')
    
    test_data = pd.read_csv(f'D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/{database}/testing_data.csv') # Load testing data
    val_data = pd.read_csv(f'D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/{database}/validation_data.csv') # Load validation data
    sup_data = pd.read_csv(f'D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/{database}/supervalidation_data.csv') # Load supervalidation data
    
    X_test = test_data.drop(columns=['claim']) # Extract features from testing data
    y_test = test_data['claim'] # Extract labels from testing data
    X_val = val_data.drop(columns=['claim']) # Extract features from validation data
    y_val = val_data['claim'] # Extract labels from validation data
    X_sup = sup_data.drop(columns=['claim']) # Extract features from supervalidation data
    y_sup = sup_data['claim'] # Extract labels from supervalidation data
    
    print("Testing Data Classification Report:")
    test_eval = evaluate_model(model, X_test, y_test) # Evaluate model on testing data
    
    print("Validation Data Classification Report:")
    val_eval = evaluate_model(model, X_val, y_val) # Evaluate model on validation data
    
    print("Supervalidation Data Classification Report:")
    superval_eval = evaluate_model(model, X_sup, y_sup) # Evaluate model on supervalidation data

    return test_eval, val_eval, superval_eval

if __name__ == "__main__":
    infer_model(database='SQLite') # Run model inference on SQLite database