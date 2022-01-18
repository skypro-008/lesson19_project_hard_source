from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_by_name[config_name])
    app.config.from_pyfile('local_config.py')
    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    from .api import blueprint as api
    app.register_blueprint(api)
