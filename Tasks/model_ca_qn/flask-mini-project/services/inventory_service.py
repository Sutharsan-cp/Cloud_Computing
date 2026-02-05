class InventoryService:
    def __init__(self):
        self.inventory = {}

    def get_items(self):
        return self.inventory

    def add_item(self, item, price):
        self.inventory[item] = price

    def remove_item(self, item):
        if item in self.inventory:
            del self.inventory[item]