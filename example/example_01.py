import requests
import json

# This is an example to select 

payload = {
  "rule": {
    "type": "all",
    "list": [ 
      {
        "entity": "from_email",
        "condition": "equal",
        "value": "pradeek@happyfox.recruiterbox.com"
      },
      {
        "entity": "from_email",
        "condition": "contains",
        "value": "sharon"
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