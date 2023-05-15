import os
import click


def register(app):
    @app.cli.command()
    def seed_db():
        pass
