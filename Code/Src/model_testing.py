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
     
    # Description: This code loads test data and a trained model to evaluate the model's performance on the test set, calculating and returning the test accuracy.
        # MYSQL: Yes
        # MQs: No
        # Cloud: No
        # Data versioning: No
        # Data masking: No


# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        #Streamlit: 1.36.0

# Loading the necessary libraries
import pandas as pd # Used to load the data
import joblib # Used to save the model
from sklearn.metrics import accuracy_score # Used to calculate the accuracy of the model

def test_model():
    # Load the test data
    X_test = pd.read_csv('Data/Processed/X_test.csv')
    y_test = pd.read_csv('Data/Processed/y_test.csv')
    
    # Load the model
    model = joblib.load('model.pkl')
    
    # Test the model
    y_pred_test = model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred_test)
    
    return test_accuracy