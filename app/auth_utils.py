from passlib.context import CryptContext


pwd_contex = CryptContext(schemes=["bcrypt"], debrecated="auto")


def hash_password(password: str) -> str:
    return pwd_contex.hash(password)

def verify_password(plain_pwd: str, hashed_pwd: str) -> bool:
    return pwd_contex.verify(plain_pwd, hashed_pwd)