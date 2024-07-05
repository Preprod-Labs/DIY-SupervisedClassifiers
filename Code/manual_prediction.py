# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Developer details: 
    # Name: Mohini T and Vansh R
    # Role: Architects
    # Code ownership rights: Mohini T and Vansh R
# Version:
    # Version: V 1.1 (05 July 2024)
    # Developer: Mohini T and Vansh R
    # Unit test: Pass
    # Integration test: Pass

# Description: This code takes user inputs for features and makes predictions using a pre-trained
# K-Nearest Neighbors model.
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
        # joblib 1.4.2

import joblib

def manual_predict(age, vehicle_age, annual_mileage, accident_history, vehicle_type, model_path):
    # Load the pre-trained K-Nearest Neighbors model
    model = joblib.load(model_path)
    
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