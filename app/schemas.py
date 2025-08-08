from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Annotated

# User
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True

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
        from_attributes = True

# Notes
class NoteCreate(BaseModel):
    title: str
    text: str
    category: str | None = None

class NotesOut(BaseModel):
    id: int
    title: str
    text: str
    created: datetime
    created_by: int
    category: int
    class Config:
        from_attributes = True

# Authentifiezierung benötigt response durch Tokens
class Token(BaseModel):
    access_token: str
    token_type: str

# Token Daten
class TokenData(BaseModel):
    email: str | None = None