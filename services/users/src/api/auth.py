import logging
from src import basic_auth, token_auth
from src.api.errors import error_response
from src.models import User


@basic_auth.verify_password
def verify_password(username, password):
    logging.info('users :: verify_password :: get called')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user


@basic_auth.error_handler
def basic_auth_error(status):
    logging.info('users :: basic_auth_error :: get called')
    return error_response(status)


@token_auth.verify_token
def verify_token(token):
    logging.info('users :: verify_token :: get called')
    return User.check_token(token) if token else None


@token_auth.error_handler
def token_auth_error(status):
    logging.info('users :: token_auth_error :: get called')
    return error_response(status)
