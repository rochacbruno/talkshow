from flask import Blueprint

from .admin import AdminProposal
from .views import index, event

bp_webui = Blueprint("webui", __name__)


def configure(app):
    """Register the Blueprint to the app"""

    # Register URL rules using declarative instead of decorator
    bp_webui.add_url_rule('/', view_func=index)
    bp_webui.add_url_rule(
        '/<event_id>/', methods=['GET', 'POST'], view_func=event
    )

    # register blueprint
    app.register_blueprint(bp_webui)

    # register admin views
    app.admin.add_view(AdminProposal(app.db['proposal'], 'Proposals'))
