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

# Description: This code loads the data from MongoDB database.
    # MongoDB: Yes

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Python 3.11.5
        # Pandas 2.2.2
        # pymongo 4.7.3

import pandas as pd # For data manipulation
from pymongo import MongoClient # For MongoDB

def load_from_mongo(collection_name): # Load data from MongoDB
    client = MongoClient('mongodb://localhost:27017/') # Connect to MongoDB
    db = client['insurance_db'] # Select the database
    collection = db[collection_name] # Select the collection
    data = pd.DataFrame(list(collection.find())) # Fetch the data from the collection
    data.drop(columns=['_id'], inplace=True) # Drop the MongoDB default '_id' field
    return data # Return the data

def get_train_mongo():
    # Load and return training data from MongoDB
    train_data = load_from_mongo('training_data')
    
    return train_data
    
def get_eval_mongo():
    # Load and return the evaluation data from MongoDB
    
    test_data = load_from_mongo('testing_data')
    val_data = load_from_mongo('validation_data')
    sup_data = load_from_mongo('supervalidation_data')
    
    return test_data, val_data, sup_data