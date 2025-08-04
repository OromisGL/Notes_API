from pydantic import BaseModel
from datetime import datetime

# User
class UserCreate(BaseModel):
    name: str
    email: str
    password_hash: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str

# Category
class CartegoryCreate(BaseModel):
    description: str

class CategoryOut(BaseModel):
    id: int
    description: str
    class Config:
        orm_mode: True

# Notes
class NoteCreate(BaseModel):
    text: str
    category: int

class NotesOut(BaseModel):
    id: int
    text: str
    created: datetime
    created_by: int
    category: int
    class Config:
        orm_mode = True

# Authentifiezierung benötigt response durch Tokens
class Token(BaseModel):
    access_token: str
    token_type: str

# Token Daten
class TokenData(BaseModel):
    email: str | None = None