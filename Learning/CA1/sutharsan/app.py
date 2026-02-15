import requests

url = "http://127.0.0.1:5003/bill"

res = requests.get(url)

if res.status_code == 200:
    print("Successfully")

