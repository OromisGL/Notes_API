import os
os.environ["DATABASE_URL"] = "sqlite+pysqlite:///:memory:"  # oder sqlite:///./test.db

# erst danach:
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from app.database import Base
import pytest

engine = create_engine(
    os.environ["DATABASE_URL"], connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(

bind=engine, autocommit=False, autoflush=False
)

@pytest.fixture(autouse=True)
def create_test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def db_session():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
