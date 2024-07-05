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
     
    # Description: Trains a Gaussian Naive Bayes model on the training data and evaluates it
    # using the evaluate_model function.

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
        # Scikit-learn: 1.5.0

from sklearn.naive_bayes import GaussianNB
import pickle
from load import load_train_data
from evaluate import evaluate_model
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def train_model():
    # Load the preprocessed training data from the database
    X_train, y_train = load_train_data()

    # Train the Gaussian Naive Bayes model
    model = GaussianNB()
    model.fit(X_train, y_train)
    
    # Save the model
    with open('naive_bayes.pkl', 'wb') as file:
        pickle.dump(model, file)

    # Load label encoder to decode labels
    label_encoder = LabelEncoder()
    label_encoder.fit(y_train)
    
    # Evaluate the model on the training dataset
    print("Evaluating Gaussian Naive Bayes on Training Data:")
    train_data = pd.concat([X_train, y_train], axis=1)
    accuracy, report, cross_val_scores = evaluate_model(model, train_data, label_encoder)
    print(f"Accuracy: {accuracy}")
    print(f"Classification Report:\n{report}")
    print(f"Cross-validation Scores: {cross_val_scores}\n")

if __name__ == "__main__":
    train_model()