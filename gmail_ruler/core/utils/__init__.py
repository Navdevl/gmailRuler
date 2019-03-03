#!/usr/bin/env python

import re
from datetime import datetime

def value_from_dict_array(dict_array, key):
  for element in dict_array:
    if element["name"] == key:
      return element["value"]
  return ""

def clean_email(email_string):
  email_string = email_string.lower()
  search_object = re.search("[a-z0-9]+[\.'\-]*[a-z0-9]+@[a-z0-9.]+", email_string)
  if search_object is not None:
    return search_object.group()
  return email_string
 
def convert_string_to_datetime(date_string):
  REGEX_1 = "^[0-9]{1,2}\s[a-zA-Z]{3}\s[0-9]{4}\s[0-9]{2}\:[0-9]{2}\:[0-9]{2}\s\+[0-9]{4}$"
  REGEX_2 = "^[a-zA-Z]{3}\,\s[0-9]{1,2}\s[a-zA-Z]{3}\s[0-9]{4}\s[0-9]{2}\:[0-9]{2}\:[0-9]{2}\s\+[0-9]{4}$"
  REGEX_3 = "^[a-zA-Z]{3}\,\s[0-9]{1,2}\s[a-zA-Z]{3}\s[0-9]{4}\s[0-9]{2}\:[0-9]{2}\:[0-9]{2}\s\+[0-9]{4}\s\([a-zA-Z]{3}\)$"

  if re.match(REGEX_1, date_string):
    return datetime.strptime(date_string, '%d %b %Y %H:%M:%S %z')
  elif re.match(REGEX_2, date_string):
    return datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z')
  elif re.match(REGEX_3, date_string):
    return datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z (%Z)')
  else:
    return None