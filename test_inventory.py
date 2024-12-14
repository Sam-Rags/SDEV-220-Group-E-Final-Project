import unittest
from inventory_system import InventoryManagementSystem, InventoryItem

class TestInventoryManagementSystem(unittest.TestCase):
    
    def setUp(self):
        # Create test items
        self.item1 = InventoryItem("101", "Test Item", 10.00, 5)
        self.item2 = InventoryItem("102", "Another Item", 20.00, 3)
        
        # Create instance of InventoryManagementSystem
        self.system = InventoryManagementSystem()

    def test_add_item(self):
        self.system.add_item(self.item1.item_id, self.item1.name, self.item1.price, self.item1.quantity)  # Pass individual attributes
        self.assertIn(self.item1.item_id, self.system.inventory)

    def test_add_item_existing_id(self):
        self.system.add_item(self.item1.item_id, self.item1.name, self.item1.price, self.item1.quantity)  # First time adding item1
        self.system.add_item(self.item1.item_id, self.item1.name, self.item1.price, self.item1.quantity)  # Adding item1 again, should update quantity
        self.assertEqual(self.system.inventory[self.item1.item_id].quantity, 10)  # quantity should be 10

    def test_process_sale(self):
        self.system.add_item(self.item1.item_id, self.item1.name, self.item1.price, self.item1.quantity)
        self.system.process_sale(self.item1.item_id, 3)  # Process sale for 3 items
        self.assertEqual(self.system.inventory[self.item1.item_id].quantity, 2)  # Remaining quantity should be 2

    def test_process_sale_insufficient_stock(self):
        self.system.add_item(self.item1.item_id, self.item1.name, self.item1.price, self.item1.quantity)
        self.system.process_sale(self.item1.item_id, 10)  # Trying to sell more than available
        self.assertEqual(self.system.inventory[self.item1.item_id].quantity, 5)  # Should still be 5 due to insufficient stock

    def test_remove_item(self):
        self.system.add_item(self.item1.item_id, self.item1.name, self.item1.price, self.item1.quantity)
        self.system.remove_item(self.item1.item_id)
        self.assertNotIn(self.item1.item_id, self.system.inventory)  # Should be removed

    def test_search_items(self):
        self.system.add_item(self.item1.item_id, self.item1.name, self.item1.price, self.item1.quantity)
        self.system.add_item(self.item2.item_id, self.item2.name, self.item2.price, self.item2.quantity)
        result = self.system.search_items("Test")  # Searching for "Test"
        self.assertEqual(len(result), 1)  # Should find 1 item

    def test_update_item(self):
        self.system.add_item(self.item1.item_id, self.item1.name, self.item1.price, self.item1.quantity)
        self.system.update_item(self.item1.item_id, name="Updated Item", price=15.00, quantity=10)
        self.assertEqual(self.system.inventory[self.item1.item_id].name, "Updated Item")
        self.assertEqual(self.system.inventory[self.item1.item_id].price, 15.00)
        self.assertEqual(self.system.inventory[self.item1.item_id].quantity, 10)

if __name__ == "__main__":
    unittest.main()
