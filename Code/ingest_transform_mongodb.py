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

# Description: This code ingests the original data, transforms it, and stores it into MongoDB.
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
        # Pandas 2.2.2
        # scikit-learn 1.5.0
        # pymongo 4.7.3

import pandas as pd
from sklearn.model_selection import train_test_split
from pymongo import MongoClient


def transform_data(data): # Transform raw data for model training
    # Convert categorical variable 'vehicle_type' into dummy variables
    
    print()
    data = pd.get_dummies(data, columns=['vehicle_type'], drop_first=True)
    
    print(data.head())
    
    # Separate features (X) and target variable (y)
    X = data.drop(columns=['claim', 'policy_id'])
    y = data['claim']
    
    return X, y

def split_data(X, y):
    # Combine X and y into a single DataFrame
    df = X.copy()
    df['claim'] = y

    # Shuffle the data before splitting
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Split data into training (600) and temp (400)
    train_data, temp_data = train_test_split(df, train_size=600, random_state=42, stratify=df['claim'])
    
    # Split temp data into testing (150) and remaining (250)
    test_data, val_superval_data = train_test_split(temp_data, train_size=150, random_state=42, stratify=temp_data['claim'])
    
    # Split remaining data into validation (150) and supervalidation (100)
    val_data, superval_data = train_test_split(val_superval_data, train_size=150, random_state=42, stratify=val_superval_data['claim'])
    
    return train_data, test_data, val_data, superval_data

def store_to_mongo(data, collection_name): # Store data into MongoDB
    client = MongoClient('mongodb://localhost:27017/') # Connect to MongoDB
    db = client['insurance_db'] # Select the database
    collection = db[collection_name] # Select the collection
    collection.insert_many(data.to_dict('records')) # Insert the data into the collection

def mongo_data(data_path): # Ingest, transform, and store data into MongoDB

    data = pd.read_csv(data_path) # Load the data
    
    X, y = transform_data(data) # Transform data
    train_data, test_data, val_data, superval_data = split_data(X, y) # Split data

    # Store to MongoDB
    store_to_mongo(train_data, 'training_data')
    store_to_mongo(test_data, 'testing_data')
    store_to_mongo(val_data, 'validation_data')
    store_to_mongo(superval_data, 'supervalidation_data')

    # Print a success message
    print("Data ingested, transformed, and stored to mongoDB successfully.")

if __name__ == "__main__":
    mongo_data('Data/Master/mock_data.csv')