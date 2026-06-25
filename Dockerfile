FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy psycopg2-binary pydantic

CMD ["uvicorn", "src.reservas.api:app", "--host", "0.0.0.0", "--port", "8001"]