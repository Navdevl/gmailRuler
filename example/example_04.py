import requests
import json

# This is an example to do the following functionality.
# Filer emails that are older than 220 days.
# And mark all those filtered emails to INBOX.

# The datetime instances are assumed to have loosely coupled from the client.
# So, when 2 month is selected in the client, it is assumed that the value is 
# converted into days and sent to the REST server.

payload = {
  "rule": {
    "type": "all",
    "list": [ 
      {
        "entity": "received_at",
        "condition": "less_than",
        "value": 220 # in days
      }
    ]
  },
  "action": {
    "list": [
      {
        "value": "INBOX"
      }
    ]
  }
}
response = requests.post('http://localhost:5000', json=payload)
print(json.loads(response.content))
