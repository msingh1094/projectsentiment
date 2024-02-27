# Sentiment Analysis Flask App with Database Integration

This project provides a sentiment analysis web application built with Flask, utilizing a deep learning model trained for classifying text as positive or negative. Predictions are stored in a MySQL database for further analysis.

## Files

- **sentiment_model.py:** Trains and saves the sentiment analysis model (embedding layer, two bidirectional LSTMs, and dense layers) along with a tokenizer.
- **app.py:** Flask app that:
  - Loads the pre-trained model and tokenizer.
  - Accepts text input via a POST request.
  - Processes and predicts sentiment.
  - Stores results in the MySQL database.
- **database.py:** Handles database operations:
  - Establishes connection and creates a table for storing predictions.
  - Inserts prediction results into the database.

## Setup and Usage

### 1. Requirements

Ensure the following Python packages are installed:

pip install flask tensorflow pandas scikit-learn mysql-connector-python

### 2. Database Configuration

Update `database.py` with your MySQL connection details: host, user, password, and database name.

### 3. Training the Model

Run `sentiment_model.py` to train and save the model and tokenizer.

### 4. Running the Flask App

Execute `app.py` to start the app (default: http://127.0.0.1:5000/).

### 5. Making Predictions

Send POST requests to `http://127.0.0.1:5000/predict_sentiment` with JSON input containing text. Response includes predicted sentiment and confidence percentage.

### 6. Database Usage

Check the MySQL database for stored predictions in the "sentiment_results" table.

## Benefits

- Analyze sentiment of user-provided text.
- Store predictions for future reference and analysis.
- Utilize a pre-trained model for immediate use.

## Docker Implementation (Not Working)

To run the app using Docker, execute `senti_A.py`. It will run the Flask app and store results in the MySQL database. However, Docker implementation is currently not functional.

## What's Working

1. AI model with training code.
2. Flask app serving model endpoint.
3. MySQL for storing the returned results by the model.
4. Frontend for Flask app (`index.html`).

## What's Not Working

1. Docker implementation.
2. Kubernetes not implemented.
3. Paraphrasing not implemented.

## Tools Used

- ChatGPT and Google Bard for Docker setup.
- Stack Overflow for troubleshooting errors and warnings.
