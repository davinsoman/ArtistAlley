"""This file holds database models"""
from .. import db
from flask_login import UserMixin

class Note(db.Model):
    """This is the Note model for the database"""
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    """This is the User model for the database"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    """We are able to see all notes associated with a user by using this many to one relationship"""
    notes = db.relationship('Note')
    posts = db.relationship('Post')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    image = db.Column(db.String(10000))
    description = db.Column(db.String(300))
    likes = db.Column(db.Integer)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
