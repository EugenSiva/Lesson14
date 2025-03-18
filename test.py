import unittest

from main import Calc

class TestCalculation(unittest.TestCase):
    def test_add_positive(self):
        calc = Calc()
        self.assertEqual(calc.add(1,2),3)

    def test_add_negative(self):
        calc = Calc()
        self.assertEqual(calc.add(-2,-3),-5)

    def test_multiply(self):
        calc = Calc()
        self.assertEqual(calc.multiply(2,3),6)

    def test_divide(self):
        calc = Calc()
        self.assertEqual(calc.divide(8,2),4)

    def test_odvesna(self):
        calc = Calc()
        self.assertEqual(calc.odvesna(5,3),4)

    def test_korene_1(self):
        calc = Calc()
        vysledok = calc.korene(1,3,2)
        print(vysledok)
