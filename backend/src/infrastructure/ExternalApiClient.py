import requests
from contextlib import contextmanager
from config import get_settings

@contextmanager
def get_request_session():
    session = requests.session()
    try:
        yield session
    finally:
        session.close()

class ExternalApiClient:
    def __init__(self) -> None:
        self.base_url = get_settings().base_url
    def get(self, path: str):
        with get_request_session() as requests_session:
            response = requests_session.get(self.base_url + path)
            response.raise_for_status()
            return response
