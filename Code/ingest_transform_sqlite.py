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
        # scikit-learn 1.5.0

import pandas as pd
from sklearn.model_selection import train_test_split
import sqlite3

def transform_data(data): # Transform raw data for model training
    data = pd.get_dummies(data, columns=['vehicle_type'], drop_first=True)
    X = data.drop(columns=['claim', 'policy_id'])
    y = data['claim']
    return X, y

def split_data(X, y): # Split data into training, testing, validation, and supervalidation sets.
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

def store_to_sqlite(data, table_name, db_path='D:\PreProd Corp\DIY-SupervisedClassifiers\Data\Processed\processed_data.db'): # Store data into SQLite database
    conn = sqlite3.connect(db_path) # Connect to the SQLite database
    data.to_sql(table_name, conn, index=False, if_exists='replace') # Store the data into the specified table
    conn.close() # Close the database connection

def sqlite_data(): # Ingest, transform, and store data into SQLite.
    data = pd.read_csv('D:\PreProd Corp\DIY-SupervisedClassifiers\Data\Master\mock_data.csv')
    X, y = transform_data(data)
    train_data, test_data, val_data, superval_data = split_data(X, y)
    
    # Store to SQLite
    store_to_sqlite(train_data, 'training_data')
    store_to_sqlite(test_data, 'testing_data')
    store_to_sqlite(val_data, 'validation_data')
    store_to_sqlite(superval_data, 'supervalidation_data')

    # Print a success message
    print("Data successfully ingested, transformed, and stored to SQLite.")

if __name__ == "__main__":
    sqlite_data()