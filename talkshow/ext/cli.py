import click
from datetime import datetime
from talkshow.ext.login import create_user
from slugify import slugify


def configure(app):
    """Attach new commands to app"""

    @app.cli.command()
    @click.option('--name', '-n', required=True)
    @click.option('--date', '-d', required=True)
    def addevent(name, date):
        """Creates a new event entry"""
        slug = slugify(name, to_lower=True)
        event = app.db['events'].find_one({'slug': slug})
        if event:
            click.echo(f"{event.inserted_id} evento já existe com esse nome!")
        else:
            event = app.db['events'].insert_one({
                'name': name,
                'slug': slug,
                'date': datetime.strptime(date, '%Y-%m-%d')})
            click.echo(f"{event.inserted_id} cadastrado com sucesso!")

    @app.cli.command()
    @click.option('--username', '-u', required=True)
    @click.option('--password', '-p', required=True)
    def adduser(username, password):
        """Creates a new admin user"""
        user = create_user(username, password)
        click.echo(f"{user.inserted_id} cadastrado com sucesso!")
