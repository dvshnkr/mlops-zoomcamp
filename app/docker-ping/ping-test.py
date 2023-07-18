import requests

message = {
    "id": 42
}

url = "http://localhost:9010/ping"
response = requests.post(url, json=message)

print(response.json())
