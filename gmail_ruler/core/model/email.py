# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Initializing the base object.
Base = declarative_base()

class Email(Base):
  __tablename__ = "emails"

  id = Column(Integer, primary_key=True, autoincrement=True)
  message_id = Column(String, unique=True)
  from_email = Column(String) 
  to_email = Column(String)
  subject = Column(Text)
  content = Column(Text)
  received_at = Column(DateTime)

  def __repr__(self):
    # Easy way to understand when trying to use verbose on the email instances.
    return "{0}: {1}".format(self.message_id, self.subject)