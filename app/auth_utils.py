from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status
from . import schemas
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY_PATH = os.path.join(BASE_DIR, "jwt_secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

with open(SECRET_KEY_PATH, "rb") as f:
    SECRET_KEY = f.read().decode().strip()

pwd_contex = CryptContext(schemes=["bcrypt"], debrecated=["auto"])


def hash_password(password: str) -> str:
    return pwd_contex.hash(password)

def verify_password(plain_pwd: str, hashed_pwd: str) -> bool:
    return pwd_contex.verify(plain_pwd, hashed_pwd)

# JWT erstellen 
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now(datetime.timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# JWT Token prüfen
def verfify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email in None:
            raise credentials_exception
        return schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception