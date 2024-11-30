# Author: Bella Carman
# Date started: 11/20/2024
# Assignment: Backend development connecting GUI and InventoryMgmt. 

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import PIL
import os
from inventory_system import InventoryManagementSystem, InventoryItem 

item_count = 100

class InventoryApp:
    def __init__(self, root):
        self.system = InventoryManagementSystem()
        self.root = root
        self.root.title("Inventory Management System")
        self.root.config(bg="#2a3b4c")

        # Style configuration
        style = ttk.Style()
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
        search_label = ttk.Label(root, text="Search Inventory, or Orders:")
        search_label.grid(column=1, row=0, pady=20)

        self.search_menu = ttk.Combobox(root, font=('MS Serif', 16), width=10, values=("Inventory", "Orders"))
        self.search_menu.grid(column=2, row=0, padx=(0, 200), pady=20)

        self.search_bar = ttk.Entry(root, width=22, font=('MS Serif', 16)).grid(column=2, row=0, padx=(200, 0), pady=20)

        search_button = ttk.Button(root, text="Search", command=self.search_inventory)
        search_button.grid(column=3, row=0, padx=(0, 20), pady=20)

        # Output canvas
        item_canvas = tk.Canvas(root, height=20, width=35, borderwidth=5)
        item_canvas.grid(column=1, row=1, padx=10, sticky=(tk.W, tk.E, tk.S, tk.N))

        text_id = item_canvas.create_text(
            100,
            100,
            text=(f"Item ID: {item_count} \nItem Name: Test Item\nItem Price: $100\nItem Quantity: 50\nDescription: A test item."),
            font=("MS Serif", 14)
        )

        output_listbox = tk.Listbox(root, height=10, width=30, font=('MS Serif', 16), activestyle='none')
        output_listbox.grid(column=2, row=1, padx=10, sticky=(tk.E, tk.N))

        output_listbox.insert(1, "Item 1")
        output_listbox.insert(2, "Item 2")
        output_listbox.insert(3, "Item 3")

        order_canvas = tk.Canvas(root, height=100, width=300)
        order_canvas.grid(row=1, column=2, padx=10, sticky=(tk.E, tk.S))

        totals = order_canvas.create_text(
            80,
            30,
            text=(f"{"Subtotal:" :<10} {"$100.00" :>10}\n{"Tax:" :<10} {"$7.00" :>10}\n{"Total:" :<10} {"$107.00" :>10}"),
            font=("MS Serif", 14))

        # Buttons for adding items, and/or orders
        new_item_button = ttk.Button(root, width=20, text="Add New Item", command=self.add_new_item)
        new_item_button.grid(column=3, row=1, padx=15, pady=(0, 340))

        new_order_button = ttk.Button(root, width=20, text="Start New Order", command=self.add_new_order)
        new_order_button.grid(column=0, row=1, padx=15, pady=(0, 340))

        update_item_button = ttk.Button(root, width=20, text="Update Item")
        update_item_button.grid(column=0, row=1, padx=15, pady=(0,250))

        delete_item_button = ttk.Button(root, width=20, text="Remove Item")
        delete_item_button.grid(column=0, row=1, padx=15, pady=(0,160))

        add_order_buton = ttk.Button(root, width=20, text="Add to Order")
        add_order_buton.grid(column=1, row=99, pady=20)

        checkout_button = ttk.Button(root, width=20, text="Checkout", command=self.checkout_window)
        checkout_button.grid(column=2, row=99, padx=10, sticky=tk.E)

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
        global item_count
        item_count += 1
        def save_item():
            item_id = id_entry.cget("text")
            name = name_entry.get()
            price = float(price_entry.get())
            quantity = int(quantity_entry.get())
            description = str(desc_entry.get())
            self.system.add_item(item_id, name, price, quantity, description)
            self.display_message(f"Item '{name}' added successfully!")
            add_item_window.destroy()

        def confirmCancel(newItemWindow):
            '''Confirms closing of an open entry window, to avoid accidental data loss'''
            response = messagebox.askokcancel("Confirmation", "Cancel without saving?")
            if response:
                newItemWindow.destroy()
            else:
                pass
        
        '''New Item functionality which will automatically instantiate an ID, but will ask for
        a name, price, quantity and description. THIS CONTAINS ERRORS STILL'''
        add_item_window = tk.Toplevel(self.root)
        add_item_window.title("Add New Item")
        add_item_window.attributes('-topmost', True)
        add_item_window.config(bg = "#2a3b4c")

        ttk.Label(add_item_window, text="Item ID:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = ttk.Label(add_item_window, text=item_count)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(add_item_window, text="Name:").grid(row=1, column=0, padx=10, pady=10)
        name_entry = ttk.Entry(add_item_window, width=22, font=("MS Serif", 16))
        name_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(add_item_window, text="Price:").grid(row=2, column=0, padx=10, pady=10)
        price_entry = ttk.Entry(add_item_window, width = 10, font=('MS Serif', 16))
        price_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(add_item_window, text="Quantity:").grid(row=3, column=0, padx=10, pady=10)
        quantity_entry = ttk.Entry(add_item_window, width = 10, font=('MS Serif', 16))
        quantity_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Label(add_item_window, text='Description:').grid(row=4, column=0, padx=10, pady=10, sticky=tk.N)
        desc_entry = tk.Text(add_item_window, height=4, width=20, font=('MS Serif', 16))
        desc_entry.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

        save_button = ttk.Button(add_item_window, text="Save", width=10, command=save_item)
        save_button.grid(row=5, column=0, padx=10, pady=10)

        cancel_button = ttk.Button(add_item_window, text="Cancel", width=10, command=lambda: confirmCancel(add_item_window))
        cancel_button.grid(row=5, column=1, padx=10, pady=10)

    def checkout_window(self):
        '''Checkout Window which will display total amount due & have selection of payment tender,
        will be either Cash or CC and will update dynamically based on radio buttion selection'''
        selected_var = tk.IntVar(value=1)
        change = "0"
        #text_var = tk.StringVar(value=change_amt)

        
        def calc_change():
            '''change calculator that will convert amount due & tendered amounts to float type and totalize'''
            total = total_amt.cget("text")
            tendered = tendered_amt.get()
            change = float(total) - float(tendered)
            change_amt.configure(text=change)


        def cc_checkout():
            '''This is one half of the radiobutton function which will remove the cash tender items
            and replace with CC checkout items and contain all functionality for same'''
            cash_label.grid_forget()
            tendered_amt.grid_forget()
            cash_submit.grid_forget()
            cash_change.grid_forget()
            change_amt.grid_forget()
            
            cc_label = ttk.Label(checkout_window, text="Credit Card Number")
            cc_label.grid(row=3, column=0, pady=10)

            cc_number = ttk.Entry(checkout_window, width=20)
            cc_number.grid(row=4, column=0, padx=10, pady=10)

            cc_exp = ttk.Entry(checkout_window, width=4)
            cc_exp.grid(row=4, column=1, padx=10, pady=10)

        def cash_checkout():
            '''This is one half of the radiobutton function which will remove the CC tender items
            and replace with Cash checkout items and contain all their respective functionality'''
            cash_label = ttk.Label(checkout_window, text="Amount Tendered")
            cash_label.grid(row=3, column=0, padx=10, pady=10)

            tendered_amt = ttk.Entry(checkout_window, width=10)
            tendered_amt.grid(row=3, column=1, padx=10, pady=10)

            cash_submit = ttk.Button(checkout_window, text="Submit", width=10, command=calc_change)
            cash_submit.grid(row=3, column=2, padx=10, pady=10)

            cash_change = ttk.Label(checkout_window, text="Change Due")
            cash_change.grid(row=4, column=0, padx=10, pady=10)

            change_amt = ttk.Label(checkout_window, text=change)
            change_amt.grid(row=4, column=1, padx=10, pady=10)

        '''Checkout window instantiation'''
        checkout_window = tk.Toplevel(self.root)
        checkout_window.title("Checkout")
        checkout_window.attributes('-topmost', True)
        checkout_window.config(bg = "#2a3b4c")

        ttk.Label(checkout_window, text="Total $").grid(row=0, column=0, padx=10, pady=10)
        total_amt = ttk.Label(checkout_window, text="107.00")
        total_amt.grid(row=0, column=1, padx=10, pady=10)

        '''Checkout radiobuttons which will let the user decide between CC & Cash and will dynamically update'''    
        ttk.Label(checkout_window, text="Checkout Method").grid(row=1, column=0, padx=10, pady=10)
        ttk.Radiobutton(checkout_window, text="Credit Card", variable=selected_var, value=2, command=cc_checkout).grid(row=2, column=0, padx=10, pady=10)
        ttk.Radiobutton(checkout_window, text="Cash", variable=selected_var, value=1, command=cash_checkout).grid(row=2, column=1, padx=10, pady=10)

        

        


    def add_new_order(self):
        self.display_message("Order functionality is not implemented yet.")



if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()