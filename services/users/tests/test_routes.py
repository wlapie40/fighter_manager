import json
import time


def test_healthcheck(client):
    resp = client.get('/users/healthcheck')
    assert resp.status_code == 200


def test_add_user(app, client):
    data = {"email": "test1@gmail.com",
            "password": "admin1234"}
    with app.app_context():
        resp = client.post('/users', json=data)
        assert resp.status_code == 200
        assert resp.json['account_activated'] == False
        assert resp.json['id'] == 1
        assert resp.json['alternative_id'] != False
        assert resp.json['created_on'] != False


def test_empty_request_add_user(app, client):
    data = {}
    with app.app_context():
        resp = client.post('/users', json=data)
        assert resp.status_code == 400
        assert resp.json['error'] == 'Bad Request'
        assert resp.json['message'] == 'must include email and password fields'


def test_add_twice_same_user(app, client):
    data = {"email": "test1@gmail.com",
            "password": "admin1234"}
    with app.app_context():
        resp = client.post('/users', json=data)
        resp_2 = client.post('/users', json=data)
        assert resp_2.status_code == 409
        assert resp.json['error'] == 'Conflict'
        assert resp.json['message'] == 'test1@gmail.com exists'


def test_get_user(app, client):
    with app.app_context():
        resp = client.get(f'/users/1')
        assert resp.json['account_activated'] == False
        assert resp.json['id'] == 1
        assert resp.json['email'] == "test1@gmail.com"
        assert resp.json['alternative_id'] != False
        assert resp.json['created_on'] != False


def test_wrong_get_user(app, client):
    with app.app_context():
        resp = client.get(f'/users/2')
        assert resp.json['status_code'] == 204
        assert resp.json['message'] == "user_id 2 does not exists"


# def test_get_users(app, client):
#     with app.app_context():
#         resp = client.get(f'/users/1')
#         assert resp.json['account_activated'] == False
#         assert resp.json['id'] == 1
#         assert resp.json['email'] == "test1@gmail.com"
#         assert resp.json['alternative_id'] != False
#         assert resp.json['created_on'] != False
#
#
# def test_delete_user(app, client):
#     with app.app_context():
#         resp = client.delete(f'/users/1')
#         assert resp.json['account_activated'] == False
#         assert resp.json['id'] == 1
#         assert resp.json['email'] == "test1@gmail.com"
#         assert resp.json['alternative_id'] != False
#         assert resp.json['created_on'] != False
