import json
import time


# def test_add_user(app, client):
#     data = {"account_type": "fighter",
#             "email": "test1@gmail.com",
#             "password": "admin1234",
#             "username": "test1"}
#     with app.app_context():
#         resp = client.post('/users', json=data)
#         assert resp.status_code == 200
#         assert resp.json['account_activated'] == False
#         assert resp.json['id'] != False
#         assert resp.json['alternative_id'] != False
#         assert resp.json['created_on'] != False
#
#
# def test_empty_request_add_user(app, client):
#     data = {}
#     with app.app_context():
#         resp = client.post('/users', json=data)
#         assert resp.status_code == 400
#         assert resp.json['error'] == 'Bad Request'
#         assert resp.json['message'] == 'must include email, password and username fields'
#
#
# def test_add_twice_same_username(app, client):
#     data = {"account_type": "fighter",
#             "email": "test2@gmail.com",
#             "password": "admin1234",
#             "username": "test1"}
#     with app.app_context():
#         resp = client.post('/users', json=data)
#         resp_2 = client.post('/users', json=data)
#         assert resp_2.status_code == 400
#         assert resp.json['error'] == 'Bad Request'
#         assert resp.json['message'] == 'please use a different username'
#
#
# def test_add_twice_same_email(app, client):
#     data = {"account_type": "fighter",
#             "email": "test1@gmail.com",
#             "password": "admin1234",
#             "username": "test2"}
#     with app.app_context():
#         resp = client.post('/users', json=data)
#         resp_2 = client.post('/users', json=data)
#         assert resp_2.status_code == 400
#         assert resp.json['error'] == 'Bad Request'
#         assert resp.json['message'] == 'please use a different e-mail'
#
#
def test_get_user(app, client):
    with app.app_context():
        resp = client.get('/users/1')
        # print(resp.json)
        # assert resp.json['account_activated'] == False
        # assert resp.json['id'] != False
        # assert resp.json['email'] != False
        # assert resp.json['alternative_id'] != False
        # assert resp.json['created_on'] != False

#
# def test_wrong_get_user(app, client):
#     test_id = 1000
#     with app.app_context():
#         resp = client.get(f'/users/{test_id}')
#         assert resp.json['status_code'] == 204
#         assert resp.json['message'] == f"user_id {test_id} does not exists"
#
#
# def test_get_users(app, client):
#     with app.app_context():
#         resp = client.get('/users/1')
#         assert resp.json['account_activated'] == False
#         assert resp.json['id'] != False
#         assert resp.json['email'] != False
#         assert resp.json['alternative_id'] != False
#         assert resp.json['created_on'] != False
#
#
# def test_delete_user(app, client):
#     with app.app_context():
#         resp = client.delete(f'/users/1')
#         assert resp.json['account_activated'] == False
#         assert resp.json['id'] != False
#         assert resp.json['email'] != False
#         assert resp.json['alternative_id'] != False
#         assert resp.json['created_on'] != False
