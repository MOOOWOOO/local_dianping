# coding: utf-8
from flask import Blueprint, jsonify

__author__ = 'Jux.Liu'

api = Blueprint('api', __name__)


def json_response(success, data=None, message=''):
    return jsonify({'success': success, 'data':data, 'message': message})


from . import user
from . import comment
from . import store
