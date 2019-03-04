# -*- coding: utf-8 -*-

"""
This module has the basic methods in DB controls.
Currently, it supports only the schema creation and the email model creation.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.model.email import *
from core import config

class Database():
  def __init__(self):
    self.engine = create_engine(config.DB_URI, echo=False)
    Session = sessionmaker(bind=self.engine)
    self.session = Session()

  def create_schema(self):
    # To initialize the schema if not present.
    Base.metadata.create_all(bind=self.engine)

  def create_email(self, kwargs):
    # This takes in the keyworded arguments and creates the email in the database
    email = Email(**kwargs)
    self.session.add(email)
    self.session.commit()
