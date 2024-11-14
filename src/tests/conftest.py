import pytest
from starlette.testclient import TestClient

from api.main import app


SERVER_URL = "http://127.0.0.1:8000"


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app, base_url=SERVER_URL)
    yield client  # testing happens here
