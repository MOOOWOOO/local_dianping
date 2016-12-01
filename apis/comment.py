# coding: utf-8
from utils.decorators import login_required
from . import api

__author__ = 'Jux.Liu'


@api.route('/comment/add', methods=['POST'])
@login_required
def comment_add():
    pass


@api.route('/comment/delete/<int:comment_id>')
@login_required
def comment_delete(comment_id):
    pass
