# Sentiment-Analysis-API
 A Sentiment Analysis API a small web API that analyzes the sentiment of a given text (positive, negative, or neutral) using LangChain and Docker 

## Instructions to Run locally
1.pip install fastapi uvicorn

2.uvicorn app.main:app --reload

## Instructions to Test
curl -X POST http://localhost:8000/analyze-sentiment \
-H "Content-Type: application/json" \
-d '{"text": "I love this!"}'

## Instructions for Docker
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
