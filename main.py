from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(
    title="Sentiment Analysis API",
    description="A simple API to analyze the sentiment of a text using a Hugging Face model.",
    version="0.1.0",
)

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)

class TextToAnalyze(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    label: str
    score: float

@app.get("/")
def read_root():
    """Корневой эндпоинт, который может проверить на доступность API"""
    return {"status": "API is running"}

@app.post("/predict", response_model=SentimentResponse)
def predict_sentiment(payload: TextToAnalyze):
    """
    Предсказывает тональность текста.
    Принимает JSON с полем "text" и возвращает тональность и уверенность.
    """
    result = sentiment_pipeline(payload.text)[0]
    return SentimentResponse(label=result['label'], score=result['score'])

# Чтобы запустить локально: uvicorn main:app --reload
