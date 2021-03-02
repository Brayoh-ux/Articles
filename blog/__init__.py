from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnsjddh4ckmvttl6pvcllxty6add'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


def create_app(config_name):
    db.init_app(app)
    

from blog import routes