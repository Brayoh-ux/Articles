from datetime import datetime
from .import db

# stroring data in db

class User(db.Model):
    '''user model'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    usename = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True)
    image_file = db.Column(db.String(20), default = 'default.jpeg')
    password = db.Column(db.String(60))
    posts = db.relationship('Post', backref = 'author', lazy = True) #get the user

    def __repr__(self):
        return f"User('{self.usename}', '{self.email}', '{self.image_file}')"

# class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime, datetime.utcnow)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return (f"Post('{self.title}', '{self.date_posted}')")
