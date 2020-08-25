# def test_model(app, client):    # with app.app_context():
#         data = {"email": "test_model@gmail.com",
#                 "password": "admin1234"}
#         client.post('/users', json=data)
#
#         from src.models import db, User
#         resp = client.get('/users/1')
#         print(resp.json)
#         user = User.get_user_by_id(id=1)
#         db.session.delete(user)
#         db.session.commit()
