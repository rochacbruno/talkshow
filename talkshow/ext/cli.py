import click
from talkshow.ext.login import create_user
from talkshow.utils import slugify


def configure(app):
    """Attach new commands to app"""

    @app.cli.command()
    @click.option('--name', '-n', required=True)
    @click.option('--date', '-d', required=True)
    def addevent(name, date):
        """Creates a new event entry"""

        # Generate a slug from a event name
        slug = slugify(name)

        app.db['events'].insert_one({'name': name, 'date': date,
                                     'slug': slug})
        click.echo(f"{slug} cadastrado com sucesso!")

    @app.cli.command()
    @click.option('--username', '-u', required=True)
    @click.option('--password', '-p', required=True)
    def adduser(username, password):
        """Creates a new admin user"""
        user = create_user(username, password)
        click.echo(f"{user.inserted_id} cadastrado com sucesso!")
