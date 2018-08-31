from flask import Flask
from talkshow import blueprints, ext


def create_app():
    """Creates a new Flask app using the Factory Pattern"""
    app = Flask(__name__)
    # extensions
    ext.configure(app)  # <-- registro dinâmico das extensões
    # blueprints
    blueprints.configure(app)  # <-- registro dinâmico dos blueprints
    return app
