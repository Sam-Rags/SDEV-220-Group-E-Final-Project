# Author: Tommy Huggins III
# Start Date: 11/15/24
# SDEV 220

import sqlite3
import sys

class InventoryManagementSystem:
    def __init__(self):
        # Initialize database connection
        self.connection = sqlite3.connect('inventory.db')  # Creates database file if it doesn't exist
        self.cursor = self.connection.cursor()

        # Create table if it doesn't exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                item_id TEXT PRIMARY KEY,
                name TEXT,
                price REAL,
                quantity INTEGER
            )
        ''')
        self.connection.commit()

    def add_item(self, item):
        """
        Add an item to the inventory database.
        """
        if isinstance(item, InventoryItem):
            # Check if item already exists
            self.cursor.execute('SELECT * FROM inventory WHERE item_id = ?', (item.item_id,))
            existing_item = self.cursor.fetchone()

            if existing_item:
                # Update quantity if item already exists
                new_quantity = existing_item[3] + item.quantity  # Add the quantities
                self.cursor.execute('UPDATE inventory SET quantity = ? WHERE item_id = ?',
                                    (new_quantity, item.item_id))
            else:
                # Add new item to the database
                self.cursor.execute('''
                    INSERT INTO inventory (item_id, name, price, quantity)
                    VALUES (?, ?, ?, ?)
                ''', (item.item_id, item.name, item.price, item.quantity))

            self.connection.commit()
            print(f"Item '{item.name}' added or updated successfully.")

    def remove_item(self, item_id):
        self.cursor.execute('DELETE FROM inventory WHERE item_id = ?', (item_id,))
        self.connection.commit()
        print(f"Item ID {item_id} removed successfully.")

    def update_item(self, item_id, name=None, price=None, quantity=None):
        if name:
            self.cursor.execute('UPDATE inventory SET name = ? WHERE item_id = ?', (name, item_id))
        if price:
            self.cursor.execute('UPDATE inventory SET price = ? WHERE item_id = ?', (price, item_id))
        if quantity is not None:  # Allow setting to 0
            self.cursor.execute('UPDATE inventory SET quantity = ? WHERE item_id = ?', (quantity, item_id))

        self.connection.commit()
        print(f"Item ID {item_id} updated successfully.")

    def view_inventory(self):
        self.cursor.execute('SELECT * FROM inventory')
        items = self.cursor.fetchall()
        if items:
            print("\nCurrent Inventory:")
            for item in items:
                print(f"{item[0]} | {item[1]} | ${item[2]:.2f} | Quantity: {item[3]}")
        else:
            print("Inventory is empty.")

    def process_sale(self, item_id, quantity):
        self.cursor.execute('SELECT * FROM inventory WHERE item_id = ?', (item_id,))
        item = self.cursor.fetchone()
        if item:
            if item[3] >= quantity:
                new_quantity = item[3] - quantity
                self.cursor.execute('UPDATE inventory SET quantity = ? WHERE item_id = ?',
                                    (new_quantity, item_id))
                self.connection.commit()
                total_price = item[2] * quantity
                print(f"Sale successful! Total: ${total_price:.2f}")
            else:
                print("Insufficient stock.")
        else:
            print("Item not found in inventory.")
