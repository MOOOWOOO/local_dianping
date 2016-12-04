# coding: utf-8
from flask import request

from models.user import User
from utils.decorators import admin_required, login_required
from . import api, json_response

__author__ = 'Jux.Liu'


@api.route('/user/add', methods=['POST'])
@admin_required
def user_add():
    pass


@api.route('/user/delete/<int:user_id>')
@admin_required
def user_delete(user_id):
    pass


@api.route('/user/update/<int:user_id>')
@login_required
def user_update(user_id):
    pass


@api.route('/register', methods=['POST'])
def user_register():
    form = request.get_json()
    user = User(form)
    user.save()
    return json_response(True)
