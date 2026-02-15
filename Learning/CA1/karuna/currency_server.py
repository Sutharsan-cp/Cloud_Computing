from flask import Flask , request , jsonify
import requests

app = Flask(__name__)

@app.route("/currency" , methods = ['POST'])
def currency_converter():

    data = request.get_json()
    currency = str(data.get('currency'))
    value = float(data.get('value'))

    if currency == 'dollar':
        return {"currency" : "rupees" , "value" : value * 90}

    if currency == 'euro':
        return {"currency" : "rupees" , "value" : value * 105}

app.run(host = '0.0.0.0' , port = 5002 , debug = True)