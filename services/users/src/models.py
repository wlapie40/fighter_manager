import base64
import os
import uuid
from datetime import datetime, timedelta
from flask import current_app as app
from flask import url_for
from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.postgresql import UUID
from src.logger import logger
from time import time
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from . import db

ma = Marshmallow(app)


class User(UserMixin, db.Model):
    """User account model."""

    __table_args__ = {'schema': f'{os.environ.get("USER_SCHEMA", None)}'}
    __tablename__ = 'user'

    id = db.Column(db.Integer,
                           primary_key=True)
    alternative_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    account_activated = db.Column(db.Boolean, default=False, nullable=False)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def __init__(self, email, password, username):
        self.email = email
        self.username = username
        self.password_hash = User.set_password(password)
        self.account_activated = False
        self.created_on = datetime.now()
        self.last_login = datetime.now()

    # def to_dict(self, include_email=False):
    #     data = {
    #         'id': self.id,
    #         'alternative_id': self.alternative_id,
    #         'account_activated': self.account_activated,
    #         'last_login': self.last_login,
    #         'created_on': self.created_on,
    #         '_links': {
    #         }
    #     }
    #     if include_email:
    #         data['email'] = self.email
    #     return data

    @staticmethod
    def set_alternative_id():
        """Generate UUID4 code as an """
        return uuid.uuid4()

    @staticmethod
    def set_password(password):
        """Create hashed password."""
        return generate_password_hash(password, method='sha256', salt_length=9)

    @logger
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_user_by_id(cls, id: int):
        return db.session.query(cls).\
                filter(cls.id == id).first()

    def get_token(self, expires_in=3600):
        now = datetime.now()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.now() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.now():
            return None
        return user

    def __repr__(self):
        return '<User {}>'.format(self.username)


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "alternative_id", "email", "account_activated", "created_on")

    # # Smart hyperlinking
    # _links = ma.Hyperlinks(
    #     {"self": ma.URLFor("add_user", id="<id>"), "collection": ma.URLFor("users")}
    # )


user_schema = UserSchema()
users_schema = UserSchema(many=True)
