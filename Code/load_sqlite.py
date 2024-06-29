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

import pandas as pd
import sqlite3

def load_from_sqlite(table_name, db_path='D:\PreProd Corp\DIY-SupervisedClassifiers\Data\Processed\processed_data.db'): # Load data from SQLite database
    conn = sqlite3.connect(db_path) # Establish a connection to the SQLite database
    data = pd.read_sql(f'SELECT * FROM {table_name}', conn) # Read data from the specified table
    conn.close() # Close the database connection
    return data # Return the loaded data

def call_sqlite():
    # Load data from SQLite
    train_data = load_from_sqlite('training_data')
    test_data = load_from_sqlite('testing_data')
    val_data = load_from_sqlite('validation_data')
    sup_data = load_from_sqlite('supervalidation_data')
    
    # Save to CSV
    train_data.to_csv('D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/SQLite/training_data.csv', index=False)
    test_data.to_csv('D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/SQLite/testing_data.csv', index=False)
    val_data.to_csv('D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/SQLite/validation_data.csv', index=False)
    sup_data.to_csv('D:/PreProd Corp/DIY-SupervisedClassifiers/Data/Processed/SQLite/supervalidation_data.csv', index=False)

    # Print a success message
    print("Data succesfully loaded from SQLite and stored to CSV.")

if __name__ == "__main__":
    call_sqlite()