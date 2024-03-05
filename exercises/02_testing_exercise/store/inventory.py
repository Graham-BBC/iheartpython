"""
Exercise 2 (Part Two)
==========

Objective

Implement the code so that the tests pass
"""

class ProductAlreadyExistsError(Exception):
    pass

class NoSuchProductError(Exception):
    pass

class NotEnoughQuantityError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0

    def __repr__(self):
        return f"<Product '{self.name}' @ £{self.price} (Qty: {self.quantity})>"

class Inventory:
    def __init__(self):
        self._inventory = {}
        self._takings = 0.0

    def __repr__(self):
        return f"<Inventory with {len(self._inventory)} products: {','.join(self._inventory)}>"

    def add_product(self, product, quantity):
        """
        Add a product to the inventory, using product name as key

        :raises: ProductAlreadyExistsError: if a product with the same name already exists

        :param product: The product to add to the inventory
        :param quantity: How many items to place in the inventory
        """
        pass

    def sell_product(self, name, quantity):
        """
        Sell a quantity of a product

        :raises: NoSuchProductError: if the product is not in the inventory
        :raises: NotEnoughQuantityError: if the customer wants more items than exists

        :param name: The product name the customer wants to buy
        :param quantity: How many the customer wants to buy
        """
        pass

    def total_items(self):
        """
        Total number of items in the inventory (sum of quantities)

        :return: The total number of items in stock
        """
        pass

    def total_value(self):
        """
        Total value of stock in the inventory (sum of quantities multiplied by price)

        :return: The total value of all items in stock
        """
        pass

def main():
    p = Product("Peas", 1.29)

    inv = Inventory()
    inv.add_product(p, 10)

    print(inv)
    print(inv.total_items())
    print(inv.total_value())


if __name__ == "__main__":
    main()
