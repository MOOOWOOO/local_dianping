# coding: utf-8
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import url_for

from utils.decorators import current_user

__author__ = 'Jux.Liu'

main = Blueprint('main', __name__)


@main.route('/login')
def login_view():
    user = current_user()
    if user is None:
        return render_template('login.html', current_user=user)
    else:
        return redirect(url_for('.index_view'))


@main.route('/register')
def register_view():
    user = current_user()
    if user is None:
        return render_template('register.html', current_user=user)
    else:
        return redirect(url_for('.index_view'))


@main.route('/')
@main.route('/index')
def index_view():
    user = current_user()
    return render_template('index.html', current_user=user)
