from flask import Blueprint
from flask_restful import Api

from blueprints.restapi.resource import Event, EventItem

bp = Blueprint('restapi', __name__, url_prefix='/api/v1')
api = Api(bp)


def configure(app):
    """Initialize API and register blueprint"""
    api.add_resource(Event, '/event/')
    api.add_resource(EventItem, '/event/<event_id>')

    app.register_blueprint(bp)
