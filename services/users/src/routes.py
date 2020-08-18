import logging
from .logger import logger
from flask import current_app as app
from flask import request, jsonify
from .models import db, User

@logger
@app.route('/users/healthcheck', methods=['GET'])
def healthcheck():
    return {"code": "200",
            "msg": "Hello from users"}


@logger
@app.route('/users/user', methods=['POST'])
def add_user():
    logging.info('auth :: add_user :: get called')
    content = request.json
    logging.info(f'TEST :: CONTENT :: {content}')

    user = User.query.filter_by(email=content['email']).first()
    if not user:
        user = User(
            email=content['email'],
            password=content['password'])
        db.session.add(user)
        db.session.commit()
        logging.info(f'auth :: add_user :: user: {content["email"]} added')
    else:
        return {"code": "409",
            "msg": f"Conflict.Email: {user.email} exists"}

    return {"code": "201",
            "msg": f"New user_id:{user.id} added"}