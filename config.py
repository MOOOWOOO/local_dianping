# coding: utf-8
from datetime import timedelta
from os import getenv

from blueprint import register_blueprint

__author__ = 'Jux.Liu'


class Config(object):
    SECRET_KEY = getenv('MY_DIANPING_KEY') or 'DianpingKeey'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    WTF_CSRF_ENABLED = True
    WTF_CSRF_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

    DBUSER = 'postgres'
    DBPWD = 'postgres'
    DBHOST = 'localhost'
    DBNAME = 'my_dianping'
    DBPORT = 5432

    REMEMBER_COOKIE_DURATION = timedelta(30)

    @staticmethod
    def init_app(app):
        register_blueprint(app)



uri_str = '{protocol}://{username}:{password}@{host}:{port}/{database}'

SQLALCHEMY_DATABASE_URI = uri_str.format(
    protocol='postgresql',
    username=Config.DBUSER,
    password=Config.DBUSER,
    host=Config.DBHOST,
    port=Config.DBPORT,
    database=Config.DBNAME)


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = getenv('MY_DIANPING_DB_DEV') or SQLALCHEMY_DATABASE_URI


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = getenv('MY_DIANPING_DB_TEST') or SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = True

    SQLALCHEMY_DATABASE_URI = getenv('MY_DIANPING_DB') or SQLALCHEMY_DATABASE_URI


config = {
    'default': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
