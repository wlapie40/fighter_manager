import logging
from flask import current_app as app
from flask import request, jsonify
from src.api.auth import basic_auth, token_auth
from src.models import db


@app.route('/users/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    logging.info('users :: get_token :: get called')
    token = basic_auth.current_user().get_token()
    db.session.commit()
    logging.info('users :: get_token :: token created')
    return jsonify({'token': token})


@app.route('/users/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204
