import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # APP
    FLASK_ENV = os.environ.get("FLASK_ENV", None)
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG", None)
    FLASK_APP = os.environ.get("FLASK_APP", None)
    FLASK_PORT = os.environ.get("FLASK_USERS_PORT", None)
    FLASK_TESTING = os.environ.get("FLASK_TESTING", 0)
    INGRESS = os.environ.get("INGRESS", None)
    SECRET_KEY = os.urandom(24)
    # DB
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", None)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_SCHEMA = os.environ.get("USER_SCHEMA", None)


class TestConfig:
    FLASK_ENV = "development"
    FLASK_DEBUG = 1
    FLASK_APP = "wsgi.py"
    FLASK_PORT = 5010
    FLASK_TESTING = 1
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://coco_butter_user:superstrongpassword@db:5432/cocoa_butter_dev"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USER_SCHEMA = "test_cocoa_butter_users"
