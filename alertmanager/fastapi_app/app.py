#!/usr/bin/env python3

from fastapi import FastAPI
import uvicorn
from prometheus_client import Counter, make_asgi_app

app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

REQUEST_COUNT = Counter(
    "app_http_requests_total",        # имя метрики
    "Общее количество HTTP-запросов", # описание
    ["method", "endpoint"],           # два лейбла: метод и путь
)

@app.get("/hello")
def hello():
    # устанавливаем лейблы и увеличиваем счётчик
    REQUEST_COUNT.labels(method="GET", endpoint="/hello").inc()
    return {"message": "Hello, Prometheus!"}

# # uvicorn app:app --reload --port 8000

# if __name__ == '__main__':
#     uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)  # duplicate error
