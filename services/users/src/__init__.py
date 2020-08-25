import logging
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from pprint import pprint

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Globally accessible libraries
db = SQLAlchemy()
basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


def create_app(test_config=False):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    if not test_config:
        logging.info(":::__init__.py::: DEV")
        app.config.from_object('config.Config')
        pprint(app.config)
    else:
        logging.info(":::__init__.py::: TESTING")
        from dotenv import load_dotenv
        import os

        BASEDIR = os.path.abspath(os.path.dirname(__file__))
        load_dotenv(os.path.join(BASEDIR, '.env_test'))
        app.config.from_object('config.TestConfig')

        app.config.update(
            BCRYPT_LOG_ROUNDS=4,
            HASH_ROUNDS=1,
            LOGIN_DISABLED=True,
        )

    logging.info(':::__init__.py::: Starting app')
    db.init_app(app)
    with app.app_context():
        from src.api import tokens
        from src.api import users
        from src.api import health_check

        if not test_config:
            logging.info(':::__init__.py::: Creating database')
            db.create_all()
            logging.info(':::__init__.py::: Database created')
        return app