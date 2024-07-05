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
        # scikit-learn 1.5.0
        # joblib 1.4.2

from sklearn.metrics import classification_report
import joblib

from load_sqlite import get_eval_sqlite
from load_mongodb import get_eval_mongo

def evaluate_model(model, X, y): # Evaluate the model and return classification report
    y_pred = model.predict(X)
    return (classification_report(y, y_pred))

def infer_model(database, model_path, db_path=""):
    model = joblib.load(model_path) # Load the trained model
    
    # Loads the eval data from Mongo if database is MongoDB, else loads from SQLite
    test_data, val_data, sup_data = get_eval_mongo() if database == 'MongoDB' else get_eval_sqlite(db_path)
    
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