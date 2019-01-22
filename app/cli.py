import os
import click


def register(app):
    @app.cli.group()
    def setup():
        """Prepare database and data"""
        pass


    @setup.command()
    def go():
        """Init application, create database tables 
        and create a new user named admin with password admin 
        """
        from app.database import db
        from app.models import User
        click.echo("create database")
        db.create_all()
        click.echo("done")

        click.echo("create user")
        user = User(
            username='admin',
            email='admin@mail.com',
            password='admin',
            active=True
        )
        db.session.add(user)
        db.session.commit()
        click.echo("created user admin")
