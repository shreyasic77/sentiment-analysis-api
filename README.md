Implement a FastAPI endpoint that performs sentiment analysis on a given text. The endpoint should:
1. Accept POST requests with JSON payload containing a "text" field.
2. Use a pre-trained sentiment analysis model (e.g., from Hugging Face Transformers).
3. Return the sentiment (positive, negative, or neutral) and a confidence score.
4. Include proper error handling and input validation.
5. Implement rate limiting to prevent abuse.