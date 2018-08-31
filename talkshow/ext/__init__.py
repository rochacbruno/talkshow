from werkzeug.utils import import_string
from dynaconf import FlaskDynaconf


def configure(app):
    """Initialize all extensios of APP
    :param app: Instance of flask application
    """
    # first start dynaconf to get access to variables
    # defined in settings.toml
    FlaskDynaconf(app)

    # then start all the extensions defined
    for ext in app.config.get('EXTENSIONS', []):
        mod = import_string(ext)
        app.logger.debug(f"initialing extension {mod}")
        mod.configure(app)
