from flask import Flask
from inventory_service import inventory_service
from billing_service import billing_service
from currency_converter_service import currency_converter_service

app = Flask(__name__)

# Register blueprints
app.register_blueprint(inventory_service, url_prefix='/inventory')
app.register_blueprint(billing_service, url_prefix='/billing')
app.register_blueprint(currency_converter_service, url_prefix='/currency')

if __name__ == '__main__':
    app.run(debug=True)
