from flask_debugtoolbar import DebugToolbarExtension


def configure(app):
    """ Instancia a Debug Tool Bar para a aplicação Flask

    :param app: Aplicação Flask que será instanciada
    """

    if app.config.get('DEBUG_TOOLBAR_ENABLED'):
        DebugToolbarExtension(app)
