from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.labels',
          'https://www.googleapis.com/auth/gmail.modify'
          ]

class Engine:
  def __init__(self):
    self.creds = None
    self.load_creds()
    self.load_service()

  def load_creds(self):
    if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
        self.creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not self.creds or not self.creds.valid:
      if self.creds and self.creds.expired and self.creds.refresh_token:
        self.creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        self.creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
          pickle.dump(self.creds, token)

  def load_service(self):
    self.service = build('gmail', 'v1', credentials=self.creds)