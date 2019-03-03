import requests
import json

payload = {
  "rule": {
    "type": "all",
    "list": [ 
      {
        "entity": "received_at",
        "condition": "greater_than",
        "value": 30
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