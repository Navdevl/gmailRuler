import requests
import json

# This is an example to select emails from a certain person and mark it read.
# It is assumed that the client sends the action's value as READ if it is operated to "Read all filtered messages"

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