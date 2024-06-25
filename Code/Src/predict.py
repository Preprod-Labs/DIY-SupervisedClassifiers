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
     
    # Description: This code preprocesses new weather data, scales it using a preloaded scaler, and predicts the weather using a preloaded machine learning model. It returns the predicted weather condition.
        # MYSQL: Yes
        # MQs: No
        # Cloud: No
        # Data versioning: No
        # Data masking: No


# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Pandas: 2.2.2

# Loading the necessary libraries
import pandas as pd # Used to load the data
import joblib # Used to load the model

def preprocess_new_data(data, scaler):
    # Convert new data to DataFrame
    df = pd.DataFrame([data], columns=['temperature', 'humidity', 'wind_speed'])
    
    # Scale the numerical columns
    df[['temperature', 'humidity', 'wind_speed']] = scaler.transform(df[['temperature', 'humidity', 'wind_speed']])
    return df

def predict_weather(data):
    # Load the model
    model = joblib.load('model.pkl')
    
    # Load preprocessors and label mapping
    scaler = joblib.load('scaler.pkl')
    
    # Preprocess the new data
    df = preprocess_new_data(data, scaler)
    print(df)
    
    # Predict the weather
    prediction = model.predict(df)
    
    mapping = {0: 'Cloudy', 1: 'Rainy', 2: 'Sunny'}

    return mapping[prediction[0]]