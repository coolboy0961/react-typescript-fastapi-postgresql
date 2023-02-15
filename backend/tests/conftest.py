import pytest
from fastapi.testclient import TestClient
from ..main import create_app


@pytest.fixture()
def app():
    app = create_app()

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app) -> TestClient:
    return TestClient(create_app())
