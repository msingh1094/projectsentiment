# Use an official Python runtime as a parent image
FROM python:3.9.8

EXPOSE 5000

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# Copy the model files into the container at /app
COPY /tokenizer.pkl /app
COPY /sentiment_analysis_model.h5 /app
COPY /templates/ /app/

# Copy the application code into the container at /app
COPY app.py /app

# Define environment variable
ENV NAME SentimentAnalysisIMDB

# Run the Flask application
CMD ["python", "app.py"]





