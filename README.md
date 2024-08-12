# Metrics Ingestion Application

Metrics Ingestion Application
This repository contains a Python application that ingests user metrics data and stores it in a PostgreSQL database. The setup includes a Dockerfile for containerizing the application, a docker-compose.yml file to orchestrate the containers, and a Python script that handles the data ingestion.

Table of Contents
Getting Started
Running the Application
Database Schema
Maintaining and Extending the Pipeline
Assumptions
Limitations
Future Improvements

Getting Started
Prerequisites
Ensure you have the following installed:

Docker: Install Docker
Docker Compose: Install Docker Compose
PostgreSQL: Ensure you have the necessary permissions to create databases if running locally.

Directory Structure

├── Dockerfile
├── docker-compose.yml
├── app.py
├── requirements.txt
├── init.sql
└── README.md

Setting Up
Dockerfile: Defines the environment for running the Python application.
docker-compose.yml: Orchestrates the application, database, and pgAdmin containers.
app.py: The Python script that ingests metrics data.
requirements.txt: Specifies the Python dependencies.
init.sql: SQL script to initialize the database.

Running the Application
Build and Start the Containers:
docker-compose up --build
This command will build the Docker image for the application and start the containers for the app, PostgreSQL database, and pgAdmin.

Database Schema
The database contains a single table named user_metrics, which stores the user metrics data.

Database Schema
The database contains a single table named user_metrics, which stores the user metrics data.

### `user_metrics` Table

| Column            | Type           | Constraints                            | Description                                             |
|-------------------|----------------|----------------------------------------|---------------------------------------------------------|
| `id`              | SERIAL         | PRIMARY KEY                            | Auto-incremented unique identifier                      |
| `user_id`         | VARCHAR(255)   | NOT NULL                               | Unique identifier for the user                          |
| `session_id`      | VARCHAR(255)   | NOT NULL                               | Unique identifier for the session                       |
| `timestamp`       | BIGINT         | NOT NULL                               | Unix timestamp of the event                             |
| `talked_time`     | INT            | NOT NULL                               | Duration of time the user talked during the session (in seconds) |
| `microphone_used` | BOOLEAN        | NOT NULL                               | Whether a microphone was used                           |
| `speaker_used`    | BOOLEAN        | NOT NULL                               | Whether a speaker was used                              |
| `voice_sentiment` | VARCHAR(50)    |                                        | Sentiment analysis of the user's voice                  |
| `created_at`      | TIMESTAMPTZ    | DEFAULT NOW()                          | Timestamp when the record was created                   |

Maintaining and Extending the Pipeline
Adding New Fields
To add a new field to the user_metrics table:

Update the CREATE TABLE statement in app.py and the corresponding INSERT statement.
Modify the data ingestion process in app.py to include the new field.
Scaling the Application
For handling larger volumes of data, consider:

Implementing data partitioning strategies.
Using a message queue (e.g., RabbitMQ, Kafka) to manage the data stream.
Optimizing the database by indexing frequently queried fields.

Assumptions
The data being ingested is pre-processed and valid.
The application will primarily be used in a development or testing environment.
The database schema will evolve over time as new requirements emerge.

Limitations
The application currently handles only a single data stream. Multi-stream ingestion may require modifications.
Error handling in the data ingestion process is minimal. Consider adding more robust error handling for production use.

Future Improvements
Enhanced Error Handling: Implement better exception management and logging.
Unit Tests: Add unit tests for the data ingestion logic.
Data Validation: Integrate data validation checks before inserting records into the database.
Performance Optimization: Optimize the database queries and the ingestion process for better performance.
