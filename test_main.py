from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    """Тест для корневого эндпоинта"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}


def test_predict_positive_sentiment():
    """Тест для предсказания позитивной тональности"""
    response = client.post("/predict", json={"text": "I love MLOps, it is so cool!"})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["label"] == "POSITIVE"
    assert isinstance(json_data["score"], float)


def test_predict_negative_sentiment():
    """Тест для предсказания негативной тональности"""
    response = client.post(
        "/predict", json={"text": "I hate bugs in my code, it is so frustrating!"}
    )
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["label"] == "NEGATIVE"
    assert isinstance(json_data["score"], float)
