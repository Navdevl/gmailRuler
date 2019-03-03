from core.model.email import Email
from core.database import Database
from core.engine import Engine
from sqlalchemy import not_
from sqlalchemy_pagination import paginate
from sqlalchemy.types import DateTime, String
import datetime


class Ruler:
  def __init__(self):
    self.db = Database()
    self.db.create_schema()
    self.query = self.db.session.query(Email)
    self.engine = Engine()
    self.service = self.engine.service

  def apply(self, rule, action):
    self.filter(rule)
    self.execute(action)
    return len(self.response.all())

  def filter(self, rule):
    rule_type = rule['type']
    rule_list = rule['list']
    master_query = None
    for rule_element in rule_list:
      query = self.apply_condition(**rule_element)
      if master_query is None:
        master_query = query
      else:
        if rule_type == "all":
          master_query = master_query & query
        else:
          master_query = master_query | query

    self.response = self.query.filter(master_query)

  def execute(self, action):
    action_list = action['list']
    action_payload = { "removeLabelIds": [], "addLabelIds": [], "ids": [] }
    for action_element in action_list:
      action_payload = self.apply_action(action_payload, **action_element)
    
    current_page = 1
    while True:
      page = paginate(self.response, current_page, 25)
      message_ids = [item.message_id for item in page.items]
      action_payload["ids"] = message_ids
      self.service.users().messages().batchModify(userId='me', body=action_payload).execute()
      current_page = page.next_page
      if current_page is None:
        break

  def apply_action(self, action_payload, value):
    if value == "READ":
      action_payload["removeLabelIds"].append("UNREAD")
    else:
      action_payload["addLabelIds"].append(value)
    return action_payload

  def apply_condition(self, entity, condition, value):
    if condition == "contains":
      return self.contains(entity, value)
    elif condition == "not_contains":
      return self.contains(entity, value, neg=True)
    elif condition == "equal":
      return self.equals(entity, value)
    elif condition == "not_equal":
      return self.equals(entity, value, neg=True)
    elif condition == "less_than":
      return self.less_than(entity, value)
    elif condition == "greater_than":
      return self.less_than(entity, value, neg=True)


  def contains(self, entity, value, neg=False):
    query_entity = getattr(Email, entity)
    if isinstance(query_entity.type, String):
      if neg:
        return not_(query_entity.like("%{0}%".format(value)))
      return query_entity.like("%{0}%".format(value))
    else:
      return

  def equals(self, entity, value, neg=False):
    query_entity = getattr(Email, entity)
    if isinstance(query_entity.type, String):
      if neg:
        return not_(query_entity == "{0}".format(value))
      return query_entity == "{0}".format(value)
    else:
      return

  def less_than(self, entity, value, neg=False):
    query_entity = getattr(Email, entity)
    print(isinstance(query_entity.type, DateTime))
    if isinstance(query_entity.type, DateTime):
      current_time = datetime.datetime.utcnow()
      query_datetime = current_time - datetime.timedelta(days=value)
      if neg:
        return not_(query_entity < "{0}".format(query_datetime))
      return query_entity < "{0}".format(query_datetime)
    else:
      return