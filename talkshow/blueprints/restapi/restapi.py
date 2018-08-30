from flask import Blueprint
from flask_restful import Api

from talkshow.blueprints.restapi.resource import Event, EventItem

bp_restapi = Blueprint('restapi', __name__, url_prefix='/api/v1')
api = Api(bp_restapi)


def configure(app):
    """Initialize API and register blueprint"""
    api.add_resource(Event, '/event/')
    api.add_resource(EventItem, '/event/<event_id>')

    app.register_blueprint(bp_restapi)
