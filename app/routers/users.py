from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, database, auth_utils
from typing import Optional, List

router = APIRouter(prefix="/users", tags=["Users"])

# Bei allen get anfragen List[] bnutzen 
@router.get("/getuserdata", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(database.get_db)):
    return crud.get_user(db)

@router.post("/post/notes", response_model=schemas.NotesOut)
def create_note(
        note: schemas.NoteCreate, 
        db: Session = Depends(database.get_db),
        current_user: schemas.UserOut = Depends(auth_utils.get_current_user)):
    category_obj = crud.create_category(db, note.category)
    
    title = note.title
    
    if title == "string":
        temp = ''
        text = note.text.split()
        for i in range(2):
            temp += text[i]
            temp += ' '
        title = temp
    
    note_obj = crud.create_notes(
        db,
        title,
        note.text,
        current_user.id,
        category_obj.id,
    )
    return note_obj

@router.get("/get/notes", response_model=List[schemas.NotesOut])
def get_note_from_user(
        db: Session = Depends(database.get_db),
        current_user: schemas.UserOut = Depends(auth_utils.get_current_user)):
    
    return crud.get_notes_by_user(db, current_user.id)


@router.get("/notes/{category}", response_model=List[schemas.NotesOut]) 
def get_notes_category(
        category: str,
        db: Session = Depends(database.get_db),
        current_user: schemas.UserOut = Depends(auth_utils.get_current_user)):
    
    category_id = crud.get_category_id_by_desc(db, category)
    
    if category_id is None:
        raise HTTPException(status_code=404, detail="Kategorie nicht gefunden")
    
    return crud.get_notes_by_category(db, current_user.id, category_id)