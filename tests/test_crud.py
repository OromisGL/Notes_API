from app import crud, models
from app.auth_utils import BASE_DIR
import os

with open(os.path.join(BASE_DIR, "/tests/test_text.txt"), "rb") as f:
    TEST_TEXT = f.read()


def test_create_note_sets_create_and_returns_object(db_session):
    user = models.User(email="u@e.de", password="...")
    category = models.Category(description="Test")
    db_session.add_all([user, category])
    db_session.commit()
    db_session.refresh(user)
    db_session.refresh(category)
    
    note = crud.create_notes(
        db=db_session,
        text=TEST_TEXT,
        user_id=user.id,
        category=category.id
    )
    # Assert
    assert note.id is not None
    assert note.text == TEST_TEXT
    assert note.category == category.id
    assert note.created is not None 