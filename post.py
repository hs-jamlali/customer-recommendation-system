import requests

url = 'http://127.0.0.1:5000/predict'
data = {
    "user_id": 0,
    "item_id": 0
}

response = requests.post(url, json=data)
print(response.json())
