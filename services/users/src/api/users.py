import logging
from flask import current_app as app
from flask import request, jsonify, abort

from src.models import db, User, user_schema, users_schema
from src.api.errors import bad_request, error_response
from src.api.responses import response
from src import token_auth


@app.route('/users', methods=['POST'])
def add_user():
    logging.info('users :: add_user :: get called')
    content = request.json
    if 'email' not in content or 'password' not in content or 'username' not in content:
        return bad_request('must include email, password and username fields')
    if User.query.filter_by(username=content['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=content['email']).first():
        return bad_request('please use a different e-mail')
    user = User(
        email=content['email'],
        password=content['password'],
        username=content['username'])
    db.session.add(user)
    db.session.commit()
    logging.info(f'auth :: add_user :: user: {content["email"]} added')
    return user_schema.jsonify(user)


@app.route('/users/<user_id>', methods=['GET'])
@token_auth.login_required
def get_user(user_id):
    logging.info('users :: get_user :: get called')

    if int(token_auth.current_user().id) != int(user_id):
        abort(403)

    user = User.get_user_by_id(id=user_id)
    if user:
        return user_schema.jsonify(user)
    return jsonify({"status_code": 204, "message": f"user_id {user_id} does not exists"})


@app.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    logging.info('users :: get_users :: get called')

    users = User.query.all()
    if users:
      result = users_schema.dump(users)
      return jsonify(result)
    else:
      return jsonify({"status_code": 204, "message": f"There are no users"})


@app.route('/users/<user_id>', methods=['DELETE'])
@token_auth.login_required
def delete_user(user_id):
    logging.info('users :: delete_user :: get called')

    if int(token_auth.current_user().id) != int(user_id):
        abort(403)

    user = User.get_user_by_id(id=user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return user_schema.jsonify(user)
    else:
        return jsonify({"status_code": 204, "message": f"user_id {user_id} does not exists"})


# @app.route('/users/<user_id>', methods=['PUT'])
# def update_user(user_id):
#     logging.info('users :: update_user :: get called')
#    if token_auth.current_user().id != user_id:
#         abort(403)
#     content = request.json
#     user = User.get_user_by_id(id=user_id)
#     if not user:
#         return bad_request('user not found')
#     data = users_schema.dump(users)
#     if 'email' in content and content['email'] != user.email and \
#             User.query.filter_by(email=content['email']).first():
#         return bad_request('please use a different email address')
#     user.email = content['email']
#     # db.session.commit()
#     #
#     #   result = users_schema.dump(users)
#     #   return jsonify(result)
#     # else:
#     #   return jsonify({"status_code": 204, "message": f"There are no users"})
