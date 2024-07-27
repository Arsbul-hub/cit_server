from sqlalchemy_serializer import SerializerMixin

from app import db, db_session
from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash

import sqlalchemy as sa

__basemodel = db.Model


class Account(UserMixin, __basemodel):
    __tablename__ = 'accounts'
    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(), index=True, unique=True)
    password_hash = sa.Column(sa.String(128))
    timestamp = sa.Column(sa.DateTime, index=True, default=datetime.utcnow)

    #account_data = db.relationship('AccountData', backref='Account', uselist=False)

    def __repr__(self):
        return 'Пользователь {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class AccountData(__basemodel, SerializerMixin):
    __tablename__ = 'accounts_data'
    serialize_only = ('fio', 'phone', 'date')
    id = sa.Column(sa.Integer, primary_key=True)
    fio = sa.Column(sa.String)
    phone = sa.Column(sa.String)
    date = sa.Column(sa.String)

    account_id = sa.Column(sa.Integer, db.ForeignKey('accounts_data.id'))
