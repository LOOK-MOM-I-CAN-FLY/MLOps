FROM python:3.9-slim

WORKDIR /app

ENV HF_HOME /app/cache

RUN mkdir -p /app/cache && chmod 777 /app/cache

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]