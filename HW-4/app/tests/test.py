import requests


url = 'http://127.0.0.1:8000/user'

req = requests.post(url, json={'name': 'Johan', 'age': 18})

print(req.text)