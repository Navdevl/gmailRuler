from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from database import *
from utils import *

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.labels',
          'https://www.googleapis.com/auth/gmail.modify'
          ]

class Synchronizer:
    def __init__(self):
        self.creds = None
        self.load_creds()
        self.load_service()
        self.db = Database()
        self.db.create_schema()

    def load_creds(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

    def load_service(self):
        self.service = build('gmail', 'v1', credentials=self.creds)

    def sync_emails(self):
        pass

    def load_emails(self):
        messages = self.service.users().messages().list(userId='me').execute()
        for message in messages['messages']:
            message_id = message['id']
            result = self.service.users().messages().get(userId='me', id=message_id).execute()
            payload = result['payload']

            from_email = clean_email(value_from_dict_array(payload["headers"], "From"))
            to_email = clean_email(value_from_dict_array(payload["headers"], "To"))
            subject = value_from_dict_array(payload["headers"], "Subject")
            received_at = convert_string_to_datetime(value_from_dict_array(payload["headers"], "Date"))

            self.db.create_email({"from_email": from_email, 
                                 "to_email": to_email, 
                                 "subject": subject, 
                                 "message_id": message_id,
                                 "received_at": received_at
                                 })
    def action(self, message_ids):
        print(self.service.users().labels().list(userId='me').execute())
        body = {
            "addLabelIds": ["INBOX"],
            "removeLabelIds": ["UNREAD"],
            "ids": message_ids
        }

        self.service.users().messages().batchModify(userId='me', body=body).execute()
        # print(self.service.users().messages().get(userId='me', id="1692806686b9b864").execute())

synchronizer = Synchronizer()
# synchronizer.load_emails()
synchronizer.action(["1692806686b9b864"])