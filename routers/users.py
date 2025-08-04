from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Pydantic validiert hier automatisch: name, email, password sind Pflichtfelder
    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db)