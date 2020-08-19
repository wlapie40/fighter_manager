import pytest
from src import create_app, db


@pytest.fixture(scope='session')
def app():
    app = create_app(test_config=True)
    app.config.from_object('config.TestConfig')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
