# https://github.com/nahTwan/lab11-JL-LL
# Partner 1: Jordon Lawson
# Partner 2: Lucas Leinweber

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(5,2), 7)
        self.assertEqual(add(5,4), 9)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5,4), 1)
        self.assertEqual(subtract(9,4), 5)
        self.assertEqual(subtract(-2,3), -5)
    ######## Partner 1
    def test_multiply(self):
        # 3 assertions
        self.assertEqual(mul(9, 3), 27)
        self.assertEqual(mul(8, 12), 96)
        self.assertEqual(mul(-2, 4), -8)

    def test_divide(self):
        # 3 assertions
        self.assertEqual(div(9, 3), 3)
        self.assertEqual(div(8, 10), 0.8)
        self.assertEqual(div(-10, 2), -5)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertEqual(div(0,1), 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(1,2), 0)
        self.assertEqual(logarithm(1,3), 0)
        self.assertEqual(logarithm(1,4), 0)


    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, logarithm, 0,8)
    
    ######## Partner 1
    def test_log_invalid_argument(self):
            # 1 assertion
        self.assertRaises(ValueError,logarithm,-1, 5)

    def test_hypotenuse(self):
            # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(5, 12), 13.0)
        self.assertEqual(hypotenuse(8, 15), 17.0)

    def test_sqrt(self):
            # 3 assertions
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(25), 5.0)
        self.assertEqual(square_root(100), 10.0)

    # Do not touch this
if __name__ == "__main__":
    unittest.main()
