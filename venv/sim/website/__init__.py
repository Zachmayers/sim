import os
from os import path


def create_app(config_file='settings.py'):
    from flask import Flask
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'asdlkjasdlkjasldkjasldkjasdlkj'

    from .views import views


    app.register_blueprint(views, url_prefix='/')


    return app
