import json
import time


def test_healthcheck(client):
    resp = client.get('/users/healthcheck')
    assert resp.status_code == 200