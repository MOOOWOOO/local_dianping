# coding: utf-8
from . import api
from ..utils.decorators import admin_required, login_required

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
