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
     
    # Description: This code loads supervalidation data and a trained model to evaluate the model's performance on the supervalidation set, calculating the accuracy and returning the predictions in a DataFrame.

        # MYSQL: Yes
        # Streamlit: Yes
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

def supervalidate_model():
    # Load the supervalidation data
    X_superval = pd.read_csv('Data/Processed/X_superval.csv')
    y_superval = pd.read_csv('Data/Processed/y_superval.csv')
    
    # Load the model
    model = joblib.load('model.pkl')
    
    # Supervalidate the model
    y_pred_superval = model.predict(X_superval)
    superval_accuracy = accuracy_score(y_superval, y_pred_superval)
    
    # Convert predictions to DataFrame for clarity
    predictions_df = pd.DataFrame({
        'Actual': y_superval.values.flatten(),  # Flatten to match y_pred_superval shape
        'Predicted': y_pred_superval
    })
    
    return superval_accuracy, predictions_df
