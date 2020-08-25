import json
import time
from requests.auth import _basic_auth_str


def test_tokens(app, client):
    data = {"email": "token_1@gmail.com",
            "password": "admin1234",
            "username": "token_1"}
    with app.app_context():
        client.post('/users', json=data)
        resp = client.post('/users/tokens', headers={"Authorization": "Basic {'token_1', 'admin1234'}"})
        print(resp)
        print(resp.json)
