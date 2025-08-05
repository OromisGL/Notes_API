from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from . import schemas, crud, database
from .. import auth_utils

router = APIRouter(prefix="/auth", tags=["Authentication"])

# Login Endpoint 

@router.post("/login", response_model=schemas.Token)
def login(from_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = crud.get_users_by_email(db, from_data.username)
    
    if not user or not auth_utils.verify_password(from_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = auth_utils.create_access_token({"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}