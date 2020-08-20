import datetime
import os
import uuid
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

from . import db


class User(UserMixin, db.Model):
    """User account model."""

    __table_args__ = {'schema': f'{os.environ.get("USER_SCHEMA", None)}'}
    __tablename__ = 'user'

    id = db.Column(db.Integer,
                           primary_key=True)
    alternative_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
    email = db.Column(db.String(40),
                           unique=True,
                           nullable=False)
    password = db.Column(db.String(200),
                           primary_key=False,
                           unique=False,
                           nullable=False)
    account_activated = db.Column(db.Boolean,
                           default=False,
                           nullable=False)
    created_on = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)
    last_login = db.Column(db.DateTime,
                           index=False,
                           unique=False,
                           nullable=True)

    def __init__(self, email, password):
        self.email = email
        self.password = User.set_password(password)
        self.account_activated = False
        self.created_on = datetime.datetime.now()
        self.last_login = datetime.datetime.now()

    @staticmethod
    def set_alternative_id():
        """Generate UUID4 code as an """
        return uuid.uuid4()

    @staticmethod
    def set_password(password):
        """Create hashed password."""
        return generate_password_hash(password, method='sha256', salt_length=9)

    @staticmethod
    def check_password(password):
        """Check hashed password."""
        return check_password_hash(password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
