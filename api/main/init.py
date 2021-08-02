"""Init.py"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI


db = SQLAlchemy() #SQLAlchemy instance


def init_app():
    """Contructing core application"""
    app = Flask(__name__)  #Creating an instance of Flask class
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI #configuring daatbase to URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app) #Initialise SQLAlchemy to flask app
    with app.app_context():

        from main import routes, models
        from main.utils import errors
        return app
