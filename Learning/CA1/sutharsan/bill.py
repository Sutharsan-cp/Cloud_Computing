from flask import Flask
import requests
import pandas as pd
import logging

url_inventory = "http://127.0.0.1:5001/inventory"
url_currency = "http://127.0.0.1:5002/currency"

app = Flask(__name__)

logging.basicConfig(
    filename = "app.log",
    level = logging.INFO,
    format= "%(asctime)s - %(levelname)s -%(message)s"
)

@app.route('/bill',methods = ["GET"])
def bill():
    data = requests.get(url_inventory)
    logging.info("post to bill")
    print(pd.DataFrame(data.json()))
    data = data.json()
    choose = input("Enter the item name , u want : ")
    item = data[choose]
    print(item["currency"])
    if(item["currency"] == "dollars"):
        new_price = requests.post(url_currency,json = item)
        logging.info("currency convertion")
        new_price = new_price.json()    
        item["currency"] = "ruppees"
        print(new_price)
        item["price"] = new_price["converted"]
    print(item)
    return data

app.run(host = "0.0.0.0" ,port = 5003,debug = True) 