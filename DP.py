# coding: utf-8

from flask import Flask
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_script import Server
from flask_script import Shell

from models import db
from models.comment import CinemaEnvironment
from models.comment import CinemaOther
from models.comment import CinemaQuality
from models.comment import CinemaService
from models.comment import Comment
from models.comment import RestaurantEnvironment
from models.comment import RestaurantOther
from models.comment import RestaurantQuality
from models.comment import RestaurantService
from models.role import Role
from models.store import Store
from models.user import User


__author__ = 'Jux.Liu'

app = Flask(__name__)
manager = Manager(app)


def configure_app(configure_name='default'):
    db.init_app(app=app)

    from config import config
    app.config.from_object(config[configure_name])
    config[configure_name].init_app(app=app)


def configured_app():
    configure_app('production')
    return app


def configure_logger():
    pass


@manager.command
def rebuild_db():
    db.drop_all()
    db.create_all()
    print('rebuild database')


@manager.command
def server():
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,
    )
    app.run(**config)


def configure_manager():
    Migrate(app, db)
    manager.add_command('db', MigrateCommand)
    context = {
        'app': app,
        'db': db,
        'User': User,
        'Role': Role,
        'Store': Store,
        'CinemaService': CinemaService,
        'CinemaQuality': CinemaQuality,
        'CinemaEnvironment': CinemaEnvironment,
        'CinemaOther': CinemaOther,
        'Comment': Comment,
        'RestaurantService': RestaurantService,
        'RestaurantQuality': RestaurantQuality,
        'RestaurantEnvironment': RestaurantEnvironment,
        'RestaurantOther': RestaurantOther,
    }
    cmd = Shell(
        use_bpython=True,
        make_context=lambda: context
    )
    manager.add_command('shell', cmd)
    cmd = Server(
        host='0.0.0.0',
        port=3000,
        use_debugger=True,
        use_reloader=True
    )
    manager.add_command('runserver', cmd)


if __name__ == '__main__':
    configure_manager()
    configure_app()
    manager.run()
