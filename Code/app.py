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
     
    # Description: This code loads and preprocesses weather data from a CSV file, connects to a
    # MySQL database, creates a weather table, and ingests the data into the database.

        # MYSQL: Yes
        # MQs: No
        # Cloud: No
        # Data versioning: No
        # Data masking: No


# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Python: 3.11.5
        # Streamlit: 1.36.0
        
        
# Importing the necessary libraries
import streamlit as st

# # Importing the .py helper files
# from ingestion as di # Used to ingest the data from the Master into the database
# from preprocess as pp # Used to preprocess (scale and encode) the data
# from split as sp # This is used to split the data into train, test, validation, and supervalidation
# from model_training as mt # Used to train the model
# from model_testing as mtest # Used to test the model
# from model_validation as mval # Used to obtain the validation accuracy of the model
# from model_supervalidation as msv # Used to obtain the super validation accuracy of the model
# from predict as pr # Used to predict the weather based on the user's input

# # Setting the page configuration
st.set_page_config(page_title="Weather Prediction", page_icon=":cash:", layout="centered")
st.markdown("<h1 style='text-align: center; color: white;'>Weather Prediction</h1>", unsafe_allow_html=True)
st.divider()

# Declaring session states(streamlit variables) for saving the path throughout page reloads
# This is how we declare session state variables in streamlit.

if "master_data_path" not in st.session_state:
    st.session_state.master_data_path = "Data/Master/Mock_Data.csv"

if "naive_bayes_model_path" not in st.session_state:
    st.session_state.naive_bayes_model_path = "naive_bayes.pkl"
    
if "ridge_model_path" not in st.session_state:
    st.session_state.ridge_model_path = "ridge.pkl"
    
if 'mysql_db_url' not in st.session_state:
    st.session_state.mysql_db_url = 'mysql+mysqlconnector://root:password@localhost/preprod_db'
    
tab1, tab2, tab3, tab4 =  st.tabs(["Model Config", "Model Training", "Model Evaluation", "Model Prediction"])

# Tab for Model Config
with tab1:
    st.subheader("Model Config")
    st.write("This is where you can set your paths for the model.")
    
    with st.form(key="model_config"):
        master_data_path = st.text_input("Master Data Path", st.session_state.master_data_path)
        st.session_state.master_data_path = master_data_path
        
        naive_bayes_model_path = st.text_input("Naive Bayes Model Path", st.session_state.naive_bayes_model_path)
        st.session_state.naive_bayes_model_path = naive_bayes_model_path
        
        ridge_model_path = st.text_input("Ridge Model Path", st.session_state.ridge_model_path)
        st.session_state.ridge_model_path = ridge_model_path
        
        mysql_db_url = st.text_input("MySQL DB URL", st.session_state.mysql_db_url)
        st.session_state.mysql_db_url = mysql_db_url

        if st.form_submit_button("Save Config", use_container_width=True):
            st.success("Config Saved!")
            
# Tab for Model Training
with tab2:
    pass

# Tab for Model Evaluation
with tab3:
    pass

# Tab for Model Prediction
with tab4:
    pass

# # Model Training button that executes the whole training process
# st.title("Train Model")
# if st.button("Train Model", use_container_width=True):
#     with st.status("Training model..."):

#         # Ingesting the data
#         st.write("Ingesting data..")
#         df = di.load_data("Data/Master/Mock_Data.csv")
#         connection = di.create_connection()
#         di.ingest_to_db(df, connection)

#         # Preprocessing the data
#         st.write("PreProcessing Data.. ")
#         df = pp.fetch_data_from_db(connection)
#         df = pp.preprocess_data(df)
#         sp.split_data(df)

#         # Training the model
#         st.write("Training Model..")
#         mt.train_model()

#     # Loading the metrics
#     st.title("Metrics: ")
#     test_accuracy = mtest.test_model()
#     val_accuracy = mval.validate_model()
#     superval_accuracy, superval_df = msv.supervalidate_model()

#     # Displaying the metrics
#     st.write(f"Test Accuracy: {round(test_accuracy, 2)}%")
#     st.write(f"Validation Accuracy: {round(val_accuracy, 2)}%")
#     st.write(f"Super Validation Accuracy: {round(superval_accuracy, 2)}%")

#     # Displaying the super validation data
#     st.write("Super Validation Data: ")
#     st.write(superval_df)

# # User data prediction
# st.divider()
# st.title("Predict Weather")

# # Divided the screen into 3 columns for better UI
# col1,col2,col3 = st.columns(3)
# with col1:
#     # Taking the temperature input from the user
#     temp = st.number_input("Temperature", min_value=0.0, max_value=50.0, step=0.5)

# with col2:
#     # Taking the humidity input from the user
#     humidity = st.number_input("Humidity", min_value=10.0, max_value=90.0, step=0.5)

# with col3:
#     # Taking the wind speed input from the user
#     wind_speed = st.number_input("Wind Speed", min_value=0.0, max_value=30.0, step=0.5)

# data = [temp, humidity, wind_speed]

# # Predict button that predicts the weather based on the user's input
# if st.button("Predict", use_container_width=True):
#     prediction = pr.predict_weather(data)
#     st.write(f"Prediction: {prediction}")