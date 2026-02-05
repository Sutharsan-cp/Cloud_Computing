class BillingService:
    def calculate_total(self, selected_items):
        total = 0
        for item in selected_items:
            total += item['price'] * item['quantity']
        return total