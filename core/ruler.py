from model.email import *
from database import *
from sqlalchemy import not_

class Ruler:
  def __init__(self):
    self.db = Database()
    self.db.create_schema()
    self.query = self.db.session.query(Email)

  def filter(self, rule_type, rule_value):
    if rule_type == "contains":
      emails = self.contains(self.query, rule_value).all()
      print(emails)
    else:
      emails = self.contains(self.query, rule_value, True).all()
      print(emails)

  def contains(self, query, string, neg=False):
    if neg:
      return query.filter(not_(Email.subject.like("%{0}%".format(string))))
      return query.filter(Email.subject.like("%{0}%".format(string)))
    else:
      return query.filter(Email.subject.like("%{0}%".format(string)))


ruler = Ruler()
ruler.filter("contains", "GET")

# OPERATORS = {
#     'is_null': lambda f: f.is_(None),
#     'is_not_null': lambda f: f.isnot(None),
#     '==': lambda f, a: f == a,
#     'eq': lambda f, a: f == a,
#     '!=': lambda f, a: f != a,
#     'ne': lambda f, a: f != a,
#     '>': lambda f, a: f > a,
#     'gt': lambda f, a: f > a
#   }
