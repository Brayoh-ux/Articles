from datetime import datetime
from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from app import login
# from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User( UserMixin ,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), index = True, unique = True)
    email = db.Column(db.String(150), index = True, unique =True)
    image_file = db.Column(db.String(30), index = True, default = 'default.jpeg')
    password = db.Column(db.String(60))

    posts = db.relationship('Post', backref='author', lazy='dynamic')


    def __repr__(self):

        return f" User('{ self.username } ', '{ self.email} ', '{ self.image_file } ' )"

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(140))
    content = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default = datetime.utcnow )

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return f" Post('{ self.title } ', '{ self.date_posted} ')"