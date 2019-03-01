from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Email(Base):
  __tablename__ = "emails"

  id = Column(Integer, primary_key=True, autoincrement=True)
  message_id = Column(String)
  from_email = Column(String)
  to_email = Column(String)
  subject = Column(Text)
  received_at = Column(DateTime)

  def __repr__(self):
    return "{0}: {1}".format(self.message_id, self.subject)