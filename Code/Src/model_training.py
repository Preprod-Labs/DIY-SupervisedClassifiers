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
     
    # Description: This code loads preprocessed training data, trains a Gaussian Naive Bayes model, and saves the trained model to a file.
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

# Import the necessary libraries
import pandas as pd # Used to load the data
from sklearn.naive_bayes import GaussianNB # Used to import the Gaussian Naive Bayes model from the scikit-learn library
import joblib # Used to save the model

def train_model():
    # Load the preprocessed training data
    X_train = pd.read_csv('Data/Processed/X_train.csv')
    y_train = pd.read_csv('Data/Processed/y_train.csv').values.ravel()  # Ensure y_train is a 1D array
    
    # Train the model
    model = GaussianNB()
    model.fit(X_train, y_train)
    
    # Save the model
    joblib.dump(model, 'model.pkl')
    
    print('Model trained and saved successfully!')
