import requests


payload = {"name": "naveen"}
response = requests.post('http://localhost:5000', json=payload)

print(response)