# coding: utf-8
from models import BaseModel, db

__author__ = 'Jux.Liu'

class Store(db.Model, BaseModel):
    __tablename__ = 'store'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(40), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    typeid = db.Column(db.Integer, nullable=False)
