# -*- coding: utf-8 -*-

"""
This module contains the CLI based commands that provides an easy way to
start the server, sync the emails to DB and also can provide a easy plugin 
approach to add more custom commands in future.

python gmail_ruler/cli.py server 
  - This command will start the server

python gmail_ruler/cli.py initialize
 - This command will initialize the db with emails

You can learn more about the commands by doing
python gmail_ruler/cli.py --help

"""

import click
from server import app
from core.synchronizer import Synchronizer

@click.group()
def main():
  pass

@main.command()
@click.option('--all', is_flag=True, help='Enable to sync all your emails.')
def initialize(all):
  click.echo('Initializing the database')
  synchronizer = Synchronizer()
  synchronizer.sync_emails(sync_all=all)
  click.echo('Initialized successfully')

@main.command()
def server():
  click.echo('Starting the server')
  app.run(debug=True)

if __name__ == '__main__':
  main()

