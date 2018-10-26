from base64 import b64encode
from contextlib import suppress

import pytest

from talkshow.app import create_app
from talkshow.ext.login import create_user


@pytest.fixture(scope='module')
def app():
    """Flask Pytest uses it"""
    _app = create_app(MONGODB_NAME='test_db')
    with _app.app_context(), suppress(RuntimeError):
        # creates new admin user to be used in tests if it does not exist
        create_user("admin", "1234")
    return _app


@pytest.fixture(scope='module')
def auth():
    """The Basic Auth credentials for testing"""
    credentials = b64encode(bytes("admin:1234", 'ascii')).decode('ascii')
    data = {'Authorization': 'Basic ' + credentials}
    return data
