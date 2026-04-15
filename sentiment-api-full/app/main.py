import os
from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to analyze")


class SentimentResult(BaseModel):
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        ..., description="Overall sentiment classification"
    )
    explanation: str = Field(
        ..., description="Short explanation of why the text has this sentiment"
    )


app = FastAPI(
    title="Sentiment Analysis API",
    description="Analyze sentiment with LangChain + OpenAI",
    version="1.0.0",
)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a sentiment analysis assistant. "
            "Classify the user's text as positive, negative, or neutral. "
            "Return a short explanation. Keep the explanation under 30 words.",
        ),
        (
            "human",
            "Analyze the sentiment of this text: {text}",
        ),
    ]
)


# The model name is configurable so the project can be reused easily.
llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
)


# LangChain structured output ensures the response matches the schema.
chain = prompt | llm.with_structured_output(SentimentResult)


@app.get("/")
def read_root() -> dict:
    return {"message": "Sentiment Analysis API is running"}


@app.post("/analyze-sentiment", response_model=SentimentResult)
def analyze_sentiment(payload: SentimentRequest) -> SentimentResult:
    try:
        return chain.invoke({"text": payload.text})
    except Exception as exc:  # pragma: no cover - runtime integration error path
        raise HTTPException(status_code=500, detail=f"Sentiment analysis failed: {exc}") from exc
