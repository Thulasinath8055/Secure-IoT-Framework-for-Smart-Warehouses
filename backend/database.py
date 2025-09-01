# backend/database.py
import psycopg2

DB_CONFIG = {
    "dbname": "iot_db",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sensor_data (
        id SERIAL PRIMARY KEY,
        device_id VARCHAR(50),
        temperature FLOAT,
        humidity FLOAT,
        movement INT,
        ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("[DB] sensor_data table ready")

def insert_sensor_data(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO sensor_data (device_id, temperature, humidity, movement)
        VALUES (%s, %s, %s, %s);
    """, (data["device_id"], data["temperature"], data["humidity"], data["movement"]))
    conn.commit()
    cur.close()
    conn.close()
    print("[DB] Data inserted")

# Create table on import
create_table()
