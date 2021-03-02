from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnsjddh4ckmvttl6pvcllxty6'

def create_app(config_name):
    db.init_app(app)
    

from blog import routes