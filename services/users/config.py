import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # APP
    FLASK_ENV = os.environ.get("FLASK_ENV", None)
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG", None)
    FLASK_APP = os.environ.get("FLASK_APP", None)
    FLASK_PORT = os.environ.get("FLASK_PORT", None)
    FLASK_TESTING = os.environ.get("FLASK_TESTING", 0)
    INGRESS = os.environ.get("INGRESS", None)
    SECRET_KEY = os.urandom(24)
    # DB
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", None)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_SCHEMA = os.environ.get("USER_SCHEMA", None)


class TestConfig:
    FLASK_ENV = os.environ.get("FLASK_ENV", None)
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG", None)
    FLASK_APP = os.environ.get("FLASK_APP", None)
    FLASK_PORT = os.environ.get("FLASK_PORT_TEST", None)
    FLASK_TESTING = os.environ.get("FLASK_TESTING_TEST", None)
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_TEST", None)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_SCHEMA = os.environ.get("USER_SCHEMA_TEST", None)
