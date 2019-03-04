import requests
import json

# This is an example to do the following functionality.
# Filer emails that contains a specific keyword either in the subject or in the content
# And mark all those filtered emails to UNREAD.

payload = {
  "rule": {
    "type": "any",
    "list": [ 
      {
        "entity": "subject",
        "condition": "contains",
        "value": "keyword"
      },
      {
        "entity": "content",
        "condition": "contains",
        "value": "keyword"
      }
    ]
  },
  "action": {
    "list": [
      {
        "value": "UNREAD"
      }
    ]
  }
}
response = requests.post('http://localhost:5000', json=payload)
print(json.loads(response.content))

