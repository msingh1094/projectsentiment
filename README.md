Sentiment Analysis Flask App with Database Integration

This project provides a sentiment analysis web application built with Flask, utilizing a deep learning model trained for classifying text as positive or negative. Predictions are stored in a MySQL database for further analysis.

Files:

sentiment_model.py: Trains and saves the sentiment analysis model (embedding layer, two bidirectional LSTMs, and dense layers) along with a tokenizer.

app.py: Flask app that:
Loads the pre-trained model and tokenizer.
Accepts text input via a POST request.
Processes and predicts sentiment.
Stores results in the MySQL database.
database.py: Handles database operations:
Establishes connection and creates a table for storing predictions.
Inserts prediction results into the database.
Setup and Usage:

1. Requirements:

Python packages: flask, tensorflow, pandas, scikit-learn, mysql-connector-python
Install via: pip install flask tensorflow pandas scikit-learn mysql-connector-python
2. Database Configuration:

Update database.py with your MySQL connection details: host, user, password, and database name.
3. Training the Model:

Run sentiment_model.py to train and save the model and tokenizer.
4. Running the Flask App:

Execute app.py to start the app (default: http://127.0.0.1:5000/).
5. Making Predictions:

Send POST requests to http://127.0.0.1:5000/predict_sentiment with JSON input containing text.
Response includes predicted sentiment and confidence percentage.
6. Database Usage:

Check the MySQL database for stored predictions in the "sentiment_results" table.
Benefits:

Analyze sentiment of user-provided text.
Store predictions for future reference and analysis.
Utilize a pre-trained model for immediate use.


DOCKER IMPLEMENTED - BUT NOT WORKING
TO RUN THE APP ON FLASK TO ACCESS THE ENDPOINT API OF THE MODEL
PLEASE RUN senti_A.py it will run on flask which will stores the reuslt in MYSQL databases entered text and sentiment as positive or negative and its percentage


-----------------------------------WHATS WORKING---------------------------------------------


1. AI MODEL WITH TRAINING CODE
2. FLASK APP WHICH IS SERVING MODEL ENDPOINT
3. MYSQL FOR STORING THE RETURNED RESULTS BY MODEL 
4. FRONETEND FOR FLASK APP (index.html)

-----------------------------------WHATS NOT WORKING-------------------------------------------

1. DOCKER IMPLEMENTED BUT NOT WORKING
2. KUBERNETES NOT IMPLEMENTED
3. PARAPHRASING NOT IMPLEMENTED

------------------------TOOLS USED-----------------------
1. CHATGPT AND GOOGLE BARD FOR DOCKER HELP AND SETTING UP --- IM NEW TO THIS
2. STACK OVERFLOW FOR WARNINGS AND ERROR



TO RUN THE MODEL AND SEE ITS WORKING PLEASE RUN senti_A.py


