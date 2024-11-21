# Author: Bella Carman
# Date started: 11/20/2024
# Assignment: Backend development connecting GUI and InventoryMgmt. 

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import PIL
import os
from inventory_system import InventoryManagementSystem, InventoryItem 

class InventoryApp:
    def __init__(self, root):
        self.system = InventoryManagementSystem()
        self.root = root
        self.root.title("Inventory Management System")
        self.root.config(bg="#2a3b4c")

        # Style configuration
        style = ttk.Style(self.root)
        style.theme_use('winnative')
        style.configure('.', font=('MS Serif', 16))
        style.configure('TButton', background='#1fcc81', foreground='#1fcc81')
        style.configure('TLabel', background='#2a3b4c', foreground="white")

        # Logo setup
        script_directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_directory)
        image = Image.open("generic-logo.jpg")
        new_size = (200, 66)
        resized_image = image.resize(new_size, PIL.Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(resized_image)
        image_label = tk.Label(root, image=photo, bd=0)
        image_label.image = photo  # Keep reference to avoid garbage collection
        image_label.grid(row=0, column=0)

        # Search bar setup
        search_label = ttk.Label(root, text="Search Customers, Inventory, or Orders:")
        search_label.grid(column=1, row=0, pady=20)

        self.search_menu = ttk.Combobox(root, font=('MS Serif', 16), width=10, values=("Customer", "Inventory", "Orders"))
        self.search_menu.grid(column=2, row=0, padx=(0, 200), pady=20)

        self.search_bar = ttk.Entry(root, width=22, font=('MS Serif', 16))
        self.search_bar.grid(column=2, row=0, padx=(200, 0), pady=20)

        search_button = ttk.Button(root, text="Search", command=self.search_inventory)
        search_button.grid(column=3, row=0, padx=(0, 20), pady=20)

        # Output canvas
        self.output_canvas = tk.Text(root, height=20, width=80, font=('MS Serif', 16))
        self.output_canvas.grid(column=1, row=1, columnspan=2, padx=20)

        # Buttons for adding items, orders, and customers
        new_item_button = ttk.Button(root, width=20, text="Add New Item", command=self.add_new_item)
        new_item_button.grid(column=0, row=1, padx=15, pady=(0, 250))

        new_order_button = ttk.Button(root, width=20, text="Add New Order", command=self.add_new_order)
        new_order_button.grid(column=0, row=1, padx=15, pady=(0, 340))

        new_customer_button = ttk.Button(root, width=20, text="Add New Customer")
        new_customer_button.grid(column=0, padx=15, row=1, pady=(0, 160))

        exit_button = ttk.Button(root, text="Quit Program", width=20, command=root.destroy)
        exit_button.grid(column=0, row=99, pady=20)

    def display_message(self, message):
        self.output_canvas.delete('1.0', tk.END)  # Clear previous output
        self.output_canvas.insert(tk.END, message)

    def search_inventory(self):
        query = self.search_bar.get()
        if self.search_menu.get() == "Inventory":
            results = [str(item) for item in self.system.inventory.values() if query.lower() in item.name.lower()]
            if results:
                self.display_message("\n".join(results))
            else:
                self.display_message("No items found in inventory.")
        else:
            self.display_message("Search functionality is only implemented for Inventory.")

    def add_new_item(self):
        # Pop-up window to add a new item
        def save_item():
            item_id = id_entry.get()
            name = name_entry.get()
            price = float(price_entry.get())
            quantity = int(quantity_entry.get())
            self.system.add_item(item_id, name, price, quantity)
            self.display_message(f"Item '{name}' added successfully!")
            add_item_window.destroy()

        add_item_window = tk.Toplevel(self.root)
        add_item_window.title("Add New Item")

        tk.Label(add_item_window, text="Item ID:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(add_item_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_item_window, text="Name:").grid(row=1, column=0, padx=10, pady=10)
        name_entry = tk.Entry(add_item_window)
        name_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(add_item_window, text="Price:").grid(row=2, column=0, padx=10, pady=10)
        price_entry = tk.Entry(add_item_window)
        price_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(add_item_window, text="Quantity:").grid(row=3, column=0, padx=10, pady=10)
        quantity_entry = tk.Entry(add_item_window)
        quantity_entry.grid(row=3, column=1, padx=10, pady=10)

        save_button = ttk.Button(add_item_window, text="Save", command=save_item)
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_new_order(self):
        self.display_message("Order functionality is not implemented yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
