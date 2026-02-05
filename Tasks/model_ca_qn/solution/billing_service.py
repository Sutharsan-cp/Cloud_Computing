from flask import Flask, jsonify, request
from inventory.models import Item
from billing.models import Bill

app = Flask(__name__)

@app.route("/billing", methods=["POST"])
def calculate_bill():
    data = request.json
    items_data = data.get("items", [])
    items = [Item(i["id"], i["name"], i["price"], i["currency"]) for i in items_data]

    total = sum(item.price for item in items)
    bill = Bill(items, total, items[0].currency if items else "USD")

    return jsonify(bill.to_dict())

if __name__ == "__main__":
    app.run(port=5002, debug=True)
