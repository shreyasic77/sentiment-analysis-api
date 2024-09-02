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

3.**Install dependencies**:
```bash
pip install -r requirements.txt

Execution:
The app could be accessed from http://localhost:8000/docs
