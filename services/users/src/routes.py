import logging
from flask import current_app as app
from flask import request, jsonify

from .logger import logger
from .models import db, User, user_schema


@logger
@app.route('/users/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"code": "200",
            "msg": "Hello from users23"})


@logger
@app.route('/users/user', methods=['POST'])
def add_user():
    logging.info('auth :: add_user :: get called')
    content = request.json

    user = User.query.filter_by(email=content['email']).first()
    if not user:
        user = User(
            email=content['email'],
            password=content['password'])
        db.session.add(user)
        db.session.commit()
        logging.info(f'auth :: add_user :: user: {content["email"]} added')
    else:
        return {"code": 409,
            "msg": f"Conflict.Email: {user.email} exists"}

    return {"code": 201,
            "msg": f"New user_id:{user.id} added"}

