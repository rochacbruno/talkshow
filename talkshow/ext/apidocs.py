from flasgger import Flasgger


def configure(app):
    """Starts openapispec"""
    Flasgger(app)
