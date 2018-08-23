from flask import Flask
from talkshow.ext import db
from talkshow.ext import cli
from talkshow.ext import bootstrap
from talkshow.ext import admin
from talkshow.ext import apidocs
from talkshow.ext import login
from talkshow.blueprints import webui
from talkshow.blueprints import restapi


def create_app():
    """Creates a new Flask app"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    # extensions
    db.configure(app)  # <-- `app` passado para o db factory
    cli.configure(app)  # <-- `app` passado para o cli factory
    bootstrap.configure(app)  # <-- `app` passado para o bootstrap factory
    admin.configure(app)  # <-- `app` passado para o admin factory
    apidocs.configure(app)  # <-- `app` passado para o apidocs factory
    login.configure(app)  # <-- `app` passado para o login factory
    # blueprints
    webui.configure(app)  # <-- registro do webui
    restapi.configure(app)  # <-- registro do restapi
    return app
