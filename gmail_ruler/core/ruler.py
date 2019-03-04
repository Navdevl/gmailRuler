# -*- coding: utf-8 -*-

"""
This is the trivial module among all other core modules.
This provides the filter and execute action functionalities.

filter() and execute() functions makes the beautiful moves in the
whole python package.

The number of functions defined are reduced using neg operation. 
To understand, instead of having two different functions like equals() and not_equals(),
the equals() function has a neg parameter which will negate the whole operation and
making it not_equal. Same applies to all other functions too.
"""

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
    """
    Apply function is the one that is exposes to be called from API endpont.
    This does the filter and execute operation and returns the number of emails 
    touched through this functionality call.

    """

    self.filter(rule)
    self.execute(action)
    return len(self.response.all())

  def filter(self, rule):
    """
    filter function uses the list of rule elements and the rule type to proceed.
    """
    rule_type = rule['type']
    rule_list = rule['list']
    master_query = None
    for rule_element in rule_list:
      query = self.apply_condition(**rule_element)
      if master_query is None:
        master_query = query
      else:
        """
        Depending on the rule_type, the AND or the OR operation is decided.
        """
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
    
    # This pagination call is happening because of the gmail client's restriction on 1000 message_ids at once.
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
    """
    All "move to" actions are handled through "addLabelIds" attribute.
    Only "Mark as read" action needs to be handled by "removeLabelIds" attribute
    by removing the UNREAD label.
    """
    if value == "READ":
      action_payload["removeLabelIds"].append("UNREAD")
    else:
      action_payload["addLabelIds"].append(value)
    return action_payload

  def apply_condition(self, entity, condition, value):
    """
    This function acts like the router to different functions based on condition.
    """
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
    """
    contains function acts only on the string type.
    So, once it is validated, we proceed to create the 
    query.
    """
    query_entity = getattr(Email, entity)
    if isinstance(query_entity.type, String):
      if neg:
        return not_(query_entity.like("%{0}%".format(value)))
      return query_entity.like("%{0}%".format(value))
    else:
      return

  def equals(self, entity, value, neg=False):
    """
    equal function acts only on the string type.
    So, once it is validated, we proceed to create the 
    query.
    """
    query_entity = getattr(Email, entity)
    if isinstance(query_entity.type, String):
      if neg:
        return not_(query_entity == "{0}".format(value))
      return query_entity == "{0}".format(value)
    else:
      return

  def less_than(self, entity, value, neg=False):
    """
    less_than function acts only on the datetime type.
    So, once it is validated, we proceed to create the 
    query.
    """
    query_entity = getattr(Email, entity)
    if isinstance(query_entity.type, DateTime):
      current_time = datetime.datetime.utcnow()
      query_datetime = current_time - datetime.timedelta(days=value)
      if neg:
        return not_(query_entity < "{0}".format(query_datetime))
      return query_entity < "{0}".format(query_datetime)
    else:
      return