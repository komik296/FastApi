import requests


url = 'http://127.0.0.1:8000/feedback'
data = {'name': 'John', 'message': 'Johan is already sexy'}

req = requests.get(url, json=data)

print(req.text)