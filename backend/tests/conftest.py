import time
import subprocess
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

@pytest.fixture()
def json_server(request):
    json_file_path = request.param
    print(f"json_server will start on {json_file_path}")
    print("start json server")
    server_process = subprocess.Popen(
        ["pipenv", "run", "json-server", json_file_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print("wait for json server starting")
    time.sleep(2)

    yield

    print("kill json server")
    server_process.terminate()