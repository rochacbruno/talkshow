from pymongo import MongoClient
from tinymongo import TinyMongoClient
from tinymongo.serializers import DateTimeSerializer
from tinydb_serialization import SerializationMiddleware


class CustomClient(TinyMongoClient):
    @property
    def _storage(self):
        serialization = SerializationMiddleware()
        serialization.register_serializer(DateTimeSerializer(), 'TinyDate')

        # register other custom serializers
        return serialization


def configure(app):
    """Creates a new database connection"""

    if app.env == "production":
        client = MongoClient(host="localhost")
    else:
        client = CustomClient('database')

    db_name = app.config.get('MONGODB_NAME', 'db')
    app.db = client[db_name]
