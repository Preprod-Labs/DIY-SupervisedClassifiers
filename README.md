# DIY-SupervisedClassifiers

This is the K-Nearest Neighbors branch.

# KNN Classifier

## Problem Definition

Develop a microservices-based architecture for a K-Nearest Neighbors (KNN) Supervised Classifier to predict the likelihood of a vehicle insurance claim using a dataset with features like age, vehicle age, mileage, accident history, and vehicle type to predict claim status.

## Data Definition

Mock data for learning purposes with features: Age, Vehicle Age, Annual Mileage, Accident History, Vehicle Type, and Claim status.

## Directory Structure

- **Code/**: Contains all the scripts for data ingestion, transformation, loading, model training, inference, manual prediction, and API.
- **Data/**: Contains the raw and processed data.

## Data Splitting

- **Training Samples**: 600
- **Testing Samples**: 150
- **Validation Samples**: 150
- **Supervalidation Samples**: 100

> Since this dataset only consists of 1000 samples, with 600 used for training, the model tends to overfit and give 100% accuracy. This would not be the case for real-life scenarios with larger datasets, where more varied data would prevent such overfitting and provide a more realistic accuracy.

## Program Flow

1. **Data Ingestion:** Extract data from 'Data/Master' and ingest into MongoDB or SQLite. [`ingest_transform_mongodb.py`, `ingest_transform_sqlite.py`]
2. **Data Transformation:** Transform data by encoding and then split into Train, Test, Validation, and Supervalidation sets. [`ingest_transform_mongodb.py`, `ingest_transform_sqlite.py`, `load_mongodb.py`, `load_sqlite.py`]
3. **Model Training:** Train KNN model with GridSearchCV for hyperparameter tuning. [`model_training.py`]
4. **Model Evaluation:** Evaluate model on test, validation, and supervalidation sets, and generate classification reports. [`model_inference.py`]
5. **Manual Prediction:** Script to predict claim status based on user input data. [`manual_prediction.py`]
5. **Web Application:** Streamlit app to integrate the pipeline and provide a user-friendly GUI for predictions. [`app.py`]

## Steps to Run

1. Install the necessary packages: `pip install -r requirements.txt`
2. Ingest, transform, and split the data by running either `ingest_transform_mongodb.py` or `ingest_transform_sqlite.py`.
3. Run `load_mongodb.py` or `load_sqlite.py` to load the data into the respective CSV files.
4. Run `model_training.py` to train the KNN model and perform hyperparameter tuning.
5. Run `model_inference.py` to obtain classification reports for the test, validation, and supervalidation datasets.
6. Use `manual_prediction.py` to predict claim status based on new data points.
7. Run `app.py` to launch the Streamlit web application and use the GUI for the entire pipeline.

**Optional:** Adjust paths and configurations in the scripts as per your environment setup.