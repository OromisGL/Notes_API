# ---- Dockerfile für FastAPI ----
# Basis-Image mit Python
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /code

# Abhängigkeiten installieren
# (requirements.txt muss im app/ Ordner liegen)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Anwendungscode in den Container kopieren
COPY . .

# Standardport für FastAPI
EXPOSE 8000

# Startbefehl für FastAPI (mit uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
