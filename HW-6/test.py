import requests


url = 'http://127.0.0.1:8000/create_user'

data = {
    "name": "Tommy",
    "email": "tommyold@loh.com",
    "age": 2,
    "is_subscribed": True
    }


re = requests.post(url, json=data)

print(re)
print(re.text)