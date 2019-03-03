import requests


payload = {
  "rule": {
    "type": "all",
    "list": [ {
      "entity": "From",
      "condition": "contains",
      "value": "tenmiles.com"
      }
    ]
  },
  "action": {
    "list": []
  }
}
response = requests.post('http://localhost:5000', json=payload)

print(response)