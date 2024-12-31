import mysql.connector

# Centralized function to connect to the database
def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",  # Replace with your MySQL username
        password="Stem@2020",  # Replace with your MySQL password
        database="autisite"  # Replace with your database name
    )
try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Stem@2020",
        database="autisite"
    )
    if connection.is_connected():
        print("Connection successful!")
except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        connection.close()