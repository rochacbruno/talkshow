from werkzeug.utils import import_string


def configure(app):
    """Initialize all blueprints of APP
    :param app: Instance of flask application

    """
    for bp in app.config.get('BLUEPRINTS'):
        mod = import_string(bp)
        mod.configure(app)
