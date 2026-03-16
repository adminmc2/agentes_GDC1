FROM python:3.12-slim

WORKDIR /app

# System deps for psycopg2 + Node.js para promptfoo
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libpq-dev curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y --no-install-recommends nodejs && \
    rm -rf /var/lib/apt/lists/*

# promptfoo (CLI para comparar LLMs)
RUN npm install -g promptfoo

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "diagrama.py"]
