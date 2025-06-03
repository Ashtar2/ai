FROM python:3.12

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl \
    curl -fsSL https://ollama.com/install.sh | sh

RUN ollama pull gemma3:12b

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
