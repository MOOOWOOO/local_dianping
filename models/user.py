# coding: utf-8
from werkzeug.security import check_password_hash, generate_password_hash

from models import BaseModel, db

__author__ = 'Jux.Liu'


class User(db.Model, BaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passhash = db.Column(db.String(120), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    stores = db.relationship('Store', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    roles = db.relationship('UserRole', backref='user', lazy='dynamic')

    @property
    def password(self):
        return None

    @password.setter
    def password(self, password):
        self.passhash = generate_password_hash(password=password)

    def verify_password(self, password):
        if self.passhash and password:
            return check_password_hash(self.passhash, password)
        else:
            return False

    def __init__(self, form):
        super(User, self).__init__()
        self.email = form.get('email', '')
        self.username = form.get('username', '')
        self.password = form.get('password', '')

    def can(self, permission):
        return permission in self.roles.id

    def is_admin(self):
        return self.can(1)
