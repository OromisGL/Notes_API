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



## 1.	Einleitung 
Die Applikation soll es Usern ermöglichen Notizen auf einem Webserver zu speichern und auf die Notizen über einen Login und Register zuzugreifen. Es soll vom Web sowie vom Desktop möglich sein darauf zuzugreifen.

## 2.	Projektbeschreibung
Zur Umsetzung der Anwendung wird eine API erstellt die von verschiedenen Plattformen Angesprochen werden kann. Für die Oberfläche wird eine Web und eine Desktop version erstellt. Für die Desktop App wird QT und C++ verwendet für die API Python und FastAPI
Das Projekt wird von dem Autor selbst durchgeführt und soll innerhalb von 2 Wochen zum Abschluss kommen.

## 3.	Architektur und Design

API Struktur
```plaintext
Notes/
│
├── app/
│   ├── __init__.py
│   ├── auth_util.py           # Funktionen zur Validierung und Authentifizierung
│   ├── main.py                # Einstiegspunkt für FastAPI
│   ├── config.py              # Konfiguration (Datenbank-URL etc.)
│   ├── database.py            # Datenbankverbindung und Session-Handling
│   ├── models.py              # SQLAlchemy-Modelle (Tabellen-Definitionen)
│   ├── schemas.py             # Pydantic-Schemas (Request/Response-Validierung)
│   ├── crud.py                # CRUD-Operationen (Funktionen für DB-Zugriffe)
│   ├── private.pem            # Privater Hash 
│   ├── public.pem             # Öffentlicher Hash
│   └── routers/               # API-Routen modular organisiert
│       ├── __init__.py
│       ├── users.py           # Beispiel-Router für User-Endpunkte
│       └── auth.py            # Beispiel-Router für User-Endpunkte
├── requirements.txt           # Abhängigkeiten (FastAPI, SQLAlchemy, psycopg2 etc.) 
├── docker-compose.yaml        # Definition der Docker services
├── Dokerfile                  # Commands für den Docker container 
```

Für die Authentifizierung wird das JWT Protokoll verwendet. Aus der python libary jose, die alle Algorythmen zur verfügung stellt.
Hier wird auf Asymetrische verschlüsselung gesetzt um die Authetifizierung mit der API möglichst sicher zu gestalten, da es sich 
hier um möglicherweise sensible Daten handeln könnte. Um das Schlüsselpaar zu erzeugen wurde openssl verwendet mit dem "RS256" Hashing Algorythmus.
Falls das Projekt Öffentlich gemacht wird muss die Architektur dh. die Speicherung der Schlüssel Angepasst werden. 
```plaintext
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

Für das Hashing der Passwörter wird die passlib libary verwendet. [Doku passlib](https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html#context-basic-example)

Zur Validierung der eingegebenen Daten werden schemas mit Pydantic BaseModel erstellt, um die richtigen 
Datentypen und die Übermittelte Struktur zu gewährleisten. [BaseModel Doku](https://docs.pydantic.dev/latest/concepts/models/)

Das Relationale Modell wird mit sqlAlchemy Erstellt. 
Verwendung finden hier funktion declarative_base(), die in der deklaration der Klassen für die Tabellen 
verwendet wird und "mapped" die einzelnen klassen zusammen zu einem Datenbank Modell. 
Die Verwendung von declarative_base() ermöglicht die verwendung des Attributes "__tablename__" und der Klasse Column(). Zudem kann man Relationen erstellen mit relationship die sich auf einzelne Datensätze beziehen. [Doku SQLAlchemy](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html)


Die Gerstaltung der 
