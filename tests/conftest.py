import pytest
from base64 import b64encode
from talkshow.app import create_app


@pytest.fixture(scope="module")
def app():
    """Flask Pytest uses it"""
    return create_app()


@pytest.fixture(scope="module")
def auth():
    """The Basic Auth credentials for testing"""
    credentials = b64encode(bytes("admin:1234", 'ascii')).decode('ascii')
    data = {'Authorization': 'Basic ' + credentials}
    return data
