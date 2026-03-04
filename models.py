from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    @abstractmethod
    def get_info(self):
        pass

class Product(Item):
    def __init__(self, item_id, name, price, quantity, category):
        super().__init__(item_id, name, price)
        self.__quantity = quantity
        self.category = category

    def update_quantity(self, amount):
        self.__quantity += amount

    def get_info(self):
        return f"{self.item_id} - {self.name}, ${self.price}, Qty: {self.__quantity}, Category: {self.category}"

    def get_quantity(self):
        return self.__quantity

class Inventory:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        self.__products[product.item_id] = product

    def remove_product(self, item_id):
        if item_id in self.__products:
            del self.__products[item_id]

    def search_product(self, item_id):
        return self.__products.get(item_id, None)

    def list_all_products(self):
        return [p.get_info() for p in self.__products.values()]

    def category_summary(self):
        summary = {}
        for p in self.__products.values():
            summary[p.category] = summary.get(p.category, 0) + p.get_quantity()
        return summary

    def total_quantity(self):
        return sum(p.get_quantity() for p in self.__products.values())

    def low_stock_count(self, threshold=10):
        return sum(1 for p in self.__products.values() if p.get_quantity() < threshold)

    def avg_price(self):
        if not self.__products:
            return 0
        return sum(p.price for p in self.__products.values()) / len(self.__products)

    def category_count(self):
        return len(set(p.category for p in self.__products.values()))
