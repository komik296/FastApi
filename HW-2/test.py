import requests

url = 'http://127.0.0.1:8000/calculate'

req = requests.post(url, json={'num1': 7, 'num2': 3})

print(req.text)