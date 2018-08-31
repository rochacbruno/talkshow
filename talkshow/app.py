from flask import Flask

from talkshow.blueprints import blueprints
from talkshow.ext import configuration, extensions


def create_app():
    """Creates a new Flask app"""
    app = Flask(__name__)
    configuration.configure(app)  # <-- registro dinâmico das extensões

    # extensions
    extensions.configure(app)

    # blueprints
    blueprints.configure(app)  # <-- registro dinâmico dos blueprints

    return app
