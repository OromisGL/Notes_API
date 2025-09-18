**Dokumentation Notes API**

Autor:

Louis Krämer

04.08.2025

**Inhaltsverzeichnis**

1. **Einleitung**
2. **Projektbeschreibung**
3. **Architektur und Design**
4. **Implementierung**
5. **Benutzerdokumentation**
6. **Referenzen**
7. Einleitung

Die Folgende Dokumentation soll einen Einblick in die Implementierung einer API mit Client geben. Sie wurde im Rahmen der Umschung zum Fachinformatiker für Anwendungsentwicklung erstellt und ist Teil der Abschlussprüfung.

Das Projekt ist in Python geschrieben mit einem Fokus auf Funktionalität der API und nicht auf UX Design.

Die Folgenden Punkte führen den Leser durch den Gedanklichen Prozess während der Entwicklungs und Implemtierungsphase. Am ende Werden sich einige Ausschnitte aus dem Code finden um Kernelemente besser zu zeigen.

1. Projektbeschreibung

Das Ziel dieser API soll es sein Sicher Daten von Verschiedenen Anwendungen und Endgeräten zu speichern. Durch die Flexible Gestaltung wird es einer Desktop anwendung genau so möglich sein anfragen zu stellen wie eine klassische UI im Browser.

Am Ausgangspunkt für dieses Projekt stand die Frage nach eine brauchbaren Anwendung die auf vielen Plattformen verwendung finden kann und einfach zu Implementieren ist. Dieses Projekt dient als Fallstudie für API Design und Konzenption. Alle Probleme und Lösungen auf die dieses Projekt stößt genießen nicht den Anspruch die Besten oder Effizientesten zu sein, es sind schlicht weg meine Lösungen die auf dem Momentanten Stand meines Wissens und erfahrungslevels beruhen.

Das Projekt Nutzt FastAPI um eineübersichtliche, schnelle und eine universell ansprachbare API zu gestalten. Die Datenbank ist auf PostgresSQL Basis. Das SQL Toolkit SQLAlchemy dient zur Verbindung der Backendlogik mit der Relationalen Datenbank.

Für die sichere Datenübermittlung zwischen Server und Client wird das Python Modul Jose verwendet dass die Verwendung von JWT (JSON Web Tokens) ermöglicht.

Das Ziel dieser Anwendung ist es Notizen von einzelnen Nutzern zu speichern. Die Notizen können einen Titel und eine Kategorie bekommen. Die Kategorien können neu erstellt oder vorhandene Verwendet werden. Um die Anwendung zu Nutzen muss man einen Account erstellen. Dies erfolgt über einen Register Endpoint in der API. Der Nutzer kann hier eine Email Adresse Angeben und ein Password festlegen. Das Passwort wird als Hash in der Datenbank gespeichert.

Bei der Registrierung sowie beim darauf folgenden Login wird ein Cookie für eine Session erstellt der die sichere Kommunikation während der Session herstellt. Nachdem der Cookie Abgelaufen ist kann er erneuert werden indem man sich erneut anmeldet.

Das Projekt beschränkt sich auf eine Rudimentäre API die alle Basis Funktionen zum Zugriff auf eine API bietet. Der damit einhergehende Client ist auch in FastAPI Entiwickelt und kann über eine einfache eingabemaske im Browser bedient werden. Alle weiteren Clients sind nicht für dieses Projekt gedacht, die API soll nur beweisen dass sie mit dem Wb Client interagieren kann. Der Client soll als Vorlage für eine Desktop App und Browser Erweiterung genutzt werden.

Das Projekt wurde in Python Verwirklicht. Dies ermöglicht eine Plattform Unabhängige Verwendung des Produkts. Als IDE Wurde Visual Studio Code verwendet auf dem Betriebssystem MacOS.

1. Architektur und Design

![Ein Bild, das Text, Screenshot, Schrift, Dokument enthält.  KI-generierte Inhalte können fehlerhaft sein.](data:image/png;base64...)Für das Projekt habe ich eine einfache Ordnerstrucktur gewählt. Durch die Bereitstellung des Services über Docker-Container bekomme ich eine Flexible Entwicklungsumgebung. Für gute Lesabarkeit des Codes habe ich Versucht sinnvolle Unterteilungen der Module in verschiedene Dateien zu finden. So sind für die Übersichtlichkeit gewisse Konstanten in einzelne Dateien ausgelagert worden, z.B. In config.py in der ausschießlich die URL für die Datenbank verbindung steht. So kann die URL gut Verändert und Importiert werden an Orten an denen sie benötigt wird. Dieser Modulare Projektaufbau vereinfacht die Lesbarkeit und die Wartbarkeit des Codes. Alle Benötigten zusätzlichen Abhängigkeiten können einfach in die Textdatei requirements.txt hinzugefügt werden und werden nach erneutem Starten des Docker-Containers Integriert. Das Verinfacht das Deployment und die Skalierbarkeit für Zukünftige erweiterungen oder Anwendungen die mit dieser API verwirklicht werden sollen. Zudem ermöglicht die Verwendung von Router eine klare Abgrenzung der einzelnen Zuständigkeiten der ein einzelnen Zugriffspunkte die es so ermöglichen die Anwendung einfach um Funktionen zu erweitern ohne zusätzliche Architektonische die bis hier hin getroffen wurden zu verändern.

Abbildung Projektstruktur

Abbildung Struktur der API

Die Datenbank ist in drei Tabellen unterteilt. Für dieses Projekt wird die Version postgres 17 verwendet. Die Relationale Datenbank wird auf einem Docker-Container Virtualisiert und kann mit Start der Container Sofort von der Anwendung erreicht werden. Das Toolkit sqlalchemy ermöglicht mit seinen Klassen eine Komfortable Erstellung der Datenbank und seiner Relationen. Durch die Klasse Session wird das Mapping für die einzelnen CRUD Funktionen ermöglicht. Die Aktualisierung von Inhalten in der Datenbank geschieht über von sqlalchemy bereitgestellten Funktionen wie:

Add(), commit(), rollback(), und refresh()

![Ein Bild, das Screenshot, Text, Schrift, Design enthält.  KI-generierte Inhalte können fehlerhaft sein.](data:image/png;base64...)

Abbildung Datenbank

![](data:image/png;base64...)In der Folgenden Abildung wird die Verkettung der Verschiedenen Routes in der Anwendung abgebildet. Hier ist gut die Trennung von User Funktionen und der Authentifizierung zu erkennen. Die verschiednen Routes auf der User seite sind erreichbar nach eine Erfolgreichen Authentifizierung und Validierung der Login Daten. Die Schemas sind die Daten die bei der Abfrage übermittelt werden um die Richtige Menge an Informationen zu liefern und nicht dden gesamten Datensatz aus der Tabelle. Wie auch gut zu erkenne ist, ist dass der Login jediglich die erzeugung eines Tokens zur Folge hat. Dieser Token wird bei allen weiteren Abfragen der API Verwendet um die Abfrage zu Verifizieren. Der Token hat eine Lebensdauer von 30min und ermöglicht so einen sicheren Umgang mit der Session bei Inaktiviät des Users.

Abbildung Router Graph (FastAPI)
