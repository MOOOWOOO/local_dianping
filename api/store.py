# coding: utf-8
from utils.decorators import admin_required, login_required
from . import api

__author__ = 'Jux.Liu'


@api.route('/store/delete/<int:store_id>')
@admin_required
def store_delete(store_id):
    pass


@api.route('/store/add', methods=['POST'])
@login_required
def store_add():
    pass


@api.route('/store/update/<int:store_id>', methods=['POST'])
@login_required
def store_update(store_id):
    pass
