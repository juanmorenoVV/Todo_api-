FROM python:3.11-slim

WORKDIR /app

# Copiamos solo requirements para aprovechar cache
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del proyecto
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
