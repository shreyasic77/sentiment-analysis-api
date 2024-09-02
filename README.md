# Sentiment Analysis API

This project implements a sentiment analysis API using FastAPI. The API accepts text input via POST requests and returns the sentiment (positive, negative, or neutral) along with a confidence score. It features input validation, error handling, and rate limiting to ensure robust performance.

## Features

- **Sentiment Analysis**: Analyzes the sentiment of a given text using a pre-trained model (e.g., from Hugging Face Transformers).
- **JSON Input**: Accepts POST requests with a JSON payload containing a `text` field.
- **Response**: Returns the sentiment label (`positive`, `negative`, or `neutral`) along with a confidence score.
- **Error Handling**: Proper validation and error handling for various edge cases.
- **Rate Limiting**: Prevents abuse by limiting the number of requests per user.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shreyasic77/sentiment-analysis-api.git
   cd sentiment-analysis-api

2. **Create and activate virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate

#install dependencies
pip install -r requirements.txt
```

3. **Run**:
```bash   
uvicorn main:app --reload
```

4. **Accessing API Documentation**:
Open your browser and go to http://localhost:8000/docs

5. **Sending a POST Request**:
- Use an HTTP client like curl, Postman, or any programming language's HTTP library to send a POST request to /sentiment with a JSON payload.
- The API will return a JSON response containing the sentiment label and a confidence score.

6. **API Endpoints**:

- **`POST /sentiment`**: Analyzes the sentiment of the provided text.
  - **Request Body**: JSON object with a `text` field.
  - **Response**: JSON object with `sentiment` and `confidence` fields.

7. **Error Handling**:

The API includes input validation and error handling. Common errors include:

- **400 Bad Request**: If the `text` field is missing or invalid.
- **429 Too Many Requests**: If the user exceeds the rate limit.  
