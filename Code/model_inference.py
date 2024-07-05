# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Developer details: 
        # Name: Mohini T and Vansh R
        # Role: Architect
        # Code ownership rights: Mohini T and Vansh R
    # Version:
        # Version: V 1.1 (05 July 2024)
            # Developer: Mohini T and Vansh R
            # Unit test: Pass
            # Integration test: Pass
     
    # Description: Performs inference using a saved model and test, validation, and supervalidation
    # datasets.

        # MYSQL: Yes
        # MQs: No
        # Cloud: No
        # Data versioning: No
        # Data masking: No


# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Python: 3.11.5
        # Pandas: 2.2.2
        # SQLAlchemy: 2.0.31

import pickle
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from evaluate import evaluate_model
from sklearn.preprocessing import LabelEncoder

def load_data(db_url, table_name):
    try:
        # Create database engine
        engine = create_engine(db_url)
        # Load data from the specified table
        data = pd.read_sql(f"SELECT * FROM {table_name}", con=engine)
        return data
    except SQLAlchemyError as e:
        # Print error message if data loading fails
        print(f"Error loading data from {table_name}: {e}")
        return None

def model_inference(model_path, db_url):
    # Load the model
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    # Load label encoder to decode labels
    label_encoder = LabelEncoder()
    # Fetching a sample of training data to fit the label encoder
    engine = create_engine(db_url)
    train_data = pd.read_sql('SELECT * FROM train_data', con=engine)
    label_encoder.fit(train_data['weather'])

    # Load the datasets
    datasets = {
        'Testing': 'test_data',
        'Validation': 'val_data',
        'Supervalidation': 'superval_data'
    }

    for dataset_name, table_name in datasets.items():
        # Print dataset name
        print(f"Evaluating on {dataset_name} Data:")
        # Load data from the specified table
        data = load_data(db_url, table_name)
        if data is not None:
            # Drop 'day' column if it exists
            if 'day' in data.columns:
                data = data.drop(columns=['day'])
            # Fit label encoder with 'weather' column
            if 'weather' in data.columns:
                label_encoder.fit(data['weather'])
            # Evaluate the model on the data
            accuracy, report, cross_val_scores = evaluate_model(model, data, label_encoder)
            # Print accuracy, classification report, and cross-validation scores
            print(f"Accuracy: {accuracy}")
            print(f"Classification Report:\n{report}")
            print(f"Cross-validation Scores: {cross_val_scores}\n")
        else:
            # Print error message if data loading fails
            print(f"Skipping {dataset_name} evaluation due to data loading error.")