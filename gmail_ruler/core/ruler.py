from core.model.email import *
from core.database import *
from sqlalchemy import not_

class Ruler:
  def __init__(self):
    self.db = Database()
    self.db.create_schema()
    self.query = self.db.session.query(Email)

  def apply(self, rule, action):
    rule_type = rule['type']
    rule_list = rule['list']

    for rule_element in rule_list:
      self.filter(**rule_element)
    pass

  def filter(self, entity, condition, value):
    # if condition == "contains":
      # emails = self.contains(self.query, value).all()
      # print(emails)
    # else:
      # emails = self.contains(self.query, value, True).all()
      # print(emails)

  def contains(self, query, string, neg=False):
    
    # if neg:
      # return query.filter(not_(Email.subject.like("%{0}%".format(string))))
    # else:
      # return query.filter(Email.subject.like("%{0}%".format(string)))


# ruler = Ruler()
# ruler.filter("contains", "GET")
print(getattr(Email, 'subject'))
# print((Email.subject.like("%GET"))&((Email.subject.like("%GET"))))

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
