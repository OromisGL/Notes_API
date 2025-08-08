from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app import schemas, crud, database
from app import auth_utils
from pathlib import Path

router = APIRouter(prefix="/auth", tags=["Authentication"])

PUBLIC_KEY_PATH = Path(__file__).resolve().parent.parent / "public.pem"

# Public Key Endpoint

@router.get("/public_key", summary="Liefert den Public Key für die Respons Validation des Clients")
def get_key():
    key = PUBLIC_KEY_PATH.read_text()
    return Response(content=key, media_type="application/x-pem-file")

# Login/register Endpoint 

@router.post("/register", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Pydantic validiert hier automatisch: name, email, password sind Pflichtfelder
    existing_user = crud.get_users_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="User already exists.")

    return crud.create_user(db=db, user=user)

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = crud.get_users_by_email(db, form_data.username)
    
    if not user or not auth_utils.verify_password(form_data.password, user.password):
        return RedirectResponse(url="/", status_code=303)
    
    access_token = auth_utils.create_access_token({"sub": form_data.username})
    
    return {"access_token": access_token, "token_type": "bearer"} 