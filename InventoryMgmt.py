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
            print(f"Item ID {item_id} already exists. Updating quantity.")
            self.inventory[item_id].quantity += quantity
        else:
            self.inventory[item_id] = InventoryItem(item_id, name, price, quantity)
        print(f"Item '{name}' added successfully.")

    def remove_item(self, item_id):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item ID {item_id} removed successfully.")
        else:
            print("Item not found in inventory.")

    def update_item(self, item_id, name=None, price=None, quantity=None):
        if item_id in self.inventory:
            if name:
                self.inventory[item_id].name = name
            if price:
                self.inventory[item_id].price = price
            if quantity is not None:  # Allow setting to 0
                self.inventory[item_id].quantity = quantity
            print(f"Item ID {item_id} updated successfully.")
        else:
            print("Item not found in inventory.")

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
            print("Item not found in inventory.")


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
        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            system.add_item(item_id, name, price, quantity)
        elif choice == "2":
            item_id = input("Enter item ID to remove: ")
            system.remove_item(item_id)
        elif choice == "3":
            item_id = input("Enter item ID to update: ")
            name = input("Enter new name (leave blank to skip): ") or None
            price = input("Enter new price (leave blank to skip): ")
            price = float(price) if price else None
            quantity = input("Enter new quantity (leave blank to skip): ")
            quantity = int(quantity) if quantity else None
            system.update_item(item_id, name, price, quantity)
        elif choice == "4":
            system.view_inventory()
        elif choice == "5":
            item_id = input("Enter item ID to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            system.process_sale(item_id, quantity)
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

