import pytest
from datetime import datetime, timedelta
from src import create_app, db


@pytest.fixture(scope='session', autouse=True)
def app():
    app = create_app(test_config=True)
    app.config.from_object('config.TestConfig')
    with app.app_context():
        db.create_all()

        add_test_user()

        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


def add_test_user():
    from src.models import User

    test_user_1 = User(
        account_type="fighter",
        username="john_conftest",
        email="john_conftest@gmail.com",
        password="admin1234"
    )
    db.session.add(test_user_1)
    test_user_1.token = '3lw/P3MAltQ/l4a66ZFRFyFDcqwgtlVx'
    test_user_1.token_expiration = datetime.now() + timedelta(seconds=3600)
    db.session.commit()

