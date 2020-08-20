import os


def test_testing_config(app):
    app.config.from_object('config.TestConfig')
    assert app.config['USER_SCHEMA'] == os.environ.get("USER_SCHEMA")
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get("SQLALCHEMY_DATABASE_URI")
