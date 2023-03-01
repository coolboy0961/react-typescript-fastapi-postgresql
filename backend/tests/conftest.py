import time
import subprocess
import pytest
from fastapi.testclient import TestClient
from wiremock.server import WireMockServer
from wiremock.constants import Config

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
def wiremock_server():
    server = WireMockServer(port=3000)
    Config.base_url = 'http://localhost:{}/__admin'.format(server.port)
    server.start()
    yield
    server.stop()