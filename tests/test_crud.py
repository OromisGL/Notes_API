from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "app"
(APP_DIR / "private.pem").write_text("dummy")
(APP_DIR / "public.pem").write_text("dummy")

from app import crud, models

TEST_TEXT = Path(__file__).with_name("test_text.txt").read_text()

def test_create_note_sets_create_and_returns_object(db_session):
    user = models.User(email="u@e.de", password="...")
    category = models.Category(description="Test")
    db_session.add_all([user, category])
    db_session.commit()
    db_session.refresh(user)
    db_session.refresh(category)

    note = crud.create_notes(
        db=db_session,
        title="Test Title",
        text=TEST_TEXT,
        user_id=user.id,

    category=category.id,
    )


    assert note.id is not None
    assert note.text == TEST_TEXT
    assert note.category == category.id
    assert note.created is not None
