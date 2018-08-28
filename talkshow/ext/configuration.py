from dynaconf import FlaskDynaconf


def configure(app):
    """ Initialize Dynaconf Extension
    :param app: Instance of flask application
    """
    FlaskDynaconf(app)
