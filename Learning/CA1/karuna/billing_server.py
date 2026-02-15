from flask import Flask , request , jsonify
import requests
import pandas as pd
import json


app = Flask(__name__)
url1 = "http://127.0.0.1:5001/inventory"
url2 = "http://127.0.0.1:5002/currency"

@app.route("/billing" , methods = ["GET"])
def billing():

    items = requests.get(url1)
    df = pd.DataFrame(items.json())
    print(df)

    c = 1
    print("Press ID number to add an item in cart")
    for i in df:
        print("ID Number:" , c)
        print(i , df[i].to_list())
        c += 1

    item_id = int(input("Enter the item id number: "))
    key = "Item " + str(item_id)
    
    value = df[key]["Price"]
    currency = df[key]["Currency"]

    payload = {"currency" : currency , "value" : value}
    value = requests.post(url2,json = payload)
    print(value)
    curr = value.json()
    print("Final Bill")
    final = {"Name" : key , "Price" : curr['value'] , "Currency" : curr['currency']}
    print(final)
    return final

app.run(host="0.0.0.0", port=5000, debug=True)
