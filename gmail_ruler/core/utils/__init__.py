# -*- coding: utf-8 -*-
#!/usr/bin/env python

import re
import base64
from bs4 import BeautifulSoup
from datetime import datetime


def value_from_dict_array(dict_array, key):
  """
  Provided an array of dictionary objects and to extract a value depending on the condition,
  this function makes a beautiful purpose.
  """
  for element in dict_array:
    if element["name"] == key:
      return element["value"]
  return ""

def clean_email(email_string):
  """
  This function cleans the email_string from the Gmail client's response.
  """
  email_string = email_string.lower()
  search_object = re.search("[a-z0-9]+[\.'\-]*[a-z0-9]+@[a-z0-9.]+", email_string)
  if search_object is not None:
    return search_object.group()
  return email_string
 
def convert_string_to_datetime(date_string):
  """
  This function matches the date_string from the Gmail client's response and does the appropriate 
  action to convert them to a datetime object.
  """
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

def get_html_part(parts):
  """
  Extracts the right body part from the payload parts. 
  This is identified by taking the mimeType as text/html.
  """
  for part in parts:
    if part["mimeType"] == "text/html":
      return part["body"]["data"]
  return ""

def convert_base64_to_string(base64_string):
  """
  Converts the base64 string to a proper clean raw text.
  """
  html = base64.urlsafe_b64decode(base64_string.encode('ASCII'))
  soup = BeautifulSoup(html, features="html.parser")
  for s in soup(['script', 'style']):
      s.decompose()
  return ' '.join(soup.stripped_strings)
