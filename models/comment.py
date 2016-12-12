# coding: utf-8
from models import BaseModel, db
from utils.time_funcs import utctime

__author__ = 'Jux.Liu'


class Comment(db.Model, BaseModel):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Float)
    created_time = db.Column(db.Integer, default=utctime())
    updated_time = db.Column(db.Integer, default=utctime())
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
    deleted = db.Column(db.Boolean, default=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    check_ticket_time = db.Column(db.Integer, default=15)
    glass_3d_type = db.Column(db.Integer, default=0)
    snack_star = db.Column(db.Integer, default=0)
    snack_comment = db.Column(db.Text, default='')
    ads = db.Column(db.Integer, default=0)
    staff_star = db.Column(db.Integer, default=0)
    staff_comment = db.Column(db.Text, default='')


class CinemaQuality(db.Model, BaseModel):
    __tablename__ = 'cinema_quality'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    sound_star = db.Column(db.Integer, default=0)
    movie_name = db.Column(db.String(30), default='')
    video_star = db.Column(db.Integer, default=0)
    video_comment = db.Column(db.Text, default='')


class CinemaEnvironment(db.Model, BaseModel):
    __tablename__ = 'cinema_environment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    ticket_machine = db.Column(db.Boolean, default=True)
    reset_seat = db.Column(db.Boolean, default=True)
    reset_seat_star = db.Column(db.Integer, default=0)
    hall_light_star = db.Column(db.Integer, default=0)
    room_light_star = db.Column(db.Integer, default=0)
    room_number = db.Column(db.String(4), default='')
    screen_size_star = db.Column(db.Integer, default=0)
    this_seat = db.Column(db.Float, default=0.0)
    best_seat = db.Column(db.Float, default=0.0)
    seat_comfort_star = db.Column(db.Integer, default=0)
    smells_star = db.Column(db.Integer, default=0)


class CinemaOther(db.Model, BaseModel):
    __tablename__ = 'cinema_other'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    toilet_clean_star = db.Column(db.Integer, default=0)
    toilet_paper = db.Column(db.Boolean, default=False)
    traffic_star = db.Column(db.Integer, default=0)
    restaurant = db.Column(db.Boolean, default=False)


class RestaurantService(db.Model, BaseModel):
    __tablename__ = 'restaurant_service'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    pickup = db.Column(db.Boolean, default=False)
    snack_star = db.Column(db.Integer, default=0)
    line_number = db.Column(db.Integer, default=0)
    waiting_time = db.Column(db.Integer, default=0)
    menu_type = db.Column(db.Integer, default=0)
    staff_star = db.Column(db.Integer, default=0)
    staff_comment = db.Column(db.String, default='')
    speed = db.Column(db.Integer, default=0)


class RestaurantQuality(db.Model, BaseModel):
    __tablename__ = 'restaurant_quality'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    relish = db.Column(db.Integer, default=0)
    looks_star = db.Column(db.Integer, default=0)
    smells_star = db.Column(db.Integer, default=0)
    taste_star = db.Column(db.Integer, default=0)
    temperature_star = db.Column(db.Integer, default=0)


class RestaurantEnvironment(db.Model, BaseModel):
    __tablename__ = 'restaurant_environment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    noise_star = db.Column(db.Integer, default=0)
    size = db.Column(db.Integer, default=0)
    light_star = db.Column(db.Integer, default=0)
    table_star = db.Column(db.Integer, default=0)
    floor_clean_star = db.Column(db.Integer, default=0)
    wall_clean_star = db.Column(db.Integer, default=0)
    smell_star = db.Column(db.Integer, default=0)
    bug = db.Column(db.Boolean, default=False)
    cutlery_clean_star = db.Column(db.Integer, default=0)


class RestaurantOther(db.Model, BaseModel):
    __tablename__ = 'restaurant_other'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    napkin_star = db.Column(db.Integer, default=0)
    discount = db.Column(db.Integer, default=10)
    group_buy = db.Column(db.Integer, default=0)
    traffic_star = db.Column(db.Integer, default=0)
