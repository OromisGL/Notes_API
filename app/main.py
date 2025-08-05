from fastapi import FastAPI
from app.routers import users, auth
from app.database import Base, engine
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app import crud, schemas, database

app = FastAPI()
router = APIRouter()

# Creating Tables in the Database
Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)