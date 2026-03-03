import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# --- OOP Classes ---
class Item(ABC):
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    @abstractmethod
    def get_info(self):
        pass

class Product(Item):
    def __init__(self, item_id, name, price, quantity):
        super().__init__(item_id, name, price)
        self.__quantity = quantity

    def update_quantity(self, amount):
        self.__quantity += amount

    def get_info(self):
        return f"{self.item_id} - {self.name}, ${self.price}, Qty: {self.__quantity}"

class Inventory:
    def __init__(self):
        self.__products = {}

    def add_product(self, product):
        self.__products[product.item_id] = product

    def remove_product(self, item_id):
        if item_id in self.__products:
            del self.__products[item_id]

    def list_all_products(self):
        return [p.get_info() for p in self.__products.values()]

# --- GUI Application ---
class InventoryApp:
    def __init__(self, root):
        self.inventory = Inventory()
        self.root = root
        self.root.title("Inventory System")

        # Input fields
        tk.Label(root, text="Item ID").grid(row=0, column=0)
        tk.Label(root, text="Name").grid(row=1, column=0)
        tk.Label(root, text="Price").grid(row=2, column=0)
        tk.Label(root, text="Quantity").grid(row=3, column=0)

        self.entry_id = tk.Entry(root)
        self.entry_name = tk.Entry(root)
        self.entry_price = tk.Entry(root)
        self.entry_qty = tk.Entry(root)

        self.entry_id.grid(row=0, column=1)
        self.entry_name.grid(row=1, column=1)
        self.entry_price.grid(row=2, column=1)
        self.entry_qty.grid(row=3, column=1)

        # Buttons
        tk.Button(root, text="Add Product", command=self.add_product).grid(row=4, column=0)
        tk.Button(root, text="Remove Product", command=self.remove_product).grid(row=4, column=1)
        tk.Button(root, text="List Products", command=self.list_products).grid(row=5, column=0, columnspan=2)

        # Display area
        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.grid(row=6, column=0, columnspan=2)

    def add_product(self):
        try:
            item_id = self.entry_id.get()
            name = self.entry_name.get()
            price = float(self.entry_price.get())
            qty = int(self.entry_qty.get())
            product = Product(item_id, name, price, qty)
            self.inventory.add_product(product)
            messagebox.showinfo("Success", f"Product {name} added!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    def remove_product(self):
        item_id = self.entry_id.get()
        self.inventory.remove_product(item_id)
        messagebox.showinfo("Success", f"Product {item_id} removed!")

    def list_products(self):
        self.text_area.delete("1.0", tk.END)
        products = self.inventory.list_all_products()
        for p in products:
            self.text_area.insert(tk.END, p + "\n")

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()