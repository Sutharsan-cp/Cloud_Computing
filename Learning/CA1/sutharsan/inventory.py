from flask import Flask
import logging

app = Flask(__name__)
# logging.basicConfig(
#     filename = "app.log",
#     level = logging.INFO,
#     format = "%(asctime)s - %(levelname)s - %(message)s"
# )

items = {
    "laptop": {"price": 50000, "stock": 10,"currency" : "dollars"},
    "phone": {"price": 20000, "stock": 20,"currency" : "ruppess"},
    "tablet": {"price": 30000, "stock": 15,"currency" : "dollars"}
}


@app.route('/inventory',methods = ["GET"])
def inventory():
    #logging.info("Accessed Inventory Items")
    return items

@app.route('/inventory/<name>')
def check_inventory(name):
    #logging.info("Check whether the item " + name + " existed")
    if name in items :
        return items[name]
    
    return "Item not found in Inventory"


app.run(host = "0.0.0.0" ,port = 5001,debug = True)