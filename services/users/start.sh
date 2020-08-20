#!/bin/bash
export FLASK_ENV=development
export FLASK_DEBUG=1
export FLASK_APP=wsgi.py
export FLASK_PORT=5000
export FLASK_TESTING=False
export SECRET_KEY=superstrongsecret
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://coco_butter_user:superstrongpassword@192.28.1.2:5432/cocoa_butter_dev
export SQLALCHEMY_ECHO=False
export SQLALCHEMY_TRACK_MODIFICATIONS=False
export USER_SCHEMA=local_cocoa_butter_users

#python3 -m wsgi.py
#flask run
gunicorn --config gunicorn-cfg.py wsgi:app