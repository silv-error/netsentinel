import requests

url = "http://127.0.0.1:8000/api/send_status"
url_two = "http://127.0.0.1:8000/api/device_data"
data = [
    {
    "interface": "Device01",
    "status": "Online",
    "ip": "192.168.1.10",
    "protocol": "UP"
},
    {
    "interface": "Device01",
    "status": "Online",
    "ip": "192.168.1.10",
    "protocol": "UP"
},
    {
    "interface": "Device01",
    "status": "Online",
    "ip": "192.168.1.10",
    "protocol": "UP"
}
]

response = requests.post(url, json=data)

another_response = requests.get(url_two)
print(response.json())
print(another_response.json())

