from core.engine import Engine
from core.database import Database
from core.utils import *

FRAMES = ["⢄","⢂","⢁","⡁","⡈","⡐","⡠"]

class Synchronizer:
  def __init__(self):
    self.database = Database()
    self.engine = Engine()
    self.service = self.engine.service

  def sync_emails(self, sync_all=False):
    if sync_all:
      self.sync_all_emails()
    else:
      self.sync_recent_emails()
  
  def sync_recent_emails(self):
    emails = self.service.users().messages().list(userId='me').execute()
    for message in emails['messages']:
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

  def sync_all_emails(self):
    email_response = self.service.users().messages().list(userId='me').execute()
    frame_iteration = 0
    while email_response is not None:
      for message in email_response['messages']:
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
      next_page_token = email_response['nextPageToken']
      email_response = self.service.users().messages().list(userId='me', pageToken=next_page_token).execute()
      
      print("Syncing {0}".format(FRAMES[frame_iteration%7]), flush=True, end='\r')
      frame_iteration += 1
