# coding: utf-8
from models import BaseModel, db

__author__ = 'Jux.Liu'


class Comment(db.Model, BaseModel):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Float, nullable=False)
    cinema_service = db.relationship('CinemaService', backref='comment', lazy='dynamic')
    cinema_quality = db.relationship('CinemaQuality', backref='comment', lazy='dynamic')
    cinema_environment = db.relationship('CinemaEnvironment', backref='comment', lazy='dynamic')
    cinema_other = db.relationship('CinemaOther', backref='comment', lazy='dynamic')
    restaurant_service = db.relationship('RestaurantService', backref='comment', lazy='dynamic')
    restaurant_quality = db.relationship('RestaurantQuality', backref='comment', lazy='dynamic')
    restaurant_environment = db.relationship('RestaurantEnvironment', backref='comment', lazy='dynamic')
    restaurant_other = db.relationship('RestaurantOther', backref='comment', lazy='dynamic')


class CinemaService(db.Model, BaseModel):
    __tablename__ = 'cinema_service'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    check_ticket_time = db.Column(db.Integer, nullable=False, default=0)
    glass_3d_type = db.Column(db.Integer, nullable=False, default=0)
    snack_star = db.Column(db.Integer, nullable=False, default=5)
    snack_comment = db.Column(db.Text, nullable=True)
    ads = db.Column(db.Integer, nullable=False, default=0)
    staff_star = db.Column(db.Integer, nullable=False, default=0)
    staff_comment = db.Column(db.Text, nullable=True)


class CinemaQuality(db.Model, BaseModel):
    __tablename__ = 'cinema_quality'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    sound_star = db.Column(db.Integer, nullable=False, default=0)
    movie_name = db.Column(db.String(30), nullable=False, default='')
    video_star = db.Column(db.Integer, nullable=False, default=0)
    video_comment = db.Column(db.Text, nullable=True)


class CinemaEnvironment(db.Model, BaseModel):
    __tablename__ = 'cinema_environment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    ticket_machine = db.Column(db.Boolean, nullable=False, default=True)
    reset_seat = db.Column(db.Boolean, nullable=False, default=True)
    hall_light = db.Column(db.Integer, nullable=False, default=0)
    room_light = db.Column(db.Integer, nullable=False, default=0)
    room_number = db.Column(db.String(4), nullable=False, default='')
    screen_size = db.Column(db.Integer, nullable=False, default=0)
    this_seat = db.Column(db.Float, nullable=False, default=0.0)
    best_seat = db.Column(db.Float, nullable=False, default=0.0)
    seat_comfort = db.Column(db.Integer, nullable=False, default=0)
    smells = db.Column(db.Integer, nullable=False, default=3)


class CinemaOther(db.Model, BaseModel):
    __tablename__ = 'cinema_other'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    toilet_clean = db.Column(db.Integer, nullable=True)
    toilet_paper = db.Column(db.Boolean, nullable=True)
    traffic = db.Column(db.Integer, nullable=True)
    restaurant = db.Column(db.Integer, nullable=True)


class RestaurantService(db.Model, BaseModel):
    __tablename__ = 'restaurant_service'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))


class RestaurantQuality(db.Model, BaseModel):
    __tablename__ = 'restaurant_quality'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))


class RestaurantEnvironment(db.Model, BaseModel):
    __tablename__ = 'restaurant_environment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))


class RestaurantOther(db.Model, BaseModel):
    __tablename__ = 'restaurant_other'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
