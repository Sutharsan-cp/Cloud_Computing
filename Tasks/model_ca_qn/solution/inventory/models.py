class Item:
    def __init__(self,item_id,name,price,currency):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.currency = currency

    def to_print(self):
        return {
            'item_id' : self.item_id,
            'name' : self.name,
            'price' : self.price,
            'currency' : self.currency
        }
    
# class Inventory:
#     def __init__(self):
#         self.items = []

#     def add_item(self,item):
#         self.items.append(item)

#     def get_items(self):
#         return [item.to_print() for item in self.items]
    
#     def find_item_by_id(self,item_id):
#         for item in self.items:
#             if(item_id == item.item_id):
#                 return item.to_print()
#         return None