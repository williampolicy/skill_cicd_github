# tests/test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    print("test client")
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    print("test test_hello_world")
    rv = client.get('/')
    assert rv.data == b'Hello, World!'


if __name__ == '__main__':
    pytest.main()
