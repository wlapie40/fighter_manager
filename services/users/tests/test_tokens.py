import base64
import json
import time
from requests.auth import _basic_auth_str


def test_tokens(client):
    valid_credentials = base64.b64encode(b"john_conftest:admin1234").decode("utf-8")
    resp = client.post('/users/tokens',
                       headers={"Authorization": "Basic " + valid_credentials})
    assert resp.status_code == 200


def test_tokens_failed(client):
    invalid_credentials = base64.b64encode(b"john_conftest:test1234").decode("utf-8")
    resp = client.post('/users/tokens',
                       headers={"Authorization": "Basic " + invalid_credentials})
    assert resp.status_code == 401
