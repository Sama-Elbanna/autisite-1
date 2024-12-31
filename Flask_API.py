from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import pooling
import bcrypt

app = Flask(__name__)

# Database configuration
dbconfig = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Stem@2020",
    "database": "autisite"
}

# Initialize the connection pool
connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,  # Adjust the pool size as needed
    **dbconfig
)

# Function to get a connection from the pool
def connect_db():
    return connection_pool.get_connection()

# Register a new patient
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        guardian_name = data['guardian_name']
        patient_name = data['patient_name']
        register_date = data['register_date']
        email = data['email']
        password = data['password']
        patient_birth_date = data['patient_birth_date']
        genetic_history = data.get('genetic_history', None)
        pregnancy_disease = data.get('pregnancy_disease', None)
        other_disorders = data.get('other_disorders', None)

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        connection = connect_db()
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO registration 
        (guardian_name, patient_name, registration_date, email, password, patient_birth_date, genetic_history, pregnancy_disease, other_disorders) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (guardian_name, patient_name, register_date, email, hashed_password.decode('utf-8'),
                                      patient_birth_date, genetic_history, pregnancy_disease, other_disorders))
        connection.commit()

        return jsonify({'message': 'Registration successful'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

# Login user
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        email = data['email']
        password = data['password']

        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute("SELECT password FROM registration WHERE email=%s", (email,))
        result = cursor.fetchone()

        if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'error': 'Invalid credentials'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

# Add symptoms endpoint
@app.route('/symptoms', methods=['POST'])
def add_symptoms():
    try:
        data = request.json
        patient_id = data['patient_id']  # Ensure this is passed in the request
        symptoms = data['symptoms']

        connection = connect_db()
        cursor = connection.cursor()

        # Insert each symptom into the database
        for symptom in symptoms:
            insert_query = """
            INSERT INTO symptoms (patient_id, symptom) 
            VALUES (%s, %s)
            """
            cursor.execute(insert_query, (patient_id, symptom))

        connection.commit()

        return jsonify({'message': 'Symptoms added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

# Entry point for Waitress
if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
