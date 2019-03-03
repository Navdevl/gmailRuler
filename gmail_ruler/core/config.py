import os

DB_NAME = 'emails.db'

CUR_DIR = os.getcwd()
DATA_DIR = os.path.join(CUR_DIR, 'data')

DB_FILE = os.path.join(DATA_DIR, DB_NAME)
DB_URI="sqlite:///{0}".format(DB_FILE)

CREDENTIALS_JSON = os.path.join(DATA_DIR, 'credentials.json')
PICKLED_CONFIG = os.path.join(DATA_DIR, 'token.pickle')

ENGINE_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly',
          'https://www.googleapis.com/auth/gmail.labels',
          'https://www.googleapis.com/auth/gmail.modify'
          ]
