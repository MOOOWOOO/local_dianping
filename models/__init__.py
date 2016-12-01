# coding: utf-8

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import sql

__author__ = 'Jux.Liu'

db = SQLAlchemy()
sql = sql


class BaseModel(object):
    def black_list(self):
        b = []
        return b

    def json(self):
        _dict = self.__dict__.copy()
        d = {k: v for k, v in _dict.items() if k not in self.black_list()}
        return d

    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{0} = {1}'.format(k, v) for k, v in self.__dict__.items())
        return '<{0}: \n  {1}\n>'.format(class_name, '\n  '.join(properties))

    @staticmethod
    def exists(**kwargs):
        return db.session.query(db.exists().where(kwargs)).scalar()

    def save(self):
        """Saves the object to the database."""
        db.session.add(self)
        try:
            db.session.commit()
            return self
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self, soft=True):
        if soft:
            if not hasattr(self, 'deleted'):
                raise AttributeError('%s dose not have "deleted" column, cannot perform soft deleting')
            self.deleted = True
            db.session.add(self)
        else:
            db.session.delete(self)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
