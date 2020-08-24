import json
import time


def test_healthcheck(client):
    resp = client.get('/users/healthcheck')
    assert resp.status_code == 200


def test_add_user(app, client):
    data = {"email": "test1@gmail.com",
            "password": "admin1234"}
    with app.app_context():
        resp = client.post('/users/user', json=data)
        assert resp.status_code == 200
        assert resp.json['account_activated'] == False
        assert resp.json['id'] == 1
        assert resp.json['alternative_id'] != False
        assert resp.json['created_on'] != False


def test_empty_request_add_user(app, client):
    data = {}
    with app.app_context():
        resp = client.post('/users/user', json=data)
        assert resp.status_code == 200
        assert resp.json['code'] == 404
        assert resp.json['msg'] == "KeyError: key 'email' not found"


def test_add_twice_same_user(app, client):
    data = {"email": "test1@gmail.com",
            "password": "admin1234"}
    with app.app_context():
        resp = client.post('/users/user', json=data)
        resp_2 = client.post('/users/user', json=data)
        assert resp_2.status_code == 200
        assert resp_2.json['code'] == 409
        assert resp.json['msg'] == 'Conflict.Email: test1@gmail.com exists'


def test_get_user(app, client):
    with app.app_context():
        resp = client.get(f'/users/user/1')
        assert resp.json['account_activated'] == False
        assert resp.json['id'] == 1
        assert resp.json['email'] == "test1@gmail.com"
        assert resp.json['alternative_id'] != False
        assert resp.json['created_on'] != False


def test_wrong_get_user(app, client):
    with app.app_context():
        resp = client.get(f'/users/user/2')
        assert resp.json['code'] == 204
        assert resp.json['msg'] == "user_id 2 does not exists"


def test_get_users(app, client):
    with app.app_context():
        resp = client.get(f'/users/user/1')
        assert resp.json['account_activated'] == False
        assert resp.json['id'] == 1
        assert resp.json['email'] == "test1@gmail.com"
        assert resp.json['alternative_id'] != False
        assert resp.json['created_on'] != False


def test_delete_user(app, client):
    with app.app_context():
        resp = client.delete(f'/users/user/1')
        assert resp.json['account_activated'] == False
        assert resp.json['id'] == 1
        assert resp.json['email'] == "test1@gmail.com"
        assert resp.json['alternative_id'] != False
        assert resp.json['created_on'] != False
