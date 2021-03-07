from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from app import login



class User( UserMixin ,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), index = True, unique = True)
    email = db.Column(db.String(150), index = True, unique =True)
    password_hash = db.Column(db.String(150))
    pitches = db.relationship('Pitches', backref='author', lazy='dynamic')


    def __repr__(self):

        return 'User {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):

        return check_password_hash(self.password_hash, password)

class Pitches(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))