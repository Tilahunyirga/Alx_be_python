import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(self.calc, 2,3),5)
        self.assertEqual(self.calc.add(self.calc,-1,1),0)
        self.assertEqual(self.calc.add(self.calc, 1, 1), 2)
        self.assertEqual(self.calc.add(self.calc, 1,-5),-4)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(self.calc,5,2),3)
        self.assertEqual(self.calc.subtract(self.calc,5,-2), 7)
        self.assertEqual(self.calc.subtract(self.calc, -5, 2), -7)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(self.calc, 1,1),1)
        self.assertEqual(self.calc.multiply(self.calc, 1, 0), 0)
        self.assertEqual(self.calc.multiply(self.calc, -10, 10), -100)
    def test_division(self):
        self.assertEqual(self.calc.divide(self.calc, 10,5),2)
        self.assertEqual(self.calc.divide(self.calc, -10, 5), -2)
        self.assertEqual(self.calc.divide(self.calc, 5, 10), 0.5)
        self.assertEqual(self.calc.divide(self.calc, 5, 0), None)


