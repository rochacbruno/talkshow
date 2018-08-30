from flask import Blueprint

from talkshow.blueprints.webui.admin import AdminProposal

bp_webui = Blueprint("webui", __name__)


def configure(app):
    """Register the Blueprint to the app"""
    app.register_blueprint(bp_webui)
    app.admin.add_view(AdminProposal(app.db['proposal'], 'Proposals'))
