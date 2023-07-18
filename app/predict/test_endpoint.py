import requests

ride = {
    "trip_distance": 1.7,
    "total_amount": 10,
}

url = 'http://localhost:9696/predict'
response = requests.post(url=url, json=ride)

print(response.json())