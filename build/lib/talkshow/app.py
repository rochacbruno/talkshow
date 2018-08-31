from flask import Flask

from talkshow.blueprints.restapi import restapi
from talkshow.blueprints.webui import webui
from talkshow.ext import admin
from talkshow.ext import apidocs
from talkshow.ext import bootstrap
from talkshow.ext import cli
from talkshow.ext import configuration
from talkshow.ext import db
from talkshow.ext import login


def create_app():
    """Creates a new Flask app"""
    app = Flask(__name__)
    configuration.configure(app)
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
