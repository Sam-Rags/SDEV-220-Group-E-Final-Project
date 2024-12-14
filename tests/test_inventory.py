# tests/test_inventory.py

import unittest
from inventory_system import InventoryManagementSystem, InventoryItem

class TestInventoryManagementSystem(unittest.TestCase):
    
    def setUp(self):
        """Create the InventoryManagementSystem and some initial items."""
        self.system = InventoryManagementSystem()
        self.item1 = InventoryItem("1", "Laptop", 1000.00, 10)
        self.item2 = InventoryItem("2", "Phone", 500.00, 15)
        
    def test_add_item(self):
        """Test adding a new item to the inventory."""
        self.system.add_item(self.item1)
        self.assertEqual(len(self.system.inventory), 1)
        self.assertIn(self.item1.item_id, self.system.inventory)

    def test_add_existing_item(self):
        """Test adding an existing item, which should update the quantity."""
        self.system.add_item(self.item1)
        initial_quantity = self.system.inventory[self.item1.item_id].quantity
        self.system.add_item(self.item1)
        self.assertEqual(self.system.inventory[self.item1.item_id].quantity, initial_quantity + self.item1.quantity)

    def test_remove_item(self):
        """Test removing an item from the inventory."""
        self.system.add_item(self.item1)
        self.system.remove_item(self.item1.item_id)
        self.assertNotIn(self.item1.item_id, self.system.inventory)

    def test_remove_non_existing_item(self):
        """Test removing an item that doesn't exist in the inventory."""
        result = self.system.remove_item("non_existing_id")
        self.assertFalse(result)

    def test_update_item(self):
        """Test updating an item's information."""
        self.system.add_item(self.item1)
        self.system.update_item(self.item1.item_id, name="Gaming Laptop", price=1200.00, quantity=5)
        updated_item = self.system.inventory[self.item1.item_id]
        self.assertEqual(updated_item.name, "Gaming Laptop")
        self.assertEqual(updated_item.price, 1200.00)
        self.assertEqual(updated_item.quantity, 5)

    def test_update_non_existing_item(self):
        """Test trying to update an item that doesn't exist."""
        result = self.system.update_item("non_existing_id", name="New Item", price=200, quantity=10)
        self.assertFalse(result)

    def test_view_inventory(self):
        """Test viewing the inventory."""
        self.system.add_item(self.item1)
        self.system.add_item(self.item2)
        inventory = self.system.view_inventory()
        self.assertEqual(len(inventory), 2)

    def test_process_sale(self):
        """Test processing a sale."""
        self.system.add_item(self.item1)
        self.system.process_sale(self.item1.item_id, 5)
        self.assertEqual(self.system.inventory[self.item1.item_id].quantity, 5)  # Should reduce quantity by 5

    def test_process_sale_insufficient_stock(self):
        """Test sale when there's insufficient stock."""
        self.system.add_item(self.item1)
        self.system.process_sale(self.item1.item_id, 20)
        self.assertEqual(self.system.inventory[self.item1.item_id].quantity, 10)  # Quantity should remain the same

if __name__ == "__main__":
    unittest.main()
