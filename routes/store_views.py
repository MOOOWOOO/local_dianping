# coding: utf-8
from flask import Blueprint

__author__ = 'Jux.Liu'

store = Blueprint('store', __name__)


@store.route('/store/list/<int:page>')
def store_list_view(page):
    pass


@store.route('/store/detail/<int:store_id>')
def store_detail_view(store_id):
    pass


@store.route('/comment/list/<int:store_id>')
def store_comment_view(store_id):
    pass


# @store.route('/comment/')
