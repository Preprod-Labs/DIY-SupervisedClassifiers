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

# Description: This code takes user inputs for features and makes predictions using a pre-trained K-Nearest Neighbors model.
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
        # Numpy 2.0.0
        # joblib 1.4.2

import joblib
import numpy as np

def manual_predict(age, vehicle_age, annual_mileage, accident_history, vehicle_type):
    # Load the pre-trained K-Nearest Neighbors model
    model = joblib.load('D:\PreProd Corp\DIY-SupervisedClassifiers\knn_model.pkl')
    
    # Encode the vehicle type
    vehicle_type_encoded = [0, 0, 0, 0]  # [SUV, Sedan, Tractor, Truck]
    if vehicle_type == "SUV":
        vehicle_type_encoded[0] = 1
    elif vehicle_type == "Sedan":
        vehicle_type_encoded[1] = 1
    elif vehicle_type == "Tractor":
        vehicle_type_encoded[2] = 1
    elif vehicle_type == "Truck":
        vehicle_type_encoded[3] = 1
    
    # Prepare the input data
    input_data = [age, vehicle_age, annual_mileage, accident_history] + vehicle_type_encoded
    
    # Make the prediction
    prediction = model.predict([input_data])
    
    # Return the prediction result
    return (f"Prediction: {'Claim' if prediction[0] else 'No Claim'}")

if __name__ == "__main__":
    manual_predict()