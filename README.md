# Notes_API

Doku Projekt Notes

Author 
    Louis Krämer
Datum 
    04.08.2025
Inhalt:
1.	Einleitung 
2.	Projketbeschreibung 
3.	Architektur und Design
4.	Implementierung 
5.	Benutzerdokumentation
6.	Referencen



1.	Einleitung 
Die Applikation soll es Usern ermöglichen Notizen auf einem Webserver zu speichern und auf die Notizen über einen Login und Register zuzugreifen. Es soll vom Web sowie vom Desktop möglich sein darauf zuzugreifen.

2.	Projektbeschreibung
Zur Umsetzung der Anwendung wird eine API erstellt die von verschiedenen Plattformen Angesprochen werden kann. Für die Oberfläche wird eine Web und eine Desktop version erstellt. Für die Desktop App wird QT und C++ verwendet für die API Python und FastAPI
Das Projekt wird von dem Autor selbst durchgeführt und soll innerhalb von 2 Wochen zum Abschluss kommen.

3.	Architektur und Design

API Struktur
Notes/
│
── app/
│   ├── __init__.py
│   ├── main.py                # Einstiegspunkt für FastAPI
│   ├── config.py              # Konfiguration (Datenbank-URL etc.)
│   ├── database.py            # Datenbankverbindung und Session-Handling
│   ├── models.py              # SQLAlchemy-Modelle (Tabellen-Definitionen)
│   ├── schemas.py             # Pydantic-Schemas (Request/Response-Validierung)
│   ├── crud.py                # CRUD-Operationen (Funktionen für DB-Zugriffe)
│   └── routers/               # API-Routen modular organisiert
│       └── users.py           # Beispiel-Router für User-Endpunkte
│       └── auth.py           # Beispiel-Router für User-Endpunkte
── auth_utils.py
── requirements.txt           # Abhängigkeiten (FastAPI, SQLAlchemy, psycopg2 etc.) 
