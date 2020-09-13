def test_model(client):
        data = {"account_type": "fighter",
                "username": "test_model_1",
                "email": "test_model_1@gmail.com",
                "password": "admin1234"}
        client.post('/users', json=data)

        from src.models import db, User
        user = User.get_user_by_email(email="test_model_1@gmail.com")
        assert user.email == "test_model_1@gmail.com"
