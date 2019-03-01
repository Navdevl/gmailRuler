import click
from server import app
from core import Synchronizer

@click.group()
def main():
  pass

@main.command()
def initialize():
  click.echo('Initialized the database')
  synchronizer = Synchronizer()
  synchronizer.sync_emails()

@main.command()
def server():
  click.echo('Starting the server')
  app.run()

if __name__ == '__main__':
  main()
