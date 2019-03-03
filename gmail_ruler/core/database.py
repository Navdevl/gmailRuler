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
    Base.metadata.create_all(bind=self.engine)

  def create_email(self, kwargs):
    email = Email(**kwargs)
    self.session.add(email)
    self.session.commit()
