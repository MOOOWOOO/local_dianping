# coding: utf-8
from models import BaseModel, db

__author__ = 'Jux.Liu'


class Role(db.Model, BaseModel):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    name = db.Column(db.String(20), nullable=False)

class UserRole(db.Model, BaseModel):
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
