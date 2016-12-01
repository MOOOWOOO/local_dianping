# coding: utf-8
from flask import Blueprint
from flask import render_template

__author__ = 'Jux.Liu'

main = Blueprint('main', __name__)


@main.route('/login')
def login_view():
    return render_template('login.html')


@main.route('/')
@main.route('/index')
def index_view():
    return render_template('index.html')
