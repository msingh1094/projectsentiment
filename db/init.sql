-- -- init.sql

-- -- Create the database if it doesn't exist
-- CREATE DATABASE IF NOT EXISTS sentiment_db;

-- -- Use the sentiment_db database
-- USE sentiment_db;

-- -- Create the sentiment_results table if it doesn't exist
-- CREATE TABLE IF NOT EXISTS sentiment_results (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     original_text TEXT,
--     prediction_percentage FLOAT,
--     sentiment_label VARCHAR(10)
-- );
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS sentiment_db;

-- Create the sentiment_results table if it doesn't exist
CREATE TABLE IF NOT EXISTS sentiment_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_text TEXT,
    prediction_percentage FLOAT,
    sentiment_label VARCHAR(10)
);
