from sqlalchemy.orm import Session
from . import models, schemas
from auth_utils import hash_password
from datetime import datetime
def create_user(db: Session, user: schemas.UserCreate):
    hashed_pwd = hash_password(user.password)
    db_user = models.User(
        name=user.name, 
        email=user.email,
        hashed_password=hashed_pwd
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session):
    return db.query(models.User).all()

def create_category(db: Session, category: schemas.CartegoryCreate):
    db_cat = models.Category(description=category.description)
    db.app(db_cat)
    db.commit()
    db.refresh()
    return db_cat

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def create_notes(db: Session, note: schemas.NoteCreate):
    db_note = models.Notes(
        text=note.text,
        created=datetime.now(datetime.timezone.utc),
        created_by=note.created_by,
        category=note.category
    )
    db.add(db_note)
    db.commit()
    db.refresh()
    return db_note

def get_notes(db: Session):
    return db.query(models.Notes).all()

def get_notes_by_user(db: Session, user_id: int):
    return db.query(models.Notes).filter(models.Notes.created_by == user_id).all()

def get_notes_by_id(db: Session, note_id: int):
    return db.query(models.Notes).filter(models.Notes.id == note_id).first()

def get_notes_by_category(db: Session, user_id: int, category_id: int):
    return (
        db.query(models.Notes).filter(
            models.Notes.created_by == user_id,
            models.Notes.category == category_id).all()
        )

