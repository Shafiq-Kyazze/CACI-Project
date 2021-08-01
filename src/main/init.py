"""Init.py"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI,secret_key
from flask_login import LoginManager
from flask_jwt_extended import JWTManager



db = SQLAlchemy()
login = LoginManager()
jwt =JWTManager()


def init_app():
    """Contructing core application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['JWT_SECRET_KEY'] = secret_key
    db.init_app(app)
    login.init_app(app)
    jwt.init_app(app)
    with app.app_context():
        db.create_all()

        from main import routes, models
        from main.utils import errors
        return app
