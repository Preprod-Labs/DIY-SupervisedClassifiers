# META DATA - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    # Developer details: 
        # Name: Vansh R
        # Role: Architect
        # Code ownership rights: Vansh R
    # Version:
        # Version: V 1.0 (24 July 2024)
            # Developer: Vansh R
            # Unit test: Pass
            # Integration test: Pass
     
    # Description: This code enables data ingestion, preprocessing, model training, and weather prediction using user inputs through a Streamlit web application.
        # MYSQL: Yes
        # Streamlit: Yes
        # MQs: No
        # Cloud: No
        # Data versioning: No
        # Data masking: No


# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        #Streamlit: 1.36.0

# Importing the necessary libraries
import streamlit as st

# Importing the .py helper files
import ingestion as di # Used to ingest the data from the Master into the database
import preprocess as pp # Used to preprocess (scale and encode) the data
import split as sp # This is used to split the data into train, test, validation, and supervalidation
import model_training as mt # Used to train the model
import model_testing as mtest # Used to test the model
import model_validation as mval # Used to obtain the validation accuracy of the model
import model_supervalidation as msv # Used to obtain the super validation accuracy of the model
import predict as pr # Used to predict the weather based on the user's input

# Setting the page configuration
st.set_page_config(page_title="Weather Prediction", page_icon=":cloud:", layout="wide")
st.title("Weather Prediction")
st.divider()

# Model Training button that executes the whole training process
st.title("Train Model")
if st.button("Train Model", use_container_width=True):
    with st.status("Training model..."):
        
        # Ingesting the data
        st.write("Ingesting data..")
        df = di.load_data("Data/Master/Mock_Data.csv")
        connection = di.create_connection()
        di.ingest_to_db(df, connection)
        
        # Preprocessing the data
        st.write("PreProcessing Data.. ")
        df = pp.fetch_data_from_db(connection)
        df = pp.preprocess_data(df)
        sp.split_data(df)
        
        # Training the model
        st.write("Training Model..")
        mt.train_model()
        
    # Loading the metrics
    st.title("Metrics: ")
    test_accuracy = mtest.test_model()
    val_accuracy = mval.validate_model()
    superval_accuracy, superval_df = msv.supervalidate_model()
    
    # Displaying the metrics
    st.write(f"Test Accuracy: {round(test_accuracy, 2)}%")
    st.write(f"Validation Accuracy: {round(val_accuracy, 2)}%")
    st.write(f"Super Validation Accuracy: {round(superval_accuracy, 2)}%")
    
    # Displaying the super validation data
    st.write("Super Validation Data: ")
    st.write(superval_df)
    
# User data prediction
st.divider()
st.title("Predict Weather")

# Divided the screen into 3 columns for better UI
col1,col2,col3 = st.columns(3)
with col1:
    # Taking the temperature input from the user
    temp = st.number_input("Temperature", min_value=0.0, max_value=50.0, step=0.5)
    
with col2:
    # Taking the humidity input from the user
    humidity = st.number_input("Humidity", min_value=10.0, max_value=90.0, step=0.5)
    
with col3:
    # Taking the wind speed input from the user
    wind_speed = st.number_input("Wind Speed", min_value=0.0, max_value=30.0, step=0.5)
    
data = [temp, humidity, wind_speed]

# Predict button that predicts the weather based on the user's input
if st.button("Predict", use_container_width=True):
    prediction = pr.predict_weather(data)
    st.write(f"Prediction: {prediction}")