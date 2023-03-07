import os
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
    server = WireMockServer(port=3000) # http://localhost:3000
    Config.base_url = f'http://localhost:{server.port}/__admin' # http://localhost:3000/__admin
    server.start()
    yield
    server.stop()

@pytest.fixture
def change_test_dir(request):
    os.chdir(request.fspath.dirname)
    yield
    os.chdir(request.config.invocation_dir)

def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """
