from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database, auth_utils

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/getuserdata", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(database.get_db)):
    return crud.get_user(db)

@router.post("/post/notes", response_model=schemas.NotesOut)
def create_note(
        note: schemas.NoteCreate, 
        db: Session = Depends(database.get_db),
        current_user: schemas.UserOut = Depends(auth_utils.get_current_user)
        ):
    category_obj = crud.create_category(db, note.category)
    note_obj = crud.create_notes(
        db,
        note.text,
        current_user.id,
        category_obj.id,
    )
    return note_obj