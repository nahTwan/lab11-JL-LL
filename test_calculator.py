import unittest

from calculator import *

# https://github.com/nahTwan/lab11-JL-LL
# Partner 1: Jordan Lawson
# Partner 2: Lucas Leinweber

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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertEqual(divide(0,1), 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(1,2), 0)
        self.assertEqual(logarithm(1,3), 0)
        self.assertEqual(logarithm(1,4), 0)


    def test_log_invalid_base(self): # 1 assertion
        self.assertRaises(ValueError, logarithm, 0,8)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()