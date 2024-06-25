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
     
    # Description: This code splits weather data into training, test, validation, and supervalidation sets using train_test_split from scikit-learn and saves them as CSV files for further processing.
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

# Import necessary libraries
import pandas as pd # Used to load the data
from sklearn.model_selection import train_test_split # Used to split the data into train, test, validation, and supervalidation sets

def split_data(df):
    # Split features and target
    X = df[['temperature', 'humidity', 'wind_speed']]
    y = df['weather']
    
    # Split the data into train, test, validation, and supervalidation sets
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
    X_test, X_temp, y_test, y_temp = train_test_split(X_temp, y_temp, test_size=0.625, random_state=42) # 0.625 * 0.4 = 0.25
    X_val, X_superval, y_val, y_superval = train_test_split(X_temp, y_temp, test_size=0.4, random_state=42) # 0.4 * 0.25 = 0.1
    
    # Save the split data
    X_train.to_csv('Data/Processed/X_train.csv', index=False)
    y_train.to_csv('Data/Processed/y_train.csv', index=False)
    X_test.to_csv('Data/Processed/X_test.csv', index=False)
    y_test.to_csv('Data/Processed/y_test.csv', index=False)
    X_val.to_csv('Data/Processed/X_val.csv', index=False)
    y_val.to_csv('Data/Processed/y_val.csv', index=False)
    X_superval.to_csv('Data/Processed/X_superval.csv', index=False)
    y_superval.to_csv('Data/Processed/y_superval.csv', index=False)
    
    print('Data ingested, preprocessed, and split successfully!')