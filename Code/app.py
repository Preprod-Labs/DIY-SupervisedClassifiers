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

# Description: This Streamlit app allows users to input features and make predictions using a pre-trained K-Nearest Neighbors model.
# MYSQL: No
# NoSQL: Yes (MongoDB)
# MQs: No
# Cloud: No
# Data versioning: No
# Data masking: Yes

# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
    # Python 3.11.5
    # Streamlit 1.36.0

import streamlit as st

# Importing the .py helper files
import ingest_transform_mongodb as itm  # Used to ingest and transform the data from the Master into the MongoDB database
import ingest_transform_sqlite as its # Used to ingest and transform the data from the Master into the SQLite database
import load_mongodb as ldm  # Used to load the data from the MongoDB database and split into CSV files
import load_sqlite as lds  # Used to load the data from the SQLite database and split into CSV files
import model_training as mt  # Used to train the model
import model_inference as mi  # Used to test the model
import manual_prediction as mp  # Used to predict the claim based on the user's input

# Setting the page configuration
st.set_page_config(page_title="Claim Prediction", page_icon=":chart_with_upwards_trend:", layout="centered")
st.title("Vehicle Insurance Claim Prediction 🚙🚗🚜🚚")
st.divider()

# Database selection
st.header("Select Database")
database_option = st.radio("Choose a database to use:", ('MongoDB', 'SQLite'))

# Model Training button that executes the whole training process
st.header("Train Model")
if st.button("Train Model", use_container_width=True):
    with st.spinner("Training model..."):
        
        # Ingesting and transforming the data
        st.write("Ingesting and transforming data...")
        if database_option == 'MongoDB':
            df = itm.mongo_data()
        else:
            df = its.sqlite_data()
        
        # Loading the data
        st.write("Loading data...")
        if database_option == 'MongoDB':
            ldm.call_mongo()
        else:
            lds.call_sqlite()
        
        # Training the model
        st.write("Training Model...")
        if database_option == 'MongoDB':
            train_report, train_grid = mt.train_model(database='MongoDB')
        else:
            train_report, train_grid = mt.train_model(database='SQLite')
        
        st.text(train_report)
        st.text(train_grid)
        st.success("Model trained successfully!")
        
    # Loading the metrics
    st.header("Metrics: ")
    test_report, val_report, superval_report = mi.infer_model(database_option)

    st.subheader("Test Data Classification Report:")
    st.text(test_report)

    st.subheader("Validation Data Classification Report:")
    st.text(val_report)

    st.subheader("Supervalidation Data Classification Report:")
    st.text(superval_report)
    
# User data prediction
st.divider()
st.header("Predict Claim")

# Divided the screen into 4 columns for better UI
col1, col2, col3, col4 = st.columns(4)
with col1:
    # Taking the age input from the user
    age = st.number_input("Age", min_value=18, max_value=100, step=1)

with col2:
    # Taking the vehicle age input from the user
    vehicle_age = st.number_input("Vehicle Age", min_value=0, max_value=30, step=1)

with col3:
    # Taking the annual mileage input from the user
    annual_mileage = st.number_input("Annual Mileage", min_value=0, max_value=300000, step=1000)

with col4:
    # Taking the accident history input from the user
    accident_history = st.number_input("Accident History", min_value=0, max_value=10, step=1)

# Vehicle type selection
vehicle_type = st.selectbox("Vehicle Type", options=["SUV", "Sedan", "Tractor", "Truck"])

# Predict button that predicts the claim based on the user's input
if st.button("Predict", use_container_width=True):
    prediction = mp.manual_predict(age, vehicle_age, annual_mileage, accident_history, vehicle_type)
    st.write(prediction)