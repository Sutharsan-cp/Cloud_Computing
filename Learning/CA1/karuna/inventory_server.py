import requests
from flask import jsonify , request , Flask

app = Flask(__name__)

@app.route("/inventory" , methods = ["GET"])
def get_inventory():

    items = {"Item 1" : {"Price" : 200 , "Currency" : "dollar"},
             "Item 2" : {"Price" : 300 , "Currency" : "euro"},
             "Item 3" : {"Price" : 400 , "Currency" : "dollar"}
            }

    return items
app.run(host = "0.0.0.0" , port = 5001 , debug = True)