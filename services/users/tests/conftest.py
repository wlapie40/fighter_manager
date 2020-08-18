import pytest
from users.src import create_app

@pytest.fixture
def app():
    app = create_app(test_config=True)
    with app.app_context():
        # alternative pattern to app.app_context().push()
        # all commands indented under 'with' are run in the app context
        db.create_all()
        return app