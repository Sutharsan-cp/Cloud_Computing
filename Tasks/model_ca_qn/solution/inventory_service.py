from flask import Flask,request,jsonify
from inventory.models import Item
from billing.models import Bill

app = Flask(__name__)

#sample inventory items
inventory_items ={
    1 : {"name" : "Item A","price" : 10.0},
    2 : {"name" : "Item B","price" : 20.0}
} 

@app.route('/inventory',methods = ['GET'])
def get_items():
    return jsonify(inventory_items)

@app.route('/inventory/<itemname>',methods = ['GET'])
def check_item(itemname):
    for item in inventory_items:
        if itemname == item["name"]:
            return jsonify(item.to_print())
    return None

@app.route("/inventory/select", methods=["POST"]) 
def select_items(): 
    data = request.json 
    selected_ids = data.get("item_ids", []) 
    selected_items = [item for item in inventory_items if item.item_id in selected_ids] 
    return jsonify([item.to_print() for item in selected_items]) 
    
if __name__ == '__main__':
    app.run(debug = True,port = 5003)
