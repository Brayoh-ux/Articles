from flask_sqlalchemy import SQLAlchemy



class Config:
    
SECRET_KEY= 'fc6dadcdbce0027894bdb79de2347804'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaaccess:8900@localhost/blogger'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass