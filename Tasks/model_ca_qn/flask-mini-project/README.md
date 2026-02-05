# Flask Mini Project

This project is a mini application built using Flask that includes three services: an inventory service, a billing service, and a currency converter service.

## Project Structure

```
flask-mini-project
├── app.py
├── services
│   ├── inventory_service.py
│   ├── billing_service.py
│   └── currency_converter_service.py
├── requirements.txt
└── README.md
```

## Services

1. **Inventory Service**: Manages the inventory of items.
   - Methods:
     - `get_items()`: Retrieves available items.
     - `add_item(item)`: Adds new items to the inventory.

2. **Billing Service**: Calculates the total cost of selected items.
   - Methods:
     - `calculate_total(selected_items)`: Computes the total price based on the selected items.

3. **Currency Converter Service**: Handles currency conversion between dollars and rupees.
   - Methods:
     - `convert_to_rupees(amount)`: Converts dollars to rupees.
     - `convert_to_dollars(amount)`: Converts rupees to dollars.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-mini-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

## Usage Examples

- To retrieve available items, call the `get_items()` method from the Inventory Service.
- To calculate the total cost of selected items, use the `calculate_total(selected_items)` method from the Billing Service.
- For currency conversion, utilize the `convert_to_rupees(amount)` or `convert_to_dollars(amount)` methods from the Currency Converter Service.

## License

This project is licensed under the MIT License.