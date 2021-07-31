"""Init.py"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_URI



db = SQLAlchemy()


def init_app():
    """Contructing core application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    db.init_app(app)
    with app.app_context():
        db.create_all()

        from main import routes, models
        return app
