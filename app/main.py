from fastapi import FastAPI
from app.routers import users, auth
from app.database import Base, engine
from fastapi import APIRouter

app = FastAPI()
router = APIRouter()

# Creating Tables in the Database
@app.on_event("startup")
def _startup():
    Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)