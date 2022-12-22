import os
import click

from app.seed_db import dummy_data


def register(app):
    @app.cli.command()
    def seed_db():
        click.echo('Seeding the database...')
        dummy_data()
        click.echo('Done!')
