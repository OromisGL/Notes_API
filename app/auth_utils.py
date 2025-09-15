from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app import database, crud, schemas
from sqlalchemy.orm import Session
import os

"""
    The code defines functions for hashing passwords, creating and verifying JWT tokens, and getting the
    current user based on the token provided.
    
    :param password: The code you provided defines functions for hashing passwords, verifying passwords,
    creating access tokens, and verifying JWT tokens. It also includes a function to get the current
    user based on the token provided
    :type password: str
    :return: The code snippet provided defines several functions and variables related to authentication
    and token handling in a FastAPI application. Here is a summary of what is being returned by the
    code:
    """


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALGORITHM = "RS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

with open(os.path.join(BASE_DIR, "private.pem"), "rb") as f:
    # Liest den Private Key aus
    PRIVATE_KEY = f.read()

with open(os.path.join(BASE_DIR, "public.pem"), "rb") as f:
    # liest den Public Key aus
    PUBLIC_KEY = f.read()
    
# Algorythmus für Passwort Verschlüsselung
pwd_contex = CryptContext(schemes=["bcrypt"])


def hash_password(password: str) -> str:
    # Nimmt Klartext und gibt hash 
    return pwd_contex.hash(password)

def verify_password(plain_pwd: str, hashed_pwd: str) -> bool:
    # gleicht den Klartext mit gespeicherten Hashwert ab
    return pwd_contex.verify(plain_pwd, hashed_pwd)

# JWT erstellen 
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    # Erstellt einen Tokenstring und übermittelt die Lebensdauer 
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, PRIVATE_KEY, algorithm=ALGORITHM)

# JWT Token prüfen
def verfify_token(token: str, credentials_exception):
    # Verifiziert den Token mit dem Public Key
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        return schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    # User anhand des Tokens Verifizien 
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = crud.get_users_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user