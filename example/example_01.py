import requests
import json

# This is an example to do the following functionality.
# Filer by from_email that equals to specific email ID.
# And mark all those filtered emails to READ.

payload = {
  "rule": {
    "type": "all",
    "list": [ 
      {
        "entity": "from_email",
        "condition": "equal",
        "value": "pradeek@happyfox.recruiterbox.com"
      }
    ]
  },
  "action": {
    "list": [
      {
        "value": "READ"
      }
    ]
  }
}

response = requests.post('http://localhost:5000', json=payload)
print(json.loads(response.content))