# Author: Tommy Huggins III
# Start Date: 11/15/24
# SDEV 220

import sys


class InventoryItem:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.item_id} | {self.name} | ${self.price:.2f} | Quantity: {self.quantity}"


class InventoryManagementSystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, name, price, quantity):
        if item_id in self.inventory:
            print(f"Item ID '{item_id}' already exists. Updating quantity.")
            self.inventory[item_id].quantity += quantity
        else:
            self.inventory[item_id] = InventoryItem(item_id, name, price, quantity)
        print(f"Item '{name}' added successfully.")

    def remove_item(self, item_id):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item ID '{item_id}' removed successfully.")
        else:
            print(f"Item ID '{item_id}' not found in inventory.")

    def update_item(self, item_id, name=None, price=None, quantity=None):
        if item_id in self.inventory:
            if name:
                self.inventory[item_id].name = name
            if price is not None:
                self.inventory[item_id].price = price
            if quantity is not None:
                self.inventory[item_id].quantity = quantity
            print(f"Item ID '{item_id}' updated successfully.")
        else:
            print(f"Item ID '{item_id}' not found in inventory.")

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            for item in self.inventory.values():
                print(item)

    def process_sale(self, item_id, quantity):
        if item_id in self.inventory:
            item = self.inventory[item_id]
            if item.quantity >= quantity:
                item.quantity -= quantity
                total_price = item.price * quantity
                print(f"Sale successful! Total: ${total_price:.2f}")
            else:
                print("Insufficient stock.")
        else:
            print(f"Item ID '{item_id}' not found in inventory.")


def main():
    system = InventoryManagementSystem()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View Inventory")
        print("5. Process Sale")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            item_id = input("Enter item ID: ").strip()
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: ").strip())
                quantity = int(input("Enter item quantity: ").strip())
                system.add_item(item_id, name, price, quantity)
            except ValueError:
                print("Invalid price or quantity. Please enter numeric values.")
        elif choice == "2":
            item_id = input("Enter item ID to remove: ").strip()
            system.remove_item(item_id)
        elif choice == "3":
            item_id = input("Enter item ID to update: ").strip()
            name = input("Enter new name (leave blank to skip): ").strip() or None
            price_input = input("Enter new price (leave blank to skip): ").strip()
            quantity_input = input("Enter new quantity (leave blank to skip): ").strip()

            price = float(price_input) if price_input else None
            quantity = int(quantity_input) if quantity_input else None

            try:
                system.update_item(item_id, name, price, quantity)
            except ValueError:
                print("Invalid price or quantity. Please enter numeric values.")
        elif choice == "4":
            system.view_inventory()
        elif choice == "5":
            item_id = input("Enter item ID to sell: ").strip()
            try:
                quantity = int(input("Enter quantity to sell: ").strip())
                system.process_sale(item_id, quantity)
            except ValueError:
                print("Invalid quantity. Please enter a numeric value.")
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

