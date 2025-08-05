# ---- Dockerfile für FastAPI ----
# Basis-Image mit Python
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /code
ENV PYTHONPATH=/code

# requirements.txt zuerst kopieren und installieren (bessere Caching-Schichten)
COPY app/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# Restlichen Code kopieren
COPY . /code

# Standardport für FastAPI
EXPOSE 8000

# Startbefehl für FastAPI (mit uvicorn)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
