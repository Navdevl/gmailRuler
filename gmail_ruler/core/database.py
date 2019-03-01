from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.model.email import *

class Database():
  def __init__(self):
    self.engine = create_engine('sqlite:///emails.db', echo=True)
    Session = sessionmaker(bind=self.engine)
    self.session = Session()

  def create_schema(self):
    Base.metadata.create_all(bind=self.engine)

  def create_email(self, kwargs):
    email = Email(**kwargs)
    self.session.add(email)
    self.session.commit()
