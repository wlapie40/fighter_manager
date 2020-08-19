import logging

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Globally accessible libraries
db = SQLAlchemy()


def create_app(test_config=False):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    if not test_config:
        app.config.from_object('config.Config')
    else:
        from dotenv import load_dotenv
        load_dotenv()
        logging.info(":::__init__.py::: TESTING")
        app.config.from_object('config.TestConfig')
        app.config.update(
            BCRYPT_LOG_ROUNDS=4,
            HASH_ROUNDS=1,
            LOGIN_DISABLED=True,
        )

    logging.info(':::__init__.py::: Starting app')
    db.init_app(app)
    with app.app_context():
        from . import routes
        # logging.info(':::__init__.py::: Creating database')
        # db.create_all()
        # logging.info(':::__init__.py::: Database created')
        return app