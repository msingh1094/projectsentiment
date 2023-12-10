



from flask import Flask, request, jsonify, render_template
import re
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import mysql.connector
import os

app = Flask(__name__)

model_path = os.path.join(os.path.dirname(__file__), "sentiment_analysis_model.h5")
tokenizer_path = os.path.join(os.path.dirname(__file__), "tokenizer.pkl")

model = load_model(model_path)
with open(tokenizer_path, 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    # port="3306",
    database="sentiment_db"
)

cursor = db.cursor()

# Create table if not exists
create_table = """
CREATE TABLE IF NOT EXISTS sentiment_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original_text TEXT,
    prediction_percentage FLOAT,
    sentiment_label VARCHAR(10)
);
"""
cursor.execute(create_table)
db.commit()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9().,!?]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    try:
        data = request.get_json()
        original_text = data['Input']

        cleaned_text = clean_text(original_text)
        text_sequence = tokenizer.texts_to_sequences([cleaned_text])
        text_padded = pad_sequences(text_sequence, maxlen=200)
        prediction = model.predict(text_padded)[0][0]

        prediction_percentage = round(float(prediction) * 100, 2)
        sentiment_label = "Positive" if prediction > 0.5 else "Negative"

        # Use the existing 'cursor' and 'db' objects
        query = "INSERT INTO sentiment_results (original_text, prediction_percentage, sentiment_label) VALUES (%s, %s, %s)"
        values = (original_text, prediction_percentage, sentiment_label)
        cursor.execute(query, values)
        db.commit()

        result = {
            'Original_text': original_text,
            'Sentiment_prediction': f'{prediction_percentage}% {sentiment_label}'
        }
        return jsonify(result)
    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({'error': str(e)})

    finally:
        # Close the cursor and database connection in the 'finally' block
        cursor.close()
        db.close()

if __name__ == '__main__':
    app.run(debug=True)
