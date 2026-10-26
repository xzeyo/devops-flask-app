# TW1 3.1 - minimal image for the Flask "Hello World" app, serving on port 5000
FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir flask psycopg2-binary
COPY hello.py .
EXPOSE 5000
CMD ["python", "hello.py"]
