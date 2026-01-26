
#Initial Code to hit the public url with parameters and get the output from it
'''import requests

lat = (input("Enter the latitude : "))
long = (input("Enter the longitude : "))

url = "https://api.open-meteo.com/v1/forecast?latitude="+lat+"&longitude="+long+"&hourly=temperature_2m"
response = requests.get(url)
print(response.json())
'''


# Frontend using html for input and output
'''
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h1>Enter Latitude and Longitude</h1>
    <form method="post">
        Latitude: <input type="text" name="latitude"><br>
        Longitude: <input type="text" name="longitude"><br>
        <input type="submit" value="Get Forecast">
    </form>
    {% if forecast %}
    <h2>Forecast Data:</h2>
    <pre>{{ forecast }}</pre>
    {% endif %}
</body>
</html>
"""

from flask import Flask, request, render_template_string
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    forecast = None
    if request.method == 'POST':
        lat = request.form['latitude']
        long = request.form['longitude']
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m"
        response = requests.get(url)
        forecast = response.json()
        #proper formatting of json
        import json
        forecast = json.dumps(forecast, indent=4)
    return render_template_string(html_code, forecast=forecast)

if __name__ == '__main__':
    app.run(debug=True)
'''
    

#add css styling to the html
html_code = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f9;
        }
        h1 {
            color: #333;
        }
        form {
            margin-bottom: 20px;
        }
        input[type="text"] {
            padding: 8px;
            margin: 5px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            padding: 10px 15px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #218838;
        }
        pre {
            background-color: #e9ecef;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>Enter Latitude and Longitude</h1>
    <form method="post">
        Latitude: <input type="text" name="latitude"><br>
        Longitude: <input type="text" name="longitude"><br>
        <input type="submit" value="Get Forecast">
    </form>
    {% if forecast %}
    <h2>Forecast Data:</h2>
    <pre>{{ forecast }}</pre>
    {% endif %}
</body>
</html>
"""

from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    forecast = None
    if request.method == 'POST':
        lat = request.form['latitude']
        long = request.form['longitude']
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&hourly=temperature_2m"
        response = requests.get(url)
        forecast = response.json()
        #proper formatting of json
        import json
        forecast = json.dumps(forecast, indent=4)
    return render_template_string(html_code, forecast=forecast)

if __name__ == '__main__':
    app.run('0.0.0.0',debug=True)

