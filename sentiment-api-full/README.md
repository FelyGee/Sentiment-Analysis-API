# Sentiment Analysis API with LangChain, Docker, and Git

This project exposes a small FastAPI web service with one endpoint:

- `POST /analyze-sentiment`

It uses **LangChain** with **OpenAI** to classify text as:

- `positive`
- `negative`
- `neutral`

and returns a short explanation in JSON.

## Project Structure

```text
sentiment-api-full/
├── app/
│   └── main.py
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

## How LangChain Is Used

The API uses LangChain in three steps:

1. **Prompt template**
   - A `ChatPromptTemplate` tells the model to classify the text and give a short explanation.

2. **LLM connection**
   - `ChatOpenAI` connects the app to an OpenAI chat model.

3. **Structured output**
   - `with_structured_output(SentimentResult)` forces the model response into a Pydantic schema so the API can safely return JSON with:
     - `sentiment`
     - `explanation`

## Requirements

- Python 3.11+
- An OpenAI API key
- Docker (optional, for containerized run)

## Local Setup

### 1. Extract the project and enter the folder

```bash
cd sentiment-api-full
```

### 2. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set environment variables

**macOS / Linux**

```bash
export OPENAI_API_KEY="your_api_key_here"
export OPENAI_MODEL="gpt-4o-mini"
```

**Windows PowerShell**

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
$env:OPENAI_MODEL="gpt-4o-mini"
```

### 5. Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- `http://localhost:8000`
- Swagger docs: `http://localhost:8000/docs`

## Test the API

### Browser test

Open:

- `http://localhost:8000/docs`

Use the `POST /analyze-sentiment` endpoint with sample input:

```json
{
  "text": "I love this product!"
}
```

### cURL test

```bash
curl -X POST http://localhost:8000/analyze-sentiment \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'
```

### Example response

```json
{
  "sentiment": "positive",
  "explanation": "The text expresses strong satisfaction and enthusiasm."
}
```

## Run with Docker

### 1. Build the image

```bash
docker build -t sentiment-api-full .
```

### 2. Run the container

```bash
docker run -p 8000:8000 \
  -e OPENAI_API_KEY="your_api_key_here" \
  -e OPENAI_MODEL="gpt-4o-mini" \
  sentiment-api-full
```

Then open:

- `http://localhost:8000/docs`

## Suggested Git Commit History

If you want to mirror the assignment request, use commits like:

```bash
git init
git add .
git commit -m "Setup FastAPI project structure"
git commit -am "Add LangChain sentiment analysis chain"
git commit -am "Add Docker configuration"
git commit -am "Improve README and environment setup"
```

## Notes

- This project requires a valid OpenAI API key to run the real LangChain chain.
- The endpoint is intentionally small and focused so it is easy to demo and explain.
- You can swap the model by changing `OPENAI_MODEL`.
