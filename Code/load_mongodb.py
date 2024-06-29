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

# Description: This code loads the data from MongoDB and stores it into .csv files in the Processed folder.
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
        # pymongo 4.7.3

import pandas as pd
from pymongo import MongoClient

def load_from_mongo(collection_name): # Load data from MongoDB
    client = MongoClient('mongodb://localhost:27017/') # Connect to MongoDB
    db = client['insurance_db'] # Select the database
    collection = db[collection_name] # Select the collection
    data = pd.DataFrame(list(collection.find())) # Fetch the data from the collection
    data.drop(columns=['_id'], inplace=True) # Drop the MongoDB default '_id' field
    return data # Return the data

def call_mongo():
    # Load data from MongoDB
    train_data = load_from_mongo('training_data')
    test_data = load_from_mongo('testing_data')
    val_data = load_from_mongo('validation_data')
    sup_data = load_from_mongo('supervalidation_data')
    
    # Save to CSV
    train_data.to_csv('D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/MongoDB/training_data.csv', index=False)
    test_data.to_csv('D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/MongoDB/testing_data.csv', index=False)
    val_data.to_csv('D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/MongoDB/validation_data.csv', index=False)
    sup_data.to_csv('D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/MongoDB/supervalidation_data.csv', index=False)

    # Print a success message
    print("Data sucessfully loaded from MongoDB and stored in .csv files.")

if __name__ == "__main__":
    call_mongo()