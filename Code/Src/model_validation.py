# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Developer details: 
        # Name: Vansh R
        # Role: Architect
        # Code ownership rights: Vansh R
    # Version:
        # Version: V 1.0 (24 July 2024)
            # Developer: Vansh R
            # Unit test: Pass
            # Integration test: Pass
     
    # Description: This code loads validation data and a trained model to evaluate the model's performance on the validation set, calculating and returning the validation accuracy.
        # MYSQL: Yes
        # MQs: No
        # Cloud: No
        # Data versioning: No
        # Data masking: No


# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Pandas: 2.2.2
        # Scikit-learn: 1.5.0

# Loading the necessary libraries
import pandas as pd # Used to load the data
import joblib # Used to save the model
from sklearn.metrics import accuracy_score # Used to calculate the accuracy of the model

def validate_model():
    # Load the validation data
    X_val = pd.read_csv('Data/Processed/X_val.csv')
    y_val = pd.read_csv('Data/Processed/y_val.csv')
    
    # Load the model
    model = joblib.load('model.pkl')
    
    # Validate the model
    y_pred_val = model.predict(X_val)
    val_accuracy = accuracy_score(y_val, y_pred_val)
    
    return val_accuracy
