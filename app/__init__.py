from flask import Flask
import os
from app import auth, api
from app.database import db
from app.extensions import jwt, migrate, celery
from app.config import config

def create_app():
    """Application factory, used to create application
    """
    app = Flask('fim_rate')

    configure_app(app)
    configure_db(app)
    configure_extensions(app)
    register_blueprints(app)
    init_celery(app)

    return app


def configure_app(app):
    """set configuration for application
    """
    # default configuration
    current_env = os.environ.get('FLASK_ENV') or 'default'
    app.config.from_object(config[current_env])


def configure_db(app):
    """configure flask db and migrate
    """
    db.init_app(app)
    migrate.init_app(app, db)


def configure_extensions(app):
    """configure flask extensions
    """
    jwt.init_app(app)


def register_blueprints(app):
    """register all blueprints for application
    """
    app.register_blueprint(auth.views.blueprint)
    app.register_blueprint(api.views.blueprint)


def init_celery(app=None):
    app = app or create_app()
    celery.conf.broker_url = app.config['CELERY_BROKER_URL']
    celery.conf.result_backend = app.config['CELERY_RESULT_BACKEND']
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        """Make celery tasks work with Flask app context"""
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
