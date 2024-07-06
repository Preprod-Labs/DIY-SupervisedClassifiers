# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Developer details: 
        # Name: Mohini T and Vansh R
        # Role: Architect
        # Code ownership rights: Mohini T and Vansh R
    # Version:
        # Version: V 1.1 (05 July 2024)
            # Developer: Mohini T and Vansh R
            # Unit test: Pass
            # Integration test: Pass
     
    # Description: Takes user inputs for features and outputs a prediction using one of the saved models.

        # MYSQL: Yes
        # MQs: No
        # Cloud: No
        # Data versioning: No
        # Data masking: No


# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Python: 3.11.5
        # Pandas: 2.2.2

import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from load import load_train_data

def load_model_and_encoder(model_path, mysql_db_url, mysql_db_name):
    # Load the trained model
    model = joblib.load(model_path)
    
    # Fetch a sample of training data to fit the label encoder
    X_train, y_train = load_train_data(mysql_db_url, mysql_db_name)
    label_encoder = LabelEncoder()
    label_encoder.fit(y_train)
    
    return model, label_encoder

def get_user_input():
    # Get user input for features
    print("Please enter the following features:")
    temperature = float(input("Temperature: "))
    humidity = float(input("Humidity: "))
    wind_speed = float(input("Wind Speed: "))
    
    # Create a DataFrame with the correct feature names
    features = pd.DataFrame([[temperature, humidity, wind_speed]], columns=['temperature', 'humidity', 'wind_speed'])
    return features

def manual_prediction(temperature, humidity, wind_speed, model_path, mysql_db_url, mysql_db_name):
    model_path = 'ridge_classifier.pkl'  # Path to the Ridge Classifier model
    model, label_encoder = load_model_and_encoder(model_path, mysql_db_url, mysql_db_name)
    
    features = pd.DataFrame([[temperature, humidity, wind_speed]], columns=['temperature', 'humidity', 'wind_speed'])

    # Scale the features
    X_train, _ = load_train_data(mysql_db_url, mysql_db_name)
    scaler = StandardScaler()
    scaler.fit(X_train)  # Fit scaler on the training data
    scaled_features = scaler.transform(features)
    
    # Make prediction
    prediction = model.predict(scaled_features)
    weather_prediction = label_encoder.inverse_transform(prediction)
    
    return weather_prediction[0]