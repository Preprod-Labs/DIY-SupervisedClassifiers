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

# Description: This code loads the data from SQLite database.
    # SQLite: Yes

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Python 3.11.5
        # Pandas 2.2.2

import pandas as pd # For data manipulation
import sqlite3 # For SQLite

def load_from_sqlite(table_name, db_path): # Load data from SQLite database
    conn = sqlite3.connect(db_path) # Establish a connection to the SQLite database
    data = pd.read_sql(f'SELECT * FROM {table_name}', conn) # Read data from the specified table
    conn.close() # Close the database connection
    
    return data # Return the loaded data

def get_train_sqlite(db_path):
    # Load and return training data from SQLite
    train_data = load_from_sqlite('training_data', db_path)
    
    return train_data
    
def get_eval_sqlite(db_path):
    # Load and return the evaluation data from SQLite
    test_data = load_from_sqlite('testing_data', db_path)
    val_data = load_from_sqlite('validation_data', db_path)
    sup_data = load_from_sqlite('supervalidation_data', db_path)
    
    return test_data, val_data, sup_data