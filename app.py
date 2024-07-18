from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, constr, ValidationError
from transformers import pipeline
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Initialize sentiment analysis pipeline with a model that includes neutral sentiment
sentiment_pipe = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Define a mapping for the model labels to human-readable sentiments
label_mapping = {
    "LABEL_0": "negative",
    "LABEL_1": "neutral",
    "LABEL_2": "positive"
}

app = FastAPI()

# Initialize the rate limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

class RequestModel(BaseModel):
    text: constr(min_length=1)  # Input validation to ensure text is not empty

@app.post("/analyser")
@limiter.limit("2/5seconds")  # Rate limit: 2 requests per 5 seconds per IP
async def sentiment_analyser(request: Request, request_model: RequestModel):
    try:
        text = request_model.text
        sentiment = sentiment_pipe(text)
        label = sentiment[0]["label"]
        category = label_mapping.get(label, "unknown")
        return {
            "result": {
                "sentiment_category": category,
                "score": sentiment[0]["score"]
            }
        }
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail="Invalid input data")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred during sentiment analysis")
