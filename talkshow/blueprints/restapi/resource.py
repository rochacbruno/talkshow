from datetime import datetime
from flask import current_app as app
from flask_restful import reqparse, Resource
from flask_simplelogin import login_required
from slugify import slugify

event_post_parser = reqparse.RequestParser()
event_post_parser.add_argument('name', required=True)
event_post_parser.add_argument('date', required=True)


class Event(Resource):
    def get(self):
        return {'events': list(app.db['events'].find())}

    @login_required(basic=True)
    def post(self):
        """
        Creates new event
        ---
        parameters:
          - in: body
            name: body
            schema:
              id: Event
              properties:
                name:
                  type: string
                date:
                  type: string
        responses:
          201:
            description: Success or failure message
            schema:
              properties:
                event_created:
                  type: string
                  description: The id of the created event
        """
        event = event_post_parser.parse_args()
        slug = slugify(event.name, to_lower=True)
        event_db = app.db['events'].find_one({'slug': slug})
        if event_db:
            return {'event_duplicate': event_db['_id']}, 409

        new = app.db['events'].insert({
          'name': event.name,
          'slug': slug,
          'date': datetime.strptime(event.date, '%Y-%m-%d')})
        return {'event_created': new.inserted_id}, 201


proposal_post_parser = reqparse.RequestParser()
proposal_post_parser.add_argument('name', required=True)
proposal_post_parser.add_argument('email', required=True)
proposal_post_parser.add_argument('title', required=True)
proposal_post_parser.add_argument('description', required=True)


class EventItem(Resource):
    def get(self, event_id):
        event = app.db['events'].find_one({'_id': event_id})
        proposals = app.db['proposal'].find({'event_id': event_id})
        return {'event': event, 'proposals': list(proposals)}

    def post(self, event_id):
        event = app.db['events'].find_one({'_id': event_id})
        prop = proposal_post_parser.parse_args()
        new = app.db['proposal'].insert({
            'event_id': event['_id'],
            'name': prop.name,
            'email': prop.email,
            'title': prop.title,
            'description': prop.description,
            'approved': False
        })
        return {'proposal created': new.inserted_id}, 201
