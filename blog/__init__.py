from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnsjddh4ckmvttl6pvcllxty6add'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tuwdmxxnafbflg:d59552a7759b49ceb405196eff30c56ad47c34ef0762bd64f0a56174ab9f7922@ec2-18-211-97-89.compute-1.amazonaws.com:5432/def9bqfmrk6r4u'
db = SQLAlchemy(app)

from blog import routes

