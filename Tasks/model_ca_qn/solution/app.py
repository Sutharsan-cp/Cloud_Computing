from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

INVENTORY_URL = "http://localhost:5001"
BILLING_URL = "http://localhost:5002"
CURRENCY_URL = "http://localhost:5003"

@app.route("/checkout", methods=["POST"])
def checkout():
    data = request.json
    item_ids = data.get("item_ids", [])
    target_currency = data.get("target_currency", "USD")

    # Step 1: Get selected items from inventory
    inv_resp = requests.post(f"{INVENTORY_URL}/inventory/select", json={"item_ids": item_ids})
    items = inv_resp.json()

    # Step 2: Send items to billing
    bill_resp = requests.post(f"{BILLING_URL}/billing", json={"items": items})
    bill = bill_resp.json()

    # Step 3: Convert total if needed
    if bill["currency"] != target_currency:
        conv_resp = requests.post(f"{CURRENCY_URL}/convert", json={
            "amount": bill["total"],
            "from_currency": bill["currency"],
            "to_currency": target_currency
        })
        conversion = conv_resp.json()
        bill["total"] = conversion["converted_amount"]
        bill["currency"] = target_currency

    return jsonify(bill)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
