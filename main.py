import tkinter as tk
from tkinter import messagebox
from abc import ABC, 

# --- OOP CLASS --- 

clsas Item(ABC):
    def __init__(self, item_id,name, price):
        self.item_id = item_id
        self.name = name
        self.price = price
    
    @abstractmethod
    def get_info(self):
        pass
class Product(Item):
    def __init__ (self,item_id,name,price,quantity):
        super().__init__(item_id,name,price)
        self.__quantity = quantity

    def update_quantity(self,amount):
        self.__quantity += amount

    def get_info(self):
        return f"{self.item_id} - {self.name}, ${self.price},Qty : {self.__quantity}"

class Inventory:
    def __init__(self):
        self.products = {}

    def __add_product(self, product )