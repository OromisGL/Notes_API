import time, requests
from jose import jwt
from app.auth_utils import PUBLIC_KEY

#TODO
ATH_URL = "http://localhost:8000/docs#/"

class TokenManager:
    """_summary_
    Classe zur Clientseitigen Token Validierung und Verifizierung mit der API.
    Authentifiezierung geschieht über email und password.
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.expiers_at = 0
    
    def authenticate(self):
        # Fetching von email und Passwort
        response = requests.post(ATH_URL, json={
            "username": self.username,
            "password": self.password
        })
        # Check von HTTP Errors
        response.raise_for_status()
        # Daten in JSON Format umwandeln 
        data = response.json()
        # Access Token raus Filtern 
        self.token = data["access_token"]
        # Verfalsszeit Festlegen
        self.expiers_at = time.time() + data.get("expires_in", 3600)
    
    def get_token(self):
        if not self.token or time.time() > self.expiers_at - 3000:
            self.authenticate()
        return self.token
    
    def verify(self, token):
        return jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
