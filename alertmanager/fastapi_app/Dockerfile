FROM python:3.13-alpine
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
ENTRYPOINT [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
