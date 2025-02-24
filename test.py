import unittest
import math
from scientific_calculator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = ScientificCalculator()

    def test_square_root(self):
        self.assertAlmostEqual(self.calculator.square_root(4), 2)
        self.assertAlmostEqual(self.calculator.square_root(9), 3)
        with self.assertRaises(ValueError):
            self.calculator.square_root(-1)

    def test_factorial(self):
        self.assertEqual(self.calculator.factorial(5), 120)
        self.assertEqual(self.calculator.factorial(0), 1)
        with self.assertRaises(ValueError):
            self.calculator.factorial(-3)

    def test_natural_log(self):
        self.assertAlmostEqual(self.calculator.natural_log(math.e), 1)
        with self.assertRaises(ValueError):
            self.calculator.natural_log(0)
        with self.assertRaises(ValueError):
            self.calculator.natural_log(-10)

    def test_power(self):
        self.assertAlmostEqual(self.calculator.power(2, 3), 8)
        self.assertAlmostEqual(self.calculator.power(5, 0), 1)
        self.assertAlmostEqual(self.calculator.power(10, -1), 0.1)

if __name__ == "__main__":
    unittest.main()
