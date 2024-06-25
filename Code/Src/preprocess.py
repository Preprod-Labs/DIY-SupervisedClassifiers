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
     
    # Description: This code fetches weather data from a MySQL database, preprocesses it by dropping unnecessary columns, encoding categorical weather data, scaling numerical features, and saves the scaler object for prediction.
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
from sklearn.preprocessing import StandardScaler, LabelEncoder # Used to preprocess the data (scale and encode)
import joblib # Used to save the scaler object

def fetch_data_from_db(connection):
    query = "SELECT * FROM weather"
    df = pd.read_sql(query, connection)
    return df

def preprocess_data(df):
    # Drop the 'day' column
    df = df.drop(columns=['day'])
    
    # Encode the 'weather' column
    label_encoder = LabelEncoder()
    df['weather'] = label_encoder.fit_transform(df['weather'])
    
    # Print the mapping of original labels to encoded labels
    print("Encoded weather classes:", label_encoder.classes_)
    
    # Scale the numerical columns
    scaler = StandardScaler()
    df[['temperature', 'humidity', 'wind_speed']] = scaler.fit_transform(df[['temperature', 'humidity', 'wind_speed']])
    
    # Save the scaler object as a pickle file using joblib
    joblib.dump(scaler, 'scaler.pkl')
    
    return df