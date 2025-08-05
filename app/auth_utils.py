from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app import database, crud, auth_utils, schemas
from sqlalchemy.orm import Session
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALGORITHM = "RS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

with open(os.path.join(BASE_DIR, "private.pem"), "rb") as f:
    PRIVATE_KEY = f.read()

with open(os.path.join(BASE_DIR, "public.pem"), "rb") as f:
    PUBLIC_KEY = f.read()
    
pwd_contex = CryptContext(schemes=["bcrypt"])


def hash_password(password: str) -> str:
    return pwd_contex.hash(password)

def verify_password(plain_pwd: str, hashed_pwd: str) -> bool:
    return pwd_contex.verify(plain_pwd, hashed_pwd)

# JWT erstellen 
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, PRIVATE_KEY, algorithm=ALGORITHM)

# JWT Token prüfen
def verfify_token(token: str, credentials_exception):
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