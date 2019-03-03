# -*- coding: utf-8 -*-

from core.engine import Engine
from core.database import Database
from core.utils import *

# Defining a set of sprites, so that it can be used while long-time email sync.
FRAMES = ["⢄","⢂","⢁","⡁","⡈","⡐","⡠"]

class Synchronizer:
  def __init__(self):
    self.database = Database()
    self.engine = Engine()
    self.service = self.engine.service

  def sync_emails(self, sync_all=False):
    print("Please grab a cup of coffee. It is going to take some time to finish syncing.")
    if sync_all:
      self.sync_all_emails()
    else:
      self.sync_recent_emails()
  
  def sync_recent_emails(self):
    email_response = self.service.users().messages().list(userId='me').execute()
    self.sync_messages(email_response['messages'])

  def sync_all_emails(self):
    email_response = self.service.users().messages().list(userId='me').execute()
    while email_response is not None:
      self.sync_messages(email_response['messages'])
      next_page_token = email_response['nextPageToken']
      email_response = self.service.users().messages().list(userId='me', pageToken=next_page_token).execute()
      
  def sync_messages(self, messages):
    frame_iteration = 0
    for message in messages:
      message_id = message['id']
      result = self.service.users().messages().get(userId='me', id=message_id).execute()
      payload = result['payload']

      from_email = clean_email(value_from_dict_array(payload["headers"], "From"))
      to_email = clean_email(value_from_dict_array(payload["headers"], "To"))
      subject = value_from_dict_array(payload["headers"], "Subject")
      received_at = convert_string_to_datetime(value_from_dict_array(payload["headers"], "Date"))

      self.database.create_email({"from_email": from_email, 
                           "to_email": to_email, 
                           "subject": subject, 
                           "message_id": message_id,
                           "received_at": received_at
                           })
      print("Syncing {0}".format(FRAMES[frame_iteration%7]), flush=True, end='\r')
      frame_iteration += 1