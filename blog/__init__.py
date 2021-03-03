from flask import Flask
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnsjddh4ckmvttl6pvcllxty6add'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringaaccess:5693@localhost/myblog'

db = SQLAlchemy(app)

db.init_app(app)

from blog import routes

