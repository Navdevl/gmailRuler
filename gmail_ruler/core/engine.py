# -*- coding: utf-8 -*-

"""
This model acts as an engine that provides the service attribute which has
the ability to communicate with gmail's APIs. 

This is referenced from the example quoted in the following URL.
https://developers.google.com/gmail/api/quickstart/python
"""
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from core import config

class Engine:
  def __init__(self):
    self.creds = None
    self.load_creds()
    self.load_service()

  def load_creds(self):
    if os.path.exists(config.PICKLED_CONFIG):
      with open(config.PICKLED_CONFIG, 'rb') as token:
        self.creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not self.creds or not self.creds.valid:
      if self.creds and self.creds.expired and self.creds.refresh_token:
        self.creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(config.CREDENTIALS_JSON, config.ENGINE_SCOPES)
        self.creds = flow.run_local_server()
        # Save the credentials for the next run
        with open(config.PICKLED_CONFIG, 'wb') as token:
          pickle.dump(self.creds, token)

  def load_service(self):
    self.service = build('gmail', 'v1', credentials=self.creds)