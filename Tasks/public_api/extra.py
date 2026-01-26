#Karuna code to socket connect to his port and run the code


import requests
import json

# Example: your Flask endpoint
url = "http://10.1.66.169:5000/add"

# Send POST request with two numbers
latitude = float(input("Enter the latitude: "))
longitude = float(input("Enter the longitude: "))
payload = {"latitude": latitude, "longitude": longitude}
response = requests.post(url, json=payload)

# Convert response to JSON
data = response
print("Response:", data)

# Save to a JSON file
with open("result.json", "w") as f:
    json.dump(data.json(), f, indent=4)