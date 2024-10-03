import unittest
from unittest.mock import Mock

from .inventory import (Product,
                        Inventory,
                        ProductAlreadyExistsError,
                        NoSuchProductError,
                        NotEnoughQuantityError)

# ignore this comment

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
        pass

    def test_add_product_mock(self):
        """Test that a product can be added using a Mock"""
        pass

    def test_total_quantity(self):
        """Test the total item *count* adds up"""
        pass

    def test_total_value(self):
        """Test the total item *value* adds up"""
        pass

    def test_add_duplicate(self):
        """Test that adding a product with the same raises ProductAlreadyExistsError"""
        pass

    def test_sell_product(self):
        """Test that selling a product increases the inventory takings"""
        pass

    def test_sell_nonexistant_product(self):
        """Test that trying to sell a product that does not exist raises NoSuchProductError"""
        pass

    def test_sell_too_much(self):
        """Test that selling a product increases the inventory takings"""
        pass


if __name__ == '__main__':
    unittest.main()
