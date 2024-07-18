from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


#sentiment analysis pipeline
sentiment_pipe = pipeline("sentiment-analysis")

app = FastAPI()



class RequestModel(BaseModel):
    text: str




#endpoints
@app.post("/analyser")
def sentiment_analyser(request: RequestModel):

    text = request.text

    sentiment = sentiment_pipe(text)

    return {
        "result": {
            "sentiment_category": sentiment[0]["label"],
            "score": sentiment[0]["score"]
        }

    }