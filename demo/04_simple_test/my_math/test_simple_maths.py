import unittest
from .simple_maths import multiply, power, divide


class SimpleMathsTestCase(unittest.TestCase):

    def test_multiply(self):
        """Test that the multiply function works"""
        value = multiply(2, 5)
        self.assertEqual(value, 10)

    def test_power(self):
        """Tests that the power function works"""
        value = power(5, 2)

        self.assertLess(value, 30)
        self.assertGreater(value, 20)

    def test_divide_by_zero(self):
        """Tests that the appropriate exception is raised"""
        self.assertRaises(ZeroDivisionError, divide, 1, 0)
