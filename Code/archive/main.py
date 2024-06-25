# Not used curently used for testing purposes

# Importing local .py files into the main.py file

import ingestion as di # Used to ingest the data from the Master into the database
import preprocess as pp # Used to preprocess (scale and encode) the data
import split as sp # This is used to split the data into train, test, validation, and supervalidation
import model_training as mt # Used to train the model
import model_testing as mtest # Used to test the model
import model_validation as mval # Used to obtain the validation accuracy of the model
import model_supervalidation as msv # Used to obtain the super validation accuracy of the model
import predict as pr # Used to predict the weather based on the user's input

# Loading the data from the Master into a Pandas DataFrame
df = di.load_data("Data/Master/Mock_Data.csv")

# Creating a connection to the MySQL database
connection = di.create_connection()

# Ingesting the data into the MySQL database
di.ingest_to_db(df, connection)

# Fetching the data from the MySQL database
df = pp.fetch_data_from_db(connection)
df = pp.preprocess_data(df)

# Splitting the data into train, test, validation, and supervalidation
sp.split_data(df)

# Training the model
mt.train_model()

# Testing the model
test_accuracy = mtest.test_model()
print(f'Test Accuracy: {test_accuracy}')
print('')

val_accuracy = mval.validate_model()
print(f'Validation Accuracy: {val_accuracy}')
print('')

superval_accuracy, superval_df = msv.supervalidate_model()
print(f'Supervalidation Accuracy: {superval_accuracy}')
print('')

print(superval_df.head())

# Predicting the weather based on the user's input
# Temp Humid Wind
new_data = [30.0, 90.0, 10.0]
prediction = pr.predict_weather(new_data)

print(f'The predicted weather is: {prediction}')