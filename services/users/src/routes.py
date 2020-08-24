import logging
from flask import current_app as app
from flask import request, jsonify

from .logger import logger
from .models import db, User, user_schema, users_schema


@logger
@app.route('/users/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"code": 200, "msg": "OK"})


@logger
@app.route('/users/user', methods=['POST'])
def add_user():
    logging.info('auth :: add_user :: get called')
    content = request.json
    try:
        user = User.query.filter_by(email=content['email']).first()
        if not user:
            user = User(
                email=content['email'],
                password=content['password'])
            db.session.add(user)
            db.session.commit()
            logging.info(f'auth :: add_user :: user: {content["email"]} added')
        else:
            return {"code": 409, "msg": f"Conflict.Email: {user.email} exists"}

        return user_schema.jsonify(user)
    except KeyError as e:
        return jsonify({"code": 404, "msg": f"KeyError: key {e} not found"})


@logger
@app.route('/users/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_user_by_id(id=user_id)
    if user:
        return user_schema.jsonify(user)
    return jsonify({"code": 204, "msg": f"user_id {user_id} does not exists"})


@logger
@app.route('/users/user', methods=['GET'])
def get_users():
  users = User.query.all()
  if users:
      result = users_schema.dump(users)
      return jsonify(result)
  else:
      return jsonify({"code": 204,
              "msg": f"There are no users"})


@logger
@app.route('/users/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get_user_by_id(id=user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return user_schema.jsonify(user)
    else:
        return jsonify({"code": 204, "msg": f"user_id {user_id} does not exists"})

