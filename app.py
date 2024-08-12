import os
import psycopg2
from psycopg2.extras import execute_batch
import json
import time

# Database connection parameters
DB_HOST = os.getenv('DATABASE_HOST')
DB_NAME = os.getenv('DATABASE_NAME')
DB_USER = os.getenv('DATABASE_USER')
DB_PASSWORD = os.getenv('DATABASE_PASSWORD')

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host=DB_HOST,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# Create the cursor and create the table
cursor = conn.cursor()
create_table = """CREATE TABLE IF NOT EXISTS user_metrics (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    session_id VARCHAR(255) NOT NULL,
    timestamp BIGINT NOT NULL,
    talked_time INT NOT NULL,
    microphone_used BOOLEAN NOT NULL,
    speaker_used BOOLEAN NOT NULL,
    voice_sentiment VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW()
)"""
cursor.execute(create_table)
conn.commit()  # Commit the table creation
cursor.close()

# Function to process and insert user metrics
def process_and_insert_metrics(data):
    cursor = conn.cursor()  # Create a new cursor for each batch
    sql = """
    INSERT INTO user_metrics (user_id, session_id, timestamp, talked_time, microphone_used, speaker_used, voice_sentiment)
    VALUES (%(user_id)s, %(session_id)s, %(timestamp)s, %(talked_time)s, %(microphone_used)s, %(speaker_used)s, %(voice_sentiment)s)
    """
    execute_batch(cursor, sql, data)
    conn.commit()
    cursor.close()  # Close the cursor after inserting

# Simulating a stream of data ingestion
try:
    while True:
        # Replace this with actual streaming logic
        data_stream = [
            {
                "user_id": "user_123",
                "session_id": "sess_456",
                "timestamp": int(time.time()),
                "talked_time": 120,
                "microphone_used": True,
                "speaker_used": True,
                "voice_sentiment": "positive"
            }
        ]
        process_and_insert_metrics(data_stream)
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping data ingestion...")

finally:
    conn.close()  # Ensure the connection is closed properly

