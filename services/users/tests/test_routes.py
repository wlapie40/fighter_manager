import json


def test_healthcheck(client):
    resp = client.get('/users/healthcheck')
    assert resp.status_code == 200


def test_add_user(app, client):
    data = {"email": "test1@gmail.com",
            "password": "admin1234"}
    with app.app_context():
        resp = client.post('/users/user', json=data)
        assert resp.status_code == 200
        assert resp.json['code'] == 201
        assert resp.json['msg'] == 'New user_id:1 added'


def test_add_twice_same_user(app, client):
    data = {"email": "test1@gmail.com",
            "password": "admin1234"}
    with app.app_context():
        resp = client.post('/users/user', json=data)
        resp_2 = client.post('/users/user', json=data)
        assert resp_2.status_code == 200
        assert resp_2.json['code'] == 409
        assert resp.json['msg'] == 'Conflict.Email: test1@gmail.com exists'