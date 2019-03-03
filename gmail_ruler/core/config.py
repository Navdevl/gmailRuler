import os

DATA_DIR_NAME = 'data'
DB_NAME = 'emails.db'

CUR_DIR = os.getcwd()
DATA_DIR = os.path.join(CUR_DIR, DATA_DIR_NAME)

DB_URI = os.path.join(DATA_DIR, DB_NAME)
DB_CONF="sqlite:///{0}".format(DB_URI)

ENGINE_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.labels',
          'https://www.googleapis.com/auth/gmail.modify'
          ]
