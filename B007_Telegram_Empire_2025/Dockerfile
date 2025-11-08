FROM python:3.12-slim
LABEL author="B 007" version="10.0" description="B 007 Telegram Empire 2025 - Unbannable Creator"

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]