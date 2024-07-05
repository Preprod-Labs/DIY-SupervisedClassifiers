# DIY-SupervisedClassifiers

This is the K-Nearest Neighbors branch.

# K-Nearest Neighbors

The k-Nearest Neighbors (KNN) algorithm is a non-parametric, instance-based learning method used for classification. For a given query point, kNN identifies the 'k' closest training examples using distance metrics like Euclidean or Manhattan distance. The class label is determined by a majority vote among these 'k' neighbors. kNN supports multi-class classification and is effective for small to moderate-sized datasets. However, it can be sensitive to the choice of 'k' and feature scaling, and may become computationally expensive for large datasets. Despite these challenges, kNN remains a popular method for classification tasks.

# KNN Classifier

## Problem Definition

Develop a microservices-based architecture for a K-Nearest Neighbors (KNN) Supervised Classifier to predict the likelihood of a vehicle insurance claim using a dataset with features like age, vehicle age, mileage, accident history, and vehicle type to predict claim status.

## Data Definition

Mock data for learning purposes with features: Age, Vehicle Age, Annual Mileage, Accident History, Vehicle Type, and Claim status.

> Since this dataset only consists of 1000 samples, with 600 used for training, the model tends to overfit and give 100% accuracy. This would not be the case for real-life scenarios with larger datasets, where more varied data would prevent such overfitting and provide a more realistic accuracy.

## Directory Structure

- **Code/**: Contains all the scripts for data ingestion, transformation, loading, model training, inference, manual prediction, and API.
- **Data/**: Contains the raw and processed data.

## Data Splitting

- **Training Samples**: 600
- **Testing Samples**: 150
- **Validation Samples**: 150
- **Supervalidation Samples**: 100

## Program Flow

1. **Data Ingestion:** Extract data from 'Data/Master' and ingest into MongoDB or SQLite. [`ingest_transform_mongodb.py`, `ingest_transform_sqlite.py`]
2. **Data Transformation:** Transform data by encoding and then split into Train, Test, Validation, and Supervalidation sets. [`ingest_transform_mongodb.py`, `ingest_transform_sqlite.py`, `load_mongodb.py`, `load_sqlite.py`]
3. **Model Training:** Train KNN model with GridSearchCV for hyperparameter tuning. [`model_training.py`]
4. **Model Evaluation:** Evaluate model on test, validation, and supervalidation sets, and generate classification reports. [`model_inference.py`]
5. **Manual Prediction:** Script to predict claim status based on user input data. [`manual_prediction.py`]
5. **Web Application:** Streamlit app to integrate the pipeline and provide a user-friendly GUI for predictions. [`app.py`]

## Steps to Run

1. Install the necessary packages: `pip install -r requirements.txt`
2. Run `app.py` to launch the Streamlit web application and use the GUI for the entire pipeline.