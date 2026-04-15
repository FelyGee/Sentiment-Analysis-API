from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    sentiment: str
    explanation: str

@app.get("/")
def root():
    return {"message": "Sentiment API is running"}

@app.post("/analyze-sentiment", response_model=SentimentResponse)
def analyze_sentiment(request: TextRequest):
    text = request.text.lower()

    if "love" in text or "great" in text:
        return {"sentiment": "positive", "explanation": "The text expresses positive feelings."}
    elif "hate" in text or "bad" in text:
        return {"sentiment": "negative", "explanation": "The text expresses negative feelings."}
    else:
        return {"sentiment": "neutral", "explanation": "The sentiment is unclear or neutral."}
