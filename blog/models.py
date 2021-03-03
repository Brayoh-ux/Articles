from datetime import datetime
from .import db


# stroring data in db

class User(db.Model):
    '''user model'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True)
    # email = db.Column(db.String(120), unique = True)
    # image_file = db.Column(db.String(20), default = 'default.jpeg')
    # password = db.Column(db.String(60))
    # posts = db.relationship('Post', backref = 'author', lazy = True) #get the user

    def __repr__(self):
        return f'User {self.username}'

