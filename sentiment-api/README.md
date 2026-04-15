# Sentiment Analysis API

## Run locally
pip install fastapi uvicorn

uvicorn app.main:app --reload

## Test
curl -X POST http://localhost:8000/analyze-sentiment \
-H "Content-Type: application/json" \
-d '{"text": "I love this!"}'

## Docker
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
