from flask import Flask, jsonify, request
from services.inventory_service import InventoryService
from services.billing_service import BillingService
from services.currency_converter_service import CurrencyConverterService

app = Flask(__name__)

inventory_service = InventoryService()
billing_service = BillingService()
currency_converter_service = CurrencyConverterService()

@app.route('/inventory', methods=['GET'])
def get_inventory():
    items = inventory_service.get_items()
    return jsonify(items)

@app.route('/inventory', methods=['POST'])
def add_item():
    item = request.json
    inventory_service.add_item(item)
    return jsonify({"message": "Item added successfully"}), 201

@app.route('/billing', methods=['POST'])
def calculate_billing():
    selected_items = request.json.get('items', [])
    total = billing_service.calculate_total(selected_items)
    return jsonify({"total": total})

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.json
    amount = data.get('amount', 0)
    currency_type = data.get('currency_type', 'dollars')
    
    if currency_type == 'dollars':
        converted_amount = currency_converter_service.convert_to_rupees(amount)
    else:
        converted_amount = currency_converter_service.convert_to_dollars(amount)
    
    return jsonify({"converted_amount": converted_amount})

if __name__ == '__main__':
    app.run(debug=True)