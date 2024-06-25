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
     
    # Description: This code loads weather data from a CSV file, connects to a MySQL database, creates a weather table, and ingests the data into the database.

        # MYSQL: Yes
        # MQs: No
        # Cloud: No
        # Data versioning: No
        # Data masking: No


# CODE - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Dependency: 
    # Environment:     
        # Pandas: 2.2.2
        # Scikit-learn: 1.5.0

# Import necessary libraries
import pandas as pd # Used to load the data
import mysql.connector # Used to connect to the MySQL database
from mysql.connector import Error # Used to handle the MySQL errors

def load_data(filepath):
    # Load the data from the file into a Pandas DataFrame
    df = pd.read_csv(filepath)
    return df

def create_connection():
    # Create a connection to the MySQL database
    connection = None
    try:
        # Connect to the database using the credentials
        connection = mysql.connector.connect(
            host='localhost',
            database='diy1',
            user='root',
            password='password',
        )
        if connection.is_connected():
            # Check the database connection
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            
        return connection
    
    except Error as e:
        # Handle the error if the connection fails
        print(f"The error '{e}' occurred")
        
def ingest_to_db(df, connection):
    # Ingest the data into the MySQL database
    cursor = connection.cursor()
    
    # Drop the table if it already exists
    cursor.execute("DROP TABLE IF EXISTS weather")
    # Create a new table to store the data
    cursor.execute("""
        CREATE TABLE weather (
            day DATE,
            temperature FLOAT,
            humidity FLOAT,
            wind_speed FLOAT,
            weather VARCHAR(10)
        )
    """)
    
    # Convert 'day' column to MySQL date format
    df['day'] = pd.to_datetime(df['day'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    
    # Ingest the data into the table
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO weather (day, temperature, humidity, wind_speed, weather)
            VALUES (%s, %s, %s, %s, %s)
        """, tuple(row))
    
    # Commit the changes to the database
    connection.commit()
    print("Data ingested into MySQL database successfully!")