# coding: utf-8
from functools import wraps

import flask
from flask import redirect
from flask import request
from flask import session
from flask import url_for

from models.user import User

__author__ = 'Jux.Liu'


def current_user():
    username = session.get('username', '')
    u = User.query.filter_by(username=username).first()
    return u


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        if current_user() is None:
            return redirect(url_for('main.login_view', next=request.url))
        return f(*args, **kwargs)

    return function


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        u = current_user()  # type: User
        if not u.is_admin():
            flask.abort(404)
        return f(*args, **kwargs)

    return function
