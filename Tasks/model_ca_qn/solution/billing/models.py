class Bill:
    def __init__(self,items,total,currency):
        self.items = items
        self.total = total
        self.currency = currency

    def to_print(self):
        return { 
            "items": [item.to_print() for item in self.items], 
            "total": self.total, 
            "currency": self.currency 
        }