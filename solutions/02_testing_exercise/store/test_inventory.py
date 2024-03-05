import unittest
from unittest.mock import Mock

from .inventory import (Product,
                        Inventory,
                        ProductAlreadyExistsError,
                        NoSuchProductError,
                        NotEnoughQuantityError)

"""
Exercise 2 (Part One)
==========

Objective

Write tests here so that later we can write production code.
"""


class ProductTest(unittest.TestCase):
    """Tests the product class"""
    def test_repr(self):
        """
        Tests the __repr__ method displays the name, price, and quantity

        Note, __repr__ is essentially the toString method for internal use
        """
        p = Product("Juice", 6.99)
        obj_str = p.__repr__()
        expected_str = "<Product 'Juice' @ £6.99 (Qty: 0)>"
        self.assertEqual(obj_str, expected_str)


class InventoryTest(unittest.TestCase):
    def test_inventory_init(self):
        """Test that the inventory is initialised"""
        inv = Inventory()
        self.assertDictEqual(inv._inventory, {})
        self.assertEqual(inv._takings, 0.0)

    def test_add_product_real(self):
        """Tests that a product can be added using a Product"""
        product = Product("Juice", 1.99)
        inv = Inventory()
        inv.add_product(product, 5)
        self.assertEqual(product.quantity, 5)
        self.assertIn(product, inv._inventory.values())

    def test_add_product_mock(self):
        """Test that a product can be added using a Mock"""
        product = Mock(name="Juice")
        inv = Inventory()
        inv.add_product(product, 5)
        self.assertEqual(product.quantity, 5)
        self.assertIn(product, inv._inventory.values())

    def test_total_quantity(self):
        """Test the total item *count* adds up"""
        p1 = Product("A", 0.0)
        p2 = Product("B", 0.0)

        inv = Inventory()
        inv.add_product(p1, 4)
        inv.add_product(p2, 8)

        self.assertEqual(inv.total_items(), 12)

    def test_total_value(self):
        """Test the total item *value* adds up"""
        p1 = Product("A", 1.5)
        p2 = Product("B", 2.25)

        inv = Inventory()
        inv.add_product(p1, 4)
        inv.add_product(p2, 8)

        total_value = (p1.price * p1.quantity) + (p2.price * p2.quantity)

        self.assertEqual(inv.total_value(), total_value)

    def test_add_duplicate(self):
        """Test that adding a product with the same raises ProductAlreadyExistsError"""
        p1 = Product("ProdName", 1.0)
        p2 = Product("ProdName", 2.0)

        inv = Inventory()
        inv.add_product(p1, 1)

        self.assertRaises(ProductAlreadyExistsError, inv.add_product, p2, 2)

    def test_sell_product(self):
        """Test that selling a product increases the inventory takings"""
        product = Product("Thing", 10.0)

        inv = Inventory()
        inv.add_product(product, 10)

        inv.sell_product(product.name, 10)

        self.assertEqual(inv._takings, 100)

    def test_sell_nonexistant_product(self):
        """Test that trying to sell a product that does not exist raises NoSuchProductError"""
        inv = Inventory()
        self.assertRaises(NoSuchProductError, inv.sell_product, "NotThing", 0)

    def test_sell_too_much(self):
        """Test that selling a product increases the inventory takings"""
        product = Product("Thing", 10.0)

        inv = Inventory()
        inv.add_product(product, 10)

        self.assertRaises(NotEnoughQuantityError, inv.sell_product, product.name, 11)


if __name__ == '__main__':
    unittest.main()
