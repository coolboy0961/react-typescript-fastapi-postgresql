from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from contextlib import contextmanager

from config import get_settings


# example:
# SQLALCHEMY_DATABASE_URL = "sqlite:///./tests/unit-test/test.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./local.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = get_settings().database_url

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
# https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager
# Dependency
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()