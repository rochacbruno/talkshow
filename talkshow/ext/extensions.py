from werkzeug.utils import import_string


def configure(app):
    """Initialize all extensios of APP
    :param app: Instance of flask application

    """
    for ext in app.config.get('EXTENSIONS'):
        mod = import_string(ext)
        mod.configure(app)
