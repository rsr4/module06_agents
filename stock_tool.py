# stock_tool.py
# Author: Rahim Rozani


class StockLookup:
    """Returns the requested stock status of an item"""

    def __init__(self, stock):
        """stores the stock for inventory"""
        self.stock = stock

    def find_product(self, text):
        for product in self.stock:
            if product in text.lower():
                return product
        return None

    def count_for(self, product):
        """Returns the quantity of a stock"""
        if product in self.stock:
            return self.stock[product]
        return None
