import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.infrastructure.database import Base
from ..main import app
from src.infrastructure.database import engine


@pytest.fixture()
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

@pytest.fixture()
def client() -> TestClient:
    return TestClient(app)
