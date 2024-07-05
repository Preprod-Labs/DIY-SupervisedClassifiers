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

# Description: This code trains a K-Nearest Neighbors model on the training data and saves the model.
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
        # joblib 1.4.2

# Note: This dataset consists of only 1000 samples, with 600 used for training. 
# The model tends to overfit and gives 100% accuracy. In real-life scenarios with larger datasets, 
# this overfitting would be less likely, and the accuracy would be more realistic.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
import joblib

from load_mongodb import get_train_mongo
from load_sqlite import get_train_sqlite

def train_model(database, model_path, db_path=""): # Train the KNN model
    # Read the training data from the specified database
    
    if database == 'MongoDB':
        train_data = get_train_mongo()
    else:
        train_data = get_train_sqlite(db_path)

    X_train = train_data.drop(columns=['claim'])
    y_train = train_data['claim']

    model = KNeighborsClassifier()

    # Define the parameter grid for hyperparameter tuning
    param_grid = {
        'n_neighbors': [3, 5, 7, 9],
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan', 'minkowski']
    }

    # Set up the GridSearchCV for finding the best hyperparameters
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')

    # Fit the GridSearchCV to find the best model
    grid_search.fit(X_train, y_train)

    # Get the best model from GridSearchCV
    best_model = grid_search.best_estimator_

    # Save the best model
    joblib.dump(best_model, model_path)

    # Predict on the training data with the best model
    y_train_pred = grid_search.predict(X_train)

    # Print the classification report for the training data
    print("Training Data Classification Report:")
    train_eval = classification_report(y_train, y_train_pred)
    print(train_eval)

    # Print the best hyperparameters found by GridSearchCV
    print("Best Hyperparameters found by GridSearchCV:")
    train_grid = grid_search.best_params_
    print(train_grid)

    return train_eval, train_grid