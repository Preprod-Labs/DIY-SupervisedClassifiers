# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Developer details: 
    # Name: Mohini T and Vansh R
    # Role: Architects
    # Code ownership rights: Mohini T and Vansh R
# Version:
    # Version: V 1.0 (05 July 2024)
    # Developer: Mohini T and Vansh R
    # Unit test: Pass
    # Integration test: Pass

# Description: This code ingests the original data, transforms it, and stores it into SQLite database.
    # SQLite: Yes

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Python 3.11.5
        # Pandas 2.2.2
        # Scikit-learn 1.5.0

import pandas as pd # For data manipulation
from sklearn.model_selection import train_test_split # For splitting data
import sqlite3 # For SQLite

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

def store_to_sqlite(data, table_name, db_path): # Store data into SQLite database
    conn = sqlite3.connect(db_path) # Connect to the SQLite database
    data.to_sql(table_name, conn, index=False, if_exists='replace') # Store the data into the specified table
    conn.close() # Close the database connection

def sqlite_data(data_path, db_path): # Ingest, transform, and store data into SQLite.
    
    # Load the data
    data = pd.read_csv(data_path)
    
    X, y = transform_data(data)
    train_data, test_data, val_data, superval_data = split_data(X, y)
    
    # Store to SQLite
    store_to_sqlite(train_data, 'training_data', db_path)
    store_to_sqlite(test_data, 'testing_data', db_path)
    store_to_sqlite(val_data, 'validation_data', db_path)
    store_to_sqlite(superval_data, 'supervalidation_data', db_path)

    # Print a success message
    print("Data successfully ingested, transformed, and stored to SQLite.")

if __name__ == "__main__":
    sqlite_data()