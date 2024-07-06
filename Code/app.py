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

# Description: This Streamlit app allows users to input features and make predictions using a re-trained
# K-Nearest Neighbors model.
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

# Importing the helper functions from the .py helper files that we have created
from ingest_transform_mongodb import mongo_data # Used to ingest and transform the data from the Master into the MongoDB database
from ingest_transform_sqlite import sqlite_data # Used to ingest and transform the data from the Master into the SQLite database
from model_training import train_model # Used to train the model
from model_inference import infer_model # Used to test the model
from manual_prediction import manual_predict # Used to predict the claim based on the user's input

# Setting the page configuration
st.set_page_config(page_title="Claim Prediction", page_icon=":chart_with_upwards_trend:", layout="centered")
st.markdown("<h1 style='text-align: center; color: white;'>Vehicle Insurance Claim Prediction 🚙🚗🚜🚚</h1>", unsafe_allow_html=True)
st.divider()

# Declaring session states(streamlit variables) for saving the path throught page reloads
    
# This is how we declare session state variables in streamlit.
if "sqlite_db_path" not in st.session_state:
    st.session_state.db_path = "Data/Processed/sqlite.db"
    
if "master_data_path" not in st.session_state:
    st.session_state.master_data_path = "Data/Master/mock_data.csv"
    
if "model_path" not in st.session_state:
    st.session_state.model_path = "knn_model.pkl"

tab1, tab2, tab3, tab4 =  st.tabs(["Model Config", "Model Training", "Model Evaluation", "Model Prediction"])

# Tab for Model Config
with tab1:
    st.subheader("Model Config")
    st.write("This is where you can set your paths for the model.")
    st.divider()
    
    with st.form(key="config_form"):
        
        sqlite_db_path = st.text_input("Enter the path to the SQLite database", value=st.session_state.db_path)
        st.session_state.db_path = sqlite_db_path
        
        master_data_path = st.text_input("Enter the path to the Master data", value=st.session_state.master_data_path)
        st.session_state.master_data_path = master_data_path
        
        model_path = st.text_input("Enter the path to the model", value=st.session_state.model_path)
        st.session_state.model_path = model_path
        
        if st.form_submit_button("Save Config"):
            st.success("Config saved successfully!")

# Tab for Model Training
with tab2:
    
    st.subheader("Model Training")
    st.write("This is where you can train the model")
    st.divider()

    # Database selection
    st.header("Select Database")
    database_option = st.radio("Choose a database to use:", ('MongoDB', 'SQLite'), horizontal=True)

    # Model Training button that executes the whole training process
    st.header("Train Model")
    if st.button("Train Model", use_container_width=True):
        with st.spinner("Training model..."):
            
            # Ingesting and transforming the data
            st.write("Ingesting and transforming data...")
            if database_option == 'MongoDB':
                df = mongo_data(st.session_state.master_data_path)
            else:
                df = sqlite_data(st.session_state.master_data_path, db_path=st.session_state.db_path)
            
            # Training the model
            st.write("Training Model...")
            if database_option == 'MongoDB':
                train_report, train_grid = train_model(database='MongoDB', model_path=st.session_state.model_path)
            else:
                train_report, train_grid = train_model(database='SQLite', model_path=st.session_state.model_path, db_path=st.session_state.db_path)
            
            st.success("Model trained successfully!")
            st.text("Training Report:")
            
            st.text(train_report)
            st.text(train_grid)
            
    
# Tab for Model Evaluation
with tab3:

        st.subheader("Model Evaluation")
        st.write("This is where you can esee the current model metrics")
        st.divider()
        
        # Loading the metrics
        st.header("Metrics: ")
        test_report, val_report, superval_report = infer_model(database_option, model_path=st.session_state.model_path, db_path=st.session_state.db_path)

        st.subheader("Test Data Classification Report:")
        st.text(test_report)

        st.subheader("Validation Data Classification Report:")
        st.text(val_report)

        st.subheader("Supervalidation Data Classification Report:")
        st.text(superval_report)

# Tab for Model Prediction
with tab4:

    st.subheader("Model Prediction")
    st.write("This is where you can predict the claim based on the user's input.")
    st.divider()
    
    with st.form("predict_form"):
    
        st.subheader("Predict Claim")

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
        if st.form_submit_button("Predict", use_container_width=True):
            prediction = manual_predict(age, vehicle_age, annual_mileage, accident_history, vehicle_type, model_path=st.session_state.model_path)
            st.write(prediction)
