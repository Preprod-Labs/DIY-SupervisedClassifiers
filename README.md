# DIY-SupervisedClassifiers

This is the Naive Bayes Algorithm Branch.

**Problem definition:**

1. Assume you are a developer who is developing a weather app. You have all the weather data required and now want to implement a feature in the app that can predict the future weather for your customers. 
2. You take the necessary data you have from the your app or find a dataset online for (temperature, humidity, wind-speed) and the target value - weather.

**Data definition:**

This is mock generated data just for learning purposes. It contains the Date, Temperature, Humidity, Wind Speed and Weather data. Since it is a mock data, it will not give the most accurate results, but it is perfect to understand the underlying concept of training a Naive Bayes Model.

**Program Flow:**
1. First the Data is extracted from the 'Data/Master' Folder and ingested into a MySql database. [```ingestion.py```]
2. Then We Scale the Numerical Values and Label Encode the Categorical Values of the data. [```preprocess.py```]
3. Then we split the data into Train - Test - Validate - Supervalidation (60 - 15 -15 - 10) [```split.py```]
4. We then proceed to train a Gaussian Naive Bayes Model. We can easily do this using the sklearn library.[```model_training.py```]
5. Then we test the accuracy of the model. [```model_testing.py , model_validation.py, model_supervalidation.py```]
6. We also make a script that will help us predict the weather from new data points. [```predict.py```]
7. Finally we use a popular quick web framework called streamlit to make a simple web gui to bring the whole pipeline together on a single button click and implement the predict function using a simple gui [```app.py```]